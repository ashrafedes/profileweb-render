import json
with open('articles/articles.json', 'r', encoding='utf-8') as f:
    articles = json.load(f)
max_id = max(a['id'] for a in articles if isinstance(a.get('id'), int))
print(f'Max ID: {max_id}')
print(f'Total: {len(articles)}')
