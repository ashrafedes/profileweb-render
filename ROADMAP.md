# Website Transformation Roadmap
## From CV Webpage → Bilingual Engineering Marketing Showcase
**Target: ashraf-eldesoky.space**

---

## Status: PLANNED (Not Yet Implemented)

---

## 1. CORE ARCHITECTURAL PRINCIPLES

- **Environment:** 100% Static — Render Free Tier, zero backend
- **Performance:** Client-side only — Vanilla JS, no Node.js, no database
- **File Structure:**
  - `index.html` → Arabic Landing Page (Primary, RTL, `dir="rtl"`)
  - `en.html` → English Landing Page (Secondary, LTR, `dir="ltr"`)
  - Retain all existing paths: `/assets/downloads/`, `/assets/images/`, `/assets/icons/`

---

## 2. DESIGN SYSTEM

| Element | Spec |
|---------|------|
| Base colors | `#0B132B` / `#1C2541` (Deep Corporate Slate/Blue) |
| Accent / CTA | `#10B981` Emerald Green or `#06B6D4` Vibrant Cyan |
| Text | Clean white / light gray on dark backgrounds |
| Arabic font | Cairo or Tajawal (Google Fonts) |
| English font | Inter or Roboto (Google Fonts) |
| Layout | CSS Grid + Flexbox, fully responsive (Mobile / Tablet / Desktop) |

---

## 3. PAGE SECTIONS

### A — Navigation & Language Toggle
- Fixed/sticky top nav with name/brand
- Quick anchors: `[SaaS Products]` `[EVM Tool]` `[Case Studies]` `[Resume]`
- Language switcher: `index.html` → "English 🌐" → `en.html` | `en.html` → "العربية 🌐" → `index.html`

### B — Hero Section (Value Proposition)

**Arabic (`index.html`):**
- Headline: `المهندس أشرف الدسوقي | قيادة التحكم بالمشاريع برؤية رقمية ومؤتمتة`
- Sub-headline: `خبير إدارة والتحكم بالمشاريع (Project Control) والبنية التحتية والاتصالات بالمملكة لأكثر من 25 عاماً...`

**English (`en.html`):**
- Headline: `Eng. Ashraf El Desoky | Project Control & Digital PMO Leader`
- Sub-headline: `Over 25 years of engineering expertise in project controls, telecom, and infrastructure across KSA...`

**Buttons:**
- Primary: `[Explore Smart Tools]` → smooth scroll to EVM section
- Secondary: `[Download CV PDF]` → link to pre-uploaded PDF

### C — Live SaaS Products Showcase (Card Components)

1. **Petty Cash Management SaaS**
   - Track site-level petty cash, financial workflows, real-time expense monitoring & analytics

2. **InfraFlow Tracking System**
   - Telecom/FTTH rollout tracker, automates contractor progress reports, validates sitemap data

### D — Interactive Client-Side EVM Calculator

**Inputs:**
- Budget at Completion (BAC)
- Planned Value (PV)
- Earned Value (EV)
- Actual Cost (AC)

**JS Formulas:**
```
CV  = EV - AC
SV  = EV - PV
CPI = EV / AC
SPI = EV / PV
EAC = BAC / CPI
```

**Dynamic UI:**
- `CPI >= 1` → Emerald Green badge: "Within Budget / ضمن الميزانية" + positive PMO feedback
- `CPI < 1`  → Crimson Red badge: "Over Budget / متجاوز للميزانية" + corrective actions
- Same logic for SPI: Ahead / Behind Schedule

### E — Engineering Case Studies

| Frame | Content |
|-------|---------|
| **Challenge (التحدي)** | Loose data loops, reporting latencies, unstructured subcontractor logs in FTTH rollouts |
| **Solution (الحل الهندسي)** | Automated workflows (containerized systems + n8n pipelines) → centralized single-source dashboards |
| **Impact (الأثر)** | Eliminated manual verification hours, accelerated executive reporting, secured data sync |

### F — Visual Timeline Resume & Certifications
- Corporate timeline of professional milestones (current: STC fixed-network project controls)
- Technical skill badges split into:
  - **Core Engineering:** EVM, KPI Architecture, PMO Governance
  - **Tech Automation:** n8n Workflows, Podman/Docker, Client-side SaaS development
- CTA grid: view certifications + download Master CV

---

## 4. IMPLEMENTATION CHECKLIST

- [ ] Create `index.html` — Arabic RTL landing page (full rebuild)
- [ ] Create `en.html` — English LTR landing page (full rebuild)
- [ ] Implement EVM Calculator (Vanilla JS, client-side only)
- [ ] SaaS Products section with card components
- [ ] Case Studies section (Arabic + English)
- [ ] Visual timeline component
- [ ] Language switcher between index.html ↔ en.html
- [ ] Cairo/Tajawal fonts for Arabic, Inter/Roboto for English
- [ ] Dark corporate color scheme (#0B132B base)
- [ ] Fully responsive (Mobile / Tablet / Desktop)
- [ ] Keep all existing pages (career.html, projects.html, etc.) accessible
- [ ] Update nav links to point to new structure
- [ ] Test all PDF/certificate download links

---

## 5. FILES TO PRESERVE (Do Not Break)

- `assets/downloads/Ashraf_El_Desoky_Master_CV_Full.pdf`
- `assets/downloads/master-cv-source.html`
- `assets/images/` (all badge, OG, and award images)
- `assets/js/core.js`, `assets/js/components.js`
- `assets/css/main.css`
- All specialty pages: `career.html`, `projects.html`, `skills.html`, `pmo.html`, etc.
- `sitemap.xml`, `robots.txt`, `manifest.json`

---

*Roadmap created: 2026-07-10*
