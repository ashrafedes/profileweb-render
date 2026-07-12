/* ============================================================
   Articles Center – Listing Page Logic
   Handles: listing, search, categories, pagination, featured
   Bilingual: detects ?lang= param or <html lang> attr
   ============================================================ */

'use strict';

(function () {
  const SITE_URL = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.SITE_URL) || '';
  const PER_PAGE = (typeof ARTICLES_CONFIG !== 'undefined' && ARTICLES_CONFIG.ARTICLES_PER_PAGE) || 6;

  // Detect subdirectory: /en/articles/ or /ar/articles/ vs root /articles/
  const _path = window.location.pathname;
  const _inSub = /\/(en|ar)\/articles\//.test(_path);
  const _subLang = _path.match(/\/(en|ar)\/articles\//);
  const IS_ARABIC = (_subLang && _subLang[1] === 'ar') ||
    new URLSearchParams(window.location.search).get('lang') === 'ar' ||
    document.documentElement.getAttribute('lang') === 'ar';
  const LANG = IS_ARABIC ? 'ar' : 'en';
  const DIR = IS_ARABIC ? 'rtl' : 'ltr';

  // Path prefixes: ../../ from subdirs, ../ from root
  const ASSET_BASE = _inSub ? '../../' : '../';
  const JSON_URL = ASSET_BASE + 'articles/articles.json?v=2';

  const T = IS_ARABIC ? {
    title: 'مركز المقالات',
    subtitle: 'مقالات ورؤى حول إدارة المشاريع والاتصالات والتحول الرقمي',
    searchPlaceholder: 'ابحث في المقالات…',
    featured: 'مميز',
    readMore: 'اقرأ المزيد',
    readingTime: 'دقائق قراءة',
    by: 'بقلم',
    noResults: 'لا توجد مقالات مطابقة',
    allCategories: 'الكل',
    popularTopics: 'مواضيع شائعة',
    latestArticles: 'أحدث المقالات',
    page: 'صفحة',
    of: 'من',
    newsletter: 'اشترك في النشرة البريدية',
    newsletterDesc: 'احصل على أحدث المقالات والرؤى مباشرة في بريدك',
    subscribe: 'اشترك',
    emailPlaceholder: 'بريدك الإلكتروني',
    backToArticles: 'العودة للمقالات'
  } : {
    title: 'Articles Center',
    subtitle: 'Articles and insights on project management, telecommunications, and digital transformation',
    searchPlaceholder: 'Search articles…',
    featured: 'Featured',
    readMore: 'Read more',
    readingTime: 'min read',
    by: 'By',
    noResults: 'No matching articles found',
    allCategories: 'All',
    popularTopics: 'Popular Topics',
    latestArticles: 'Latest Articles',
    page: 'Page',
    of: 'of',
    newsletter: 'Subscribe to Newsletter',
    newsletterDesc: 'Get the latest articles and insights delivered to your inbox',
    subscribe: 'Subscribe',
    emailPlaceholder: 'Your email',
    backToArticles: 'Back to Articles'
  };

  let allArticles = [];
  let filtered = [];
  let currentPage = 1;
  let activeCategory = 'all';
  let searchQuery = '';
  let sortDirection = -1; // -1 = newest first, 1 = oldest first

  /* ── Sorting ── */
  function sortArticles() {
    filtered.sort((a, b) => {
      const da = new Date(a.publishDate || '1970-01-01').getTime();
      const db = new Date(b.publishDate || '1970-01-01').getTime();
      return sortDirection === -1 ? db - da : da - db;
    });
  }

  function toggleSort() {
    sortDirection = sortDirection === -1 ? 1 : -1;
    const btn = document.getElementById('btn-sort-date');
    if (btn) btn.textContent = sortDirection === -1 ? (IS_ARABIC ? 'التاريخ ↓' : 'Date ↓') : (IS_ARABIC ? 'التاريخ ↑' : 'Date ↑');
    currentPage = 1;
    applySortAndRender();
  }

  function applySortAndRender() {
    sortArticles();
    renderArticles();
    renderPagination();
  }

  /* ── Fetch articles ── */
  async function loadArticles() {
    try {
      const res = await fetch(JSON_URL);
      allArticles = await res.json();
      // Filter out drafts
      filtered = allArticles.filter(a => !a.draft);
      sortArticles();
      init();
    } catch (e) {
      console.error('Failed to load articles:', e);
      document.getElementById('articles-grid').innerHTML =
        '<p style="text-align:center;padding:3rem;color:var(--text-muted);">' + T.noResults + '</p>';
    }
  }

  /* ── Render Featured ── */
  function renderFeatured() {
    const el = document.getElementById('featured-article');
    if (!el) return;
    const featured = filtered.find(a => a.featured) || filtered[0];
    if (!featured) { el.style.display = 'none'; return; }

    const data = featured[LANG] || featured.en;
    const img = featured.heroImage || '';
    const imgStyle = img ? `background-image:url('${img}')` : 'background:var(--bg-alt)';

    el.innerHTML = `
      <a href="article.html?slug=${featured.slug}&lang=${LANG}" style="text-decoration:none;color:inherit;display:block;">
        <div class="featured-card">
          <div class="featured-card-img" style="${imgStyle}"></div>
          <div class="featured-card-body">
            <span class="featured-badge">${T.featured}</span>
            <h2>${data.title}</h2>
            <p class="excerpt">${data.excerpt}</p>
            <div class="article-card-meta">
              <span>${T.by} ${featured.author}</span>
              <span>${formatDate(featured.publishDate)}</span>
              <span>· ${featured.readingTime} ${T.readingTime}</span>
            </div>
          </div>
        </div>
      </a>`;
  }

  /* ── Render Category Pills ── */
  function renderCategories() {
    const el = document.getElementById('category-pills');
    if (!el) return;
    const cats = ['all', ...new Set(allArticles.map(a => a.category))];
    el.innerHTML = cats.map(cat => `
      <button class="category-pill ${cat === activeCategory ? 'active' : ''}" data-cat="${cat}">
        ${cat === 'all' ? T.allCategories : cat}
      </button>`).join('');

    el.querySelectorAll('.category-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        activeCategory = btn.dataset.cat;
        currentPage = 1;
        applyFilters();
        renderCategories();
      });
    });
  }

  /* ── Render Popular Topics ── */
  function renderPopularTopics() {
    const el = document.getElementById('popular-topics');
    if (!el) return;
    const tagCount = {};
    allArticles.forEach(a => (a.tags || []).forEach(t => { tagCount[t] = (tagCount[t] || 0) + 1; }));
    const top = Object.entries(tagCount).sort((a, b) => b[1] - a[1]).slice(0, 10);
    el.innerHTML = top.map(([tag]) =>
      `<button class="category-pill" data-tag="${tag}">${tag}</button>`).join('');

    el.querySelectorAll('.category-pill').forEach(btn => {
      btn.addEventListener('click', () => {
        searchQuery = btn.dataset.tag;
        document.getElementById('articles-search').value = searchQuery;
        currentPage = 1;
        applyFilters();
      });
    });
  }

  /* ── Apply Filters ── */
  function applyFilters() {
    filtered = allArticles.filter(a => {
      if (a.draft) return false;
      if (activeCategory !== 'all' && a.category !== activeCategory) return false;
      if (searchQuery) {
        const q = searchQuery.toLowerCase();
        const d = a[LANG] || a.en;
        const haystack = [
          d.title, d.excerpt, d.content, d.metaTitle, d.metaDescription,
          ...(d.keywords || []), ...(a.tags || []), a.category, a.author
        ].join(' ').toLowerCase();
        if (!haystack.includes(q)) return false;
      }
      return true;
    });
    sortArticles();
    renderArticles();
    renderPagination();
  }

  /* ── Render Article Cards ── */
  function renderArticles() {
    const el = document.getElementById('articles-grid');
    if (!el) return;
    const start = (currentPage - 1) * PER_PAGE;
    const pageItems = filtered.slice(start, start + PER_PAGE);

    if (pageItems.length === 0) {
      el.innerHTML = `<div style="grid-column:1/-1;text-align:center;padding:3rem;color:var(--text-muted);">
        <div style="font-size:2.5rem;margin-bottom:0.5rem;">📭</div>${T.noResults}</div>`;
      return;
    }

    el.innerHTML = pageItems.map(a => {
      const d = a[LANG] || a.en;
      const img = a.heroImage || '';
      const imgHtml = img
        ? `<img class="article-card-img" src="${img}" alt="${d.title}" loading="lazy">`
        : `<div class="article-card-img" style="display:flex;align-items:center;justify-content:center;font-size:2rem;background:var(--bg-alt);">📝</div>`;
      return `
        <a href="article.html?slug=${a.slug}&lang=${LANG}" class="article-card" style="text-decoration:none;color:inherit;">
          ${imgHtml}
          <div class="article-card-body">
            <div class="article-card-cat">${a.category}</div>
            <h3>${d.title}</h3>
            <p class="excerpt">${d.excerpt}</p>
            <div class="article-card-meta">
              <span>${formatDate(a.publishDate)}</span>
              <span>· ${a.readingTime} ${T.readingTime}</span>
              ${(a.tags || []).slice(0, 2).map(t => `<span class="tag">${t}</span>`).join('')}
            </div>
          </div>
        </a>`;
    }).join('');
  }

  /* ── Render Pagination ── */
  function renderPagination() {
    const el = document.getElementById('pagination');
    if (!el) return;
    const totalPages = Math.ceil(filtered.length / PER_PAGE);
    if (totalPages <= 1) { el.innerHTML = ''; return; }

    let html = '';
    html += `<button ${currentPage === 1 ? 'disabled' : ''} data-page="${currentPage - 1}">‹</button>`;
    for (let i = 1; i <= totalPages; i++) {
      html += `<button class="${i === currentPage ? 'active' : ''}" data-page="${i}">${i}</button>`;
    }
    html += `<button ${currentPage === totalPages ? 'disabled' : ''} data-page="${currentPage + 1}">›</button>`;
    el.innerHTML = html;

    el.querySelectorAll('button').forEach(btn => {
      btn.addEventListener('click', () => {
        const p = parseInt(btn.dataset.page);
        if (p >= 1 && p <= totalPages) {
          currentPage = p;
          renderArticles();
          renderPagination();
          window.scrollTo({ top: 300, behavior: 'smooth' });
        }
      });
    });
  }

  /* ── Format Date ── */
  function formatDate(dateStr) {
    if (!dateStr) return '';
    const d = new Date(dateStr);
    if (IS_ARABIC) {
      return d.toLocaleDateString('ar-EG', { year: 'numeric', month: 'long', day: 'numeric' });
    }
    return d.toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric' });
  }

  /* ── Search Handler (debounced) ── */
  let searchTimer;
  function initSearch() {
    const input = document.getElementById('articles-search');
    if (!input) return;
    input.addEventListener('input', () => {
      clearTimeout(searchTimer);
      searchTimer = setTimeout(() => {
        searchQuery = input.value.trim();
        currentPage = 1;
        applyFilters();
      }, 200);
    });
  }

  /* ── Newsletter (placeholder) ── */
  function initNewsletter() {
    const form = document.getElementById('newsletter-form');
    if (!form) return;
    form.addEventListener('submit', (e) => {
      e.preventDefault();
      const email = form.querySelector('input').value;
      // Placeholder: wire up to your email provider
      console.log('Newsletter subscription:', email);
      form.innerHTML = `<p style="color:#fff;font-weight:600;">✓ ${IS_ARABIC ? 'شكراً لاشتراكك!' : 'Thanks for subscribing!'}</p>`;
    });
  }

  /* ── Init ── */
  function init() {
    document.documentElement.setAttribute('lang', LANG);
    document.documentElement.setAttribute('dir', DIR);

    // Set page title
    const titleEl = document.querySelector('#articles-page-title');
    if (titleEl) titleEl.textContent = T.title;
    const subtitleEl = document.querySelector('#articles-page-subtitle');
    if (subtitleEl) subtitleEl.textContent = T.subtitle;

    renderFeatured();
    renderCategories();
    renderPopularTopics();
    renderArticles();
    renderPagination();
    initSearch();
    initNewsletter();

    // Render newsletter section
    const nl = document.getElementById('newsletter-section');
    if (nl) {
      nl.innerHTML = `
        <div class="newsletter-box">
          <h3>${T.newsletter}</h3>
          <p>${T.newsletterDesc}</p>
          <form id="newsletter-form" class="newsletter-form">
            <input type="email" placeholder="${T.emailPlaceholder}" required>
            <button type="submit">${T.subscribe}</button>
          </form>
        </div>`;
      initNewsletter();
    }
  }

  // Expose sort toggle for HTML onclick
  window.toggleArticleSort = toggleSort;

  // Start
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadArticles);
  } else {
    loadArticles();
  }
})();
