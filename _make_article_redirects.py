#!/usr/bin/env python3
"""Create redirect HTML files for missing /articles/SLUG.html -> /en/articles/SLUG.html"""
import os
import glob

root_dir = os.path.dirname(os.path.abspath(__file__))

# Get all article slugs from en/articles/
en_articles = set()
for f in glob.glob(os.path.join(root_dir, "en", "articles", "*.html")):
    name = os.path.basename(f)
    if name not in ("index.html", "article.html"):
        en_articles.add(name)

# Get existing redirect files in articles/
existing = set()
for f in glob.glob(os.path.join(root_dir, "articles", "*.html")):
    name = os.path.basename(f)
    if name not in ("index.html", "article.html", "dashboard.html"):
        existing.add(name)

missing = en_articles - existing
print(f"EN articles: {len(en_articles)}")
print(f"Existing redirects: {len(existing)}")
print(f"Missing: {len(missing)}")

template = '<!DOCTYPE html>\n<html>\n<head>\n  <!-- Google tag (gtag.js) -->\n  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z6B9JDZ6F0"></script>\n  <script>\n    window.dataLayer = window.dataLayer || [];\n    function gtag(){dataLayer.push(arguments);}\n    gtag(\'js\', new Date());\n    gtag(\'config\', \'G-Z6B9JDZ6F0\');\n  </script>\n\n  <meta charset="UTF-8">\n  <meta http-equiv="refresh" content="0; url=/en/articles/__SLUG__">\n  <link rel="canonical" href="https://www.ashraf-eldesoky.space/en/articles/__SLUG__">\n  <title>Redirecting\u2026</title>\n</head>\n<body>\n  <p>Redirecting to <a href="/en/articles/__SLUG__">article</a>...</p>\n</body>\n</html>\n'

count = 0
for slug in sorted(missing):
    out_path = os.path.join(root_dir, "articles", slug)
    content = template.replace("__SLUG__", slug)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(content)
    count += 1

print(f"Created {count} redirect files")
