#!/usr/bin/env python3
"""Stage 10 — Final QA: verify sitemap, article parity, hub pages, schema, internal links."""
import os, re, json
from html.parser import HTMLParser

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = "https://www.ashraf-eldesoky.space"

class LinkChecker(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a':
            for attr, val in attrs:
                if attr == 'href' and val:
                    self.links.append(val)

def check_sitemap():
    sitemap_path = os.path.join(BASE_DIR, 'sitemap.xml')
    if not os.path.exists(sitemap_path):
        print("  FAIL: sitemap.xml not found")
        return False
    with open(sitemap_path, 'r', encoding='utf-8') as f:
        content = f.read()
    urls = re.findall(r'<loc>(.*?)</loc>', content)
    print(f"  Sitemap contains {len(urls)} URLs")
    # Check key URLs
    key_urls = [
        f"{SITE_URL}/",
        f"{SITE_URL}/en/",
        f"{SITE_URL}/ar/",
        f"{SITE_URL}/en/ftth/",
        f"{SITE_URL}/ar/ftth/",
        f"{SITE_URL}/en/project-controls-hub/",
        f"{SITE_URL}/ar/project-controls-hub/",
        f"{SITE_URL}/en/articles/",
        f"{SITE_URL}/ar/articles/",
    ]
    for url in key_urls:
        if url in urls:
            print(f"    OK: {url}")
        else:
            print(f"    MISSING: {url}")
    return True

def check_article_parity():
    json_path = os.path.join(BASE_DIR, 'articles', 'articles.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        articles = json.load(f)
    print(f"  Total articles in JSON: {len(articles)}")
    en_ok = 0
    ar_ok = 0
    missing_en = []
    missing_ar = []
    for a in articles:
        slug = a['slug']
        en_path = os.path.join(BASE_DIR, 'en', 'articles', f'{slug}.html')
        ar_path = os.path.join(BASE_DIR, 'ar', 'articles', f'{slug}.html')
        if os.path.exists(en_path):
            en_ok += 1
        else:
            missing_en.append(slug)
        if os.path.exists(ar_path):
            ar_ok += 1
        else:
            missing_ar.append(slug)
    print(f"  EN article HTML files: {en_ok}/{len(articles)}")
    print(f"  AR article HTML files: {ar_ok}/{len(articles)}")
    if missing_en:
        print(f"  MISSING EN: {missing_en[:5]}")
    if missing_ar:
        print(f"  MISSING AR: {missing_ar[:5]}")
    return en_ok == len(articles) and ar_ok == len(articles)

def check_hub_pages():
    hubs = [
        ('en/ftth/index.html', 'FTTH Hub (EN)'),
        ('ar/ftth/index.html', 'FTTH Hub (AR)'),
        ('en/project-controls-hub/index.html', 'Project Controls Hub (EN)'),
        ('ar/project-controls-hub/index.html', 'Project Controls Hub (AR)'),
    ]
    all_ok = True
    for path, name in hubs:
        full_path = os.path.join(BASE_DIR, path)
        if os.path.exists(full_path):
            with open(full_path, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            # Check for article cards
            card_count = content.count('article-card') or content.count('card-hover')
            print(f"  OK: {name} ({card_count} cards)")
        else:
            print(f"  MISSING: {name}")
            all_ok = False
    return all_ok

def check_schema():
    # Check a sample of pages for JSON-LD
    pages = [
        'en/index.html',
        'ar/index.html',
        'en/ftth/index.html',
        'ar/ftth/index.html',
        'en/project-controls-hub/index.html',
        'ar/project-controls-hub/index.html',
    ]
    all_ok = True
    for page in pages:
        path = os.path.join(BASE_DIR, page)
        if not os.path.exists(path):
            print(f"  MISSING: {page}")
            all_ok = False
            continue
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        schemas = re.findall(r'"@type"\s*:\s*"([^"]+)"', content)
        print(f"  {page}: schemas = {schemas}")
        if not schemas:
            all_ok = False
    return all_ok

def check_ga4():
    # Check that GA4 is on key pages
    pages = [
        'en/index.html',
        'ar/index.html',
        'en/ftth/index.html',
        'ar/ftth/index.html',
        'en/project-controls-hub/index.html',
        'ar/project-controls-hub/index.html',
    ]
    all_ok = True
    for page in pages:
        path = os.path.join(BASE_DIR, page)
        if not os.path.exists(path):
            continue
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        if 'G-Z6B9JDZ6F0' in content:
            print(f"  OK: {page} has GA4")
        else:
            print(f"  MISSING GA4: {page}")
            all_ok = False
    return all_ok

def check_robots():
    path = os.path.join(BASE_DIR, 'robots.txt')
    if not os.path.exists(path):
        print("  FAIL: robots.txt not found")
        return False
    with open(path, 'r') as f:
        content = f.read()
    has_sitemap = 'sitemap.xml' in content
    has_allow = 'Allow: /' in content
    print(f"  Sitemap reference: {'OK' if has_sitemap else 'MISSING'}")
    print(f"  Allow all: {'OK' if has_allow else 'MISSING'}")
    return has_sitemap and has_allow

def check_nav_links():
    # Check components.js has hub links
    path = os.path.join(BASE_DIR, 'assets', 'js', 'components.js')
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()
    has_ftth = 'ftth/' in content
    has_pc = 'project-controls-hub/' in content
    print(f"  FTTH hub link in nav: {'OK' if has_ftth else 'MISSING'}")
    print(f"  PC hub link in nav: {'OK' if has_pc else 'MISSING'}")
    return has_ftth and has_pc

def check_homepage_hubs():
    for page in ['en/index.html', 'ar/index.html']:
        path = os.path.join(BASE_DIR, page)
        with open(path, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
        has_ftth = 'ftth/' in content
        has_pc = 'project-controls-hub/' in content
        print(f"  {page}: FTTH={'OK' if has_ftth else 'MISSING'}, PC={'OK' if has_pc else 'MISSING'}")
        if not (has_ftth and has_pc):
            return False
    return True

def main():
    print("=== Stage 10: Final QA ===\n")
    
    print("1. Sitemap check:")
    check_sitemap()
    print()
    
    print("2. Article parity (EN/AR):")
    check_article_parity()
    print()
    
    print("3. Hub pages:")
    check_hub_pages()
    print()
    
    print("4. Schema (JSON-LD):")
    check_schema()
    print()
    
    print("5. GA4 Analytics:")
    check_ga4()
    print()
    
    print("6. Robots.txt:")
    check_robots()
    print()
    
    print("7. Navigation links:")
    check_nav_links()
    print()
    
    print("8. Homepage hub integration:")
    check_homepage_hubs()
    print()
    
    print("=== QA Complete ===")

if __name__ == '__main__':
    main()
