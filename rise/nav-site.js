// E-Group Site Nav — single source of truth
// Usage: <script src="nav-site.js"></script> (from rise/ level)
//        <script src="../nav-site.js"></script> (from rise/record/ level)
// Add data-page="thinking" (or intelligence/rise/about/record) on <body> to highlight active link
// Add data-prefix="../" on <body> when loading from a subdirectory (e.g. record/)

(function() {
  const page   = document.body.dataset.page   || '';
  const prefix = document.body.dataset.prefix || '';

  // ── DROPDOWN CSS ──────────────────────────────────────────────────────
  const style = document.createElement('style');
  style.textContent = `
    .nav-dropdown { position:relative; }
    .nav-dropdown > a::after { content:''; position:absolute; bottom:-3px; left:0; right:0; height:1px; background:var(--gold); transform:scaleX(0); transition:transform 0.2s; }
    .nav-dropdown:hover > a, .nav-dropdown > a.active { color:var(--white); }
    .nav-dropdown:hover > a::after, .nav-dropdown > a.active::after { transform:scaleX(1); }
    .nav-drop-menu { display:none; position:absolute; top:100%; right:0; background:rgba(12,12,12,0.98); border:1px solid var(--border); border-top:2px solid var(--gold); min-width:240px; z-index:200; backdrop-filter:blur(16px); }
    .nav-dropdown::after { content:''; position:absolute; top:100%; left:0; right:0; height:20px; }
    .nav-dropdown:hover .nav-drop-menu { display:block; }
    .nav-drop-item { display:block; padding:11px 20px; font-family:'DM Mono',monospace; font-size:10px; letter-spacing:1.5px; text-transform:uppercase; color:var(--dim); text-decoration:none; transition:all 0.15s; border-bottom:1px solid var(--border); white-space:nowrap; }
    .nav-drop-item:last-child { border-bottom:none; }
    .nav-drop-item:hover { color:var(--gold); background:rgba(200,169,110,0.05); padding-left:26px; }
    #site-nav { padding:0 60px !important; height:72px !important; }
    #site-nav .nav-links { gap:40px; }
    .nav-drop-label { display:block; padding:8px 20px 4px; font-family:'DM Mono',monospace; font-size:8px; letter-spacing:2px; text-transform:uppercase; color:var(--muted); border-bottom:1px solid var(--border); }
    .mob-main { font-family:'Syne',sans-serif; font-weight:800; font-size:clamp(26px,7vw,40px); color:var(--white); text-decoration:none; letter-spacing:-0.5px; padding:9px 0; width:80%; text-align:center; transition:color 0.2s; border-bottom:none; display:block; }
    .mob-main:hover { color:var(--gold); }
    .mob-divider { font-family:'DM Mono',monospace; font-size:9px; letter-spacing:3px; text-transform:uppercase; color:var(--dim); padding:20px 0 6px; width:80%; border-bottom:1px solid var(--border); text-align:center; margin-bottom:4px; }
    .mob-record { font-family:'DM Mono',monospace; font-size:11px; letter-spacing:1.5px; text-transform:uppercase; color:var(--mid); text-decoration:none; padding:7px 0; width:80%; text-align:center; transition:color 0.2s; border-bottom:none; display:block; }
    .mob-record:hover, .mob-record.active { color:var(--gold); }
    .mob-cta { font-family:'DM Mono',monospace; font-size:12px; letter-spacing:2px; text-transform:uppercase; color:var(--black); background:var(--gold); padding:14px 36px; font-weight:400; margin-top:20px; border-bottom:none; text-decoration:none; display:block; }
  `;
  document.head.appendChild(style);

  // ── NAV HTML ──────────────────────────────────────────────────────────
  const nav = document.createElement('nav');
  nav.id = 'site-nav';
  nav.innerHTML = `
    <a href="${prefix}index.html" class="nav-logo">
      <div class="logo-e">E</div>
      <span class="nav-logo-text">E-Group</span>
    </a>
    <ul class="nav-links">
      <li><a href="${prefix}intelligence.html" data-nav="intelligence">Intelligence</a></li>
      <li><a href="${prefix}rise.html"         data-nav="rise">Rise</a></li>
      <li><a href="${prefix}thinking.html"     data-nav="thinking">Thinking</a></li>
      <li><a href="${prefix}about.html"        data-nav="about">About</a></li>
      <li class="nav-dropdown">
        <a href="${prefix}record/index.html" data-nav="record">Record</a>
        <div class="nav-drop-menu">
          <span class="nav-drop-label">Projects &amp; Credentials</span>
          <a href="${prefix}record/ipcei-cis.html"   class="nav-drop-item">IPCEI-CIS — FedEU.ai</a>
          <a href="${prefix}record/kau.html"          class="nav-drop-item">KAÜ — National Identity</a>
          <a href="${prefix}record/helix.html"        class="nav-drop-item">HeliX + FedX</a>
          <a href="${prefix}record/eidas.html"        class="nav-drop-item">eIDAS 2.0 — MyD Wallet</a>
          <a href="${prefix}record/medical-ai.html"   class="nav-drop-item">Medical AI — GRaDPaLM</a>
          <a href="${prefix}record/peter-antal.html"  class="nav-drop-item">Dr. Péter Antal</a>
          <span class="nav-drop-label">Media</span>
          <a href="${prefix}record/press.html"        class="nav-drop-item">Press Kit</a>
        </div>
      </li>
    </ul>
    <a href="${prefix}index.html#contact" class="nav-cta">Work With Us</a>
    <button class="nav-hamburger" id="site-nav-hamburger" aria-label="Menu">
      <span></span><span></span><span></span>
    </button>
  `;

  // ── MOBILE MENU HTML ──────────────────────────────────────────────────
  const mobileMenu = document.createElement('div');
  mobileMenu.className = 'nav-mobile-menu';
  mobileMenu.id = 'site-nav-mobile';
  mobileMenu.innerHTML = `
    <a href="${prefix}index.html"        class="mob-main">Home</a>
    <a href="${prefix}intelligence.html" class="mob-main">Intelligence</a>
    <a href="${prefix}rise.html"         class="mob-main">Rise</a>
    <a href="${prefix}thinking.html"     class="mob-main">Thinking</a>
    <a href="${prefix}about.html"        class="mob-main">About</a>
    <div class="mob-divider">The Record</div>
    <a href="${prefix}record/index.html"          class="mob-record">Record Home</a>
    <a href="${prefix}record/ipcei-cis.html"      class="mob-record">IPCEI-CIS — FedEU.ai</a>
    <a href="${prefix}record/kau.html"            class="mob-record">KAÜ — National Identity</a>
    <a href="${prefix}record/helix.html"          class="mob-record">HeliX + FedX</a>
    <a href="${prefix}record/eidas.html"          class="mob-record">eIDAS 2.0 — MyD Wallet</a>
    <a href="${prefix}record/medical-ai.html"     class="mob-record">Medical AI — GRaDPaLM</a>
    <a href="${prefix}record/peter-antal.html"    class="mob-record">Dr. Péter Antal</a>
    <a href="${prefix}record/press.html"          class="mob-record">Press Kit</a>
    <a href="${prefix}index.html#contact"         class="mob-cta">Work With Us</a>
  `;

  // ── HIGHLIGHT ACTIVE PAGE ─────────────────────────────────────────────
  if (page) {
    const active = nav.querySelector(`[data-nav="${page}"]`);
    if (active) active.classList.add('active');
    // Also highlight mob-record links if on a record page
    const mobActive = mobileMenu.querySelector(`a[href*="${page}"]`);
    if (mobActive) mobActive.classList.add('active');
  }

  // ── INSERT INTO DOM ───────────────────────────────────────────────────
  document.body.insertBefore(mobileMenu, document.body.firstChild);
  document.body.insertBefore(nav, document.body.firstChild);

  // ── HAMBURGER LOGIC ───────────────────────────────────────────────────
  const hamburger = document.getElementById('site-nav-hamburger');
  hamburger.addEventListener('click', () => {
    hamburger.classList.toggle('open');
    mobileMenu.classList.toggle('open');
    document.body.style.overflow = mobileMenu.classList.contains('open') ? 'hidden' : '';
  });
  mobileMenu.querySelectorAll('a').forEach(a => {
    a.addEventListener('click', () => {
      hamburger.classList.remove('open');
      mobileMenu.classList.remove('open');
      document.body.style.overflow = '';
    });
  });

  // ── CURSOR HOVER ON NAV ───────────────────────────────────────────────
  nav.addEventListener('mouseenter', () => {
    const ring = document.getElementById('cursorRing');
    if (ring) { ring.style.width = '48px'; ring.style.height = '48px'; }
  });

})();
