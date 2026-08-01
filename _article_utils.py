import json, os, urllib.request, random
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
        'https://images.pexels.com/photos/4172735/pexels-photo-4172735.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4172742/pexels-photo-4172742.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5900227/pexels-photo-5900227.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8867434/pexels-photo-8867434.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'resource': [
        'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36733293/pexels-photo-36733293.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36733326/pexels-photo-36733326.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29267510/pexels-photo-29267510.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29284274/pexels-photo-29284274.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'bms': [
        'https://images.pexels.com/photos/33531829/pexels-photo-33531829.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3582392/pexels-photo-3582392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29206492/pexels-photo-29206492.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/37591158/pexels-photo-37591158.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/32237668/pexels-photo-32237668.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/30983540/pexels-photo-30983540.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825539/pexels-photo-3825539.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825529/pexels-photo-3825529.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825548/pexels-photo-3825548.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/30983540/pexels-photo-30983540.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'pacs': [
        'https://images.pexels.com/photos/1170979/pexels-photo-1170979.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7089029/pexels-photo-7089029.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7089013/pexels-photo-7089013.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5452291/pexels-photo-5452291.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4021808/pexels-photo-4021808.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'fire': [
        'https://images.pexels.com/photos/31470430/pexels-photo-31470430.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3958649/pexels-photo-3958649.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/10887301/pexels-photo-10887301.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/37833045/pexels-photo-37833045.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36731054/pexels-photo-36731054.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2689963/pexels-photo-2689963.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2689886/pexels-photo-2689886.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2689870/pexels-photo-2689870.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8801118/pexels-photo-8801118.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8801130/pexels-photo-8801130.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1251869/pexels-photo-1251869.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1251880/pexels-photo-1251880.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/280215/pexels-photo-280215.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/280218/pexels-photo-280218.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/280220/pexels-photo-280220.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'hotel': [
        'https://images.pexels.com/photos/14746032/pexels-photo-14746032.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/14332619/pexels-photo-14332619.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/15599751/pexels-photo-15599751.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/33626951/pexels-photo-33626951.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29649748/pexels-photo-29649748.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2029718/pexels-photo-2029718.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2029722/pexels-photo-2029722.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2029744/pexels-photo-2029744.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/261101/pexels-photo-261101.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/261047/pexels-photo-261047.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/261327/pexels-photo-261327.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3144594/pexels-photo-3144594.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3144605/pexels-photo-3144605.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1579586/pexels-photo-1579586.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1579712/pexels-photo-1579712.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'people': [
        'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36765716/pexels-photo-36765716.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5520330/pexels-photo-5520330.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29284337/pexels-photo-29284337.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'strategy': [
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5900227/pexels-photo-5900227.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8867434/pexels-photo-8867434.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'risk': [
        'https://images.pexels.com/photos/5668832/pexels-photo-5668832.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5778661/pexels-photo-5778661.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8730781/pexels-photo-8730781.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7841477/pexels-photo-7841477.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4172735/pexels-photo-4172735.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4172742/pexels-photo-4172742.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5900227/pexels-photo-5900227.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8867434/pexels-photo-8867434.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'cybersecurity': [
        'https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2881229/pexels-photo-2881229.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1089440/pexels-photo-1089440.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'project_management': [
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5900227/pexels-photo-5900227.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8867434/pexels-photo-8867434.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'leadership': [
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7691751/pexels-photo-7691751.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5520330/pexels-photo-5520330.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/29284337/pexels-photo-29284337.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/36765716/pexels-photo-36765716.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'technology': [
        'https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2881229/pexels-photo-2881229.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1089440/pexels-photo-1089440.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'construction': [
        'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825539/pexels-photo-3825539.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825529/pexels-photo-3825529.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825548/pexels-photo-3825548.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3582392/pexels-photo-3582392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'telecom': [
        'https://images.pexels.com/photos/8020244/pexels-photo-8020244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825539/pexels-photo-3825539.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825529/pexels-photo-3825529.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3825548/pexels-photo-3825548.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2881229/pexels-photo-2881229.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'digital_transformation': [
        'https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/2881229/pexels-photo-2881229.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181271/pexels-photo-1181271.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181244/pexels-photo-1181244.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181396/pexels-photo-1181396.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1593046/pexels-photo-1593046.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1592984/pexels-photo-1592984.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'data_analytics': [
        'https://images.pexels.com/photos/265087/pexels-photo-265087.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265152/pexels-photo-265152.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/265144/pexels-photo-265144.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036936/pexels-photo-1036936.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1036808/pexels-photo-1036808.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/1089440/pexels-photo-1089440.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5900227/pexels-photo-5900227.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8867434/pexels-photo-8867434.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184283/pexels-photo-3184283.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3183150/pexels-photo-3183150.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
    'governance': [
        'https://images.pexels.com/photos/5668832/pexels-photo-5668832.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/5778661/pexels-photo-5778661.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/8730781/pexels-photo-8730781.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/7841477/pexels-photo-7841477.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4172735/pexels-photo-4172735.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/4172742/pexels-photo-4172742.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184360/pexels-photo-3184360.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184408/pexels-photo-3184408.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184432/pexels-photo-3184432.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184423/pexels-photo-3184423.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184465/pexels-photo-3184465.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184325/pexels-photo-3184325.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184292/pexels-photo-3184292.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184392/pexels-photo-3184392.jpeg?auto=compress&cs=tinysrgb&w=1200',
        'https://images.pexels.com/photos/3184339/pexels-photo-3184339.jpeg?auto=compress&cs=tinysrgb&w=1200',
    ],
}

def random_pexel(topic, exclude=None):
    """Return a random Pexels image URL for the given topic, optionally excluding specific URLs."""
    pool = PEXEL_IMAGES.get(topic, PEXEL_IMAGES['people'])
    if exclude:
        pool = [u for u in pool if u not in exclude]
    if not pool:
        pool = PEXEL_IMAGES.get(topic, PEXEL_IMAGES['people'])
    return random.choice(pool)

def random_content_images(topic, count, exclude=None):
    """Return a list of random unique Pexels image URLs for the given topic.
    Args:
        topic: Key in PEXEL_IMAGES (e.g. 'strategy', 'risk', 'cybersecurity')
        count: Number of unique images to return
        exclude: List of URLs to exclude (e.g. hero image already used)
    Returns:
        List of unique image URLs
    """
    pool = PEXEL_IMAGES.get(topic, PEXEL_IMAGES['people'])
    if exclude:
        pool = [u for u in pool if u not in exclude]
    if len(pool) <= count:
        return pool
    return random.sample(pool, count)

def download_hero(topic, idx=None, slug=None):
    """Download a hero image. If idx is None, picks a random image from the topic."""
    if idx is not None:
        url = PEXEL_IMAGES[topic][idx]
    else:
        url = random_pexel(topic)
    filepath = f'assets/images/articles/{slug}-hero.jpeg'
    os.makedirs('assets/images/articles', exist_ok=True)
    if download_image(url, filepath):
        return f'/assets/images/articles/{slug}-hero.jpeg'
    return '/assets/images/articles/default-hero.webp'
