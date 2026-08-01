# MASTER PROMPT — ashraf-eldesoky.space Fix & Authority-Site Transformation

**For use in:** Cursor (agent mode)
**File purpose:** This is the single operating manual for fixing the identified technical/SEO/content weaknesses on ashraf-eldesoky.space and turning it into both (a) a strong executive personal-brand site and (b) a real content authority on Project Management, Project Controls, and FTTH/Telecom infrastructure. Read this whole file before touching any code.

---

## 0. HOW TO USE THIS FILE

1. Work through the stages **in order**. Do not skip ahead.
2. After each stage, produce a **Stage Report** (format in Section 3) and stop for approval before continuing.
3. Never break the existing executive-brand homepage narrative (Business Impact, Portfolio, EVM Calculator, Career Timeline, etc.) — it works well and should be preserved. You are adding a content/authority layer and fixing technical debt, not redesigning the personal brand from scratch.
4. Every fix must be verified by re-fetching the page as a crawler would see it (no JavaScript execution) — not just by looking at it in a browser. A fix that only "looks right" with JS enabled does not count as done.
5. Maintain both English (`/en/`) and Arabic (`/ar/`) versions for every page you touch or create.
6. Keep `/reports/CHANGELOG.md` updated with one entry per approved stage.

---

## 1. PROJECT VISION

**Site:** https://www.ashraf-eldesoky.space/

**Current state:** A well-designed, single-page executive resume site (PMP-certified Project Controls Director / PMO Executive / Programme Director) with strong credibility content (STC 10-year retention, Olympic City delivery, EVM calculator) but with real technical debt that hides content from search engines, and no independently rankable content on Project Management, Project Controls, or FTTH topics.

**Target state:** The same strong executive-brand homepage, technically fixed so every credibility signal actually renders for crawlers — PLUS a genuine content authority layer (individually-indexable articles, an FTTH knowledge hub, a Project Controls resource library) that makes this site come up in Google for real search queries in this space, not just for the owner's name.

**Two goals this site must now serve, without one undermining the other:**
1. Convert recruiters/executives who land on the homepage into a conversation ("hire me" / "work with me").
2. Rank in search for Project Management, Project Controls, PMO, EVM, and FTTH/telecom-infrastructure queries, via real standalone content.

---

## 2. CONFIRMED ISSUES TO FIX (from audit)

1. **Articles are not crawlable.** `/en/articles/` renders an empty article list in a no-JS fetch — the list is populated client-side. Crawlers likely see zero articles.
2. **No article has its own URL.** All three "Thought Leadership" cards on the homepage ("Read Article →") link to the same generic `/en/articles.html` instead of to individual article pages. No topic can independently rank.
3. **Achievement counters render as "0" without JS.** The "By the Numbers" section (Years Experience, Mega Projects, Sectors Covered, Countries, Concurrent Projects, Reporting Reduction) shows literal zeros in a no-JS fetch — a JS count-up animation with no static fallback.
4. **Meta-keywords tag is stuffed with 20+ terms** on the homepage — outdated practice, ignored by modern search engines, and a mild negative trust signal.
5. **Entire executive narrative lives on one URL** as anchor sections (`#exec-impact`, `#problems-solved`, `#differentiators`, `#exec-portfolio`, etc.) — none of these sections can independently rank or attract backlinks.
6. **Broken/fragile asset path**: at least one image is served from a filename containing a literal space (`PMP Badge.png`).
7. **No real content architecture for FTTH / Project Controls / PMO topics** — the site has service-description pages (`pmo.html`, `project-controls.html`, `telecommunications.html`, `digital-transformation.html`) but no evidence of deep, evergreen, keyword-targeted resource content, and no blog/knowledge-hub structure at all.
8. **Third-party visitor-counter badge** (Vercel) — cosmetic dependency, no real trust value, adds a tiny bit of unnecessary external risk.
9. **No schema/structured data confirmed** for Person, Organization, Article/BlogPosting, or Breadcrumb — needed both for personal-brand rich results and for article discoverability.

---

## 3. STAGE REPORT FORMAT (use after every stage)

```
## Stage [N] Report — [Stage Name]
Status: ✅ Complete / ⚠️ Partial / ❌ Blocked

### What was fixed / built
- ...

### Verification (no-JS crawler check)
- Page: [url] → Before: [what a crawler saw] → After: [what a crawler sees now]

### Before → After metrics
| KPI | Before | After | Status |
|---|---|---|---|

### Files changed / created
- ...

### Issues found (not yet fixed)
- ...

### Recommendation for next stage
- ...

### Awaiting approval to proceed to Stage [N+1]
```

