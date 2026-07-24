import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = 'hospital-information-system-engineering'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
en_content = read_file(os.path.join(basepath, 'his_article.txt'))
ar_content = read_file(os.path.join(basepath, 'his_article_ar.txt'))

en_title = 'Hospital Information Systems (HIS): A Comprehensive Engineering Study'
for line in en_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        en_title = line[2:].strip()
        break

ar_title = 'نظم معلومات المستشفيات (HIS): دراسة هندسية شاملة'
for line in ar_content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        ar_title = line[2:].strip()
        break

en_excerpt = 'A deep engineering study of Hospital Information Systems: architecture evolution from monolithic to microservices, HL7 FHIR interoperability, DICOM imaging standards, clinical decision support systems, security and HIPAA compliance, performance engineering, queue theory in hospital operations, revenue cycle management, and emerging AI/blockchain/IoMT technologies.'

ar_excerpt = 'دراسة هندسية شاملة لنظم معلومات المستشفيات: تطور المعمارية من النظم الموحدة إلى الخدمات المصغرة، التشغيل البيني HL7 FHIR، معايير تصوير DICOM، نظم دعم القرار السريري، الأمان والامتثال لـ HIPAA، هندسة الأداء، نظرية الطوابير في عمليات المستشفيات، إدارة دورة الإيرادات، والتقنيات الناشئة كالذكاء الاصطناعي والبلوكتشين وإنترنت الأشياء الطبي.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': 'his-01',
    'slug': slug,
    'category': 'Healthcare IT',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-15',
    'updatedDate': '2026-08-15',
    'readingTime': 30,
    'featured': False,
    'draft': False,
    'tags': ['HIS', 'hospital information system', 'healthcare IT', 'HL7', 'FHIR', 'DICOM', 'EHR', 'clinical decision support', 'HIPAA', 'interoperability', ' healthcare engineering'],
    'en': {
        'title': en_title,
        'excerpt': en_excerpt,
        'content': en_content,
        'metaTitle': 'Hospital Information Systems Engineering - Ashraf El Desoky, PMP',
        'metaDescription': 'Comprehensive engineering study of HIS: architecture, HL7 FHIR, DICOM, CDSS, security, HIPAA compliance, performance, and emerging technologies with equations and analysis.',
        'keywords': ['hospital information system', 'HIS engineering', 'HL7 FHIR', 'DICOM', 'EHR architecture', 'clinical decision support', 'HIPAA compliance', 'healthcare interoperability', 'PACS', 'revenue cycle management', 'healthcare AI']
    },
    'ar': {
        'title': ar_title,
        'excerpt': ar_excerpt,
        'content': ar_content,
        'metaTitle': ar_title + ' - أشرف الدسوقي',
        'metaDescription': ar_excerpt,
        'keywords': ['نظم معلومات المستشفيات', 'هندسة HIS', 'HL7 FHIR', 'DICOM', 'معمارية EHR', 'دعم القرار السريري', 'الامتثال لـ HIPAA', 'التشغيل البيني الصحي', 'PACS', 'إدارة دورة الإيرادات', 'الذكاء الاصطناعي الصحي']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
