#!/usr/bin/env python3
"""Convert bullet lists to narrative prose in article HTML files."""
import os
import re
import glob
import html
from html.parser import HTMLParser

root = os.path.dirname(os.path.abspath(__file__))

# Skip these files
SKIP = {"index.html", "article.html", "dashboard.html", "404.html"}

def convert_lists_to_prose(html_text):
    """Find <ul>...</ul> blocks and convert <li> items to flowing paragraphs."""
    
    # Pattern to find <ul>...</ul> blocks (non-greedy, handles nested poorly but works for most)
    # We'll process repeatedly to handle nested lists
    
    def replace_ul(match):
        """Convert a <ul> block to narrative prose paragraphs."""
        inner = match.group(1)
        
        # Extract <li> items
        li_items = re.findall(r'<li[^>]*>(.*?)</li>', inner, re.DOTALL | re.IGNORECASE)
        
        if not li_items:
            return match.group(0)
        
        # Clean each li item
        cleaned_items = []
        for li in li_items:
            # Remove nested <ul> from li (we'll handle them separately)
            li = re.sub(r'<ul[^>]*>.*?</ul>', '', li, flags=re.DOTALL | re.IGNORECASE)
            # Strip tags but keep text
            li_text = re.sub(r'<[^>]+>', '', li)
            li_text = html.unescape(li_text).strip()
            # Remove trailing colons/semicolons
            li_text = re.sub(r'[:;]\s*$', '', li_text)
            if li_text:
                cleaned_items.append(li_text)
        
        if not cleaned_items:
            return ''
        
        # Join items into flowing prose
        if len(cleaned_items) == 1:
            prose = f'<p>{cleaned_items[0]}.</p>'
        elif len(cleaned_items) == 2:
            prose = f'<p>{cleaned_items[0]}, and {cleaned_items[1]}.</p>'
        else:
            # Join with commas and "and" for last item
            all_but_last = ', '.join(cleaned_items[:-1])
            prose = f'<p>{all_but_last}, and {cleaned_items[-1]}.</p>'
        
        return prose
    
    # Repeatedly replace <ul> blocks (innermost first for nested lists)
    prev = None
    result = html_text
    for _ in range(5):  # max 5 levels of nesting
        new_result = re.sub(r'<ul[^>]*>(.*?)</ul>', replace_ul, result, flags=re.DOTALL | re.IGNORECASE)
        if new_result == result:
            break
        result = new_result
    
    # Also convert <ol> blocks
    def replace_ol(match):
        inner = match.group(1)
        li_items = re.findall(r'<li[^>]*>(.*?)</li>', inner, re.DOTALL | re.IGNORECASE)
        
        if not li_items:
            return match.group(0)
        
        cleaned_items = []
        for li in li_items:
            li = re.sub(r'<ol[^>]*>.*?</ol>', '', li, flags=re.DOTALL | re.IGNORECASE)
            li_text = re.sub(r'<[^>]+>', '', li)
            li_text = html.unescape(li_text).strip()
            li_text = re.sub(r'[:;]\s*$', '', li_text)
            if li_text:
                cleaned_items.append(li_text)
        
        if not cleaned_items:
            return ''
        
        if len(cleaned_items) == 1:
            prose = f'<p>{cleaned_items[0]}.</p>'
        elif len(cleaned_items) == 2:
            prose = f'<p>First, {cleaned_items[0]}. Then, {cleaned_items[1]}.</p>'
        else:
            parts = []
            for i, item in enumerate(cleaned_items):
                if i == 0:
                    parts.append(f'First, {item}')
                elif i == len(cleaned_items) - 1:
                    parts.append(f'and finally, {item}')
                elif i == 1:
                    parts.append(f'then, {item}')
                else:
                    parts.append(f'next, {item}')
            prose = f'<p>{". ".join(parts)}.</p>'
        
        return prose
    
    result = re.sub(r'<ol[^>]*>(.*?)</ol>', replace_ol, result, flags=re.DOTALL | re.IGNORECASE)
    
    return result


def process_file(filepath):
    """Process a single HTML file, converting lists to prose."""
    with open(filepath, "r", encoding="utf-8") as f:
        original = f.read()
    
    # Count lists before
    ul_before = len(re.findall(r'<ul[>\s]', original, re.IGNORECASE))
    ol_before = len(re.findall(r'<ol[>\s]', original, re.IGNORECASE))
    li_before = len(re.findall(r'<li[>\s]', original, re.IGNORECASE))
    
    if ul_before == 0 and ol_before == 0:
        return False, 0, 0
    
    converted = convert_lists_to_prose(original)
    
    # Count lists after
    ul_after = len(re.findall(r'<ul[>\s]', converted, re.IGNORECASE))
    ol_after = len(re.findall(r'<ol[>\s]', converted, re.IGNORECASE))
    li_after = len(re.findall(r'<li[>\s]', converted, re.IGNORECASE))
    
    if converted == original:
        return False, 0, 0
    
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(converted)
    
    removed = (ul_before + ol_before + li_before) - (ul_after + ol_after + li_after)
    return True, removed, ul_after + ol_after


# Process English articles
en_count = 0
en_remaining = 0
for f in sorted(glob.glob(os.path.join(root, "en", "articles", "*.html"))):
    name = os.path.basename(f)
    if name in SKIP:
        continue
    changed, removed, remaining = process_file(f)
    if changed:
        en_count += 1
        en_remaining += remaining
        if remaining > 0:
            print(f"  EN PARTIAL: {name} - removed {removed}, remaining {remaining}")

# Process Arabic articles
ar_count = 0
ar_remaining = 0
for f in sorted(glob.glob(os.path.join(root, "ar", "articles", "*.html"))):
    name = os.path.basename(f)
    if name in SKIP:
        continue
    changed, removed, remaining = process_file(f)
    if changed:
        ar_count += 1
        ar_remaining += remaining
        if remaining > 0:
            print(f"  AR PARTIAL: {name} - removed {removed}, remaining {remaining}")

print(f"\n=== RESULTS ===")
print(f"EN articles converted: {en_count}, remaining lists: {en_remaining}")
print(f"AR articles converted: {ar_count}, remaining lists: {ar_remaining}")
