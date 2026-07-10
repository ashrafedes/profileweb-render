/* ============================================================
   ECMS – Shared HTML Components (Nav + Footer)
   Injected at runtime for DRY page builds
   ============================================================ */

'use strict';

const NAV_HTML = `
<a class="skip-link" href="#main-content">Skip to main content</a>
<div class="page-progress" role="progressbar" aria-label="Page scroll progress"></div>

<nav class="ecms-nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="index.html" class="nav-brand" aria-label="ECMS Home">
      <div class="brand-icon" aria-hidden="true">AE</div>
      <div class="brand-text">
        <span class="brand-name">Ashraf El Desoky</span>
        <span class="brand-title">Executive Career Management System</span>
      </div>
    </a>

    <ul class="nav-links" id="navLinks" role="menubar">
      <li role="none"><a href="index.html" role="menuitem">Dashboard</a></li>
      <li role="none"><a href="about.html" role="menuitem">About</a></li>
      <li role="none"><a href="career.html" role="menuitem">Experience</a></li>
      <li role="none"><a href="projects.html" role="menuitem">Projects</a></li>
      <li role="none"><a href="skills.html" role="menuitem">Skills</a></li>
      <li role="none" class="nav-dropdown-wrap">
        <button class="nav-dropdown-btn" aria-expanded="false" aria-haspopup="true">More ▾</button>
        <ul class="nav-dropdown" role="menu">
          <li><a href="companies.html" role="menuitem">Companies</a></li>
          <li><a href="achievements.html" role="menuitem">Achievements</a></li>
          <li><a href="pmo.html" role="menuitem">PMO Leadership</a></li>
          <li><a href="telecommunications.html" role="menuitem">Telecommunications</a></li>
          <li><a href="project-controls.html" role="menuitem">Project Controls</a></li>
          <li><a href="digital-transformation.html" role="menuitem">Digital Transformation</a></li>
          <li><a href="leadership.html" role="menuitem">Leadership</a></li>
          <li><a href="software.html" role="menuitem">Software</a></li>
          <li><a href="certifications.html" role="menuitem">Certifications</a></li>
          <li><a href="education.html" role="menuitem">Education</a></li>
          <li><a href="awards.html" role="menuitem">Awards</a></li>
        </ul>
      </li>
      <li role="none"><a href="downloads.html" role="menuitem">Downloads</a></li>
      <li role="none"><a href="contact.html" role="menuitem">Contact</a></li>
    </ul>

    <div class="nav-actions">
      <button class="btn-nav btn-nav-search" data-search-open aria-label="Search (Ctrl+K)">
        🔍 Search
      </button>
      <button class="btn-i18n-toggle" id="i18n-toggle" aria-label="Switch language" style="background:none;border:1px solid var(--border);border-radius:var(--radius-sm);padding:0.35rem 0.6rem;font-size:0.78rem;font-weight:600;cursor:pointer;color:var(--text);transition:var(--transition);">العربية 🌐</button>
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
      <input type="search" id="searchInput" placeholder="Search experience, projects, skills, certifications…" autocomplete="off" aria-label="Search">
      <kbd style="font-size:0.7rem;color:var(--text-muted);border:1px solid var(--border);padding:2px 6px;border-radius:4px;">ESC</kbd>
    </div>
    <div class="search-results" id="searchResults" role="listbox"></div>
  </div>
</div>

<button id="backToTop" aria-label="Back to top" title="Back to top">↑</button>
`;

const FOOTER_HTML = `
<footer class="ecms-footer" role="contentinfo">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <div class="brand-name">Ashraf Ibrahim El Desoky, PMP®</div>
        <p>Projects Director | PMO & Project Controls Executive | Telecommunications & Digital Infrastructure Leader. This Executive Career Management System is the permanent digital knowledge base for my professional career.</p>
      </div>
      <div>
        <div class="footer-col-title">Navigation</div>
        <ul class="footer-links">
          <li><a href="index.html">Dashboard</a></li>
          <li><a href="about.html">About</a></li>
          <li><a href="career.html">Experience</a></li>
          <li><a href="companies.html">Companies</a></li>
          <li><a href="projects.html">Projects</a></li>
          <li><a href="achievements.html">Achievements</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">Expertise</div>
        <ul class="footer-links">
          <li><a href="pmo.html">PMO Leadership</a></li>
          <li><a href="project-controls.html">Project Controls</a></li>
          <li><a href="telecommunications.html">Telecommunications</a></li>
          <li><a href="digital-transformation.html">Digital Transformation</a></li>
          <li><a href="leadership.html">Leadership</a></li>
          <li><a href="skills.html">All Skills</a></li>
        </ul>
      </div>
      <div>
        <div class="footer-col-title">Resources</div>
        <ul class="footer-links">
          <li><a href="education.html">Education</a></li>
          <li><a href="certifications.html">Certifications</a></li>
          <li><a href="awards.html">Awards</a></li>
          <li><a href="downloads.html">Downloads</a></li>
          <li><a href="search.html">Search</a></li>
          <li><a href="contact.html">Contact</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <span>© ${new Date().getFullYear()} Ashraf Ibrahim El Desoky, PMP® – All Rights Reserved</span>
      <span>Executive Career Management System v1.0</span>
    </div>
  </div>
</footer>
`;

function injectComponents() {
  const navTarget = document.getElementById('ecms-nav-inject');
  if (navTarget) navTarget.outerHTML = NAV_HTML;

  const footerTarget = document.getElementById('ecms-footer-inject');
  if (footerTarget) footerTarget.outerHTML = FOOTER_HTML;

  // Re-apply i18n after nav/footer injection
  if (window.I18N) {
    setTimeout(function() { I18N.refresh(); }, 0);
  }
}

document.addEventListener('DOMContentLoaded', injectComponents);
