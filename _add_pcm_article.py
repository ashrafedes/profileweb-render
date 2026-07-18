import json, os
from datetime import datetime, timedelta

ARTICLES_JSON = 'articles/articles.json'
SITE_URL = 'https://www.ashraf-eldesoky.space'

def load_articles():
    with open(ARTICLES_JSON, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_articles(articles):
    with open(ARTICLES_JSON, 'w', encoding='utf-8') as f:
        json.dump(articles, f, ensure_ascii=False, indent=2)

def download_image(url, filepath):
    try:
        import urllib.request
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=30) as resp:
            with open(filepath, 'wb') as f:
                f.write(resp.read())
        return True
    except Exception as e:
        print(f'  WARNING: Failed to download {url}: {e}')
        return False

HERO_URL = 'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200'

ARTICLE = {
    'slug': 'project-controls-manager-complete-guide',
    'category': 'Project Management',
    'tags': ['Project Controls Manager', 'Project Controls', 'EVM', 'Planning', 'Cost Control', 'PMP'],
    'en': {
        'title': 'Project Controls Manager: Complete Guide to Roles, Skills & Career Path',
        'excerpt': 'Everything you need to know about the Project Controls Manager role — responsibilities, key skills, tools, certifications, salary expectations, and career progression in 2026.',
        'keywords': ['project controls manager', 'project controls', 'project control manager', 'cost control manager', 'planning manager', 'EVM', 'earned value management', 'Primavera P6', 'PMP certification', 'project controls career', 'project controls salary', 'project controls responsibilities'],
        'content': """## What is a Project Controls Manager?

A **Project Controls Manager** is a senior project management professional responsible for overseeing the planning, monitoring, and controlling of project performance across cost, schedule, quality, and risk dimensions. The Project Controls Manager serves as the critical link between project execution teams and executive leadership, ensuring that projects are delivered on time, within budget, and to the required quality standards.

Unlike a traditional Project Manager who focuses on overall project delivery, the Project Controls Manager specializes in the **analytical and governance aspects** of project management — the systems, processes, and tools that provide visibility and control over project performance.

## Key Responsibilities of a Project Controls Manager

### Planning and Scheduling
- Develop and maintain master project schedules using Primavera P6 or MS Project
- Define Work Breakdown Structures (WBS) aligned with project scope
- Establish baseline schedules with critical path analysis
- Monitor schedule performance and identify variances
- Implement schedule recovery plans when delays occur

### Cost Control and Budgeting
- Develop project budgets and cost estimates
- Track actual costs against baseline budgets
- Manage cash flow projections and forecasts
- Implement change control processes for budget modifications
- Report cost variances and recommend corrective actions

### Earned Value Management (EVM)
- Implement EVM systems to measure project performance
- Calculate key metrics: CPI, SPI, EAC, ETC, VAC
- Analyse trends and forecast project outcomes
- Report EVM metrics to stakeholders and executives

### Risk Management
- Facilitate risk identification workshops
- Maintain project risk registers
- Develop risk response strategies
- Monitor risk triggers and implement mitigation plans
- Report risk exposure to project leadership

### Reporting and Communication
- Prepare weekly, monthly, and executive progress reports
- Develop KPI dashboards using Power BI or Excel
- Present project status to steering committees
- Maintain project documentation and audit trails

### Team Leadership
- Lead a team of planners, cost engineers, and risk analysts
- Mentor junior project controls staff
- Coordinate with discipline leads and package managers
- Establish project controls standards and procedures

## Essential Skills for a Project Controls Manager

### Technical Skills
- **Scheduling tools:** Primavera P6, MS Project, Asta Powerproject
- **Cost management:** Cost estimating, budgeting, forecasting
- **EVM:** Earned Value Management per ANSI/EIA-748 standard
- **Data analytics:** Power BI, Advanced Excel, SQL
- **Risk analysis:** Monte Carlo simulation, quantitative risk analysis
- **Project management:** PMP, PRINCE2, APM qualifications

### Soft Skills
- **Analytical thinking:** Ability to interpret complex data sets
- **Communication:** Present technical information to non-technical stakeholders
- **Leadership:** Guide and develop project controls teams
- **Problem-solving:** Identify issues and propose solutions proactively
- **Attention to detail:** Precision in reporting and analysis
- **Stakeholder management:** Build relationships across all project levels

## Certifications That Boost Your Project Controls Career

### Essential Certifications
1. **PMP® (Project Management Professional):** The gold standard from PMI — demonstrates comprehensive project management knowledge
2. **PRINCE2®:** Process-based project management certification widely recognised in Europe and Middle East
3. **ACP® (Agile Certified Practitioner):** For projects using agile methodologies

### Specialised Certifications
4. **EVM Certification:** Earned Value Professional (EVP) from AACE International
5. **CCP (Certified Cost Professional):** From AACE International for cost engineering
6. **PSP (Planning & Scheduling Professional):** From AACE International for scheduling
7. **RMP (Risk Management Professional):** From PMI for risk management specialists
8. **Primavera P6 Certification:** Oracle Primavera certified specialist

## Project Controls Manager Salary Expectations (2026)

### By Region
- **Saudi Arabia:** SAR 25,000 – 45,000/month (tax-free)
- **UAE:** AED 25,000 – 50,000/month (tax-free)
- **United Kingdom:** £70,000 – £120,000/year
- **United States:** $120,000 – $180,000/year
- **Australia:** AUD 150,000 – $220,000/year
- **Egypt:** EGP 50,000 – 120,000/month

### By Industry
- **Oil & Gas:** Highest paying — 20-30% premium
- **Construction & Infrastructure:** Strong demand and competitive salaries
- **Telecommunications:** Growing demand with 5G and FTTH rollouts
- **Healthcare:** Stable demand for hospital and medical facility projects
- **Railway & Transport:** Major projects driving demand globally

## Career Progression Path

### Entry Level (0-5 years)
- Project Controls Engineer
- Planning Engineer
- Cost Engineer
- Junior Scheduler

### Mid Level (5-10 years)
- Senior Project Controls Engineer
- Lead Planner
- Senior Cost Engineer
- Risk Analyst

### Senior Level (10-15 years)
- **Project Controls Manager**
- Lead Project Controls Consultant
- Programme Controls Manager

### Executive Level (15+ years)
- Director of Project Controls
- Head of PMO
- VP of Project Management
- Chief Project Officer

## Tools Every Project Controls Manager Should Master

### Scheduling
- **Primavera P6:** Industry standard for large-scale projects
- **MS Project:** Widely used for mid-size projects
- **Asta Powerproject:** Popular in Europe and construction

### Cost and EVM
- **Oracle Primavera Costing:** Integrated cost management
- **SAP Project System:** Enterprise project cost tracking
- **Custom EVM tools:** Excel-based or proprietary systems

### Reporting and Dashboards
- **Power BI:** Leading dashboard and visualisation tool
- **Tableau:** Advanced data visualisation
- **Advanced Excel:** Pivot tables, Power Query, VBA

### Risk Management
- **@RISK:** Monte Carlo simulation for Excel
- **Primavera Risk Analysis (PRA):** Schedule risk analysis
- **Custom risk registers:** Excel or database-based

## Industries That Need Project Controls Managers

### Telecommunications
The telecom sector has massive demand for Project Controls Managers, particularly for 5G rollout, FTTH network deployment, and data centre construction. Project Controls Managers in telecom manage complex multi-site programmes with thousands of concurrent activities.

### Construction and Infrastructure
Mega-projects in construction — airports, railways, highways, smart cities — require experienced Project Controls Managers to manage budgets often exceeding billions of dollars.

### Oil and Gas
The highest-paying sector for Project Controls Managers, with complex EPC (Engineering, Procurement, Construction) projects requiring rigorous cost and schedule control.

### Healthcare
Hospital construction, medical facility fit-out, and healthcare IT implementation projects all require project controls expertise.

### Railway and Transport
High-speed rail, metro systems, and national railway modernisation programmes are major employers of Project Controls Managers.

## How to Become a Project Controls Manager

### Step 1: Get the Right Education
- Bachelor's degree in Engineering, Construction Management, or related field
- Master's degree (MBA or MSc Project Management) for senior roles
- Specialised courses in planning, cost control, and EVM

### Step 2: Gain Hands-On Experience
- Start as a Planning Engineer or Cost Engineer
- Work on diverse project types and sizes
- Gain experience with Primavera P6 and MS Project
- Learn EVM implementation on real projects

### Step 3: Get Certified
- Obtain PMP® certification — essential for credibility
- Add specialised certifications (EVP, CCP, PSP)
- Complete Primavera P6 formal training

### Step 4: Develop Leadership Skills
- Take on team leadership roles
- Mentor junior staff
- Present to executive audiences
- Build cross-functional relationships

### Step 5: Build a Track Record
- Document successful project deliveries
- Build a portfolio of project controls deliverables
- Network with industry professionals
- Contribute to professional bodies (PMI, AACE)

## Common Challenges Faced by Project Controls Managers

- **Data quality:** Ensuring accurate and timely data from project teams
- **Resistance to processes:** Overcoming team reluctance to follow controls procedures
- **Tool limitations:** Working with inadequate or legacy systems
- **Scope creep:** Managing uncontrolled scope changes
- **Multi-project coordination:** Balancing priorities across concurrent projects
- **Executive communication:** Translating technical data for decision-makers

## Best Practices for Effective Project Controls

1. **Establish baselines early:** Set schedule and cost baselines before execution begins
2. **Implement robust change control:** No changes without formal impact assessment
3. **Use EVM consistently:** Regular EVM reporting provides early warning of problems
4. **Maintain data integrity:** Ensure all data is current, accurate, and auditable
5. **Communicate proactively:** Don't wait for problems — report trends and forecasts
6. **Invest in tools:** Use professional-grade scheduling and reporting tools
7. **Train your team:** Continuous improvement in project controls skills
8. **Learn from lessons:** Conduct post-project reviews and apply learnings

## Conclusion

The **Project Controls Manager** role is one of the most critical positions in project-based organisations. It combines technical expertise in planning, cost control, and risk management with leadership and communication skills. As projects become increasingly complex and budgets grow, the demand for skilled Project Controls Managers continues to rise across all major industries.

For professionals looking to advance their project controls career, the path is clear: build technical skills, gain diverse project experience, obtain professional certifications, and develop the leadership qualities needed to guide project controls functions at the highest level."""
    },
    'ar': {
        'title': 'مدير ضوابط المشاريع: دليل شامل للأدوار والمهارات والمسار المهني',
        'excerpt': 'كل ما تحتاج معرفته عن دور مدير ضوابط المشاريع — المسؤوليات والمهارات الرئيسية والأدوات والشهادات وتوقعات الراتب والتطور المهني في 2026.',
        'keywords': ['مدير ضوابط المشاريع', 'ضوابط المشاريع', 'project controls manager', 'مدير مراقبة التكاليف', 'مدير التخطيط', 'EVM', 'القيمة المكتسبة', 'Primavera P6', 'شهادة PMP', 'مسار ضوابط المشاريع', 'راتب ضوابط المشاريع', 'مسؤوليات ضوابط المشاريع'],
        'content': """## ما هو مدير ضوابط المشاريع؟

**مدير ضوابط المشاريع** هو محترف إدارة مشاريع كبير مسؤول عن الإشراف على تخطيط ومراقبة والتحكم في أداء المشروع عبر أبعاد التكلفة والجدول الزمني والجودة والمخاطر. يعمل مدير ضوابط المشاريع كحلقة الوصل الحرجة بين فرق تنفيذ المشاريع والقيادة التنفيذية، مما يضمن تسليم المشاريع في الوقت المحدد وضمن الميزانية ووفقاً لمعايير الجودة المطلوبة.

على عكس مدير المشروع التقليدي الذي يركز على تسليم المشروع بشكل عام، يتخصص مدير ضوابط المشاريع في **الجوانب التحليلية والحوكمة** لإدارة المشاريع — الأنظمة والعمليات والأدوات التي توفر الرؤية والتحكم في أداء المشروع.

## المسؤوليات الرئيسية لمدير ضوابط المشاريع

### التخطيط والجدولة
- تطوير وصيانة الجداول الزمنية الرئيسية للمشروع باستخدام Primavera P6 أو MS Project
- تحديد هياكل تقسيم العمل (WBS) المتوافقة مع نطاق المشروع
- إنشاء جداول أساسية مع تحليل المسار الحرج
- مراقبة أداء الجدول وتحديد الانحرافات
- تنفيذ خطط استرداد الجدول عند حدوث تأخيرات

### مراقبة التكاليف والميزانية
- تطوير ميزانيات المشروع وتقديرات التكلفة
- تتبع التكاليف الفعلية مقابل الميزانيات الأساسية
- إدارة توقعات التدفق النقدي والتنبؤات
- تنفيذ عمليات ضبط التغيير لتعديلات الميزانية
- الإبلاغ عن انحرافات التكلفة والتوصية بإجراءات تصحيحية

### إدارة القيمة المكتسبة (EVM)
- تنفيذ أنظمة EVM لقياس أداء المشروع
- حساب المؤشرات الرئيسية: CPI، SPI، EAC، ETC، VAC
- تحليل الاتجاهات والتنبؤ بنتائج المشروع
- الإبلاغ عن مقاييس EVM لأصحاب المصلحة والتنفيذيين

### إدارة المخاطر
- تسهيل ورش تحديد المخاطر
- صيانة سجلات مخاطر المشروع
- تطوير استراتيجيات الاستجابة للمخاطر
- مراقبة محفزات المخاطر وتنفيذ خطط التخفيف
- الإبلاغ عن التعرض للمخاطر لقيادة المشروع

### التقارير والتواصل
- إعداد تقارير تقدم أسبوعية وشهرية وتنفيذية
- تطوير لوحات KPI باستخدام Power BI أو Excel
- تقديم حالة المشروع للجان التوجيه
- صيانة وثائق المشروع ومسارات التدقيق

### قيادة الفريق
- قيادة فريق من المخططين ومهندسي التكاليف ومحللي المخاطر
- توجيه موظفي ضوابط المشاريع المبتدئين
- التنسيق مع قادة التخصصات ومديري الحزم
- إنشاء معايير وإجراءات ضوابط المشاريع

## المهارات الأساسية لمدير ضوابط المشاريع

### المهارات التقنية
- **أدوات الجدولة:** Primavera P6، MS Project، Asta Powerproject
- **إدارة التكاليف:** تقدير التكاليف، الميزانية، التنبؤ
- **EVM:** إدارة القيمة المكتسبة وفق معيار ANSI/EIA-748
- **تحليل البيانات:** Power BI، Excel المتقدم، SQL
- **تحليل المخاطر:** محاكاة مونت كارلو، التحليل الكمي للمخاطر
- **إدارة المشاريع:** PMP، PRINCE2، مؤهلات APM

### المهارات الشخصية
- **التفكير التحليلي:** القدرة على تفسير مجموعات البيانات المعقدة
- **التواصل:** تقديم المعلومات التقنية لأصحاب المصلحة غير التقنيين
- **القيادة:** توجيه وتطوير فرق ضوابط المشاريع
- **حل المشكلات:** تحديد القضايا واقتراح الحلول بشكل استباقي
- **الاهتمام بالتفاصيل:** الدقة في التقارير والتحليل
- **إدارة أصحاب المصلحة:** بناء العلاقات عبر جميع مستويات المشروع

## الشهادات التي تعزز مسار ضوابط المشاريع

### الشهادات الأساسية
1. **PMP® (محترف إدارة المشاريع):** المعيار الذهبي من PMI — يظهر معرفة شاملة بإدارة المشاريع
2. **PRINCE2®:** شهادة إدارة مشاريع قائمة على العمليات معترف بها على نطاق واسع في أوروبا والشرق الأوسط
3. **ACP® (ممارس Agile المعتمد):** للمشاريع باستخدام منهجيات Agile

### الشهادات المتخصصة
4. **شهادة EVM:** محترف القيمة المكتسبة (EVP) من AACE International
5. **CCP (محترف التكاليف المعتمد):** من AACE International لهندسة التكاليف
6. **PSP (محترف التخطيط والجدولة):** من AACE International للجدولة
7. **RMP (محترف إدارة المخاطر):** من PMI لمتخصصي إدارة المخاطر
8. **شهادة Primavera P6:** أوراكل بريمافرا متخصص معتمد

## توقعات راتب مدير ضوابط المشاريع (2026)

### حسب المنطقة
- **السعودية:** 25,000 – 45,000 ريال/شهر (معفى من الضريبة)
- **الإمارات:** 25,000 – 50,000 درهم/شهر (معفى من الضريبة)
- **المملكة المتحدة:** £70,000 – £120,000/سنة
- **الولايات المتحدة:** $120,000 – $180,000/سنة
- **أستراليا:** AUD 150,000 – $220,000/سنة
- **مصر:** 50,000 – 120,000 جنيه/شهر

### حسب الصناعة
- **النفط والغاز:** الأعلى أجراً — علاوة 20-30%
- **الإنشاءات والبنية التحتية:** طلب قوي ورواتب تنافسية
- **الاتصالات:** طلب متزايد مع توسع 5G و FTTH
- **الرعاية الصحية:** طلب مستقر لمشاريع المستشفيات والمرافق الطبية
- **السكك الحديدية والنقل:** مشاريع كبرى تقود الطلب عالمياً

## مسار التطور المهني

### المستوى التمهيدي (0-5 سنوات)
- مهندس ضوابط المشاريع
- مهندس التخطيط
- مهندس التكاليف
- مجدول مبتدئ

### المستوى المتوسط (5-10 سنوات)
- مهندس ضوابط مشاريع أول
- مخطط رئيسي
- مهندس تكاليف أول
- محلل مخاطر

### المستوى الأقدم (10-15 سنة)
- **مدير ضوابط المشاريع**
- مستشار ضوابط مشاريع رئيسي
- مدير ضوابط البرامج

### المستوى التنفيذي (15+ سنة)
- مدير ضوابط المشاريع
- رئيس مكتب إدارة المشاريع
- نائب رئيس إدارة المشاريع
- رئيس المشاريع التنفيذي

## الأدوات التي يجب أن يتقنها مدير ضوابط المشاريع

### الجدولة
- **Primavera P6:** المعيار الصناعي للمشاريع واسعة النطاق
- **MS Project:** يستخدم على نطاق واسع للمشاريع متوسطة الحجم
- **Asta Powerproject:** شائع في أوروبا والإنشاءات

### التكاليف و EVM
- **Oracle Primavera Costing:** إدارة تكاليف متكاملة
- **SAP Project System:** تتبع تكاليف المشاريع المؤسسية
- **أدوات EVM مخصصة:** قائمة على Excel أو أنظمة مملوكة

### التقارير ولوحات المعلومات
- **Power BI:** أداة لوحات المعلومات والتصور الرائدة
- **Tableau:** تصور بيانات متقدم
- **Excel المتقدم:** جداول محورية، Power Query، VBA

### إدارة المخاطر
- **@RISK:** محاكاة مونت كارلو لـ Excel
- **Primavera Risk Analysis (PRA):** تحليل مخاطر الجدول
- **سجلات مخاطر مخصصة:** قائمة على Excel أو قواعد بيانات

## الصناعات التي تحتاج مديري ضوابط المشاريع

### الاتصالات
قطاع الاتصالات لديه طلب هائل على مديري ضوابط المشاريع، خاصة لتوسع 5G ونشر شبكات FTTH وبناء مراكز البيانات. يدير مديرو ضوابط المشاريع في الاتصالات برامج معقدة متعددة المواقع بآلاف الأنشطة المتزامنة.

### الإنشاءات والبنية التحتية
المشاريع الضخمة في الإنشاءات — المطارات، السكك الحديدية، الطرق السريعة، المدن الذكية — تتطلب مديري ضوابط مشاريع ذوي خبرة لإدارة ميزانيات تتجاوز غالباً مليارات الدولارات.

### النفط والغاز
القطاع الأعلى أجراً لمديري ضوابط المشاريع، مع مشاريع EPC (هندسة، شراء، إنشاء) معقدة تتطلب تحكماً صارماً في التكاليف والجدول.

### الرعاية الصحية
بناء المستشفيات وتجهيز المرافق الطبية وتنفيذ تكنولوجيا الرعاية الصحية تتطلب جميعها خبرة ضوابط المشاريع.

### السكك الحديدية والنقل
قطارات السرعة العالية وأنظمة المترو وبرامج تحديث السكك الحديدية الوطنية هي أرباب عمل رئيسيون لمديري ضوابط المشاريع.

## كيف تصبح مدير ضوابط المشاريع

### الخطوة 1: احصل على التعليم المناسب
- بكالوريوس في الهندسة أو إدارة الإنشاءات أو مجال ذي صلة
- ماجستير (MBA أو MSc إدارة المشاريع) للأدوار القيادية
- دورات متخصصة في التخطيط ومراقبة التكاليف و EVM

### الخطوة 2: اكتسب خبرة عملية
- ابدأ كمهندس تخطيط أو مهندس تكاليف
- اعمل على أنواع وأحجام متنوعة من المشاريع
- اكتسب خبرة مع Primavera P6 و MS Project
- تعلم تنفيذ EVM على مشاريع حقيقية

### الخطوة 3: احصل على الشهادات
- احصل على شهادة PMP® — أساسية للمصداقية
- أضف شهادات متخصصة (EVP، CCP، PSP)
- أكمل تدريب Primavera P6 الرسمي

### الخطوة 4: طور مهارات القيادة
- تولّ أدوار قيادة الفريق
- وجّه الموظفين المبتدئين
- قدم للجمهور التنفيذي
- ابنِ علاقات عبر الوظائف

### الخطوة 5: ابنِ سجل إنجازات
- وثّق تسليمات المشاريع الناجحة
- ابنِ محفظة من مخرجات ضوابط المشاريع
- تواصل مع محترفي الصناعة
- ساهم في الهيئات المهنية (PMI، AACE)

## التحديات الشائعة التي يواجهها مديرو ضوابط المشاريع

- **جودة البيانات:** ضمان بيانات دقيقة وفي الوقت المناسب من فرق المشروع
- **مقاومة العمليات:** التغلب على عدم رغبة الفريق في اتباع إجراءات الضوابط
- **قيود الأدوات:** العمل مع أنظمة غير كافية أو قديمة
- **زحف النطاق:** إدارة تغييرات النطاق غير المنضبطة
- **تنسيق المشاريع المتعددة:** موازنة الأولويات عبر المشاريع المتزامنة
- **التواصل التنفيذي:** ترجمة البيانات التقنية لصناع القرار

## أفضل الممارسات لضوابط المشاريع الفعالة

1. **أنشئ خطوط أساسية مبكراً:** اضبط خطوط أساس الجدول والتكلفة قبل بدء التنفيذ
2. **نفذ ضبط تغيير قوي:** لا تغييرات بدون تقييم أثر رسمي
3. **استخدم EVM باستمرار:** تقارير EVM المنتظمة توفر إنذاراً مبكراً للمشاكل
4. **حافظ على سلامة البيانات:** تأكد جميع البيانات حالية ودقيقة وقابلة للتدقيق
5. **تواصل بشكل استباقي:** لا تنتظر المشاكل — أبلغ عن الاتجاهات والتنبؤات
6. **استثمر في الأدوات:** استخدم أدوات جدولة وتقارير بمستوى احترافي
7. **درّب فريقك:** تحسين مستمر في مهارات ضوابط المشاريع
8. **تعلم من الدروس:** أجرِ مراجعات بعد المشروع وطبق التعلمات

## الخلاصة

دور **مدير ضوابط المشاريع** هو أحد أكثر المناصب حرجية في المنظمات القائمة على المشاريع. يجمع بين الخبرة التقنية في التخطيط ومراقبة التكاليف وإدارة المخاطر ومهارات القيادة والتواصل. مع تعقيد المشاريع المتزايد ونمو الميزانيات، يستمر الطلب على مديري ضوابط المشاريع المهرة في الارتفاع عبر جميع الصناعات الرئيسية.

للمحترفين الذين يتطلعون لتطوير مسار ضوابط المشاريع، المسار واضح: ابنِ المهارات التقنية، اكتسب خبرة مشروعات متنوعة، احصل على شهادات مهنية، وطور صفات القيادة اللازمة لتوجيه وظائف ضوابط المشاريع في أعلى مستوى."""
    }
}

