import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = 'low-voltage-network-distribution-engineering'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
en_content = read_file(os.path.join(basepath, 'lv_distribution_article.txt'))
ar_content = read_file(os.path.join(basepath, 'lv_distribution_ar.txt'))

en_title = 'Low Voltage Network Distribution: Engineering Principles, Design Methodology, and System Optimization for Modern Power Networks'
for line in en_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        en_title = line[2:].strip()
        break

ar_title = 'شبكات توزيع الجهد المنخفض: المبادئ الهندسية ومنهجية التصميم وتحسين النظم لشبكات الطاقة الحديثة'
for line in ar_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        ar_title = line[2:].strip()
        break

en_excerpt = 'A comprehensive engineering analysis of low voltage network distribution: topological configurations, transformer sizing, conductor optimization, voltage regulation, short-circuit analysis, protection coordination, power quality, distributed generation integration, and smart grid evolution with mathematical formulations.'

ar_excerpt = 'تحليل هندسي شامل لشبكات توزيع الجهد المنخفض: التكوينات الطوبولوجية وتحديد حجم المحولات وتحسين الموصلات وتنظيم الجهد وتحليل القصر وتنسيق الحماية وجودة الطاقة ودمج التوليد الموزع وتطور الشبكة الذكية مع صيغ رياضية.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': 'lvdist-01',
    'slug': slug,
    'category': 'Electrical Engineering',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-12',
    'updatedDate': '2026-08-12',
    'readingTime': 25,
    'featured': False,
    'draft': False,
    'tags': ['low voltage', 'power distribution', 'electrical engineering', 'voltage regulation', 'short circuit analysis', 'protection coordination', 'power quality', 'smart grid', 'distributed generation'],
    'en': {
        'title': en_title,
        'excerpt': en_excerpt,
        'content': en_content,
        'metaTitle': 'Low Voltage Network Distribution Engineering - Ashraf El Desoky, PMP',
        'metaDescription': 'Comprehensive engineering guide to LV network distribution: topology, transformer sizing, conductor optimization, voltage regulation, protection coordination, power quality, and smart grid integration with equations.',
        'keywords': ['low voltage distribution', 'LV network design', 'power distribution engineering', 'voltage drop calculation', 'short circuit analysis', 'protection coordination', 'power factor correction', 'distributed generation', 'EV charging impact', 'smart grid']
    },
    'ar': {
        'title': ar_title,
        'excerpt': ar_excerpt,
        'content': ar_content,
        'metaTitle': ar_title + ' - أشرف الدسوقي',
        'metaDescription': ar_excerpt,
        'keywords': ['توزيع الجهد المنخفض', 'تصميم شبكات LV', 'هندسة توزيع الطاقة', 'حساب هبوط الجهد', 'تحليل القصر', 'تنسيق الحماية', 'تصحيح معامل القدرة', 'التوليد الموزع', 'تأثير شحن السيارات الكهربائية', 'الشبكة الذكية']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
