import json, os
from _mep_images import load_articles, save_articles, make_article, download_hero

def read_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        return f.read().strip()

articles = load_articles()
next_id = max(a['id'] for a in articles) + 1

# Article 1: MEP in Construction
a1_en = read_file('mep_a1_en.txt')
a1_ar = read_file('mep_a1_ar.txt')
hero1 = download_hero(0, 'mep-in-construction-complete-technical-guide')
art1 = make_article(
    next_id, 'mep-in-construction-complete-technical-guide',
    'Construction Engineering',
    ['MEP', 'Mechanical', 'Electrical', 'Plumbing', 'HVAC', 'Construction', 'Building Services'],
    {'title': 'MEP in Construction: Complete Technical Guide for Engineers',
     'excerpt': 'Comprehensive technical guide to Mechanical, Electrical and Plumbing (MEP) systems in construction covering design coordination, installation, BIM integration, commissioning and quality control for expert engineers.',
     'keywords': ['MEP', 'MEP construction', 'mechanical electrical plumbing', 'HVAC', 'building services', 'MEP coordination', 'MEP BIM', 'plumbing systems', 'electrical systems', 'fire protection', 'MEP commissioning', 'MEP design'],
     'content': a1_en},
    {'title': 'MEP في الإنشاءات: دليل تقني شامل للمهندسين',
     'excerpt': 'دليل تقني شامل لأنظمة الميكانيكا والكهرباء والصحي (MEP) في الإنشاءات يغطي تصميم التنسيق والتركيب وتكامل BIM والتشغيل التجريبي ومراقبة الجودة للمهندسين الخبراء.',
     'keywords': ['MEP', 'MEP في الإنشاءات', 'ميكانيكا كهرباء صحي', 'HVAC', 'خدمات المباني', 'تنسيق MEP', 'BIM MEP', 'أنظمة الصحي', 'الأنظمة الكهربائية', 'الحماية من الحرائق', 'تشغيل MEP', 'تصميم MEP'],
     'content': a1_ar},
    hero1, date_offset=0, reading_time=15
)
articles.append(art1)
print(f'Added article {next_id}: MEP in Construction')
next_id += 1

# Article 2: Consulting Services
a2_en = read_file('mep_a2_en.txt')
a2_ar = read_file('mep_a2_ar.txt')
hero2 = download_hero(1, 'consulting-services-in-construction-technical-guide')
art2 = make_article(
    next_id, 'consulting-services-in-construction-technical-guide',
    'Construction Engineering',
    ['Consulting', 'Construction', 'Engineering', 'Project Management', 'Design Review', 'Supervision', 'FIDIC'],
    {'title': 'Consulting Services in Construction: Technical Guide for Engineers',
     'excerpt': 'Comprehensive guide to construction consulting services covering design review, supervision, technical advisory, value engineering, feasibility studies, and the consultant-executor relationship for expert engineers.',
     'keywords': ['consulting services construction', 'construction consultant', 'engineering consultant', 'design review', 'supervision consultant', 'value engineering', 'feasibility study', 'technical advisory', 'construction management', 'consultant responsibilities', 'FIDIC', 'engineer role'],
     'content': a2_en},
    {'title': 'خدمات الاستشارات في الإنشاءات: دليل تقني للمهندسين',
     'excerpt': 'دليل شامل لخدمات الاستشارات في الإنشاءات يغطي مراجعة التصميم والإشراف والاستشارات التقنية وهندسة القيمة ودراسات الجدوى وعلاقة الاستشاري بالمنفذ للمهندسين الخبراء.',
     'keywords': ['خدمات استشارات إنشاءات', 'استشاري إنشاءات', 'استشاري هندسي', 'مراجعة تصميم', 'استشاري إشراف', 'هندسة القيمة', 'دراسة جدوى', 'استشارات تقنية', 'إدارة الإنشاءات', 'مسؤوليات الاستشاري', 'FIDIC', 'دور المهندس'],
     'content': a2_ar},
    hero2, date_offset=1, reading_time=12
)
articles.append(art2)
print(f'Added article {next_id}: Consulting Services')
next_id += 1

# Article 3: Document Types and Work Cycle
a3_en = read_file('mep_a3_en.txt')
a3_ar = read_file('mep_a3_ar.txt')
hero3 = download_hero(2, 'construction-document-types-and-consultant-contractor-work-cycle')
art3 = make_article(
    next_id, 'construction-document-types-and-consultant-contractor-work-cycle',
    'Construction Engineering',
    ['Documents', 'Construction', 'Consultant', 'Contractor', 'Work Cycle', 'Shop Drawings', 'Quality Control', 'FIDIC'],
    {'title': 'Construction Document Types and Consultant-Contractor Work Cycle: Technical Guide',
     'excerpt': 'Complete technical guide to construction document types (shop drawings, method statements, ITPs, NCRs) and the step-by-step work cycle between consultant and execution companies for expert engineers.',
     'keywords': ['construction documents', 'document types construction', 'shop drawings', 'method statement', 'inspection request', 'non-conformance report', 'ITP', 'consultant contractor cycle', 'work cycle construction', 'document control', 'construction quality', 'FIDIC documents'],
     'content': a3_en},
    {'title': 'أنواع وثائق الإنشاءات ودورة العمل بين الاستشاري والمقاول: دليل تقني',
     'excerpt': 'دليل تقني شامل لأنواع وثائق الإنشاءات (رسومات ورشة، بيانات طرق، ITP، NCR) ودورة العمل خطوة بخطوة بين الاستشاري وشركات التنفيذ للمهندسين الخبراء.',
     'keywords': ['وثائق الإنشاءات', 'أنواع الوثائق', 'رسومات ورشة', 'بيان طريقة', 'طلب تفتيش', 'تقرير عدم مطابقة', 'ITP', 'دورة الاستشاري والمقاول', 'دورة العمل', 'مراقبة الوثائق', 'جودة الإنشاءات', 'وثائق FIDIC'],
     'content': a3_ar},
    hero3, date_offset=2, reading_time=12
)
articles.append(art3)
print(f'Added article {next_id}: Document Types and Work Cycle')

save_articles(articles)
print(f'\nTotal articles: {len(articles)}')
print('Done! All 3 articles added to articles.json')
