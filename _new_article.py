# -*- coding: utf-8 -*-
"""
New-article generator — creates ALL artifacts for a bilingual article.

Usage:
    python _new_article.py draft.json

Spec file (UTF-8 JSON):
{
  "slug": "my-article-slug",            // optional — derived from EN title
  "category_en": "Project Management",  // required
  "category_ar": "إدارة المشاريع",       // optional — defaults to category_en
  "date": "2026-11-26",                 // optional — defaults to today
  "reading_time": 6,                    // optional — auto-estimated from words
  "featured": false,                    // optional
  "image": "https://.../hero.jpeg",     // optional — default pexels fallback
  "tags": ["AI", "PMP"],                // optional
  "related": ["slug-a","slug-b","slug-c"], // optional — auto-picks 3 newest same-category
  "en": { "title": "...", "description": "...", "body": "..." },
  "ar": { "title": "...", "description": "...", "body": "..." }
}

Body may be HTML (used as-is) OR plain text where blank lines split
paragraphs and lines starting with "## " become <h2> headings.

Outputs:
  en/articles/<slug>.html  +  ar/articles/<slug>.html   (full static pages)
  articles/<slug>.html                                 (redirect stub)
  articles/articles.json                               (entry appended)
  en|ar/articles/index.html                            (card at grid top)
  sitemap.xml                                          (EN + AR urls)
"""
import json, re, sys, os, datetime

SITE = 'https://www.ashraf-eldesoky.space'
DEFAULT_IMG = 'https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1200'
AR_MONTHS = ['يناير','فبراير','مارس','أبريل','مايو','يونيو','يوليو','أغسطس','سبتمبر','أكتوبر','نوفمبر','ديسمبر']
EN_MONTHS = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']


def slugify(t):
    t = re.sub(r'[^a-z0-9\s-]', '', t.lower())
    return re.sub(r'[\s_]+', '-', t).strip('-')[:70]


def to_html(text):
    if re.search(r'<\s*(p|h[1-6]|ul|ol|div|section|blockquote)\b', text):
        return text
    out = []
    for para in re.split(r'\n\s*\n', text.strip()):
        para = para.strip()
        if not para:
            continue
        if para.startswith('## '):
            out.append('<h2>' + para[3:] + '</h2>')
        elif para.startswith('# '):
            out.append('<h2>' + para[2:] + '</h2>')
        else:
            out.append('<p>' + para.replace('\n', ' ') + '</p>')
    return '\n'.join(out)


def words_of(html):
    t = re.sub(r'<[^>]+>', ' ', html)
    return len(re.sub(r'\s+', ' ', t).split())


