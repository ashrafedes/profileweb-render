import json, sys
sys.path.insert(0, '.')
from _article_utils import load_articles, save_articles

EN_TITLE = "Cyber Security Essentials: A Comprehensive Guide to Threats, Attacks, and Defense"
EN_EXCERPT = "A complete guide to cyber security fundamentals — information assurance, cryptography, attacker techniques, exploitation methods, malicious code, and defense strategies for protecting systems and data."

EN_CONTENT = r"""## Introduction: The Cyber Security Imperative

Every organization today depends on digital systems that are under constant attack. Cyber security is no longer an IT department concern — it is a board-level priority that affects every aspect of business operations, customer trust, and regulatory compliance. The threat landscape evolves continuously as attackers develop new techniques, automate existing ones, and monetize stolen data through sophisticated criminal ecosystems.

Understanding cyber security requires grasping both the attacker's perspective and the defender's toolkit. This guide examines the full spectrum — from information assurance fundamentals and cryptography through attacker techniques, exploitation methods, malicious code, and the defense strategies that security professionals deploy to protect systems.

![Cyber security essentials overview](https://images.pexels.com/photos/5380642/pexels-photo-5380642.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Information Assurance Fundamentals

### The CIA Triad and Beyond

Information assurance rests on five foundational principles that every security professional must understand:

**Confidentiality** ensures that information is accessible only to authorized entities. Breaches of confidentiality include data theft, unauthorized disclosure, and interception of communications. Encryption, access controls, and data classification systems protect confidentiality. When an attacker steals a database of customer records, they have violated confidentiality.

**Integrity** ensures that information has not been altered or destroyed in an unauthorized manner. Integrity violations include tampering with financial records, modifying log files to hide attacks, or injecting malicious code into legitimate software. Hashing, digital signatures, and file integrity monitoring systems protect integrity. When an attacker modifies a web page to serve malware to visitors, they have violated integrity.

**Availability** ensures that information and systems are accessible when needed. Availability attacks include denial-of-service floods, ransomware that encrypts data, and infrastructure failures. Redundancy, backup systems, and DDoS mitigation services protect availability. When a botnet floods a website with traffic until it crashes, they have attacked availability.

**Authentication** verifies the identity of a user, system, or process. Passwords, biometrics, smart cards, and multi-factor authentication systems provide authentication. Without authentication, any entity could claim any identity, making authorization meaningless.

**Authorization** determines what an authenticated entity is allowed to do. Access control lists, role-based access control, and attribute-based access control systems implement authorization. The principle of least privilege — granting only the permissions needed for a task — is the cornerstone of secure authorization.

**Non-repudiation** ensures that an action cannot be denied by the entity that performed it. Digital signatures and audit logs provide non-repudiation. In financial transactions, non-repudiation prevents a party from claiming they did not authorize a transfer.

![Information assurance CIA triad](https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Cryptography: The Foundation of Secure Communication

### Symmetric Encryption

Symmetric encryption uses a single key for both encryption and decryption. The sender encrypts the plaintext with the key, producing ciphertext; the receiver decrypts the ciphertext with the same key, recovering the plaintext. The security of symmetric encryption depends entirely on keeping the key secret.

Stream ciphers encrypt data one bit or byte at a time, making them suitable for real-time communications. Block ciphers encrypt data in fixed-size blocks (typically 128 bits), providing stronger security for stored data. The Advanced Encryption Standard (AES) is the dominant block cipher, used by governments, financial institutions, and security products worldwide. AES operates with key sizes of 128, 192, or 256 bits, with larger keys providing greater security against brute-force attacks.

The fundamental challenge in symmetric encryption is key distribution — how do two parties securely share a secret key over an insecure channel? This problem led to the development of public key cryptography.

### Public Key Encryption

Public key cryptography solves the key distribution problem by using two mathematically related keys: a public key that can be freely shared and a private key that must be kept secret. Data encrypted with the public key can only be decrypted with the private key, and vice versa.

The RSA algorithm, based on the mathematical difficulty of factoring large prime numbers, remains the most widely deployed public key system. Elliptic Curve Cryptography (ECC) provides equivalent security with smaller keys, making it preferred for mobile and IoT devices where computational resources are limited.

Public key cryptography enables two critical security functions. First, confidential communication: Alice encrypts a message with Bob's public key; only Bob can decrypt it with his private key. Second, digital signatures: Alice signs a message with her private key; anyone can verify the signature with her public key, proving the message came from Alice and has not been modified.

### Hash Functions

Cryptographic hash functions take input of any size and produce a fixed-size output called a hash or digest. A secure hash function has three properties: it is one-way (the input cannot be recovered from the hash), it is collision-resistant (two different inputs should not produce the same hash), and it is deterministic (the same input always produces the same hash).

Hash functions protect integrity — comparing the hash of a file before and after transmission detects any modification. They also protect stored passwords — instead of storing a password in plaintext, a system stores its hash; when the user logs in, the system hashes the entered password and compares it to the stored hash. SHA-256 and SHA-3 are the current standard hash functions, replacing the compromised MD5 and SHA-1.

![Cryptography and encryption methods](https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Network Security Infrastructure

### Firewalls

Firewalls control traffic between network segments based on rules. Three generations of firewall technology have evolved:

**Packet-filtering firewalls** examine individual packets against rules based on source IP, destination IP, source port, destination port, and protocol. They are fast but limited — they cannot inspect packet content or track connection state. A packet filter might allow all traffic to port 80 (HTTP) without distinguishing a legitimate web request from an attack payload.

**Stateful firewalls** track the state of network connections, allowing return traffic for established connections while blocking unsolicited traffic. This provides better security than packet filtering with minimal performance overhead. Stateful firewalls understand that a response to an outbound request is different from an unsolicited inbound connection.

**Application gateway firewalls** (next-generation firewalls) inspect the content of traffic at the application layer, enabling them to block specific attacks such as SQL injection or cross-site scripting. They can identify applications (not just ports), enforce application-specific rules, and integrate with threat intelligence feeds. Modern enterprise firewalls combine all three approaches.

### The Domain Name System and Security

DNS translates human-readable domain names into IP addresses. This critical infrastructure is also a frequent attack target. DNS cache poisoning injects false entries into DNS resolver caches, redirecting users to malicious sites. DNS amplification attacks use DNS servers to magnify denial-of-service traffic, overwhelming targets with responses they never requested.

DNSSEC adds cryptographic signatures to DNS responses, allowing resolvers to verify that responses are authentic and unmodified. However, DNSSEC adoption remains incomplete, leaving many domains vulnerable to manipulation.

### Virtualization Security

Virtualization consolidates multiple virtual machines onto single physical hardware, introducing new security considerations. Virtual machine escape — where an attacker breaks out of a VM to access the host or other VMs — is the most severe virtualization risk. Hypervisor vulnerabilities, VM-to-VM attacks, and insecure VM migration all require specific security controls.

![Network security infrastructure](https://images.pexels.com/photos/1148820/pexels-photo-1148820.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Attacker Techniques and Motivations

### How Attackers Cover Their Tracks

Sophisticated attackers use proxy chains to hide their origin, routing traffic through multiple compromised systems across different jurisdictions. Each hop obscures the source, making attribution difficult. Attackers also use tunneling techniques — encapsulating traffic within legitimate protocols like HTTP, DNS, or ICMP — to bypass firewalls that allow these protocols.

Anti-forensics techniques include clearing log files, modifying timestamps, encrypting stolen data, and using memory-only malware that leaves no disk trace. The goal is to make incident response and forensic analysis as difficult as possible.

### Fraud Techniques

**Phishing** remains the most effective initial access method. Attackers send emails impersonating trusted entities, tricking victims into entering credentials on fake websites. **Smishing** (SMS phishing) and **vishing** (voice phishing) extend this technique to mobile and voice channels. Mobile devices are particularly vulnerable — smaller screens make it harder to spot fake URLs, and users tend to trust SMS messages more than emails.

**Rogue antivirus** scams trick users into believing their computer is infected, then charge them for fake security software. The rogue AV displays alarming pop-ups, performs fake scans, and pressures victims into paying for "protection" that is itself the malware.

**Click fraud** automates advertisement clicks to generate fraudulent revenue or deplete competitors' advertising budgets. Botnets generate clicks from thousands of infected machines, making the traffic appear legitimate.

### Threat Infrastructure: Botnets and Fast-Flux

**Botnets** are networks of compromised computers controlled by a botmaster through command-and-control (C&C) servers. Botnets are the workhorses of cybercrime — they send spam, launch DDoS attacks, steal credentials, and distribute malware. Centralized botnets use a single C&C server (easy to shut down), while decentralized botnets use peer-to-peer communication (resilient but complex).

**Fast-flux** rapidly cycles the IP addresses associated with a domain name, making server takedowns difficult. When law enforcement shuts down one IP, the domain immediately resolves to another. **Domain generation algorithms** (DGA) take this further — bots generate thousands of potential domain names daily, and the botmaster registers only the ones the bots will check. This makes domain takedowns nearly impossible because the active domain changes constantly.

![Attacker techniques and botnets](https://images.pexels.com/photos/2151/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1200)

---

## Exploitation Techniques

### Buffer Overflows

Buffer overflow vulnerabilities occur when a program writes more data to a buffer than it can hold, overwriting adjacent memory. **Stack-based buffer overflows** overwrite the return address on the stack, causing the program to execute attacker-controlled code. Attackers craft input that fills the buffer, overwrites the return address with a pointer to their shellcode, and the program jumps to that code when the function returns.

Protections against buffer overflows include stack canaries (values placed on the stack that detect overwrites), data execution prevention (marking stack memory as non-executable), and address space layout randomization (randomizing memory locations so attackers cannot predict where shellcode will be).

### SQL Injection

SQL injection exploits applications that construct database queries from user input without proper sanitization. An attacker enters SQL commands into input fields, tricking the application into executing unauthorized queries. A simple attack might enter `' OR '1'='1` in a login field, causing the query to return all records and bypass authentication.

Parameterized queries prevent SQL injection by separating SQL code from user input. The database engine treats user input strictly as data, never as executable SQL. Input validation and web application firewalls provide additional layers of defense.

### Cross-Site Scripting (XSS)

XSS injects malicious JavaScript into web pages viewed by other users. **Reflected XSS** embeds the script in a URL that the victim clicks. **Stored XSS** persists the script in the application's database, executing it for every user who views the affected page. **DOM-based XSS** manipulates the page's Document Object Model client-side.

XSS enables attackers to steal session cookies, redirect users to malicious sites, deface web pages, and perform actions on behalf of the victim. Defense requires output encoding (converting special characters to HTML entities), input validation, and Content Security Policy headers that restrict script sources.

### Social Engineering

Social engineering exploits human psychology rather than technical vulnerabilities. Attackers impersonate authority figures, create urgency, appeal to helpfulness, or exploit trust. Pretexting creates a fabricated scenario — an attacker calls claiming to be from IT support, needing the victim's password to "fix a problem."

The human element makes social engineering difficult to defend against with technology alone. Security awareness training, verification procedures, and a culture of healthy skepticism are essential controls.

![Exploitation techniques in cyber security](https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Malicious Code

### Worms and Viruses

**Worms** self-replicate across networks without user interaction, exploiting vulnerabilities to spread from system to system. Conficker, Stuxnet, and WannaCry demonstrate the destructive potential of network worms. Modern worms often combine multiple spreading mechanisms and use sophisticated evasion techniques.

**Viruses** attach themselves to legitimate programs and execute when the host program runs. Unlike worms, viruses require user action to spread. Polymorphic viruses mutate their code with each infection to evade signature-based detection. Metamorphic viruses rewrite their code entirely between infections.

### Rootkits

Rootkits maintain persistent, privileged access while hiding their presence. **User-mode rootkits** modify system binaries and APIs in user space, hiding processes, files, and network connections. They are easier to detect because they operate at the same privilege level as security tools.

**Kernel-mode rootkits** operate at the operating system kernel level, giving them deeper control and better stealth. They can intercept system calls, modify kernel data structures, and subvert security software. Kernel rootkits are extremely difficult to detect from within the compromised system — memory forensics and external inspection are often required.

### Spyware and Information Theft

Spyware silently collects user activity — keystrokes, web browsing, credentials, and financial data. **Form grabbing** intercepts web form data before it is encrypted by SSL, capturing passwords and credit card numbers. **Man-in-the-middle attacks** intercept and potentially modify communications between two parties who believe they are communicating directly.

**DLL injection** forces a legitimate process to load malicious code, allowing attackers to execute within the context of trusted applications. This technique bypasses security software that trusts certain processes.

![Malicious code types and behaviors](https://images.pexels.com/photos/1809632/pexels-photo-1809632.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Defense and Analysis Techniques

### Memory Forensics

Memory forensics examines the volatile contents of a system's RAM to find evidence of compromise that disk forensics cannot detect. Memory-only malware, rootkits hiding processes, and injected code all leave traces in memory that disappear when the system powers off.

Tools like Volatility analyze memory dumps to identify hidden processes, network connections, injected code, and rootkit hooks. Memory forensics is particularly valuable for investigating sophisticated attacks where the malware never writes to disk.

### Antivirus and Detection

Traditional antivirus software uses signature-based detection — identifying malware by comparing files to a database of known threats. This approach is increasingly insufficient as malware authors create thousands of new variants daily. Heuristic detection identifies suspicious behavior patterns, while behavioral analysis monitors what programs do rather than what they look like.

Modern endpoint detection and response (EDR) platforms combine multiple detection methods with continuous monitoring, enabling rapid identification and response to both known and novel threats.

### Intrusion Detection and Prevention

**Intrusion Detection Systems (IDS)** monitor network or system activity for malicious patterns. Network-based IDS inspects traffic for attack signatures; host-based IDS monitors system logs and file integrity. **Intrusion Prevention Systems (IPS)** go further by actively blocking detected attacks.

The challenge with IDS/IPS is balancing detection accuracy with false positive rates. Signature-based systems miss novel attacks; anomaly-based systems generate false positives when user behavior changes legitimately. Modern systems use machine learning to improve accuracy over time.

![Defense and analysis techniques](https://images.pexels.com/photos/1089440/pexels-photo-1089440.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## Building a Defense-in-Depth Strategy

No single security control is sufficient. Defense-in-depth layers multiple controls so that if one fails, others provide protection:

- **Perimeter defense:** Firewalls, intrusion prevention, DDoS mitigation
- **Network segmentation:** Isolating critical systems from general networks
- **Endpoint protection:** EDR, application whitelisting, patch management
- **Identity and access management:** Multi-factor authentication, least privilege, privileged access management
- **Data protection:** Encryption at rest and in transit, data loss prevention
- **Security monitoring:** SIEM, threat hunting, incident response
- **Security awareness:** Training, phishing simulations, reporting culture
- **Backup and recovery:** Regular backups, offline copies, recovery testing

Each layer addresses different threats and attack vectors. An attacker who breaches the firewall still faces endpoint protection. An attacker who compromises an endpoint still faces network segmentation limiting lateral movement. An attacker who steals credentials still faces multi-factor authentication.

---

## FAQ

### What is the CIA triad in cyber security?

The CIA triad — Confidentiality, Integrity, and Availability — is the foundational model for information security. Confidentiality prevents unauthorized access, integrity prevents unauthorized modification, and availability ensures systems are accessible when needed. Together with authentication, authorization, and non-repudiation, these principles form the basis of information assurance.

### What is the difference between symmetric and public key encryption?

Symmetric encryption uses one key for both encryption and decryption, requiring secure key distribution. Public key encryption uses two keys — a public key for encryption and a private key for decryption — solving the key distribution problem but requiring more computational resources. Most systems use both: public key for key exchange, symmetric for bulk data encryption.

### How do buffer overflow attacks work?

Buffer overflow attacks send more data to a program's buffer than it can hold, overwriting adjacent memory including the return address. When the program returns from the function, it jumps to the attacker's code instead of the legitimate return point. Protections include stack canaries, data execution prevention, and address space layout randomization.

### What is a botnet and how does it work?

A botnet is a network of compromised computers controlled by an attacker through command-and-control servers. Botnets distribute spam, launch DDoS attacks, steal data, and spread malware. They use fast-flux and domain generation algorithms to resist takedown efforts. Defense requires endpoint protection, network monitoring, and coordinated law enforcement action.

### What is defense-in-depth?

Defense-in-depth is a security strategy that layers multiple controls so that failure of any single control does not compromise the system. Layers include perimeter defense, network segmentation, endpoint protection, identity management, data encryption, security monitoring, awareness training, and backup recovery. Each layer addresses different threats and provides redundancy.

---

## Conclusion

Cyber security is a continuous arms race between attackers who develop new techniques and defenders who build new protections. Understanding the fundamentals — information assurance principles, cryptographic building blocks, network security infrastructure, attacker methodologies, exploitation techniques, malicious code, and defense strategies — provides the knowledge base that security professionals need to protect their organizations.

The most effective security programs combine technical controls with human awareness and organizational processes. Technology alone cannot prevent phishing; awareness training fills that gap. Processes alone cannot detect zero-day attacks; behavioral monitoring fills that gap. The defense-in-depth principle — layering controls so that no single failure is catastrophic — remains the most reliable approach in an environment where no single control can be guaranteed to work.
"""

