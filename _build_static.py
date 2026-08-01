#!/usr/bin/env python3
"""
Build script: Pre-renders article content into static HTML for SEO/crawlability.
Reads articles.json and generates:
  - Individual article pages (EN + AR) with static hero + body content
  - Articles index pages (EN + AR) with static article cards
The JS still runs as progressive enhancement (search, filter, TOC, related).
"""
import json
import os
import re
import html
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARTICLES_JSON = os.path.join(BASE_DIR, 'articles', 'articles.json')
SITE_URL = 'https://www.ashraf-eldesoky.space'

# ── Minimal Markdown renderer (mirrors article.js renderMarkdown) ──

def render_markdown(md):
    if not md:
        return ''
    text = md

    # Code blocks
    text = re.sub(r'```(\w*)\n([\s\S]*?)```', lambda m: f'<pre><code>{html.escape(m.group(2).strip())}</code></pre>', text)

    # Tables
    def table_replacer(m):
        header = m.group(1)
        sep = m.group(2)
        body = m.group(3)
        heads = [h.strip() for h in header.split('|') if h.strip()]
        rows = []
        for line in body.strip().split('\n'):
            cells = [c.strip() for c in line.split('|') if c.strip()]
            if cells:
                rows.append(cells)
        t = '<table><thead><tr>' + ''.join(f'<th>{h}</th>' for h in heads) + '</tr></thead><tbody>'
        for r in rows:
            t += '<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>'
        t += '</tbody></table>'
        return t
    text = re.sub(r'^\|(.+)\|\n\|([-:\s|]+)\|\n((?:\|.+\|\n?)+)', table_replacer, text, flags=re.MULTILINE)

    # Headings
    text = re.sub(r'^### (.+)$', r'<h3>\1</h3>', text, flags=re.MULTILINE)
    text = re.sub(r'^## (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)
    text = re.sub(r'^# (.+)$', r'<h2>\1</h2>', text, flags=re.MULTILINE)

    # Blockquotes
    text = re.sub(r'^> (.+)$', r'<blockquote>\1</blockquote>', text, flags=re.MULTILINE)

    # Callout boxes
    text = re.sub(r'^\[info\] (.+)$', r'<div class="callout callout-info"><div class="callout-title">ℹ️ Info</div>\1</div>', text, flags=re.MULTILINE)
    text = re.sub(r'^\[warning\] (.+)$', r'<div class="callout callout-warning"><div class="callout-title">⚠️ Warning</div>\1</div>', text, flags=re.MULTILINE)
    text = re.sub(r'^\[success\] (.+)$', r'<div class="callout callout-success"><div class="callout-title">✅ Success</div>\1</div>', text, flags=re.MULTILINE)

    # Bold and italic
    text = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', text)
    text = re.sub(r'\*(.+?)\*', r'<em>\1</em>', text)

    # Inline code
    text = re.sub(r'`([^`]+)`', r'<code>\1</code>', text)

    # Images (before links)
    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', r'<img src="\2" alt="\1" style="max-width:100%;height:auto;border-radius:8px;margin:1rem 0;" loading="lazy">', text)

    # Links
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', text)

    # Lists
    text = re.sub(r'^(\d+)\. (.+)$', r'<li>\2</li>', text, flags=re.MULTILINE)
    text = re.sub(r'^- (.+)$', r'<li>\1</li>', text, flags=re.MULTILINE)
    text = re.sub(r'(<li>.*</li>\n?)+', lambda m: '<ul>' + m.group(0) + '</ul>', text)

    # Paragraphs
    lines = text.split('\n')
    result = []
    for line in lines:
        t = line.strip()
        if not t:
            result.append('')
            continue
        if re.match(r'^<(h2|h3|h4|ul|ol|pre|blockquote|table|div|li|img)', t):
            result.append(t)
        else:
            result.append(f'<p>{t}</p>')
    text = '\n'.join(result)
    text = re.sub(r'\n+', '\n', text)
    return text


def format_date(date_str, lang='en'):
    if not date_str:
        return ''
    try:
        d = datetime.strptime(date_str, '%Y-%m-%d')
        if lang == 'ar':
            months = ['يناير', 'فبراير', 'مارس', 'أبريل', 'مايو', 'يونيو',
                      'يوليو', 'أغسطس', 'سبتمبر', 'أكتوبر', 'نوفمبر', 'ديسمبر']
            return f'{d.day} {months[d.month-1]} {d.year}'
        else:
            months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
                      'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
            return f'{months[d.month-1]} {d.day}, {d.year}'
    except:
        return date_str


def esc(s):
    if not s:
        return ''
    return html.escape(str(s))


# ── Article page template ──

def build_article_head(article, lang):
    data = article.get(lang, article.get('en', {}))
    slug = article['slug']
    url = f'{SITE_URL}/{lang}/articles/{slug}.html'
    alt_lang = 'ar' if lang == 'en' else 'en'
    alt_url = f'{SITE_URL}/{alt_lang}/articles/{slug}.html'
    title = data.get('metaTitle', data.get('title', ''))
    desc = data.get('metaDescription', data.get('excerpt', ''))
    keywords = ', '.join(data.get('keywords', []))
    hero_img = article.get('heroImage', '')
    og_image = f'{SITE_URL}{hero_img}' if hero_img else ''
    pub_date = article.get('publishDate', '')
    upd_date = article.get('updatedDate', pub_date)
    font_family = 'Cairo' if lang == 'ar' else 'Inter'
    font_weights = '300;400;500;600;700;800;900' if lang == 'ar' else '300;400;500;600;700;800;900'
    dir_attr = 'rtl' if lang == 'ar' else 'ltr'
    og_locale = 'ar_SA' if lang == 'ar' else 'en_US'

    # JSON-LD Article schema
    jsonld = {
        "@context": "https://schema.org",
        "@type": "Article",
        "headline": data.get('title', ''),
        "description": desc,
        "author": {"@type": "Person", "name": article.get('author', 'Ashraf Ibrahim El Desoky')},
        "datePublished": pub_date,
        "dateModified": upd_date,
        "image": og_image if og_image else None,
        "publisher": {"@type": "Person", "name": article.get('author', 'Ashraf Ibrahim El Desoky')},
        "mainEntityOfPage": url,
        "inLanguage": lang
    }
    jsonld_str = json.dumps({k: v for k, v in jsonld.items() if v is not None}, ensure_ascii=False)

    # Breadcrumb schema
    bc = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home" if lang == 'en' else "الرئيسية", "item": SITE_URL},
            {"@type": "ListItem", "position": 2, "name": "Articles" if lang == 'en' else "المقالات", "item": f"{SITE_URL}/{lang}/articles/"},
            {"@type": "ListItem", "position": 3, "name": data.get('title', ''), "item": url}
        ]
    }
    bc_str = json.dumps(bc, ensure_ascii=False)

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
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
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(desc)}">
  <meta name="author" content="{esc(article.get('author', 'Ashraf Ibrahim El Desoky'))}">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="article">
  <meta property="og:title" content="{esc(data.get('title', ''))}">
  <meta property="og:description" content="{esc(desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:image" content="{og_image}">
  <meta property="og:image:width" content="1200">
  <meta property="og:image:height" content="630">
  <meta property="og:locale" content="{og_locale}">
  <meta property="article:published_time" content="{pub_date}">
  <meta property="article:modified_time" content="{upd_date}">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{esc(data.get('title', ''))}">
  <meta name="twitter:description" content="{esc(desc)}">
  <meta name="twitter:image" content="{og_image}">
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
  <script type="application/ld+json">{jsonld_str}</script>
  <script type="application/ld+json">{bc_str}</script>
