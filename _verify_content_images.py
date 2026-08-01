import json, re, urllib.request, urllib.error

with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Collect all unique Pexels image URLs from content
pexels_urls = {}
for a in articles:
    for lang in ['en', 'ar']:
        content = a.get(lang, {}).get('content', '')
        urls = re.findall(r'!\[.*?\]\((https://images\.pexels\.com[^)]+)\)', content)
        for url in urls:
            if url not in pexels_urls:
                pexels_urls[url] = []
            pexels_urls[url].append((a['id'], a['slug'], lang))

print(f'Total unique Pexels content images: {len(pexels_urls)}')
print('Checking...')

broken = []
for i, (url, refs) in enumerate(pexels_urls.items()):
    try:
        req = urllib.request.Request(url, method='HEAD')
        req.add_header('User-Agent', 'Mozilla/5.0')
        resp = urllib.request.urlopen(req, timeout=10)
        status = resp.status
        if status != 200:
            print(f'BROKEN ({status}): {url}')
            broken.append((url, refs))
    except urllib.error.HTTPError as e:
        print(f'BROKEN ({e.code}): {url}')
        broken.append((url, refs))
    except Exception as e:
        print(f'ERROR: {url} - {str(e)[:50]}')
        broken.append((url, refs))

print(f'\nTotal broken content images: {len(broken)}')
for url, refs in broken:
    print(f'URL: {url}')
    for aid, slug, lang in refs:
        print(f'  ID={aid} lang={lang} slug={slug}')