def page(lang, spec, body_html, related_html):
    d = spec['date']
    title = spec[lang]['title']
    desc = spec[lang]['description']
    cat = spec['category_ar'] if lang == 'ar' else spec['category_en']
    img = spec['image']
    slug = spec['slug']
    url = f'{SITE}/{lang}/articles/{slug}.html'
    is_ar = lang == 'ar'
    html_tag = '<html lang="ar" dir="rtl">' if is_ar else '<html lang="en" dir="ltr">'
    font = 'Cairo' if is_ar else 'Inter'
    author = spec.get('author', 'Ashraf Ibrahim El Desoky')
    site_name = 'أشرف الدسوقي' if is_ar else 'Ashraf El Desoky'
    meta = (f'<span>{author if not is_ar else "أشرف إبراهيم الدسوقي"}</span>'
            f'<span>· {d["ar_human"]}</span><span>· {spec["reading_time"]} دقائق قراءة</span>'
            if is_ar else
            f'<span>By {author}</span><span>· {d["en_human"]}</span><span>· {spec["reading_time"]} min read</span>')
    return f'''<!DOCTYPE html>
{html_tag}
<head>
 <!-- Google tag (gtag.js) -->
 <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z6B9JDZ6F0"></script>
 <script>
 window.dataLayer = window.dataLayer || [];
 function gtag(){{dataLayer.push(arguments);}}
 gtag('js', new Date());
 gtag('config', 'G-Z6B9JDZ6F0');
 </script>

 <meta charset="UTF-8">
 <meta name="viewport" content="width=device-width, initial-scale=1.0">
 <title>{title} | {site_name}</title>
 <meta name="description" content="{desc}">
 <meta name="author" content="{author}">
 <meta name="robots" content="index, follow">
 <meta property="og:type" content="article">
 <meta property="og:title" content="{title}">
 <meta property="og:description" content="{desc}">
 <meta property="og:url" content="{url}">
 <meta property="og:image" content="{img}">
 <meta property="og:image:width" content="1200">
 <meta property="og:image:height" content="630">
 <meta property="og:locale" content="{'ar_SA' if is_ar else 'en_US'}">
 <meta property="article:published_time" content="{d['iso']}">
 <meta property="article:modified_time" content="{d['iso']}">
 <meta name="twitter:card" content="summary_large_image">
 <meta name="twitter:title" content="{title} | {site_name}">
 <meta name="twitter:description" content="{desc}">
 <meta name="twitter:image" content="{img}">
 <link rel="canonical" href="{url}">
 <link rel="alternate" hreflang="en" href="{SITE}/en/articles/{slug}.html">
 <link rel="alternate" hreflang="ar" href="{SITE}/ar/articles/{slug}.html">
 <link rel="icon" type="image/svg+xml" href="../../assets/icons/favicon.svg">
 <link rel="manifest" href="../../manifest.json">
 <link rel="preconnect" href="https://fonts.googleapis.com">
 <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
 <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
 <link href="https://fonts.googleapis.com/css2?family={font}:wght@300;400;500;600;700;800;900&display=swap" rel="stylesheet">
 <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">
 <link rel="stylesheet" href="../../assets/css/main.css?v=4">
 <link rel="stylesheet" href="../../assets/css/articles.css">
 <script type="application/ld+json">{{"@context": "https://schema.org", "@type": "Article", "headline": "{title}", "description": "{desc}", "author": {{"@type": "Person", "name": "{author}"}}, "datePublished": "{d['iso']}", "dateModified": "{d['iso']}", "image": "{img}", "publisher": {{"@type": "Person", "name": "{author}"}}, "mainEntityOfPage": "{url}", "inLanguage": "{lang}"}}</script>
 <script type="application/ld+json">{{"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [{{"@type": "ListItem", "position": 1, "name": "Home", "item": "{SITE}"}}, {{"@type": "ListItem", "position": 2, "name": "Articles", "item": "{SITE}/{lang}/articles/"}}, {{"@type": "ListItem", "position": 3, "name": "{title}", "item": "{url}"}}]}}</script>
</head>
<body>
 <div id="ecms-nav-inject"></div>

 <main id="main-content" class="page-wrapper" style="padding-top:0;">
    <div class="article-hero" id="article-hero">
        <img class="article-hero-img" src="{img}" alt="{title}">
        <div class="article-hero-overlay"></div>
        <div class="container article-hero-content">
          <span class="article-hero-cat">{cat}</span>
          <h1>{title}</h1>
          <div class="article-hero-meta">{meta}</div>
        </div>
    </div>

 <section class="section" style="padding:2.5rem 0;">
 <div class="container">
{body_html}
 </div>
 </section>

 <section class="section" style="padding:0 0 2rem;">
{related_html}
 </section>

 </main>

 <div id="ecms-footer-inject"></div>
 <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
 <script src="../../config.js"></script>
 <script src="../../assets/js/i18n.js?v=2"></script>
 <script src="../../assets/js/components.js?v=6"></script>
 <script src="../../assets/js/core.js?v=7"></script>
 <script src="../../assets/js/article.js?v=12"></script>
</body>
</html>
'''


def related_block(lang, spec, articles):
    rels = spec.get('related')
    if not rels:
        cat = spec['category_en']
        same = [a for a in articles if a.get('category') == cat and a.get('slug') != spec['slug']]
        same.sort(key=lambda a: a.get('publishDate', ''), reverse=True)
        rels = [a['slug'] for a in same[:3]]
    cat = spec['category_ar'] if lang == 'ar' else spec['category_en']
    h = 'Related Articles' if lang == 'en' else 'مقالات ذات صلة'
    cards = ''
    for s in rels[:3]:
        p = f'{lang}/articles/{s}.html'
        if not os.path.exists(p):
            print(f'  ! related slug not found, skipped: {s}')
            continue
        t = open(p, encoding='utf-8').read()
        ti = re.search(r'property="og:title" content="([^"]+)"', t)[1]
        de = re.search(r'property="og:description" content="([^"]+)"', t)[1]
        im = re.search(r'property="og:image" content="([^"]+)"', t)[1]
        if not im.startswith('http'):
            im = SITE + im
        cards += f'''<a href="{s}.html" class="article-card" style="text-decoration:none;color:inherit;">
            <img class="article-card-img" src="{im}" alt="{ti}" loading="lazy">
            <div class="article-card-body">
              <div class="article-card-cat">{cat}</div>
              <h3>{ti}</h3>
              <p class="excerpt">{de}</p>
            </div>
          </a>'''
    return f'''<div class="container" id="related-articles">
        <h2 style="font-size:1.3rem;margin-bottom:1rem;">{h}</h2>
      <div class="related-grid">
        {cards}
      </div>
      </div>'''


