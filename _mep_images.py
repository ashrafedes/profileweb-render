import json, os, urllib.request
from datetime import datetime, timedelta

def load_articles():
    with open('articles/articles.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def save_articles(articles):
    with open('articles/articles.json', 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def download_image(url, filepath):
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(filepath, 'wb') as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f'  WARNING: Failed to download {url}: {e}')
        return False

def make_article(aid, slug, category, tags, en, ar, hero_image_path, date_offset=0, reading_time=12, featured=False):
    base = datetime(2026, 7, 20) + timedelta(days=date_offset)
    return {
        'id': aid, 'slug': slug, 'category': category,
        'author': 'Ashraf Ibrahim El Desoky',
        'heroImage': hero_image_path,
        'publishDate': base.strftime('%Y-%m-%d'),
        'updatedDate': base.strftime('%Y-%m-%d'),
        'readingTime': reading_time, 'featured': featured, 'draft': False,
        'tags': tags,
        'en': {
            'title': en['title'], 'excerpt': en['excerpt'], 'content': en['content'],
            'metaTitle': en.get('metaTitle', en['title'] + ' - Ashraf El Desoky, PMP'),
            'metaDescription': en.get('metaDescription', en['excerpt']),
            'keywords': en.get('keywords', [])
        },
        'ar': {
            'title': ar['title'], 'excerpt': ar['excerpt'], 'content': ar['content'],
            'metaTitle': ar.get('metaTitle', ar['title'] + ' - أشرف الدسوقي, PMP'),
            'metaDescription': ar.get('metaDescription', ar['excerpt']),
            'keywords': ar.get('keywords', [])
        }
    }

PEXEL_MEP = [
    'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/5668832/pexels-photo-5668832.jpeg?auto=compress&cs=tinysrgb&w=1200',
    'https://images.pexels.com/photos/3582392/pexels-photo-3582392.jpeg?auto=compress&cs=tinysrgb&w=1200',
]

def download_hero(idx, slug):
    url = PEXEL_MEP[idx]
    filepath = f'assets/images/articles/{slug}-hero.jpeg'
    os.makedirs('assets/images/articles', exist_ok=True)
    if download_image(url, filepath):
        return f'/assets/images/articles/{slug}-hero.jpeg'
    return '/assets/images/articles/default-hero.webp'
