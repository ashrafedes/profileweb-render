import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = 'procurement-and-disposal-methods-guide'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
en_content = read_file(os.path.join(basepath, 'procurement_methods_article.txt'))
ar_content = read_file(os.path.join(basepath, 'procurement_methods_article_ar.txt'))

en_title = 'Procurement and Disposal Methods: A Comprehensive Engineering and Regulatory Guide'
for line in en_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        en_title = line[2:].strip()
        break

ar_title = 'أساليب التعاقد والتصرف: دليل هندسي وتنظيمي شامل'
for line in ar_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        ar_title = line[2:].strip()
        break

en_excerpt = 'A comprehensive guide to public procurement and disposal methods: public tender, direct contracting, limited competition, direct purchase, framework agreements, two-stage competition, design competitions, industry localization, public auction, sealed bid sale, direct sale, and investment bidding — with evaluation formulas, risk analysis, and digital transformation insights.'

ar_excerpt = 'دليل شامل لأساليب التعاقد والتصرف في المشتريات العامة: المناقصة العامة، الممارسة، المنافسة المحدودة، الشراء المباشر، الاتفاقية الإطارية، المنافسة على مرحلتين، المسابقة، توطين الصناعة، البيع بالمزاد العلني، الظروف المختومة، البيع المباشر، والمزايدة الاستثمارية — مع صيغ تقييم وتحليل مخاطر ورؤى التحول الرقمي.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': 'procurement-methods-01',
    'slug': slug,
    'category': 'Project Management',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-20',
    'updatedDate': '2026-08-20',
    'readingTime': 32,
    'featured': False,
    'draft': False,
    'tags': ['procurement', 'public tender', 'contracting', 'disposal methods', 'auction', 'framework agreement', 'two-stage competition', 'localization', 'investment bidding', 'government procurement', 'project management'],
    'en': {
        'title': en_title,
        'excerpt': en_excerpt,
        'content': en_content,
        'metaTitle': 'Procurement and Disposal Methods Guide - Public Tender, Auction, Framework Agreements - Ashraf El Desoky',
        'metaDescription': 'Comprehensive guide to government procurement and disposal methods: public tender, direct contracting, limited competition, framework agreements, two-stage competition, design competitions, localization, auctions, sealed bids, investment bidding with formulas and risk analysis.',
        'keywords': ['procurement methods', 'public tender', 'direct contracting', 'limited competition', 'framework agreement', 'two-stage competition', 'design competition', 'industry localization', 'public auction', 'sealed bid sale', 'direct sale', 'investment bidding', 'government procurement law', 'disposal methods']
    },
    'ar': {
        'title': ar_title,
        'excerpt': ar_excerpt,
        'content': ar_content,
        'metaTitle': ar_title + ' - أشرف الدسوقي',
        'metaDescription': ar_excerpt,
        'keywords': ['أساليب التعاقد', 'المناقصة العامة', 'الممارسة', 'المنافسة المحدودة', 'الشراء المباشر', 'الاتفاقية الإطارية', 'المنافسة على مرحلتين', 'المسابقة', 'توطين الصناعة', 'المزاد العلني', 'الظروف المختومة', 'البيع المباشر', 'المزايدة الاستثمارية', 'المشتريات الحكومية']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
