import _generate_and_regen as g
from _neg2_utils import load_articles
import os

articles = load_articles()
count = 0
for a in articles:
    if a.get('draft'):
        continue
    slug = a['slug']
    en_path = f'en/articles/{slug}.html'
    ar_path = f'ar/articles/{slug}.html'
    with open(en_path, 'w', encoding='utf-8') as f:
        f.write(g.gen_en_page(a))
    with open(ar_path, 'w', encoding='utf-8') as f:
        f.write(g.gen_ar_page(a))
    count += 1
print(f'Regenerated {count} article pairs ({count*2} files)')
