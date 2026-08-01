#!/usr/bin/env python3
"""Check sitemap URLs for invalid entries: missing files, redirect stubs, empty templates"""
import os
import re

root = os.path.dirname(os.path.abspath(__file__))
base = "https://www.ashraf-eldesoky.space"

with open(os.path.join(root, "sitemap.xml"), "r", encoding="utf-8") as f:
    content = f.read()

urls = re.findall(r'<loc>(.*?)</loc>', content)

missing_files = []
redirects = []
tiny_files = []
ok = 0

for url in urls:
    path = url.replace(base, "")
    if path == "" or path == "/":
        fpath = os.path.join(root, "index.html")
    elif path.endswith("/"):
        fpath = os.path.join(root, path.strip("/"), "index.html")
    else:
        fpath = os.path.join(root, path.lstrip("/"))
    fpath = os.path.normpath(fpath)

    if not os.path.isfile(fpath):
        missing_files.append((url, fpath))
        continue

    size = os.path.getsize(fpath)
    
    # Read file to check if it's a redirect stub
    with open(fpath, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    
    is_redirect = "http-equiv='refresh'" in text or 'http-equiv="refresh"' in text or "location.replace" in text
    # Redirect stubs are typically <1KB
    if is_redirect and size < 2000:
        redirects.append((url, fpath, size))
    elif size < 1000:
        tiny_files.append((url, fpath, size))
    else:
        ok += 1

print(f"Total URLs: {len(urls)}")
print(f"OK (real content): {ok}")
print(f"Missing files: {len(missing_files)}")
print(f"Redirect stubs: {len(redirects)}")
print(f"Tiny files (<1KB): {len(tiny_files)}")

if missing_files:
    print("\n=== MISSING FILES ===")
    for url, fpath in missing_files:
        print(f"  {url}")
        print(f"    -> {fpath}")

if redirects:
    print("\n=== REDIRECT STUBS (should not be in sitemap) ===")
    for url, fpath, size in redirects:
        print(f"  {url} ({size} bytes)")

if tiny_files:
    print("\n=== TINY FILES (<1KB, possibly invalid) ===")
    for url, fpath, size in tiny_files:
        print(f"  {url} ({size} bytes)")
