import json, re, os

with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Collect all image URLs from articles
image_urls = []
for a in articles:
    # Hero images (local paths)
    hero = a.get('heroImage', '')
    if hero:
        image_urls.append(('hero', a['id'], a['slug'], hero))
    
    # Content images (Pexels URLs in en content)
    en_content = a.get('en', {}).get('content', '')
    ar_content = a.get('ar', {}).get('content', '')
    
    for lang, content in [('en', en_content), ('ar', ar_content)]:
        urls = re.findall(r'!\[.*?\]\((https://images\.pexels\.com[^)]+)\)', content)
        for url in urls:
            image_urls.append(('pexels', a['id'], a['slug'], url))

# Check hero images exist locally
print("=== HERO IMAGES (local) ===")
missing_hero = []
for img_type, aid, slug, url in image_urls:
    if img_type == 'hero':
        local_path = url.lstrip('/')
        full_path = os.path.join(os.getcwd(), local_path)
        exists = os.path.exists(full_path)
        if not exists:
            missing_hero.append((aid, slug, url))
            print(f'MISSING: ID={aid} slug={slug} path={url}')
        else:
            print(f'OK: ID={aid} slug={slug} path={url}')

print(f'\nTotal hero images missing: {len(missing_hero)}')

# Collect unique Pexels URLs
print("\n=== PEXELS IMAGE URLS ===")
pexels_urls = set()
for img_type, aid, slug, url in image_urls:
    if img_type == 'pexels':
        pexels_urls.add(url)

print(f'Total unique Pexels URLs: {len(pexels_urls)}')
for url in sorted(pexels_urls):
    print(url)