---

## 4. GLOBAL RULES

- **No client-side-only content.** Anything meant to be indexed (articles, stats, key credibility numbers) must be present in the initial server-rendered HTML. JS enhancement (animations, counting-up effects) is fine ONLY as a progressive enhancement on top of real static values already in the markup.
- **Every article = its own URL, its own file, its own metadata.** No article-preview card may link to a shared generic listing page. Format: `/en/articles/[slug].html` and `/ar/articles/[slug].html`.
- **No meta-keywords stuffing.** Replace with a single, focused meta description per page (150–160 characters) written for humans, and a tightly scoped `<title>`.
- **No filenames with spaces or special characters** anywhere in `/assets/` or `/Resources/`. Use kebab-case (`pmp-badge.png`).
- **Every content page needs:** unique title, unique meta description, canonical tag, Open Graph tags, and appropriate JSON-LD schema (Article/BlogPosting for articles, Person + Organization sitewide, BreadcrumbList on all non-homepage pages, FAQPage where relevant).
- **Preserve the existing visual design system** — colors, typography, spacing already established on the homepage. New pages (articles, hub pages) must look like they belong to the same site, not a bolted-on blog.
- **Bilingual parity** — every English page built or fixed in a stage must have a matching Arabic page in that same stage, not deferred.

---

## 5. THE STAGES

---

### STAGE 1 — Crawlability & Technical Audit (verification pass, no fixes yet)
**Role:** Technical SEO Auditor

**Tasks:**
- Fetch every page on the site with JavaScript disabled (simulate a basic crawler) and record exactly what content is/isn't present.
- Specifically verify: article list on `/en/articles/` and `/ar/articles/`, the "By the Numbers" counters, and any other dynamically-injected content sitewide.
- Check every internal link for whether it points to a unique URL or a shared generic page.
- Audit all image/asset filenames for spaces, uppercase inconsistency, or special characters.
- Check current meta tags (title, description, keywords, OG, canonical) on every page.
- Check for any existing JSON-LD schema and validate it.

**Deliverables:** Full no-JS content audit, broken/shared-link audit, filename audit, meta tag audit.

**Acceptance criteria:** A definitive list of every page/section that is invisible or degraded to a crawler, with exact before-state documented (needed to prove the fix later).

---

### STAGE 2 — Fix Static Rendering of Critical Content
**Role:** Frontend Developer

