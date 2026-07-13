/* ============================================================
   Articles Center – Admin Dashboard Logic
   Handles: password gate, CRUD, stats, editor, live preview,
   AI translation placeholder, sitemap/RSS generation
   ============================================================ */

'use strict';

(function () {
  const SITE_URL = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.SITE_URL) || '';
  const ADMIN_PW = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.ADMIN_PASSWORD) || 'admin';
  const JSON_PATH = '/articles/articles.json';

  let articles = [];
  let editingId = null;
  let editorLang = 'en'; // current tab in editor

  const T = {
    totalArticles: 'Total Articles',
    published: 'Published',
    drafts: 'Drafts',
    categories: 'Categories',
    lastPublished: 'Last Published',
    newArticle: '+ New Article',
    edit: 'Edit',
    delete: 'Delete',
    duplicate: 'Duplicate',
    preview: 'Preview',
    saveDraft: 'Save Draft',
    publish: 'Publish',
    cancel: 'Cancel',
    title: 'Title',
    excerpt: 'Excerpt',
    content: 'Content',
    metaTitle: 'Meta Title',
    metaDescription: 'Meta Description',
    keywords: 'SEO Keywords (comma-separated)',
    heroImage: 'Hero Image URL',
    category: 'Category',
    tags: 'Tags (comma-separated)',
    readingTime: 'Reading Time (min)',
    author: 'Author',
    slug: 'Slug (URL)',
    publishDate: 'Publish Date',
    featured: 'Featured',
    translate: '✨ Translate EN → AR',
    translating: 'Translating…',
    translateDone: '✓ Translated!',
    livePreview: 'Live Preview',
    backToDashboard: '← Back to Dashboard',
    confirmDelete: 'Delete this article?',
    passwordLabel: 'Administrator Password',
    passwordError: 'Incorrect password',
    enter: 'Enter',
    noArticles: 'No articles yet. Click "New Article" to create one.',
    status: 'Status',
    actions: 'Actions',
    article: 'Article',
    date: 'Date',
    saveSuccess: '✓ Article saved successfully!',
    saveError: '3 files downloaded. Replace them in your project root and push to git.',
    english: '🇺🇸 English',
    arabic: '🇸🇦 العربية',
    gallery: 'Gallery Images (comma-separated URLs)',
    exportJson: 'Export JSON',
    importJson: 'Import JSON'
  };

  /* ── Password Gate ── */
  function initPasswordGate() {
    const screen = document.getElementById('password-screen');
    const dashboard = document.getElementById('dashboard-app');
    const input = document.getElementById('pw-input');
    const btn = document.getElementById('pw-btn');
    const err = document.getElementById('pw-error');

    function tryPassword() {
      if (input.value === ADMIN_PW) {
        sessionStorage.setItem('articles_admin', '1');
        screen.style.display = 'none';
        dashboard.style.display = '';
        initDashboard();
      } else {
        err.style.display = 'block';
        input.value = '';
        input.focus();
      }
    }

    btn.addEventListener('click', tryPassword);
    input.addEventListener('keydown', (e) => { if (e.key === 'Enter') tryPassword(); });

    // Auto-unlock if already authenticated this session
    if (sessionStorage.getItem('articles_admin') === '1') {
      screen.style.display = 'none';
      dashboard.style.display = '';
      initDashboard();
    }
  }

  /* ── Load Articles ── */
  async function loadArticles() {
    try {
      const res = await fetch('../articles/articles.json?v=' + Date.now(), { cache: 'no-store' });
      articles = await res.json();
    } catch (e) {
      console.error('Failed to load articles:', e);
      articles = [];
    }
  }

  /* ── GitHub config ── */
  const GH_REPO = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.GITHUB_REPO) || 'ashrafedes/profileweb-render';
  const GH_BRANCH = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.GITHUB_BRANCH) || 'main';

  /* ── Get GitHub token from config or localStorage ── */
  function getGHToken() {
    const cfgToken = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.GITHUB_TOKEN) || '';
    if (cfgToken) return cfgToken;
    return localStorage.getItem('gh_token') || '';
  }

  /* ── Prompt for GitHub token if not set ── */
  function ensureGHToken() {
    let token = getGHToken();
    if (token) return token;
    token = prompt('Enter your GitHub Personal Access Token (repo scope):\n\nGet one at: https://github.com/settings/tokens\nClick "Generate new token (classic)" and check "repo" scope');
    if (token && token.trim()) {
      token = token.trim();
      localStorage.setItem('gh_token', token);
    }
    return token || '';
  }

  /* ── Base64 encode UTF-8 string reliably ── */
  function toBase64(str) {
    // Use chunked approach for reliability with large strings (e.g. articles.json with embedded images)
    const bytes = new TextEncoder().encode(str);
    const CHUNK = 8192;
    let binary = '';
    for (let i = 0; i < bytes.length; i += CHUNK) {
      binary += String.fromCharCode.apply(null, bytes.subarray(i, i + CHUNK));
    }
    return btoa(binary);
  }

  /* ── Save Articles — commits to GitHub via Contents API ── */
  async function saveArticles() {
    renderStats();
    renderTable();

    const GH_TOKEN = ensureGHToken();
    if (!GH_TOKEN) {
      showSaveBanner(true, '⚠ No GitHub token. Click Publish again and enter your token when prompted.');
      return;
    }

    // Fetch fresh articles.json from GitHub to avoid overwriting new articles added elsewhere
    showSaveBanner(true, '⏳ Fetching latest articles from GitHub…');
    try {
      const freshRes = await fetch(`https://raw.githubusercontent.com/${GH_REPO}/${GH_BRANCH}/articles/articles.json?v=${Date.now()}`, { cache: 'no-store' });
      if (freshRes.ok) {
        const freshArticles = await freshRes.json();
        const currentSlug = getVal('ed-slug');
        if (currentSlug) {
          const currentLocal = articles.find(a => a.slug === currentSlug);
          const freshIdx = freshArticles.findIndex(a => a.slug === currentSlug);
          if (currentLocal && freshIdx >= 0) {
            freshArticles[freshIdx] = currentLocal;
          } else if (currentLocal) {
            freshArticles.push(currentLocal);
          }
        }
        articles = freshArticles;
        renderStats();
        renderTable();
      }
    } catch (e) {
      console.warn('Could not fetch fresh articles from GitHub, using locally cached list:', e);
    }

    const jsonContent = JSON.stringify(articles, null, 2);
    const sitemapContent = buildSitemapXML();
    const rssContent = buildRSSXML();

    // Warn if JSON is very large (base64 images inflate it significantly)
    const jsonSizeKB = Math.round(new TextEncoder().encode(jsonContent).length / 1024);
    if (jsonSizeKB > 2048) {
      const proceed = confirm(`⚠ articles.json is ${jsonSizeKB}KB — this is very large due to embedded base64 images.\n\nLarge files may fail to push to GitHub. Consider using external image URLs instead of uploading images directly.\n\nProceed anyway?`);
      if (!proceed) return;
    }

    showSaveBanner(true, '⏳ Pushing to GitHub…');

    const now = new Date().toISOString().split('T')[0];
    const files = [
      { path: 'articles/articles.json', content: jsonContent },
      { path: 'sitemap.xml', content: sitemapContent },
      { path: 'rss.xml', content: rssContent }
    ];

    try {
      // Get latest commit on branch
      const branchRes = await fetch(`https://api.github.com/repos/${GH_REPO}/branches/${GH_BRANCH}`, {
        headers: { 'Authorization': `Bearer ${GH_TOKEN}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28' }
      });
      if (!branchRes.ok) throw new Error('Cannot read branch: ' + branchRes.statusText);
      const branchData = await branchRes.json();
      const latestCommitSha = branchData.commit.sha;
      const baseTreeSha = branchData.commit.commit.tree.sha;

      // Create blobs for all files
      const treeItems = [];
      for (const f of files) {
        const blobRes = await fetch(`https://api.github.com/repos/${GH_REPO}/git/blobs`, {
          method: 'POST',
          headers: { 'Authorization': `Bearer ${GH_TOKEN}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json' },
          body: JSON.stringify({ content: toBase64(f.content), encoding: 'base64' })
        });
        if (!blobRes.ok) throw new Error(`Failed to create blob for ${f.path}: ${blobRes.statusText}`);
        const blobData = await blobRes.json();
        treeItems.push({ path: f.path, mode: '100644', type: 'blob', sha: blobData.sha });
      }

      // Create tree with all 3 files
      const treeRes = await fetch(`https://api.github.com/repos/${GH_REPO}/git/trees`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${GH_TOKEN}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json' },
        body: JSON.stringify({ base_tree: baseTreeSha, tree: treeItems })
      });
      if (!treeRes.ok) throw new Error('Failed to create tree: ' + treeRes.statusText);
      const treeData = await treeRes.json();

      // Create commit
      const commitRes = await fetch(`https://api.github.com/repos/${GH_REPO}/git/commits`, {
        method: 'POST',
        headers: { 'Authorization': `Bearer ${GH_TOKEN}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json' },
        body: JSON.stringify({
          message: `Dashboard: update articles, sitemap, rss (${now})`,
          tree: treeData.sha,
          parents: [latestCommitSha]
        })
      });
      if (!commitRes.ok) throw new Error('Failed to create commit: ' + commitRes.statusText);
      const commitData = await commitRes.json();

      // Update branch ref
      const refRes = await fetch(`https://api.github.com/repos/${GH_REPO}/git/refs/heads/${GH_BRANCH}`, {
        method: 'PATCH',
        headers: { 'Authorization': `Bearer ${GH_TOKEN}`, 'Accept': 'application/vnd.github+json', 'X-GitHub-Api-Version': '2022-11-28', 'Content-Type': 'application/json' },
        body: JSON.stringify({ sha: commitData.sha, force: true })
      });
      if (!refRes.ok) {
        const refErr = await refRes.json().catch(() => ({}));
        throw new Error(refErr.message || 'Failed to update branch: ' + refRes.statusText);
      }

      showSaveBanner(true, '✓ Pushed to GitHub!<br><span style="font-weight:400;font-size:0.8rem;opacity:0.9;">articles.json, sitemap.xml, rss.xml committed. Arabic content is saved. If the live site still shows English after 5 minutes, log in to Render and click “Manual Deploy” because Render is not auto-deploying the latest commits.</span>');
      // Reload articles from server after a short delay to confirm changes
      setTimeout(() => loadArticles().then(() => { renderStats(); renderTable(); }), 3000);
    } catch (e) {
      console.error('GitHub commit failed:', e);
      showSaveBanner(true, '⚠ GitHub push failed: ' + e.message);
    }
  }

  /* ── Save banner (non-blocking) ── */
  function showSaveBanner(direct, msg) {
    let banner = document.getElementById('save-banner');
    if (!banner) {
      banner = document.createElement('div');
      banner.id = 'save-banner';
      banner.style.cssText = 'position:fixed;top:1rem;right:1rem;z-index:9999;padding:1rem 1.5rem;border-radius:8px;box-shadow:0 4px 12px rgba(0,0,0,0.3);font-size:0.9rem;font-weight:600;max-width:380px;color:#fff;';
      document.body.appendChild(banner);
    }
    banner.style.background = '#1a7f37';
    if (msg) {
      banner.innerHTML = msg;
    } else if (direct) {
      banner.innerHTML = '✓ Saved directly to disk!<br><span style="font-weight:400;font-size:0.8rem;opacity:0.9;">articles.json, sitemap.xml, rss.xml updated. Push to git when ready.</span>';
    } else {
      banner.innerHTML = '✓ Saved! 3 files downloaded:<br>1. articles.json<br>2. sitemap.xml<br>3. rss.xml<br><span style="font-weight:400;font-size:0.8rem;opacity:0.9;">Replace them in your project & push to git.</span>';
    }
    banner.style.display = 'block';
    setTimeout(() => { banner.style.display = 'none'; }, 8000);
  }

  /* ── Dashboard Init ── */
  async function initDashboard() {
    await loadArticles();
    renderStats();
    renderTable();

    document.getElementById('btn-new-article').addEventListener('click', () => openEditor(null));
    document.getElementById('btn-export').addEventListener('click', exportJSON);
    document.getElementById('btn-import').addEventListener('click', importJSON);
  }

  /* ── Render Stats ── */
  function renderStats() {
    const published = articles.filter(a => !a.draft);
    const drafts = articles.filter(a => a.draft);
    const cats = new Set(articles.map(a => a.category));
    const lastPub = published.length > 0
      ? published.map(a => a.publishDate).sort().reverse()[0] : '—';

    document.getElementById('stat-total').textContent = articles.length;
    document.getElementById('stat-published').textContent = published.length;
    document.getElementById('stat-drafts').textContent = drafts.length;
    document.getElementById('stat-categories').textContent = cats.size;
    document.getElementById('stat-last-pub').textContent = lastPub;
  }

  /* ── Sorting ── */
  let sortDirection = -1; // -1 = newest first, 1 = oldest first
  function getSortedArticles() {
    return [...articles].sort((a, b) => {
      const da = new Date(a.publishDate || '1970-01-01').getTime();
      const db = new Date(b.publishDate || '1970-01-01').getTime();
      return sortDirection === -1 ? db - da : da - db;
    });
  }

  function toggleSort() {
    sortDirection = sortDirection === -1 ? 1 : -1;
    const btn = document.getElementById('btn-sort-date');
    if (btn) btn.textContent = sortDirection === -1 ? 'Date ↓' : 'Date ↑';
    renderTable();
  }

  /* ── Render Table ── */
  function renderTable() {
    const tbody = document.getElementById('articles-tbody');
    const sorted = getSortedArticles();
    if (sorted.length === 0) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:2rem;color:#8b949e;">${T.noArticles}</td></tr>`;
      return;
    }

    tbody.innerHTML = sorted.map(a => `
      <tr>
        <td style="font-weight:600;color:#e6edf3;">${(a.en && a.en.title) || 'Untitled'}</td>
        <td>${a.category}</td>
        <td>${a.publishDate || '—'}</td>
        <td>${a.readingTime || '—'} min</td>
        <td><span class="status-badge ${a.draft ? 'status-draft' : 'status-published'}">${a.draft ? 'Draft' : 'Published'}</span></td>
        <td>
          <button class="dash-btn" onclick="ArticlesDashboard.edit(${a.id})">${T.edit}</button>
          <button class="dash-btn" onclick="ArticlesDashboard.preview(${a.id})">${T.preview}</button>
          <button class="dash-btn" onclick="ArticlesDashboard.duplicate(${a.id})">${T.duplicate}</button>
          <button class="dash-btn dash-btn-danger" onclick="ArticlesDashboard.remove(${a.id})">${T.delete}</button>
        </td>
      </tr>`).join('');
  }

  /* ── Open Editor ── */
  function openEditor(article) {
    editingId = article ? article.id : null;
    editorLang = 'en';

    const overlay = document.getElementById('editor-overlay');
    overlay.style.display = 'block';

    const a = article || {
      id: getNextId(),
      slug: '',
      category: '',
      author: ARTICLES_CONFIG.DEFAULT_AUTHOR || 'Ashraf Ibrahim El Desoky',
      heroImage: '',
      publishDate: new Date().toISOString().split('T')[0],
      updatedDate: new Date().toISOString().split('T')[0],
      readingTime: 5,
      featured: false,
      draft: true,
      tags: [],
      en: { title: '', excerpt: '', content: '', metaTitle: '', metaDescription: '', keywords: [] },
      ar: { title: '', excerpt: '', content: '', metaTitle: '', metaDescription: '', keywords: [] }
    };

    // Fill common fields
    setVal('ed-slug', a.slug);
    setVal('ed-category', a.category);
    setVal('ed-author', a.author);
    setVal('ed-hero-image', a.heroImage);
    setVal('ed-publish-date', a.publishDate);
    setVal('ed-reading-time', a.readingTime);
    document.getElementById('ed-featured').checked = a.featured;
    document.getElementById('ed-draft').checked = a.draft;
    setVal('ed-tags', (a.tags || []).join(', '));

    // Show hero preview if image exists
    showHeroPreview(a.heroImage);

    // Fill EN fields
    fillLangFields('en', a.en || {});
    // Fill AR fields
    fillLangFields('ar', a.ar || {});

    updatePreview();
    overlay.scrollTop = 0;
  }

  function fillLangFields(lang, d) {
    setVal(`ed-${lang}-title`, d.title || '');
    setVal(`ed-${lang}-excerpt`, d.excerpt || '');
    setVal(`ed-${lang}-content`, d.content || '');
    setVal(`ed-${lang}-meta-title`, d.metaTitle || '');
    setVal(`ed-${lang}-meta-desc`, d.metaDescription || '');
    setVal(`ed-${lang}-keywords`, (d.keywords || []).join(', '));
  }

  function getLangFields(lang) {
    return {
      title: getVal(`ed-${lang}-title`),
      excerpt: getVal(`ed-${lang}-excerpt`),
      content: getVal(`ed-${lang}-content`),
      metaTitle: getVal(`ed-${lang}-meta-title`),
      metaDescription: getVal(`ed-${lang}-meta-desc`),
      keywords: getVal(`ed-${lang}-keywords`).split(',').map(s => s.trim()).filter(Boolean)
    };
  }

  function setVal(id, val) {
    const el = document.getElementById(id);
    if (el) el.value = val;
  }
  function getVal(id) {
    const el = document.getElementById(id);
    return el ? el.value.trim() : '';
  }

  function getNextId() {
    return articles.length > 0 ? Math.max(...articles.map(a => a.id)) + 1 : 1;
  }

  /* ── Save Article ── */
  async function saveArticle(publish) {
    const slug = getVal('ed-slug') || slugify(getVal('ed-en-title'));
    const article = {
      id: editingId || getNextId(),
      slug: slug,
      category: getVal('ed-category'),
      author: getVal('ed-author'),
      heroImage: getVal('ed-hero-image'),
      publishDate: getVal('ed-publish-date'),
      updatedDate: new Date().toISOString().split('T')[0],
      readingTime: parseInt(getVal('ed-reading-time')) || 5,
      featured: document.getElementById('ed-featured').checked,
      draft: publish ? false : document.getElementById('ed-draft').checked,
      tags: getVal('ed-tags').split(',').map(s => s.trim()).filter(Boolean),
      en: getLangFields('en'),
      ar: getLangFields('ar')
    };

    if (editingId) {
      const idx = articles.findIndex(a => a.id === editingId);
      if (idx >= 0) articles[idx] = article;
    } else {
      articles.push(article);
    }

    await saveArticles();
    closeEditor();
  }

  /* ── Close Editor ── */
  function closeEditor() {
    document.getElementById('editor-overlay').style.display = 'none';
    editingId = null;
  }

  /* ── Edit / Delete / Duplicate / Preview ── */
  function editArticle(id) {
    const a = articles.find(x => x.id === id);
    if (a) openEditor(JSON.parse(JSON.stringify(a)));
  }

  function deleteArticle(id) {
    if (!confirm(T.confirmDelete)) return;
    articles = articles.filter(a => a.id !== id);
    saveArticles();
  }

  function duplicateArticle(id) {
    const a = articles.find(x => x.id === id);
    if (!a) return;
    const copy = JSON.parse(JSON.stringify(a));
    copy.id = getNextId();
    copy.slug = a.slug + '-copy';
    copy.en.title = (a.en.title || '') + ' (Copy)';
    copy.draft = true;
    articles.push(copy);
    saveArticles();
  }

  function previewArticle(id) {
    const a = articles.find(x => x.id === id);
    if (a) window.open(`${SITE_URL}/en/articles/${a.slug}.html`, '_blank');
  }

  /* ── Editor Tab Switching ── */
  function switchEditorTab(lang) {
    editorLang = lang;
    document.querySelectorAll('.editor-tab').forEach(t => t.classList.remove('active'));
    document.querySelector(`.editor-tab[data-lang="${lang}"]`).classList.add('active');

    document.querySelectorAll('.editor-lang-panel').forEach(p => p.style.display = 'none');
    document.getElementById(`editor-panel-${lang}`).style.display = '';

    // RTL for Arabic
    const preview = document.getElementById('editor-preview-content');
    if (lang === 'ar') {
      preview.setAttribute('dir', 'rtl');
      preview.style.fontFamily = "'Cairo', 'Segoe UI', sans-serif";
    } else {
      preview.setAttribute('dir', 'ltr');
      preview.style.fontFamily = "'Inter', 'Segoe UI', sans-serif";
    }

    updatePreview();
  }

  /* ── Live Preview ── */
  function updatePreview() {
    const d = getLangFields(editorLang);
    const preview = document.getElementById('editor-preview-content');
    if (!preview) return;

    let html = '';
    if (d.title) html += `<h2>${d.title}</h2>`;
    if (d.excerpt) html += `<p style="color:#8b949e;font-style:italic;">${d.excerpt}</p>`;
    if (d.content) {
      // Reuse simple markdown rendering
      html += renderMarkdownSimple(d.content);
    }
    preview.innerHTML = html || `<p style="color:#484f58;">${T.livePreview}…</p>`;
  }

  function renderMarkdownSimple(md) {
    let html = md;
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (m, l, c) => `<pre><code>${c.trim()}</code></pre>`);
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>');
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');
    // Images — must be before links
    html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" style="max-width:100%;height:auto;border-radius:8px;margin:1rem 0;" loading="lazy">');
    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');
    html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>\n?)+/g, (m) => '<ul>' + m + '</ul>');
    html = html.split('\n').map(line => {
      const t = line.trim();
      if (!t) return '';
      if (/^<(h2|h3|ul|pre|blockquote|img)/.test(t)) return t;
      return '<p>' + t + '</p>';
    }).join('\n');
    return html;
  }

  /* ── AI Translation Placeholder ── */
  async function translateToArabic() {
    const btn = document.getElementById('btn-translate');
    btn.textContent = T.translating;
    btn.disabled = true;

    const enData = getLangFields('en');

    try {
      // ── Placeholder: Wire up your AI translation provider here ──
      // Example integration points:
      // 1. OpenRouter / OpenAI API: POST to your endpoint with the English text
      // 2. Google Translate API
      // 3. DeepL API
      // 4. Azure Translator
      //
      // For now, this function copies the English content as a starting point
      // so you can manually edit the Arabic version after.
      //
      // To integrate, replace the section below with your API call:
      //
      // const res = await fetch(ARTICLES_CONFIG.AI_TRANSLATE_ENDPOINT, {
      //   method: 'POST',
      //   headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer YOUR_KEY' },
      //   body: JSON.stringify({ text: enData, target_lang: 'ar' })
      // });
      // const translated = await res.json();

      const translated = await translateArticleToArabic(enData);

      // Populate Arabic fields
      setVal('ed-ar-title', translated.title || enData.title);
      setVal('ed-ar-excerpt', translated.excerpt || enData.excerpt);
      setVal('ed-ar-content', translated.content || enData.content);
      setVal('ed-ar-meta-title', translated.metaTitle || enData.metaTitle);
      setVal('ed-ar-meta-desc', translated.metaDescription || enData.metaDescription);
      setVal('ed-ar-keywords', (translated.keywords || enData.keywords).join(', '));

      btn.textContent = T.translateDone;
      setTimeout(() => { btn.textContent = T.translate; btn.disabled = false; }, 2000);

      // Switch to Arabic tab to review
      switchEditorTab('ar');
    } catch (e) {
      console.error('Translation error:', e);
      btn.textContent = 'Error — check console';
      btn.disabled = false;
    }
  }

  /* ── Translate full article using OpenRouter AI in a single call ── */
  function getOpenRouterKey() {
    // Reuse the same key as the chatbot (base64 to match chatbot.js)
    try {
      const _k = atob('c2stb3ItdjEtMGQwMWE4NGMyZmM2N2U4NmViZmIwMDc5NGI0ZmNiMjFlNTRhMmY1YmI0NTZmNDcwMDYxZTQxYTFiNzdmNTQ5Yw==');
      if (_k) return _k;
    } catch (e) {}

    // Backwards-compatible fallbacks
    let key = (typeof window !== 'undefined' && window.CHATBOT_API_KEY) || '';
    if (key) return key;
    key = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.OPENROUTER_API_KEY) || '';
    if (key) return key;
    return localStorage.getItem('openrouter_key') || '';
  }

  async function translateWithMyMemory(text) {
    if (!text || !text.trim()) return '';
    const encoded = encodeURIComponent(text);
    const res = await fetch(`https://api.mymemory.translated.net/get?q=${encoded}&langpair=en|ar`, { mode: 'cors' });
    if (!res.ok) throw new Error(`MyMemory HTTP ${res.status}`);
    const data = await res.json();
    if (data && data.responseData && data.responseData.translatedText) {
      return data.responseData.translatedText;
    }
    throw new Error('MyMemory returned empty translation');
  }

  async function translateArticleToArabic(enData) {
    const key = getOpenRouterKey();

    // Try OpenRouter first if we have a key
    if (key) {
      try {
        const systemPrompt = `You are a professional translator. Translate the provided English article into fluent, natural Arabic. Preserve Markdown formatting. Return ONLY a valid JSON object with these exact keys: title, excerpt, content, metaTitle, metaDescription, keywords (array). Do not wrap the JSON in markdown code blocks.`;
        const userPrompt = JSON.stringify({
          title: enData.title,
          excerpt: enData.excerpt,
          content: enData.content,
          metaTitle: enData.metaTitle || enData.title,
          metaDescription: enData.metaDescription || enData.excerpt,
          keywords: enData.keywords || []
        });

        const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${key}`,
            'HTTP-Referer': (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.SITE_URL) || location.origin,
            'X-Title': 'Articles Dashboard Translation'
          },
          body: JSON.stringify({
            model: 'meta-llama/llama-3.3-70b-instruct:free',
            messages: [
              { role: 'system', content: systemPrompt },
              { role: 'user', content: userPrompt }
            ]
          })
        });

        if (res.ok) {
          const data = await res.json();
          const raw = data.choices && data.choices[0] && data.choices[0].message && data.choices[0].message.content;
          if (raw) {
            const cleaned = raw.replace(/^```json\s*/, '').replace(/\s*```$/, '').trim();
            const translated = JSON.parse(cleaned);
            return {
              title: translated.title || enData.title,
              excerpt: translated.excerpt || enData.excerpt,
              content: translated.content || enData.content,
              metaTitle: translated.metaTitle || enData.metaTitle || enData.title,
              metaDescription: translated.metaDescription || enData.metaDescription || enData.excerpt,
              keywords: Array.isArray(translated.keywords) ? translated.keywords : enData.keywords
            };
          }
        }
      } catch (e) {
        console.warn('OpenRouter failed, falling back to MyMemory:', e.message);
      }
    }

    // Fallback: MyMemory field by field, then English copy
    const tryMem = async (text) => { try { return await translateWithMyMemory(text); } catch (e) { return text; } };
    return {
      title: await tryMem(enData.title),
      excerpt: await tryMem(enData.excerpt),
      content: await tryMem(enData.content),
      metaTitle: await tryMem(enData.metaTitle || enData.title),
      metaDescription: await tryMem(enData.metaDescription || enData.excerpt),
      keywords: await Promise.all((enData.keywords || []).map(k => tryMem(k)))
    };
  }

  /* ── Slugify ── */
  function slugify(text) {
    return text.toLowerCase()
      .replace(/[^a-z0-9 -]/g, '')
      .replace(/\s+/g, '-')
      .replace(/-+/g, '-')
      .trim();
  }

  /* ── Export / Import JSON ── */
  function exportJSON() {
    const blob = new Blob([JSON.stringify(articles, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'articles.json';
    a.click();
    URL.revokeObjectURL(url);
  }

  function importJSON() {
    const input = document.createElement('input');
    input.type = 'file';
    input.accept = '.json';
    input.addEventListener('change', (e) => {
      const file = e.target.files[0];
      if (!file) return;
      const reader = new FileReader();
      reader.onload = (ev) => {
        try {
          articles = JSON.parse(ev.target.result);
          saveArticles();
        } catch (err) {
          alert('Invalid JSON file');
        }
      };
      reader.readAsText(file);
    });
    input.click();
  }

  /* ── Build Sitemap XML (returns string) ── */
  function buildSitemapXML() {
    const today = new Date().toISOString().split('T')[0];
    const PAGES = [
      { loc: SITE_URL + '/', lastmod: today, changefreq: 'weekly', priority: '1.0' },
      { loc: SITE_URL + '/en.html', lastmod: today, changefreq: 'weekly', priority: '0.9' },
      { loc: SITE_URL + '/about.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/career.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/featured-projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/skills.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/achievements.html', lastmod: today, changefreq: 'monthly', priority: '0.90' },
      { loc: SITE_URL + '/certifications.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/education.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/awards.html', lastmod: today, changefreq: 'yearly', priority: '0.85' },
      { loc: SITE_URL + '/companies.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/pmo.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/telecommunications.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/project-controls.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/digital-transformation.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/leadership.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/software.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/contact.html', lastmod: today, changefreq: 'yearly', priority: '0.80' },
      { loc: SITE_URL + '/downloads.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/search.html', lastmod: today, changefreq: 'monthly', priority: '0.70' },
      { loc: SITE_URL + '/404.html', lastmod: today, changefreq: 'yearly', priority: '0.30' },
      // Arabic pages
      { loc: SITE_URL + '/ar/', lastmod: today, changefreq: 'weekly', priority: '1.0' },
      { loc: SITE_URL + '/ar/about.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/ar/career.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/ar/featured-projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/ar/projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/ar/skills.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/ar/achievements.html', lastmod: today, changefreq: 'monthly', priority: '0.90' },
      { loc: SITE_URL + '/ar/certifications.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/ar/education.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/ar/awards.html', lastmod: today, changefreq: 'yearly', priority: '0.85' },
      { loc: SITE_URL + '/ar/companies.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/pmo.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/telecommunications.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/project-controls.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/digital-transformation.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/leadership.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/ar/software.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/ar/contact.html', lastmod: today, changefreq: 'yearly', priority: '0.80' },
      { loc: SITE_URL + '/ar/downloads.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/ar/search.html', lastmod: today, changefreq: 'monthly', priority: '0.70' },
      // English pages
      { loc: SITE_URL + '/en/', lastmod: today, changefreq: 'weekly', priority: '1.0' },
      { loc: SITE_URL + '/en/about.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/en/career.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/en/featured-projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/en/projects.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/en/skills.html', lastmod: today, changefreq: 'monthly', priority: '0.95' },
      { loc: SITE_URL + '/en/achievements.html', lastmod: today, changefreq: 'monthly', priority: '0.90' },
      { loc: SITE_URL + '/en/certifications.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/en/education.html', lastmod: today, changefreq: 'yearly', priority: '0.90' },
      { loc: SITE_URL + '/en/awards.html', lastmod: today, changefreq: 'yearly', priority: '0.85' },
      { loc: SITE_URL + '/en/companies.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/pmo.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/telecommunications.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/project-controls.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/digital-transformation.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/leadership.html', lastmod: today, changefreq: 'monthly', priority: '0.85' },
      { loc: SITE_URL + '/en/software.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/en/contact.html', lastmod: today, changefreq: 'yearly', priority: '0.80' },
      { loc: SITE_URL + '/en/downloads.html', lastmod: today, changefreq: 'monthly', priority: '0.80' },
      { loc: SITE_URL + '/en/search.html', lastmod: today, changefreq: 'monthly', priority: '0.70' },
      // Articles center pages
      { loc: SITE_URL + '/articles/', lastmod: today, changefreq: 'weekly', priority: '0.80' },
      { loc: SITE_URL + '/en/articles/', lastmod: today, changefreq: 'weekly', priority: '0.80' },
      { loc: SITE_URL + '/ar/articles/', lastmod: today, changefreq: 'weekly', priority: '0.80' }
    ];

    let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n';

    // Static pages
    PAGES.forEach(p => {
      xml += `  <url><loc>${p.loc}</loc><lastmod>${p.lastmod}</lastmod><changefreq>${p.changefreq}</changefreq><priority>${p.priority}</priority></url>\n`;
    });

    // Dynamic article pages (EN + AR + root)
    articles.filter(a => !a.draft).forEach(a => {
      const aDate = a.updatedDate || a.publishDate;
      xml += `  <url><loc>${SITE_URL}/articles/${a.slug}.html</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.70</priority></url>\n`;
      xml += `  <url><loc>${SITE_URL}/en/articles/${a.slug}.html</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>\n`;
      xml += `  <url><loc>${SITE_URL}/ar/articles/${a.slug}.html</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>\n`;
    });

    xml += '</urlset>';
    return xml;
  }

  /* ── Build RSS XML (returns string) ── */
  function buildRSSXML() {
    const today = new Date().toISOString();
    let xml = '<?xml version="1.0" encoding="UTF-8"?>\n';
    xml += '<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">\n';
    xml += '  <channel>\n';
    xml += `    <title>Ashraf El Desoky – Articles</title>\n`;
    xml += `    <link>${SITE_URL}/articles/</link>\n`;
    xml += `    <description>Articles and insights on project management, telecommunications, and digital transformation</description>\n`;
    xml += `    <language>en-us</language>\n`;
    xml += `    <lastBuildDate>${today}</lastBuildDate>\n`;

    articles.filter(a => !a.draft).forEach(a => {
      const d = a.en || {};
      xml += '    <item>\n';
      xml += `      <title>${d.title || ''}</title>\n`;
      xml += `      <link>${SITE_URL}/en/articles/${a.slug}.html</link>\n`;
      xml += `      <description>${d.excerpt || ''}</description>\n`;
      xml += `      <author>${a.author || ''}</author>\n`;
      xml += `      <pubDate>${new Date(a.publishDate).toUTCString()}</pubDate>\n`;
      xml += `      <guid>${SITE_URL}/en/articles/${a.slug}.html</guid>\n`;
      xml += '    </item>\n';
    });

    xml += '  </channel>\n</rss>';
    return xml;
  }

  function downloadFile(content, filename, type) {
    const blob = new Blob([content], { type: type });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = filename;
    a.click();
    URL.revokeObjectURL(url);
  }

  /* ── Editor Toolbar (simple formatting) ── */
  function execFormat(command, value) {
    const textarea = document.getElementById(`ed-${editorLang}-content`);
    if (!textarea) return;
    const start = textarea.selectionStart;
    const end = textarea.selectionEnd;
    const selected = textarea.value.substring(start, end);
    let replacement = selected;

    switch (command) {
      case 'bold': replacement = `**${selected || 'text'}**`; break;
      case 'italic': replacement = `*${selected || 'text'}*`; break;
      case 'h2': replacement = `## ${selected || 'Heading'}`; break;
      case 'h3': replacement = `### ${selected || 'Heading'}`; break;
      case 'code': replacement = `\`${selected || 'code'}\``; break;
      case 'quote': replacement = `> ${selected || 'quote'}`; break;
      case 'list': replacement = `- ${selected || 'item'}`; break;
      case 'link': replacement = `[${selected || 'text'}](url)`; break;
      case 'image':
        triggerContentImageUpload(editorLang);
        return;
    }

    textarea.value = textarea.value.substring(0, start) + replacement + textarea.value.substring(end);
    textarea.focus();
    textarea.setSelectionRange(start, start + replacement.length);
    updatePreview();
  }

  /* ── Image Upload (compresses then converts to base64 data URI) ── */
  function compressImage(file, maxWidth, quality) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => {
        const img = new Image();
        img.onload = () => {
          const canvas = document.createElement('canvas');
          let w = img.width;
          let h = img.height;
          if (w > maxWidth) {
            h = Math.round(h * (maxWidth / w));
            w = maxWidth;
          }
          canvas.width = w;
          canvas.height = h;
          const ctx = canvas.getContext('2d');
          ctx.drawImage(img, 0, 0, w, h);
          const dataUrl = canvas.toDataURL('image/webp', quality);
          resolve(dataUrl);
        };
        img.onerror = reject;
        img.src = reader.result;
      };
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  function fileToBase64(file) {
    return new Promise((resolve, reject) => {
      const reader = new FileReader();
      reader.onload = () => resolve(reader.result);
      reader.onerror = reject;
      reader.readAsDataURL(file);
    });
  }

  function showHeroPreview(dataUrl) {
    const el = document.getElementById('hero-preview');
    if (!el) return;
    if (!dataUrl) { el.innerHTML = ''; return; }
    el.innerHTML = `<img src="${dataUrl}" style="max-width:200px;max-height:120px;border-radius:6px;object-fit:cover;border:1px solid #30363d;">`;
  }

  function triggerContentImageUpload(lang) {
    const input = document.getElementById(`content-file-input-${lang}`);
    if (!input) return;
    input.value = '';
    input.click();
  }

  async function handleContentImage(file, lang) {
    if (!file || !file.type.startsWith('image/')) return;
    if (file.size > 5 * 1024 * 1024) {
      alert('Image too large. Max 5MB for inline images.');
      return;
    }
    const dataUrl = await compressImage(file, 1000, 0.75);
    const textarea = document.getElementById(`ed-${lang}-content`);
    if (!textarea) return;
    const start = textarea.selectionStart;
    const alt = file.name.replace(/\.[^.]+$/, '').replace(/[-_]/g, ' ');
    const md = `\n![${alt}](${dataUrl})\n`;
    textarea.value = textarea.value.substring(0, start) + md + textarea.value.substring(textarea.selectionEnd);
    textarea.focus();
    textarea.setSelectionRange(start, start + md.length);
    updatePreview();
  }

  async function handleHeroImage(file) {
    if (!file || !file.type.startsWith('image/')) return;
    if (file.size > 10 * 1024 * 1024) {
      alert('Image too large. Max 10MB for hero images.');
      return;
    }

    const GH_TOKEN = getGHToken();
    if (!GH_TOKEN) {
      alert('No GitHub token found. Please publish an article first to set your token, then try uploading again.');
      return;
    }

    // Show uploading state
    const btnUpload = document.getElementById('btn-upload-hero');
    const origText = btnUpload ? btnUpload.textContent : '';
    if (btnUpload) { btnUpload.textContent = '⏳ Uploading…'; btnUpload.disabled = true; }

    try {
      // Compress to webp
      const dataUrl = await compressImage(file, 1200, 0.82);

      // Convert dataUrl to raw base64 (strip the data:image/webp;base64, prefix)
      const base64Data = dataUrl.split(',')[1];

      // Build a unique filename
      const ext = 'webp';
      const slug = getVal('ed-slug') || ('hero-' + Date.now());
      const filename = slug.replace(/[^a-z0-9\-]/gi, '-').toLowerCase() + '-' + Date.now() + '.' + ext;
      const ghPath = `assets/images/articles/${filename}`;

      // Upload to GitHub via Contents API
      const uploadRes = await fetch(`https://api.github.com/repos/${GH_REPO}/contents/${ghPath}`, {
        method: 'PUT',
        headers: {
          'Authorization': `Bearer ${GH_TOKEN}`,
          'Accept': 'application/vnd.github+json',
          'X-GitHub-Api-Version': '2022-11-28',
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          message: `Upload hero image: ${filename}`,
          content: base64Data
        })
      });

      if (!uploadRes.ok) {
        const err = await uploadRes.json().catch(() => ({}));
        throw new Error(err.message || uploadRes.statusText);
      }

      const uploadData = await uploadRes.json();
      const imagePath = '/' + ghPath;

      // Store the path (not base64) in the input
      const input = document.getElementById('ed-hero-image');
      if (input) input.value = imagePath;
      showHeroPreview(dataUrl); // show local preview while site redeploys

    } catch (e) {
      console.error('Hero image upload failed:', e);
      alert('Image upload failed: ' + e.message + '\n\nYou can manually enter an image URL in the Hero Image field instead.');
    } finally {
      if (btnUpload) { btnUpload.textContent = origText; btnUpload.disabled = false; }
    }
  }

  /* ── Public API ── */
  window.ArticlesDashboard = {
    edit: editArticle,
    remove: deleteArticle,
    duplicate: duplicateArticle,
    preview: previewArticle,
    toggleSort: toggleSort
  };

  /* ── Init ── */
  document.addEventListener('DOMContentLoaded', () => {
    initPasswordGate();

    // Editor buttons
    const btnSave = document.getElementById('btn-save');
    const btnPublish = document.getElementById('btn-publish');
    const btnCancel = document.getElementById('btn-cancel');
    const btnTranslate = document.getElementById('btn-translate');

    if (btnSave) btnSave.addEventListener('click', () => saveArticle(false));
    if (btnPublish) btnPublish.addEventListener('click', () => saveArticle(true));
    if (btnCancel) btnCancel.addEventListener('click', closeEditor);
    if (btnTranslate) btnTranslate.addEventListener('click', translateToArabic);

    // Editor tabs
    document.querySelectorAll('.editor-tab').forEach(tab => {
      tab.addEventListener('click', () => switchEditorTab(tab.dataset.lang));
    });

    // Editor toolbar
    document.querySelectorAll('.editor-toolbar button').forEach(btn => {
      btn.addEventListener('click', () => execFormat(btn.dataset.cmd));
    });

    // Hero image upload
    const btnUploadHero = document.getElementById('btn-upload-hero');
    const heroFileInput = document.getElementById('hero-file-input');
    if (btnUploadHero && heroFileInput) {
      btnUploadHero.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        heroFileInput.value = '';
        heroFileInput.click();
      });
      heroFileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) handleHeroImage(e.target.files[0]);
      });
    }

    // Remove hero image
    const btnRemoveHero = document.getElementById('btn-remove-hero');
    if (btnRemoveHero) {
      btnRemoveHero.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        const input = document.getElementById('ed-hero-image');
        if (input) input.value = '';
        if (heroFileInput) heroFileInput.value = '';
        showHeroPreview('');
      });
    }

    // Content image upload (EN)
    const contentInputEn = document.getElementById('content-file-input-en');
    if (contentInputEn) {
      contentInputEn.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) handleContentImage(e.target.files[0], 'en');
      });
    }

    // Content image upload (AR)
    const contentInputAr = document.getElementById('content-file-input-ar');
    if (contentInputAr) {
      contentInputAr.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) handleContentImage(e.target.files[0], 'ar');
      });
    }

    // Hero preview on manual URL input
    const heroInput = document.getElementById('ed-hero-image');
    if (heroInput) {
      heroInput.addEventListener('input', () => showHeroPreview(heroInput.value));
    }

    // Live preview on input
    document.addEventListener('input', (e) => {
      if (e.target && e.target.id && e.target.id.startsWith('ed-')) {
        updatePreview();
      }
    });

    // Default to EN tab
    switchEditorTab('en');
  });
})();
