/* ============================================================
   ECMS – Shared HTML Components (Nav + Footer)
   Bilingual: detects lang attr and directory for en/ ar/ routing
   ============================================================ */

'use strict';

(function () {

  // ── Detect language and directory ──
  const IS_ARABIC = document.documentElement.getAttribute('lang') === 'ar';
  const DIR = IS_ARABIC ? 'rtl' : 'ltr';
  const path = window.location.pathname;
  const IN_SUBDIR = /\/(en|ar)\//.test(path);
  const SUBDIR = IN_SUBDIR ? (IS_ARABIC ? '../en/' : '../ar/') : '';
  const CURRENT_PAGE = path.split('/').pop() || 'index.html';

  // ── Language toggle: link to same page in other language dir ──
  const langToggleUrl = SUBDIR + CURRENT_PAGE;

  // ── Bilingual UI strings ──
  const T = IS_ARABIC ? {
    skipLink: 'تخطي إلى المحتوى',
    brandName: 'أشرف الدسوقي',
    brandTitle: 'نظام إدارة المسيرة التنفيذية',
    dashboard: 'الرئيسية',
    about: 'نبذة',
    experience: 'المسيرة',
    projects: 'المشاريع',
    featuredProjects: 'المشاريع المميزة',
    skills: 'المهارات',
    more: 'المزيد ▾',
    companies: 'الشركات',
    achievements: 'الإنجازات',
    pmoLeadership: 'قيادة مكتب إدارة المشاريع',
    telecommunications: 'الاتصالات',
    projectControls: 'التحكم بالمشاريع',
    digitalTransformation: 'التحول الرقمي',
    leadership: 'القيادة',
    software: 'البرمجيات',
    certifications: 'الشهادات',
    education: 'التعليم',
    awards: 'الجوائز',
    downloads: 'التحميلات',
    contact: 'تواصل',
    search: '🔍 بحث',
    searchPlaceholder: 'ابحث في الخبرة، المشاريع، المهارات، الشهادات…',
    langToggle: 'English 🌐',
    langToggleAria: 'التبديل إلى الإنجليزية',
    backToTop: '↑',
    footerBrand: 'المهندس أشرف إبراهيم الدسوقي، PMP®',
    footerDesc: 'مدير المشاريع | رئيس مكتب إدارة المشاريع والتحكم بالمشاريع | قائد الاتصالات والبنية الرقمية. نظام إدارة المسيرة التنفيذية هو قاعدة المعرفة الرقمية الدائمة لمسيرتي المهنية.',
    footerNav: 'التنقل',
    footerExpertise: 'خبرات',
    footerResources: 'موارد',
    footerAllSkills: 'كل المهارات',
    footerSearch: 'بحث',
    footerRights: '© ' + new Date().getFullYear() + ' أشرف إبراهيم الدسوقي، PMP® – جميع الحقوق محفوظة',
    footerVersion: 'نظام إدارة المسيرة التنفيذية v1.0'
  } : {
    skipLink: 'Skip to main content',
    brandName: 'Ashraf El Desoky',
    brandTitle: 'Executive Career Management System',
    dashboard: 'Dashboard',
    about: 'About',
    experience: 'Experience',
    projects: 'Projects',
    featuredProjects: 'Featured Projects',
    skills: 'Skills',
    more: 'More ▾',
    companies: 'Companies',
    achievements: 'Achievements',
    pmoLeadership: 'PMO Leadership',
    telecommunications: 'Telecommunications',
    projectControls: 'Project Controls',
    digitalTransformation: 'Digital Transformation',
    leadership: 'Leadership',
    software: 'Software',
    certifications: 'Certifications',
    education: 'Education',
    awards: 'Awards',
    downloads: 'Downloads',
    contact: 'Contact',
    search: '🔍 Search',
    searchPlaceholder: 'Search experience, projects, skills, certifications…',
    langToggle: 'العربية 🌐',
    langToggleAria: 'Switch to Arabic',
    backToTop: '↑',
    footerBrand: 'Ashraf Ibrahim El Desoky, PMP®',
    footerDesc: 'Projects Director | PMO & Project Controls Executive | Telecommunications & Digital Infrastructure Leader. This Executive Career Management System is the permanent digital knowledge base for my professional career.',
    footerNav: 'Navigation',
    footerExpertise: 'Expertise',
    footerResources: 'Resources',
    footerAllSkills: 'All Skills',
    footerSearch: 'Search',
    footerRights: '© ' + new Date().getFullYear() + ' Ashraf Ibrahim El Desoky, PMP® – All Rights Reserved',
    footerVersion: 'Executive Career Management System v1.0'
  };

  const NAV_HTML = `
<a class="skip-link" href="#main-content">${T.skipLink}</a>
<div class="page-progress" role="progressbar" aria-label="Page scroll progress"></div>

<nav class="ecms-nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand" aria-label="${T.dashboard}">
      <div class="brand-icon" aria-hidden="true">AE</div>
      <div class="brand-text">
        <span class="brand-name">${T.brandName}</span>
        <span class="brand-title">${T.brandTitle}</span>
      </div>
    </a>

    <ul class="nav-links" id="navLinks" role="menubar">
      <li role="none"><a href="index.html" role="menuitem">${T.dashboard}</a></li>
      <li role="none"><a href="about.html" role="menuitem">${T.about}</a></li>
      <li role="none"><a href="career.html" role="menuitem">${T.experience}</a></li>
      <li role="none"><a href="projects.html" role="menuitem">${T.projects}</a></li>
      <li role="none"><a href="featured-projects.html" role="menuitem">${T.featuredProjects}</a></li>
      <li role="none"><a href="skills.html" role="menuitem">${T.skills}</a></li>
      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">${T.more}</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="companies.html" role="menuitem">${T.companies}</a></li>
          <li><a href="achievements.html" role="menuitem">${T.achievements}</a></li>
          <li><a href="pmo.html" role="menuitem">${T.pmoLeadership}</a></li>
          <li><a href="telecommunications.html" role="menuitem">${T.telecommunications}</a></li>
          <li><a href="project-controls.html" role="menuitem">${T.projectControls}</a></li>
          <li><a href="digital-transformation.html" role="menuitem">${T.digitalTransformation}</a></li>
          <li><a href="leadership.html" role="menuitem">${T.leadership}</a></li>
          <li><a href="software.html" role="menuitem">${T.software}</a></li>
          <li><a href="certifications.html" role="menuitem">${T.certifications}</a></li>
          <li><a href="education.html" role="menuitem">${T.education}</a></li>
          <li><a href="awards.html" role="menuitem">${T.awards}</a></li>
        </ul>
      </li>
      <li role="none"><a href="downloads.html" role="menuitem">${T.downloads}</a></li>
      <li role="none"><a href="contact.html" role="menuitem">${T.contact}</a></li>
    </ul>

    <div class="nav-actions">
      <button class="btn-nav btn-nav-search" data-search-open aria-label="Search (Ctrl+K)">
        ${T.search}
      </button>
      <a href="${langToggleUrl}" class="btn-i18n-toggle" aria-label="${T.langToggleAria}" style="background:rgba(255,255,255,0.1);border:1px solid rgba(255,255,255,0.15);border-radius:var(--radius-sm);padding:0.35rem 0.6rem;font-size:0.78rem;font-weight:600;cursor:pointer;color:rgba(255,255,255,0.8);transition:var(--transition);text-decoration:none;display:inline-block;">${T.langToggle}</a>
      <button class="btn-theme-toggle" id="themeToggle" aria-label="Toggle dark/light mode">🌙</button>
      <button class="nav-hamburger" id="navHamburger" aria-label="Open navigation menu" aria-expanded="false" aria-controls="navLinks">
        <span></span><span></span><span></span>
      </button>
    </div>
  </div>
</nav>

<!-- Search Modal -->
<div class="search-overlay" id="searchOverlay" role="dialog" aria-modal="true" aria-label="Search">
  <div class="search-modal">
    <div class="search-input-wrap">
      <span class="search-icon" aria-hidden="true">🔍</span>
      <input type="search" id="searchInput" placeholder="${T.searchPlaceholder}" autocomplete="off" aria-label="Search">
      <kbd style="font-size:0.7rem;color:var(--text-muted);border:1px solid var(--border);padding:2px 6px;border-radius:4px;">ESC</kbd>
    </div>
    <div class="search-results" id="searchResults" role="listbox"></div>
  </div>
</div>

<button id="backToTop" aria-label="Back to top" title="Back to top">${T.backToTop}</button>
`;

  const FOOTER_HTML = `
<footer class="ecms-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="brand-name">${T.footerBrand}</div>
        <p>${T.footerDesc}</p>
      </div>
      <div>
        <div class="footer-col-title">${T.footerNav}</div>
        <ul class="footer-links">
          <li><a href="index.html">${T.dashboard}</a></li>
          <li><a href="about.html">${T.about}</a></li>
          <li><a href="career.html">${T.experience}</a></li>
          <li><a href="companies.html">${T.companies}</a></li>
          <li><a href="projects.html">${T.projects}</a></li>
          <li><a href="featured-projects.html">${T.featuredProjects}</a></li>
          <li><a href="achievements.html">${T.achievements}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">${T.footerExpertise}</div>
        <ul class="footer-links">
          <li><a href="pmo.html">${T.pmoLeadership}</a></li>
          <li><a href="project-controls.html">${T.projectControls}</a></li>
          <li><a href="telecommunications.html">${T.telecommunications}</a></li>
          <li><a href="digital-transformation.html">${T.digitalTransformation}</a></li>
          <li><a href="leadership.html">${T.leadership}</a></li>
          <li><a href="skills.html">${T.footerAllSkills}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">${T.footerResources}</div>
        <ul class="footer-links">
          <li><a href="education.html">${T.education}</a></li>
          <li><a href="certifications.html">${T.certifications}</a></li>
          <li><a href="awards.html">${T.awards}</a></li>
          <li><a href="downloads.html">${T.downloads}</a></li>
          <li><a href="search.html">${T.footerSearch}</a></li>
          <li><a href="contact.html">${T.contact}</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>${T.footerRights}</span>
      <span>${T.footerVersion}</span>
    </div>
  </div>
</footer>
`;

  function injectComponents() {
    const navTarget = document.getElementById('ecms-nav-inject');
    if (navTarget) navTarget.outerHTML = NAV_HTML;

    const footerTarget = document.getElementById('ecms-footer-inject');
    if (footerTarget) footerTarget.outerHTML = FOOTER_HTML;
  }

  document.addEventListener('DOMContentLoaded', injectComponents);

})();