</head>'''


def build_article_hero(article, lang):
    data = article.get(lang, article.get('en', {}))
    hero_img = article.get('heroImage', '')
    title = data.get('title', '')
    category = article.get('category', '')
    author = article.get('author', 'Ashraf Ibrahim El Desoky')
    pub_date = article.get('publishDate', '')
    reading_time = article.get('readingTime', '')
    upd_date = article.get('updatedDate', pub_date)

    by_text = 'بقلم' if lang == 'ar' else 'By'
    updated_text = 'مُحدّث' if lang == 'ar' else 'Updated'
    min_read = 'دقيقة قراءة' if lang == 'ar' else 'min read'

    img_html = f'<img class="article-hero-img" src="{hero_img}" alt="{esc(title)}">' if hero_img else ''
    updated_html = f'<span>· {updated_text}: {format_date(upd_date, lang)}</span>' if upd_date != pub_date else ''

    return f'''<div class="article-hero" id="article-hero">
        {img_html}
        <div class="article-hero-overlay"></div>
        <div class="container article-hero-content">
          <span class="article-hero-cat">{esc(category)}</span>
          <h1>{esc(title)}</h1>
          <div class="article-hero-meta">
            <span>{by_text} {esc(author)}</span>
            <span>· {format_date(pub_date, lang)}</span>
            <span>· {reading_time} {min_read}</span>
            {updated_html}
          </div>
        </div>
      </div>'''


def build_article_body(article, lang):
    data = article.get(lang, article.get('en', {}))
    slug = article['slug']
    content_html = render_markdown(data.get('content', ''))
    tags = article.get('tags', [])

    share_text = 'مشاركة' if lang == 'ar' else 'Share'
    tags_text = 'الوسوم:' if lang == 'ar' else 'Tags:'
    back_text = '← العودة للمقالات' if lang == 'ar' else '← Back to Articles'
    encoded_title = esc(data.get('title', ''))
    article_url = f'{SITE_URL}/{lang}/articles/{slug}.html'

    tags_html = ''
    if tags:
        tags_html = f'''
            <div class="article-tags" style="margin:1.5rem 0;">
              <span style="font-size:0.85rem;font-weight:600;color:var(--text-muted);margin-right:0.5rem;">{tags_text}</span>
              {''.join(f'<a href="../articles/index.html?tag={esc(t)}" class="article-tag" style="display:inline-block;background:var(--bg-alt);border:1px solid var(--border-light);border-radius:999px;padding:0.25rem 0.75rem;font-size:0.8rem;color:var(--text);text-decoration:none;margin:0.25rem;">#{esc(t)}</a>' for t in tags)}
            </div>'''

    return f'''<div id="article-body">
        <div class="article-layout">
          <div>
            <div class="article-content" id="article-content">{content_html}</div>

            <div style="margin:2.5rem 0 1.5rem;padding-top:1.5rem;border-top:1px solid var(--border-light);">
              <div class="share-buttons">
                <span style="font-size:0.85rem;font-weight:600;color:var(--text-muted);margin-right:0.5rem;">{share_text}:</span>
                <a class="share-btn" href="https://twitter.com/intent/tweet?url={article_url}&text={encoded_title}" target="_blank" rel="noopener">𝕏 Twitter</a>
                <a class="share-btn" href="https://www.linkedin.com/sharing/share-offsite/?url={article_url}" target="_blank" rel="noopener">LinkedIn</a>
                <a class="share-btn" href="https://www.facebook.com/sharer/sharer.php?u={article_url}" target="_blank" rel="noopener">Facebook</a>
                <button class="share-btn" onclick="navigator.clipboard.writeText(window.location.href);this.textContent='✓ Copied'">🔗 Copy Link</button>
              </div>
            </div>

            {tags_html}

            <div style="display:flex;justify-content:space-between;gap:1rem;margin:1.5rem 0;flex-wrap:wrap;" id="prev-next"></div>

            <a href="index.html" style="display:inline-block;margin-top:1rem;font-weight:600;color:var(--accent);text-decoration:none;">{back_text}</a>
          </div>

          <aside class="article-sidebar">
            <div style="margin-top:2rem;">
              <div class="article-lang-switch">
                <button class="{'active' if lang == 'en' else ''}" data-lang="en">🇺🇸 EN</button>
                <button class="{'active' if lang == 'ar' else ''}" data-lang="ar">🇸🇦 ع</button>
              </div>
            </div>
          </aside>
        </div>
      </div>'''


def build_article_page(article, lang):
    head = build_article_head(article, lang)
    hero = build_article_hero(article, lang)
    body = build_article_body(article, lang)
    font_style = '<style>* { font-family: \'Cairo\', sans-serif; }</style>' if lang == 'ar' else ''

    return f'''{head}
