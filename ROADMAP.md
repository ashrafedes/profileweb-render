# Website Transformation Roadmap v2
## From CV Webpage → Bilingual Engineering Marketing Showcase
**Target: ashraf-eldesoky.space**

---

## Status: PLANNED (Not Yet Implemented)
*Last updated: 2026-07-10*

---

## 1. STATIC SYSTEM ARCHITECTURE

| Principle | Spec |
|-----------|------|
| **Deployment** | 100% Client-Side Static — Render Free Tier, zero cold-start latency |
| **Logic** | Vanilla JavaScript only — no Node.js, no backend, no database |
| **Primary page** | `index.html` → Arabic RTL layout (`dir="rtl"`) |
| **Secondary page** | `en.html` → English LTR layout (`dir="ltr"`) |
| **Existing assets** | Retain all paths: `/assets/downloads/`, `/assets/images/`, `/assets/icons/` |

### Known Asset URLs
| Asset | Path / URL |
|-------|-----------|
| Master CV PDF | `assets/downloads/Ashraf_El_Desoky_Master_CV_Full.pdf` |
| PMP Certificate | `assets/downloads/PMP_Certificate_Ashraf_ElDesoky.pdf` |
| Petty Cash Marketing Page | https://pettycash-marketing.web.app/ |
| Petty Cash SaaS App | https://pattycashsystem.web.app/ |

---

## 2. DESIGN SYSTEM

| Element | Spec |
|---------|------|
| **Base background** | `#0A1128` / `#1C2541` — Deep Corporate Slate/Navy |
| **Body text** | Ice Blue / Light Silver (`#CBD5E1` / `#E2E8F0`) |
| **Accent / CTA** | `#10B981` Emerald Green or `#06B6D4` Neon Cyan |
| **Warning / Over budget** | Crimson Red (`#EF4444`) |
| **Arabic font** | Cairo or Tajawal — Google Fonts |
| **English font** | Inter or Roboto — Google Fonts |
| **Component style** | Tailwind CSS utility classes, glassmorphism navbar, micro-interactions |
| **Layout** | CSS Grid + Flexbox, fully responsive: Mobile / Tablet / Desktop |

---

## 3. PAGE SECTIONS (Both `index.html` & `en.html`)

### Section 1 — Global Navbar (Glassmorphism)
- Sticky top nav: branding "Eng. Ashraf El Desoky"
- Anchor links: `[SaaS Products]` `[EVM Calculator]` `[Case Studies]` `[Resume]`
- Language toggle button:
  - On `index.html` → **"English 🌐"** links to `en.html`
  - On `en.html` → **"العربية 🌐"** links to `index.html`

### Section 2 — Hero (Solution Architect Value Prop)

**Arabic (`index.html`):**
- Headline: `المهندس أشرف الدسوقي | قيادة التحكم بالمشاريع برؤية رقمية ومؤتمتة`
- Sub: `خبير إدارة والتحكم بالمشاريع (Project Control) والبنية التحتية والاتصالات بالمملكة لأكثر من 25 عاماً. لا أدير المشاريع بالطرق التقليدية، بل أبتكر الأنظمة الرقمية وأتمتة مكاتب الـ PMO لضبط الأداء، تقليل الهدر المالي، وحماية أرباح المشاريع الكبرى.`

**English (`en.html`):**
- Headline: `Eng. Ashraf El Desoky | Project Control & Digital PMO Leader`
- Sub: `Over 25 years of engineering leadership in project controls, telecom, and infrastructure across KSA. Bridging traditional PMO methodologies with custom automated systems, local RAG architectures, and centralized cloud platforms.`

**CTA Buttons:**
- Primary: **`[Explore Smart Tools]`** → smooth scroll to Section 4 (EVM)
- Secondary: **`[Download CV PDF]`** → `assets/downloads/Ashraf_El_Desoky_Master_CV_Full.pdf`

### Section 3 — Live SaaS Products Showcase

**Card 1: Petty Cash Management SaaS Platform**
- Description: A complete dual-layer SaaS ecosystem solving site expense leaks, minimizing manual paperwork delays, and giving corporate leadership a live data pipeline of decentralised spending.
- Button 1: **`[View Marketing Page]`** → https://pettycash-marketing.web.app/
- Button 2: **`[Launch SaaS App]`** → https://pattycashsystem.web.app/

**Card 2: InfraFlow Enterprise Tracking System**
- Description: A highly specialized project control engine built for telecom and FTTH infrastructure rollouts, optimizing subcontractor logging and managing automated sitemap metadata validations.
- Button: **`[Learn More]`** → internal anchor or modal

### Section 4 — Interactive Client-Side EVM Calculator

