from _neg_utils import *

articles = load_articles()
nid = max(a['id'] for a in articles) + 1

# 16. Negotiating with Subcontractors
hero = download_hero(0, 'negotiating-with-subcontractors-construction-projects')
articles.append(make_article(nid, 'negotiating-with-subcontractors-construction-projects', 'Negotiation',
 ['negotiation', 'subcontractors', 'construction subcontractors', 'subcontract negotiation', 'back-to-back'],
 {'title': 'Negotiating with Subcontractors in Construction Projects: Strategies and Best Practices',
  'excerpt': 'Expert guide to subcontractor negotiation — selection, back-to-back terms, risk transfer, payment terms, performance management, and dispute resolution in construction subcontracting.',
  'keywords': ['subcontractor negotiation', 'construction subcontractors', 'subcontract terms', 'back-to-back contract', 'risk transfer subcontractor', 'subcontractor payment terms', 'subcontractor management', 'construction subcontracting', 'subcontractor selection', 'subcontractor performance'],
  'content': """## Negotiating with Subcontractors in Construction Projects

### The Subcontractor Negotiation Landscape

Subcontractors execute 60-80% of construction project value. Negotiating effectively with subcontractors is therefore one of the most critical skills for main contractors. The negotiation covers selection, terms, pricing, risk allocation, and ongoing performance management.

### Phase 1: Subcontractor Selection Negotiation

**Pre-Qualification:**
- Financial capacity: audited accounts, bank references, bonding capacity
- Technical capability: relevant project experience, key personnel CVs, equipment list
- Quality systems: ISO 9001 certification, QA/QC procedures
- Safety record: HSE statistics, OSHA/TRIR rates, safety management system
- Current workload: can they take on this project without overstretching?

**Tender Negotiation:**
- Maintain competitive tension with 3-4 pre-qualified subcontractors
- Request itemised breakdowns, not lump sums
- Compare unit rates against market benchmarks and previous projects
- Identify abnormally low rates (risk of cutting corners) and abnormally high rates
- Negotiate on total value, not individual rates — subcontractors may trade rates

### Phase 2: Subcontract Terms Negotiation

**1. Back-to-Back Provisions**

The subcontract should flow down the main contract obligations:
- Time: subcontract completion dates must precede main contract dates by a buffer
- Quality: same specifications, standards, and acceptance criteria
- Safety: same HSE requirements and reporting
- Liquidated damages: subcontractor LDs should match or exceed main contract LDs for their scope
- Insurance: subcontractor must maintain insurance matching main contract requirements

**Negotiation point:** Do not blindly back-to-back everything. Some main contract terms may be inappropriate for subcontractors (e.g., requiring a small subcontractor to provide parent company guarantees).

**2. Risk Allocation**

Transfer risks to the subcontractor that they can manage:
- Design risk: if subcontractor is design-build, transfer design responsibility
- Material price risk: fixed-price subcontract transfers escalation risk to subcontractor
- Productivity risk: lump sum transfers productivity risk to subcontractor
- Weather risk: generally retained by main contractor (force majeure provision)

**Retain risks that the main contractor must manage:**
- Site access and coordination
- Interface with other subcontractors
- Employer-directed changes
- Site conditions (unless subcontractor has investigated)

**3. Payment Terms**

- Payment timing: "pay-when-paid" vs "pay-if-paid" vs fixed payment terms
- Pay-when-paid: main contractor pays subcontractor within X days after receiving payment from employer — legal in some jurisdictions, prohibited in others
- Retention: typically 5-10%, released in two halves (completion + defects period)
- Advance payment: negotiate for mobilisation, with recovery from subsequent payments
- Payment conditional on: approved inspection, accepted deliverables, valid invoices

**4. Performance Security**

- Performance bond: 10% of subcontract value, from acceptable bank/insurer
- Advance payment guarantee: matches advance payment amount, reduces as recovered
- Warranty: defects liability period typically 12 months from taking-over
- Parent company guarantee: for large subcontracts with subsidiary entities

### Phase 3: Ongoing Negotiation During Execution

**1. Variation Negotiation**
- Subcontractor must submit variation pricing within agreed timeframe (typically 14 days)
- Main contractor reviews and approves/rejects before work starts
- Use subcontract rates where applicable; derive new rates for new items
- Negotiate overhead and profit percentage for variations (typically 10%)

**2. Delay and Disruption**
- Subcontractor must notify delays within 24-48 hours
- Main contractor assesses impact on overall programme
- If subcontractor causes delay: LDs, acceleration costs, recovery plan
- If main contractor causes delay to subcontractor: EOT, standing time costs, disruption

**3. Payment Disputes**
- Main contractor cannot withhold payment unreasonably
- Disputed amounts: pay undisputed portion, resolve disputed portion through negotiation
- Do not use payment as leverage for unrelated issues
- Document all payment-related communications

### Common Subcontractor Negotiation Mistakes

1. **Squeezing subcontractor margin too hard:** Results in cutting corners, claims, and poor quality
2. **Unclear scope boundaries:** Leads to scope gaps, disputes, and rework
3. **Inadequate back-to-back:** Main contractor bears risk that should have been transferred
4. **Late payment:** Damages trust and causes subcontractor to prioritise other projects
5. **Over-management:** Micromanaging subcontractors wastes resources and damages relationship
6. **No dispute mechanism:** Small disputes escalate because no resolution process exists"""},

 {'title': 'التفاوض مع المقاولين من الباطن في مشاريع الإنشاءات',
  'excerpt': 'دليل الخبراء للتفاوض مع المقاولين من الباطن — الاختيار، الشروط المرتدة، نقل المخاطر، شروط الدفع، إدارة الأداء، وحل النزاعات.',
  'keywords': ['تفاوض المقاولين من الباطن', 'مقاولو الباطن في الإنشاءات', 'شروط المقاول من الباطن', 'عقد مرتد', 'نقل المخاطر', 'شروط دفع المقاول من الباطن', 'إدارة المقاولين من الباطن'],
  'content': """## التفاوض مع المقاولين من الباطن في مشاريع الإنشاءات

### مشهد تفاوض المقاولين من الباطن

ينفذ المقاولون من الباطن 60-80% من قيمة مشروع الإنشاءات. التفاوض الفعال معهم من أهم المهارات للمقاول الرئيسي.

### المرحلة 1: تفاوض اختيار المقاول من الباطن

**التأهيل المسبق:**
- القدرة المالية: حسابات مدققة، مراجع بنكية، قدرة ضمان
- القدرة التقنية: خبرة مشاريع ذات صلة، سير ذاتية للموظفين الرئيسيين
- أنظمة الجودة: شهادة ISO 9001
- سجل السلامة: إحصائيات HSE

**تفاوض العطاء:**
- حافظ على توتر تنافسي مع 3-4 مقاولين مؤهلين
- اطلب تفصيلات بندية، لا مقطوع
- قارن أسعار الوحدة مع معايير السوق
- تفاوض على القيمة الإجمالية، لا الأسعار الفردية

### المرحلة 2: تفاوض شروط المقاول من الباطن

**1. الأحكام المرتدة**
يجب أن ينقل عقد الباطن التزامات العقد الرئيسي:
- الوقت: تواريخ إكمال الباطن يجب أن تسبق العقد الرئيسي بفترة
- الجودة: نفس المواصفات والمعايير
- الغرامات: غرامات الباطن يجب أن تطابق أو تتجاوز العقد الرئيسي

**2. توزيع المخاطر**
انقل للمقاول من الباطن المخاطر التي يمكنه إدارتها:
- مخاطر التصميم: إذا كان design-build
- مخاطر سعر المواد: سعر ثابت ينقل مخاطر التصاعد
- مخاطر الإنتاجية: مقطوع ينقل مخاطر الإنتاجية

احتفظ بالمخاطر التي يجب على المقاول الرئيسي إدارتها:
- وصول الموقع والتنسيق
- الواجهة مع مقاولين آخرين
- تغييرات صاحب العمل

**3. شروط الدفع**
- توقيت الدفع: "ادفع عند الدفع" مقابل شروط دفع ثابتة
- الاحتجاز: عادة 5-10%
- الدفع المقدم: للتعبئة مع الاسترداد من الدفعات اللاحقة

### المرحلة 3: التفاوض المستمر أثناء التنفيذ

**1. تفاوض التغييرات**
- يقدم المقاول من الباطن تسعير التغيير خلال 14 يوماً
- يراجع المقاول الرئيسي ويعتمد قبل بدء العمل
- استخدم أسعار الباطن حيث ينطبق

**2. التأخير والإعاقة**
- يجب إخطار التأخيرات خلال 24-48 ساعة
- إذا تسبب الباطن في التأخير: غرامات، تكاليف تسريع
- إذا تسبب المقاول الرئيسي: تمديد، تكاليف وقوف

### أخطاء تفاوض المقاولين من الباطن الشائعة

1. ضغط هامش الباطن بشدة → قطع زوايا، مطالبات، جودة سيئة
2. حدود نطاق غير واضحة → فجوات نطاق، نزاعات
3. مرتد غير كافٍ → المقاول الرئيسي يتحمل مخاطر كان يجب نقلها
4. دفع متأخر → يضر الثقة ويجعل الباطن يعطي أولوية لمشاريع أخرى"""}, hero, 15))
nid += 1

