/* ============================================================
   ECMS – Core JavaScript v1.0
   ============================================================ */

'use strict';

/* ── Theme Management ── */
const Theme = (() => {
  const KEY = 'ecms-theme';
  const DARK = 'dark';
  const LIGHT = 'light';

  function get() {
    return localStorage.getItem(KEY) ||
      (window.matchMedia('(prefers-color-scheme: dark)').matches ? DARK : LIGHT);
  }

  function set(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem(KEY, theme);
    const btn = document.getElementById('themeToggle');
    if (btn) btn.textContent = theme === DARK ? '☀️' : '🌙';
    btn && btn.setAttribute('aria-label', `Switch to ${theme === DARK ? 'light' : 'dark'} mode`);
  }

  function toggle() {
    set(get() === DARK ? LIGHT : DARK);
  }

  function init() {
    set(get());
    const btn = document.getElementById('themeToggle');
    if (btn) btn.addEventListener('click', toggle);
  }

  return { init, get, set, toggle };
})();

/* ── Navigation ── */
const Nav = (() => {
  function init() {
    const hamburger = document.getElementById('navHamburger');
    const links = document.getElementById('navLinks');

    if (hamburger && links) {
      hamburger.addEventListener('click', () => {
        links.classList.toggle('open');
        hamburger.setAttribute('aria-expanded', links.classList.contains('open'));
      });

      links.querySelectorAll('a').forEach(a => {
        a.addEventListener('click', () => {
          links.classList.remove('open');
          hamburger.setAttribute('aria-expanded', 'false');
        });
      });
    }

    highlightActive();
  }

  function highlightActive() {
    const path = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a').forEach(a => {
      const href = a.getAttribute('href');
      if (href === path || (path === '' && href === 'index.html')) {
        a.classList.add('active');
      }
    });
  }

  return { init };
})();

/* ── Scroll Animations ── */
const ScrollAnim = (() => {
  function init() {
    const elements = document.querySelectorAll('.reveal');
    if (!elements.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach((entry, i) => {
        if (entry.isIntersecting) {
          setTimeout(() => {
            entry.target.classList.add('visible');
          }, i * 60);
          observer.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1, rootMargin: '0px 0px -40px 0px' });

    elements.forEach(el => observer.observe(el));
  }

  return { init };
})();

/* ── Progress Bar ── */
const ProgressBar = (() => {
  function init() {
    const bar = document.querySelector('.page-progress');
    if (!bar) return;

    window.addEventListener('scroll', () => {
      const scrollTop = window.scrollY;
      const docHeight = document.documentElement.scrollHeight - window.innerHeight;
      const pct = docHeight > 0 ? (scrollTop / docHeight) * 100 : 0;
      bar.style.width = pct + '%';
    }, { passive: true });
  }

  return { init };
})();

/* ── Back to Top ── */
const BackToTop = (() => {
  function init() {
    const btn = document.getElementById('backToTop');
    if (!btn) return;

    window.addEventListener('scroll', () => {
      btn.classList.toggle('visible', window.scrollY > 400);
    }, { passive: true });

    btn.addEventListener('click', () => {
      window.scrollTo({ top: 0, behavior: 'smooth' });
    });
  }

  return { init };
})();

/* ── Counter Animations ── */
const Counter = (() => {
  function animateValue(el, from, to, duration) {
    const start = performance.now();
    const isDecimal = to !== Math.floor(to);

    function update(timestamp) {
      const elapsed = timestamp - start;
      const progress = Math.min(elapsed / duration, 1);
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = from + (to - from) * eased;
      el.textContent = isDecimal ? current.toFixed(1) : Math.floor(current).toLocaleString();
      if (progress < 1) requestAnimationFrame(update);
    }

    requestAnimationFrame(update);
  }

  function init() {
    const counters = document.querySelectorAll('[data-counter]');
    if (!counters.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const el = entry.target;
          const target = parseFloat(el.dataset.counter);
          animateValue(el, 0, target, 1800);
          observer.unobserve(el);
        }
      });
    }, { threshold: 0.5 });

    counters.forEach(c => observer.observe(c));
  }

  return { init };
})();

