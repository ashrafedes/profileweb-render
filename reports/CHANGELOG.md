# Changelog — ashraf-eldesoky.site Fix & Authority-Site Transformation

All notable changes to this project are documented in this file.
One entry per approved stage.

---

## Stage 1 — Crawlability & Technical Audit (Verification Pass)
**Date:** 2026-08-01
**Status:** ✅ Complete

### Audit Findings

#### 1. Articles are not crawlable (CONFIRMED)
- `/en/articles/index.html` and `/ar/articles/index.html` have all content containers empty: `#articles-grid`, `#featured-article`, `#category-pills`, `#popular-topics`, `#pagination`
- All content is injected by `assets/js/articles.js` via `fetch('articles/articles.json')`
- A no-JS crawler sees zero articles on the listing pages

#### 2. Article pages themselves are not crawlable (CONFIRMED — additional finding)
- Individual article pages (e.g., `en/articles/earned-value-management.html`) have empty containers: `#article-hero`, `#article-body`, `#related-articles`
- Content is injected by `assets/js/article.js` via fetch from `articles.json`
- A no-JS crawler sees zero article content on any article page
- **Article pages DO have correct metadata in static HTML** (title, meta description, OG tags, canonical, hreflang, Article JSON-LD schema)

#### 3. Homepage "Read Article" links all point to generic page (CONFIRMED — EN only)
- EN homepage: 3 "Read Article →" links all point to `articles.html` (generic listing)
- AR homepage: 3 article links point to individual slugs BUT the slugs are WRONG:
  - `articles/risk-management-standards.html` → actual file is `risk-management-standards-project-management.html`
  - `articles/business-strategy.html` → actual file is `business-strategy-strategic-planning-guide.html`
  - `articles/cyber-security-essentials.html` → actual file is `cyber-security-essentials-guide.html`
- All 6 links are broken or non-specific

#### 4. Achievement counters (NOT AN ISSUE — already static)
- Homepage `#exec-impact` section has all 8 stats as static HTML values: 25+, 10, 20+, 60%, 6, 6, 3, 2
- No JS count-up animation found — values are in the DOM
- **No fix needed**

#### 5. Meta-keywords stuffing (CONFIRMED)
- 312 HTML files have `<meta name="keywords">` tags
- EN homepage has 20+ keywords: "Project Controls Director, PMO Director, Programme Director, Telecom Executive, Digital Transformation, Project Director, Construction Executive, Infrastructure Executive, Saudi Arabia, Riyadh, Mega Projects, Executive Leadership, FTTH, EVM, PMO Governance, Earned Value Management, PMP Certified, Project Controls Manager, PMO Executive, Construction Project Controls, Hospitality Project Manager, Egypt Project Director, project control manager, Riyadh project controls"
- Needs removal sitewide

#### 6. Executive narrative on single URL (CONFIRMED — by design)
- Sections are anchor-based: `#exec-impact`, `#problems-solved`, `#differentiators`, `#exec-portfolio`
- This is the personal-brand homepage and should remain as-is per plan
- The content authority layer (Stages 5-7) will add independently rankable pages

#### 7. Broken asset filename with spaces (CONFIRMED)
- `Resources/PMP Badge.png` — referenced in `en/index.html` (3 locations) and `ar/index.html` (2 locations)
- `Resources/cisco_ccna_Badge.png` — has uppercase `B`
- `Resources/2023-distinguished-expert.png` — has uppercase
- Many other Resources files with spaces, uppercase, Arabic characters
- Needs renaming to kebab-case + updating all references

#### 8. No content architecture for FTTH/Project Controls/PMO (CONFIRMED)
- Service pages exist: `pmo.html`, `project-controls.html`, `telecommunications.html`, `digital-transformation.html`
- No hub pages, no knowledge hub structure
- 150+ articles exist in `articles.json` but are invisible to crawlers

#### 9. Third-party visitor counter badge (CONFIRMED)
- `https://page-visitor.vercel.app/ashraf-eldesoky-space/count.svg` found on 5 pages:
  - `en/index.html`, `ar/index.html`, `en.html`, `en/featured-projects.html`, `ar/featured-projects.html`
- External dependency for cosmetic value

#### 10. Schema/structured data (PARTIAL)
- **Homepage** (`en/index.html`, `ar/index.html`): Has `Person` schema + `WebSite` schema ✅
- **Article pages**: Have `Article` JSON-LD schema ✅
- **Missing**: `BreadcrumbList` on non-homepage pages, `Organization`/`ProfilePage` on homepage
- **Missing**: `BlogPosting` schema type (using `Article` instead — acceptable but `BlogPosting` is more specific)
- Article schema is present but inline in `<head>` — needs verification of required fields