# 17. Negotiation in Public-Private Partnerships
hero = download_hero(1, 'negotiation-public-private-partnerships-construction')
articles.append(make_article(nid, 'negotiation-public-private-partnerships-construction', 'Negotiation',
 ['negotiation', 'PPP', 'P3', 'public private partnership', 'infrastructure', 'concession'],
 {'title': 'Negotiation in Public-Private Partnerships: Infrastructure Project Strategies',
  'excerpt': 'Expert guide to PPP negotiation — concession agreements, risk allocation, payment mechanisms, government guarantees, value for money, and lifecycle contract management for infrastructure projects.',
  'keywords': ['PPP negotiation', 'public private partnership', 'P3 negotiation', 'concession agreement', 'infrastructure negotiation', 'PPP risk allocation', 'availability payment', 'government guarantee', 'value for money PPP', 'lifecycle contract PPP'],
  'content': """## Negotiation in Public-Private Partnerships: Infrastructure Project Strategies

### Understanding PPP Negotiation Complexity

Public-Private Partnership (PPP) negotiations are among the most complex in construction. They involve multiple stakeholders (government, private consortium, lenders, insurers), long concession periods (15-30 years), and interrelated financial, technical, and legal terms that cannot be negotiated in isolation.

### PPP Structure and Key Negotiation Points

**1. Concession Agreement**

The concession agreement is the core PPP contract. Key negotiation points:

- **Concession period:** Typically 15-30 years. Longer periods reduce annual payment but increase risk exposure. Negotiate based on asset lifecycle and financing amortisation.

- **Scope definition:** Design, build, finance, operate, maintain (DBFOM) vs build-operate-transfer (BOT) vs design-build-finance (DBF). Each structure allocates risk differently.

- **Exclusivity:** Will the government guarantee no competing infrastructure? Critical for toll roads, ports, airports.

- **Handback requirements:** At concession end, the asset must be returned in specified condition. Negotiate condition standards, inspection process, and handback valuation.

**2. Risk Allocation**

PPP risk allocation follows the principle: allocate risk to the party best able to manage it.

| Risk | Typically Allocated To | Negotiation Considerations |
|------|----------------------|---------------------------|
| Design risk | Private party | If government provides reference design, who bears design errors? |
| Construction risk | Private party | Cost overrun, delay, defects — capped or uncapped? |
| Operating risk | Private party | Operating cost overrun, availability failure |
| Demand risk | Government (availability PPP) or Private (concession PPP) | Traffic volume, usage revenue |
| Regulatory risk | Government | Change in law, tax, environmental standards |
| Force majeure | Shared | Insurance, relief events, compensation events |
| Financing risk | Private party | Interest rate, refinancing, currency |

**3. Payment Mechanism**

**Availability-based payment:**
- Government pays fixed periodic amount if asset meets availability standards
- Deductions for unavailability, performance shortfalls
- Negotiate: availability definition, deduction levels, performance thresholds
- Advantage: demand risk stays with government

**Usage-based payment (concession):**
- Private party collects user fees (tolls, fares, port charges)
- Negotiate: tariff structure, tariff escalation, revenue sharing above threshold
- Revenue cap: government caps total revenue; excess returned to government
- Revenue floor: government guarantees minimum revenue; if actual is lower, government tops up

**4. Government Support and Guarantees**

- **Minimum revenue guarantee:** Government guarantees minimum traffic/revenue level
- **Viability gap funding:** Government contributes capital to make project financially viable
- **Tax exemptions:** Import duty waivers, tax holidays during construction
- **Land acquisition:** Government responsibility for acquiring and clearing land
- **Permitting:** Government fast-tracks permits and approvals

**Negotiation strategy:** Government support reduces private party risk but increases government fiscal exposure. Negotiate support that is necessary but not excessive.

**5. Financing Terms**

- **Debt-equity ratio:** Typically 70:30 to 80:20 for PPP projects. Higher leverage increases equity returns but increases financial risk.
- **Interest rates:** Fixed vs floating. Negotiate interest rate hedging or caps.
- **Refinancing:** Refinancing gains typically shared 50:50 between government and private party.
- **Drawdown schedule:** Align with construction milestones to minimise financing costs.
- **Reserve accounts:** Debt service reserve, maintenance reserve, insurance reserve — negotiate funding levels.

**6. Performance Standards and Penalties**

- Availability: uptime percentage (e.g., 98% for a toll road)
- Quality: ride quality index, lighting functionality, signage condition
- Safety: accident rate targets, response time for incidents
- Environmental: emissions, noise, water discharge compliance
- Penalties: per-event deduction, cumulative cap, step-in rights for persistent failure

### Phase 1: Bid-Stage Negotiation

- **Bid clarification:** Request clarification on ambiguous RFP terms before bidding
- **Bid negotiation:** Shortlisted bidders may negotiate specific terms before award
- **Best and final offer:** Government may request BAFO after initial negotiation round
- **Exclusivity period:** Government may grant exclusivity to preferred bidder for final negotiation

### Phase 2: Financial Close Negotiation

- **Lender requirements:** Lenders impose conditions precedent to disbursement
- **Step-in rights:** Lenders' right to replace the private party if they default
- **Direct agreements:** Between lenders and government — lender step-in, cure periods
- **Insurance requirements:** Coverage levels, named insureds, waiver of subrogation

### Phase 3: Lifecycle Negotiation During Concession

- **Change in law:** Who bears cost of regulatory changes? Negotiate relief mechanism.
- **Variation to scope:** Government-initiated changes — pricing, time, financing impact
- **Renegotiation triggers:** Material adverse change, force majeure, sustained underperformance
- **Refinancing:** Refinancing gain sharing mechanism
- **Dispute resolution:** Negotiation, mediation, expert determination, arbitration

### Common PPP Negotiation Challenges

1. **Long-term uncertainty:** 25-year projections are inherently unreliable — build in flexibility mechanisms
2. **Multi-party complexity:** Government, consortium, lenders, insurers, operators — all must agree
3. **Political risk:** Government changes may affect commitment — secure bipartisan support
4. **Demand forecasting:** Traffic/revenue projections often overly optimistic — negotiate revenue floors
5. **Change in law:** Regulatory environment evolves over 25 years — negotiate clear compensation mechanism
6. **Handback condition:** Asset condition at year 25 is difficult to specify today — negotiate condition standards and inspection process"""},

 {'title': 'التفاوض في شراكات القطاعين العام والخاص: استراتيجيات مشاريع البنية التحتية',
  'excerpt': 'دليل الخبراء لتفاوض PPP — اتفاقيات الامتياز، توزيع المخاطر، آليات الدفع، ضمانات الحكومة، القيمة مقابل المال، وإدارة العقود طويلة المدى لمشاريع البنية التحتية.',
  'keywords': ['تفاوض PPP', 'شراكة القطاعين العام والخاص', 'تفاوض P3', 'اتفاقية امتياز', 'تفاوض البنية التحتية', 'توزيع مخاطر PPP', 'دفع التوفر', 'ضمان الحكومة', 'القيمة مقابل المال'],
  'content': """## التفاوض في شراكات القطاعين العام والخاص

### فهم تعقيد تفاوض PPP

مفاوضات شراكات القطاعين العام والخاص (PPP) من أكثرها تعقيداً في الإنشاءات. تتضمن أطرافاً متعددين (حكومة، اتحاد خاص، مقرضين، مؤمنين)، فترات امتياز طويلة (15-30 سنة)، وشروطاً مالية وتقنية وقانونية مترابطة.

### هيكل PPP ونقاط التفاوض الرئيسية

**1. اتفاقية الامتياز**
- **فترة الامتياز:** عادة 15-30 سنة. الفترات الأطول تقلل الدفع السنوي لكن تزيد التعرض للمخاطر.
- **النطاق:** صمم، ابنِ، مول، شغل، صِن (DBFOM) مقابل ابنِ-شغل-انقل (BOT)
- **التميز:** هل تضمن الحكومة عدم وجود بنية تحتية منافسة؟
- **متطلبات الإعادة:** عند انتهاء الامتياز، يجب إعادة الأصل بحالة محددة.

**2. توزيع المخاطر**

| المخاطرة | المخصصة عادة لـ | اعتبارات التفاوض |
|------|----------------------|---------------------------|
| مخاطر التصميم | القطاع الخاص | إذا قدمت الحكومة تصميم مرجعي، من يتحمل الأخطاء؟ |
| مخاطر الإنشاء | القطاع الخاص | تجاوز التكلفة، التأخير، العيوب |
| مخاطر التشغيل | القطاع الخاص | تجاوز تكلفة التشغيل، فشل التوفر |
| مخاطر الطلب | الحكومة (توفر) أو الخاص (امتياز) | حجم المرور |
| مخاطر تنظيمية | الحكومة | تغيير القانون، الضرائب |
| القوة القاهرة | مشترك | التأمين، أحداث الإعفاء |

**3. آلية الدفع**

**دفع قائم على التوفر:**
- الحكومة تدفع مبلغاً دورياً ثابتاً إذا حقق الأصل معايير التوفر
- خصومات لعدم التوفر، قصور الأداء

**دفع قائم على الاستخدام (امتياز):**
- القطاع الخاص يجمع رسوم المستخدم (رسوم عبور، أجور)
- هيكل التعريفة، تصاعد التعريفة، مشاركة الإيراد فوق العتبة

**4. دعم الحكومة والضمانات**
- ضمان الحد الأدنى للإيراد
- تمويل فجوة الجدوى
- إعفاءات ضريبية
- الاستملاك: مسؤولية الحكومة
- الترخيص: الحكومة تسرع التصاريح

### المرحلة 1: تفاوض مرحلة العطاء
- توضيح العطاء، تفاوض العرض، أفضل عرض نهائي، فترة الإقصائية

### المرحلة 2: تفاوض الإغلاق المالي
- متطلبات المقرضين، حقوق التدخل، الاتفاقيات المباشرة، متطلبات التأمين

### المرحلة 3: تفاوض دورة الحياة أثناء الامتياز
- تغيير القانون، تغيير النطاق، محفزات إعادة التفاوض، إعادة التمويل، حل النزاعات

### تحديات تفاوض PPP الشائعة

1. عدم يقين طويل المدى: توقعات 25 سنة غير موثوقة بطبيعتها
2. تعقيد متعدد الأطراف
3. مخاطر سياسية: تغيير الحكومة
4. توقعات الطلب متفائلة مفرطة
5. تغيير القانون
6. حالة الإعادة"""}, hero, 16))
nid += 1

