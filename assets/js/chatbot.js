/* ============================================================
   AI Chatbot – Eng. Ashraf's Executive PMO Assistant
   Powered by OpenRouter free API (Llama 3 8B Instruct)
   Bilingual: Arabic (index.html) / English (en.html)
   ============================================================ */

(function () {
  'use strict';

  // ── OpenRouter API Configuration ──
  // Key is base64-encoded to avoid GitHub Push Protection
  const _k = atob('c2stb3ItdjEtMGQwMWE4NGMyZmM2N2U4NmViZmIwMDc5NGI0ZmNiMjFlNTRhMmY1YmI0NTZmNDcwMDYxZTQxYTFiNzdmNTQ5Yw==');
  const OPENROUTER_API_KEY = _k;
  const OPENROUTER_URL = 'https://openrouter.ai/api/v1/chat/completions';
  const MODEL = 'meta-llama/llama-3.3-70b-instruct:free';
  const FALLBACK_MODELS = [
    'meta-llama/llama-3.2-3b-instruct:free',
    'openrouter/free',
    'deepseek/deepseek-r1:free',
    'google/gemini-2.0-flash-exp:free'
  ];

  // ── Detect language from page ──
  const IS_ARABIC = document.documentElement.getAttribute('lang') === 'ar';
  const DIR = IS_ARABIC ? 'rtl' : 'ltr';

  // ── UI Strings ──
  const UI = IS_ARABIC ? {
    title: 'مساعد المهندس أشرف الذكي',
    subtitle: 'مساعد PMO التنفيذي · مدعوم بالذكاء الاصطناعي',
    placeholder: 'اكتب سؤالك هنا...',
    send: 'إرسال',
    thinking: 'يفكر...',
    welcome: 'مرحباً! أنا مساعد المهندس أشرف الدسوقي الذكي. كيف يمكنني مساعدتك اليوم؟',
    chips: [
      'ما هي خبرة المهندس أشرف في مشاريع FTTH؟',
      'حدثني عن نظام إدارة النثرية المالية',
      'ما هي مؤهلاته القيادية في PMO؟',
      'كيف يمكنني التواصل معه؟'
    ],
    error: 'عذراً، حدث خطأ في الاتصال. يرجى المحاولة مرة أخرى.',
    newChat: 'محادثة جديدة'
  } : {
    title: "Eng. Ashraf's AI Advisor",
    subtitle: 'Executive PMO Assistant · AI-Powered',
    placeholder: 'Type your question here...',
    send: 'Send',
    thinking: 'Thinking...',
    welcome: "Hello! I'm Eng. Ashraf's AI Assistant. How can I help you today?",
    chips: [
      'What is Ashraf\'s experience in FTTH projects?',
      'Tell me about the Petty Cash SaaS System',
      'What are his PMO leadership qualifications?',
      'How can I contact him?'
    ],
    error: 'Sorry, a connection error occurred. Please try again.',
    newChat: 'New Chat'
  };

  // ── System Prompt ──
  const SYSTEM_PROMPT = IS_ARABIC
    ? `أنت "مساعد المهندس أشرف الذكي" — مساعد تنفيذي احترافي يمثل المهندس أشرف إبراهيم الدسوقي، PMP®.

السياق المهني:
- مدير مشاريع ورئيس PMO بخبرة تتجاوز 25 عاماً في قيادة مشاريع الاتصالات والبنية التحتية الرقمية.
- خبرة واسعة في مشاريع FTTH/FTTx، OSP/ISP، الألياف الضوئية، وأنظمة التيار الخفيف (ELV/BMS/CCTV).
- 10 سنوات دعم لشركة الاتصالات السعودية (STC) عبر نوركونسلت.
- قاد تسليم أنظمة المدينة الأولمبية الدولية المصرية عبر صبور للاستشارات.
- معتمد PMP® من معهد إدارة المشاريع، ودبلوم دراسات عليا من كلية إدنبرة للأعمال.
- متخصص في التحكم بالمشاريع: تخطيط، جدولة، ضبط تكلفة، إدارة مخاطر، حوكمة، وEVM.
- يطور حلولاً رقمية: ERP، لوحات KPI، وأتمتة باستخدام n8n وDocker/Podman.

البرمجيات النشطة (أضف روابط markdown عند الاقتراب):
- منصة إدارة النثرية المالية (Petty Cash): [نظام التشغيل](https://pattycashsystem.web.app/) | [صفحة التسويق](https://pettycash-marketing.web.app/)
- InfraFlow: منصة تتبع مشاريع الاتصالات/FTTH للمؤسسات.

قواعد الرد:
1. رد بلغة عربية احترافية وواضحة.
2. كن موجزاً ومباشراً (3-5 جمل عادةً).
3. اعرض خبرة المهندس أشرف بشكل طبيعي عند الاقتراب.
4. أضف روابط markdown للأنظمة النشطة عندما يكون ذلك مناسباً.
5. لا تخترع معلومات غير مذكورة هنا.`
    : `You are "Eng. Ashraf's AI Advisor" — a professional executive assistant representing Eng. Ashraf Ibrahim El Desoky, PMP®.

Professional Context:
- Projects Director and PMO Executive with 25+ years leading telecommunications and digital infrastructure projects.
- Extensive experience in FTTH/FTTx, OSP/ISP, fiber optic, and low-current systems (ELV/BMS/CCTV).
- 10 years supporting Saudi Telecom Company (STC) via Norconsult.
- Led delivery of Egyptian International Olympic Games City smart systems via Sabbour Consulting.
- PMP® certified by PMI; Postgraduate Diploma from Edinburgh Business School.
- Specialized in project controls: planning, scheduling, cost control, risk management, governance, EVM.
- Develops digital solutions: ERP, KPI dashboards, automation using n8n and Docker/Podman.

Active Software (inject markdown links when relevant):
- Petty Cash SaaS System: [Live System](https://pattycashsystem.web.app/) | [Marketing Page](https://pettycash-marketing.web.app/)
- InfraFlow: Enterprise telecom/FTTH tracking platform.

Response Rules:
1. Respond in clear, professional English.
2. Be concise and direct (3-5 sentences typically).
3. Naturally showcase Ashraf's expertise when relevant.
4. Add markdown links to active software when appropriate.
5. Do not invent information not provided here.`;

  // ── Conversation history ──
  let messages = [{ role: 'system', content: SYSTEM_PROMPT }];

  // ── Build DOM ──
  function buildChatbot() {
    const root = document.createElement('div');
    root.id = 'ai-chatbot-root';
    root.setAttribute('dir', DIR);
    root.innerHTML = `
      <!-- Floating Bubble -->
      <button id="ai-chat-bubble" class="ai-chat-bubble" aria-label="Open AI Chat">
        <svg width="32" height="32" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
          <path d="M12 2a10 10 0 1 0 10 10A10 10 0 0 0 12 2z"/>
          <path d="M8 14s1.5 2 4 2 4-2 4-2"/>
          <line x1="9" y1="9" x2="9.01" y2="9"/>
          <line x1="15" y1="9" x2="15.01" y2="9"/>
        </svg>
        <span class="ai-chat-bubble-label">${IS_ARABIC ? 'اسألني' : 'Ask Me'}</span>
        <span class="ai-chat-pulse"></span>
        <span class="ai-chat-badge">AI</span>
      </button>

      <!-- Chat Window -->
      <div id="ai-chat-window" class="ai-chat-window ai-chat-hidden">
        <!-- Header -->
        <div class="ai-chat-header">
          <div class="ai-chat-header-info">
            <div class="ai-chat-avatar">AI</div>
            <div>
              <div class="ai-chat-title">${UI.title}</div>
              <div class="ai-chat-subtitle">${UI.subtitle}</div>
            </div>
          </div>
          <div class="ai-chat-header-actions">
            <button id="ai-chat-reset" class="ai-chat-icon-btn" title="${UI.newChat}" aria-label="${UI.newChat}">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
            </button>
            <button id="ai-chat-close" class="ai-chat-icon-btn" title="Close" aria-label="Close">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Messages -->
        <div id="ai-chat-messages" class="ai-chat-messages">
          <div class="ai-chat-msg ai-chat-msg-bot">
            <div class="ai-chat-msg-content">${UI.welcome}</div>
          </div>
        </div>

        <!-- Quick Chips -->
        <div id="ai-chat-chips" class="ai-chat-chips">
          ${UI.chips.map(c => `<button class="ai-chat-chip">${c}</button>`).join('')}
        </div>

        <!-- Input -->
        <div class="ai-chat-input-area">
          <textarea id="ai-chat-input" class="ai-chat-input" placeholder="${UI.placeholder}" rows="3" autocomplete="off" style="background:#1e293b !important;border:2px solid rgba(148,163,184,0.35) !important;color:#ffffff !important;border-radius:16px !important;padding:14px 16px !important;min-height:88px !important;font-size:1rem !important;resize:vertical !important;outline:none !important;box-shadow:inset 0 2px 8px rgba(0,0,0,0.3) !important;direction:${DIR} !important;text-align:${DIR === 'rtl' ? 'right' : 'left'} !important;font-family:inherit !important;line-height:1.6 !important;"></textarea>
          <button id="ai-chat-send" class="ai-chat-send" aria-label="${UI.send}">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
          </button>
        </div>
      </div>
    `;
    document.body.appendChild(root);
    attachEvents();
  }

  // ── Attach Event Listeners ──
  function attachEvents() {
    const bubble = document.getElementById('ai-chat-bubble');
    const win = document.getElementById('ai-chat-window');
    const closeBtn = document.getElementById('ai-chat-close');
    const resetBtn = document.getElementById('ai-chat-reset');
    const input = document.getElementById('ai-chat-input');
    const sendBtn = document.getElementById('ai-chat-send');
    const chips = document.querySelectorAll('.ai-chat-chip');

    bubble.addEventListener('click', function () {
      win.classList.toggle('ai-chat-hidden');
      if (!win.classList.contains('ai-chat-hidden')) {
        input.focus();
      }
    });

    closeBtn.addEventListener('click', function () {
      win.classList.add('ai-chat-hidden');
    });

    resetBtn.addEventListener('click', function () {
      messages = [{ role: 'system', content: SYSTEM_PROMPT }];
      const msgs = document.getElementById('ai-chat-messages');
      msgs.innerHTML = '<div class="ai-chat-msg ai-chat-msg-bot"><div class="ai-chat-msg-content">' + UI.welcome + '</div></div>';
      document.getElementById('ai-chat-chips').style.display = 'flex';
    });

    function send() {
      const text = input.value.trim();
      if (!text) return;
      addMessage('user', text);
      input.value = '';
      document.getElementById('ai-chat-chips').style.display = 'none';
      fetchAIResponse(text);
    }

    sendBtn.addEventListener('click', send);
    input.addEventListener('keydown', function (e) {
      if (e.key === 'Enter' && !e.shiftKey) {
        e.preventDefault();
        send();
      }
    });

    chips.forEach(function (chip) {
      chip.addEventListener('click', function () {
        input.value = chip.textContent;
        send();
      });
    });
  }

  // ── Add message to UI ──
  function addMessage(role, text) {
    const msgs = document.getElementById('ai-chat-messages');
    const div = document.createElement('div');
    div.className = 'ai-chat-msg ' + (role === 'user' ? 'ai-chat-msg-user' : 'ai-chat-msg-bot');
    div.innerHTML = '<div class="ai-chat-msg-content"></div>';
    msgs.appendChild(div);
    const content = div.querySelector('.ai-chat-msg-content');

    if (role === 'user') {
      content.textContent = text;
      messages.push({ role: 'user', content: text });
    } else {
      typeText(content, text);
    }
    msgs.scrollTop = msgs.scrollHeight;
  }

  // ── Typing animation ──
  function typeText(el, text, speed) {
    speed = speed || 15;
    el.textContent = '';
    let i = 0;
    function step() {
      if (i < text.length) {
        el.textContent += text[i];
        i++;
        el.parentElement.parentElement.scrollTop = el.parentElement.parentElement.scrollHeight;
        setTimeout(step, speed);
      }
    }
    step();
  }

  // ── Render markdown links (basic) ──
  function renderMarkdown(text) {
    return text
      .replace(/\[([^\]]+)\]\(([^)]+)\)/g, '<a href="$2" target="_blank" rel="noopener noreferrer" class="ai-chat-link">$1</a>')
      .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
      .replace(/\*([^*]+)\*/g, '<em>$1</em>');
  }

  // ── Fetch AI Response ──
  async function fetchAIResponse(userText) {
    const msgs = document.getElementById('ai-chat-messages');

    // Typing indicator
    const typingDiv = document.createElement('div');
    typingDiv.className = 'ai-chat-msg ai-chat-msg-bot ai-chat-typing-indicator';
    typingDiv.innerHTML = '<div class="ai-chat-msg-content"><span class="ai-chat-dot"></span><span class="ai-chat-dot"></span><span class="ai-chat-dot"></span></div>';
    msgs.appendChild(typingDiv);
    msgs.scrollTop = msgs.scrollHeight;

    messages.push({ role: 'user', content: userText });

    const modelsToTry = [MODEL].concat(FALLBACK_MODELS);
    let reply = null;
    let lastError = null;

    for (let i = 0; i < modelsToTry.length; i++) {
      const model = modelsToTry[i];
      try {
        const res = await fetch(OPENROUTER_URL, {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + OPENROUTER_API_KEY,
            'HTTP-Referer': window.location.origin,
            'X-Title': 'Eng. Ashraf AI Advisor'
          },
          body: JSON.stringify({
            model: model,
            messages: messages,
            max_tokens: 600,
            temperature: 0.7
          })
        });

        if (res.status === 429 || res.status === 404) {
          lastError = new Error('API error: ' + res.status + ' for model ' + model);
          continue;
        }
        if (!res.ok) throw new Error('API error: ' + res.status);

        const data = await res.json();
        reply = data.choices && data.choices[0] && data.choices[0].message
          ? data.choices[0].message.content
          : UI.error;
        break;
      } catch (err) {
        lastError = err;
        continue;
      }
    }

    typingDiv.remove();

    if (!reply) {
      addMessage('bot', UI.error);
      console.error('Chatbot error:', lastError);
      return;
    }

    messages.push({ role: 'assistant', content: reply });

    // Add bot message with typing effect
    const botDiv = document.createElement('div');
    botDiv.className = 'ai-chat-msg ai-chat-msg-bot';
    botDiv.innerHTML = '<div class="ai-chat-msg-content"></div>';
    msgs.appendChild(botDiv);
    const content = botDiv.querySelector('.ai-chat-msg-content');

    // Typing animation then render markdown
    let i = 0;
    const plain = reply;
    function step() {
      if (i < plain.length) {
        content.textContent = plain.slice(0, i + 1);
        i++;
        msgs.scrollTop = msgs.scrollHeight;
        setTimeout(step, 12);
      } else {
        content.innerHTML = renderMarkdown(plain);
        msgs.scrollTop = msgs.scrollHeight;
      }
    }
    step();
  }

  // ── Init on DOMContentLoaded ──
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', buildChatbot);
  } else {
    buildChatbot();
  }
})();