<body>{font_style}
  <div id="ecms-nav-inject"></div>

  <main id="main-content" class="page-wrapper" style="padding-top:0;">
    {hero}

    <section class="section" style="padding:2.5rem 0;">
      <div class="container">
        {body}
      </div>
    </section>

    <section class="section" style="padding:0 0 2rem;">
      <div class="container" id="related-articles"></div>
    </section>

  </main>

  <div id="ecms-footer-inject"></div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
  <script src="../../config.js"></script>
  <script src="../../assets/js/i18n.js?v=2"></script>
  <script src="../../assets/js/components.js?v=4"></script>
  <script src="../../assets/js/core.js?v=6"></script>
  <script src="../../assets/js/article.js?v=9"></script>
</body>
</html>'''


# ── Articles index page builder ──

def build_articles_index(articles, lang):
    font_family = 'Cairo' if lang == 'ar' else 'Inter'
    font_weights = '300;400;500;600;700;800;900' if lang == 'ar' else '300;400;500;600;700;800;900'
    dir_attr = 'rtl' if lang == 'ar' else 'ltr'
    og_locale = 'ar_SA' if lang == 'ar' else 'en_US'

    if lang == 'ar':
        page_title = 'المقالات – أشرف الدسوقي، PMP® | رؤى إدارة المشاريع'
        meta_desc = 'مقالات ورؤى حول إدارة المشاريع والاتصالات والتحول الرقمي وقيادة مكتب إدارة المشاريع وضوابط المشاريع بقلم أشرف الدسوقي، PMP®.'
        og_title = 'المقالات – أشرف الدسوقي، PMP®'
        og_desc = 'مقالات ورؤى حول إدارة المشاريع والاتصالات والتحول الرقمي.'
        h1 = 'مركز المقالات'
        subtitle = 'مقالات ورؤى حول إدارة المشاريع والاتصالات والتحول الرقمي'
        search_placeholder = 'ابحث في المقالات…'
        search_label = 'ابحث في المقالات'
        popular_label = 'مواضيع شائعة'
        latest_label = 'أحدث المقالات'
        sort_label = 'التاريخ ↓'
        home_text = 'الرئيسية'
        articles_text = 'المقالات'
        by_text = 'بقلم'
        min_read = 'دقائق قراءة'
        featured_label = 'مميز'
        read_more = 'اقرأ المزيد'
    else:
        page_title = 'Articles – Ashraf El Desoky, PMP® | Project Management Insights'
        meta_desc = 'Articles and insights on project management, telecommunications, digital transformation, PMO leadership, and project controls by Ashraf El Desoky, PMP®.'
        og_title = 'Articles – Ashraf El Desoky, PMP®'
        og_desc = 'Articles and insights on project management, telecommunications, and digital transformation.'
        h1 = 'Articles Center'
        subtitle = 'Articles and insights on project management, telecommunications, and digital transformation'
        search_placeholder = 'Search articles…'
        search_label = 'Search articles'
        popular_label = 'Popular Topics'
        latest_label = 'Latest Articles'
        sort_label = 'Date ↓'
        home_text = 'Home'
        articles_text = 'Articles'
        by_text = 'By'
        min_read = 'min read'
        featured_label = 'Featured'
        read_more = 'Read more'

    # Sort articles by date (newest first)
    published = [a for a in articles if not a.get('draft')]
    published.sort(key=lambda a: a.get('publishDate', '1970-01-01'), reverse=True)

    # Featured article
    featured = next((a for a in published if a.get('featured')), published[0] if published else None)
    featured_html = ''
    if featured:
        fd = featured.get(lang, featured.get('en', {}))
        fimg = featured.get('heroImage', '')
        fimg_style = f"background-image:url('{fimg}')" if fimg else 'background:var(--bg-alt)'
        featured_html = f'''<a href="{featured['slug']}.html" style="text-decoration:none;color:inherit;display:block;">
        <div class="featured-card">
          <div class="featured-card-img" style="{fimg_style}"></div>
          <div class="featured-card-body">
            <span class="featured-badge">{featured_label}</span>
            <h2>{esc(fd.get('title', ''))}</h2>
            <p class="excerpt">{esc(fd.get('excerpt', ''))}</p>
            <div class="article-card-meta">
              <span>{by_text} {esc(featured.get('author', ''))}</span>
              <span>{format_date(featured.get('publishDate', ''), lang)}</span>
              <span>· {featured.get('readingTime', '')} {min_read}</span>
            </div>
          </div>
        </div>
      </a>'''

    # Category pills
    cats = sorted(set(a.get('category', '') for a in published))
    all_cat = 'الكل' if lang == 'ar' else 'All'
    cat_pills = ''.join(
        f'<button class="category-pill" data-cat="{esc(cat)}">{esc(cat)}</button>'
        for cat in [all_cat] + cats
    )

    # Popular topics (top 10 tags)
    tag_count = {}
    for a in published:
        for t in a.get('tags', []):
            tag_count[t] = tag_count.get(t, 0) + 1
    top_tags = sorted(tag_count.items(), key=lambda x: -x[1])[:10]
    popular_html = ''.join(
        f'<button class="category-pill" data-tag="{esc(tag)}">{esc(tag)}</button>'
        for tag, _ in top_tags
    )

    # Article cards (all articles, JS will paginate)
    cards_html = ''
    for a in published:
        d = a.get(lang, a.get('en', {}))
        img = a.get('heroImage', '')
        if img:
            img_html = f'<img class="article-card-img" src="{img}" alt="{esc(d.get("title", ""))}" loading="lazy">'
        else:
            img_html = '<div class="article-card-img" style="display:flex;align-items:center;justify-content:center;font-size:2rem;background:var(--bg-alt);">📝</div>'
        tag_html = ''.join(
            f'<span class="tag" data-tag="{esc(t)}" style="cursor:pointer;">#{esc(t)}</span>'
            for t in (a.get('tags', []) or [])[:2]
        )
        cards_html += f'''
        <a href="{a['slug']}.html" class="article-card" style="text-decoration:none;color:inherit;">
          {img_html}
          <div class="article-card-body">
            <div class="article-card-cat">{esc(a.get('category', ''))}</div>
            <h3>{esc(d.get('title', ''))}</h3>
            <p class="excerpt">{esc(d.get('excerpt', ''))}</p>
            <div class="article-card-meta">
              <span>{format_date(a.get('publishDate', ''), lang)}</span>
              <span>· {a.get('readingTime', '')} {min_read}</span>
              {tag_html}
            </div>
          </div>
        </a>'''

    url = f'{SITE_URL}/{lang}/articles/'
    alt_lang = 'ar' if lang == 'en' else 'en'
    alt_url = f'{SITE_URL}/{alt_lang}/articles/'
    font_style = f'<style>* {{ font-family: \'Cairo\', sans-serif; }}</style>' if lang == 'ar' else ''

    return f'''<!DOCTYPE html>