/* ── Skill Bars ── */
const SkillBars = (() => {
  function init() {
    const bars = document.querySelectorAll('.skill-bar-fill');
    if (!bars.length) return;

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          const bar = entry.target;
          const pct = bar.dataset.width || '0';
          bar.style.width = pct + '%';
          observer.unobserve(bar);
        }
      });
    }, { threshold: 0.3 });

    bars.forEach(b => observer.observe(b));
  }

  return { init };
})();

/* ── Accordion ── */
const Accordion = (() => {
  function init() {
    document.querySelectorAll('.accordion-header').forEach(header => {
      header.addEventListener('click', () => {
        const item = header.closest('.accordion-item');
        const isOpen = item.classList.contains('open');
        item.classList.toggle('open', !isOpen);
        header.setAttribute('aria-expanded', !isOpen);
      });
    });
  }

  return { init };
})();

/* ── Filter Tabs ── */
const FilterTabs = (() => {
  function init() {
    document.querySelectorAll('.filter-tabs').forEach(tabGroup => {
      tabGroup.querySelectorAll('.filter-tab').forEach(tab => {
        tab.addEventListener('click', () => {
          const group = tab.closest('.filter-tabs');
          group.querySelectorAll('.filter-tab').forEach(t => t.classList.remove('active'));
          tab.classList.add('active');

          const filter = tab.dataset.filter;
          const targetGroup = tab.dataset.target;
          const items = document.querySelectorAll(`[data-filter-group="${targetGroup}"]`);

          items.forEach(item => {
            if (filter === 'all' || item.dataset.category === filter ||
                (item.dataset.tags && item.dataset.tags.includes(filter))) {
              item.style.display = '';
              item.classList.add('reveal');
              setTimeout(() => item.classList.add('visible'), 50);
            } else {
              item.style.display = 'none';
            }
          });
        });
      });
    });
  }

  return { init };
})();

/* ── Search Modal ── */
const SearchModal = (() => {
  let data = null;

  async function loadData() {
    if (data) return data;
    try {
      const res = await fetch('data/career-knowledge-base.json');
      data = await res.json();
      return data;
    } catch (e) {
      console.error('Failed to load career data:', e);
      return null;
    }
  }

  function buildIndex(kb) {
    const items = [];

    if (kb.experience) {
      kb.experience.forEach(e => {
        items.push({
          icon: '🏢',
          title: e.role,
          subtitle: `${e.company} • ${e.duration}`,
          url: `career.html#${e.id}`,
          tags: [e.company, e.country, ...(e.technologies || [])].join(' ').toLowerCase()
        });
      });
    }

    if (kb.projects) {
      kb.projects.forEach(p => {
        items.push({
          icon: '📋',
          title: p.name,
          subtitle: `${p.projectType} • ${p.country}`,
          url: `projects.html#${p.id}`,
          tags: [p.name, p.client, p.country, ...(p.technologies || [])].join(' ').toLowerCase()
        });
      });
    }

    if (kb.certifications) {
      kb.certifications.forEach(c => {
        items.push({
          icon: '🏆',
          title: c.name,
          subtitle: c.issuingBody,
          url: `certifications.html#${c.id}`,
          tags: [c.name, c.issuingBody].join(' ').toLowerCase()
        });
      });
    }

    if (kb.skills) {
      Object.entries(kb.skills).forEach(([cat, arr]) => {
        arr.forEach(skill => {
          items.push({
            icon: '⚡',
            title: skill,
            subtitle: `Skill – ${cat}`,
            url: `skills.html`,
            tags: (cat + ' ' + skill).toLowerCase()
          });
        });
      });
    }

    return items;
  }

  function render(items) {
    const container = document.getElementById('searchResults');
    if (!container) return;

    if (!items.length) {
      container.innerHTML = '<div class="search-no-results">No results found. Try a different search term.</div>';
      return;
    }

    container.innerHTML = items.slice(0, 12).map(item => `
      <a class="search-result-item" href="${item.url}">
        <div class="search-result-icon">${item.icon}</div>
        <div>
          <div class="search-result-title">${item.title}</div>
          <div class="search-result-sub">${item.subtitle}</div>
        </div>
      </a>
    `).join('');
  }

  async function search(query) {
    const kb = await loadData();
    if (!kb) return;

    const index = buildIndex(kb);
    const q = query.toLowerCase().trim();

    if (!q) {
      render([]);
      return;
    }

    const results = index.filter(item =>
      item.title.toLowerCase().includes(q) ||
      item.subtitle.toLowerCase().includes(q) ||
      item.tags.includes(q)
    );

    render(results);
  }

  function open() {
    const overlay = document.getElementById('searchOverlay');
    const input = document.getElementById('searchInput');
    if (overlay) overlay.classList.add('active');
    if (input) { input.value = ''; input.focus(); }
    document.body.style.overflow = 'hidden';
  }

  function close() {
    const overlay = document.getElementById('searchOverlay');
    if (overlay) overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  function init() {
    const openBtns = document.querySelectorAll('[data-search-open]');
    openBtns.forEach(btn => btn.addEventListener('click', open));

    const overlay = document.getElementById('searchOverlay');
    if (overlay) {
      overlay.addEventListener('click', (e) => {
        if (e.target === overlay) close();
      });
    }

    const input = document.getElementById('searchInput');
    if (input) {
      let timer;
      input.addEventListener('input', () => {
        clearTimeout(timer);
        timer = setTimeout(() => search(input.value), 200);
      });
    }

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') close();
      if ((e.ctrlKey || e.metaKey) && e.key === 'k') { e.preventDefault(); open(); }
    });
  }

  return { init, open, close };
})();

