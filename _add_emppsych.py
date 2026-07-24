import sys, os, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _neg2_utils import load_articles, save_articles, read_file

articles = load_articles()

slug = 'employee-psychology-workplace-productivity'
if any(a.get('slug') == slug for a in articles):
    print(f'{slug} already exists, skipping')
    sys.exit(0)

basepath = os.path.dirname(os.path.abspath(__file__))
content = read_file(os.path.join(basepath, 'employee_psychology_article.txt'))

title = 'علم نفس الموظف في العمل: تأثير الزملاء والضغط الوظيفي والرضا المالي على الإنتاجية والاستمرارية والارتياح النفسي'
for line in content.split('\n'):
    line = line.strip()
    if line.startswith('# '):
        title = line[2:].strip()
        break

excerpt = 'تحليل عميق لعلم نفس الموظف في بيئة العمل: كيف تؤثر العلاقات مع الزملاء والضغط الوظيفي المزمن وقلة الراتب على الإنتاجية والاستمرارية الوظيفية والارتياح النفسي.'

hero = '/assets/images/articles/art-of-war-strategic-principles-hero.jpeg'

article = {
    'id': 'emppsych-01',
    'slug': slug,
    'category': 'Organizational Psychology',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': hero,
    'publishDate': '2026-08-11',
    'updatedDate': '2026-08-11',
    'readingTime': 20,
    'featured': False,
    'draft': False,
    'tags': ['employee psychology', 'workplace productivity', 'work stress', 'salary satisfaction', 'organizational behavior', 'burnout', 'workplace culture', 'mental health'],
    'en': {
        'title': 'Employee Psychology in the Workplace: How Colleagues, Work Pressure, and Salary Satisfaction Affect Productivity and Mental Wellbeing',
        'excerpt': 'A deep analysis of employee psychology: how workplace relationships, chronic stress, and salary dissatisfaction impact productivity, retention, and psychological wellbeing.',
        'content': content,
        'metaTitle': 'Employee Psychology: Workplace Productivity, Stress & Salary - Ashraf El Desoky',
        'metaDescription': 'How colleagues, work pressure, and salary affect employee productivity, retention, and psychological wellbeing. Evidence-based organizational psychology analysis.',
        'keywords': ['employee psychology', 'workplace productivity', 'work stress', 'salary satisfaction', 'burnout', 'organizational behavior', 'workplace culture', 'mental health', 'employee engagement']
    },
    'ar': {
        'title': title,
        'excerpt': excerpt,
        'content': content,
        'metaTitle': title + ' - أشرف الدسوقي',
        'metaDescription': excerpt,
        'keywords': ['علم نفس الموظف', 'الإنتاجية في العمل', 'الضغط الوظيفي', 'الرضا المالي', 'الاحتراق الوظيفي', 'السلوك التنظيمي', 'الصحة النفسية', 'ثقافة العمل']
    }
}

articles.append(article)
save_articles(articles)
print(f'Added: {slug}')
print(f'Total articles: {len(articles)}')
print(f'Hero image: {hero}')
