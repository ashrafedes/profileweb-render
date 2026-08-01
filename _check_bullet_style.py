#!/usr/bin/env python3
"""Scan all article HTML files for bullet points / lists that violate narrative prose style"""
import os
import re
import glob

root = os.path.dirname(os.path.abspath(__file__))

def count_lists(filepath):
    """Count <ul>, <ol>, <li> tags in the article content area"""
    with open(filepath, "r", encoding="utf-8", errors="replace") as f:
        text = f.read()
    
    # Count list-related tags
    ul_count = len(re.findall(r'<ul[>\s]', text, re.IGNORECASE))
    ol_count = len(re.findall(r'<ol[>\s]', text, re.IGNORECASE))
    li_count = len(re.findall(r'<li[>\s]', text, re.IGNORECASE))
    
    # Also check for bullet characters
    bullet_chars = len(re.findall(r'[•▪◦‣⁃]', text))
    
    return ul_count, ol_count, li_count, bullet_chars

results_en = []
results_ar = []

# English articles
for f in sorted(glob.glob(os.path.join(root, "en", "articles", "*.html"))):
    name = os.path.basename(f)
    if name in ("index.html", "article.html"):
        continue
    ul, ol, li, bullets = count_lists(f)
    total = ul + ol + li + bullets
    if total > 0:
        results_en.append((name, ul, ol, li, bullets, total))

# Arabic articles
for f in sorted(glob.glob(os.path.join(root, "ar", "articles", "*.html"))):
    name = os.path.basename(f)
    if name in ("index.html", "article.html"):
        continue
    ul, ol, li, bullets = count_lists(f)
    total = ul + ol + li + bullets
    if total > 0:
        results_ar.append((name, ul, ol, li, bullets, total))

print(f"=== ENGLISH ARTICLES WITH LISTS ===")
print(f"Total articles with lists: {len(results_en)}")
for name, ul, ol, li, bullets, total in sorted(results_en, key=lambda x: -x[5]):
    print(f"  {name}: ul={ul} ol={ol} li={li} bullets={bullets} (total={total})")

print(f"\n=== ARABIC ARTICLES WITH LISTS ===")
print(f"Total articles with lists: {len(results_ar)}")
for name, ul, ol, li, bullets, total in sorted(results_ar, key=lambda x: -x[5]):
    print(f"  {name}: ul={ul} ol={ol} li={li} bullets={bullets} (total={total})")

print(f"\n=== SUMMARY ===")
print(f"EN articles with lists: {len(results_en)} / 161")
print(f"AR articles with lists: {len(results_ar)} / 161")
