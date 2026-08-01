#!/usr/bin/env python3
"""
Stage 3 — Site-Wide Technical Cleanup
1. Remove all meta-keywords tags from HTML files
2. Rename asset files with spaces/uppercase to kebab-case + update references
3. Remove third-party visitor counter badge
4. Add Organization schema to homepage
"""
import os
import re
import json

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ── 1. Remove meta-keywords from all HTML files ──

def remove_meta_keywords(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    # Remove <meta name="keywords" content="..."> (case insensitive, handles multi-line)
    new_content = re.sub(r'<meta\s+name=["\']keywords["\']\s+content=["\'][^"\']*["\']\s*/?>', '', content, flags=re.IGNORECASE)
    # Also remove any reversed order: content before name
    new_content = re.sub(r'<meta\s+content=["\'][^"\']*["\']\s+name=["\']keywords["\']\s*/?>', '', new_content, flags=re.IGNORECASE)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


# ── 2. Rename asset files and update references ──

# Map of old → new filenames (only ones referenced in HTML)
ASSET_RENAMES = {
    'PMP Badge.png': 'pmp-badge.png',
    'cisco_ccna_Badge.png': 'cisco-ccna-badge.png',
    '2023-distinguished-expert.png': '2023-distinguished-expert.png',  # already kebab-case
}

def rename_assets():
    resources_dir = os.path.join(BASE_DIR, 'Resources')
    renamed = []
    for old_name, new_name in ASSET_RENAMES.items():
        if old_name == new_name:
            continue
        old_path = os.path.join(resources_dir, old_name)
        new_path = os.path.join(resources_dir, new_name)
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            renamed.append((old_name, new_name))
            print(f'  Renamed: {old_name} → {new_name}')
    return renamed

def update_asset_references(renamed):
    """Update all HTML files to use new asset filenames"""
    # Build search/replace pairs for Resources/ references
    replacements = {}
    for old_name, new_name in renamed:
        # Handle both "Resources/PMP Badge.png" and "Resources/PMP%20Badge.png"
        replacements[f'Resources/{old_name}'] = f'Resources/{new_name}'
        replacements[f'Resources/{old_name.replace(" ", "%20")}'] = f'Resources/{new_name}'
        # Also handle ../Resources/ prefix
        replacements[f'../Resources/{old_name}'] = f'../Resources/{new_name}'
        replacements[f'../Resources/{old_name.replace(" ", "%20")}'] = f'../Resources/{new_name}'

    count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root:
            continue
        for fname in files:
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            with open(fpath, 'r', encoding='utf-8', errors='replace') as f:
                content = f.read()
            original = content
            for old_ref, new_ref in replacements.items():
                content = content.replace(old_ref, new_ref)
            if content != original:
                with open(fpath, 'w', encoding='utf-8') as f:
                    f.write(content)
                count += 1
    return count


# ── 3. Remove visitor counter badge ──

def remove_visitor_counter(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    # Remove the visitor counter img tag and preceding separator
    new_content = re.sub(
        r'\s*<span>·</span>\s*<img\s+src=["\']https://page-visitor\.vercel\.app/[^"\']*["\'][^>]*>',
        '',
        content,
        flags=re.IGNORECASE
    )
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


# ── 4. Add Organization schema to homepage ──

ORG_SCHEMA_EN = '''<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Organization", "name": "Ashraf El Desoky", "url": "https://www.ashraf-eldesoky.space/", "logo": "https://www.ashraf-eldesoky.space/assets/images/og-image.jpg", "founder": {"@type": "Person", "name": "Ashraf Ibrahim El Desoky"}, "sameAs": ["https://www.linkedin.com/in/ashraf-eldesoky", "https://github.com/ashrafedes"]}</script>'''
ORG_SCHEMA_AR = '''<script type="application/ld+json">{"@context": "https://schema.org", "@type": "Organization", "name": "Ashraf El Desoky", "url": "https://www.ashraf-eldesoky.space/", "logo": "https://www.ashraf-eldesoky.space/assets/images/og-image.jpg", "founder": {"@type": "Person", "name": "Ashraf Ibrahim El Desoky"}, "sameAs": ["https://www.linkedin.com/in/ashraf-eldesoky", "https://github.com/ashrafedes"]}</script>'''

def add_organization_schema(filepath, lang='en'):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
    except UnicodeDecodeError:
        with open(filepath, 'r', encoding='utf-8', errors='replace') as f:
            content = f.read()
    # Check if Organization schema already exists
    if '"@type": "Organization"' in content or '"@type":"Organization"' in content:
        return False
    # Find the last JSON-LD script tag in <head> and insert after it
    schema = ORG_SCHEMA_AR if lang == 'ar' else ORG_SCHEMA_EN
    # Insert before </head>
    new_content = content.replace('</head>', f'  {schema}\n</head>')
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        return True
    return False


# ── Main ──

def main():
    # 1. Remove meta-keywords
    print('=== 1. Removing meta-keywords tags ===')
    kw_count = 0
    for root, dirs, files in os.walk(BASE_DIR):
        if '.git' in root:
            continue
        for fname in files:
            if not fname.endswith('.html'):
                continue
            fpath = os.path.join(root, fname)
            if remove_meta_keywords(fpath):
                kw_count += 1
    print(f'  Removed meta-keywords from {kw_count} files')

    # 2. Rename assets and update references
    print('\n=== 2. Renaming asset files ===')
    renamed = rename_assets()
    if renamed:
        ref_count = update_asset_references(renamed)
        print(f'  Updated references in {ref_count} HTML files')

    # 3. Remove visitor counter
    print('\n=== 3. Removing visitor counter badge ===')
    vc_files = [
        'en/index.html', 'ar/index.html', 'en.html',
        'en/featured-projects.html', 'ar/featured-projects.html'
    ]
    vc_count = 0
    for f in vc_files:
        fpath = os.path.join(BASE_DIR, f)
        if os.path.exists(fpath):
            if remove_visitor_counter(fpath):
                vc_count += 1
                print(f'  Removed from: {f}')
    print(f'  Removed visitor counter from {vc_count} files')

    # 4. Add Organization schema to homepages
    print('\n=== 4. Adding Organization schema ===')
    for f, lang in [('en/index.html', 'en'), ('ar/index.html', 'ar')]:
        fpath = os.path.join(BASE_DIR, f)
        if os.path.exists(fpath):
            if add_organization_schema(fpath, lang):
                print(f'  Added to: {f}')
            else:
                print(f'  Already present or failed: {f}')

    print('\nDone! Stage 3 cleanup complete.')


if __name__ == '__main__':
    main()