# 18. Negotiation in Design-Build Contracts
hero = download_hero(2, 'negotiation-design-build-contracts-construction')
articles.append(make_article(nid, 'negotiation-design-build-contracts-construction', 'Negotiation',
 ['negotiation', 'design-build', 'EPC', 'turnkey', 'construction contracts'],
 {'title': 'Negotiation in Design-Build and EPC Construction Contracts',
  'excerpt': 'Expert guide to design-build and EPC contract negotiation — employer requirements, design risk, performance guarantees, interface management, and turnkey delivery negotiation strategies.',
  'keywords': ['design-build negotiation', 'EPC negotiation', 'turnkey contract', 'design-build contract', 'employer requirements', 'design risk allocation', 'performance guarantee construction', 'EPC contract terms', 'design-build risk', 'lump sum turnkey'],
  'content': """## Negotiation in Design-Build and EPC Construction Contracts

### The Design-Build Negotiation Paradigm

Design-build (DB) and EPC (Engineer-Procure-Construct) contracts shift design responsibility to the contractor. This fundamentally changes the negotiation landscape compared to traditional design-bid-build. The contractor now controls both design and construction, creating different risk dynamics.

### Key Negotiation Points

**1. Employer Requirements vs Contractor Design**

The employer's requirements document is the foundation of a DB/EPC contract. Negotiation focuses on:

- **Completeness:** Are the employer requirements sufficiently detailed to define the expected outcome? Vague requirements lead to disputes over what was intended.
- **Performance specifications vs prescriptive specifications:** Performance specs give the contractor design freedom but require clear acceptance criteria. Prescriptive specs limit contractor innovation but reduce design risk.
- **Compliance standards:** Which codes, standards, and regulations apply? Negotiate specific versions to avoid future code changes affecting design.
- **Site conditions:** What site information has the employer provided? Is the contractor relying on it? Negotiate "reliance" provisions — if the employer provides geotechnical data, can the contractor rely on it?

**2. Design Review and Approval**

- **Employer review period:** Typically 14-21 days per submission. Negotiate shorter periods for critical path items.
- **Deemed approval:** If the employer does not respond within the review period, is the design deemed approved? Negotiate this carefully — employers resist it.
- **Review scope:** The employer reviews for compliance with requirements, NOT for technical correctness. The contractor remains responsible for design adequacy.
- **Design changes after approval:** Can the employer request changes after design approval? If so, how are cost and time impacts handled?

**3. Performance Guarantees**

DB/EPC contracts typically include performance guarantees:
- **Output guarantees:** production capacity, throughput, efficiency
- **Consumption guarantees:** energy use per unit output, water consumption
- **Availability guarantees:** uptime percentage over warranty period
- **Environmental guarantees:** emissions, noise, discharge levels

**Negotiation strategy:**
- Negotiate tolerance bands: 95% of guaranteed output is acceptable; below that, liquidated damages apply
- Cap LDs for performance: typically 10-15% of contract value
- Negotiate buy-out option: contractor can pay to reduce performance guarantee instead of remedial work
- Define test conditions: what are the conditions under which performance is measured?

**4. Lump Sum Price and Risk**

- **Fixed price:** The lump sum is fixed unless employer changes the scope. Negotiate clear change control procedures.
- **Price escalation:** In DB/EPC, the contractor typically bears material price escalation risk. Consider escalation clauses for long-duration projects.
- **Cost reduction:** If the contractor finds a cheaper design solution that meets requirements, who benefits? Negotiate gain-sharing provisions.
- **Basis of payment:** Milestone payments vs progress payments. Milestone payments align with deliverables; progress payments align with physical progress.

**5. Interface Management**

In complex DB/EPC projects, interfaces between systems are critical:
- **Mechanical-electrical interfaces:** Who designs the connection between the HVAC system and the electrical supply?
- **Civil-MEP interfaces:** Who coordinates slab penetrations for MEP services?
- **External interfaces:** Connection to utility networks, access roads, boundary conditions
- **Negotiation approach:** The contractor is responsible for all internal interfaces. The employer is responsible for external interfaces (utility connections, site boundaries) unless the contract states otherwise.

**6. Warranty and Defects**

- **Defects liability period:** Typically 12-24 months for DB/EPC (longer than design-bid-build)
- **Design warranty:** The contractor warrants the design for the defects period (and sometimes longer for latent defects)
- **Performance warranty:** Performance guarantees may extend beyond the defects period (e.g., 5 years for chiller efficiency)
- **Latent defects:** Who bears the cost of defects that appear after the warranty period? Negotiate latent defect coverage for structural elements.

### DB vs EPC vs LSTK — Negotiation Differences

**Design-Build (DB):**
- Employer provides requirements; contractor designs and builds
- Moderate risk transfer
- Employer has some design involvement through review process
- Typically used for buildings, infrastructure

**EPC (Engineer-Procure-Construct):**
- Similar to DB but with greater risk transfer to contractor
- Employer has minimal design involvement
- Contractor bears most risks including site conditions (usually)
- Typically used for industrial plants, power stations

**LSTK (Lump Sum Turnkey):**
- Maximum risk transfer — contractor delivers a turnkey facility
- Fixed price, fixed date
- Contractor bears nearly all risks
- Employer simply "turns the key" and operates
- Negotiation focus: ensure requirements are crystal clear; any ambiguity benefits the contractor

### Common DB/EPC Negotiation Pitfalls

1. **Ambiguous employer requirements:** The contractor interprets requirements differently from the employer — invest time in precise requirements
2. **Inadequate site investigation:** The contractor underestimates ground conditions — negotiate reliance on employer-provided data
3. **Design review delays:** The employer takes too long to review, delaying construction — negotiate deemed approval
4. **Scope creep:** The employer requests "small" changes that accumulate — enforce strict change control
5. **Performance test disputes:** Test conditions differ from operating conditions — define test conditions precisely
6. **Interface gaps:** No one is responsible for a critical interface — map all interfaces during negotiation"""},

 {'title': 'التفاوض في عقود التصميم-والتنفيذ و EPC في الإنشاءات',
  'excerpt': 'دليل الخبراء لتفاوض عقود التصميم-والتنفيذ و EPC — متطلبات صاحب العمل، مخاطر التصميم، ضمانات الأداء، إدارة الواجهات، واستراتيجيات التسليم المفتاح.',
  'keywords': ['تفاوض التصميم-والتنفيذ', 'تفاوض EPC', 'عقد تسليم المفتاح', 'عقد تصميم-تنفيذ', 'متطلبات صاحب العمل', 'توزيع مخاطر التصميم', 'ضمان الأداء', 'شروط عقد EPC', 'مخاطر التصميم-والتنفيذ'],
  'content': """## التفاوض في عقود التصميم-والتنفيذ و EPC

### نموذج تفاوض التصميم-والتنفيذ

تنقل عقود التصميم-والتنفيذ (DB) و EPC مسؤولية التصميم للمقاول. هذا يغير مشهد التفاوض جذرياً مقارنة بالتصميم-مناقصة-تنفيذ التقليدي.

### نقاط التفاوض الرئيسية

**1. متطلبات صاحب العمل مقابل تصميم المقاول**
- **الاكتمال:** هل المتطلبات مفصلة بما يكفي لتحديد النتيجة المتوقعة؟
- **مواصفات الأداء مقابل المواصفات الوصفية:** مواصفات الأداء تعطي المقاول حرية تصميم
- **معايير الامتثال:** أي أكواد ومعايرات تنطبق؟
- **ظروف الموقع:** ما معلومات الموقع التي قدمها صاحب العمل؟

**2. مراجعة التصميم والاعتماد**
- فترة مراجعة صاحب العمل: عادة 14-21 يوماً
- الاعتماد الضمني: إذا لم يستجب صاحب العمل خلال الفترة
- نطاق المراجعة: صاحب العمل يراجع للامتثال، لا للصحة التقنية

**3. ضمانات الأداء**
- ضمانات الإخراج: طاقة الإنتاج، الكفاءة
- ضمانات الاستهلاك: استخدام الطاقة
- ضمانات التوفر: نسبة وقت التشغيل
- استراتيجية: تفاوض على نطاق سماحية، حد لغرامات الأداء

**4. السعر المقطوع والمخاطر**
- سعر ثابت ما لم يغير صاحب العمل النطاق
- تصاعد الأسعار: المقاول يتحمل عادة مخاطر تصاعد أسعار المواد
- خفض التكلفة: من يستفيد من حلول تصميم أرخص؟

**5. إدارة الواجهات**
- واجهات ميكانيكية-كهربائية
- واجهات مدنية-MEP
- واجهات خارجية
- المقاول مسؤول عن جميع الواجهات الداخلية

### DB مقابل EPC مقابل LSTK

**التصميم-والتنفيذ (DB):** نقل مخاطر معتدل، صاحب العمل لديه بعض إشراف على التصميم
**EPC:** نقل مخاطر أكبر، صاحب العمل لديه إشراف أدنى
**LSTK:** نقل مخاطر أقصى، سعر ثابت وتاريخ ثابت

### مزالق تفاوض DB/EPC الشائعة

1. متطلبات صاحب عمل غامضة
2. تحقيق موقع غير كافٍ
3. تأخير مراجعة التصميم
4. زحف النطاق
5. نزاعات اختبار الأداء
6. فجوات الواجهة"""}, hero, 17))
nid += 1

