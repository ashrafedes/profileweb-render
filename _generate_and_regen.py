import json, os, html
from datetime import datetime
from email.utils import formatdate

SITE_URL = 'https://www.ashraf-eldesoky.space'
ARTICLES_JSON = 'articles/articles.json'

def load_articles():
    with open(ARTICLES_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def esc(s):
    return html.escape(s, quote=True)

def gen_en_page(article):
    slug = article['slug']
    en = article['en']
    title = en['title']
    desc = en['excerpt']
    keywords = ', '.join(en.get('keywords', []))
    pub = article['publishDate']
    upd = article.get('updatedDate', pub)
    hero = article.get('heroImage', '')
    hero_url = f"{SITE_URL}{hero}" if hero else ''
    canonical = f"{SITE_URL}/en/articles/{slug}.html"
    ar_url = f"{SITE_URL}/ar/articles/{slug}.html"

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Person", "name": article.get('author', 'Ashraf Ibrahim El Desoky')},
        "datePublished": pub,
        "dateModified": upd,
        "image": hero,
        "publisher": {"@type": "Person", "name": "Ashraf Ibrahim El Desoky"},
        "mainEntityOfPage": canonical,
        "inLanguage": "en"
    }, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="en" dir="ltr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)} | Ashraf El Desoky</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="keywords" content="{esc(keywords)}">
  <meta name="author" content="Ashraf Ibrahim El Desoky">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{hero_url}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="en_US">
  <meta property="article:published_time" content="{pub}">
  <meta property="article:modified_time" content="{upd}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)} | Ashraf El Desoky">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{hero_url}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{canonical}">
  <link rel="alternate" hreflang="ar" href="{ar_url}">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="manifest" href="../../manifest.json">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="../../assets/css/articles.css">
  <script type="application/ld+json">{ld_json}</script>
</head>
<body>
  <div id="ecms-nav-inject"></div>

  <main id="main-content" class="page-wrapper" style="padding-top:0;">
    <div class="article-hero" id="article-hero"></div>

    <section class="section" style="padding:2.5rem 0;">
      <div class="container">
        <div id="article-body"></div>
      </div>
    </section>

    <section class="section" style="padding:0 0 2rem;">
      <div class="container" id="related-articles"></div>
    </section>

    <section class="section" style="padding:0 0 3rem;">
      <div class="container" id="newsletter-section"></div>
    </section>
  </main>

  <div id="ecms-footer-inject"></div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
  <script src="../../config.js"></script>
  <script src="../../assets/js/i18n.js?v=2"></script>
  <script src="../../assets/js/components.js?v=4"></script>
  <script src="../../assets/js/core.js?v=6"></script>
  <script src="../../assets/js/article.js?v=7"></script>
</body>
</html>
"""

def gen_ar_page(article):
    slug = article['slug']
    ar = article['ar']
    title = ar['title']
    desc = ar['excerpt']
    keywords = ', '.join(ar.get('keywords', []))
    pub = article['publishDate']
    upd = article.get('updatedDate', pub)
    hero = article.get('heroImage', '')
    hero_url = f"{SITE_URL}{hero}" if hero else ''
    canonical = f"{SITE_URL}/ar/articles/{slug}.html"
    en_url = f"{SITE_URL}/en/articles/{slug}.html"

    ld_json = json.dumps({
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": title,
        "description": desc,
        "author": {"@type": "Person", "name": article.get('author', 'Ashraf Ibrahim El Desoky')},
        "datePublished": pub,
        "dateModified": upd,
        "image": hero,
        "publisher": {"@type": "Person", "name": "Ashraf Ibrahim El Desoky"},
        "mainEntityOfPage": canonical,
        "inLanguage": "ar"
    }, ensure_ascii=False)

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{esc(title)} | أشرف الدسوقي</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="keywords" content="{esc(keywords)}">
  <meta name="author" content="Ashraf Ibrahim El Desoky">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(title)}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{canonical}">
  <meta property="og:image" content="{hero_url}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="ar_SA">
  <meta property="article:published_time" content="{pub}">
  <meta property="article:modified_time" content="{upd}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(title)} | أشرف الدسوقي">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{hero_url}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="ar" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{en_url}">
  <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
  <link rel="manifest" href="../../manifest.json">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="stylesheet" href="../../assets/css/main.css">
  <link rel="stylesheet" href="../../assets/css/articles.css">
  <style>* {{ font-family: 'Cairo', sans-serif; }}</style>
  <script type="application/ld+json">{ld_json}</script>
</head>
<body>
  <div id="ecms-nav-inject"></div>

  <main id="main-content" class="page-wrapper" style="padding-top:0;">
    <div class="article-hero" id="article-hero"></div>

    <section class="section" style="padding:2.5rem 0;">
      <div class="container">
        <div id="article-body"></div>
      </div>
    </section>

    <section class="section" style="padding:0 0 2rem;">
      <div class="container" id="related-articles"></div>
    </section>

    <section class="section" style="padding:0 0 3rem;">
      <div class="container" id="newsletter-section"></div>
    </section>
  </main>

  <div id="ecms-footer-inject"></div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
  <script src="../../config.js"></script>
  <script src="../../assets/js/i18n.js?v=2"></script>
  <script src="../../assets/js/components.js?v=4"></script>
  <script src="../../assets/js/core.js?v=6"></script>
  <script src="../../assets/js/article.js?v=7"></script>
</body>
</html>
"""