**Form Inputs (numbers only):**
- Budget at Completion (BAC)
- Planned Value (PV)
- Earned Value (EV)
- Actual Cost (AC)

**Vanilla JS Formulas (on `input` event — live calculation):**
```
CV  = EV - AC
SV  = EV - PV
CPI = EV / AC
SPI = EV / PV
EAC = BAC / CPI
```

**Dynamic Status Badges:**

| Condition | Badge color | Label |
|-----------|-------------|-------|
| `CPI >= 1` | 🟢 Emerald `#10B981` | "Within Budget / ضمن الميزانية" |
| `CPI < 1` | 🔴 Crimson `#EF4444` | "Over Budget / متجاوز للميزانية" |
| `SPI >= 1` | 🟢 Emerald `#10B981` | "Ahead of Schedule / متقدم عن الجدول الزمني" |
| `SPI < 1` | 🔴 Crimson `#EF4444` | "Behind Schedule / متأخر عن الجدول الزمني" |

### Section 5 — Real-World Case Studies

**Format: Challenge ➔ Engineered Solution ➔ Measured Impact**

| Frame | Content |
|-------|---------|
| **Challenge (التحدي)** | Disconnected subcontractor reporting, unstructured data loops, and reporting latency in massive KSA FTTH rollouts |
| **Solution (الحل الهندسي)** | Deployed containerized automation (n8n + Docker/Podman) → centralized Single Source of Truth dashboard |
| **Impact (الأثر)** | Eliminated manual verification hours, accelerated executive reporting cycles, secured cross-domain data synchronization |

### Section 6 — Smart Experiential Resume & Certifications
- Visual corporate timeline: career milestones → current STC Group Fixed Network project controls
- Technical badge groups:
  - **Core Project Controls:** EVM, KPI Metrics, PMO Governance, Earned Value Analysis
  - **Tech Automation:** n8n Workflows, Podman/Docker, Local AI/RAG tooling, Client-side SaaS
- CTA download grid:
  - Master CV PDF
  - PMP Certificate
  - CCNA Certificate
  - All other professional certifications

---

## 4. IMPLEMENTATION CHECKLIST

### Phase 1 — New Landing Pages
- [ ] Create `en.html` — English LTR landing page (all 6 sections)
- [ ] Rebuild `index.html` → Arabic RTL version of same 6 sections
- [ ] Glassmorphism sticky navbar on both pages
- [ ] Language toggle button wired correctly on both pages
- [ ] Hero section with correct Arabic/English copy and CTA buttons
- [ ] Smooth scroll anchors working

### Phase 2 — Interactive Components
- [ ] EVM Calculator — Vanilla JS live calculation on `input` event
- [ ] CPI/SPI status badges — dynamic color switching
- [ ] SaaS product cards with real external links
- [ ] Case study blocks (Challenge / Solution / Impact)

### Phase 3 — Resume & Assets
- [ ] Visual timeline component
- [ ] Technical skill badge groups
- [ ] Download CTA grid (CV + Certificates)
- [ ] Verify all PDF/asset paths resolve correctly

### Phase 4 — Polish & Deploy
- [ ] Cairo/Tajawal fonts loaded for Arabic
- [ ] Inter/Roboto fonts loaded for English
- [ ] Tailwind CSS — all responsive breakpoints tested
- [ ] Dark color scheme (`#0A1128` base) consistent throughout
- [ ] Mobile hamburger menu working
- [ ] All existing specialty pages still accessible (career.html, etc.)
- [ ] Update sitemap.xml to include `en.html`
- [ ] Git commit + push → Render auto-deploy

---

## 5. FILES TO PRESERVE (Do Not Break)

- `assets/downloads/Ashraf_El_Desoky_Master_CV_Full.pdf`
- `assets/downloads/master-cv-source.html`
- `assets/images/` — all badge, OG, award images
- `assets/js/core.js`, `assets/js/components.js`
- `assets/css/main.css`
- All specialty pages: `career.html`, `projects.html`, `skills.html`, `pmo.html`, `about.html`, etc.
- `sitemap.xml`, `robots.txt`, `manifest.json`, `render.yaml`

---

## 6. TECHNICAL NOTES

- **No Tailwind CDN build step required** — use Tailwind CDN `<script>` tag for static delivery
- **RTL/LTR symmetry** — identical section structure on both pages, text direction flips via `dir` attribute
- **EVM calculator** — purely client-side, zero API calls, works offline
- **SaaS links** — open in `target="_blank"` with `rel="noopener noreferrer"`
- **Visitor counter** — already implemented on current `index.html` via hits.sh badge; carry forward to new pages

---

*Roadmap v1 created: 2026-07-10*
*Roadmap v2 updated: 2026-07-10*
