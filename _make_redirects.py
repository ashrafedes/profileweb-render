import json, os

a = json.load(open('articles/articles.json', encoding='utf-8'))
existing = set(os.listdir('articles'))
count = 0

for x in a:
    if x.get('draft'):
        continue
    fname = x['slug'] + '.html'
    if fname in existing or fname == 'articles.json':
        continue
    title = (x.get('en', {}).get('title', '') or x['slug']).replace('"', '&quot;')
    slug = x['slug']
    html = '<!DOCTYPE html>\n<html>\n<head>\n  <meta charset="UTF-8">\n'
    html += f'  <meta http-equiv="refresh" content="0; url=/en/articles/{slug}.html">\n'
    html += f'  <link rel="canonical" href="https://www.ashraf-eldesoky.space/en/articles/{slug}.html">\n'
    html += f'  <title>{title}</title>\n</head>\n<body>\n'
    html += f'  <p>Redirecting to <a href="/en/articles/{slug}.html">article</a>...</p>\n'
    html += '</body>\n</html>\n'
    with open(f'articles/{fname}', 'w', encoding='utf-8') as f:
        f.write(html)
    count += 1

print(f'Created {count} redirect stubs')
