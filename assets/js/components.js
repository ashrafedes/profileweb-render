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
  const IN_ARTICLES_DIR = /\/articles\//.test(path);
  const IN_LANG_ARTICLES = /\/(en|ar)\/articles\//.test(path);
  const IN_HUB_DIR = /\/(ftth|project-controls-hub)\//.test(path);
  const IN_LANG_HUB = /\/(en|ar)\/(ftth|project-controls-hub)\//.test(path);
  const CURRENT_PAGE = path.split('/').pop() || 'index.html';

  // ── Nav base: '../' when inside any subdir (articles, ftth, project-controls-hub), '' otherwise ──
  const NAV_BASE = (IN_ARTICLES_DIR || IN_HUB_DIR) ? '../' : '';

  // ── Articles link: 'index.html' if already in articles, else NAV_BASE + 'articles/' ──
  const ARTICLES_LINK = IN_ARTICLES_DIR ? 'index.html' : NAV_BASE + 'articles/';

  // ── Language toggle: link to same page in other language dir ──
  let langToggleUrl;
  if (IN_LANG_ARTICLES) {
    const otherLang = IS_ARABIC ? 'en' : 'ar';
    langToggleUrl = `../../${otherLang}/articles/${CURRENT_PAGE}`;
  } else if (IN_LANG_HUB) {
    const otherLang = IS_ARABIC ? 'en' : 'ar';
    const hubMatch = path.match(/\/(en|ar)\/(ftth|project-controls-hub)\//);
    const hub = hubMatch ? hubMatch[2] : '';
    langToggleUrl = `../../${otherLang}/${hub}/${CURRENT_PAGE}`;
  } else if (IN_SUBDIR) {
    langToggleUrl = (IS_ARABIC ? '../en/' : '../ar/') + CURRENT_PAGE;
  } else {
    langToggleUrl = '';
  }

  // ── Bilingual UI strings ──
  const T = IS_ARABIC ? {
    skipLink: 'تخطي إلى المحتوى',
    brandName: 'أشرف الدسوقي',
    brandTitle: 'نظام إدارة المسيرة التنفيذية',
    dashboard: 'الرئيسية',
    services: 'الخدمات',
    servicesOverview: 'نظرة عامة',
    projectControls: 'التحكم بالمشاريع',
    pmoLeadership: 'قيادة مكتب إدارة المشاريع',
    telecommunications: 'الاتصالات',
    digitalTransformation: 'التحول الرقمي',
    leadership: 'القيادة',
    softwareTools: 'البرمجيات والأدوات',
    experience: 'المسيرة المهنية',
    professionalExperience: 'الخبرة المهنية',
    selectedProjects: 'المشاريع المختارة',
    allProjects: 'كل المشاريع',
    skills: 'المهارات',
    certifications: 'الشهادات',
    achievements: 'الإنجازات',
    awards: 'الجوائز',
    companies: 'الشركات',
    education: 'التعليم',
    insights: 'الرؤى والمقالات',
    articles: 'المقالات',
    projectControlsHub: 'مركز التحكم بالمشاريع',
    ftthHub: 'مركز FTTH',
    toolsCalculators: 'الأدوات والحاسبات',
    resourcesDownloads: 'الموارد والتحميلات',
    about: 'نبذة',
    aboutAshraf: 'عن أشرف',
    professionalProfile: 'الملف التنفيذي',
    careerBackground: 'الخلفية المهنية',
    contact: 'تواصل',
    search: '🔍 بحث',
    searchPlaceholder: 'ابحث في الخبرة، المشاريع، المهارات، الشهادات…',
    downloads: 'التحميلات',
    discussProject: 'ناقش مشروعاً',
    langToggle: 'English 🌐',
    langToggleAria: 'التبديل إلى الإنجليزية',
    backToTop: '↑',
    footerBrand: 'المهندس أشرف إبراهيم الدسوقي، PMP®',
    footerDesc: 'مدير المشاريع | رئيس مكتب إدارة المشاريع والتحكم بالمشاريع | قائد الاتصالات والبنية الرقمية. نظام إدارة المسيرة التنفيذية هو قاعدة المعرفة الرقمية الدائمة لمسيرتي المهنية.',
    footerNav: 'التنقل',
    footerExpertise: 'مجالات الخبرة',
    footerResources: 'المصادر والرؤى',
    footerProfile: 'الملف والمسيرة',
    footerSearch: 'بحث',
    footerRights: '© ' + new Date().getFullYear() + ' أشرف إبراهيم الدسوقي، PMP® – جميع الحقوق محفوظة',
    footerVersion: 'نظام إدارة المسيرة التنفيذية v1.0'
  } : {
    skipLink: 'Skip to main content',
    brandName: 'Ashraf El Desoky',
    brandTitle: 'Executive Career Management System',
    dashboard: 'Home',
    services: 'Services',
    servicesOverview: 'Services Overview',
    projectControls: 'Project Controls',
    pmoLeadership: 'PMO Leadership',
    telecommunications: 'Telecommunications',
    digitalTransformation: 'Digital Transformation',
    leadership: 'Leadership',
    softwareTools: 'Software & Tools',
    experience: 'Experience',
    professionalExperience: 'Professional Experience',
    selectedProjects: 'Selected Projects',
    allProjects: 'All Projects',
    skills: 'Skills',
    certifications: 'Certifications',
    achievements: 'Achievements',
    awards: 'Awards',
    companies: 'Companies',
    education: 'Education',
    insights: 'Insights',
    articles: 'Articles',
    projectControlsHub: 'Project Controls Hub',
    ftthHub: 'FTTH Hub',
    toolsCalculators: 'Tools & Calculators',
    resourcesDownloads: 'Resources & Downloads',
    about: 'About',
    aboutAshraf: 'About Ashraf',
    professionalProfile: 'Professional Profile',
    careerBackground: 'Career Background',
    contact: 'Contact',
    search: '🔍 Search',
    searchPlaceholder: 'Search experience, projects, skills, certifications…',
    downloads: 'Downloads',
    discussProject: 'Discuss a Project',
    langToggle: 'العربية 🌐',
    langToggleAria: 'Switch to Arabic',
    backToTop: '↑',
    footerBrand: 'Ashraf Ibrahim El Desoky, PMP®',
    footerDesc: 'Projects Director | PMO & Project Controls Executive | Telecommunications & Digital Infrastructure Leader. This Executive Career Management System is the permanent digital knowledge base for my professional career.',
    footerNav: 'Navigation',
    footerExpertise: 'Expertise',
    footerResources: 'Insights & Resources',
    footerProfile: 'Profile & Career',
    footerSearch: 'Search',
    footerRights: '© ' + new Date().getFullYear() + ' Ashraf Ibrahim El Desoky, PMP® – All Rights Reserved',
    footerVersion: 'Executive Career Management System v1.0'
  };

  const NAV_HTML = `
<a class="skip-link" href="#main-content">${T.skipLink}</a>
<div class="page-progress" role="progressbar" aria-label="Page scroll progress"></div>

<nav class="ecms-nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="${NAV_BASE}index.html" class="nav-brand" aria-label="${T.dashboard}">
      <div class="brand-icon" aria-hidden="true">AE</div>
      <div class="brand-text">
        <span class="brand-name">${T.brandName}</span>
        <span class="brand-title">${T.brandTitle}</span>
      </div>
    </a>

    <ul class="nav-links" id="navLinks" role="menubar">
      <li role="none"><a href="${NAV_BASE}index.html" role="menuitem" data-active="index.html">${T.dashboard}</a></li>

      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true" data-active="services.html,project-controls.html,pmo.html,telecommunications.html,digital-transformation.html,leadership.html,software.html">${T.services}</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="${NAV_BASE}services.html" role="menuitem" data-active="services.html">${T.servicesOverview}</a></li>
          <li><a href="${NAV_BASE}project-controls.html" role="menuitem" data-active="project-controls.html">${T.projectControls}</a></li>
          <li><a href="${NAV_BASE}pmo.html" role="menuitem" data-active="pmo.html">${T.pmoLeadership}</a></li>
          <li><a href="${NAV_BASE}telecommunications.html" role="menuitem" data-active="telecommunications.html">${T.telecommunications}</a></li>
          <li><a href="${NAV_BASE}digital-transformation.html" role="menuitem" data-active="digital-transformation.html">${T.digitalTransformation}</a></li>
          <li><a href="${NAV_BASE}leadership.html" role="menuitem" data-active="leadership.html">${T.leadership}</a></li>
          <li><a href="${NAV_BASE}software.html" role="menuitem" data-active="software.html">${T.softwareTools}</a></li>
        </ul>
      </li>

      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true" data-active="career.html,projects.html,featured-projects.html,companies.html,achievements.html,skills.html,education.html,certifications.html,awards.html">${T.experience}</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="${NAV_BASE}career.html" role="menuitem" data-active="career.html">${T.professionalExperience}</a></li>
          <li><a href="${NAV_BASE}featured-projects.html" role="menuitem" data-active="featured-projects.html">${T.selectedProjects}</a></li>
          <li><a href="${NAV_BASE}projects.html" role="menuitem" data-active="projects.html">${T.allProjects}</a></li>
          <li><a href="${NAV_BASE}skills.html" role="menuitem" data-active="skills.html">${T.skills}</a></li>
          <li><a href="${NAV_BASE}certifications.html" role="menuitem" data-active="certifications.html">${T.certifications}</a></li>
          <li><a href="${NAV_BASE}achievements.html" role="menuitem" data-active="achievements.html">${T.achievements}</a></li>
          <li><a href="${NAV_BASE}awards.html" role="menuitem" data-active="awards.html">${T.awards}</a></li>
          <li><a href="${NAV_BASE}companies.html" role="menuitem" data-active="companies.html">${T.companies}</a></li>
          <li><a href="${NAV_BASE}education.html" role="menuitem" data-active="education.html">${T.education}</a></li>
        </ul>
      </li>

      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true" data-active="insights.html,downloads.html">${T.insights}</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="${NAV_BASE}articles/index.html" role="menuitem">${T.articles}</a></li>
          <li><a href="${NAV_BASE}project-controls-hub/index.html" role="menuitem">${T.projectControlsHub}</a></li>
          <li><a href="${NAV_BASE}ftth/index.html" role="menuitem">${T.ftthHub}</a></li>
          <li><a href="${NAV_BASE}software.html" role="menuitem" data-active="software.html">${T.toolsCalculators}</a></li>
          <li><a href="${NAV_BASE}downloads.html" role="menuitem" data-active="downloads.html">${T.resourcesDownloads}</a></li>
          <li><a href="${NAV_BASE}search.html" role="menuitem" data-active="search.html">${T.search}</a></li>
        </ul>
      </li>

      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true" data-active="about.html,career.html">${T.about}</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="${NAV_BASE}about.html" role="menuitem" data-active="about.html">${T.aboutAshraf}</a></li>
          <li><a href="${NAV_BASE}career.html" role="menuitem" data-active="career.html">${T.careerBackground}</a></li>
          <li><a href="${NAV_BASE}about.html" role="menuitem">${T.professionalProfile}</a></li>
        </ul>
      </li>

      <li role="none"><a href="${NAV_BASE}contact.html" role="menuitem" data-active="contact.html">${T.contact}</a></li>
    </ul>

    <div class="nav-actions">
      <a href="${NAV_BASE}contact.html" class="btn-nav btn-nav-cta" aria-label="${T.discussProject}">${T.discussProject}</a>
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
          <li><a href="${NAV_BASE}index.html">${T.dashboard}</a></li>
          <li><a href="${NAV_BASE}services.html">${T.services}</a></li>
          <li><a href="${NAV_BASE}career.html">${T.experience}</a></li>
          <li><a href="${NAV_BASE}insights.html">${T.insights}</a></li>
          <li><a href="${NAV_BASE}about.html">${T.about}</a></li>
          <li><a href="${NAV_BASE}contact.html">${T.contact}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">${T.footerExpertise}</div>
        <ul class="footer-links">
          <li><a href="${NAV_BASE}services.html">${T.servicesOverview}</a></li>
          <li><a href="${NAV_BASE}project-controls.html">${T.projectControls}</a></li>
          <li><a href="${NAV_BASE}pmo.html">${T.pmoLeadership}</a></li>
          <li><a href="${NAV_BASE}telecommunications.html">${T.telecommunications}</a></li>
          <li><a href="${NAV_BASE}digital-transformation.html">${T.digitalTransformation}</a></li>
          <li><a href="${NAV_BASE}leadership.html">${T.leadership}</a></li>
          <li><a href="${NAV_BASE}software.html">${T.softwareTools}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">${T.footerResources}</div>
        <ul class="footer-links">
          <li><a href="${NAV_BASE}articles/index.html">${T.articles}</a></li>
          <li><a href="${NAV_BASE}project-controls-hub/index.html">${T.projectControlsHub}</a></li>
          <li><a href="${NAV_BASE}ftth/index.html">${T.ftthHub}</a></li>
          <li><a href="${NAV_BASE}software.html">${T.toolsCalculators}</a></li>
          <li><a href="${NAV_BASE}downloads.html">${T.resourcesDownloads}</a></li>
          <li><a href="${NAV_BASE}search.html">${T.footerSearch}</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">${T.footerProfile}</div>
        <ul class="footer-links">
          <li><a href="${NAV_BASE}about.html">${T.aboutAshraf}</a></li>
          <li><a href="${NAV_BASE}career.html">${T.professionalExperience}</a></li>
          <li><a href="${NAV_BASE}featured-projects.html">${T.selectedProjects}</a></li>
          <li><a href="${NAV_BASE}skills.html">${T.skills}</a></li>
          <li><a href="${NAV_BASE}certifications.html">${T.certifications}</a></li>
          <li><a href="${NAV_BASE}achievements.html">${T.achievements}</a></li>
          <li><a href="${NAV_BASE}awards.html">${T.awards}</a></li>
          <li><a href="${NAV_BASE}companies.html">${T.companies}</a></li>
          <li><a href="${NAV_BASE}education.html">${T.education}</a></li>
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
