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

def make_article(aid, slug, category, tags, en, ar, hero_image_path, date_offset=0):
    base = datetime(2026, 7, 18) + timedelta(days=date_offset)
    return {
        'id': aid,
        'slug': slug,
        'category': category,
        'author': 'Ashraf Ibrahim El Desoky',
        'heroImage': hero_image_path,
        'publishDate': base.strftime('%Y-%m-%d'),
        'updatedDate': base.strftime('%Y-%m-%d'),
        'readingTime': 8,
        'featured': False,
        'draft': False,
        'tags': tags,
        'en': {
            'title': en['title'],
            'excerpt': en['excerpt'],
            'content': en['content'],
            'metaTitle': en.get('metaTitle', en['title'] + ' – Ashraf El Desoky, PMP®'),
            'metaDescription': en.get('metaDescription', en['excerpt']),
            'keywords': en.get('keywords', [])
        },
        'ar': {
            'title': ar['title'],
            'excerpt': ar['excerpt'],
            'content': ar['content'],
            'metaTitle': ar.get('metaTitle', ar['title'] + ' – أشرف الدسوقي, PMP®'),
            'metaDescription': ar.get('metaDescription', ar['excerpt']),
            'keywords': ar.get('keywords', [])
        }
    }

PEXEL_IMAGES = {
    'procurement': [
        'https://images.pexels.com/photos/5668832/pexels-photo-5668832.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36729672/pexels-photo-36729672.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5778661/pexels-photo-5778661.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8730781/pexels-photo-8730781.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7841477/pexels-photo-7841477.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'resource': [
        'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36733293/pexels-photo-36733293.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36733326/pexels-photo-36733326.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29267510/pexels-photo-29267510.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29284274/pexels-photo-29284274.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'bms': [
        'https://images.pexels.com/photos/33531829/pexels-photo-33531829.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3582392/pexels-photo-3582392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29206492/pexels-photo-29206492.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/37591158/pexels-photo-37591158.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'pacs': [
        'https://images.pexels.com/photos/1170979/pexels-photo-1170979.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7089029/pexels-photo-7089029.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7089013/pexels-photo-7089013.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5452291/pexels-photo-5452291.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4021808/pexels-photo-4021808.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'fire': [
        'https://images.pexels.com/photos/31470430/pexels-photo-31470430.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3958649/pexels-photo-3958649.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/10887301/pexels-photo-10887301.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/37833045/pexels-photo-37833045.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36731054/pexels-photo-36731054.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'hotel': [
        'https://images.pexels.com/photos/14746032/pexels-photo-14746032.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/14332619/pexels-photo-14332619.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/15599751/pexels-photo-15599751.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/33626951/pexels-photo-33626951.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29649748/pexels-photo-29649748.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'people': [
        'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36765716/pexels-photo-36765716.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5520330/pexels-photo-5520330.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29284337/pexels-photo-29284337.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
}

def download_hero(topic, idx, slug):
    url = PEXEL_IMAGES[topic][idx]
    filepath = f'assets/images/articles/{slug}-hero.jpeg'
    os.makedirs('assets/images/articles', exist_ok=True)
    if download_image(url, filepath):
        return f'/assets/images/articles/{slug}-hero.jpeg'
    return '/assets/images/articles/default-hero.webp'
