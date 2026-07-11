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
    saveError: 'Error saving article. In production, changes save to articles.json on the server.',
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
      const res = await fetch(SITE_URL + JSON_PATH);
      articles = await res.json();
    } catch (e) {
      console.error('Failed to load articles:', e);
      articles = [];
    }
  }

  /* ── Save Articles (client-side; in production, POST to server) ── */
  function saveArticles() {
    // In a static site, we can't write to the server directly.
    // This triggers a download of the updated JSON for manual replacement.
    // In production, wire this up to a serverless function or API endpoint.
    const blob = new Blob([JSON.stringify(articles, null, 2)], { type: 'application/json' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = 'articles.json';
    a.click();
    URL.revokeObjectURL(url);
    alert(T.saveSuccess + '\n\n' + T.saveError);
    renderStats();
    renderTable();
    generateSitemap();
    generateRSS();
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

  /* ── Render Table ── */
  function renderTable() {
    const tbody = document.getElementById('articles-tbody');
    if (articles.length === 0) {
      tbody.innerHTML = `<tr><td colspan="6" style="text-align:center;padding:2rem;color:#8b949e;">${T.noArticles}</td></tr>`;
      return;
    }

    tbody.innerHTML = articles.map(a => `
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
  function saveArticle(publish) {
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

    saveArticles();
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
    if (a) window.open(`article.html?slug=${a.slug}&lang=en`, '_blank');
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
    html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>\n?)+/g, (m) => '<ul>' + m + '</ul>');
    html = html.split('\n').map(line => {
      const t = line.trim();
      if (!t) return '';
      if (/^<(h2|h3|ul|pre|blockquote)/.test(t)) return t;
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

  /* ── Placeholder function for future AI integration ── */
  async function translateArticleToArabic(enData) {
    // ═══════════════════════════════════════════════════
    //  AI TRANSLATION PLACEHOLDER
    //  Replace this function body with your AI provider call.
    //  Expected return: { title, excerpt, content, metaTitle, metaDescription, keywords[] }
    //
    //  Example with OpenRouter:
    //  const res = await fetch('https://openrouter.ai/api/v1/chat/completions', {
    //    method: 'POST',
    //    headers: {
    //      'Authorization': 'Bearer YOUR_KEY',
    //      'Content-Type': 'application/json'
    //    },
    //    body: JSON.stringify({
    //      model: 'meta-llama/llama-3.3-70b-instruct',
    //      messages: [
    //        { role: 'system', content: 'Translate the following article from English to Arabic. Return JSON with keys: title, excerpt, content, metaTitle, metaDescription, keywords.' },
    //        { role: 'user', content: JSON.stringify(enData) }
    //      ]
    //    })
    //  });
    //  const data = await res.json();
    //  return JSON.parse(data.choices[0].message.content);
    // ═══════════════════════════════════════════════════

    // For now: return English as starting point for manual editing
    return {
      title: enData.title,
      excerpt: enData.excerpt,
      content: enData.content,
      metaTitle: enData.metaTitle,
      metaDescription: enData.metaDescription,
      keywords: enData.keywords
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

  /* ── Generate Complete Sitemap (all site pages + articles) ── */
  function generateSitemap() {
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
      xml += `  <url><loc>${SITE_URL}/articles/article.html?slug=${a.slug}</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.70</priority></url>\n`;
      xml += `  <url><loc>${SITE_URL}/en/articles/article.html?slug=${a.slug}</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.70</priority></url>\n`;
      xml += `  <url><loc>${SITE_URL}/ar/articles/article.html?slug=${a.slug}</loc><lastmod>${aDate}</lastmod><changefreq>monthly</changefreq><priority>0.70</priority></url>\n`;
    });

    xml += '</urlset>';

    downloadFile(xml, 'sitemap.xml', 'application/xml');
  }

  /* ── Generate RSS ── */
  function generateRSS() {
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
      xml += `      <link>${SITE_URL}/articles/article.html?slug=${a.slug}</link>\n`;
      xml += `      <description>${d.excerpt || ''}</description>\n`;
      xml += `      <author>${a.author || ''}</author>\n`;
      xml += `      <pubDate>${new Date(a.publishDate).toUTCString()}</pubDate>\n`;
      xml += `      <guid>${SITE_URL}/articles/article.html?slug=${a.slug}</guid>\n`;
      xml += '    </item>\n';
    });

    xml += '  </channel>\n</rss>';
    downloadFile(xml, 'rss.xml', 'application/xml');
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

  /* ── Image Upload (converts to base64 data URI) ── */
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
    if (file.size > 2 * 1024 * 1024) {
      alert('Image too large. Max 2MB for inline images. Use a URL for larger images.');
      return;
    }
    const dataUrl = await fileToBase64(file);
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
    if (file.size > 2 * 1024 * 1024) {
      alert('Image too large. Max 2MB for hero images. Use a URL for larger images.');
      return;
    }
    const dataUrl = await fileToBase64(file);
    const input = document.getElementById('ed-hero-image');
    if (input) input.value = dataUrl;
    showHeroPreview(dataUrl);
  }

  /* ── Public API ── */
  window.ArticlesDashboard = {
    edit: editArticle,
    remove: deleteArticle,
    duplicate: duplicateArticle,
    preview: previewArticle
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
      btnUploadHero.addEventListener('click', () => { heroFileInput.value = ''; heroFileInput.click(); });
      heroFileInput.addEventListener('change', (e) => {
        if (e.target.files && e.target.files[0]) handleHeroImage(e.target.files[0]);
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