# 19. Mediation and Alternative Dispute Resolution
hero = download_hero(3, 'mediation-alternative-dispute-resolution-construction')
articles.append(make_article(nid, 'mediation-alternative-dispute-resolution-construction', 'Negotiation',
 ['negotiation', 'mediation', 'ADR', 'dispute resolution', 'construction disputes'],
 {'title': 'Mediation and Alternative Dispute Resolution in Construction Negotiation',
  'excerpt': 'Expert guide to mediation and ADR in construction — mediation process, facilitation techniques, negotiation in mediation, when to mediate vs arbitrate, and achieving settlement through assisted negotiation.',
  'keywords': ['mediation construction', 'alternative dispute resolution', 'ADR construction', 'construction mediation', 'dispute resolution negotiation', 'facilitated negotiation', 'construction arbitration', 'dispute board', 'mediation settlement', 'construction dispute management'],
  'content': """## Mediation and Alternative Dispute Resolution in Construction Negotiation

### When Direct Negotiation Fails

When direct negotiation reaches impasse, alternative dispute resolution (ADR) methods provide structured processes to achieve settlement without the cost and time of arbitration or litigation. Mediation is the most common and effective ADR method in construction.

### The Mediation Process

**Phase 1: Pre-Mediation**

- **Mediator selection:** Both parties must agree on the mediator. Select someone with construction expertise — not just a legal mediator. Qualifications: construction law experience, technical knowledge, mediation training (IMI or CEDR certified).
- **Mediation agreement:** Defines the process, confidentiality, without-prejudice nature, costs, and mediator authority
- **Position papers:** Each party submits a concise position statement (typically 10-20 pages) to the mediator
- **Document exchange:** Key documents exchanged before mediation to avoid surprise
- **Logistics:** Neutral venue, full-day or multi-day sessions, private caucus rooms for each party

**Phase 2: Joint Session**

- **Opening statement:** Mediator sets ground rules, explains process, establishes neutral tone
- **Party presentations:** Each party presents its position — uninterrupted, typically 30-60 minutes
- **Issue identification:** Mediator helps identify the key issues and common ground
- **Agenda setting:** Mediator proposes an agenda for discussion

**Phase 3: Private Caucuses**

- **Separate meetings:** Mediator meets privately with each party
- **Reality testing:** Mediator challenges each party's assumptions and positions
- **Interest exploration:** Mediator uncovers underlying interests that parties cannot express directly
- **Settlement exploration:** Mediator floats potential settlement options without attributing them to either party
- **Shuttle diplomacy:** Mediator moves between rooms carrying proposals and counter-proposals

**Phase 4: Negotiation and Settlement**

- **Convergence:** Mediator brings parties closer through iterative proposals
- **Package building:** Combine multiple issues into settlement packages
- **Drafting:** Once agreement is reached, draft a binding settlement agreement immediately
- **Signing:** Both parties sign before leaving mediation — do not leave signing for later

### Negotiation Techniques in Mediation

**1. Use the Mediator as a Conduit**

- Send messages through the mediator that you cannot say directly: "Tell them we will not accept less than $500K, but we are willing to drop the disruption claim"
- The mediator can frame proposals more palatably than the originating party
- The mediator can test the other party's reaction without committing your position

**2. Prepare for Reality Testing**

The mediator will challenge your position. Be prepared:
- "What is your best case in arbitration?" — have a realistic answer
- "What will it cost to pursue arbitration?" — have a cost estimate
- "How long will arbitration take?" — have a timeline
- "What is your worst case?" — know your downside risk

**3. Use the Mediation Day Strategically**

- Bring decision-makers with full settlement authority
- Bring technical experts who can answer questions on the spot
- Prepare a draft settlement agreement template
- Plan for fatigue — mediations often settle late in the day or evening
- Have your BATNA clearly defined — know when to walk away

**4. Leverage the Without-Prejudice Nature**

- Everything said in mediation is without prejudice — it cannot be used in subsequent arbitration
- This allows parties to make concessions they would not make in direct negotiation
- Use this safety to explore creative solutions without fear of precedent

### When to Mediate vs Arbitrate

**Mediate when:**
- The dispute is primarily about money, not principle
- Both parties want to preserve the relationship
- The cost of arbitration/litigation exceeds the disputed amount
- A negotiated solution can include non-monetary terms (future work, scope changes)
- Time is critical — mediation can resolve in days vs years for arbitration

**Arbitrate when:**
- One party is unwilling to compromise
- The dispute involves a point of law that needs determination
- One party is using mediation as a delay tactic
- The relationship is already destroyed
- A precedent is needed for future disputes

### Other ADR Methods in Construction

**1. Dispute Adjudication Boards (DAB)**

- Standing DAB: appointed at project start, visits site regularly, familiar with project
- Ad hoc DAB: appointed when dispute arises
- DAB issues binding decisions that parties must comply with pending arbitration
- FIDIC Clause 20 requires DAB before arbitration
- Effective because DAB members understand the project context

**2. Expert Determination**

- Appoint an independent expert to decide technical issues
- Binding decision on technical matters (e.g., whether a material meets specification)
- Faster and cheaper than arbitration for narrow technical disputes
- Parties agree in advance to accept the expert's determination

**3. Early Neutral Evaluation**

- A respected expert gives a non-binding opinion on the merits
- Helps parties assess the strength of their case
- Often leads to settlement when one party learns their case is weak
- Less formal than mediation, cheaper than arbitration

**4. Dispute Review Boards (DRB)**

- Similar to DAB but recommendations are non-binding
- Common in US construction (especially underground/tunnel projects)
- Regular site visits and proactive dispute prevention
- High success rate — most DRB recommendations are accepted

### Maximising Settlement Probability in Mediation

1. **Choose the right mediator:** Construction expertise is more important than legal expertise
2. **Prepare thoroughly:** Position paper, document bundle, BATNA analysis, settlement authority
3. **Be realistic:** Assess your case objectively — overconfidence prevents settlement
4. **Listen:** The other party's presentation may reveal information you did not have
5. **Be patient:** Mediations often take longer than expected — do not leave early
6. **Focus on interests:** What do you really need? Not what you are demanding
7. **Close the deal:** Do not leave mediation without a signed settlement agreement"""},

 {'title': 'الوساطة وحل النزاعات البديل في تفاوض الإنشاءات',
  'excerpt': 'dليل الخبراء للوساطة و ADR في الإنشاءات — عملية الوساطة، تقنيات التيسير، التفاوض في الوساطة، متى تتوسط مقابل التحكيم، وتحقيق التسوية عبر التفاوض بمساعدة.',
  'keywords': ['وساطة الإنشاءات', 'حل النزاعات البديل', 'ADR في الإنشاءات', 'وساطة الإنشاءات', 'تفاوض حل النزاعات', 'تفاوض بمساعدة', 'تحكيم الإنشاءات', 'مجلس النزاعات', 'تسوية الوساطة'],
  'content': """## الوساطة وحل النزاعات البديل في تفاوض الإنشاءات

### متى يفشل التفاوض المباشر

عندما يصل التفاوض المباشر إلى طريق مسدود، توفر طرق حل النزاعات البديلة (ADR) عمليات منظمة لتحقيق التسوية دون تكلفة ووقت التحكيم أو التقاضي. الوساطة هي أكثر طرق ADR شيوعاً وفعالية في الإنشاءات.

### عملية الوساطة

**المرحلة 1: ما قبل الوساطة**
- **اختيار الوسيط:** كلا الطرفين يجب أن يوافقا على الوسيط. اختر شخصاً بخبرة إنشاءات
- **اتفاقية الوساطة:** تحدد العملية، السرية، طبيعة بدون تحفظ، التكاليف
- **أوراق الموقف:** كل طرف يقدم بيان موقف موجز للوسيط
- **تبادل الوثائق:** تبادل الوثائق الرئيسية قبل الوساطة

**المرحلة 2: الجلسة المشتركة**
- **بيان افتتاحي:** الوسيط يضع القواعد ويشرح العملية
- **عروض الأطراف:** كل طرف يقدم موقفه — دون مقاطعة
- **تحديد القضايا:** الوسيط يساعد في تحديد القضايا الرئيسية

**المرحلة 3: الاجتماعات الخاصة**
- **اجتماعات منفصلة:** الوسيط يلتقي بشكل خاص مع كل طرف
- **اختبار الواقع:** الوسيط يتحدى افتراضات ومواقف كل طرف
- **استكشاف المصالح:** الوسيط يكتشف المصالح الأساسية
- **الدبلوماسية المكوكية:** الوسيط يتنقل بين الغرف

**المرحلة 4: التفاوض والتسوية**
- **التقارب:** الوسيط يقرب الأطراف عبر مقترحات تكرارية
- **بناء الحزمة:** اجمع قضايا متعددة في حزم تسوية
- **الصياغة:** بمجرد الاتفاق، صغ اتفاقية تسوية ملزمة فوراً
- **التوقيع:** كلا الطرفين يوقع قبل مغادرة الوساطة

### تقنيات التفاوض في الوساطة

**1. استخدم الوسيط كقناة**
- أرسل رسائل عبر الوسيط لا يمكنك قولها مباشرة
- الوسيط يمكنه تأطير المقترحات بشكل أكثر قبولاً

**2. استعد لاختبار الواقع**
- "ما أفضل حالة في التحكيم؟" — لديك إجابة واقعية
- "ما تكلفة التحكيم؟" — لديك تقدير تكلفة
- "كم سيستغرق التحكيم؟" — لديك جدول زمني

**3. استخدم يوم الوساطة استراتيجياً**
- أحضر صناع قرار بسلطة تسوية كاملة
- أحضر خبراء تقنيين
- أعد قالب اتفاقية تسوية
- خطط للإرهاق — الوساطات غالباً تُتسوى في وقت متأخر

### متى تتوسط مقابل التحكيم

**توسط عندما:**
- النزاع أساساً عن المال، لا المبدأ
- كلا الطرفين يريد الحفاظ على العلاقة
- تكلفة التحكيم تتجاوز المبلغ المتنازع عليه
- الوقت حرج

**تحكّم عندما:**
- طرف غير مستعد للتسوية
- النزاع يتضمن نقطة قانونية تحتاج تحديد
- طرف يستخدم الوساطة كتكتيك تأخير

### طرق ADR أخرى في الإنشاءات

**1. مجالس تحكيم النزاعات (DAB)**
- DAB دائم: يعين عند بدء المشروع، يزور الموقع بانتظام
- يصدر قرارات ملزمة يجب الامتثال لها pending التحكيم
- FIDIC البند 20 يتطلب DAB قبل التحكيم

**2. تحديد الخبير**
- تعيين خبير مستقل لتحديد القضايا التقنية
- قرار ملزم في المسائل التقنية

**3. التقييم المحايد المبكر**
- خبير محترم يعطي رأي غير ملزم في الجدارة
- غالباً يؤدي للتسوية

### تعظيم احتمال التسوية في الوساطة

1. اختر الوسيط المناسب: خبرة الإنشاءات أهم من الخبرة القانونية
2. استعد جيداً: ورقة موقف، حزمة وثائق، تحليل BATNA
3. كن واقعياً: قيم قضتك بموضوعية
4. استمع: عرض الطرف الآخر قد يكشف معلومات لم تكن تملكها
5. كن صبوراً: الوساطات تستغرق أطول من المتوقع
6. ركز على المصالح: ماذا تحتاج فعلاً؟ لا ماذا تطالب
7. أغلق الصفقة: لا تغادر الوساطة بدون اتفاقية تسوية موقعة"""}, hero, 18))
nid += 1

