import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = 'agile-methodology-mega-projects'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
en_content = read_file(os.path.join(basepath, 'agile_mega_article.txt'))
ar_content = read_file(os.path.join(basepath, 'agile_mega_article_ar.txt'))

en_title = 'Agile Methodology for Mega Projects'
for line in en_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        en_title = line[2:].strip()
        break

ar_title = 'منهجية أجايل لإدارة المشاريع الضخمة'
for line in ar_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        ar_title = line[2:].strip()
        break

en_excerpt = 'A comprehensive engineering study of applying agile methodology to billion-dollar mega projects: framework selection (SAFe, LeSS, Nexus, Spotify), contract restructuring (progressive fixed-price, target cost, IPD), governance adaptation, risk management, EVM integration, and real-world case studies from FTTH rollout, hospital complex, and high-speed rail programs.'

ar_excerpt = 'دراسة هندسية شاملة لتطبيق منهجية أجايل على المشاريع الضخمة بمليارات الدولارات: اختيار الإطار (SAFe، LeSS، Nexus، Spotify)، إعادة هيكلة العقود، تكييف الحوكمة، إدارة المخاطر، تكامل EVM، ودراسات حالة واقعية من شبكة FTTH الوطنية ومجمع طبي وإشارات سكك حديدية عالية السرعة.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': 'agile-mega-01',
    'slug': slug,
    'category': 'Project Management',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-20',
    'updatedDate': '2026-08-20',
    'readingTime': 35,
    'featured': False,
    'draft': False,
    'tags': ['agile', 'mega projects', 'SAFe', 'LeSS', 'scaled agile', 'project management', 'EVM', 'governance', 'contract structures', 'IPD', 'risk management'],
    'en': {
        'title': en_title,
        'excerpt': en_excerpt,
        'content': en_content,
        'metaTitle': 'Agile Methodology for Mega Projects - Scaling Beyond Teams - Ashraf El Desoky, PMP',
        'metaDescription': 'Comprehensive study of agile on billion-dollar mega projects: SAFe/LeSS framework selection, contract restructuring, governance adaptation, risk management, EVM integration, and case studies with equations and analysis.',
        'keywords': ['agile mega projects', 'scaled agile framework', 'SAFe', 'LeSS', 'agile project management', 'mega project delivery', 'agile EVM', 'IPD contracts', 'progressive fixed price', 'agile governance', 'agile transformation']
    },
    'ar': {
        'title': ar_title,
        'excerpt': ar_excerpt,
        'content': ar_content,
        'metaTitle': ar_title + ' - أشرف الدسوقي',
        'metaDescription': ar_excerpt,
        'keywords': ['أجايل المشاريع الضخمة', 'إطار أجايل الموسع', 'SAFe', 'LeSS', 'إدارة المشاريع الرشيقة', 'تسليم المشاريع الضخمة', 'EVM الرشيق', 'عقود IPD', 'الحوكمة الرشيقة', 'تحول أجايل']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