<html lang="{lang}" dir="{dir_attr}">
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
  <title>{esc(page_title)}</title>
  <meta name="description" content="{esc(meta_desc)}">
  <meta name="author" content="Ashraf Ibrahim El Desoky">
  <meta name="robots" content="index, follow">
  <meta property="og:type" content="website">
  <meta property="og:title" content="{esc(og_title)}">
  <meta property="og:description" content="{esc(og_desc)}">
  <meta property="og:url" content="{url}">
  <meta property="og:locale" content="{og_locale}">
  <meta name="twitter:card" content="summary_large_image">
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
</head>
<body>{font_style}
  <div id="ecms-nav-inject"></div>

  <main id="main-content" class="page-wrapper">

    <!-- Hero -->
    <div class="articles-hero">
      <div class="container">
        <nav aria-label="Breadcrumb" class="breadcrumb" style="margin-bottom:1.5rem;">
          <a href="../index.html" style="color:rgba(255,255,255,0.7);">{home_text}</a>
          <span style="color:rgba(255,255,255,0.4);margin:0 0.5rem;">{'‹' if lang == 'ar' else '›'}</span>
          <span style="color:#fff;font-weight:600;">{articles_text}</span>
        </nav>
        <h1 id="articles-page-title" style="display:inline-flex;align-items:center;gap:0.6rem;">{h1}
          <a href="../../rss.xml" target="_blank" rel="noopener" title="RSS Feed" aria-label="RSS Feed" style="text-decoration:none;display:inline-flex;align-items:center;">
            <img src="../../assets/icons/rss-feed.png" alt="RSS Feed" width="32" height="32" style="vertical-align:middle;filter:drop-shadow(0 1px 3px rgba(0,0,0,0.3));" onerror="this.style.display='none'">
          </a>
        </h1>
        <p id="articles-page-subtitle">{subtitle}</p>

        <!-- Search -->
        <div class="articles-search-wrap" style="margin-top:1.5rem;">
          <span class="articles-search-icon">🔍</span>
          <input type="search" id="articles-search" class="articles-search-input"
            placeholder="{search_placeholder}" autocomplete="off"
            aria-label="{search_label}">
        </div>
      </div>
    </div>

    <section class="section" style="padding:2.5rem 0;">
      <div class="container">

        <!-- Featured Article -->
        <div id="featured-article" style="margin-bottom:2.5rem;">{featured_html}</div>

        <!-- Categories -->
        <div style="margin-bottom:1.5rem;">
          <div class="category-pills" id="category-pills">{cat_pills}</div>
        </div>

        <!-- Popular Topics -->
        <div style="margin-bottom:2rem;">
          <h3 style="font-size:0.88rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em;margin-bottom:0.75rem;">{popular_label}</h3>
          <div class="category-pills" id="popular-topics">{popular_html}</div>
        </div>

        <!-- Articles Grid -->
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:1rem;flex-wrap:wrap;gap:0.75rem;">
          <h3 style="font-size:0.88rem;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:0.06em;margin:0;">{latest_label}</h3>
          <button id="btn-sort-date" class="category-pill" onclick="toggleArticleSort()" style="font-size:0.82rem;padding:0.4rem 0.8rem;cursor:pointer;">{sort_label}</button>
        </div>
        <div class="articles-grid" id="articles-grid">{cards_html}</div>

        <!-- Pagination -->
        <div class="pagination" id="pagination"></div>

      </div>
    </section>

  </main>

  <div id="ecms-footer-inject"></div>
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.bundle.min.js" defer></script>
  <script src="../../config.js"></script>
  <script src="../../assets/js/i18n.js?v=2"></script>
  <script src="../../assets/js/components.js?v=4"></script>
  <script src="../../assets/js/core.js?v=6"></script>
  <script src="../../assets/js/articles.js?v=12"></script>
