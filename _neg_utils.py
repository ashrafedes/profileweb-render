import json, os
from datetime import datetime, timedelta

def load_articles():
    with open('articles/articles.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_articles(articles):
    with open('articles/articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def download_image(url, filepath):
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(filepath, 'wb') as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f'  WARNING: {e}')
        return False

PEXEL_NEG = [
    'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/5668832/pexels-photo-5668832.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/1170979/pexels-photo-1170979.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
]

def download_hero(idx, slug):
    url = PEXEL_NEG[idx % len(PEXEL_NEG)]
    filepath = f'assets/images/articles/{slug}-hero.jpeg'
    os.makedirs('assets/images/articles', exist_ok=True)
    if download_image(url, filepath):
        return f'/assets/images/articles/{slug}-hero.jpeg'
    return '/assets/images/articles/default-hero.webp'

def make_article(aid, slug, category, tags, en, ar, hero, date_offset=0, reading_time=8):
    base = datetime(2026, 7, 21) + timedelta(days=date_offset)
    return {
        'id': aid, 'slug': slug, 'category': category,
        'author': 'Ashraf Ibrahim El Desoky',
        'heroImage': hero,
        'publishDate': base.strftime('%Y-%m-%d'),
        'updatedDate': base.strftime('%Y-%m-%d'),
        'readingTime': reading_time, 'featured': False, 'draft': False,
        'tags': tags,
        'en': {'title': en['title'], 'excerpt': en['excerpt'], 'content': en['content'],
               'metaTitle': en.get('metaTitle', en['title'] + ' - Ashraf El Desoky, PMP'),
               'metaDescription': en.get('metaDescription', en['excerpt']),
               'keywords': en.get('keywords', [])},
        'ar': {'title': ar['title'], 'excerpt': ar['excerpt'], 'content': ar['content'],
               'metaTitle': ar.get('metaTitle', ar['title'] + ' - أشرف الدسوقي, PMP'),
               'metaDescription': ar.get('metaDescription', ar['excerpt']),
               'keywords': ar.get('keywords', [])}
    }
