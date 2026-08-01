#!/usr/bin/env python3
"""Fix double </p> tags and other artifacts from bullet-to-prose conversion"""
import os
import re
import glob

root = os.path.dirname(os.path.abspath(__file__))
SKIP = {"index.html", "article.html", "dashboard.html", "404.html"}

count = 0
for f in glob.glob(os.path.join(root, "en", "articles", "*.html")) + glob.glob(os.path.join(root, "ar", "articles", "*.html")):
    name = os.path.basename(f)
    if name in SKIP:
        continue
    with open(f, "r", encoding="utf-8") as fh:
        text = fh.read()
    
    original = text
    # Fix double </p></p>
    text = re.sub(r'</p></p>', '</p>', text)
    text = re.sub(r'</p>\s*</p>', '</p>', text)
    # Fix empty <p></p>
    text = re.sub(r'<p>\s*</p>', '', text)
    # Fix <p> followed by whitespace then </p> with content that already ends in .
    # Fix multiple spaces
    text = re.sub(r'  +', ' ', text)
    
    if text != original:
        with open(f, "w", encoding="utf-8") as fh:
            fh.write(text)
        count += 1

print(f"Fixed {count} files")