def generate_static_pages(articles):
    en_dir = 'en/articles'
    ar_dir = 'ar/articles'
    os.makedirs(en_dir, exist_ok=True)
    os.makedirs(ar_dir, exist_ok=True)
    count = 0
    for a in articles:
        if a.get('draft'):
            continue
        slug = a['slug']
        en_path = os.path.join(en_dir, f'{slug}.html')
        ar_path = os.path.join(ar_dir, f'{slug}.html')
        if not os.path.exists(en_path):
            with open(en_path, 'w', encoding='utf-8') as f:
                f.write(gen_en_page(a))
            count += 1
        if not os.path.exists(ar_path):
            with open(ar_path, 'w', encoding='utf-8') as f:
                f.write(gen_ar_page(a))
            count += 1
    print(f"Generated {count} new static HTML pages")

def regenerate_sitemap(articles):
    lines = ['<?xml version="1.0" encoding="UTF-8"?>']
    lines.append('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">')

    static_pages = [
        ('/', 'weekly', '1.0'),
        ('/en.html', 'weekly', '0.9'),
        ('/about.html', 'monthly', '0.95'),
        ('/career.html', 'monthly', '0.95'),
        ('/featured-projects.html', 'monthly', '0.95'),
        ('/projects.html', 'monthly', '0.95'),
        ('/skills.html', 'monthly', '0.95'),
        ('/achievements.html', 'monthly', '0.90'),
        ('/certifications.html', 'yearly', '0.90'),
        ('/education.html', 'yearly', '0.90'),
        ('/awards.html', 'yearly', '0.85'),
        ('/companies.html', 'monthly', '0.85'),
        ('/pmo.html', 'monthly', '0.85'),
        ('/telecommunications.html', 'monthly', '0.85'),
        ('/project-controls.html', 'monthly', '0.85'),
        ('/digital-transformation.html', 'monthly', '0.85'),
        ('/leadership.html', 'monthly', '0.85'),
        ('/software.html', 'monthly', '0.80'),
        ('/contact.html', 'yearly', '0.80'),
        ('/downloads.html', 'monthly', '0.80'),
        ('/search.html', 'monthly', '0.70'),
        ('/404.html', 'yearly', '0.30'),
        ('/ar/', 'weekly', '1.0'),
        ('/ar/about.html', 'monthly', '0.95'),
        ('/ar/career.html', 'monthly', '0.95'),
        ('/ar/featured-projects.html', 'monthly', '0.95'),
        ('/ar/projects.html', 'monthly', '0.95'),
        ('/ar/skills.html', 'monthly', '0.95'),
        ('/ar/achievements.html', 'monthly', '0.90'),
        ('/ar/certifications.html', 'yearly', '0.90'),
        ('/ar/education.html', 'yearly', '0.90'),
        ('/ar/awards.html', 'yearly', '0.85'),
        ('/ar/companies.html', 'monthly', '0.85'),
        ('/ar/pmo.html', 'monthly', '0.85'),
        ('/ar/telecommunications.html', 'monthly', '0.85'),
        ('/ar/project-controls.html', 'monthly', '0.85'),
        ('/ar/digital-transformation.html', 'monthly', '0.85'),
        ('/ar/leadership.html', 'monthly', '0.85'),
        ('/ar/software.html', 'monthly', '0.80'),
        ('/ar/contact.html', 'yearly', '0.80'),
        ('/ar/downloads.html', 'monthly', '0.80'),
        ('/ar/search.html', 'monthly', '0.70'),
        ('/articles/', 'weekly', '0.90'),
        ('/en/articles/', 'weekly', '0.90'),
        ('/ar/articles/', 'weekly', '0.90'),
    ]

    today = datetime.now().strftime('%Y-%m-%d')
    for path, freq, pri in static_pages:
        lines.append(f'  <url><loc>{SITE_URL}{path}</loc><lastmod>{today}</lastmod><changefreq>{freq}</changefreq><priority>{pri}</priority></url>')

    for a in articles:
        if a.get('draft'):
            continue
        slug = a['slug']
        pub = a.get('publishDate', today)
        for prefix in ['', '/en', '/ar']:
            pri = '0.70' if prefix == '' else '0.85'
            path = f'{prefix}/articles/{slug}.html'
            lines.append(f'  <url><loc>{SITE_URL}{path}</loc><lastmod>{pub}</lastmod><changefreq>monthly</changefreq><priority>{pri}</priority></url>')

    lines.append('</urlset>')
    with open('sitemap.xml', 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"Regenerated sitemap.xml with {len(lines)-2} URLs")

def regenerate_rss(articles):
    items = []
    for a in sorted(articles, key=lambda x: x.get('publishDate', ''), reverse=True):
        if a.get('draft'):
            continue
        slug = a['slug']
        en = a['en']
        pub = a.get('publishDate', '')
        link = f"{SITE_URL}/en/articles/{slug}.html"
        pub_date = formatdate(datetime.strptime(pub, '%Y-%m-%d').timestamp(), usegmt=True)
        items.append(f"""    <item>
      <title>{esc(en['title'])}</title>
      <link>{link}</link>
      <description>{esc(en['excerpt'])}</description>
      <author>Ashraf Ibrahim El Desoky</author>
      <pubDate>{pub_date}</pubDate>
      <guid>{link}</guid>
    </item>""")

    rss = f"""<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>Ashraf El Desoky – Articles</title>
    <link>{SITE_URL}/articles/</link>
    <description>Articles and insights on project management, telecommunications, and digital transformation</description>
    <language>en-us</language>
    <lastBuildDate>{formatdate(usegmt=True)}</lastBuildDate>
{chr(10).join(items)}
  </channel>
</rss>
"""
    with open('rss.xml', 'w', encoding='utf-8') as f:
        f.write(rss)
    print(f"Regenerated rss.xml with {len(items)} items")

if __name__ == '__main__':
    articles = load_articles()
    print(f"Loaded {len(articles)} articles")
    generate_static_pages(articles)
    regenerate_sitemap(articles)
    regenerate_rss(articles)
    print("Done!")
