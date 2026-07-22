import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, download_hero, read_file

articles = load_articles()

slug = 'art-of-war-strategic-principles'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

content = read_file(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'artofwar_article.txt'))

# Extract title (first # heading)
title = 'The Art of War: Strategic Principles That Still Shape Leadership, Business, Negotiation, and Modern Decision-Making'
for line in content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        title = line[2:].strip()
        break

excerpt = 'A comprehensive analysis of Sun Tzu\'s Art of War and its enduring influence on modern leadership, business strategy, negotiation, and decision-making under uncertainty.'

hero = download_hero(0, slug)

article = {
    'id': 'artofwar-01',
    'slug': slug,
    'category': 'Strategy',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-10',
    'updatedDate': '2026-08-10',
    'readingTime': 25,
    'featured': False,
    'draft': False,
    'tags': ['Sun Tzu', 'Art of War', 'strategy', 'leadership', 'negotiation', 'military history', 'business strategy', 'decision-making'],
    'en': {
        'title': title,
        'excerpt': excerpt,
        'content': content,
        'metaTitle': 'The Art of War: Strategic Principles for Modern Leadership - Ashraf El Desoky, PMP',
        'metaDescription': 'How Sun Tzu\'s Art of War still shapes leadership, business, negotiation, and decision-making. A 5,500-word analysis with modern examples.',
        'keywords': ['Art of War', 'Sun Tzu', 'strategic principles', 'leadership strategy', 'business strategy', 'negotiation', 'military strategy', 'decision-making', 'competitive strategy', 'game theory']
    },
    'ar': {
        'title': title,
        'excerpt': excerpt,
        'content': content,
        'metaTitle': title + ' - أشرف الدسوقي, PMP',
        'metaDescription': excerpt,
        'keywords': ['Art of War', 'Sun Tzu', 'strategic principles', 'leadership strategy', 'business strategy']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
print(f'Hero image: {hero}')
