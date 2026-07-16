/* ============================================================
   Articles Center – Single Article Page Logic
   Handles: rendering, TOC, share, related, lang switch, SEO
   ============================================================ */

'use strict';

(function () {
  const SITE_URL = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.SITE_URL) || '';

  function getParam(name) {
    return new URLSearchParams(window.location.search).get(name);
  }

  // Detect subdirectory: /en/articles/ or /ar/articles/ vs root /articles/
  const _path = window.location.pathname;
  const _inSub = /\/(en|ar)\/articles\//.test(_path);
  const _subLang = _path.match(/\/(en|ar)\/articles\//);
  const ASSET_BASE = _inSub ? '../../' : '../';
  let lang = (_subLang && _subLang[1]) || getParam('lang') || 'en';
  if (lang !== 'ar') lang = 'en';
  const IS_ARABIC = lang === 'ar';
  const DIR = IS_ARABIC ? 'rtl' : 'ltr';

  const T = IS_ARABIC ? {
    readingTime: 'دقائق قراءة',
    by: 'بقلم',
    published: 'نُشر',
    updated: 'مُحدّث',
    tableOfContents: 'جدول المحتويات',
    share: 'مشاركة',
    relatedArticles: 'مقالات ذات صلة',
    previousArticle: 'المقال السابق',
    nextArticle: 'المقال التالي',
    backToArticles: '← العودة للمقالات',
    newsletter: 'اشترك في النشرة البريدية',
    newsletterDesc: 'احصل على أحدث المقالات والرؤى مباشرة في بريدك',
    subscribe: 'اشترك',
    emailPlaceholder: 'بريدك الإلكتروني',
    notFound: 'المقال غير موجود',
    notFoundDesc: 'لم نتمكن من العثور على هذا المقال',
    minRead: 'دقيقة قراءة'
  } : {
    readingTime: 'min read',
    by: 'By',
    published: 'Published',
    updated: 'Updated',
    tableOfContents: 'Table of Contents',
    share: 'Share',
    relatedArticles: 'Related Articles',
    previousArticle: 'Previous Article',
    nextArticle: 'Next Article',
    backToArticles: '← Back to Articles',
    newsletter: 'Subscribe to Newsletter',
    newsletterDesc: 'Get the latest articles and insights delivered to your inbox',
    subscribe: 'Subscribe',
    emailPlaceholder: 'Your email',
    notFound: 'Article Not Found',
    notFoundDesc: 'We could not find this article',
    minRead: 'min read'
  };

  /* ── Minimal Markdown Renderer ── */
  function renderMarkdown(md) {
    if (!md) return '';
    let html = md;

    // Code blocks (```...```)
    html = html.replace(/```(\w*)\n([\s\S]*?)```/g, (m, lang, code) =>
      `<pre><code>${escapeHtml(code.trim())}</code></pre>`);

    // Tables
    html = html.replace(/^\|(.+)\|\n\|([-:\s|]+)\|\n((?:\|.+\|\n?)+)/gm, (m, header, sep, body) => {
      const heads = header.split('|').map(h => h.trim()).filter(Boolean);
      const rows = body.trim().split('\n').map(r =>
        r.split('|').map(c => c.trim()).filter(Boolean));
      let t = '<table><thead><tr>' + heads.map(h => `<th>${h}</th>`).join('') + '</tr></thead><tbody>';
      rows.forEach(r => { t += '<tr>' + r.map(c => `<td>${c}</td>`).join('') + '</tr>'; });
      t += '</tbody></table>';
      return t;
    });

    // Headings
    html = html.replace(/^### (.+)$/gm, '<h3>$1</h3>');
    html = html.replace(/^## (.+)$/gm, '<h2>$1</h2>');
    html = html.replace(/^# (.+)$/gm, '<h2>$1</h2>');

    // Blockquotes
    html = html.replace(/^> (.+)$/gm, '<blockquote>$1</blockquote>');

    // Callout boxes
    html = html.replace(/^\[info\] (.+)$/gm, '<div class="callout callout-info"><div class="callout-title">ℹ️ Info</div>$1</div>');
    html = html.replace(/^\[warning\] (.+)$/gm, '<div class="callout callout-warning"><div class="callout-title">⚠️ Warning</div>$1</div>');
    html = html.replace(/^\[success\] (.+)$/gm, '<div class="callout callout-success"><div class="callout-title">✅ Success</div>$1</div>');

    // Bold and italic
    html = html.replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>');
    html = html.replace(/\*(.+?)\*/g, '<em>$1</em>');

    // Inline code
    html = html.replace(/`([^`]+)`/g, '<code>$1</code>');

    // Images — must be before links
    html = html.replace(/!\[([^\]]*)\]\(([^)]+)\)/g, '<img src="$2" alt="$1" style="max-width:100%;height:auto;border-radius:8px;margin:1rem 0;" loading="lazy">');

    // Links
    html = html.replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener">$1</a>');

    // Lists
    html = html.replace(/^(\d+)\. (.+)$/gm, '<li>$2</li>');
    html = html.replace(/^- (.+)$/gm, '<li>$1</li>');
    html = html.replace(/(<li>.*<\/li>\n?)+/g, (m) => '<ul>' + m + '</ul>');

    // Paragraphs (lines not already wrapped)
    html = html.split('\n').map(line => {
      const t = line.trim();
      if (!t) return '';
      if (/^<(h2|h3|h4|ul|ol|pre|blockquote|table|div|li|img)/.test(t)) return t;
      return '<p>' + t + '</p>';
    }).join('\n');

    // Clean up extra newlines
    html = html.replace(/\n+/g, '\n');

    return html;
  }

  function escapeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
  }

  function formatDate(dateStr) {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    return IS_ARABIC
      ? d.toLocaleDateString('ar-EG', { year: 'numeric', month: 'long', day: 'numeric' })
      : d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }

  /* ── Build TOC from content ── */
  function buildTOC(html) {
    const temp = document.createElement('div');
    temp.innerHTML = html;
    const headings = temp.querySelectorAll('h2, h3');
    if (headings.length === 0) return '';

    let tocHtml = '<h3 style="font-size:0.82rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.75rem;">' + T.tableOfContents + '</h3><ul class="toc">';
    headings.forEach((h, i) => {
      const id = 'heading-' + i;
      h.id = id;
      const cls = h.tagName === 'H3' ? 'toc-h3' : '';
      tocHtml += `<li><a href="#${id}" class="${cls}">${h.textContent}</a></li>`;
    });
    tocHtml += '</ul>';
    return tocHtml;
  }

  /* ── Update SEO meta tags ── */
  function updateSEO(article, data) {
    const url = `${SITE_URL}/${lang}/articles/${article.slug}.html`;
    const altLangUrl = `${SITE_URL}/${lang === 'en' ? 'ar' : 'en'}/articles/${article.slug}.html`;

    document.title = data.metaTitle || data.title;

    setMeta('description', data.metaDescription || data.excerpt);
    setMeta('keywords', (data.keywords || []).join(', '));
    setMeta('author', article.author);

    setOG('og:title', data.title);
    setOG('og:description', data.metaDescription || data.excerpt);
    setOG('og:url', url);
    setOG('og:type', 'article');
    setOG('og:image', article.heroImage ? SITE_URL + article.heroImage : '');
    setOG('og:locale', lang === 'ar' ? 'ar_SA' : 'en_US');

    setMeta('twitter:card', 'summary_large_image');
    setMeta('twitter:title', data.title);
    setMeta('twitter:description', data.metaDescription || data.excerpt);
    setMeta('twitter:image', article.heroImage ? SITE_URL + article.heroImage : '');

    // Canonical
    setLink('canonical', url);

    // hreflang
    setLinkAlt('alternate', url, lang);
    setLinkAlt('alternate', altLangUrl, lang === 'en' ? 'ar' : 'en');

    // JSON-LD
    const jsonLd = {
      "@context": "https://schema.org",
      "@type": "Article",
      "headline": data.title,
      "description": data.metaDescription || data.excerpt,
      "author": { "@type": "Person", "name": article.author },
      "datePublished": article.publishDate,
      "dateModified": article.updatedDate || article.publishDate,
      "image": article.heroImage ? SITE_URL + article.heroImage : undefined,
      "publisher": { "@type": "Person", "name": article.author },
      "mainEntityOfPage": url,
      "inLanguage": lang === 'ar' ? 'ar' : 'en'
    };
    let script = document.getElementById('article-jsonld');
    if (!script) {
      script = document.createElement('script');
      script.id = 'article-jsonld';
      script.type = 'application/ld+json';
      document.head.appendChild(script);
    }
    script.textContent = JSON.stringify(jsonLd);

    // Breadcrumb schema
    const breadcrumb = {
      "@context": "https://schema.org",
      "@type": "BreadcrumbList",
      "itemListElement": [
        { "@type": "ListItem", "position": 1, "name": IS_ARABIC ? 'الرئيسية' : 'Home', "item": SITE_URL },
        { "@type": "ListItem", "position": 2, "name": IS_ARABIC ? 'المقالات' : 'Articles', "item": SITE_URL + '/articles/' },
        { "@type": "ListItem", "position": 3, "name": data.title, "item": url }
      ]
    };
    let bcScript = document.getElementById('breadcrumb-jsonld');
    if (!bcScript) {
      bcScript = document.createElement('script');
      bcScript.id = 'breadcrumb-jsonld';
      bcScript.type = 'application/ld+json';
      document.head.appendChild(bcScript);
    }
    bcScript.textContent = JSON.stringify(breadcrumb);
  }

  function setMeta(name, content) {
    if (!content) return;
    let el = document.querySelector(`meta[name="${name}"]`);
    if (!el) { el = document.createElement('meta'); el.setAttribute('name', name); document.head.appendChild(el); }
    el.setAttribute('content', content);
  }
  function setOG(prop, content) {
    if (!content) return;
    let el = document.querySelector(`meta[property="${prop}"]`);
    if (!el) { el = document.createElement('meta'); el.setAttribute('property', prop); document.head.appendChild(el); }
    el.setAttribute('content', content);
  }
  function setLink(rel, href) {
    let el = document.querySelector(`link[rel="${rel}"]`);
    if (!el) { el = document.createElement('link'); el.setAttribute('rel', rel); document.head.appendChild(el); }
    el.setAttribute('href', href);
  }
  function setLinkAlt(rel, href, hreflang) {
    let el = document.querySelector(`link[rel="${rel}"][hreflang="${hreflang}"]`);
    if (!el) { el = document.createElement('link'); el.setAttribute('rel', rel); el.setAttribute('hreflang', hreflang); document.head.appendChild(el); }
    el.setAttribute('href', href);
  }

  /* ── Render Article ── */
  async function renderArticle() {
    let slug = getParam('slug');
    // Support static slug-based URLs like /en/articles/slug.html
    if (!slug) {
      const m = window.location.pathname.match(/\/articles\/([^/]+)\.html$/);
      if (m) slug = decodeURIComponent(m[1]);
    }
    if (!slug) { window.location.href = 'index.html'; return; }

    try {
      const res = await fetch(ASSET_BASE + 'articles/articles.json?v=' + Date.now(), { cache: 'no-store' });
      const articles = await res.json();
      const article = articles.find(a => a.slug === slug);

      if (!article || article.draft) { showNotFound(); return; }

      const data = article[lang] || article.en;
      document.documentElement.setAttribute('lang', lang);
      document.documentElement.setAttribute('dir', DIR);

      // Update SEO
      updateSEO(article, data);

      // Hero
      const heroEl = document.getElementById('article-hero');
      const heroImg = article.heroImage || '';
      heroEl.innerHTML = `
        ${heroImg ? `<img class="article-hero-img" src="${heroImg}" alt="${data.title}">` : ''}
        <div class="article-hero-overlay"></div>
        <div class="container article-hero-content">
          <span class="article-hero-cat">${article.category}</span>
          <h1>${data.title}</h1>
          <div class="article-hero-meta">
            <span>${T.by} ${article.author}</span>
            <span>· ${formatDate(article.publishDate)}</span>
            <span>· ${article.readingTime} ${T.minRead}</span>
            ${article.updatedDate !== article.publishDate ? `<span>· ${T.updated}: ${formatDate(article.updatedDate)}</span>` : ''}
          </div>
        </div>`;

      // Content
      const contentHtml = renderMarkdown(data.content);
      const tocHtml = buildTOC(contentHtml);

      const bodyEl = document.getElementById('article-body');
      bodyEl.innerHTML = `
        <div class="article-layout">
          <div>
            <div class="article-content" id="article-content">${contentHtml}</div>

            <div style="margin:2.5rem 0 1.5rem;padding-top:1.5rem;border-top:1px solid var(--border-light);">
              <div class="share-buttons">
                <span style="font-size:0.85rem;font-weight:600;color:var(--text-muted);margin-right:0.5rem;">${T.share}:</span>
                <a class="share-btn" href="https://twitter.com/intent/tweet?url=${encodeURIComponent(SITE_URL + '/' + lang + '/articles/' + article.slug + '.html')}&text=${encodeURIComponent(data.title)}" target="_blank" rel="noopener">𝕏 Twitter</a>
                <a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url=${encodeURIComponent(SITE_URL + '/' + lang + '/articles/' + article.slug + '.html')}" target="_blank" rel="noopener">LinkedIn</a>
                <a class="share-btn" href="https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(SITE_URL + '/' + lang + '/articles/' + article.slug + '.html')}" target="_blank" rel="noopener">Facebook</a>
                <button class="share-btn" onclick="navigator.clipboard.writeText(window.location.href);this.textContent='✓ Copied'">🔗 Copy Link</button>
              </div>
            </div>

            ${(article.tags || []).length ? `
            <div class="article-tags" style="margin:1.5rem 0;">
              <span style="font-size:0.85rem;font-weight:600;color:var(--text-muted);margin-right:0.5rem;">${IS_ARABIC ? 'الوسوم:' : 'Tags:'}</span>
              ${(article.tags || []).map(tag => `<a href="../articles/index.html?tag=${encodeURIComponent(tag)}" class="article-tag" style="display:inline-block;background:var(--bg-alt);border:1px solid var(--border-light);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.8rem;color:var(--text);text-decoration:none;margin:0.25rem;">#${tag}</a>`).join('')}
            </div>
            ` : ''}

            <div style="display:flex;justify-content:space-between;gap:1rem;margin:1.5rem 0;flex-wrap:wrap;" id="prev-next"></div>

            <a href="index.html" style="display:inline-block;margin-top:1rem;font-weight:600;color:var(--accent);text-decoration:none;">${T.backToArticles}</a>
          </div>

          <aside class="article-sidebar">
            ${tocHtml}
            <div style="margin-top:2rem;">
              <div class="article-lang-switch">
                <button class="${lang === 'en' ? 'active' : ''}" data-lang="en">🇺🇸 EN</button>
                <button class="${lang === 'ar' ? 'active' : ''}" data-lang="ar">🇸🇦 ع</button>
              </div>
            </div>
          </aside>
        </div>`;

      // Lang switch
      bodyEl.querySelectorAll('.article-lang-switch button').forEach(btn => {
        btn.addEventListener('click', () => {
          const newLang = btn.dataset.lang;
          window.location.href = `${SITE_URL}/${newLang}/articles/${article.slug}.html`;
        });
      });

      // Related articles
      renderRelated(articles, article);
      renderPrevNext(articles, article);

      // Newsletter
      renderNewsletter();

      // TOC scroll spy
      initScrollSpy();
    } catch (e) {
      console.error('Failed to load article:', e);
      showNotFound();
    }
  }

  /* ── Related Articles ── */
  function renderRelated(articles, current) {
    const el = document.getElementById('related-articles');
    if (!el) return;

    const currentTags = new Set(current.tags || []);
    const scored = articles
      .filter(a => !a.draft && a.slug !== current.slug)
      .map(a => {
        let score = 0;
        if (a.category === current.category) score += 3;
        const tagMatches = (a.tags || []).filter(t => currentTags.has(t)).length;
        score += tagMatches;
        return { article: a, score };
      })
      .filter(a => a.score > 0)
      .sort((a, b) => b.score - a.score)
      .slice(0, 6)
      .map(a => a.article);

    if (scored.length === 0) { el.style.display = 'none'; return; }
    const related = scored;

    el.innerHTML = `
      <h2 style="font-size:1.3rem;margin-bottom:1rem;">${T.relatedArticles}</h2>
      <div class="related-grid">
        ${related.map(a => {
          const d = a[lang] || a.en;
          const img = a.heroImage || '';
          const imgHtml = img
            ? `<img class="article-card-img" src="${img}" alt="${d.title}" loading="lazy">`
            : `<div class="article-card-img" style="display:flex;align-items:center;justify-content:center;font-size:2rem;background:var(--bg-alt);">📝</div>`;
          return `<a href="${a.slug}.html" class="article-card" style="text-decoration:none;color:inherit;">
            ${imgHtml}
            <div class="article-card-body">
              <div class="article-card-cat">${a.category}</div>
              <h3>${d.title}</h3>
              <p class="excerpt">${d.excerpt}</p>
            </div>
          </a>`;
        }).join('')}
      </div>`;
  }

  /* ── Prev / Next ── */
  function renderPrevNext(articles, current) {
    const el = document.getElementById('prev-next');
    if (!el) return;
    const published = articles.filter(a => !a.draft);
    const idx = published.findIndex(a => a.slug === current.slug);
    const prev = idx > 0 ? published[idx - 1] : null;
    const next = idx < published.length - 1 ? published[idx + 1] : null;

    let html = '';
    if (prev) {
      const d = prev[lang] || prev.en;
      html += `<a href="${prev.slug}.html" style="flex:1;min-width:200px;text-decoration:none;">
        <div style="font-size:0.78rem;color:var(--text-light);">← ${T.previousArticle}</div>
        <div style="font-weight:600;color:var(--text);font-size:0.9rem;margin-top:0.2rem;">${d.title}</div>
      </a>`;
    }
    if (next) {
      const d = next[lang] || next.en;
      html += `<a href="${next.slug}.html" style="flex:1;min-width:200px;text-align:right;text-decoration:none;">
        <div style="font-size:0.78rem;color:var(--text-light);">${T.nextArticle} →</div>
        <div style="font-weight:600;color:var(--text);font-size:0.9rem;margin-top:0.2rem;">${d.title}</div>
      </a>`;
    }
    el.innerHTML = html;
  }

  /* ── Newsletter ── */
  function renderNewsletter() {
    const el = document.getElementById('newsletter-section');
    if (!el) return;
    el.innerHTML = `
      <div class="newsletter-box">
        <h3>${T.newsletter}</h3>
        <p>${T.newsletterDesc}</p>
        <form id="newsletter-form" class="newsletter-form">
          <input type="email" placeholder="${T.emailPlaceholder}" required>
          <button type="submit">${T.subscribe}</button>
        </form>
      </div>`;
    document.getElementById('newsletter-form').addEventListener('submit', (e) => {
      e.preventDefault();
      e.target.innerHTML = `<p style="color:#fff;font-weight:600;">✓ ${IS_ARABIC ? 'شكراً لاشتراكك!' : 'Thanks for subscribing!'}</p>`;
    });
  }

  /* ── Scroll Spy for TOC ── */
  function initScrollSpy() {
    const tocLinks = document.querySelectorAll('.toc a');
    if (tocLinks.length === 0) return;
    const headings = document.querySelectorAll('.article-content h2, .article-content h3');

    window.addEventListener('scroll', () => {
      let current = '';
      headings.forEach(h => {
        if (window.scrollY >= h.offsetTop - 120) current = h.id;
      });
      tocLinks.forEach(link => {
        link.classList.toggle('active', link.getAttribute('href') === '#' + current);
      });
    }, { passive: true });
  }

  /* ── Not Found ── */
  function showNotFound() {
    document.getElementById('article-hero').style.display = 'none';
    document.getElementById('article-body').innerHTML = `
      <div style="text-align:center;padding:4rem 1rem;">
        <div style="font-size:3rem;margin-bottom:1rem;">📄</div>
        <h2>${T.notFound}</h2>
        <p style="color:var(--text-muted);margin:0.5rem 0 1.5rem;">${T.notFoundDesc}</p>
        <a href="index.html" style="font-weight:600;color:var(--accent);">${T.backToArticles}</a>
      </div>`;
    document.getElementById('related-articles').style.display = 'none';
    document.getElementById('newsletter-section').style.display = 'none';
  }

  // Start
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', renderArticle);
  } else {
    renderArticle();
  }
})();
