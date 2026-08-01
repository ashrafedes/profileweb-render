#!/usr/bin/env python3
"""Check all sitemap URLs exist as files on disk, excluding dashboard.html"""
import os
import re

root = os.path.dirname(os.path.abspath(__file__))
base = "https://www.ashraf-eldesoky.space"

with open(os.path.join(root, "sitemap.xml"), "r", encoding="utf-8") as f:
    content = f.read()

urls = re.findall(r'<loc>(.*?)</loc>', content)

missing = []
ok = 0
skip = 0

for url in urls:
    # Skip dashboard
    if "articles/dashboard.html" in url:
        skip += 1
        continue

    path = url.replace(base, "")
    if path == "" or path == "/":
        fpath = os.path.join(root, "index.html")
    elif path.endswith("/"):
        fpath = os.path.join(root, path.strip("/"), "index.html")
    else:
        fpath = os.path.join(root, path.lstrip("/"))

    # Normalize path separators
    fpath = os.path.normpath(fpath)

    if os.path.isfile(fpath):
        ok += 1
    else:
        missing.append((url, fpath))

print(f"Total URLs in sitemap: {len(urls)}")
print(f"Skipped (dashboard): {skip}")
print(f"OK: {ok}")
print(f"Missing: {len(missing)}")
print()
for url, fpath in missing:
    print(f"MISSING: {url}")
    print(f"  -> expected at: {fpath}")