### Site Structure Summary
- **424 HTML files** total (excluding .git)
- **150+ articles** in `articles.json` with EN+AR content
- **~100 article HTML files** exist in both `en/articles/` and `ar/articles/`
- Sitemap exists with 347 lines, includes article URLs
- robots.txt exists and is correct
- RSS feed exists (`rss.xml`)

### Files Audited
- `en/index.html` (1624 lines)
- `ar/index.html` (1479 lines)
- `en/articles/index.html` (109 lines)
- `ar/articles/index.html` (111 lines)
- `en/articles/earned-value-management.html` (74 lines)
- `assets/js/articles.js` (345 lines)
- `assets/js/article.js` (466 lines)
- `articles/articles.json` (7845 lines, 150+ articles)
- `sitemap.xml` (347 lines)
- `robots.txt` (6 lines)
- `Resources/` directory (50+ files with naming issues)

### KPI Baseline
| KPI | Baseline |
|---|---|
| Pages with content invisible to no-JS crawler | 100+ (all article pages + 2 listing pages) |
| Articles with dedicated, unique URLs | 150+ exist but content is JS-rendered |
| Homepage stat blocks rendering real numbers with no JS | 8 of 8 ✅ |
| Filenames with spaces/special characters | 50+ in Resources/ |
| Pages with unique meta description | Most pages have unique descriptions ✅ |
| Pages with valid schema | Homepage + articles have schema, missing BreadcrumbList |
| FTTH hub articles published | 0 (hub doesn't exist) |
| Project Controls hub articles published | 0 (hub doesn't exist) |
| Pages with meta-keywords tag | 312 |
| Third-party visitor counter | 5 pages |

### Recommendation for next stage
Proceed to Stage 3 — Site-Wide Technical Cleanup

---

## Stage 2 — Fix Static Rendering of Critical Content
**Date:** 2026-08-01
**Status:** ✅ Complete

### What was fixed / built
- Created `_build_static.py` — Python build script that pre-renders all article content from `articles.json` into static HTML
- Generated 300 static article pages (150 EN + 150 AR) with full content in server-rendered HTML:
  - Article hero (title, category, author, date, reading time) in static HTML
  - Article body content (rendered from markdown to HTML) in static HTML
  - Article schema (JSON-LD) and BreadcrumbList schema in static HTML
  - All meta tags (title, description, OG, Twitter, canonical, hreflang) in static HTML
- Rebuilt `/en/articles/index.html` and `/ar/articles/index.html` with static article cards, featured article, category pills, and popular topics
- Updated `assets/js/articles.js` to preserve static content and only re-render on user interaction (search, filter, sort)
- Updated `assets/js/article.js` to preserve static content and only enhance (TOC, related articles, prev/next, lang switch)
- Fixed EN homepage "Read Article →" links to point to individual article URLs:
  - Risk Management → `articles/risk-management-standards-project-management.html`
  - Cyber Security → `articles/cyber-security-essentials-guide.html`
  - Business Strategy → `articles/business-strategy-strategic-planning-guide.html`
  - "Explore All Articles" → `articles/` (index page)
- Fixed AR homepage broken article links (wrong slugs corrected to match actual filenames)
- Fixed AR "Explore All Articles" link from `articles.html` to `articles/`

### Verification (no-JS crawler check)
- Article page (`/en/articles/earned-value-management.html`): Before → empty `#article-body` div → After → full article content with h2/h3/p/table elements in static HTML
- Articles index (`/en/articles/`): Before → empty `#articles-grid` div → After → 150 article cards with titles, excerpts, images, dates in static HTML
- Homepage links: Before → all 3 "Read Article" links point to generic `articles.html` → After → each links to its own unique article URL

### Files changed / created
- `_build_static.py` (new — build script)
- `assets/js/articles.js` (modified — preserve static content)
- `assets/js/article.js` (modified — preserve static content)
- `en/index.html` (modified — fixed article links)
- `ar/index.html` (modified — fixed article links)
- 300 article HTML files regenerated (EN + AR)
- 2 articles index pages regenerated (EN + AR)

### Issues found (not yet fixed)
- Meta-keywords tags still present on 312 files (Stage 3)
- Asset filenames with spaces in Resources/ (Stage 3)
- Third-party visitor counter badge on 5 pages (Stage 3)
- Missing Organization schema on homepage (Stage 3)

### Recommendation for next stage
Proceed to Stage 3 — Site-Wide Technical Cleanup
