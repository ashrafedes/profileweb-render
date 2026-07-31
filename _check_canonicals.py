import os, re

base = os.getcwd()
pages = []
for lang in ['en', 'ar']:
    lang_dir = os.path.join(base, lang)
    for f in os.listdir(lang_dir):
        if f.endswith('.html') and 'articles' not in f:
            pages.append(os.path.join(lang_dir, f))

for p in sorted(pages):
    with open(p, 'r', encoding='utf-8') as fh:
        content = fh.read()
    m = re.search(r'rel="canonical"\s+href="([^"]+)"', content)
    rel = p.replace(base + os.sep, '').replace(os.sep, '/')
    if m:
        print(f'{rel} => {m.group(1)}')
    else:
        print(f'{rel} => NO CANONICAL')
