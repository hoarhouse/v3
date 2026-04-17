(function() {
  // ── CONFIG ──────────────────────────────────────────────────────────────
  var PROXY = 'http://localhost:3000';
  var ENDPOINT = PROXY + '/v1/messages';

  // ── SYSTEM PROMPT ───────────────────────────────────────────────────────
  var SYSTEM = `You are E-Group's AI assistant, embedded on the E-Group ICT Software Zrt. website. You answer questions about E-Group accurately, concisely, and in brand voice.

BRAND VOICE: Quiet confidence. Short sentences. Active voice. Never use: solutions, disrupt, innovative, cutting-edge, leverage, synergy. Always use: built, delivered, operates, proven, live in production. No hype. No padding. If you don't know something, say so directly.

ABOUT E-GROUP:
- Full name: E-Group ICT Software Zrt.
- Founded: 1993, Budapest, Hungary. 100% Hungarian-owned.
- Staff: 90+ professionals, 50+ external associates
- Offices: Budapest HQ, Pécs R&D, Miskolc R&D, Hong Kong (E-Group Asia), Vietnam (E-Group Vietnam)
- Sectors: FinTech, HealthTech, GovTech, SpaceTech, EnergyTech
- Legal: Reg 01 10 045390 HUN, Tax 13665908-2-41, EU VAT HU13665908
- Address: Alsó Törökvész út 2, H-1022 Budapest, Hungary
- Website: egroup.hu
- LinkedIn: linkedin.com/company/e-group-ict-group

FOUNDERS & LEADERSHIP:
- Antal Kuthy — Co-founder & CEO. MSc BME. IBM R&D Heidelberg. NTT Tokyo. FCO Chevening Scholar UCL London. Founded E-Group Asia (Hong Kong) and E-Group Vietnam. Chairs the AI Cluster and sits on EU Industry Steering Board of IPCEI-CIS. Coined #DoersParadise.
- András Nagy — Co-founder & CTO. MSc BME. IBM Watson Heidelberg. CISA certified. Personally designed and implemented KAÜ — Hungary's national digital authorisation service.
- László Blénessy — Deputy Group CEO
- Tibor Farkas — COO/CFO
- Mark Marosi — Head of Research
- Dr. Péter Antal — Lead Researcher. BME Associate Professor. FedEU.ai lead. Awarded Hungary's Knight's Cross of the Order of Merit, August 2025.
- Ágota Benedek — Research Engineer. Lead author of GRaDPaLM. Neumann Colloquium Best Scientific Article winner, November 2025.
- Csaba Potyók — Research Engineer. GRaDPaLM co-author. Neumann Colloquium + BME TDK winner, November 2025.
- Tamás Mészáros PhD — Senior Researcher, BME Associate Professor. GRaDPaLM co-author. BME TDK first place, November 2025.
- Dr. Anna Kovács — HealthTech AI Research Lead. Back-to-back international first place 2024.
- Gábor Mészáros — FinTech Lead
- Katalin Varga — GovTech Lead

LIVE PRODUCTS & PROJECTS:
- MAVIR: Hungary's electricity transmission system operator. E-Group's longest client — 25+ years unbroken. Mission-critical settlement systems, market modelling, regulatory change management.
- KAÜ: Hungary's national digital authorisation service. Designed and implemented personally by András Nagy. Authenticates millions of Hungarian citizens across all government services daily.
- FedX / HeliX: Federated learning platform. 8 biobank clients, 50+ healthcare providers, 12,000+ individuals. EHDEN certified. Running in the HeliX Health Data Space — one of Europe's largest sovereign health data ecosystems. HeliX General Assembly hosted at E-Group HQ, March 2026.
- MyD Wallet: Hungary's live EUDI Wallet implementation. Post-quantum cryptography. All eIDAS 2.0 testbed scenarios passed. White-label ready. Client: Hungarian Government. EWC consortium member.
- CORPEX: Corporate internet banking platform. Live in production for 20+ years across Central European financial institutions.
- IPCEI-CIS / FedEU.ai: European Commission approved. 7 EU member states. €1.2bn programme. E-Group co-leads Workstream 3 and the AI Cluster — building sovereign federated AI infrastructure for Europe.

IN DEVELOPMENT:
- COIOS (Cognitive Open Intelligence Operating Sovereign): Europe's first sovereign agentic AI platform for system integrators. Nine capability pillars. Deploy anywhere — on-premise, air-gapped, regional cloud. White-label ready. GDPR, EU AI Act, HIPAA compliant by design. 52/52 feature categories covered. No direct European competitor. PoC partnerships open. Target sectors: FinTech, HealthTech, GovTech, SpaceTech. TAM €125B.
- ProofX: Cryptographic image and video verification. Galileo OSNMA satellite authentication + C2PA standards. Court-admissible evidence chains. ESA partnership active.
- GENESIS: Synthetic satellite imagery generation and analysis. ESA partnership active. Built for space data, defence-adjacent, geospatial intelligence.
- SpadaX: Real-time sensor analytics, anomaly detection, predictive maintenance for space and ground infrastructure.
- Neonatal Intelligence: AI-powered neonatal tracking and care intelligence. Built on FedX foundations.

EU PROGRAMMES & RECOGNITION:
- IPCEI-CIS: Co-leads Workstream 3 + AI Cluster. 7 member states. €1.2bn.
- HeliX: EU health data space. FedX platform validated.
- EWC (European Wallet Consortium): eIDAS 2.0 member.
- EU DOME: European data marketplace participant.
- ESA partnerships: ProofX and GENESIS.
- Dr. Péter Antal: Knight's Cross of the Order of Merit of Hungary, August 2025.
- GRaDPaLM: Best Scientific Article at Neumann Colloquium + BME TDK first place, November 2025.
- Dr. Anna Kovács: Back-to-back international first place 2024.

CONTACT:
- For partnerships, PoC discussions, or press: contact form at egroup.hu or via the Work With Us page on this site.
- Response time: within 48 hours if there is a fit.

INSTRUCTIONS:
- Answer questions directly and accurately. Keep answers concise — 2-4 sentences unless more detail is genuinely needed.
- If asked about pricing, say E-Group discusses commercial terms directly and suggest contacting them.
- If asked about something not covered above, say you don't have that information and suggest visiting egroup.hu or using the contact form.
- Suggest the contact page ONLY when the question is specifically about partnering, PoC, working together, or procurement — not for general questions.
- Never make up facts about E-Group. Never claim capabilities that aren't listed above.
- You can answer in the same language the user writes in.`;

  // ── STATE ────────────────────────────────────────────────────────────────
  var history = [];
  var isOpen = false;
  var isLoading = false;

  // ── STYLES ───────────────────────────────────────────────────────────────
  var css = `
    #eg-chat-btn {
      position:fixed;bottom:28px;right:28px;z-index:998;
      display:flex;align-items:center;gap:10px;
      background:#C8A96E;color:#080808;
      font-family:'DM Mono',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;
      border:none;padding:14px 20px;cursor:pointer;
      box-shadow:0 4px 24px rgba(0,0,0,0.4);
      transition:background 0.2s,transform 0.2s;
    }
    #eg-chat-btn:hover{background:#A07840;transform:translateY(-1px);}
    #eg-chat-btn .eg-btn-dot{width:8px;height:8px;border-radius:50%;background:#080808;animation:eg-pulse 2s ease-in-out infinite;}
    @keyframes eg-pulse{0%,100%{opacity:1;}50%{opacity:0.4;}}

    #eg-chat-panel {
      position:fixed;bottom:90px;right:28px;z-index:999;
      width:380px;max-height:560px;
      background:#0A0A0A;border:1px solid #1A1A1A;
      display:flex;flex-direction:column;
      box-shadow:0 8px 40px rgba(0,0,0,0.6);
      transform:translateY(20px) scale(0.97);opacity:0;
      transition:transform 0.25s ease,opacity 0.25s ease;
      pointer-events:none;
    }
    #eg-chat-panel.open{transform:translateY(0) scale(1);opacity:1;pointer-events:all;}

    .eg-panel-header{
      display:flex;align-items:center;justify-content:space-between;
      padding:16px 20px;border-bottom:1px solid #1A1A1A;
      background:#080808;flex-shrink:0;
    }
    .eg-panel-title{display:flex;align-items:center;gap:10px;}
    .eg-logo-e{width:24px;height:24px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:12px;flex-shrink:0;}
    .eg-title-text{font-family:'DM Mono',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#EFEFEF;}
    .eg-title-sub{font-family:'DM Mono',monospace;font-size:9px;letter-spacing:1px;color:#555;margin-top:2px;}
    .eg-close{background:none;border:none;color:#555;cursor:pointer;font-size:18px;line-height:1;padding:4px;transition:color 0.2s;}
    .eg-close:hover{color:#EFEFEF;}

    .eg-messages{flex:1;overflow-y:auto;padding:20px;display:flex;flex-direction:column;gap:12px;scroll-behavior:smooth;}
    .eg-messages::-webkit-scrollbar{width:3px;}
    .eg-messages::-webkit-scrollbar-track{background:transparent;}
    .eg-messages::-webkit-scrollbar-thumb{background:#1A1A1A;}

    .eg-msg{display:flex;flex-direction:column;max-width:88%;}
    .eg-msg.user{align-self:flex-end;align-items:flex-end;}
    .eg-msg.ai{align-self:flex-start;align-items:flex-start;}
    .eg-msg-bubble{padding:12px 16px;font-family:'DM Sans',sans-serif;font-size:13px;line-height:1.6;border-radius:2px;}
    .eg-msg.user .eg-msg-bubble{background:#C8A96E;color:#080808;}
    .eg-msg.ai .eg-msg-bubble{background:#161616;color:#B0B0B0;border:1px solid #1A1A1A;}
    .eg-msg-time{font-family:'DM Mono',monospace;font-size:9px;color:#333;margin-top:4px;letter-spacing:0.5px;}

    .eg-typing{display:flex;gap:4px;align-items:center;padding:12px 16px;background:#161616;border:1px solid #1A1A1A;align-self:flex-start;}
    .eg-typing span{width:5px;height:5px;border-radius:50%;background:#555;animation:eg-typing 1.2s ease-in-out infinite;}
    .eg-typing span:nth-child(2){animation-delay:0.2s;}
    .eg-typing span:nth-child(3){animation-delay:0.4s;}
    @keyframes eg-typing{0%,60%,100%{transform:translateY(0);}30%{transform:translateY(-6px);}}

    .eg-contact-nudge{margin-top:8px;display:inline-block;}
    .eg-contact-nudge a{font-family:'DM Mono',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#C8A96E;text-decoration:none;border-bottom:1px solid rgba(200,169,110,0.3);padding-bottom:1px;}
    .eg-contact-nudge a:hover{border-color:#C8A96E;}

    .eg-input-wrap{padding:16px;border-top:1px solid #1A1A1A;display:flex;gap:8px;flex-shrink:0;background:#080808;}
    .eg-input{flex:1;background:#111;border:1px solid #252525;color:#EFEFEF;font-family:'DM Sans',sans-serif;font-size:13px;padding:10px 14px;outline:none;resize:none;line-height:1.5;max-height:80px;transition:border-color 0.2s;}
    .eg-input:focus{border-color:#C8A96E;}
    .eg-input::placeholder{color:#333;}
    .eg-send{background:#C8A96E;border:none;color:#080808;padding:10px 16px;cursor:pointer;font-family:'DM Mono',monospace;font-size:11px;letter-spacing:1px;transition:background 0.2s;flex-shrink:0;align-self:flex-end;}
    .eg-send:hover{background:#A07840;}
    .eg-send:disabled{background:#1A1A1A;color:#333;cursor:not-allowed;}

    .eg-error{font-family:'DM Mono',monospace;font-size:10px;color:#BF7C7C;padding:8px 14px;background:#1A0A0A;border:1px solid #3A1A1A;margin-top:4px;}

    @media(max-width:768px){
      #eg-chat-btn{bottom:16px;right:16px;}
      #eg-chat-panel{bottom:78px;}
    }
    @media(max-width:480px){
      #eg-chat-panel{width:calc(100vw - 32px);right:16px;bottom:80px;}
      #eg-chat-btn{right:16px;bottom:16px;}
    }
  `;

  // ── INJECT STYLES ────────────────────────────────────────────────────────
  var style = document.createElement('style');
  style.textContent = css;
  document.head.appendChild(style);

  // ── BUILD HTML ───────────────────────────────────────────────────────────
  var container = document.createElement('div');
  container.innerHTML = `
    <button id="eg-chat-btn" aria-label="Ask E-Group AI">
      <span class="eg-btn-dot"></span>
      Ask E-Group
    </button>

    <div id="eg-chat-panel" role="dialog" aria-label="E-Group AI Assistant">
      <div class="eg-panel-header">
        <div class="eg-panel-title">
          <div class="eg-logo-e">E</div>
          <div>
            <div class="eg-title-text">E-Group AI</div>
            <div class="eg-title-sub">Ask anything about E-Group</div>
          </div>
        </div>
        <button class="eg-close" id="eg-close-btn" aria-label="Close">×</button>
      </div>
      <div class="eg-messages" id="eg-messages"></div>
      <div class="eg-input-wrap">
        <textarea class="eg-input" id="eg-input" placeholder="Ask about our work, team, products..." rows="1"></textarea>
        <button class="eg-send" id="eg-send-btn" disabled>Send</button>
      </div>
    </div>
  `;
  document.body.appendChild(container);

  // ── ELEMENTS ─────────────────────────────────────────────────────────────
  var btn = document.getElementById('eg-chat-btn');
  var panel = document.getElementById('eg-chat-panel');
  var closeBtn = document.getElementById('eg-close-btn');
  var messages = document.getElementById('eg-messages');
  var input = document.getElementById('eg-input');
  var sendBtn = document.getElementById('eg-send-btn');

  // ── HELPERS ───────────────────────────────────────────────────────────────
  function timestamp() {
    var d = new Date();
    return d.getHours().toString().padStart(2,'0') + ':' + d.getMinutes().toString().padStart(2,'0');
  }

  function addMessage(role, text, showNudge) {
    var msg = document.createElement('div');
    msg.className = 'eg-msg ' + role;
    var bubble = document.createElement('div');
    bubble.className = 'eg-msg-bubble';
    bubble.textContent = text;
    msg.appendChild(bubble);
    if (showNudge) {
      var nudge = document.createElement('div');
      nudge.className = 'eg-contact-nudge';
      nudge.innerHTML = '<a href="contact.html">Start a conversation →</a>';
      msg.appendChild(nudge);
    }
    var time = document.createElement('div');
    time.className = 'eg-msg-time';
    time.textContent = timestamp();
    msg.appendChild(time);
    messages.appendChild(msg);
    messages.scrollTop = messages.scrollHeight;
  }

  function showTyping() {
    var t = document.createElement('div');
    t.className = 'eg-typing';
    t.id = 'eg-typing';
    t.innerHTML = '<span></span><span></span><span></span>';
    messages.appendChild(t);
    messages.scrollTop = messages.scrollHeight;
  }

  function hideTyping() {
    var t = document.getElementById('eg-typing');
    if (t) t.remove();
  }

  function showError(msg) {
    var e = document.createElement('div');
    e.className = 'eg-error';
    e.textContent = msg;
    messages.appendChild(e);
    messages.scrollTop = messages.scrollHeight;
  }

  var contactKeywords = ['partner','partnership','poc','pilot','work with','work together','contact','pricing','price','cost','hire','procurement','buy','purchase','collaborate','interest','interested','demo'];

  function shouldNudge(text) {
    var lower = text.toLowerCase();
    return contactKeywords.some(function(k) { return lower.includes(k); });
  }

  // ── OPEN / CLOSE ──────────────────────────────────────────────────────────
  function openChat() {
    isOpen = true;
    panel.classList.add('open');
    btn.style.display = 'none';
    if (messages.children.length === 0) {
      addMessage('ai', 'Hi — I\'m E-Group\'s AI assistant. Ask me anything about our work, products, team, or history. What would you like to know?');
    }
    setTimeout(function() { input.focus(); }, 300);
  }

  function closeChat() {
    isOpen = false;
    panel.classList.remove('open');
    btn.style.display = 'flex';
  }

  btn.addEventListener('click', openChat);
  closeBtn.addEventListener('click', closeChat);

  // ── INPUT HANDLING ────────────────────────────────────────────────────────
  input.addEventListener('input', function() {
    sendBtn.disabled = !this.value.trim() || isLoading;
    this.style.height = 'auto';
    this.style.height = Math.min(this.scrollHeight, 80) + 'px';
  });

  input.addEventListener('keydown', function(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      if (!sendBtn.disabled) send();
    }
  });

  // ── SEND ──────────────────────────────────────────────────────────────────
  function send() {
    var text = input.value.trim();
    if (!text || isLoading) return;

    addMessage('user', text);
    history.push({ role: 'user', content: text });
    input.value = '';
    input.style.height = 'auto';
    sendBtn.disabled = true;
    isLoading = true;

    showTyping();

    fetch(ENDPOINT, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        model: 'claude-sonnet-4-20250514',
        max_tokens: 400,
        system: SYSTEM,
        messages: history
      })
    })
    .then(function(r) {
      if (!r.ok) throw new Error('API error ' + r.status);
      return r.json();
    })
    .then(function(data) {
      hideTyping();
      var reply = data.content && data.content[0] && data.content[0].text
        ? data.content[0].text
        : 'Sorry, I could not retrieve a response.';
      var nudge = shouldNudge(text) || shouldNudge(reply);
      addMessage('ai', reply, nudge);
      history.push({ role: 'assistant', content: reply });
    })
    .catch(function(err) {
      hideTyping();
      if (err.message.includes('Failed to fetch') || err.message.includes('NetworkError')) {
        showError('Could not connect to the local proxy. Make sure proxy2.js is running on port 3000.');
      } else {
        showError('Something went wrong. Please try again.');
      }
    })
    .finally(function() {
      isLoading = false;
      sendBtn.disabled = !input.value.trim();
    });
  }

  sendBtn.addEventListener('click', send);

})();
