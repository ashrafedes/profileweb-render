import os, re

base = os.getcwd()
fixed = 0

for lang in ['en', 'ar']:
    lang_dir = os.path.join(base, lang)
    for f in os.listdir(lang_dir):
        if not f.endswith('.html') or 'articles' in f or f in ('index.html', '404.html'):
            continue
        filepath = os.path.join(lang_dir, f)
        with open(filepath, 'r', encoding='utf-8') as fh:
            content = fh.read()
        
        # Check if canonical already has the lang prefix
        m = re.search(r'rel="canonical"\s+href="https://www\.ashraf-eldesoky\.space/([^"]+)"', content)
        if not m:
            continue
        
        canonical_path = m.group(1)
        
        # If canonical already starts with en/ or ar/, skip
        if canonical_path.startswith(f'{lang}/'):
            continue
        
        # Build new canonical with lang prefix
        new_canonical = f'https://www.ashraf-eldesoky.space/{lang}/{canonical_path}'
        
        # Replace in content
        old_href = f'href="https://www.ashraf-eldesoky.space/{canonical_path}"'
        new_href = f'href="{new_canonical}"'
        
        # Only replace in the canonical link tag
        old_tag = f'rel="canonical" {old_href}'
        new_tag = f'rel="canonical" {new_href}'
        
        if old_tag in content:
            content = content.replace(old_tag, new_tag)
            # Also handle alternate order: href before rel
            old_tag2 = f'{old_href} rel="canonical"'
            new_tag2 = f'{new_href} rel="canonical"'
            content = content.replace(old_tag2, new_tag2)
            
            with open(filepath, 'w', encoding='utf-8') as fh:
                fh.write(content)
            print(f'Fixed: {lang}/{f} => {new_canonical}')
            fixed += 1

print(f'\nTotal fixed: {fixed}')