**Tasks:**
- Rewrite the "By the Numbers" achievement stats so the real final numbers (25+, 6, 3, 20+, 60%, etc. — pull exact figures from the homepage's own "Executive Business Impact" section, which already has them correctly) are present in the static HTML. The count-up animation, if kept, must animate FROM the static value already in the DOM, not from zero with a JS-injected target.
- Rewrite the `/en/articles/` and `/ar/articles/` pages so the article list is present in server-rendered/static HTML (a JS-powered search/filter UI on top of that static list is fine — the base list must not depend on JS to exist).
- Verify with a no-JS fetch that both fixes hold.

**Deliverables:** Fixed homepage stats section, fixed articles listing pages (even if the article pages themselves don't exist yet — build the correct empty/placeholder-free structure first).

**Acceptance criteria:** No-JS fetch of the homepage shows real numbers, not zeros. No-JS fetch of the articles index shows actual article titles/links (once Stage 4 populates them) or, at minimum, correct static markup ready to receive them.

---

### STAGE 3 — Site-Wide Technical Cleanup
**Role:** Technical SEO / Frontend Developer

**Tasks:**
- Rename all asset files with spaces or inconsistent casing to kebab-case; update every reference sitewide.
- Replace the meta-keywords tag sitewide with a focused, unique meta description per page.
- Add/verify canonical tags, Open Graph, and Twitter Card tags on every page.
- Add JSON-LD: `Person` schema (for Ashraf himself) and `Organization`/`ProfilePage` schema on the homepage; `BreadcrumbList` on every non-homepage page.
- Remove or replace the third-party visitor-counter badge with either nothing, or a first-party, privacy-respecting alternative if a "social proof" number is wanted.
- Validate everything in Google's Rich Results Test equivalent checks (structure only — you don't have live Search Console access, so validate schema syntax and required fields).

**Deliverables:** Clean asset filenames, unique meta descriptions sitewide, canonical/OG/Twitter tags sitewide, Person/Organization/Breadcrumb schema.

**Acceptance criteria:** Zero filenames with spaces/special characters; zero duplicate meta descriptions; zero schema syntax errors.

---

### STAGE 4 — Article Architecture: Give Every Article a Real URL
**Role:** Technical Architect + Frontend Developer

**Tasks:**
- Design the article URL and file structure: `/en/articles/[slug].html` and `/ar/articles/[slug].html`, each with its own title, meta description, canonical, OG tags, and `BlogPosting`/`Article` JSON-LD schema.
- Build the article page template (matching the site's existing visual system): header/hero with title + reading time + category, body content area, author box (Ashraf's credentials, reused component), related-articles module, CTA back to relevant homepage section (e.g., an FTTH article links to the STC/FTTH portfolio piece).
- Migrate the three existing homepage-referenced topics — Risk Management Standards, Cyber Security Essentials, Business Strategy & Strategic Planning — into real standalone article pages with real URLs (if the full content already exists somewhere, migrate it; if only a stub exists, flag it and write a properly developed full article, minimum 1,000 words, in continuous prose, no filler bullet-point summarizing).
- Update every homepage "Read Article →" link to point to its specific article URL instead of the shared listing page.
- Update the articles index pages (`/en/articles/`, `/ar/articles/`) to list real links to these real pages.

**Deliverables:** Article page template, 3 migrated/rebuilt article pages (EN + AR), updated homepage links, updated article index pages.

**Acceptance criteria:** Every "Read Article" link on the homepage goes to a distinct URL; each article page independently passes the no-JS content check; each has unique schema and metadata.

---

### STAGE 5 — Information Architecture for the Content Authority Layer
**Role:** Technical Architect + SEO Manager

**Tasks:**
- Design the full authority-content structure, separate from (but linked to) the executive personal-brand pages:
  - `/en/insights/` (or reuse `/articles/`) — general PM/PMO/Leadership thought leadership
  - `/en/ftth/` or `/en/telecom/` — FTTH/FTTx/OSP knowledge hub (deep, technical, evergreen content: FTTH rollout planning, OSP design basics, subcontractor management, common FTTH project pitfalls, KSA-specific telecom infrastructure considerations)
  - `/en/project-controls/` — expand the existing service page into a real resource hub (EVM explained, KPI architecture, PMO governance frameworks, risk register templates)
  - Keep `/en/pmo.html`, `/en/project-controls.html`, `/en/telecommunications.html`, `/en/digital-transformation.html` as the "service/expertise" pages they already are, but link each one out to 3–5 deep-dive articles in the new hubs — don't turn the service pages themselves into 3,000-word articles.
- Define keyword targets per hub (Project Controls: EVM, PMO KPI dashboards, project risk registers, earned value management explained; FTTH: FTTH rollout planning, OSP design, FTTx subcontractor management, fiber network project management KSA; PM/Leadership: programme recovery, executive reporting automation, PMO governance frameworks).
- Produce a sitemap update and an internal linking plan connecting hub pages ↔ articles ↔ homepage portfolio/differentiator sections.

**Deliverables:** New sitemap, hub landing pages structure (not yet written in full), keyword-to-page mapping, internal linking plan.

**Acceptance criteria:** Every planned hub and article has an assigned URL and a place in the navigation; no orphaned sections; the executive personal-brand pages remain untouched in tone and structure.

---

### STAGE 6 — Build the FTTH & Telecom Infrastructure Knowledge Hub
**Role:** Content Writer (subject-matter voice: 25 years of hands-on FTTH/OSP telecom project delivery) + SEO Manager

**Tasks:**
- Build the FTTH hub landing page.
- Write 5–8 cornerstone articles drawing on real, specific project experience already referenced on the site (STC 10-year national FTTH rollout, Olympic City FTTH integration, New Capital fiber backbone, Egypt Railways fiber deployment) — e.g., "How National FTTH Rollouts Are Actually Planned and Controlled," "Managing 20+ Concurrent FTTH Sites Without Losing Visibility," "OSP Subcontractor Management: What Breaks at Scale," "FTTH Project Controls in Saudi Arabia: What's Different."
- Every article: full prose (no bullet-summarizing), 1,500–3,000 words, real specificity drawn from the career history already on the site, proper heading structure, internal links to the relevant homepage portfolio project and to the InfraFlow SaaS mention (since InfraFlow is explicitly built for this exact niche).
- Each article gets its own URL, metadata, and schema per the Stage 4 template.

**Deliverables:** FTTH hub landing page + 5–8 full articles (EN + AR).

**Acceptance criteria:** Each article is genuinely differentiated (no near-duplicate content between them), properly linked from the hub and from at least 2 other relevant pages, and passes the no-JS content check.

---

### STAGE 7 — Build the Project Controls & PMO Resource Hub
**Role:** Content Writer + SEO Manager

**Tasks:**
- Build the Project Controls hub landing page.
- Write 5–8 cornerstone articles: "Earned Value Management Explained (With the Same Calculator Used on This Site)," "Building a PMO Executive Dashboard That Actually Gets Used," "Cutting Reporting Time by 60%: The Automation Playbook," "Programme Recovery: Diagnosing a Project That's Fallen Behind," "Risk Registers That Protect Margin, Not Just Paperwork."
- Link the EVM article directly to the live EVM Calculator already on the homepage (`#evm`) — this is a strong, unique differentiator (a working tool, not just an explainer) and should be used as the anchor of that article.
- Same content/SEO/schema standards as Stage 6.

**Deliverables:** Project Controls hub landing page + 5–8 full articles (EN + AR).

**Acceptance criteria:** Same as Stage 6, plus a working internal link from at least one article directly into the live EVM calculator section.

---

### STAGE 8 — Internal Linking, Navigation & Homepage Integration
**Role:** UX Designer + SEO Manager

**Tasks:**
- Add the new hubs (FTTH, Project Controls, general Insights) to the main site navigation, without cluttering the existing executive-focused nav.
- Add a homepage module (or expand "Thought Leadership") that surfaces the best 3–4 hub articles with real links.
- Cross-link every hub article back to the most relevant homepage portfolio project or differentiator section, and vice versa, so recruiters and search visitors flow naturally between the "hire me" narrative and the "authority content" narrative.
- Update sitemap.xml and robots.txt.

**Deliverables:** Updated navigation, updated homepage module, full internal linking pass, updated sitemap/robots.

**Acceptance criteria:** No page is more than 3 clicks from the homepage; every hub and article is reachable from navigation, not just from other articles.

---

### STAGE 9 — Analytics & Search Console Verification
**Role:** Analytics Expert

**Tasks:**
- Confirm Google Search Console is verified for the domain; submit the updated sitemap.
- Confirm GA4 (or existing analytics) is tracking page views on the new hub/article pages specifically.
- Set up event tracking for: CV downloads, contact form submissions, EVM calculator usage, article reads (scroll depth), outbound LinkedIn clicks.
- Request indexing for the newly created article/hub pages via Search Console URL inspection.

**Deliverables:** Verified Search Console + sitemap submission, event tracking plan implemented, indexing requested for new pages.

**Acceptance criteria:** All new pages submitted for indexing; key events confirmed firing in GA4 real-time view.

---

### STAGE 10 — Final QA
**Role:** QA Lead

**Tasks:**
- Full no-JS crawl of the entire site (every page) to confirm nothing critical still depends on client-side rendering.
- Check every internal link for correctness (no more shared/generic article links).
- Validate all schema sitewide.
- Check Arabic/English parity — every new page exists in both languages with proper `hreflang` tags.
- Check mobile responsiveness and Lighthouse scores (Performance, Accessibility, Best Practices, SEO) on the homepage, one article page, and one hub page.
- Produce a final before/after comparison against the Stage 1 audit.

**Deliverables:** Final QA report, before/after comparison table, production checklist.

**Acceptance criteria:** Zero content invisible to a no-JS crawler; zero broken/shared-generic links; Lighthouse 90+ across the board on the three sampled page types; full AR/EN parity with correct `hreflang`.

---

## 6. PROJECT DASHBOARD (update at the end of every stage)

| KPI | Baseline (Stage 1) | Current | Target |
|---|---|---|---|
| Pages with content invisible to no-JS crawler | | | 0 |
| Articles with dedicated, unique URLs | 0 (all shared) | | 16+ |
| Homepage stat blocks rendering real numbers with no JS | 0 of 6 | | 6 of 6 |
| Filenames with spaces/special characters | ≥1 | | 0 |
| Pages with unique meta description | | | 100% |
| Pages with valid schema | | | 100% |
| FTTH hub articles published | 0 | | 5–8 |
| Project Controls hub articles published | 0 | | 5–8 |
| Indexed pages (Search Console) | | | matches total live pages |
| Lighthouse (homepage / article / hub) | | | 90+ / 90+ / 90+ |

---

## 7. DEFINITION OF DONE

The project is complete when:
- All 10 stages are marked Approved in the changelog.
- Every item in Section 2 ("Confirmed Issues to Fix") is verifiably resolved, with before/after proof from a no-JS fetch.
- The Project Dashboard shows Current meeting or exceeding Target for every KPI, or an explicit agreed-upon reason a target was adjusted.
- The existing executive personal-brand homepage narrative is fully intact and undiminished — this project adds an authority layer, it does not replace the personal brand.
