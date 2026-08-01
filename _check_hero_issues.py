import json, re, os

with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Find all articles with missing hero images
missing_hero = []
for a in articles:
    hero = a.get('heroImage', '')
    if hero and not hero.startswith('http'):
        local_path = hero.lstrip('/')
        full_path = os.path.join(os.getcwd(), local_path)
        if not os.path.exists(full_path):
            missing_hero.append((a['id'], a['slug'], hero))
    elif hero and hero.startswith('http'):
        # Hero is a URL (like Pexels) - check if it's valid format
        missing_hero.append((a['id'], a['slug'], hero))

print("=== ALL ARTICLES WITH HERO IMAGE ISSUES ===")
for aid, slug, hero in missing_hero:
    print(f'ID={aid} slug={slug} hero={hero}')
print(f'\nTotal: {len(missing_hero)}')