</body>
</html>'''


# ── Main ──

def main():
    with open(ARTICLES_JSON, 'r', encoding='utf-8') as f:
        articles = json.load(f)

    print(f'Loaded {len(articles)} articles from articles.json')

    # Build individual article pages
    en_dir = os.path.join(BASE_DIR, 'en', 'articles')
    ar_dir = os.path.join(BASE_DIR, 'ar', 'articles')
    os.makedirs(en_dir, exist_ok=True)
    os.makedirs(ar_dir, exist_ok=True)

    count = 0
    for article in articles:
        if article.get('draft'):
            continue
        slug = article['slug']

        for lang, dir_path in [('en', en_dir), ('ar', ar_dir)]:
            if lang not in article and 'en' not in article:
                continue
            html_content = build_article_page(article, lang)
            filepath = os.path.join(dir_path, f'{slug}.html')
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            count += 1

    print(f'Generated {count} article pages')

    # Build articles index pages
    for lang, dir_path in [('en', en_dir), ('ar', ar_dir)]:
        index_html = build_articles_index(articles, lang)
        index_path = os.path.join(dir_path, 'index.html')
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(index_html)
        print(f'Built {lang} articles index: {index_path}')

    print('Done! Static content rendered for all articles.')


if __name__ == '__main__':
    main()