AR_TITLE = "أساسيات الأمن السيبراني: دليل شامل للتهديدات والهجمات والدفاع"
AR_EXCERPT = "دليل كامل لأساسيات الأمن السيبراني — ضمان المعلومات والتشفير وتقنيات المهاجمين وأساليب الاستغلال والبرمجيات الخبيثة واستراتيجيات الدفاع لحماية الأنظمة والبيانات."

AR_CONTENT = r"""## مقدمة: ضرورة الأمن السيبراني

كل منظمة اليوم تعتمد على أنظمة رقمية تتعرض لهجمات مستمرة. الأمن السيبراني لم يعد شأناً لقسم تكنولوجيا المعلومات — إنه أولوية على مستوى مجلس الإدارة تؤثر على كل جانب من جوانب العمليات التجارية وثقة العملاء والامتثال التنظيمي.

![نظرة عامة على أساسيات الأمن السيبراني](https://images.pexels.com/photos/5380642/pexels-photo-5380642.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## أساسيات ضمان المعلومات

### ثلاثية CIA وما بعدها

**السرية:** ضمان وصول المعلومات فقط للكيانات المخول لها.
**السلامة:** ضمان عدم تعديل المعلومات أو تدميرها بطريقة غير مصرح بها.
**التوافر:** ضمان إمكانية الوصول للمعلومات والأنظمة عند الحاجة.
**المصادقة:** التحقق من هوية المستخدم أو النظام أو العملية.
**التفويض:** تحديد ما يُسمح للكيان المصادق عليه بفعله.
**عدم الإنكار:** ضمان عدم قدرة الكيان على إنكار إجراء قام به.

![ثلاثية CIA لضمان المعلومات](https://images.pexels.com/photos/60504/security-protection-anti-virus-software-60504.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## التشفير: أساس الاتصال الآمن

### التشفير المتماثل
يستخدم مفتاحاً واحداً للتشفير وفك التشفير. معيار AES هو التشفير المتماثل المهيمن.

### التشفير بالمفتاح العام
يستخدم مفتاحين — عام للتشفير وخاص لفك التشفير. خوارزمية RSA هي الأكثر انتشاراً.

### دوال التجزئة
تأخذ مدخلات بأي حجم وتنتج مخرجات بحجم ثابت. SHA-256 و SHA-3 هي المعايير الحالية.

![التشفير وطرق التشفير](https://images.pexels.com/photos/270700/pexels-photo-270700.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## البنية التحتية لأمن الشبكات

### جدران الحماية
ثلاثة أجيال: تصفية الحزم، الحالة، بوابة التطبيقات.

### نظام أسماء النطاقات (DNS) والأمن
DNSSEC يضيف تواقيع تشفيرية لاستجابات DNS.

### أمن المحاكاة الافتراضية
خطر هروب الآلة الافتراضية والاختراق من VM إلى VM.

![البنية التحتية لأمن الشبكات](https://images.pexels.com/photos/1148820/pexels-photo-1148820.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## تقنيات المهاجمين ودوافعهم

### كيف يخفي المهاجمون آثارهم
سلاسل الوكلاء، تقنيات النفق، مكافحة الطب الشرعي.

### تقنيات الاحتيال
التصيد الإلكتروني، التصيد عبر SMS، التصيد الصوتي، برامج مكافحة الفيروسات المزيفة، احتيال النقرات.

### البنية التحتية للتهديدات: البوتنت والتدفق السريع
البوتنت شبكة من أجهزة مخترقة تتحكم بها خوادم القيادة والتحكم. التدفق السريع يبدل عناوين IP بسرعة.

![تقنيات المهاجمين والبوتنت](https://images.pexels.com/photos/2151/pexels-photo.jpg?auto=compress&cs=tinysrgb&w=1200)

---

## تقنيات الاستغلال

### فيضان المخزن المؤقت
كتابة بيانات أكثر مما يحتمله المخزن، الكتابة فوق عنوان العودة لتنفيذ كود المهاجم.

### حقن SQL
استغلال التطبيقات التي تبني استعلامات قاعدة البيانات من مدخلات المستخدم دون تعقيم مناسب.

### البرمجة عبر المواقع (XSS)
حقن JavaScript خبيث في صفحات الويب. ثلاثة أنواع: منعكس، مخزن، قائم على DOM.

### الهندسة الاجتماعية
استغلال علم النفس البشري بدلاً من الثغرات التقنية.

![تقنيات الاستغلال في الأمن السيبراني](https://images.pexels.com/photos/1181467/pexels-photo-1181467.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## البرمجيات الخبيثة

### الديدان والفيروسات
الديدان تتكرر ذاتياً عبر الشبكات. الفيروسات ترفق نفسها بالبرامج الشرعية.

### الروت كيت
روت كيت وضع المستخدم يعدل واجهات برمجة التطبيقات. روت كيت وضع النواة يعمل على مستوى النواة.

### برامج التجسس وسرقة المعلومات
التقاط النماذج، هجمات الرجل في الوسط، حقن DLL.

![أنواع البرمجيات الخبيثة وسلوكها](https://images.pexels.com/photos/1809632/pexels-photo-1809632.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## تقنيات الدفاع والتحليل

### الطب الشرعي للذاكرة
فحص محتويات RAM المتطايرة للعثور على أدلة الاختراق.

### مكافحة الفيروسات والكشف
الكشف القائم على التوقيع، الكشف الاستدلالي، التحليل السلوكي.

### كشف ومنع التسلل
أنظمة كشف التسلل تراقب النشاط. أنظمة منع التسلل تحظر الهجمات بنشاط.

![تقنيات الدفاع والتحليل](https://images.pexels.com/photos/1089440/pexels-photo-1089440.jpeg?auto=compress&cs=tinysrgb&w=1200)

---

## بناء استراتيجية الدفاع متعدد الطبقات

لا يوجد ضمان أمني واحد كافٍ. الدفاع متعدد الطبقات يضع ضوابط متعددة:
- الدفاع المحيطي: جدران الحماية، منع التسلل، تخفيف DDoS
- تقسيم الشبكة: عزل الأنظمة الحرجة
- حماية النقاط الطرفية: EDR، قائمة التطبيقات المسموح بها
- إدارة الهوية والوصول: مصادقة متعددة العوامل، أقل امتياز
- حماية البيانات: التشفير، منع فقدان البيانات
- المراقبة الأمنية: SIEM، صيد التهديدات
- التوعية الأمنية: التدريب، محاكاة التصيد
- النسخ الاحتياطي والاسترداد: نسخ احتياطية منتظمة

---

## الأسئلة الشائعة

### ما هي ثلاثية CIA في الأمن السيبراني؟
السرية والسلامة والتوافر — النموذج الأساسي لأمن المعلومات.

### ما الفرق بين التشفير المتماثل والتشفير بالمفتاح العام؟
المتماثل يستخدم مفتاحاً واحداً. بالمفتاح العام يستخدم مفتاحين — عام وخاص.

### كيف تعمل هجمات فيضان المخزن المؤقت؟
ترسل بيانات أكثر مما يحتمله المخزن، الكتابة فوق عنوان العودة لتنفيذ كود المهاجم.

### ما هو البوتنت وكيف يعمل؟
شبكة من أجهزة مخترقة تتحكم بها خوادم القيادة والتحكم لتوزيع الرسائل المزعجة وإطلاق هجمات DDoS.

### ما هو الدفاع متعدد الطبقات؟
استراتيجية أمنية تضع ضوابط متعددة بحيث لا يؤدي فشل أي ضمان واحد إلى اختراق النظام.

---

## الخلاصة

الأمن السيبراني سباق تسلح مستمر بين المهاجمين الذين يطورون تقنيات جديدة والمدافعين الذين يبنون حماية جديدة. فهم الأساسيات — مبادئ ضمان المعلومات، اللبنات التشفيرية، البنية التحتية لأمن الشبكات، منهجيات المهاجمين، تقنيات الاستغلال، البرمجيات الخبيثة، واستراتيجيات الدفاع — يوفر قاعدة المعرفة التي يحتاجها محترفو الأمن لحماية منظماتهم.

أكثر برامج الأمن فعالية تجمع بين الضوابط التقنية والوعي البشري والعمليات التنظيمية. مبدأ الدفاع متعدد الطبقات — وضع ضوابط متعددة بحيث لا يكون فشل أي ضمان واحداً كارثياً — يبقى النهج الأكثر موثوقية.
"""

