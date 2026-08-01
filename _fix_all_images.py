import json, re

with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)

# Replacement map for broken Pexels content images
# Old URL -> New valid URL
content_replacements = {
    'https://images.pexels.com/photos/7989670/pexels-photo-7989670.jpeg?auto=compress&cs=tinysrgb&w=1200':
        'https://images.pexels.com/photos/4348404/pexels-photo-4348404.jpeg?auto=compress&cs=tinysrgb&w=1200',  # telecom/data network
    
    'https://images.pexels.com/photos/53610/large-stones-and-mountains-53610.jpeg?auto=compress&cs=tinysrgb&w=1200':
        'https://images.pexels.com/photos/2582937/pexels-photo-2582937.jpeg?auto=compress&cs=tinysrgb&w=1200',  # fiber/infrastructure
    
    'https://images.pexels.com/photos/5900200/pexels-photo-5900200.jpeg?auto=compress&cs=tinysrgb&w=1200':
        'https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1200',  # project management
    
    'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200':
        'https://images.pexels.com/photos/3184303/pexels-photo-3184303.jpeg?auto=compress&cs=tinysrgb&w=1200',  # business/team
    
    'https://images.pexels.com/photos/2151/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1200':
        'https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg?auto=compress&cs=tinysrgb&w=1200',  # cyber security
}

# Hero image replacements (missing local files -> valid Pexels URLs)
hero_replacements = {
    137: 'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',  # project management
    145: 'https://images.pexels.com/photos/3184291/pexels-photo-3184291.jpeg?auto=compress&cs=tinysrgb&w=1200',  # telecom PM
    147: 'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',  # risk management
    148: 'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',  # risk governance
    149: 'https://images.pexels.com/photos/5380642/pexels-photo-5380642.jpeg?auto=compress&cs=tinysrgb&w=1200',  # cyber security
    150: 'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',  # business strategy
}

fixed_count = 0

for a in articles:
    aid = a['id']
    
    # Fix hero image
    if aid in hero_replacements:
        old_hero = a.get('heroImage', '')
        a['heroImage'] = hero_replacements[aid]
        print(f'Fixed hero for ID={aid}: {old_hero} -> {a["heroImage"]}')
        fixed_count += 1
    
    # Fix content images in both languages
    for lang in ['en', 'ar']:
        content = a.get(lang, {}).get('content', '')
        for old_url, new_url in content_replacements.items():
            if old_url in content:
                content = content.replace(old_url, new_url)
                print(f'Fixed content image in ID={aid} lang={lang}: {old_url[:60]}... -> {new_url[:60]}...')
                fixed_count += 1
        a[lang]['content'] = content

with open('articles/articles.json', 'w', encoding='utf-8') as f:
    json.dump(articles, f, ensure_ascii=False, indent=2)

print(f'\nTotal fixes applied: {fixed_count}')