def index_card(lang, spec):
    d = spec['date']
    cat = spec['category_en']
    title = spec[lang]['title']
    desc = spec[lang]['description']
    img = spec['image']
    slug = spec['slug']
    date_str = d['en_human'] if lang == 'en' else d['ar_human']
    rt = f"· {spec['reading_time']} min read" if lang == 'en' else f"· {spec['reading_time']} دقائق قراءة"
    tags = ''.join(f'<span class="tag" data-tag="{t}" style="cursor:pointer;">#{t}</span>' for t in spec.get('tags', []))
    return f'''        <a href="{slug}.html" class="article-card" style="text-decoration:none;color:inherit;">
          <img class="article-card-img" src="{img}" alt="{title}" loading="lazy">
          <div class="article-card-body">
            <div class="article-card-cat">{cat}</div>
            <h3>{title}</h3>
            <p class="excerpt">{desc}</p>
            <div class="article-card-meta">
              <span>{date_str}</span>
              <span>{rt}</span>
              {tags}
            </div>
          </div>
        </a>
'''


def main(spec_path):
    spec = json.load(open(spec_path, encoding='utf-8'))
    for req in ('en', 'ar'):
        for k in ('title', 'description', 'body'):
            assert spec.get(req, {}).get(k), f'missing {req}.{k}'
    assert spec.get('category_en'), 'missing category_en'

    if not spec.get('slug'):
        spec['slug'] = slugify(spec['en']['title'])
    slug = spec['slug']
    out = f'en/articles/{slug}.html'
    if os.path.exists(out) and '--force' not in sys.argv:
        sys.exit(f'ERROR: {out} already exists (use --force to overwrite)')

    today = datetime.date.today().isoformat()
    iso = spec.get('date', today)
    y, m, dd = map(int, iso.split('-'))
    spec['date'] = {'iso': iso,
                    'en_human': f'{EN_MONTHS[m-1]} {dd}, {y}',
                    'ar_human': f'{dd} {AR_MONTHS[m-1]} {y}'}
    spec['image'] = spec.get('image') or DEFAULT_IMG

    bodies = {l: '<div class="article-layout">\n          <div>\n            <div class="article-content" id="article-content">'
              + to_html(spec[l]['body']) + '\n            </div>\n          </div>\n        </div>'
              for l in ['en', 'ar']}
    if not spec.get('reading_time'):
        spec['reading_time'] = max(2, round(words_of(bodies['en']) / 200))

    articles = json.load(open('articles/articles.json', encoding='utf-8'))

    # 1+2) article pages
    for l in ['en', 'ar']:
        p = f'{l}/articles/{slug}.html'
        open(p, 'w', encoding='utf-8').write(page(l, spec, bodies[l], related_block(l, spec, articles)))
        print('wrote', p)

    # 3) root stub
    open(f'articles/{slug}.html', 'w', encoding='utf-8').write(f'''<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <meta http-equiv="refresh" content="0; url=/en/articles/{slug}.html">
  <link rel="canonical" href="{SITE}/en/articles/{slug}.html">
  <meta name="robots" content="noindex,follow">
  <title>{spec['en']['title']}</title>
</head>
<body>
  <p>Redirecting to <a href="/en/articles/{slug}.html">article</a>...</p>
</body>
</html>
''')
    print('wrote stub')

    # 4) articles.json
    if not any(a.get('slug') == slug for a in articles):
        ids = [a['id'] for a in articles if isinstance(a.get('id'), int)]
        articles.append({
            'id': (max(ids) + 1) if ids else len(articles) + 1,
            'slug': slug, 'category': spec['category_en'],
            'author': spec.get('author', 'Ashraf Ibrahim El Desoky'),
            'heroImage': spec['image'],
            'publishDate': iso, 'updatedDate': iso,
            'readingTime': spec['reading_time'],
            'featured': bool(spec.get('featured')), 'draft': False,
            'tags': spec.get('tags', []),
            'en': {'title': spec['en']['title'], 'excerpt': spec['en']['description'],
                   'content': re.sub(r'<[^>]+>', '', spec['en']['body'])[:400]},
            'ar': {'title': spec['ar']['title'], 'excerpt': spec['ar']['description'],
                   'content': re.sub(r'<[^>]+>', '', spec['ar']['body'])[:400]},
        })
        json.dump(articles, open('articles/articles.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('articles.json updated')

    # 5) index cards at grid top
    for l in ['en', 'ar']:
        p = f'{l}/articles/index.html'
        s = open(p, encoding='utf-8').read()
        anchor = '<div class="articles-grid" id="articles-grid">\n'
        if slug not in s and anchor in s:
            s = s.replace(anchor, anchor + index_card(l, spec), 1)
            open(p, 'w', encoding='utf-8').write(s)
            print('index card added:', p)

    # 6) sitemap
    sm = open('sitemap.xml', encoding='utf-8').read()
    if slug not in sm:
        add = ''.join(f'  <url><loc>{SITE}/{l}/articles/{slug}.html</loc><lastmod>{iso}</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>\n' for l in ['en', 'ar'])
        sm = sm.replace('</urlset>', add + '</urlset>')
        open('sitemap.xml', 'w', encoding='utf-8').write(sm)
        print('sitemap updated')

    print(f'\nDONE: {SITE}/en/articles/{slug}.html')
    print('Next: git add -A && git commit && git push')


if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit('usage: python _new_article.py draft.json [--force]')
    main(sys.argv[1])