/* ── Data Loader ── */
const DataLoader = (() => {
  let cache = {};

  async function load(url) {
    if (cache[url]) return cache[url];
    const res = await fetch(url);
    const data = await res.json();
    cache[url] = data;
    return data;
  }

  return { load };
})();

/* ── Nav Dropdown ── */
const NavDropdown = (() => {
  function init() {
    const wrap = document.querySelector('.nav-dropdown-wrap');
    if (!wrap) return;
    const btn = wrap.querySelector('.nav-dropdown-btn');
    const menu = wrap.querySelector('.nav-dropdown');
    if (!btn || !menu) return;

    btn.addEventListener('click', (e) => {
      e.stopPropagation();
      const isOpen = menu.classList.contains('open');
      menu.classList.toggle('open', !isOpen);
      btn.setAttribute('aria-expanded', String(!isOpen));
    });

    document.addEventListener('click', () => {
      menu.classList.remove('open');
      btn.setAttribute('aria-expanded', 'false');
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        menu.classList.remove('open');
        btn.setAttribute('aria-expanded', 'false');
      }
    });
  }

  return { init };
})();

/* ── Active Nav Link ── */
const ActiveNav = (() => {
  function init() {
    const current = window.location.pathname.split('/').pop() || 'index.html';
    document.querySelectorAll('.nav-links a, .nav-dropdown a').forEach(a => {
      const href = a.getAttribute('href');
      if (href === current || (current === '' && href === 'index.html')) {
        a.style.color = 'var(--accent)';
        a.setAttribute('aria-current', 'page');
      }
    });
  }
  return { init };
})();

/* ── App Init ── */
document.addEventListener('DOMContentLoaded', () => {
  if (window.I18N) I18N.init();
  Theme.init();
  Nav.init();
  NavDropdown.init();
  ActiveNav.init();
  ScrollAnim.init();
  ProgressBar.init();
  BackToTop.init();
  Counter.init();
  SkillBars.init();
  Accordion.init();
  FilterTabs.init();
  SearchModal.init();
});

/* ── Global Exports ── */
window.ECMS = { Theme, Nav, DataLoader, SearchModal, I18N };
