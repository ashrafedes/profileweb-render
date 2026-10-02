/* ============================================================
   Article Engagement – likes, dislikes & comments (no login)
   - Reactions: shared counters via Abacus API (no account needed)
     with localStorage fallback if the API is unreachable.
   - Comments: saved in the visitor's browser (localStorage).
   Works on statically generated article pages (EN + AR).
   ============================================================ */

(function () {
  'use strict';

  var NS = 'ashraf-eldesoky-space';
  var API = 'https://abacus.jasoncameron.dev';
  var VOTE_KEY = 'aer_votes_v1';
  var COMMENT_KEY = 'aec_comments_v1';
  var LOCAL_COUNT_KEY = 'aer_local_counts_v1';

  function getSlug() {
    var m = window.location.pathname.match(/\/articles\/([^/]+)\.html$/);
    if (m) return decodeURIComponent(m[1]);
    return new URLSearchParams(window.location.search).get('slug') || '';
  }

  function getLang() {
    var m = window.location.pathname.match(/\/(en|ar)\/articles\//);
    if (m) return m[1];
    return 'en';
  }

  function strings(lang) {
    if (lang === 'ar') {
      return {
        helpful: 'هل كان المقال مفيداً؟',
        like: 'أعجبني',
        dislike: 'لم يعجبني',
        thanks: 'شكراً على ملاحظتك',
        comments: 'التعليقات',
        name: 'الاسم (اختياري)',
        anon: 'زائر',
        placeholder: 'شارك رأيك…',
        post: 'أرسل التعليق',
        note: 'تُحفظ التعليقات في متصفحك على هذا الجهاز.',
        empty: 'لا توجد تعليقات بعد — كن أول من يعلّق.'
      };
    }
    return {
      helpful: 'Was this article helpful?',
      like: 'Like',
      dislike: 'Dislike',
      thanks: 'Thanks for your feedback',
      comments: 'Comments',
      name: 'Name (optional)',
      anon: 'Anonymous',
      placeholder: 'Share your thoughts…',
      post: 'Post Comment',
      note: 'Comments are saved in your browser on this device.',
      empty: 'No comments yet — be the first to comment.'
    };
  }

  function esc(s) {
    return String(s)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;');
  }

  function linkify(s) {
    var urlRe = /(https?:\/\/[^\s<>"']+|www\.[^\s<>"']+)/gi;
    var out = '', last = 0, m;
    while ((m = urlRe.exec(s)) !== null) {
      out += esc(s.slice(last, m.index));
      var u = m[0];
      var href = /^https?:\/\//i.test(u) ? u : 'https://' + u;
      out += '<a href="' + esc(href) + '" target="_blank" rel="noopener noreferrer" class="ae-link">' + esc(u) + '</a>';
      last = urlRe.lastIndex;
    }
    return out + esc(s.slice(last));
  }

  function loadJSON(key) {
    try { return JSON.parse(localStorage.getItem(key)) || {}; }
    catch (e) { return {}; }
  }
  function saveJSON(key, v) {
    try { localStorage.setItem(key, JSON.stringify(v)); } catch (e) {}
  }

  /* ── Shared counter API (Abacus) with local fallback ── */
  function remoteGet(key) {
    return fetch(API + '/get/' + NS + '/' + key)
      .then(function (r) { if (!r.ok) throw new Error('get'); return r.json(); })
      .then(function (j) { return typeof j.value === 'number' ? j.value : 0; });
  }
  function remoteHit(key) {
    return fetch(API + '/hit/' + NS + '/' + key)
      .then(function (r) { if (!r.ok) throw new Error('hit'); return r.json(); })
      .then(function (j) { return typeof j.value === 'number' ? j.value : 0; });
  }
  function localGet(key) { return loadJSON(LOCAL_COUNT_KEY)[key] || 0; }
  function localBump(key) {
    var c = loadJSON(LOCAL_COUNT_KEY);
    c[key] = (c[key] || 0) + 1;
    saveJSON(LOCAL_COUNT_KEY, c);
    return c[key];
  }
  function getCount(key) {
    return remoteGet(key).catch(function () { return localGet(key); });
  }
  function bumpCount(key) {
    return remoteHit(key).catch(function () { return localBump(key); });
  }

  function injectStyles() {
    if (document.getElementById('ae-styles')) return;
    var s = document.createElement('style');
    s.id = 'ae-styles';
    s.textContent = [
      '#ae-root{margin-top:2.5rem;padding-top:2rem;border-top:1px solid var(--border-light);}',
      '.ae-reactions{display:flex;align-items:center;gap:.75rem;flex-wrap:wrap;margin-bottom:2.5rem;}',
      '.ae-reactions-label{font-size:.9rem;font-weight:600;color:var(--text-muted);}',
      '.ae-vote-btn{display:inline-flex;align-items:center;gap:.5rem;padding:.6rem 1.1rem;border:1px solid var(--border);border-radius:999px;background:var(--bg-card);color:var(--text);font-size:.9rem;font-weight:600;cursor:pointer;transition:all .2s;font-family:inherit;}',
      '.ae-vote-btn:hover{border-color:var(--accent);color:var(--accent);}',
      '.ae-vote-btn.active{background:var(--accent);color:#fff;border-color:var(--accent);}',
      '.ae-vote-btn:disabled{opacity:.85;cursor:default;}',
      '.ae-comments h2{font-size:1.3rem;margin-bottom:1rem;}',
      '.ae-form{display:grid;gap:.75rem;margin-bottom:.5rem;}',
      '.ae-form input,.ae-form textarea{width:100%;padding:.7rem .9rem;border:1px solid var(--border);border-radius:var(--radius-sm);background:var(--bg-card);color:var(--text);font-family:inherit;font-size:.9rem;}',
      '.ae-form textarea{min-height:110px;resize:vertical;}',
      '.ae-form input:focus,.ae-form textarea:focus{outline:none;border-color:var(--accent);}',
      '.ae-submit{justify-self:start;padding:.65rem 1.6rem;border:none;border-radius:var(--radius-sm);background:var(--accent);color:#fff;font-weight:600;font-size:.9rem;cursor:pointer;font-family:inherit;}',
      '.ae-submit:hover{background:var(--accent-hover);}',
      '.ae-note{font-size:.78rem;color:var(--text-light);margin:0 0 1.5rem;}',
      '.ae-list{display:grid;gap:1rem;}',
      '.ae-comment{display:flex;gap:.8rem;}',
      '.ae-avatar{width:38px;height:38px;border-radius:50%;background:var(--bg-alt);border:1px solid var(--border-light);display:flex;align-items:center;justify-content:center;font-weight:700;color:var(--accent);flex-shrink:0;font-size:.9rem;}',
      '.ae-c-body{flex:1;background:var(--bg-alt);border:1px solid var(--border-light);border-radius:var(--radius-md);padding:.8rem 1rem;}',
      '.ae-c-head{display:flex;gap:.6rem;align-items:baseline;flex-wrap:wrap;margin-bottom:.3rem;}',
      '.ae-c-name{font-weight:700;font-size:.88rem;}',
      '.ae-c-date{font-size:.75rem;color:var(--text-light);}',
      '.ae-c-text{font-size:.9rem;color:var(--text);white-space:pre-wrap;word-break:break-word;margin:0;}',
      '.ae-link{color:#2563eb;text-decoration:underline;word-break:break-all;}',
      '.ae-empty{color:var(--text-muted);font-size:.9rem;}'
    ].join('\n');
    document.head.appendChild(s);
  }

  function formatCommentDate(iso, lang) {
    var d = new Date(iso);
    if (isNaN(d.getTime())) return '';
    return d.toLocaleDateString(lang === 'ar' ? 'ar-EG' : 'en-US',
      { year: 'numeric', month: 'short', day: 'numeric' });
  }

  function init() {
    var slug = getSlug();
    var body = document.getElementById('article-body');
    if (!slug || !body || document.getElementById('ae-root')) return;

    var lang = getLang();
    var T = strings(lang);
    injectStyles();

    var likeKey = slug + '-like';
    var dislikeKey = slug + '-dislike';

    /* ── Build DOM ── */
    var root = document.createElement('div');
    root.id = 'ae-root';
    root.innerHTML =
      '<div class="ae-reactions">' +
        '<span class="ae-reactions-label">' + T.helpful + '</span>' +
        '<button type="button" class="ae-vote-btn" data-vote="like">👍 <span>' + T.like + '</span> · <b data-count="like">0</b></button>' +
        '<button type="button" class="ae-vote-btn" data-vote="dislike">👎 <span>' + T.dislike + '</span> · <b data-count="dislike">0</b></button>' +
      '</div>' +
      '<div class="ae-comments">' +
        '<h2>' + T.comments + ' <span id="ae-count" style="color:var(--text-light);font-weight:400;font-size:0.9rem;"></span></h2>' +
        '<form class="ae-form" id="ae-form">' +
          '<input type="text" id="ae-name" maxlength="60" placeholder="' + T.name + '">' +
          '<textarea id="ae-text" maxlength="1000" required placeholder="' + T.placeholder + '"></textarea>' +
          '<button type="submit" class="ae-submit">' + T.post + '</button>' +
        '</form>' +
        '<p class="ae-note">' + T.note + '</p>' +
        '<div class="ae-list" id="ae-list"></div>' +
      '</div>';
    body.appendChild(root);

    /* ── Reactions ── */
    var votes = loadJSON(VOTE_KEY);
    var myVote = votes[slug] || null;
    var likeBtn = root.querySelector('[data-vote="like"]');
    var dislikeBtn = root.querySelector('[data-vote="dislike"]');
    var likeCountEl = root.querySelector('[data-count="like"]');
    var dislikeCountEl = root.querySelector('[data-count="dislike"]');

    function paintVote() {
      likeBtn.classList.toggle('active', myVote === 'like');
      dislikeBtn.classList.toggle('active', myVote === 'dislike');
      if (myVote) {
        likeBtn.disabled = true;
        dislikeBtn.disabled = true;
        likeBtn.title = T.thanks;
        dislikeBtn.title = T.thanks;
      }
    }

    getCount(likeKey).then(function (n) { likeCountEl.textContent = n; });
    getCount(dislikeKey).then(function (n) { dislikeCountEl.textContent = n; });
    paintVote();

    function vote(kind) {
      if (myVote) return;
      myVote = kind;
      votes[slug] = kind;
      saveJSON(VOTE_KEY, votes);
      paintVote();
      bumpCount(kind === 'like' ? likeKey : dislikeKey).then(function (n) {
        (kind === 'like' ? likeCountEl : dislikeCountEl).textContent = n;
      });
    }
    likeBtn.addEventListener('click', function () { vote('like'); });
    dislikeBtn.addEventListener('click', function () { vote('dislike'); });

    /* ── Comments ── */
    var list = root.querySelector('#ae-list');
    var countEl = root.querySelector('#ae-count');
    var form = root.querySelector('#ae-form');
    var nameInput = root.querySelector('#ae-name');
    var textInput = root.querySelector('#ae-text');

    function getComments() {
      var all = loadJSON(COMMENT_KEY);
      return Array.isArray(all[slug]) ? all[slug] : [];
    }
    function saveComments(arr) {
      var all = loadJSON(COMMENT_KEY);
      all[slug] = arr;
      saveJSON(COMMENT_KEY, all);
    }

    function renderComments() {
      var items = getComments();
      countEl.textContent = items.length ? '(' + items.length + ')' : '';
      if (!items.length) {
        list.innerHTML = '<p class="ae-empty">' + T.empty + '</p>';
        return;
      }
      list.innerHTML = items.map(function (c) {
        var name = esc(c.n || T.anon);
        var initial = (c.n || T.anon).trim().charAt(0).toUpperCase() || '?';
        return '<div class="ae-comment">' +
          '<div class="ae-avatar">' + esc(initial) + '</div>' +
          '<div class="ae-c-body">' +
            '<div class="ae-c-head"><span class="ae-c-name">' + name + '</span>' +
            '<span class="ae-c-date">' + formatCommentDate(c.d, lang) + '</span></div>' +
            '<p class="ae-c-text">' + linkify(c.t) + '</p>' +
          '</div>' +
        '</div>';
      }).join('');
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var text = textInput.value.trim();
      if (!text) return;
      var name = nameInput.value.trim() || T.anon;
      var items = getComments();
      items.push({ n: name.slice(0, 60), t: text.slice(0, 1000), d: new Date().toISOString() });
      saveComments(items);
      textInput.value = '';
      renderComments();
    });

    renderComments();
  }

  window.ArticleEngagement = { init: init };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