article = {
    'id': 149,
    'slug': 'cyber-security-essentials-guide',
    'category': 'Cyber Security',
    'author': 'Ashraf Ibrahim El Desoky',
    'heroImage': '/assets/images/articles/cyber-security-essentials-hero.webp',
    'publishDate': '2026-07-31',
    'updatedDate': '2026-07-31',
    'readingTime': 22,
    'featured': False,
    'draft': False,
    'tags': ['Cyber Security', 'Information Assurance', 'Cryptography', 'Network Security', 'Malware', 'Penetration Testing', 'Firewalls', 'Botnets', 'Defense in Depth'],
    'en': {
        'title': EN_TITLE,
        'excerpt': EN_EXCERPT,
        'content': EN_CONTENT,
        'metaTitle': EN_TITLE + ' – Ashraf El Desoky, PMP®',
        'metaDescription': EN_EXCERPT,
        'keywords': ['cyber security', 'information assurance', 'CIA triad', 'cryptography', 'symmetric encryption', 'public key encryption', 'firewalls', 'DNS security', 'buffer overflow', 'SQL injection', 'XSS', 'social engineering', 'botnets', 'rootkits', 'malware', 'defense in depth', 'memory forensics', 'intrusion detection']
    },
    'ar': {
        'title': AR_TITLE,
        'excerpt': AR_EXCERPT,
        'content': AR_CONTENT,
        'metaTitle': AR_TITLE + ' – أشرف الدسوقي, PMP®',
        'metaDescription': AR_EXCERPT,
        'keywords': ['الأمن السيبراني', 'ضمان المعلومات', 'ثلاثية CIA', 'التشفير', 'التشفير المتماثل', 'التشفير بالمفتاح العام', 'جدران الحماية', 'أمن DNS', 'فيضان المخزن المؤقت', 'حقن SQL', 'XSS', 'الهندسة الاجتماعية', 'البوتنت', 'الروت كيت', 'البرمجيات الخبيثة', 'الدفاع متعدد الطبقات', 'الطب الشرعي للذاكرة', 'كشف التسلل']
    }
}

articles = load_articles()
articles.append(article)
save_articles(articles)
print('Article added (ID: 149, slug: cyber-security-essentials-guide)')
print('Total articles now:', len(articles))
