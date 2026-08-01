#!/usr/bin/env python3
"""
Stage 5 — Information Architecture: Build hub landing pages
- /en/ftth/ and /ar/ftth/ — FTTH & Telecom Knowledge Hub
- /en/project-controls-hub/ and /ar/project-controls-hub/ — Project Controls & PMO Resource Hub
Each hub lists relevant articles with links, has proper metadata and schema.
"""
import json
import os
import html

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = 'https://www.ashraf-eldesoky.space'

def esc(s):
    if not s: return ''
    return html.escape(str(s))

def format_date(date_str, lang='en'):
    if not date_str: return ''
    months_en = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
    months_ar = ['يناير','فبراير','مارس','أبريل','مايو','يونيو','يوليو','أغسطس','سبتمبر','أكتوبر','نوفمبر','ديسمبر']
    try:
        parts = date_str.split('-')
        y, m, d = int(parts[0]), int(parts[1]), int(parts[2])
        if lang == 'ar':
            return f'{d} {months_ar[m-1]} {y}'
        return f'{months_en[m-1]} {d}, {y}'
    except:
        return date_str

def build_hub_page(hub_type, lang, articles):
    """Build a hub landing page"""
    is_ar = lang == 'ar'
    dir_attr = 'rtl' if is_ar else 'ltr'
    font_family = 'Cairo' if is_ar else 'Inter'
    font_weights = '300;400;500;600;700;800;900'
    og_locale = 'ar_SA' if is_ar else 'en_US'
    
    if hub_type == 'ftth':
        if is_ar:
            title = 'مركز معرفة شبكات الألياف البصرية (FTTH) | أشرف الدسوقي'
            meta_desc = 'دليل شامل لتخطيط وتنفيذ وإدارة مشاريع شبكات الألياف البصرية حتى المنزل (FTTH) و OSP والبنية التحتية للاتصالات في المملكة العربية السعودية.'
            h1 = 'مركز معرفة شبكات الألياف البصرية (FTTH)'
            subtitle = 'مقالات وأدلة تقنية متعمقة حول تخطيط وتنفيذ وإدارة مشاريع FTTH و OSP والبنية التحتية للاتصالات'
            hub_path = 'ftth/'
            hub_name = 'FTTH & Telecom'
            home_text = 'الرئيسية'
            hub_text = 'FTTH'
            cat_label = 'التصنيف'
            read_more = 'اقرأ المزيد'
            min_read = 'دقائق قراءة'
            by_text = 'بقلم'
            # Filter articles for FTTH hub
            relevant = [a for a in articles if not a.get('draft') and (
                a.get('category','') in ['Telecommunications', 'Network Infrastructure'] or
                any(t in (a.get('tags',[]) or []) for t in ['FTTH','Telecom','Telecommunications','5G','Fiber','OSP','Network'])
            )]
        else:
            title = 'FTTH & Telecom Infrastructure Knowledge Hub | Ashraf El Desoky'
            meta_desc = 'Comprehensive guides on planning, delivering, and managing FTTH, OSP, and telecom infrastructure projects in Saudi Arabia and the GCC.'
            h1 = 'FTTH & Telecom Infrastructure Knowledge Hub'
            subtitle = 'Deep technical guides on FTTH rollout planning, OSP design, subcontractor management, and telecom project controls'
            hub_path = 'ftth/'
            hub_name = 'FTTH & Telecom'
            home_text = 'Home'
            hub_text = 'FTTH'
            cat_label = 'Category'
            read_more = 'Read more'
            min_read = 'min read'
            by_text = 'By'
            relevant = [a for a in articles if not a.get('draft') and (
                a.get('category','') in ['Telecommunications', 'Network Infrastructure'] or
                any(t in (a.get('tags',[]) or []) for t in ['FTTH','Telecom','Telecommunications','5G','Fiber','OSP','Network'])
            )]
    else:  # project-controls
        if is_ar:
            title = 'مركز موارد ضوابط المشاريع و PMO | أشرف الدسوقي'
            meta_desc = 'أدلة شاملة لإدارة القيمة المكتسبة (EVM) وحوكمة PMO وإدارة المخاطر وضوابط المشاريع من خبير معتمد PMP®.'
            h1 = 'مركز موارد ضوابط المشاريع و PMO'
            subtitle = 'مقالات وأدلة عملية حول إدارة القيمة المكتسبة وحوكمة مكتب إدارة المشاريع وإدارة المخاطر وضوابط المشاريع'
            hub_path = 'project-controls-hub/'
            hub_name = 'Project Controls & PMO'
            home_text = 'الرئيسية'
            hub_text = 'ضوابط المشاريع'
            cat_label = 'التصنيف'
            read_more = 'اقرأ المزيد'
            min_read = 'دقائق قراءة'
            by_text = 'بقلم'
            relevant = [a for a in articles if not a.get('draft') and (
                a.get('category','') in ['Project Controls', 'PMO Leadership', 'Project Management', 'Governance', 'Resource Management', 'Risk Management'] or
                any(t in (a.get('tags',[]) or []) for t in ['EVM','PMO','Project Controls','Risk Management','Governance','PMP','Project Management'])
            )]
        else:
            title = 'Project Controls & PMO Resource Hub | Ashraf El Desoky'
            meta_desc = 'Comprehensive guides on Earned Value Management, PMO governance, risk registers, and project controls by a PMP®-certified practitioner.'
            h1 = 'Project Controls & PMO Resource Hub'
            subtitle = 'Practical guides on EVM, PMO governance, risk management, and project controls from 25+ years of field experience'
            hub_path = 'project-controls-hub/'
            hub_name = 'Project Controls & PMO'
            home_text = 'Home'
            hub_text = 'Project Controls'
            cat_label = 'Category'
            read_more = 'Read more'
            min_read = 'min read'
            by_text = 'By'
            relevant = [a for a in articles if not a.get('draft') and (
                a.get('category','') in ['Project Controls', 'PMO Leadership', 'Project Management', 'Governance', 'Resource Management', 'Risk Management'] or
                any(t in (a.get('tags',[]) or []) for t in ['EVM','PMO','Project Controls','Risk Management','Governance','PMP','Project Management'])
            )]
    
    # Sort by date descending
    relevant.sort(key=lambda a: a.get('publishDate','1970-01-01'), reverse=True)
    
    # Build article cards
    cards_html = ''
    for a in relevant:
        d = a.get(lang, a.get('en', {}))
        img = a.get('heroImage', '')
        if img:
            img_html = f'<img class="article-card-img" src="{img}" alt="{esc(d.get("title",""))}" loading="lazy">'
        else:
            img_html = '<div class="article-card-img" style="display:flex;align-items:center;justify-content:center;font-size:2rem;background:var(--bg-alt);">📝</div>'
        
        article_url = f'../articles/{a["slug"]}.html'
        cards_html += f'''
        <a href="{article_url}" class="article-card" style="text-decoration:none;color:inherit;">
          {img_html}
          <div class="article-card-body">
            <div class="article-card-cat">{esc(a.get('category',''))}</div>
            <h3>{esc(d.get('title',''))}</h3>
            <p class="excerpt">{esc(d.get('excerpt',''))}</p>
            <div class="article-card-meta">
              <span>{format_date(a.get('publishDate',''), lang)}</span>
              <span>· {a.get('readingTime','')} {min_read}</span>
            </div>
          </div>
        </a>'''
    
    url = f'{SITE_URL}/{lang}/{hub_path}'
    alt_lang = 'ar' if lang == 'en' else 'en'
    alt_url = f'{SITE_URL}/{alt_lang}/{hub_path}'
    font_style = f'<style>* {{ font-family: \'Cairo\', sans-serif; }}</style>' if is_ar else ''
    
    # BreadcrumbList schema
    breadcrumb = json.dumps({
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": home_text, "item": f"{SITE_URL}/{lang}/"},
            {"@type": "ListItem", "position": 2, "name": hub_text, "item": url}
        ]
    }, ensure_ascii=False)
    
    # CollectionPage schema
    collection_schema = json.dumps({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": h1,
        "description": meta_desc,
        "url": url,
        "inLanguage": lang,
        "isPartOf": {"@type": "WebSite", "name": "Ashraf El Desoky", "url": SITE_URL}
    }, ensure_ascii=False)
    
    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
