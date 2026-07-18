# Ashraf El Desoky – Executive Career Management System (ECMS)

**Live Site:** https://www.ashraf-eldesoky.space  
**Owner:** Ashraf Ibrahim El Desoky, PMP®  
**Contact:** ashrafede@gmail.com | +966 53 273 8987  
**LinkedIn:** https://www.linkedin.com/in/ashraf-eldesoky/

---

## What Is This?

The **ECMS** is a permanent, static digital knowledge base for Ashraf El Desoky's entire professional career. It is **not a job application website** — it is a structured career intelligence system from which all future career documents (CVs, LinkedIn profiles, biographies, interview answers, portfolios) are generated.

Built with **pure HTML5, CSS3, Bootstrap 5, Vanilla JS, and JSON**. No backend, no database, no server-side code.

---

## Project Structure

```
📁 Profileweb render/
├── index.html                    # Executive Dashboard (home)
├── about.html                    # Biography & personal profile
├── career.html                   # Full career history & timeline
├── companies.html                # All employers & organisations
├── projects.html                 # Project portfolio
├── achievements.html             # Career achievements
├── skills.html                   # Skills & competencies
├── certifications.html           # Professional certifications
├── education.html                # Education & training
├── awards.html                   # Awards & recognition
├── pmo.html                      # PMO leadership specialty page
├── telecommunications.html       # Telecom specialty page
├── project-controls.html         # Project controls specialty page
├── digital-transformation.html   # Digital transformation specialty page
├── leadership.html               # Leadership specialty page
├── software.html                 # Software & programming
├── search.html                   # Global search page
├── downloads.html                # Download centre
├── contact.html                  # Contact page
├── 404.html                      # 404 error page
├── robots.txt                    # SEO robots file
├── sitemap.xml                   # XML sitemap (19 pages)
├── manifest.json                 # PWA manifest
│
├── 📁 data/
│   └── career-knowledge-base.json    # Master AI-ready JSON knowledge base
│
├── 📁 assets/
│   ├── 📁 css/
│   │   └── main.css                  # Complete stylesheet (dark/light mode)
│   ├── 📁 js/
│   │   ├── core.js                   # Core JS (theme, search, animations)
│   │   └── components.js             # Shared nav + footer injection
│   ├── 📁 icons/
│   │   ├── favicon.ico
│   │   ├── icon-192.png
│   │   └── icon-512.png
│   ├── 📁 images/                    # Certificate images, profile photo
│   └── 📁 downloads/                 # CV PDFs and documents
│
└── 📁 Resources/                     # Source career documents (DOCX, images)
```

---

## Pages Overview

| Page | Description |
|------|-------------|
| `index.html` | Executive dashboard with stats, competencies, timeline preview |
| `about.html` | Full biography, personal info, language skills |
| `career.html` | Complete 25-year career history with filter (country) |
| `companies.html` | All 9 employers with detailed profiles |
| `projects.html` | 6 major projects with filter tabs |
| `achievements.html` | 8+ verified career milestones |
| `skills.html` | Full skills inventory with progress bars |
| `certifications.html` | PMP®, MBA Diploma, CCNA, B.Sc. |
| `education.html` | Academic qualifications and training |
| `awards.html` | Appreciation certificates and recognition |
| `pmo.html` | PMO leadership specialty |
| `telecommunications.html` | FTTH/FTTx/OSP/ISP specialty |
| `project-controls.html` | Planning, scheduling, cost control |
| `digital-transformation.html` | ERP, Power BI, SQL, VBA |
| `leadership.html` | Executive leadership profile |
| `software.html` | Full software and tools inventory |
| `search.html` | Global search across all JSON data |
| `downloads.html` | CV, certificates, document centre |
| `contact.html` | Contact info and availability |
| `404.html` | Custom error page |

---

## Technology Stack

