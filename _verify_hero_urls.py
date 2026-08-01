import json, re, os, urllib.request, urllib.error

with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Collect all hero image URLs to check
hero_urls = []
for a in articles:
    hero = a.get('heroImage', '')
    if hero:
        hero_urls.append((a['id'], a['slug'], hero))

# Check each URL
print("=== CHECKING HERO IMAGE URLS ===")
broken = []
for aid, slug, url in hero_urls:
    if url.startswith('http'):
        # Clean URL for checking (remove _gl params)
        clean_url = re.sub(r'\?_gl=.*', '?auto=compress&cs=tinysrgb&w=1200', url)
        if '?auto=' not in clean_url and '?_gl=' not in url:
            clean_url = url
        
        try:
            req = urllib.request.Request(clean_url, method='HEAD')
            req.add_header('User-Agent', 'Mozilla/5.0')
            resp = urllib.request.urlopen(req, timeout=10)
            print(f'OK ({resp.status}): ID={aid} slug={slug}')
        except urllib.error.HTTPError as e:
            print(f'BROKEN ({e.code}): ID={aid} slug={slug} url={clean_url}')
            broken.append((aid, slug, url, clean_url))
        except Exception as e:
            print(f'ERROR ({str(e)[:50]}): ID={aid} slug={slug} url={clean_url}')
            broken.append((aid, slug, url, clean_url))
    else:
        # Local file
        local_path = url.lstrip('/')
        full_path = os.path.join(os.getcwd(), local_path)
        if not os.path.exists(full_path):
            print(f'MISSING LOCAL: ID={aid} slug={slug} path={url}')
            broken.append((aid, slug, url, url))

print(f'\n=== SUMMARY ===')
print(f'Total broken: {len(broken)}')
for aid, slug, orig, clean in broken:
    print(f'  ID={aid} slug={slug}')
    print(f'    orig: {orig}')
    if orig != clean:
        print(f'    clean: {clean}')