<head>
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z6B9JDZ6F0"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){{dataLayer.push(arguments);}}
    gtag('js', new Date());
    gtag('config', 'G-Z6B9JDZ6F0');
  </script>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <meta name="author" content="Ashraf Ibrahim El Desoky">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(h1)}">
  <meta property="og:description" content="{esc(meta_desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{og_locale}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(h1)}">
  <meta name="twitter:description" content="{esc(meta_desc)}">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="{lang}" href="{url}">
  <link rel="alternate" hreflang="{alt_lang}" href="{alt_url}">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="manifest" href="../../manifest.json">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family={font_family}:wght@{font_weights}&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="../../assets/css/articles.css">
  <script type="application/ld+json">{breadcrumb}</script>
  <script type="application/ld+json">{collection_schema}</script>
</head>
<body>{font_style}
  <div id="ecms-nav-inject"></div>

  <main id="main-content" class="page-wrapper">

    <div class="articles-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumb" style="margin-bottom:1.5rem;">
          <a href="../index.html" style="color:rgba(255,255,255,0.7);">{home_text}</a>
          <span style="color:rgba(255,255,255,0.4);margin:0 0.5rem;">{'‹' if is_ar else '›'}</span>
          <span style="color:#fff;font-weight:600;">{hub_text}</span>
        </nav>
        <h1>{h1}</h1>
        <p>{subtitle}</p>
      </div>
    </div>

    <section class="section" style="padding:2.5rem 0;">
      <div class="container">
        <div class="articles-grid">
          {cards_html}
        </div>
      </div>
    </section>

  </main>

  <div id="ecms-footer-inject"></div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
  <script src="../../config.js"></script>
  <script src="../../assets/js/i18n.js?v=2"></script>
  <script src="../../assets/js/components.js?v=4"></script>
  <script src="../../assets/js/core.js?v=6"></script>
</body>
</html>'''


def main():
    with open(os.path.join(BASE_DIR, 'articles', 'articles.json'), 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    print(f'Loaded {len(articles)} articles')
    
    # Build FTTH hub
    for lang in ['en', 'ar']:
        hub_dir = os.path.join(BASE_DIR, lang, 'ftth')
        os.makedirs(hub_dir, exist_ok=True)
        html = build_hub_page('ftth', lang, articles)
        with open(os.path.join(hub_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Built FTTH hub: {lang}/ftth/index.html')
    
    # Build Project Controls hub
    for lang in ['en', 'ar']:
        hub_dir = os.path.join(BASE_DIR, lang, 'project-controls-hub')
        os.makedirs(hub_dir, exist_ok=True)
        html = build_hub_page('project-controls', lang, articles)
        with open(os.path.join(hub_dir, 'index.html'), 'w', encoding='utf-8') as f:
            f.write(html)
        print(f'Built Project Controls hub: {lang}/project-controls-hub/index.html')
    
    print('\nDone! Stage 5 hub pages built.')


if __name__ == '__main__':
    main()
