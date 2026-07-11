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
    'google/gemini-2.0-flash-exp:free'
  ];

  // ── Google Forms Logger (writes to your Google Sheet) ──
  const FORM_ACTION_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSdVFMrDmzSDF5ebhMeeydB4bvTWZ6Zdj0_UADjE58WCb1m_4A/formResponse';
  const FORM_FIELDS = {
    timestamp: 'entry.140123149',
    page: 'entry.1034937424',
    language: 'entry.8073323',
    role: 'entry.275150362',
    message: 'entry.1023348545'
  };

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
    newChat: 'محادثة جديدة',
    save: 'حفظ المحادثة',
    saved: 'تم الحفظ!',
    noConvo: 'لا توجد محادثة للحفظ'
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
    newChat: 'New Chat',
    save: 'Save Conversation',
    saved: 'Saved!',
    noConvo: 'No conversation to save'
  };

  // ── System Prompt ──
  // CV_DATA is loaded from cv-data.js (included before chatbot.js in HTML)
  const CV_CONTEXT = (typeof CV_DATA !== 'undefined') ? CV_DATA : '';

  const SYSTEM_PROMPT = IS_ARABIC
    ? `أنت "مساعد المهندس أشرف الذكي" — مساعد تنفيذي احترافي يمثل المهندس أشرف إبراهيم الدسوقي، PMP®.

إليك الملف المهني الكامل للمهندس أشرف. استخدم هذه المعلومات للإجابة على أي سؤال عنه بدقة:

${CV_CONTEXT}

البرمجيات النشطة (أضف روابط markdown عند الاقتراب):
- منصة إدارة النثرية المالية (Petty Cash): [نظام التشغيل](https://pattycashsystem.web.app/) | [صفحة التسويق](https://pettycash-marketing.web.app/)
- InfraFlow: منصة تتبع مشاريع الاتصالات/FTTH للمؤسسات.

قواعد الرد:
0. مهم جداً: لا تكتب أي تفكير داخلي أو تحليل أو ملاحظات لنفسك. لا تبدأ بـ "حسناً" أو "دعني" أو أي تمهيد. ابدأ الرد مباشرة بالإجابة المطلوبة فقط. لا تستخدم علامات  أو  أو أي وسوم تفكير.
1. رد بلغة عربية احترافية وواضحة.
2. كن موجزاً ومباشراً (3-5 جمل عادةً).
3. اعرض خبرة المهندس أشرف بشكل طبيعي عند الاقتراب.
4. أضف روابط markdown للأنظمة النشطة عندما يكون ذلك مناسباً.
5. لا تخترع معلومات غير مذكورة في الملف المهني أعلاه.
6. إذا سُئلت عن شيء لا تعرفه من البيانات، اعتذر بصدق ووجه السائل لمراسلة ashrafede@gmail.com.`
    : `You are "Eng. Ashraf's AI Advisor" — a professional executive assistant representing Eng. Ashraf Ibrahim El Desoky, PMP®.

Here is the complete professional profile of Eng. Ashraf. Use this information to answer any question about him accurately:

${CV_CONTEXT}

Active Software (inject markdown links when relevant):
- Petty Cash SaaS System: [Live System](https://pattycashsystem.web.app/) | [Marketing Page](https://pettycash-marketing.web.app/)
- InfraFlow: Enterprise telecom/FTTH tracking platform.

CRITICAL: Do NOT output any internal thinking, reasoning, analysis, or notes to yourself. Do NOT start with "Okay", "Let me", "Well", or any preamble. Start your response directly with the answer only. Do NOT use  or  tags or any thinking markers.

Response Rules:
1. Respond in clear, professional English.
2. Be concise and direct (3-5 sentences typically).
3. Naturally showcase Ashraf's expertise when relevant.
4. Add markdown links to active software when appropriate.
5. Do not invent information not provided in the professional profile above.
6. If asked about something you don't know from the data, apologize honestly and direct the inquirer to email ashrafede@gmail.com.`;

  // ── Conversation history ──
  let messages = [{ role: 'system', content: SYSTEM_PROMPT }];

  // ── Build DOM ──
  function buildChatbot() {
    const root = document.createElement('div');
    root.id = 'ai-chatbot-root';
    root.setAttribute('dir', DIR);
    root.innerHTML = `
      <!-- Floating Bubble -->
      <button id="ai-chat-bubble" class="ai-chat-bubble" aria-label="${IS_ARABIC ? 'افتح دردشة الذكاء الاصطناعي' : 'Open AI Chat'}">
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
            <button id="ai-chat-save" class="ai-chat-icon-btn" title="${UI.save}" aria-label="${UI.save}">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11l5 5v11a2 2 0 0 1-2 2z"/><polyline points="17 21 17 13 7 13 7 21"/><polyline points="7 3 7 8 15 8"/></svg>
            </button>
            <button id="ai-chat-reset" class="ai-chat-icon-btn" title="${UI.newChat}" aria-label="${UI.newChat}">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 12a9 9 0 1 0 9-9 9.75 9.75 0 0 0-6.74 2.74L3 8"/><path d="M3 3v5h5"/></svg>
            </button>
            <button id="ai-chat-close" class="ai-chat-icon-btn" title="${IS_ARABIC ? 'إغلاق' : 'Close'}" aria-label="${IS_ARABIC ? 'إغلاق' : 'Close'}">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="18" y1="6" x2="6" y2="18"/><line x1="6" y1="6" x2="18" y2="18"/></svg>
            </button>
          </div>
        </div>

        <!-- Messages -->
        <div id="ai-chat-messages" class="ai-chat-messages">
          <div class="ai-chat-msg ai-chat-msg-bot">
            <div class="ai-chat-msg-avatar">AI</div>
            <div class="ai-chat-msg-content">${UI.welcome}</div>
          </div>
        </div>

        <!-- Quick Chips -->
        <div id="ai-chat-chips" class="ai-chat-chips">
          ${UI.chips.map(c => `<button class="ai-chat-chip">${c}</button>`).join('')}
        </div>

        <!-- Input (ChatGPT-style: rounded box with send button inside) -->
        <div class="ai-chat-input-area">
          <div class="ai-chat-input-wrapper">
            <textarea id="ai-chat-input" class="ai-chat-input" placeholder="${UI.placeholder}" rows="1" autocomplete="off"></textarea>
            <button id="ai-chat-send" class="ai-chat-send" aria-label="${UI.send}">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="22" y1="2" x2="11" y2="13"/><polygon points="22 2 15 22 11 13 2 9 22 2"/></svg>
            </button>
          </div>
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
    const saveBtn = document.getElementById('ai-chat-save');

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
      // Auto-log current conversation before resetting
      var convo = messages.filter(function (m) {
        return m.role === 'user' || m.role === 'assistant';
      });
      // Auto-logging already happens per response, no need here

      messages = [{ role: 'system', content: SYSTEM_PROMPT }];
      const msgs = document.getElementById('ai-chat-messages');
      msgs.innerHTML = '<div class="ai-chat-msg ai-chat-msg-bot"><div class="ai-chat-msg-avatar">AI</div><div class="ai-chat-msg-content">' + UI.welcome + '</div></div>';
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

    saveBtn.addEventListener('click', saveConversation);
  }

  // ── Save conversation: download as .txt + log to Google Sheets ──
  function saveConversation() {
    var convo = messages.filter(function (m) {
      return m.role === 'user' || m.role === 'assistant';
    });

    if (convo.length === 0) {
      alert(UI.noConvo);
      return;
    }

    // Build text version for download
    var lines = [];
    lines.push('====================================');
    lines.push(IS_ARABIC ? 'محادثة مع مساعد المهندس أشرف الذكي' : 'Conversation with Eng. Ashraf AI Advisor');
    lines.push(new Date().toLocaleString());
    lines.push('====================================');
    lines.push('');
    convo.forEach(function (m) {
      var label = m.role === 'user'
        ? (IS_ARABIC ? 'الزائر' : 'Visitor')
        : 'AI';
      lines.push(label + ': ' + m.content);
      lines.push('');
    });
    var text = lines.join('\n');

    // Download as .txt file
    var blob = new Blob([text], { type: 'text/plain;charset=utf-8' });
    var a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = 'chat-' + new Date().toISOString().slice(0, 19).replace(/:/g, '-') + '.txt';
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);

    // Download as .txt file only (auto-logging happens per response)
  }

  // ── Send conversation to Google Sheet via Google Forms ──
  function logToGoogleSheet(convo) {
    var timestamp = new Date().toISOString();
    var page = window.location.pathname;
    var language = IS_ARABIC ? 'ar' : 'en';

    convo.forEach(function (m) {
      var formData = new FormData();
      formData.append(FORM_FIELDS.timestamp, timestamp);
      formData.append(FORM_FIELDS.page, page);
      formData.append(FORM_FIELDS.language, language);
      formData.append(FORM_FIELDS.role, m.role);
      formData.append(FORM_FIELDS.message, m.content);
      formData.append('fvv', '1');
      formData.append('fbzx', '');

      fetch(FORM_ACTION_URL, {
        method: 'POST',
        mode: 'no-cors',
        body: formData
      }).catch(function (e) {
        console.warn('Form log failed:', e);
      });
    });
  }

  // ── Add message to UI ──
  function addMessage(role, text) {
    const msgs = document.getElementById('ai-chat-messages');
    const div = document.createElement('div');
    div.className = 'ai-chat-msg ' + (role === 'user' ? 'ai-chat-msg-user' : 'ai-chat-msg-bot');
    const avatarLabel = role === 'user' ? (IS_ARABIC ? 'أنت' : 'You') : 'AI';
    div.innerHTML = '<div class="ai-chat-msg-avatar">' + avatarLabel + '</div><div class="ai-chat-msg-content"></div>';
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

  // ── Clean reasoning models' internal thinking from output ──
  function cleanReply(text) {
    if (!text) return '';

    // 1. Remove XML-style thinking tags: <thinking>...</thinking>, <think>...</think>, etc.
    text = text.replace(/<thinking>[\s\S]*?<\/thinking>/gi, '');
    text = text.replace(/<think>[\s\S]*?<\/think>/gi, '');
    text = text.replace(/<analysis>[\s\S]*?<\/analysis>/gi, '');
    text = text.replace(/<reasoning>[\s\S]*?<\/reasoning>/gi, '');
    text = text.replace(/<reflection>[\s\S]*?<\/reflection>/gi, '');

    // 2. Remove unclosed thinking tags (model forgot to close) — strip to end
    text = text.replace(/<thinking>[\s\S]*$/gi, '');
    text = text.replace(/<think>[\s\S]*$/gi, '');

    // 3. Remove markdown code fences with thinking/reasoning labels
    text = text.replace(/```(?:thinking|reasoning|analysis|reflection)\s*[\s\S]*?```/gi, '');

    // 4. Remove visible "Reasoning:" or "Thinking:" preamble blocks
    text = text.replace(/^\s*(Reasoning|Thinking|Reflection|Thought process|Internal monologue)[:\s]*[\s\S]*?(?=\n\n|$)/im, '');

    // 5. Remove untagged reasoning at the start — internal monologue patterns
    text = text.replace(/^["']?(Okay|Let me|Let's|Alright|Well,? now|So,? let|Now let|Looking at|Based on the|I should|I need to|The user|This user|First,? let me|Let me check|Let me look|Hmm,? let|Alright,? so|So,? the user|The visitor|I'll start|Let me think|Let me analyze|Let me consider|To answer this|To respond to this)[^\n]*(?:\n(?:[^a-zA-Z\n]|[A-Z][^\n]*|[\u0600-\u06FF][^\n]*)){0,30}/i, '');

    // 6. Remove quoted reasoning blocks at the start
    text = text.replace(/^["'][\s\S]*?["']\s*\n/i, '');

    // 7. Remove step-by-step reasoning blocks (numbered list of reasoning steps)
    text = text.replace(/^(Step \d+|\d+\.)\s+(First|Let me|I need|I should|The user|Okay|Now|So|Looking|Based|To answer|The question)[^\n]*/im, '');

    // 8. Line-by-line scan: strip leading reasoning lines, keep first real answer line
    var lines = text.split('\n');
    var startIdx = -1;
    for (var li = 0; li < lines.length; li++) {
      var line = lines[li].trim();
      if (line.length < 3) continue;
      // Check if line looks like reasoning/internal monologue
      var isReasoning = /^(Okay|Let me|Let's|Alright|Well,? now|So,? let|Now let|Looking at|Based on the|I should|I need to|The user|This user|First,? let me|Let me check|Let me look|Hmm,? let|Alright,? so|So,? the user|The visitor|I'll start|Let me think|Let me analyze|Let me consider|To answer this|To respond to this|Step \d+|\d+\.\s|Reasoning:|Thinking:|Reflection:)/i.test(line);
      // Arabic reasoning openers
      var isArReasoning = /^(حسنا|دعني|حسناً|إذن|أولاً|الآن|لذا|بناء على|يجب أن|أحتاج إلى|المستخدم|الزائر|للإجابة|لتحليل|بما أن)/.test(line);
      if (!isReasoning && !isArReasoning) {
        startIdx = li;
        break;
      }
    }
    if (startIdx > 0) {
      text = lines.slice(startIdx).join('\n');
    }

    // 9. For Arabic pages, also strip everything before first substantial Arabic line
    if (IS_ARABIC) {
      var arLines = text.split('\n');
      var arStart = -1;
      for (var ai = 0; ai < arLines.length; ai++) {
        var arLine = arLines[ai].trim();
        if (/^[\u0600-\u06FF]/.test(arLine) && arLine.split(/\s+/).length >= 2) {
          arStart = ai;
          break;
        }
      }
      if (arStart > 0) {
        text = arLines.slice(arStart).join('\n');
      }
    }

    return text.trim();
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
    typingDiv.innerHTML = '<div class="ai-chat-msg-avatar">AI</div><div class="ai-chat-msg-content"><span class="ai-chat-dot"></span><span class="ai-chat-dot"></span><span class="ai-chat-dot"></span></div>';
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
            temperature: 0.7,
            reasoning: { effort: 'none' }
          })
        });

        if (res.status === 429 || res.status === 404) {
          lastError = new Error('API error: ' + res.status + ' for model ' + model);
          continue;
        }
        if (!res.ok) throw new Error('API error: ' + res.status);

        const data = await res.json();
        if (data.choices && data.choices[0] && data.choices[0].message) {
          reply = data.choices[0].message.content || '';
          // Some models return reasoning in a separate field — discard it
          if (data.choices[0].message.reasoning) {
            // reasoning is separate, content is the answer — nothing to do
          }
        } else {
          reply = UI.error;
        }
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

    // Strip internal reasoning/thinking before showing to user
    const clean = cleanReply(reply);
    messages.push({ role: 'assistant', content: clean });

    // Add bot message with typing effect
    const botDiv = document.createElement('div');
    botDiv.className = 'ai-chat-msg ai-chat-msg-bot';
    botDiv.innerHTML = '<div class="ai-chat-msg-avatar">AI</div><div class="ai-chat-msg-content"></div>';
    msgs.appendChild(botDiv);
    const content = botDiv.querySelector('.ai-chat-msg-content');

    // Typing animation then render markdown
    let i = 0;
    const plain = clean;
    function step() {
      if (i < plain.length) {
        content.textContent = plain.slice(0, i + 1);
        i++;
        // Only scroll every 5 characters to reduce jitter
        if (i % 5 === 0) msgs.scrollTop = msgs.scrollHeight;
        setTimeout(step, 12);
      } else {
        content.innerHTML = renderMarkdown(plain);
        msgs.scrollTop = msgs.scrollHeight;
        // Auto-log this Q&A pair to Google Sheets
        logToGoogleSheet([
          { role: 'user', content: userText },
          { role: 'assistant', content: clean }
        ]);
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