if __name__ == '__main__':
    articles = load_articles()
    nid = max(a['id'] for a in articles) + 1

    slug = ARTICLE['slug']
    hero_path = f'assets/images/articles/{slug}-hero.jpeg'
    os.makedirs('assets/images/articles', exist_ok=True)

    pexels_url = 'https://images.pexels.com/photos/7652126/pexels-photo-7652126.jpeg?auto=compress&cs=tinysrgb&w=1200'
    if download_image(pexels_url, hero_path):
        hero = f'/assets/images/articles/{slug}-hero.jpeg'
    else:
        hero = '/assets/images/articles/default-hero.webp'

    base = datetime(2026, 7, 18)
    article = {
        'id': nid,
        'slug': slug,
        'category': ARTICLE['category'],
        'author': 'Ashraf Ibrahim El Desoky',
        'heroImage': hero,
        'publishDate': base.strftime('%Y-%m-%d'),
        'updatedDate': base.strftime('%Y-%m-%d'),
        'readingTime': 12,
        'featured': True,
        'draft': False,
        'tags': ARTICLE['tags'],
        'en': {
            'title': ARTICLE['en']['title'],
            'excerpt': ARTICLE['en']['excerpt'],
            'content': ARTICLE['en']['content'],
            'metaTitle': ARTICLE['en']['title'] + ' – Ashraf El Desoky, PMP®',
            'metaDescription': ARTICLE['en']['excerpt'],
            'keywords': ARTICLE['en']['keywords']
        },
        'ar': {
            'title': ARTICLE['ar']['title'],
            'excerpt': ARTICLE['ar']['excerpt'],
            'content': ARTICLE['ar']['content'],
            'metaTitle': ARTICLE['ar']['title'] + ' – أشرف الدسوقي, PMP®',
            'metaDescription': ARTICLE['ar']['excerpt'],
            'keywords': ARTICLE['ar']['keywords']
        }
    }

    articles.append(article)
    save_articles(articles)
    print(f"Added: {slug} (id={nid})")
    print(f"Total: {len(articles)}")
