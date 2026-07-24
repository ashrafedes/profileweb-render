import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = '5g-mobile-technology-architecture-devices-design'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
en_content = read_file(os.path.join(basepath, '5g_mobile_article.txt'))
ar_content = read_file(os.path.join(basepath, '5g_mobile_article_ar.txt'))

en_title = '5G Mobile Technology: Architecture, Devices, and Design Engineering'
for line in en_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        en_title = line[2:].strip()
        break

ar_title = 'تقنية الجيل الخامس للهواتف المحمولة: الهندسة المعمارية والأجهزة والتصميم'
for line in ar_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        ar_title = line[2:].strip()
        break

en_excerpt = 'A deep engineering study of 5G mobile technology covering New Radio air interface, FR1/FR2 spectrum, massive MIMO, beamforming, 5G Core SBA, network slicing, Open RAN, device RF front-end and antenna design, link budget, coverage-capacity trade-offs, URLLC, private 5G, security, and the path to 5G-Advanced and 6G.'

ar_excerpt = 'دراسة هندسية معمقة في تقنية الجيل الخامس تغطي واجهة New Radio، طيف FR1/FR2، MIMO الضخم، التشكيل الحزمي، نواة 5G SBA، تقطيع الشبكة، Open RAN، تصميم الواجهة الراديوية والهوائيات للأجهزة، ميزانية الارتباط، مفاضلات التغطية والسعة، URLLC، شبكات 5G الخاصة، الأمان، والطريق إلى 5G-Advanced و6G.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': '5g-mobile-01',
    'slug': slug,
    'category': 'Telecommunications',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-20',
    'updatedDate': '2026-08-20',
    'readingTime': 30,
    'featured': False,
    'draft': False,
    'tags': ['5G', '5G NR', 'mmWave', 'massive MIMO', 'network slicing', 'Open RAN', 'RF design', 'URLLC', 'private 5G', 'telecommunications'],
    'en': {
        'title': en_title,
        'excerpt': en_excerpt,
        'content': en_content,
        'metaTitle': '5G Mobile Technology Architecture, Devices, and Design - Ashraf El Desoky',
        'metaDescription': 'In-depth engineering study of 5G mobile networks: New Radio, spectrum, massive MIMO, beamforming, 5G Core, slicing, Open RAN, device RF design, link budgets, URLLC, private 5G, and 6G roadmap.',
        'keywords': ['5G', '5G NR', 'mobile network architecture', 'massive MIMO', 'beamforming', '5G core', 'network slicing', 'Open RAN', '5G device design', 'RF front end', 'URLLC', 'private 5G', 'link budget', '5G-Advanced']
    },
    'ar': {
        'title': ar_title,
        'excerpt': ar_excerpt,
        'content': ar_content,
        'metaTitle': ar_title + ' - أشرف الدسوقي',
        'metaDescription': ar_excerpt,
        'keywords': ['5G', 'الجيل الخامس', 'هندسة شبكات الهاتف', 'تقنية 5G', '5G NR', 'MIMO الضخم', 'تشكيل حزمي', 'نواة 5G', 'تقطيع الشبكة', 'Open RAN', 'تصميم أجهزة 5G', 'URLLC', 'شبكات 5G الخاصة', 'ميزانية ارتباط', '5G-Advanced']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
