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
