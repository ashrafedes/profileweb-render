/* ============================================================
   ECMS – Internationalization (i18n) System
   Bilingual English/Arabic support for all pages
   ============================================================ */

'use strict';

const I18N = (() => {

  const LANG_KEY = 'ecms-lang';
  const AR = 'ar';
  const EN = 'en';

  /* ── Translation Dictionary ── */
  /* Keys are English strings (trimmed), values are Arabic */
  const DICT = {

    /* ── Nav: Brand ── */
    'Ashraf El Desoky': 'أشرف الدسوقي',
    'Executive Career Management System': 'نظام إدارة المسيرة المهنية',

    /* ── Nav: Links ── */
    'Dashboard': 'الرئيسية',
    'About': 'نبذة',
    'Experience': 'الخبرة',
    'Projects': 'المشاريع',
    'Skills': 'المهارات',
    'More ▾': 'المزيد ▾',
    'Companies': 'الشركات',
    'Achievements': 'الإنجازات',
    'PMO Leadership': 'قيادة PMO',
    'Telecommunications': 'الاتصالات',
    'Project Controls': 'التحكم بالمشاريع',
    'Digital Transformation': 'التحول الرقمي',
    'Leadership': 'القيادة',
    'Software': 'البرمجيات',
    'Certifications': 'الشهادات',
    'Education': 'التعليم',
    'Awards': 'التكريمات',
    'Downloads': 'التحميلات',
    'Contact': 'تواصل',
    'All Skills': 'كل المهارات',

    /* ── Nav: Actions ── */
    '🔍 Search': '🔍 بحث',
    'Search (Ctrl+K)': 'بحث (Ctrl+K)',
    'Toggle dark/light mode': 'تبديل الوضع الليلي/النهاري',
    'Open navigation menu': 'فتح القائمة',
    'Back to top': 'العودة للأعلى',
    'Skip to main content': 'تخطي إلى المحتوى',

    /* ── Search Modal ── */
    'Search experience, projects, skills, certifications…': 'ابحث في الخبرة، المشاريع، المهارات، الشهادات…',
    'ESC': 'ESC',
    'Global Search': 'البحث الشامل',
    'Search across all career data, skills, projects, companies and certifications': 'ابحث في جميع بيانات المسيرة، المهارات، المشاريع، الشركات والشهادات',
    'No results found': 'لا توجد نتائج',
    'Search…': 'بحث…',

    /* ── Footer ── */
    'Navigation': 'التنقل',
    'Expertise': 'الخبرات',
    'Resources': 'الموارد',
    'All Rights Reserved': 'جميع الحقوق محفوظة',
    'Projects Director | PMO & Project Controls Executive | Telecommunications & Digital Infrastructure Leader. This Executive Career Management System is the permanent digital knowledge base for my professional career.': 'مدير المشاريع | رئيس PMO والتحكم بالمشاريع | قائد الاتصالات والبنية التحتية الرقمية. هذا النظام هو قاعدة المعرفة الرقمية الدائمة لمسيرتي المهنية.',

    /* ── Common: Section aria-labels ── */
    'Professional experience': 'الخبرة المهنية',
    'Professional training': 'التدريب المهني',
    'Filter controls': 'عناصر التصفية',
    'Filter career by country': 'تصفية المسيرة المهنية بالدولة',
    'Skills overview': 'نظرة عامة على المهارات',
    'Contact information': 'معلومات التواصل',
    'CV Downloads': 'تحميلات السيرة الذاتية',

    /* ── Common: Breadcrumb ── */
    'Career History': 'المسيرة المهنية',
    'Project Portfolio': 'معرض المشاريع',
    'Skills & Competencies': 'المهارات والكفاءات',

    /* ── Common: Filter Tabs ── */
    'All': 'الكل',
    'All Projects': 'كل المشاريع',
    '📡 Telecom': '📡 اتصالات',
    '🏗 Infrastructure': '🏗 بنية تحتية',
    '🏙 Smart City': '🏙 مدينة ذكية',
    '🚂 Railway': '🚂 سكك حديدية',
    '🇸🇦 Saudi Arabia': '🇸🇦 السعودية',
    '🇪🇬 Egypt': '🇪🇬 مصر',
    '🇸🇩 Sudan': '🇸🇩 السودان',

    /* ── Common: Tags & Labels ── */
    'Current': 'حالياً',
    'Present': 'حالياً',
    'Flagship · 10 Years': 'رائد · 10 سنوات',
    '🇸🇦 Saudi Arabia': '🇸🇦 السعودية',
    '🇪🇬 Egypt': '🇪🇬 مصر',
    '🇸🇩 Sudan': '🇸🇩 السودان',
    'PDF': 'PDF',
    'Ready': 'جاهز',
    'Active': 'نشط',
    '2 Pages': 'صفحتان',
    'Full Version': 'النسخة الكاملة',
    'LinkedIn': 'لينكدإن',

    /* ── Common: Duration labels ── */
    '1+ Year': '+1 سنة',
    '1 Year': 'سنة واحدة',
    '2 Years': 'سنتان',
    '3 Years': '3 سنوات',
    '4+ Years': '+4 سنوات',
    '9 Months': '9 أشهر',
    '15 Months': '15 شهراً',
    '2.5 Years': '2.5 سنة',
    '10 Years': '10 سنوات',

    /* ── Common: Buttons ── */
    '⬇ Download CV': '⬇ تحميل السيرة',
    '⬇ Download PDF': '⬇ تحميل PDF',
    '✉ Contact': '✉ تواصل',
    'View Profile →': 'عرض الملف ←',
    'View LinkedIn profile': 'عرض ملف لينكدإن',

    /* ── About Page ── */
    'Executive Profile': 'الملف التنفيذي',
    'Biography, profile summary and personal information': 'السيرة الذاتية، ملخص الملف والمعلومات الشخصية',
    'PMP® Certified': 'معتمد PMP®',
    'Projects Director | PMO Executive': 'مدير المشاريع | رئيس PMO',
    '📍 Riyadh, Saudi Arabia': '📍 الرياض، السعودية',
    'Email': 'البريد الإلكتروني',
    'Phone (KSA)': 'الهاتف (السعودية)',
    'Phone (Egypt)': 'الهاتف (مصر)',
    'Nationality': 'الجنسية',
    '🇪🇬 Egyptian': '🇪🇬 مصري',
    'Date of Birth': 'تاريخ الميلاد',
    'Languages': 'اللغات',
    'Arabic · English · German': 'العربية · الإنجليزية · الألمانية',
    'Executive Biography': 'السيرة التنفيذية',
    'Professional': 'الملف',
    'Summary': 'الملخص',
    'Career Highlights': 'أبرز المحطات المهنية',
    '25+ years of international programme and project leadership': '+25 عاماً من القيادة الدولية للبرامج والمشاريع',
    'PMP® certified executive with PMO and project controls expertise': 'تنفيذي معتمد PMP® بخبرة في PMO والتحكم بالمشاريع',
    '10+ years supporting Saudi Telecom Company (STC) programmes': '+10 سنوات دعم برامج شركة الاتصالات السعودية (STC)',
    'Leadership across Saudi Arabia, Egypt and Sudan': 'قيادة عبر السعودية ومصر والسودان',
    'Expert in FTTH, FTTx, OSP, ISP, 5G and Low Current Systems': 'خبير في FTTH و FTTx و OSP و ISP و 5G وأنظمة التيار الخفيف',
    'ERP development, KPI dashboards and digital transformation': 'تطوير ERP ولوحات KPI والتحول الرقمي',
    'Commercial, cost, schedule, quality and risk management': 'إدارة التجارية والتكلفة والجدول والجودة والمخاطر',
    'B.Sc. Communication & Electronics Engineering – Helwan University': 'بكالوريوس هندسة الاتصالات والإلكترونيات – جامعة حلوان',
    'Postgraduate Diploma in BA – Edinburgh Business School': 'دبلوم دراسات عليا في إدارة الأعمال – كلية إدنبرة للأعمال',
    'Expertise Areas': 'مجالات الخبرة',
    'Core Executive': 'الكفاءات',
    'Competencies': 'التنفيذية',
    'Programme Management': 'إدارة البرامج',
    'Portfolio Management': 'إدارة المحفظة',
    'Executive Reporting': 'التقارير التنفيذية',
    'Stakeholder Management': 'إدارة أصحاب المصلحة',
    'Planning & Scheduling': 'التخطيط والجدولة',
    'Cost Control': 'ضبط التكلفة',
    'Risk Management': 'إدارة المخاطر',
    'Governance & Change Control': 'الحوكمة وضبط التغييرات',
    'Earned Value Management': 'إدارة القيمة المكتسبة',
    'FTTH / FTTx': 'FTTH / FTTx',
    'OSP / ISP': 'OSP / ISP',
    '5G Rollout': 'نشر 5G',
    'Fiber Optic Infrastructure': 'بنية الألياف الضوئية',
    'ELV / BMS / CCTV': 'ELV / BMS / كاميرات',
    'Personal Details': 'التفاصيل الشخصية',
    'Personal': 'التفاصيل',
    'Information': 'الشخصية',
    'Identity & Location': 'الهوية والموقع',
    'Full Name': 'الاسم الكامل',
    'Ashraf Ibrahim El Desoky': 'أشرف إبراهيم الدسوقي',
    'Egyptian': 'مصري',
    'Current Location': 'الموقع الحالي',
    'Riyadh, Saudi Arabia': 'الرياض، السعودية',
    'Home Address': 'العنوان البريدي',
    'El Haram, Giza, Egypt': 'الهرم، الجيزة، مصر',
    'Marital Status': 'الحالة الاجتماعية',
    'Married': 'متزوج',
    'Military Service': 'الخدمة العسكرية',
    'Completed': 'مكتملة',
    'Driving License': 'رخصة القيادة',
    'Yes (Egyptian & Saudi)': 'نعم (مصرية وسعودية)',
    'Arabic': 'العربية',
    'Native': 'اللغة الأم',
    'English': 'الإنجليزية',
    'Very Good / Fluent': 'جيد جداً / طليق',
    'German': 'الألمانية',
    'Basic': 'أساسي',
    'Countries Worked': 'الدول التي عمل بها',

    /* ── About: Biography paragraphs ── */
    'Ashraf Ibrahim El Desoky is a PMP®-certified Projects Director and PMO Executive with more than 25 years of international leadership experience delivering telecommunications, digital infrastructure and capital investment programmes across Saudi Arabia, Egypt and Sudan.': 'أشرف إبراهيم الدسوقي مدير مشاريع معتمد PMP® ورئيس PMO بخبرة قيادية دولية تتجاوز 25 عاماً في تسليم مشاريع الاتصالات والبنية التحتية الرقمية والاستثمارات الرأسمالية عبر السعودية ومصر والسودان.',

    /* ── Career Page ── */
    'Complete professional timeline – 25+ years across 3 countries and 9 organisations': 'المسيرة المهنية الكاملة – +25 عاماً عبر 3 دول و9 مؤسسات',
    'Project Control Manager': 'مدير التحكم بالمشاريع',
    'AlSharq Office Company': 'شركة الشرق',
    'Egyptian Company for General Contracting': 'الشركة المصرية للمقاولات العامة',
    'Projects Director – Telecommunications': 'مدير مشاريع – الاتصالات',
    'Lead Consultant Project Manager': 'مدير مشروع استشاري رئيسي',
    'Sabbour Consulting': 'صبور للاستشارات',
    'Senior Site Manager': 'مدير موقع أول',
    'Benya Systems': 'بينيا سيستمز',
    'Site Manager': 'مدير موقع',
    'Fiber Misr – Alstom': 'فاير مصر – ألستوم',
    'Senior Project Control Engineer / Planning Engineer': 'مهندس تحكم أول بالمشاريع / مهندس تخطيط',
    'Norconsult – Supporting STC (Saudi Telecom Company)': 'نوركونسلت – دعم STC (شركة الاتصالات السعودية)',
    'Project Manager': 'مدير مشروع',
    'Millentech Systems': 'ميلينتيك سيستمز',
    'Project Engineer': 'مهندس مشروع',
    'MITT Company (Siemens Subcontract – Sudan)': 'شركة MITT (مقاول سيمنز – السودان)',
    'Assistant General Manager': 'مساعد المدير العام',
    'Compumagic International': 'كومبوماجيك الدولية',
    'Project Control and Monitoring Engineer – External Network': 'مهندس تحكم ومراقبة بالمشاريع – الشبكة الخارجية',
    'Siemens AG (Egypt)': 'سيمنز (مصر)',
    'Shift Engineer': 'مهندس ورديات',
    'El Gezirah Sheraton Hotel': 'فندق الجزيرة شيراتون',
    'Officer – Air Defence Forces': 'ضابط – قوات الدفاع الجوي',
    'Egyptian Armed Forces': 'القوات المسلحة المصرية',

    /* ── Career: Descriptions ── */
    'Leading project planning, controls, budgeting, forecasting and reporting for telecommunications and electrical infrastructure projects.': 'قيادة تخطيط المشاريع والتحكم والميزانية والتوقعات والتقارير لمشاريع الاتصالات والبنية التحتية الكهربائية.',
    'Lead planning, budgeting, forecasting and execution of telecommunications and electrical projects': 'قيادة التخطيط والميزانية والتوقعات وتنفيذ مشاريع الاتصالات والكهرباء',
    'Manage subcontractors, engineering teams, risks, schedules and client communications': 'إدارة المقاولين والفرق الهندسية والمخاطر والجداول والتواصل مع العملاء',
    'Drive governance, KPI reporting and operational improvements': 'قيادة الحوكمة وتقارير KPI والتحسينات التشغيلية',
    'Directed end-to-end telecommunications infrastructure delivery with full lifecycle, cost, quality, risk and stakeholder management.': 'إدارة تسليم البنية التحتية للاتصالات من البداية للنهاية مع إدارة كاملة لدورة الحياة والتكلفة والجودة والمخاطر وأصحاب المصلحة.',
    'Directed end-to-end telecom infrastructure project delivery': 'إدارة تسليم مشاريع البنية التحتية للاتصالات من البداية للنهاية',
    'Managed lifecycle, cost, quality, risk and stakeholder engagement': 'إدارة دورة الحياة والتكلفة والجودة والمخاطر وأصحاب المصلحة',
    'Led multidisciplinary engineering teams across all project phases': 'قيادة فرق هندسية متعددة التخصصات عبر جميع مراحل المشروع',
    'Led delivery of smart infrastructure systems for the Egyptian International Olympic Games City and New Administrative Capital Fiber Network.': 'قيادة تسليم أنظمة البنية التحتية الذكية لمدينة الألعاب الأولمبية الدولية المصرية وشبكة الألياف في العاصمة الإدارية الجديدة.',
    'Led Egyptian International Olympic Games City ELV, BMS, CCTV, Fire Alarm and FTTH delivery': 'قيادة تسليم ELV و BMS و CCTV و إنذار الحريق و FTTH لمدينة الألعاب الأولمبية',
    'Managed New Administrative Capital Fiber Network – design and implementation': 'إدارة شبكة الألياف في العاصمة الإدارية الجديدة – التصميم والتنفيذ',
    'Stakeholder management with ACUD (Administrative Capital for Urban Development)': 'إدارة أصحاب المصلحة مع ACUD (شركة العاصمة الإدارية للتنمية الحضرية)',
    'Managed budgets, schedules, procurement and quality assurance': 'إدارة الميزانيات والجداول والمشتريات وضمان الجودة',
    'Coordinated multidisciplinary engineering and contracting teams': 'تنسيق الفرق الهندسية والمقاولة متعددة التخصصات',
    'Led Egypt National Railways Modernization Project site operations for fiber optic infrastructure deployment.': 'قيادة عمليات موقع مشروع تحديث السكك الحديدية القومية المصرية لنشر البنية التحتية للألياف الضوئية.',
    'Led Egypt National Railways Modernization Project site operations': 'قيادة عمليات موقع مشروع تحديث السكك الحديدية القومية',
    'Managed fiber optic cable installation and infrastructure deployment': 'إدارة تركيب كابلات الألياف الضوئية ونشر البنية التحتية',
    'Supervised site teams, quality control and material management': 'الإشراف على فرق الموقع وضبط الجودة وإدارة المواد',
    'Coordinated with client and engineering teams': 'التنسيق مع العميل والفرق الهندسية',
    'Managed fiber optic network deployment for railway modernization, coordinating between Fiber Misr and Alstom project teams.': 'إدارة نشر شبكة الألياف الضوئية لتحديث السكك الحديدية، مع التنسيق بين فاير مصر وألستوم.',
    '10-year flagship engagement managing planning, scheduling, progress monitoring and project controls for STC\'s national FTTH/FTTx fixed network expansion programmes across the Kingdom of Saudi Arabia.': 'ارتباط رائد لمدة 10 سنوات في إدارة التخطيط والجدولة ومراقبة التقدم والتحكم بالمشاريع لبرامج توسيع شبكة FTTH/FTTx الثابتة الوطنية لـ STC عبر المملكة العربية السعودية.',
    'Managed planning, scheduling and project controls for STC fixed network programmes': 'إدارة التخطيط والجدولة والتحكم بالمشاريع لبرامج الشبكة الثابتة لـ STC',
    'Prepared and maintained master programme schedules using MS Project and Primavera': 'إعداد وصيانة جداول البرامج الرئيسية باستخدام MS Project و Primavera',
    'Developed and maintained KPI dashboards and executive performance reports': 'تطوير وصيانة لوحات KPI وتقارير الأداء التنفيذية',
    'Developed ERP system for project tracking using MS Access VBA (SQL database)': 'تطوير نظام ERP لتتبع المشاريع باستخدام MS Access VBA (قاعدة بيانات SQL)',
    'Created and maintained Work Breakdown Structures (WBS) for complex telecom projects': 'إنشاء وصيانة هياكل تجزئة العمل (WBS) لمشاريع الاتصالات المعقدة',
    'Monitored FTTH, FTTx, OSP and ISP rollout programmes across KSA regions': 'مراقبة برامج نشر FTTH و FTTx و OSP و ISP عبر مناطق المملكة',
    'Produced weekly, monthly and executive progress reports for STC senior management': 'إنتاج تقارير تقدم أسبوعية وشهرية وتنفيذية لإدارة STC العليا',
    'Managed change control, risk registers and issue logs': 'إدارة ضبط التغييرات وسجلات المخاطر وسجلات القضايا',
    'Supported commercial management and contract administration': 'دعم الإدارة التجارية وإدارة العقود',
    'Managed ICT and telecommunications projects end-to-end including planning, scheduling, team management and stakeholder reporting.': 'إدارة مشاريع ICT والاتصالات من البداية للنهاية بما في ذلك التخطيط والجدولة وإدارة الفريق وتقارير أصحاب المصلحة.',
    'External network telecom projects in Sudan as Siemens subcontractor (MITT undertook a turnkey project with Siemens Germany-Sudan branch). International experience in challenging environments.': 'مشاريع الشبكة الخارجية للاتصالات في السودان كمقاول سيمنز (MITT تولت مشروعاً متكاملاً مع فرع سيمنز ألمانيا-السودان). خبرة دولية في بيئات صعبة.',
    'Worked as Project Site Engineer on external network projects in Sudan': 'العمل كمهندس موقع على مشاريع الشبكة الخارجية في السودان',
    'Monitored construction progress and materials on site': 'مراقبة تقدم البناء والمواد في الموقع',
    'Used MS Project for schedule control and created WBS': 'استخدام MS Project لضبط الجدولة وإنشاء WBS',
    'Prepared site progress reports and controlled warehouse': 'إعداد تقارير تقدم الموقع ومراقبة المستودع',
    'One of the largest PC sales companies in Egypt – partner with Ministry of ICT in the "Computer for Every Home" project.': 'إحدى أكبر شركات بيع الحواسيب في مصر – شريك وزارة الاتصالات في مشروع "كمبيوتر لكل بيت".',
    'Followed up RMA and Intel payment repayment programs': 'متابعة RMA وبرامج سداد Intel',
    'Supervised PBX and LAN installation in new company building': 'الإشراف على تركيب PBX و LAN في مبنى الشركة الجديد',
    'Website design responsibilities': 'مسؤوليات تصميم الموقع',
    'Designed MS Access application for accounting and time attendance': 'تصميم تطبيق MS Access للمحاسبة والحضور والانصراف',
    'External network implementation projects at the world-renowned Siemens – a foundational role developing core project controls and ERP skills.': 'مشاريع تنفيذ الشبكة الخارجية في سيمنز العالمية – دور أساسي في تطوير مهارات التحكم بالمشاريع و ERP.',
    'Controlled Siemens warehouse and material management': 'مراقبة مستودع سيمنز وإدارة المواد',
    'Created MS Access application for project progress monitoring and warehouse control': 'إنشاء تطبيق MS Access لمراقبة تقدم المشروع ومراقبة المستودع',
    'Prepared BOQ (Bill of Quantities) from planning division for client signature': 'إعداد BOQ (جدول الكميات) من قسم التخطيط لتوقيع العميل',
    'Provided implementation division with project monitoring reports vs plan': 'تقديم تقارير مراقبة المشروع مقابل الخطة لقسم التنفيذ',
    'Hotel engineering – supervised mechanical, electrical, HVAC and plumbing systems. Conducted preventive maintenance and trained junior staff.': 'هندسة الفندق – الإشراف على الأنظمة الميكانيكية والكهربائية و HVAC والسباكة. تنفيذ الصيانة الوقائية وتدريب الموظفين الجدد.',
    'Military service as Officer in Egyptian Air Defence Forces. Military engineering and operations duties (mandatory service, now completed).': 'الخدمة العسكرية كضابط في قوات الدفاع الجوي المصري. مهام الهندسة العسكرية والعمليات (خدمة إلزامية، مكتملة الآن).',

    /* ── Career: Tags ── */
    'Project Controls': 'التحكم بالمشاريع',
    'PMO': 'PMO',
    'Telecom': 'اتصالات',
    'Riyadh, KSA': 'الرياض، السعودية',
    'FTTH': 'FTTH',
    'Project Director': 'مدير مشاريع',
    'Egypt': 'مصر',
    'Olympic City': 'المدينة الأولمبية',
    'ELV': 'ELV',
    'BMS': 'BMS',
    'CCTV': 'كاميرات',
    'New Administrative Capital': 'العاصمة الإدارية الجديدة',
    'Railways': 'السكك الحديدية',
    'Fiber Optic': 'الألياف الضوئية',
    'OSP': 'OSP',
    'Railway': 'السكك الحديدية',
    'STC': 'STC',
    'FTTH/FTTx': 'FTTH/FTTx',
    'OSP/ISP': 'OSP/ISP',
    'ERP': 'ERP',
    'Primavera': 'Primavera',
    'MS Project': 'MS Project',
    'Saudi Arabia': 'السعودية',
    'ICT': 'ICT',
    'External Network': 'الشبكة الخارجية',
    'Sudan': 'السودان',
    'International': 'دولي',
    'IT': 'IT',
    'MS Access VBA': 'MS Access VBA',
    'Siemens': 'سيمنز',
    'HVAC': 'HVAC',
    'Electrical': 'كهرباء',
    'Hospitality': 'ضيافة',
    'Military': 'عسكري',

    /* ── Contact Page ── */
    'Contact Ashraf El Desoky, PMP®': 'تواصل مع المهندس أشرف الدسوقي، PMP®',
    'Get in touch for executive opportunities, collaborations or professional enquiries': 'تواصل معي للفرص التنفيذية أو التعاون أو الاستفسارات المهنية',
    'Get in Touch': 'تواصل معنا',
    'Contact': 'تواصل',
    'Information': 'المعلومات',
    'Available for senior executive opportunities in PMO leadership, project controls, telecommunications and digital infrastructure management. Open to roles across Saudi Arabia, Egypt, GCC and international markets.': 'متاح لفرص تنفيذية عليا في قيادة PMO والتحكم بالمشاريع والاتصالات وإدارة البنية التحتية الرقمية. منفتح على أدوار عبر السعودية ومصر ودول الخليج والأسواق الدولية.',
    'Email (Primary)': 'البريد (الرئيسي)',
    'Phone – Saudi Arabia': 'الهاتف – السعودية',
    'Phone – Egypt': 'الهاتف – مصر',
    '● Available': '● متاح',
    'Open to opportunities': 'منفتح على الفرص',
    'Projects Director | PMO & Project Controls Executive | Telecommunications & Digital Infrastructure Leader with 25+ years of international experience.': 'مدير المشاريع | رئيس PMO والتحكم بالمشاريع | قائد الاتصالات والبنية التحتية الرقمية بخبرة دولية تتجاوز 25 عاماً.',
    'PMP® Certified': 'معتمد PMP®',
    'Digital Infrastructure': 'البنية التحتية الرقمية',
    'Open To': 'منفتح على',
    'Projects Director / Programme Director roles': 'أدوار مدير مشاريع / مدير برامج',
    'PMO Director / Head of PMO positions': 'مناصب مدير PMO / رئيس PMO',
    'Senior Project Controls Manager': 'مدير أول للتحكم بالمشاريع',
    'Telecom Programme Manager': 'مدير برامج الاتصالات',
    'Digital Infrastructure Lead': 'قائد البنية التحتية الرقمية',
    'Senior Consulting / Advisory roles': 'أدوار استشارات / استشارية أولى',
    'Preferred Locations': 'المواقع المفضلة',

    /* ── Downloads Page ── */
    'Download Centre': 'مركز التحميل',
    'CV documents, certificates, portfolios and professional credentials': 'وثائق السيرة الذاتية والشهادات والمعرض والاعتمادات المهنية',
    'Curriculum Vitae': 'السيرة الذاتية',
    'CV': 'السيرة',
    'Documents': 'الوثائق',
    'Executive CV – 2 Pages': 'السيرة التنفيذية – صفحتان',
    'Concise 2-page executive CV optimised for senior leadership and director-level applications. PMP® headline, core competencies and career highlights.': 'سيرة تنفيذية مختصرة في صفحتين مُحسّنة للتطبيقات القيادية العليا ومستوى المدير. عنوان PMP® والكفاءات الأساسية وأبرز المحطات المهنية.',
    'Master CV – Full Version': 'السيرة الشاملة – النسخة الكاملة',
    'Comprehensive full career documentation with complete job descriptions, achievements, projects, skills and credentials for executive and board-level applications.': 'توثيق شامل للمسيرة المهنية مع أوصاف وظيفية كاملة وإنجازات ومشاريع ومهارات واعتمادات للتطبيقات التنفيذية ومستوى مجلس الإدارة.',
    'View and connect with Ashraf El Desoky on LinkedIn for professional networking and up-to-date career information.': 'عرض والتواصل مع أشرف الدسوقي على لينكدإن للتواصل المهني ومعلومات المسيرة المحدثة.',

    /* ── Projects Page ── */
    'Major projects and programmes delivered across 25+ years': 'مشاريع وبرامج كبرى تم تسليمها عبر +25 عاماً',

    /* ── Skills Page ── */
    'Technical, management and leadership skills developed over 25+ years': 'مهارات تقنية وإدارية وقيادية طُورت عبر +25 عاماً',
    'Category 1': 'الفئة 1',
    'Leadership &': 'القيادة و',
    'Management': 'الإدارة',

    /* ── Common: Section headers ── */
    'Section Eyebrow': 'القسم',

    /* ── 404 Page ── */
    'Page Not Found': 'الصفحة غير موجودة',
    'The page you are looking for does not exist or has been moved.': 'الصفحة التي تبحث عنها غير موجودة أو تم نقلها.',
    'Go to Dashboard': 'الذهاب للرئيسية',

    /* ── Misc proper nouns that stay same ── */
    'ECGC': 'ECGC',
    'ACUD': 'ACUD',

    /* ── Achievements Page ── */
    'Career Achievements': 'الإنجازات المهنية',
    'Key accomplishments and milestones verified from career documentation': 'الإنجازات الرئيسية والمحطات الموثقة من السجل المهني',
    'Career Milestones': 'المحطات المهنية',

    /* ── Awards Page ── */
    'Awards & Recognition': 'التكريمات والتقدير',
    'Appreciation certificates and professional recognition received throughout career': 'شهادات التقدير والاعتراف المهني الم تلقاها طوال المسيرة',
    'Awards &': 'التكريمات و',
    'Appreciation': 'التقدير',

    /* ── Certifications Page ── */
    'Certifications & Credentials': 'الشهادات والاعتمادات',
    'Verified professional certifications and academic qualifications': 'الشهادات المهنية المعتمدة والمؤهلات الأكاديمية',
    'Project Management Professional': 'محترف إدارة المشاريع',
    'Postgraduate Diploma in Business Administration': 'دبلوم دراسات عليا في إدارة الأعمال',
    'Cisco Certified Network Associate (CCNA)': 'سيسكو معتمد شبكات (CCNA)',
    'B.Sc. Communication and Electronics Engineering': 'بكالوريوس هندسة الاتصالات والإلكترونيات',
    'Certificate Documents': 'وثائق الشهادات',

    /* ── Companies Page ── */
    'Companies & Organisations': 'الشركات والمؤسسات',
    '9 organisations across Saudi Arabia, Egypt and Sudan over 25+ years': '9 مؤسسات عبر السعودية ومصر والسودان خلال +25 عاماً',
    'Norconsult (Supporting Saudi Telecom Company – STC)': 'نوركونسلت (دعم شركة الاتصالات السعودية – STC)',
    'MITT Company (Sudan – Siemens Subcontract)': 'شركة MITT (السودان – مقاول سيمنز)',

    /* ── Digital Transformation Page ── */
    'Digital Transformation': 'التحول الرقمي',
    'ERP development, data intelligence, business process optimisation and digital systems expertise': 'تطوير ERP وذكاء البيانات وتحسين العمليات التجارية وخبرة الأنظمة الرقمية',
    'Digital Expertise': 'الخبرة الرقمية',

    /* ── Education Page ── */
    'Education & Training': 'التعليم والتدريب',
    'Academic qualifications, professional training and continuous learning': 'المؤهلات الأكاديمية والتدريب المهني والتعلم المستمر',
    'Educational Background': 'الخلفية التعليمية',
    'Preparatory M.Sc. – Communication Engineering': 'ماجستير تمهيدي – هندسة الاتصالات',
    'Bachelor of Science – Communication and Electronics Engineering': 'بكالوريوس العلوم – هندسة الاتصالات والإلكترونيات',
    'Egyptian General Secondary Certificate (Thanawiya Amma)': 'شهادة الثانوية العامة المصرية',
    'Training &': 'التدريب و',
    'Courses': 'الدورات',
    'Professional Development': 'التطوير المهني',

    /* ── Leadership Page ── */
    'Leadership Profile': 'الملف القيادي',
    'Executive leadership, team management and strategic delivery': 'القيادة التنفيذية وإدارة الفرق والتسليم الاستراتيجي',
    'Leadership Philosophy': 'فلسفة القيادة',
    'Leadership Highlights': 'أبرز جوانب القيادة',

    /* ── PMO Page ── */
    'PMO Leadership': 'قيادة PMO',
    'Programme governance, project controls and PMO expertise': 'حوكمة البرامج والتحكم بالمشاريع وخبرة PMO',
    'PMO &': 'PMO و',
    'Governance Expertise': 'خبرة الحوكمة',
    'Programme Functions Delivered': 'الوظائف المُسلّمة للبرنامج',

    /* ── Project Controls Page ── */
    'Project Controls': 'التحكم بالمشاريع',
    'Planning, scheduling, cost control, risk management and programme governance': 'التخطيط والجدولة وضبط التكلفة وإدارة المخاطر وحوكمة البرامج',
    'Project Controls Depth': 'عمق التحكم بالمشاريع',

    /* ── Projects Page ── */
    'Projects': 'المشاريع',
    'Major projects and programmes delivered across 25+ years': 'مشاريع وبرامج كبرى تم تسليمها عبر +25 عاماً',
    'Egyptian International Olympic Games City': 'المدينة الأولمبية الدولية المصرية',
    'STC National FTTH/FTTx Fixed Network Rollout': 'نشر شبكة FTTH/FTTx الثابتة الوطنية لـ STC',
    'Egypt National Railways Modernization Project': 'مشروع تحديث السكك الحديدية القومية المصرية',
    'New Administrative Capital Fiber Network': 'شبكة الألياف في العاصمة الإدارية الجديدة',
    'Siemens External Telecom Network Projects': 'مشاريع الشبكة الخارجية للاتصالات لسيمنز',
    'MITT Telecom Infrastructure – Sudan': 'بنية الاتصالات التحتية – MITT السودان',

    /* ── Search Page ── */
    'Global Search': 'البحث الشامل',
    'Search across all career data, skills, projects, companies and certifications': 'ابحث في جميع بيانات المسيرة والمهارات والمشاريع والشركات والشهادات',

    /* ── Skills Page ── */
    'Skills & Competencies': 'المهارات والكفاءات',
    'Technical, management and leadership skills developed over 25+ years': 'مهارات تقنية وإدارية وقيادية طُورت عبر +25 عاماً',
    'Category 1': 'الفئة 1',
    'Leadership &': 'القيادة و',
    'Management': 'الإدارة',
    'Commercial Management': 'الإدارة التجارية',
    'Telecommunications Expertise': 'خبرة الاتصالات',
    'Software Tools': 'أدوات البرمجيات',

    /* ── Software Page ── */
    'Software & Programming': 'البرمجيات والبرمجة',
    'Technical software tools, programming languages and development skills': 'أدوات البرمجيات التقنية ولغات البرمجة ومهارات التطوير',

    /* ── Telecommunications Page ── */
    'Telecommunications': 'الاتصالات',
    'FTTH, FTTx, OSP, ISP, 5G, fiber optic and digital infrastructure expertise': 'خبرة FTTH و FTTx و OSP و ISP و 5G والألياف الضوئية والبنية التحتية الرقمية',
    'Telecom Specialisations': 'تخصصات الاتصالات',
    'Technology Areas': 'مجالات التقنية',

    /* ── Common: Section eyebrows ── */
    'Section Eyebrow': 'القسم',

    /* ── Contact: Additional ── */
    'Send a Message': 'إرسال رسالة',
    'What Would You Like To Do?': 'ماذا تريد أن تفعل؟',

    /* ── Common: More tags ── */
    'Completed': 'مكتملة',
    'Military': 'عسكري',
    'Hospitality': 'ضيافة',
    'Electrical': 'كهرباء',

    /* ── Downloads: Certificates section ── */
    'Certificate Downloads': 'تحميلات الشهادات',
    'Credentials': 'الاعتمادات',
    'Certificates &': 'الشهادات و',
    'PMP® Certificate': 'شهادة PMP®',
    'Project Management Institute · 2007': 'معهد إدارة المشاريع · 2007',
    'BA Diploma Certificate': 'شهادة دبلوم إدارة الأعمال',
    'Edinburgh Business School · 2017': 'كلية إدنبرة للأعمال · 2017',
    'B.Sc. University Certificate': 'شهادة بكالوريوس الجامعة',
    'Helwan University · 1996': 'جامعة حلوان · 1996',
    'Available upon request': 'متاح عند الطلب',
    'Siemens Experience Certificate': 'شهادة خبرة سيمنز',
    'Siemens AG · Egypt': 'سيمنز · مصر',
    'Appreciation Certificates': 'شهادات التقدير',
    'Various organisations · Multiple awards': 'مؤسسات متنوعة · جوائز متعددة',
    'View Awards →': 'عرض التكريمات ←',
    'Military Service Certificate': 'شهادة الخدمة العسكرية',
    'Egyptian Armed Forces · Completed': 'القوات المسلحة المصرية · مكتملة',
    '⬇ Download': '⬇ تحميل',

    /* ── Downloads: Request documents ── */
    'Request documents': 'طلب وثائق',
    'Request Additional Documents': 'طلب وثائق إضافية',
    'For recommendation letters, project portfolios, reference documents, additional certificates or any other professional documentation, please get in touch directly.': 'لخطابات التوصية ومعارض المشاريع ووثائق المرجع أو الشهادات الإضافية أو أي وثائق مهنية أخرى، يرجى التواصل مباشرة.',
    '✉ Contact Me': '✉ تواصل معي',

    /* ── Common: More nav/footer ── */
    'Search': 'بحث',
    'All Skills': 'كل المهارات',

    /* ── Featured Projects Page ── */
    'Featured Projects': 'المشاريع المميزة',
    'Featured Mega Projects': 'المشاريع الكبرى المميزة',
    'Six flagship projects spanning Construction, Hospitality, Telecommunications, Infrastructure, Healthcare and Railway sectors — delivered across Saudi Arabia, Egypt and Sudan over 25+ years of executive leadership.': 'ستة مشاريع رائدة تمتد عبر قطاعات الإنشاءات والضيافة والاتصالات والبنية التحتية والرعاية الصحية والسكك الحديدية — تم تسليمها في السعودية ومصر والسودان على مدى أكثر من 25 عاماً من القيادة التنفيذية.',
    'Mega Projects': 'مشاريع كبرى',
    'Countries': 'دول',
    'Years': 'سنوات',
    'Sectors': 'قطاعات',
    '🏟 Olympic City': '🏟 المدينة الأولمبية',
    '📡 STC FTTH': '📡 اتصالات السعودية للألياف',
    '🚂 Railways': '🚂 السكك الحديدية',
    '🌐 New Capital Fiber': '🌐 ألياف العاصمة الجديدة',
    '🏨 Sheraton Hotel': '🏨 فندق شيراتون',
    '🏥 Tanta Hospital': '🏥 مستشفى طنطا',

    /* ── FP: Project 1 - Olympic City ── */
    'National Prestige Project · Construction · Hospitality': 'مشروع وطني مرموق · إنشاءات · ضيافة',
    'Egyptian International Olympic City': 'المدينة الأولمبية الدولية المصرية',
    'Country': 'الدولة',
    '🇪🇬 Egypt – New Administrative Capital': '🇪🇬 مصر – العاصمة الإدارية الجديدة',
    'Client': 'العميل',
    'ACUD (Administrative Capital for Urban Development)': 'العاصمة الإدارية للتنمية الحضرية',
    'Role': 'الدور',
    'Lead Consultant Project Manager': 'مدير مشروع استشاري رئيسي',
    'Employer': 'جهة العمل',
    'Sabbour Consulting': 'صبور للاستشارات',
    'Duration': 'المدة',
    '2020 – 2023 (3 Years)': '2020 – 2023 (3 سنوات)',
    'Project Type': 'نوع المشروع',
    'Smart City / ELV / ICT / Hospitality': 'مدينة ذكية / أنظمة منخفضة الجهد / تكنولوجيا المعلومات / ضيافة',
    'Responsibilities': 'المسؤوليات',
    'Light Current Systems (ELV) design, procurement and delivery': 'تصميم وأنظمة التيار الخفيف والمشتريات والتسليم',
    'Building Management Systems (BMS) integration and commissioning': 'تكامل وتشغيل أنظمة إدارة المباني',
    'CCTV surveillance infrastructure planning and installation': 'تخطيط وتركيب بنية كاميرات المراقبة',
    'Fire Alarm systems design and implementation': 'تصميم وتنفيذ أنظمة إنذار الحريق',
    'Access Control systems for stadium and hotel buildings': 'أنظمة التحكم في الدخول للملعب ومباني الفندق',
    'Data Network infrastructure for the entire Olympic complex': 'بنية شبكة البيانات للمجمع الأولمبي بالكامل',
    'Hotel Buildings engineering and hospitality facilities oversight': 'إشراف هندسي على مباني الفندق ومرافق الضيافة',
    'Stakeholder management with ACUD, contractors and government entities': 'إدارة أصحاب المصلحة مع العاصمة الإدارية والمقاولين والجهات الحكومية',
    'Full project lifecycle: design, procurement, QA, delivery and handover': 'دورة حياة المشروع الكاملة: التصميم والمشتريات وضمان الجودة والتسليم والتسليم النهائي',
    'Major Achievements': 'الإنجازات الرئيسية',
    'Delivered both Olympic City ELV/FTTH and New Capital Fiber Network': 'تم تسليم مدينة الألعاب الأولمبية والأنظمة منخفضة الجهد/الألياف وشبكة ألياف العاصمة الجديدة',
    'on schedule': 'في الموعد المحدد',
    'against non-extendable national deadlines': 'ضد مواعيد وطنية غير قابلة للتمديد',
    'Zero delay on a nationally prestigious project': 'صفر تأخير في مشروع وطني مرموق',
    'Successfully managed multi-disciplinary engineering teams across all ELV systems': 'إدارة ناجحة لفرق هندسية متعددة التخصصات عبر جميع أنظمة التيار الخفيف',
    'Full integration of BMS, CCTV, Fire Alarm, Access Control and Data Network': 'تكامل كامل لأنظمة إدارة المباني وكاميرات المراقبة وإنذار الحريق والتحكم في الدخول وشبكة البيانات',
    'Technologies': 'التقنيات',
    'ELV': 'الأنظمة منخفضة الجهد',
    'BMS': 'نظام إدارة المباني',
    'CCTV': 'كاميرات المراقبة',
    'Fire Alarm': 'إنذار الحريق',
    'Access Control': 'التحكم في الدخول',
    'Data Network': 'شبكة البيانات',
    'FTTH': 'الألياف حتى المنزل',
    'Hotel Buildings': 'مباني الفندق',
    'Hospitality': 'الضيافة',
    'Project Controls Activities': 'أنشطة التحكم بالمشاريع',
    'Planning': 'التخطيط',
    'Scheduling': 'الجدولة',
    'Cost Control': 'ضبط التكلفة',
    'Risk Management': 'إدارة المخاطر',
    'Stakeholder Management': 'إدارة أصحاب المصلحة',
    'QA / QC': 'ضمان / ضبط الجودة',
    'KPIs': 'مؤشرات الأداء',
    'Days Delay': 'أيام التأخير',
    'Systems Integrated': 'أنظمة مدمجة',
    'On Schedule': 'في الموعد',
    'Timeline': 'الجدول الزمني',
    '2020 – Q1': '2020 – الربع الأول',
    'Project initiation, stakeholder alignment with ACUD': 'بدء المشروع وتوافق أصحاب المصلحة مع العاصمة الإدارية',
    '2020 – Q3': '2020 – الربع الثالث',
    'ELV systems design and procurement planning': 'تصميم أنظمة التيار الخفيف وتخطيط المشتريات',
    '2021': '2021',
    'BMS, CCTV, Fire Alarm installation and integration': 'تركيب وتكامل أنظمة إدارة المباني وكاميرات المراقبة وإنذار الحريق',
    '2022': '2022',
    'Access Control, Data Network, FTTH deployment': 'نشر أنظمة التحكم في الدخول وشبكة البيانات والألياف',
    '2023': '2023',
    'Final commissioning, QA, handover — on schedule': 'التشغيل النهائي وضمان الجودة والتسليم — في الموعد',
    'Lessons Learned': 'الدروس المستفادة',
    'Multi-system integration in a national prestige project requires early stakeholder alignment and a single source of truth for progress tracking. Integrating BMS, CCTV, Fire Alarm and Access Control under one PMO umbrella prevented interface conflicts and ensured zero-delay delivery against a non-extendable government deadline.': 'تكامل الأنظمة المتعددة في مشروع وطني مرموق يتطلب توافقاً مبكراً لأصحاب المصلحة ومصدراً موحداً للحقيقة لتتبع التقدم. دمج أنظمة إدارة المباني وكاميرات المراقبة وإنذار الحريق والتحكم في الدخول تحت مظلة مكتب إدارة مشاريع واحدة منع تعارضات الواجهات وضمن تسليماً صفر تأخير ضد موعد حكومي غير قابل للتمديد.',
    'Gallery': 'المعرض',

    /* ── FP: Project 2 - STC ── */
    '10-Year National Programme · Telecommunications': 'برنامج وطني لمدة 10 سنوات · اتصالات',
    'STC Saudi Arabia Fixed Network Program': 'برنامج الشبكة الثابتة للاتصالات السعودية',
    '🇸🇦 Kingdom of Saudi Arabia (Multiple Regions)': '🇸🇦 المملكة العربية السعودية (مناطق متعددة)',
    'Saudi Telecom Company (STC)': 'شركة الاتصالات السعودية',
    'Senior Project Control Engineer / Planning Engineer': 'مهندس تحكم أول بالمشاريع / مهندس تخطيط',
    'Norconsult': 'نوركونسلت',
    'December 2007 – December 2017 (10 Years)': 'ديسمبر 2007 – ديسمبر 2017 (10 سنوات)',
    'National FTTH / FTTx / OSP / ISP': 'ألياف حتى المنزل / النقطة / مسارات خارجية وداخلية وطنية',
    'National FTTH rollout planning and project controls across all KSA regions': 'تخطيط نشر الألياف حتى المنزل الوطني والتحكم بالمشاريع عبر جميع مناطق المملكة',
    'FTTx network expansion programme management with 20+ concurrent projects': 'إدارة برنامج توسيع شبكة النقطة مع 20+ مشروع متزامن',
    'OSP and ISP programme governance, progress monitoring and reporting': 'حوكمة برامج المسارات الخارجية والداخلية ومراقبة التقدم والتقارير',
    'PMO governance, executive reporting and KPI dashboard management': 'حوكمة مكتب إدارة المشاريع والتقارير التنفيذية وإدارة لوحات مؤشرات الأداء',
    'Designed and built custom ERP system (MS Access VBA + SQL) for contractor tracking': 'تصميم وبناء نظام تخطيط موارد مؤسسة مخصص (أكسس في بي إيه + إس كيو إل) لتتبع المقاولين',
    'Automated reporting pipelines using n8n and Docker (containerized workflows)': 'أتمتة خطوط التقارير باستخدام إنفين ودوكر (تدفقات محاوية)',
    'Stakeholder management with STC, Norconsult and 70+ subcontractors': 'إدارة أصحاب المصلحة مع الاتصالات السعودية ونوركونسلت و70+ مقاول من الباطن',
    'Earned Value Management (EVM) analysis and variance reporting': 'تحليل القيمة المكتسبة والتقارير الانحرافية',
    'Retained by STC/Norconsult for': 'الاحتفاظ بي من الاتصالات السعودية/نوركونسلت لـ',
    '10 consecutive years': '10 سنوات متتالية',
    '— unprecedented in the programme': '— رقم قياسي في البرنامج',
    'Managed': 'إدارة',
    '20+ simultaneous FTTH projects': '20+ مشروع ألياف متزامن',
    'across the Kingdom': 'عبر المملكة',
    'Reduced reporting effort by': 'تخفيض جهد التقارير بنسبة',
    '60%': '60%',
    'through custom ERP and automation': 'عبر نظام مخصص وأتمتة',
    'Eliminated manual verification bottlenecks across dozens of sites': 'القضاء على اختناقات التحقق اليدوي عبر عشرات المواقع',
    'Accelerated executive reporting cycles from days to hours': 'تسريع دورات التقارير التنفيذية من أيام إلى ساعات',
    '⭐ Flagship': '⭐ مشروع رائد',
    'FTTH/FTTx': 'الألياف حتى المنزل/النقطة',
    'OSP/ISP': 'مسارات خارجية/داخلية',
    'Primavera P6': 'بريمافيرا P6',
    'MS Project': 'مشروع مايكروسوفت',
    'MS Access VBA': 'أكسس في بي إيه',
    'SQL': 'إس كيو إل',
    'n8n': 'إنفين',
    'Docker': 'دوكر',
    'Power BI': 'باور باي آي',
    'EVM Analysis': 'تحليل القيمة المكتسبة',
    'KPI Dashboards': 'لوحات مؤشرات الأداء',
    'Contractor Management': 'إدارة المقاولين',
    'Executive Reporting': 'التقارير التنفيذية',
    'Years Retained': 'سنوات الاحتفاظ',
    'Concurrent Projects': 'مشاريع متزامنة',
    'Reporting Reduction': 'تخفيض التقارير',
    'Contractors Managed': 'مقاولون مدارون',
    '2007 – Dec': '2007 – ديسمبر',
    'Joined Norconsult/STC programme — FTTH national rollout': 'الانضمام لبرنامج نوركونسلت/الاتصالات السعودية — نشر الألياف الوطني',
    '2008 – 2012': '2008 – 2012',
    'Managed planning controls for multi-region FTTH deployment': 'إدارة ضوابط التخطيط لنشر الألياف متعدد المناطق',
    '2012 – 2015': '2012 – 2015',
    'Designed and deployed custom ERP for contractor tracking': 'تصميم ونشر نظام مخصص لتتبع المقاولين',
    '2015 – 2017': '2015 – 2017',
    'Containerized automation pipelines (n8n + Docker), programme-wide adoption': 'خطوط أتمتة محاوية (إنفين + دوكر)، اعتماد على مستوى البرنامج',
    '2017 – Dec': '2017 – ديسمبر',
    'Programme completion after 10-year engagement': 'اكتمال البرنامج بعد ارتباط 10 سنوات',
    'A national programme with 20+ concurrent projects cannot rely on manual reporting. Building a custom ERP as a single source of truth, then layering containerized automation on top, reduced reporting effort by 60% and eliminated blind spots. The key lesson: invest in systems early, and the ROI compounds across the programme lifecycle.': 'البرنامج الوطني مع 20+ مشروع متزامن لا يمكن الاعتماد فيه على التقارير اليدوية. بناء نظام مخصص كمصدر موحد للحقيقة، ثم إضافة طبقة أتمتة محاوية فوقه، خفّض جهد التقارير بنسبة 60% وقضى على النقاط العمياء. الدرس الرئيسي: استثمر في الأنظمة مبكراً، والعائد يتضاعف عبر دورة حياة البرنامج.',

    /* ── FP: Project 3 - Railways ── */
    'National Infrastructure · Railway': 'بنية تحتية وطنية · سكك حديدية',
    'Egypt National Railways Modernization': 'تحديث السكك الحديدية القومية المصرية',
    '🇪🇬 Egypt': '🇪🇬 مصر',
    'Egyptian National Railways (ENR)': 'السكك الحديدية المصرية',
    'Senior Site Manager / Site Manager': 'مدير موقع أول / مدير موقع',
    'Benya Systems / Fiber Misr – Alstom': 'بينيا سيستمز / فاير مصر – ألستوم',
    '2017 – 2020 (3 Years)': '2017 – 2020 (3 سنوات)',
    'Railway / Telecommunications / Fiber Optic': 'سكك حديدية / اتصالات / ألياف ضوئية',
    'Site management for fiber optic network deployment across Egypt\'s national railway': 'إدارة الموقع لنشر شبكة الألياف الضوئية عبر السكك الحديدية الوطنية المصرية',
    'Coordination with Alstom (global rail leader) for telecom systems integration': 'التنسيق مع ألستوم (القائد العالمي للسكك) لدمج أنظمة الاتصالات',
    'OSP fiber optic cable installation along railway corridors': 'تركيب كابلات الألياف الضوئية الخارجية على طول ممرات السكك',
    'Site supervision, quality control and safety compliance': 'الإشراف على الموقع وضبط الجودة والامتثال للسلامة',
    'Progress reporting and stakeholder coordination with ENR': 'تقارير التقدم والتنسيق مع أصحاب المصلحة في السكك الحديدية',
    'Contractor management and site team leadership': 'إدارة المقاولين وقيادة فريق الموقع',
    'Successfully deployed fiber optic infrastructure across national railway corridors': 'نشر ناجح للبنية التحتية للألياف الضوئية عبر ممرات السكك الوطنية',
    'Partnered with Alstom for integrated telecom systems delivery': 'شراكة مع ألستوم لتسليم أنظمة اتصالات متكاملة',
    'Managed multi-site deployment teams across different Egyptian regions': 'إدارة فرق نشر متعددة المواقع عبر مناطق مصرية مختلفة',
    'Railways': 'السكك الحديدية',
    'Fiber Optic': 'الألياف الضوئية',
    'OSP': 'المسارات الخارجية',
    'Telecom': 'اتصالات',
    'Alstom': 'ألستوم',
    'ENR': 'السكك الحديدية المصرية',
    'Site Supervision': 'الإشراف على الموقع',
    '3': '3',
    'Multi': 'متعدد',
    'Site Deployment': 'نشر الموقع',
    'Partnership': 'شراكة',
    '2017': '2017',
    'Joined Benya Systems / Fiber Misr – Alstom partnership': 'الانضمام لشراكة بينيا سيستمز / فاير مصر – ألستوم',
    '2018': '2018',
    'Multi-corridor fiber deployment along railway lines': 'نشر ألياف متعدد الممرات على طول خطوط السكك',
    '2019': '2019',
    'Integration with Alstom telecom systems': 'الدمج مع أنظمة اتصالات ألستوم',
    '2020': '2020',
    'Project completion and handover to ENR': 'اكتمال المشروع والتسليم للسكك الحديدية المصرية',
    'Railway fiber deployment requires meticulous site coordination along active corridors. Safety compliance and scheduling around train operations were critical. Partnering with a global leader like Alstom reinforced the value of international standards in national infrastructure programmes.': 'نشر ألياف السكك يتطلب تنسيقاً دقيقاً للموقع على طول ممرات نشطة. كان الامتثال للسلامة والجدولة حول عمليات القطارات أمراً حاسماً. الشراكة مع قائد عالمي مثل ألستوم عززت قيمة المعايير الدولية في برامج البنية التحتية الوطنية.',

    /* ── FP: Project 4 - New Capital Fiber ── */
    'Smart Capital Project · Infrastructure': 'مشروع عاصمة ذكية · بنية تحتية',
    'New Administrative Capital Fiber Project': 'مشروع ألياف العاصمة الإدارية الجديدة',
    'ACUD': 'العاصمة الإدارية',
    '2020 – 2023': '2020 – 2023',
    'Smart City / FTTH / Fiber Backbone': 'مدينة ذكية / ألياف حتى المنزل / شبكة ألياف رئيسية',
    'Fiber optic network planning, design and implementation for Egypt\'s new capital': 'تخطيط وتصميم وتنفيذ شبكة الألياف الضوئية للعاصمة الجديدة بمصر',
    'Full fiber backbone and FTTH infrastructure for a smart city': 'شبكة ألياف رئيسية كاملة وبنية ألياف حتى المنزل لمدينة ذكية',
    'Stakeholder management with ACUD and government entities': 'إدارة أصحاب المصلحة مع العاصمة الإدارية والجهات الحكومية',
    'Procurement, QA and delivery management': 'إدارة المشتريات وضمان الجودة والتسليم',
    'Integrated with Olympic City ELV/FTTH scope under unified PMO': 'دمج مع نطاق المدينة الأولمبية الأنظمة منخفضة الجهد/الألياف تحت مظلة موحدة لمكتب إدارة المشاريع',
    'Delivered fiber infrastructure': 'تسليم بنية الألياف',
    'alongside Olympic City project': 'بجانب مشروع المدينة الأولمبية',
    'Established smart city fiber backbone for Egypt\'s new capital': 'تأسيس شبكة ألياف رئيسية لمدينة ذكية للعاصمة الجديدة بمصر',
    'Zero delay against national deadline': 'صفر تأخير ضد موعد وطني',
    'Smart City': 'مدينة ذكية',
    'Procurement': 'المشتريات',
    'Smart': 'ذكي',
    'City Fiber': 'ألياف المدينة',
    'Network planning and design for new capital': 'تخطيط وتصميم الشبكة للعاصمة الجديدة',
    '2021': '2021',
    'Fiber backbone deployment': 'نشر الشبكة الرئيسية للألياف',
    '2022': '2022',
    'FTTH infrastructure installation': 'تركيب بنية الألياف حتى المنزل',
    '2023': '2023',
    'Completion and handover — on schedule': 'الاكتمال والتسليم — في الموعد',
    'Delivering fiber infrastructure for a new smart city in parallel with the Olympic City project demonstrated the value of unified PMO governance. Shared resources, aligned schedules and a single reporting framework across both ACUD projects prevented conflicts and ensured both delivered on time.': 'تسليم بنية الألياف لمدينة ذكية جديدة بالتوازي مع مشروع المدينة الأولمبية أظهر قيمة الحوكمة الموحدة لمكتب إدارة المشاريع. الموارد المشتركة والجداول المتوافقة وإطار تقارير موحد عبر مشروعَي العاصمة الإدارية منع التعارضات وضمن تسليم كليهما في الوقت المحدد.',
    '光纤': 'ألياف',

    /* ── FP: Project 5 - Sheraton ── */
    '5-Star Hospitality · Hotel Engineering': 'ضيافة 5 نجوم · هندسة الفندق',
    'Sheraton El Gezirah Hotel': 'فندق الجزيرة شيراتون',
    '🇪🇬 Egypt – Cairo': '🇪🇬 مصر – القاهرة',
    'Sheraton El Gezirah (5-Star Hotel)': 'الجزيرة شيراتون (فندق 5 نجوم)',
    'Senior Maintenance Shift Engineer': 'مهندس ورديات صيانة أول',
    'Sheraton El Gezirah Hotel': 'فندق الجزيرة شيراتون',
    'September 1999 – June 2000': 'سبتمبر 1999 – يونيو 2000',
    '5-Star Hotel Engineering / MEP': 'هندسة فندق 5 نجوم / كهروميكانيكية',
    '5-Star Hotel engineering operations and maintenance': 'عمليات وصيانة هندسة فندق 5 نجوم',
    'MEP Systems management: HVAC, Electrical, Mechanical, Plumbing': 'إدارة الأنظمة الكهروميكانيكية: التكييف والكهرباء والميكانيكا والسباكة',
    'Preventive maintenance scheduling and execution': 'جدولة وتنفيذ الصيانة الوقائية',
    'Shift engineering leadership for hotel operations': 'قيادة هندسة الورديات لعمليات الفندق',
    'Building systems monitoring and fault resolution': 'مراقبة أنظمة المبنى وحل الأعطال',
    'Coordination with hotel management for guest comfort and safety': 'التنسيق مع إدارة الفندق لراحة وسلامة النزلاء',
    'Maintenance of kitchen equipment, laundry systems and pool facilities': 'صيانة معدات المطبخ وأنظمة المغسلة ومرافق المسبح',
    'Fire safety systems testing and compliance': 'اختبار أنظمة السلامة من الحريق والامتثال',
    'Maintained 5-star hotel engineering standards with zero guest-impacting downtime': 'الحفاظ على معايير هندسة فندق 5 نجوم مع صفر توقف مؤثر على النزلاء',
    'Implemented systematic preventive maintenance scheduling': 'تطبيق جدولة منهجية للصيانة الوقائية',
    'Gained foundational hospitality engineering experience critical for later hotel construction projects': 'اكتساب خبرة هندسية أساسية في الضيافة حاسمة لمشاريع بناء الفنادق لاحقاً',
    'HVAC': 'التكييف',
    'Electrical': 'الكهرباء',
    'Mechanical': 'الميكانيكا',
    'Plumbing': 'السباكة',
    'Preventive Maintenance': 'الصيانة الوقائية',
    'MEP': 'كهروميكانيكية',
    '5-Star Hotel': 'فندق 5 نجوم',
    'Fire Safety': 'السلامة من الحريق',
    'Maintenance Planning': 'تخطيط الصيانة',
    'Shift Scheduling': 'جدولة الورديات',
    'Safety Compliance': 'الامتثال للسلامة',
    'Fault Management': 'إدارة الأعطال',
    'Reporting': 'التقارير',
    '5★': '5★',
    'Hotel Standard': 'معيار الفندق',
    'Guest Downtime': 'توقف النزلاء',
    '24/7': '24/7',
    'Operations': 'العمليات',
    '1999 – Sep': '1999 – سبتمبر',
    'Joined Sheraton El Gezirah as Shift Engineer': 'الانضمام لفندق الجزيرة شيراتون كمهندس ورديات',
    '1999 – Q4': '1999 – الربع الرابع',
    'HVAC and electrical systems maintenance': 'صيانة أنظمة التكييف والكهرباء',
    '2000 – Q1': '2000 – الربع الأول',
    'Preventive maintenance programme implementation': 'تنفيذ برنامج الصيانة الوقائية',
    '2000 – Jun': '2000 – يونيو',
    'Departed for Siemens project control role': 'المغادرة لدور التحكم بالمشاريع في سيمنز',
    '5-star hotel engineering demands zero-tolerance for downtime. This experience in MEP systems, preventive maintenance and hospitality operations became the foundation for later managing hotel construction projects (Olympic City hotel buildings). Understanding both operations and construction of hospitality facilities is a rare combination highly valued in the Gulf market.': 'هندسة فنادق 5 نجوم تتطلب صفر تسامح مع التوقف. هذه الخبرة في الأنظمة الكهروميكانيكية والصيانة الوقائية وعمليات الضيافة أصبحت الأساس لإدارة مشاريع بناء الفنادق لاحقاً (مباني فندق المدينة الأولمبية). فهم كل من العمليات والبناء لمرافق الضيافة هو مزيج نادر ذو قيمة عالية في سوق الخليج.',

    /* ── FP: Project 6 - Tanta Hospital ── */
    'Healthcare Infrastructure': 'بنية تحتية للرعاية الصحية',
    'Tanta University Hospital': 'مستشفى جامعة طنطا',
    '🇪🇬 Egypt – Tanta': '🇪🇬 مصر – طنطا',
    'Tanta University': 'جامعة طنطا',
    'Project Engineer': 'مهندس مشروع',
    'Early Career Engagement': 'مرحلة مبكرة من المسيرة',
    'Early Career Project': 'مشروع مرحلة مبكرة',
    'Healthcare / Infrastructure': 'رعاية صحية / بنية تحتية',
    'Healthcare infrastructure engineering support': 'دعم هندسي للبنية التحتية للرعاية الصحية',
    'Building systems coordination for hospital facilities': 'تنسيق أنظمة المباني لمرافق المستشفى',
    'Electrical and mechanical systems assistance': 'مساعدة في الأنظمة الكهربائية والميكانيكية',
    'Site engineering and documentation': 'هندسة الموقع والتوثيق',
    'Gained healthcare infrastructure experience early in career': 'اكتساب خبرة البنية التحتية للرعاية الصحية مبكراً في المسيرة',
    'Developed understanding of hospital engineering requirements and standards': 'تطوير فهم متطلبات ومعايير هندسة المستشفيات',
    'Built foundation for later multi-sector project management expertise': 'تأسيس قاعدة لخبرة إدارة المشاريع متعددة القطاعات لاحقاً',
    'Healthcare': 'الرعاية الصحية',
    'Infrastructure': 'البنية التحتية',
    'Hospital': 'مستشفى',
    'Site Engineering': 'هندسة الموقع',
    'Documentation': 'التوثيق',
    'Coordination': 'التنسيق',
    'Sector': 'القطاع',
    'Foundation': 'الأساس',
    'Experience': 'الخبرة',
    'Early Career': 'مرحلة مبكرة',
    'Hospital infrastructure engineering engagement': 'مشاركة هندسية في البنية التحتية للمستشفى',
    'Transition': 'الانتقال',
    'Moved to Siemens telecom projects — broadening multi-sector expertise': 'الانتقال لمشاريع اتصالات سيمنز — توسيع الخبرة متعددة القطاعات',
    'Healthcare infrastructure requires strict adherence to safety and operational standards. This early experience in hospital engineering provided cross-sector foundation knowledge that proved invaluable when managing diverse mega projects later in my career.': 'البنية التحتية للرعاية الصحية تتطلب الالتزام الصارم بمعايير السلامة والتشغيل. هذه الخبرة المبكرة في هندسة المستشفيات وفرت معرفة أساسية عبر القطاعات أثبتت قيمتها عند إدارة مشاريع كبرى متنوعة لاحقاً في مسيرتي.',

    /* ── FP: CTA Bar ── */
    'Ready to Deliver Your Next Mega Project?': 'جاهز لتسليم مشروعك الكبير القادم؟',
    '25+ years of executive project controls leadership across Construction, Hospitality, Telecom, Infrastructure, Healthcare & Railway sectors.': '+25 عاماً من القيادة التنفيذية للتحكم بالمشاريع عبر قطاعات الإنشاءات والضيافة والاتصالات والبنية التحتية والرعاية الصحية والسكك الحديدية.',
    '⬇ Download CV': '⬇ تحميل السيرة',
    'Contact Me': 'تواصل معي',
    'LinkedIn': 'لينكدإن',

    /* ── FP: Breadcrumb ── */
    'Dashboard': 'الرئيسية',
  };

  /* ── Reverse dictionary for AR→EN (for switching back) ── */
  const REVERSE_DICT = {};
  for (const [en, ar] of Object.entries(DICT)) {
    REVERSE_DICT[ar] = en;
  }

  /* ── Get/Set language ── */
  function get() {
    return localStorage.getItem(LANG_KEY) || EN;
  }

  function set(lang) {
    localStorage.setItem(LANG_KEY, lang);
    apply(lang);
  }

  function toggle() {
    set(get() === AR ? EN : AR);
  }

  /* ── Apply language to page ── */
  function apply(lang) {
    const html = document.documentElement;

    if (lang === AR) {
      html.setAttribute('dir', 'rtl');
      html.setAttribute('lang', 'ar');
      html.classList.add('i18n-rtl');
      loadArabicFont();
      translateTo(DICT);
    } else {
      html.setAttribute('dir', 'ltr');
      html.setAttribute('lang', 'en');
      html.classList.remove('i18n-rtl');
      translateTo(REVERSE_DICT);
    }

    // Update toggle button if present
    const btn = document.getElementById('i18n-toggle');
    if (btn) {
      btn.textContent = lang === AR ? 'English 🌐' : 'العربية 🌐';
      btn.setAttribute('aria-label', lang === AR ? 'Switch to English' : 'التبديل للعربية');
    }
  }

  /* ── Load Cairo font for Arabic ── */
  let fontLoaded = false;
  function loadArabicFont() {
    if (fontLoaded) return;
    fontLoaded = true;
    const link = document.createElement('link');
    link.rel = 'stylesheet';
    link.href = 'https://fonts.googleapis.com/css2?family=Cairo:wght@300;400;500;600;700;800;900&display=swap';
    document.head.appendChild(link);
  }

  /* ── Walk DOM and translate text nodes ── */
  function translateTo(dict) {
    // Translate text nodes
    const walker = document.createTreeWalker(
      document.body,
      NodeFilter.SHOW_TEXT,
      {
        acceptNode: function(node) {
          // Skip script, style, code, pre elements
          const parent = node.parentElement;
          if (!parent) return NodeFilter.FILTER_REJECT;
          const tag = parent.tagName.toLowerCase();
          if (['script', 'style', 'code', 'pre', 'textarea', 'noscript'].includes(tag)) {
            return NodeFilter.FILTER_REJECT;
          }
          // Skip if inside i18n toggle button
          if (parent.id === 'i18n-toggle') return NodeFilter.FILTER_REJECT;
          // Must have non-empty text
          const text = node.textContent.trim();
          if (!text) return NodeFilter.FILTER_REJECT;
          return NodeFilter.FILTER_ACCEPT;
        }
      }
    );

    const textNodes = [];
    let node;
    while (node = walker.nextNode()) {
      textNodes.push(node);
    }

    textNodes.forEach(function(textNode) {
      const original = textNode.textContent;
      const trimmed = original.trim();
      if (dict[trimmed]) {
        // Preserve surrounding whitespace
        const leading = original.match(/^\s*/)[0];
        const trailing = original.match(/\s*$/)[0];
        textNode.textContent = leading + dict[trimmed] + trailing;
        return;
      }

      // Try partial replacement: split on separators (·, &) and translate each part
      // This handles cases like "🇸🇦 Saudi Arabia · " where the text node includes a separator
      if (trimmed.includes('·') || trimmed.includes('&nbsp;')) {
        let modified = original;
        // Sort dict keys by length descending to match longer strings first
        const keys = Object.keys(dict).sort(function(a, b) { return b.length - a.length; });
        keys.forEach(function(key) {
          if (modified.includes(key)) {
            modified = modified.split(key).join(dict[key]);
          }
        });
        if (modified !== original) {
          textNode.textContent = modified;
        }
      }
    });

    // Translate attributes: placeholder, title, aria-label
    document.querySelectorAll('[placeholder], [title], [aria-label]').forEach(function(el) {
      ['placeholder', 'title', 'aria-label'].forEach(function(attr) {
        const val = el.getAttribute(attr);
        if (val && dict[val.trim()]) {
          el.setAttribute(attr, dict[val.trim()]);
        }
      });
    });

    // Translate data-i18n elements
    document.querySelectorAll('[data-i18n]').forEach(function(el) {
      const key = el.getAttribute('data-i18n');
      if (dict[key]) {
        el.textContent = dict[key];
      }
    });
  }

  /* ── Init on page load ── */
  function init() {
    // Apply saved language
    apply(get());

    // Add toggle button listener (may not exist yet if nav not injected)
    attachToggle();
  }

  /* ── Attach toggle button listener ── */
  function attachToggle() {
    const btn = document.getElementById('i18n-toggle');
    if (btn && !btn.dataset.i18nBound) {
      btn.addEventListener('click', toggle);
      btn.dataset.i18nBound = '1';
    }
  }

  /* ── Re-apply after dynamic content injection (nav/footer) ── */
  function refresh() {
    apply(get());
    attachToggle();
  }

  return { init, get, set, toggle, apply, refresh, attachToggle, AR, EN };
})();

// Expose globally for components.js and core.js
window.I18N = I18N;

// Auto-init on DOMContentLoaded
document.addEventListener('DOMContentLoaded', function() {
  I18N.init();
});

// Re-apply after components.js injects nav/footer
window.addEventListener('load', function() {
  I18N.refresh();
});
