/* ============================================================
   Articles Center – Global Configuration
   ============================================================ */

const ARTICLES_CONFIG = {
  /* Admin password — only to prevent visitors from opening the dashboard */
  ADMIN_PASSWORD: 'Ashraf@2026!',

  /* Site base URL (no trailing slash) */
  SITE_URL: 'https://www.ashraf-eldesoky.space',

  /* GitHub repo for direct commits from dashboard */
  GITHUB_REPO: 'ashrafedes/profileweb-render',
  GITHUB_BRANCH: 'main',
  GITHUB_TOKEN: '',  /* Paste your GitHub Personal Access Token here (repo scope) */

  /* Articles per page on the listing page */
  ARTICLES_PER_PAGE: 6,

  /* Image settings */
  IMAGE: {
    QUALITY: 0.82,
    MAX_WIDTH: 1600,
    THUMBNAIL_WIDTH: 480,
    FORMAT: 'webp'
  },

  /* Author defaults */
  DEFAULT_AUTHOR: 'Ashraf Ibrahim El Desoky',

  /* Categories (used for filter UI) */
  CATEGORIES: [
    'Project Controls',
    'Telecommunications',
    'PMO',
    'Digital Transformation',
    'Leadership',
    'PMP'
  ],

  /* AI Translation placeholder — wire up your provider here later */
  AI_TRANSLATE_ENDPOINT: '',

  /* Paths */
  PATHS: {
    JSON: '/articles/articles.json',
    IMAGES: '/assets/images/articles/',
    SITEMAP: '/sitemap.xml',
    RSS: '/rss.xml'
  }
};

/* Prevent direct modification in production console */
if (typeof window !== 'undefined') {
  window.ARTICLES_CONFIG = ARTICLES_CONFIG;
}