- **HTML5** – Semantic, ARIA-accessible markup
- **CSS3** – Custom properties, dark/light mode, responsive grid
- **Bootstrap 5.3** – CDN, grid and utility base
- **Vanilla JavaScript** – No frameworks, no build tools
- **JSON** – Master knowledge base at `data/career-knowledge-base.json`
- **Google Fonts** – Inter typeface
- **Render.com** – Free static site hosting

---

## Deployment on Render (Free)

### First Deployment

1. Push this folder to a GitHub repository (public or private)
2. Go to https://dashboard.render.com → **New** → **Static Site**
3. Connect your GitHub account and select the repository
4. Configure:
   - **Name:** `ashraf-eldesoky` (or your preferred subdomain)
   - **Branch:** `main`
   - **Build Command:** *(leave blank – no build step needed)*
   - **Publish Directory:** `.` *(root of the repository)*
5. Click **Create Static Site**
6. Render will deploy and provide a URL: `https://www.ashraf-eldesoky.space`

### Redeployment

Push any changes to the `main` branch — Render auto-deploys.

### Custom Domain (Optional)

In Render dashboard → Settings → Custom Domain → add your domain and update DNS records.

---

## SEO Files

| File | Purpose |
|------|---------|
| `robots.txt` | Allow all crawlers, point to sitemap |
| `sitemap.xml` | 19-page sitemap for Google/Bing |
| `manifest.json` | PWA manifest for mobile install |

---

## Knowledge Base JSON

`data/career-knowledge-base.json` is structured for:
- **AI document generation** (CV, LinkedIn, bio, interview answers)
- **Programmatic search** (loaded by `core.js`)
- **Future integrations** (ChatGPT, Claude, API consumption)

Schema sections:
- `personal` – Contact, identity, languages
- `executiveProfile` – Summary, tagline, career highlights
- `experience` – All roles with full descriptions
- `education` – Degrees, diplomas, courses
- `certifications` – PMP, CCNA, etc.
- `awards` – Appreciation certificates
- `skills` – Technical, management, software, tools
- `projects` – Major project portfolio
- `specializations` – Domain expertise areas

---

## Features

- ✅ Dark / Light mode toggle (persisted in localStorage)
- ✅ Global search (loads JSON, searches all data, live results)
- ✅ Responsive – mobile, tablet, desktop
- ✅ WCAG 2.2 AA accessibility (ARIA roles, keyboard nav, skip links)
- ✅ SEO optimised (JSON-LD schema, Open Graph, Twitter Cards)
- ✅ PWA manifest
- ✅ Animated skill bars, counters, scroll reveal
- ✅ Filterable career history and projects
- ✅ Interactive timeline
- ✅ Modular components (nav + footer injected from JS)
- ✅ No backend, no build step, deploys as static files

---

## Maintaining the Knowledge Base

All content lives in `data/career-knowledge-base.json`. To update:

1. Open `data/career-knowledge-base.json`
2. Find the relevant section (experience, skills, certifications, etc.)
3. Add or edit the JSON data
4. Push to GitHub — site updates automatically

HTML pages pull data dynamically (search) or are hand-synced from the JSON.

---

## Adding CV PDFs

Place PDF files in `assets/downloads/`:
- `Ashraf_El_Desoky_Executive_CV.pdf`
- `Ashraf_El_Desoky_Master_CV.pdf`

These are referenced by `downloads.html`.

---

## Adding Favicon / Icons

Place icon files in `assets/icons/`:
- `favicon.ico` (16×16, 32×32)
- `icon-192.png` (192×192 PNG)
- `icon-512.png` (512×512 PNG)

---

## Data Integrity Policy

> **This system contains ONLY verified information extracted from original career documents. No achievements, dates, numbers or names have been invented or estimated. Fields marked `TODO_VERIFIED` require manual confirmation from original Arabic-language documents.**

---

*Built for Ashraf Ibrahim El Desoky, PMP® — Executive Career Management System v1.0*