# 20. Negotiation Psychology and Cognitive Biases
hero = download_hero(4, 'negotiation-psychology-cognitive-biases-construction')
articles.append(make_article(nid, 'negotiation-psychology-cognitive-biases-construction', 'Negotiation',
 ['negotiation', 'psychology', 'cognitive biases', 'behavioral economics', 'construction negotiation'],
 {'title': 'Negotiation Psychology and Cognitive Biases in Construction: Thinking About Thinking',
  'excerpt': 'Expert guide to negotiation psychology and cognitive biases in construction — anchoring bias, confirmation bias, overconfidence, loss aversion, framing effects, and debiasing strategies for better negotiation outcomes.',
  'keywords': ['negotiation psychology', 'cognitive biases negotiation', 'anchoring bias', 'confirmation bias', 'overconfidence bias', 'loss aversion negotiation', 'framing effects', 'behavioral economics construction', 'negotiation debiasing', 'construction negotiation psychology'],
  'content': """## Negotiation Psychology and Cognitive Biases in Construction

### The Hidden Forces in Negotiation

Construction negotiations are not purely rational processes. Cognitive biases — systematic errors in thinking — affect every negotiator's decisions. Understanding these biases is essential for expert negotiators who want to make better decisions and influence the other party effectively.

### Key Cognitive Biases in Construction Negotiation

**1. Anchoring Bias**

The first number mentioned tends to anchor the entire negotiation. Even absurdly high or low anchors pull the final outcome toward them.

**In construction:**
- A contractor submits a $2M claim when the realistic value is $800K. The employer counters at $500K. They settle at $1.1M — above the realistic value because the anchor was high.
- A subcontractor quotes $500K for a package. The main contractor's budget was $350K. They settle at $420K — above budget because the anchor was high.

**Debiasing strategy:**
- If the other party anchors first and the anchor is unreasonable, reject it explicitly: "That number is not a credible basis for discussion."
- Make your own counter-anchor with supporting data: "Our analysis shows $800K based on these calculations."
- Use objective criteria to reframe: "Let us look at what the contract and standards say."

**2. Confirmation Bias**

People seek information that confirms their existing beliefs and ignore contradictory evidence.

**In construction:**
- A consultant who believes the contractor is inflating claims will scrutinise every cost item looking for evidence of inflation — while accepting compliant items without question.
- A contractor who believes the employer is unfair will interpret every rejection as further evidence of unfairness — even when rejections are contractually justified.

**Debiasing strategy:**
- Actively seek disconfirming evidence: "What would make my position wrong?"
- Assign a team member to play devil's advocate
- Use independent experts who have no stake in the outcome
- Ask: "If I were the other party, what would I find most convincing about their case?"

**3. Overconfidence Bias**

Negotiators consistently overestimate their ability to achieve favourable outcomes and underestimate the other party's strength.

**In construction:**
- "We will win this arbitration easily" — leading to rejection of reasonable settlement offers
- "Our claim is rock-solid" — leading to insufficient preparation of supporting documentation
- "They will never walk away from this deal" — leading to aggressive positions that cause the other party to walk

**Debiasing strategy:**
- Conduct a pre-mortem: "Assume we lost the negotiation. What went wrong?"
- Estimate outcomes as ranges, not point estimates: "We expect $500K-$700K, not $700K"
- Seek external calibration: ask a colleague with no involvement to assess your case
- Track your past predictions vs actual outcomes — most people are less accurate than they think

**4. Loss Aversion**

People feel losses approximately twice as intensely as equivalent gains. This makes negotiators more protective of what they have than motivated by what they could gain.

**In construction:**
- A contractor will fight harder to avoid a $100K deduction than to earn a $100K bonus
- An employer will resist paying a $200K variation more strongly than they would pursue a $200K cost saving
- This asymmetry can be exploited in framing: "Accepting this settlement avoids a $500K arbitration cost" is more persuasive than "Accepting this settlement saves $500K"

**Debiasing strategy:**
- Reframe losses as gains: instead of "We are conceding $50K", frame as "We are securing $450K of our $500K claim"
- Use loss framing strategically with the other party: "If we do not settle, both parties face $200K in legal costs"
- Be aware of your own loss aversion: are you holding a position because it is right, or because you fear the loss?

**5. Framing Effects**

How information is presented affects decisions, even when the substance is identical.

**In construction:**
- "This variation costs $100K" vs "This variation represents only 0.5% of the $20M contract value" — same cost, different perception
- "We are claiming $1M" vs "We are claiming $1M, which is 15% below the maximum we could claim under the contract" — same amount, different perception
- "The delay was 30 days" vs "The delay was 30 days, but we recovered 10 days through acceleration, net impact 20 days" — different framing of the same event

**Strategic use:**
- Frame your proposals in terms that the other party finds most palatable
- Frame concessions as gains for the other party, not losses for you
- Frame your requests as reasonable by comparing to benchmarks

**6. Sunk Cost Fallacy**

Continuing a negotiation (or dispute) because of resources already invested, even when the expected outcome does not justify continued investment.

**In construction:**
- "We have already spent $150K on legal fees preparing this claim — we cannot settle now"
- "We have been negotiating for 6 months — we cannot walk away empty-handed"
- This leads to throwing good money after bad

**Debiasing strategy:**
- Ask: "If I were starting today with no prior investment, would I continue this negotiation?"
- Consider only future costs and benefits — past costs are sunk regardless of what you do
- Set a budget for dispute resolution costs before starting — stop when the budget is exhausted

**7. Availability Bias**

Judging probability by how easily examples come to mind, not by actual probability.

**In construction:**
- "We won the last two arbitrations, so we will win this one" — ignoring that each case is different
- "I remember a project where the contractor's claim was inflated, so this one probably is too" — generalising from a single example

**Debiasing strategy:**
- Use data, not memory: "In the last 10 projects, our average claim recovery was 65%"
- Seek base rates: "What is the typical outcome for this type of claim in this jurisdiction?"

### Practical Debiasing Framework for Construction Negotiators

1. **Before negotiation:** Identify which biases you are most susceptible to (self-assessment)
2. **During negotiation:** Pause before major decisions and ask "Am I being influenced by a bias?"
3. **After negotiation:** Review your decisions — were they rational? What would you do differently?
4. **Team debiasing:** Assign one team member as the "bias checker" — their role is to challenge decisions that may be bias-driven
5. **Process debiasing:** Use structured decision frameworks (decision trees, expected value calculations) that force rational analysis"""},

 {'title': 'سيكولوجيا التفاوض والتحيزات المعرفية في الإنشاءات: التفكير في التفكير',
  'excerpt': 'دليل الخبراء لسيكولوجيا التفاوض والتحيزات المعرفية في الإنشاءات — تحيز التثبيت، تحيز التأكيد، الثقة المفرطة، النفور من الخسارة، تأثيرات التأطير، واستراتيجيات إزالة التحيز.',
  'keywords': ['سيكولوجيا التفاوض', 'التحيزات المعرفية في التفاوض', 'تحيز التثبيت', 'تحيز التأكيد', 'الثقة المفرطة', 'النفور من الخسارة', 'تأثيرات التأطير', 'الاقتصاد السلوكي في الإنشاءات', 'إزالة تحيز التفاوض'],
  'content': """## سيكولوجيا التفاوض والتحيزات المعرفية في الإنشاءات

### القوى الخفية في التفاوض

مفاوضات الإنشاءات ليست عمليات عقلانية بحتة. التحيزات المعرفية — أخطاء منهجية في التفكير — تؤثر على قرارات كل مفاوض. فهم هذه التحيزات ضروري للمفاوضين الخبراء.

### التحيزات المعرفية الرئيسية في تفاوض الإنشاءات

**1. تحيز التثبيت**

الرقم الأول المذكور يميل لتثبيت المفاوضات بأكملها.

**في الإنشاءات:**
- مقاول يقدم مطالبة بمليوني دولار عندما القيمة الواقعية 800 ألف. صاحب العمل يعارض بـ 500 ألف. يتسوى عند 1.1 مليون — فوق القيمة الواقعية لأن المرساة كانت عالية.

**استراتيجية إزالة التحيز:**
- ارفض المرساة غير المعقولة صراحة
- اصنع مرساة مضادة ببيانات داعمة
- استخدم معايير موضوعية لإعادة التأطير

**2. تحيز التأكيد**

يبحث الناس عن معلومات تؤكد معتقداتهم ويتجاهلون الأدلة المتناقضة.

**في الإنشاءات:**
- استشاري يعتقد أن المقاول يضخم المطالبات سيدقق كل بند تكلفة بحثاً عن أدلة التضخم

**استراتيجية إزالة التحيز:**
- ابحث بنشاط عن أدلة نافية: "ما الذي يجعل موقفي خاطئاً؟"
- عين عضو فريق للعب دور محامي الشيطان

**3. الثقة المفرطة**

يقدر المفاوضون قدرتهم على تحقيق نتائج مواتية بشكل مفرط.

**في الإنشاءات:**
- "سنفوز في هذا التحكيم بسهولة" — مما يؤدي لرفض عروض تسوية معقولة

**استراتيجية إزالة التحيز:**
- أجرِ ما قبل الوفاة: "افترض أننا خسرنا المفاوضات. ما الذي سار بشكل خاطئ؟"
- قدر النتائج كنطاقات، لا تقديرات نقطية

**4. النفور من الخسارة**

يشعر الناس بالخسائر بشكل أقوى تقريباً ضعف المكاسب المكافئة.

**في الإنشاءات:**
- المقاول سيقاتل أكثر لتجنب خصم 100 ألف من السعي لكسب مكافأة 100 ألف

**استراتيجية إزالة التحيز:**
- أعد تأطير الخسائر كمكاسب
- استخدم تأطير الخسارة استراتيجياً مع الطرف الآخر

**5. تأثيرات التأطير**

كيفية تقديم المعلومات تؤثر على القرارات.

**في الإنشاءات:**
- "هذا التغيير يكلف 100 ألف" مقابل "هذا التغيير يمثل 0.5% فقط من قيمة العقد 20 مليون"

**6. مغالطة التكاليف الغارقة**

الاستمرار في التفاوض بسبب الموارد المستثمرة بالفعل.

**في الإنشاءات:**
- "أنفقنا 150 ألف على الرسوم القانونية — لا يمكننا التسوية الآن"

**استراتيجية إزالة التحيز:**
- اسأل: "لو كنت أبدأ اليوم بدون استثمار سابق، هل سأستمر؟"

**7. تحيز التوفر**

الحكم على الاحتمال بمدى سهولة استحضار الأمثلة.

**في الإنشاءات:**
- "فزنا في آخر تحكيمين، لذا سنفوز في هذا"

### إطار عملي لإزالة التحيز

1. **قبل التفاوض:** حدد التحيزات الأكثر تأثيراً عليك
2. **أثناء التفاوض:** توقف قبل القرارات الكبرى واسأل "هل أتأثر بتحيز؟"
3. **بعد التفاوض:** راجع قراراتك — هل كانت عقلانية؟
4. **إزالة تحيز الفريق:** عين عضو كـ "مدقق التحيز"
5. **إزالة تحيز العملية:** استخدم أطر قرار منظمة"""}, hero, 19))
nid += 1

save_articles(articles)
print(f'Batch 4 done. Total articles: {len(articles)}')
