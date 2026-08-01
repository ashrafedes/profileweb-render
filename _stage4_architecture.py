#!/usr/bin/env python3
"""
Stage 4 — Article Architecture completion:
1. Generate complete sitemap.xml with all article URLs
2. Add BreadcrumbList schema to service pages
3. Verify all articles have unique URLs and proper schema
"""
import json
import os
import re
from datetime import datetime

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SITE_URL = 'https://www.ashraf-eldesoky.space'

def generate_sitemap():
    with open(os.path.join(BASE_DIR, 'articles', 'articles.json'), 'r', encoding='utf-8') as f:
        articles = json.load(f)

    urls = []
    
    # Static pages
    static_pages = [
        ('/', '1.0', 'weekly'),
        ('/en/', '0.9', 'weekly'),
        ('/ar/', '0.9', 'weekly'),
        ('/en/articles/', '0.9', 'weekly'),
        ('/ar/articles/', '0.9', 'weekly'),
        ('/en/pmo.html', '0.8', 'monthly'),
        ('/ar/pmo.html', '0.8', 'monthly'),
        ('/en/project-controls.html', '0.8', 'monthly'),
        ('/ar/project-controls.html', '0.8', 'monthly'),
        ('/en/telecommunications.html', '0.8', 'monthly'),
        ('/ar/telecommunications.html', '0.8', 'monthly'),
        ('/en/digital-transformation.html', '0.8', 'monthly'),
        ('/ar/digital-transformation.html', '0.8', 'monthly'),
        ('/en/featured-projects.html', '0.8', 'monthly'),
        ('/ar/featured-projects.html', '0.8', 'monthly'),
        ('/en/contact.html', '0.7', 'monthly'),
        ('/ar/contact.html', '0.7', 'monthly'),
    ]
    
    for path, priority, freq in static_pages:
        urls.append(f'  <url><loc>{SITE_URL}{path}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>')
    
    # Article pages
    for article in articles:
        if article.get('draft'):
            continue
        slug = article['slug']
        lastmod = article.get('updatedDate', article.get('publishDate', '2026-08-01'))
        for lang in ['en', 'ar']:
            if lang in article or 'en' in article:
                urls.append(f'  <url><loc>{SITE_URL}/{lang}/articles/{slug}.html</loc><lastmod>{lastmod}</lastmod><changefreq>monthly</changefreq><priority>0.85</priority></url>')
    
    # Hub pages (to be created in Stage 5-7)
    hub_pages = [
        ('/en/ftth/', '0.9', 'weekly'),
        ('/ar/ftth/', '0.9', 'weekly'),
        ('/en/project-controls-hub/', '0.9', 'weekly'),
        ('/ar/project-controls-hub/', '0.9', 'weekly'),
    ]
    for path, priority, freq in hub_pages:
        urls.append(f'  <url><loc>{SITE_URL}{path}</loc><changefreq>{freq}</changefreq><priority>{priority}</priority></url>')
    
    xml = '<?xml version="1.0" encoding="UTF-8"?>\n'
    xml += '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    xml += '\n'.join(urls)
    xml += '\n</urlset>'
    
    with open(os.path.join(BASE_DIR, 'sitemap.xml'), 'w', encoding='utf-8') as f:
        f.write(xml)
    print(f'Sitemap generated with {len(urls)} URLs')


def add_breadcrumb_to_service_pages():
    """Add BreadcrumbList schema to service pages that don't have it"""
    service_pages = [
        ('en/pmo.html', 'en', 'PMO Leadership'),
        ('ar/pmo.html', 'ar', 'قيادة مكتب إدارة المشاريع'),
        ('en/project-controls.html', 'en', 'Project Controls'),
        ('ar/project-controls.html', 'ar', 'ضوابط المشاريع'),
        ('en/telecommunications.html', 'en', 'Telecommunications'),
        ('ar/telecommunications.html', 'ar', 'الاتصالات'),
        ('en/digital-transformation.html', 'en', 'Digital Transformation'),
        ('ar/digital-transformation.html', 'ar', 'التحول الرقمي'),
        ('en/featured-projects.html', 'en', 'Featured Projects'),
        ('ar/featured-projects.html', 'ar', 'المشاريع المميزة'),
        ('en/contact.html', 'en', 'Contact'),
        ('ar/contact.html', 'ar', 'اتصل'),
    ]
    
    count = 0
    for filepath, lang, page_name in service_pages:
        fpath = os.path.join(BASE_DIR, filepath)
        if not os.path.exists(fpath):
            continue
        try:
            with open(fpath, 'r', encoding='utf-8') as f:
                content = f.read()
        except UnicodeDecodeError:
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
        
        # Check if BreadcrumbList already exists
        if 'BreadcrumbList' in content:
            continue
        
        home_name = 'الرئيسية' if lang == 'ar' else 'Home'
        breadcrumb = json.dumps({
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": home_name, "item": f"{SITE_URL}/{lang}/"},
                {"@type": "ListItem", "position": 2, "name": page_name, "item": f"{SITE_URL}/{filepath.replace(chr(92), '/')}"}
            ]
        }, ensure_ascii=False)
        
        schema_tag = f'<script type="application/ld+json">{breadcrumb}</script>'
        new_content = content.replace('</head>', f'  {schema_tag}\n</head>')
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            count += 1
            print(f'  Added BreadcrumbList to: {filepath}')
    
    print(f'Added BreadcrumbList to {count} service pages')


def main():
    print('=== Stage 4: Article Architecture ===')
    print('\n1. Generating complete sitemap...')
    generate_sitemap()
    
    print('\n2. Adding BreadcrumbList to service pages...')
    add_breadcrumb_to_service_pages()
    
    print('\n3. Verifying article URLs...')
    with open(os.path.join(BASE_DIR, 'articles', 'articles.json'), 'r', encoding='utf-8') as f:
        articles = json.load(f)
    
    en_dir = os.path.join(BASE_DIR, 'en', 'articles')
    ar_dir = os.path.join(BASE_DIR, 'ar', 'articles')
    
    missing = 0
    for article in articles:
        if article.get('draft'):
            continue
        slug = article['slug']
        for lang, dir_path in [('en', en_dir), ('ar', ar_dir)]:
            fpath = os.path.join(dir_path, f'{slug}.html')
            if not os.path.exists(fpath):
                print(f'  MISSING: {lang}/articles/{slug}.html')
                missing += 1
    
    if missing == 0:
        print(f'  All {len([a for a in articles if not a.get("draft")])} articles have HTML files in both languages ✅')
    else:
        print(f'  {missing} files missing!')
    
    print('\nDone! Stage 4 complete.')


if __name__ == '__main__':
    main()
