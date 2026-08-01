#!/usr/bin/env python3
"""Stage 9 — Add GA4 tag to all HTML files that don't have it, and create Search Console verification."""
import os, re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
GA4_TAG = """  <!-- Google tag (gtag.js) -->
  <script async src="https://www.googletagmanager.com/gtag/js?id=G-Z6B9JDZ6F0"></script>
  <script>
    window.dataLayer = window.dataLayer || [];
    function gtag(){dataLayer.push(arguments);}
    gtag('js', new Date());
    gtag('config', 'G-Z6B9JDZ6F0');
  </script>
"""

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
        content = f.read()
    if 'googletagmanager' in content or 'G-Z6B9JDZ6F0' in content:
        return False
    # Insert after <head> tag
    head_match = re.search(r'<head>', content)
    if not head_match:
        return False
    # Insert right after <head>
    insert_pos = head_match.end()
    new_content = content[:insert_pos] + '\n' + GA4_TAG + content[insert_pos:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    return True

def main():
    added = 0
    skipped = 0
    for root, dirs, files in os.walk(BASE_DIR):
        # Skip .git, node_modules, etc.
        if '.git' in root or 'node_modules' in root:
            continue
        for fname in files:
            if fname.endswith('.html'):
                filepath = os.path.join(root, fname)
                if process_file(filepath):
                    added += 1
                    print(f'  Added GA4: {os.path.relpath(filepath, BASE_DIR)}')
                else:
                    skipped += 1
    print(f'\nTotal: {added} files updated, {skipped} files already had GA4 or no <head>')

if __name__ == '__main__':
    main()
