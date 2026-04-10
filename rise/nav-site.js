(function() {
  var path = window.location.pathname;
  var inRecord = path.includes('/record/');
  var base = inRecord ? '../' : '';
  var current = path.split('/').pop() || 'index.html';
  function active(page) { return current === page ? 'color:#C8A96E;' : ''; }

  var navHtml = '<style>' +
    '@media(max-width:768px){.nav-desktop{display:none!important;}.nav-hamburger{display:flex!important;}}' +
    '.nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px;}' +
    '.nav-hamburger span{display:block;width:22px;height:1px;background:#EFEFEF;transition:all 0.3s;}' +
    '.nav-hamburger.open span:nth-child(1){transform:rotate(45deg) translate(4px,4px);}' +
    '.nav-hamburger.open span:nth-child(2){opacity:0;}' +
    '.nav-hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(4px,-4px);}' +
    '.mob-menu{display:none;position:fixed;inset:0;background:rgba(8,8,8,0.98);z-index:999;flex-direction:column;padding:100px 32px 40px;gap:0;overflow-y:auto;}' +
    '.mob-menu.open{display:flex;}' +
    '.mob-main{font-family:Syne,sans-serif;font-size:28px;font-weight:700;color:#EFEFEF;text-decoration:none;padding:16px 0;border-bottom:1px solid #1a1a1a;}' +
    '.mob-divider{font-family:"DM Mono",monospace;font-size:10px;letter-spacing:2px;color:#333;padding:20px 0 8px;text-transform:uppercase;}' +
    '.mob-record{font-family:"DM Sans",sans-serif;font-size:15px;color:#555;text-decoration:none;padding:10px 0;border-bottom:1px solid #1a1a1a;}' +
    '.mob-cta{margin-top:32px;font-family:"DM Mono",monospace;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#EFEFEF;text-decoration:none;padding:14px 24px;border:1px solid #EFEFEF;text-align:center;}' +
    '.ndrop{display:none;position:absolute;top:100%;left:0;background:#0A0A0A;border:1px solid #1a1a1a;border-top:2px solid #C8A96E;min-width:240px;padding:8px 0;z-index:999;}' +
    '.nav-rec:hover .ndrop{display:block;}' +
    '.site-footer{background:#050505;border-top:1px solid #1a1a1a;padding:64px 60px 0;}' +
    '.site-footer-grid{display:grid;grid-template-columns:1.5fr 1fr 1fr 1fr;gap:48px;padding-bottom:48px;border-bottom:1px solid #1a1a1a;}' +
    '.site-footer-brand-logo{display:flex;align-items:center;gap:10px;margin-bottom:16px;text-decoration:none;}' +
    '.site-footer-brand-logo .logo-e{width:28px;height:28px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:14px;flex-shrink:0;}' +
    '.site-footer-brand-logo span{font-family:Syne,sans-serif;font-weight:700;font-size:14px;color:#EFEFEF;letter-spacing:1px;}' +
    '.site-footer-brand-desc{font-size:13px;color:#555;line-height:1.6;margin-bottom:20px;max-width:240px;}' +
    '.site-footer-social{display:flex;gap:12px;}' +
    '.site-footer-social a{font-family:"DM Mono",monospace;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:#555;text-decoration:none;padding:6px 12px;border:1px solid #1a1a1a;transition:color 0.2s,border-color 0.2s;}' +
    '.site-footer-social a:hover{color:#C8A96E;border-color:rgba(200,169,110,0.4);}' +
    '.site-footer-col-title{font-family:"DM Mono",monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#555;margin-bottom:20px;}' +
    '.site-footer-links{display:flex;flex-direction:column;gap:10px;}' +
    '.site-footer-links a{font-size:13px;color:#666;text-decoration:none;transition:color 0.2s;line-height:1.4;}' +
    '.site-footer-links a:hover{color:#EFEFEF;}' +
    '.site-footer-contact-line{font-size:13px;color:#555;margin-bottom:6px;line-height:1.5;}' +
    '.site-footer-contact-cta{display:inline-block;margin-top:16px;font-family:"DM Mono",monospace;font-size:10px;letter-spacing:1.5px;text-transform:uppercase;color:#C8A96E;text-decoration:none;border-bottom:1px solid rgba(200,169,110,0.3);padding-bottom:2px;transition:border-color 0.2s;}' +
    '.site-footer-contact-cta:hover{border-color:#C8A96E;}' +
    '.site-footer-bottom{padding:20px 0;display:flex;align-items:center;justify-content:space-between;gap:16px;flex-wrap:wrap;}' +
    '.site-footer-legal{font-family:"DM Mono",monospace;font-size:10px;color:#333;letter-spacing:0.5px;}' +
    '@media(max-width:1023px){.site-footer-grid{grid-template-columns:1fr 1fr;gap:40px;}}' +
    '@media(max-width:768px){' +
    '.site-footer{padding:48px 24px 0;}' +
    '.site-footer-grid{grid-template-columns:1fr;gap:36px;}' +
    '.site-footer-bottom{flex-direction:column;align-items:flex-start;gap:8px;}' +
    '}' +
  '</style>' +

  '<nav style="position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:20px 48px;background:rgba(8,8,8,0.97);backdrop-filter:blur(8px);border-bottom:1px solid #1a1a1a;">' +
    '<a href="' + base + 'index.html" style="display:flex;align-items:center;gap:12px;text-decoration:none;">' +
      '<div class="logo-e" style="width:28px;height:28px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:14px;">E</div>' +
      '<span style="font-family:Syne,sans-serif;font-weight:700;font-size:14px;color:#EFEFEF;letter-spacing:1px;">E-Group</span>' +
    '</a>' +
    '<div class="nav-desktop" style="display:flex;align-items:center;gap:36px;">' +
      '<a href="' + base + 'intelligence.html" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('intelligence.html') + '">The Work</a>' +
      '<a href="' + base + 'rise.html" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('rise.html') + '">What\'s Next</a>' +
      '<a href="' + base + 'thinking.html" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('thinking.html') + '">Thinking</a>' +
      '<a href="' + base + 'about.html" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('about.html') + '">About</a>' +
      '<div class="nav-rec" style="position:relative;">' +
        '<a href="' + base + 'record/index.html" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;cursor:pointer;">Record ▾</a>' +
        '<div class="ndrop">' +
          '<a href="' + base + 'record/index.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Overview</a>' +
          '<a href="' + base + 'record/mavir.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">MAVIR — Electricity Grid</a>' +
          '<a href="' + base + 'record/ipcei-cis.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">IPCEI-CIS — FedEU.ai</a>' +
          '<a href="' + base + 'record/kau.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">KAÜ — National Identity</a>' +
          '<a href="' + base + 'record/helix.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">HeliX + FedX</a>' +
          '<a href="' + base + 'record/eidas.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">eIDAS 2.0 — MyD Wallet</a>' +
          '<a href="' + base + 'record/medical-ai.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Medical AI — GRaDPaLM</a>' +
          '<a href="' + base + 'record/peter-antal.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Dr. Péter Antal</a>' +
          '<a href="' + base + 'record/press.html" style="display:block;padding:10px 18px;font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Press Kit</a>' +
        '</div>' +
      '</div>' +
    '</div>' +
    '<a href="' + base + 'index.html#contact" class="nav-desktop" style="font-family:\'DM Mono\',monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#C8A96E;border:1px solid rgba(200,169,110,0.4);padding:10px 20px;text-decoration:none;">Work With Us</a>' +
    '<button class="nav-hamburger" id="egroup-hamburger" aria-label="Menu"><span></span><span></span><span></span></button>' +
  '</nav>' +
  '<div style="height:72px;"></div>' +

  '<div class="mob-menu" id="egroup-mobile-menu">' +
    '<a href="' + base + 'index.html" class="mob-main">Home</a>' +
    '<a href="' + base + 'intelligence.html" class="mob-main">The Work</a>' +
    '<a href="' + base + 'rise.html" class="mob-main">What\'s Next</a>' +
    '<a href="' + base + 'thinking.html" class="mob-main">Thinking</a>' +
    '<a href="' + base + 'about.html" class="mob-main">About</a>' +
    '<div class="mob-divider">The Record</div>' +
    '<a href="' + base + 'record/index.html" class="mob-record">Overview</a>' +
    '<a href="' + base + 'record/mavir.html" class="mob-record">MAVIR — Electricity Grid</a>' +
    '<a href="' + base + 'record/ipcei-cis.html" class="mob-record">IPCEI-CIS — FedEU.ai</a>' +
    '<a href="' + base + 'record/kau.html" class="mob-record">KAÜ — National Identity</a>' +
    '<a href="' + base + 'record/helix.html" class="mob-record">HeliX + FedX</a>' +
    '<a href="' + base + 'record/eidas.html" class="mob-record">eIDAS 2.0 — MyD Wallet</a>' +
    '<a href="' + base + 'record/medical-ai.html" class="mob-record">Medical AI — GRaDPaLM</a>' +
    '<a href="' + base + 'record/peter-antal.html" class="mob-record">Dr. Péter Antal</a>' +
    '<a href="' + base + 'record/press.html" class="mob-record">Press Kit</a>' +
    '<a href="' + base + 'index.html#contact" class="mob-cta">Work With Us</a>' +
  '</div>';

  var footerHtml =
  '<footer class="site-footer">' +
    '<div class="site-footer-grid">' +

      '<div>' +
        '<a href="' + base + 'index.html" class="site-footer-brand-logo">' +
          '<div class="logo-e">E</div>' +
          '<span>E-Group</span>' +
        '</a>' +
        '<p class="site-footer-brand-desc">Intelligence infrastructure for enterprises that understand what AI actually runs on. Built in Budapest since 1993.</p>' +
        '<div class="site-footer-social">' +
          '<a href="https://www.linkedin.com/company/e-group-ict-group/" target="_blank" rel="noopener">LinkedIn</a>' +
        '</div>' +
      '</div>' +

      '<div>' +
        '<div class="site-footer-col-title">Navigate</div>' +
        '<div class="site-footer-links">' +
          '<a href="' + base + 'intelligence.html">The Work</a>' +
          '<a href="' + base + 'rise.html">What\'s Next</a>' +
          '<a href="' + base + 'thinking.html">Thinking</a>' +
          '<a href="' + base + 'about.html">About</a>' +
          '<a href="' + base + 'index.html#contact">Work With Us</a>' +
        '</div>' +
      '</div>' +

      '<div>' +
        '<div class="site-footer-col-title">The Record</div>' +
        '<div class="site-footer-links">' +
          '<a href="' + base + 'record/kau.html">KAÜ — National Identity</a>' +
          '<a href="' + base + 'record/helix.html">HeliX + FedX</a>' +
          '<a href="' + base + 'record/ipcei-cis.html">IPCEI-CIS</a>' +
          '<a href="' + base + 'record/eidas.html">eIDAS 2.0</a>' +
          '<a href="' + base + 'record/medical-ai.html">Medical AI</a>' +
          '<a href="' + base + 'record/index.html">Full Record →</a>' +
        '</div>' +
      '</div>' +

      '<div>' +
        '<div class="site-footer-col-title">Contact</div>' +
        '<p class="site-footer-contact-line">Budapest, Hungary</p>' +
        '<p class="site-footer-contact-line">E-Group ICT Software Zrt.</p>' +
        '<p class="site-footer-contact-line">Est. 1993 · 90+ staff</p>' +
        '<a href="' + base + 'index.html#contact" class="site-footer-contact-cta">Working on something? Tell us →</a>' +
      '</div>' +

    '</div>' +
    '<div class="site-footer-bottom">' +
      '<div class="site-footer-legal">© 2026 E-Group ICT Software Zrt. All rights reserved.</div>' +
      '<div class="site-footer-legal">Budapest, Hungary · Intelligence Infrastructure</div>' +
    '</div>' +
  '</footer>';

  // Insert nav at top of body
  document.body.insertAdjacentHTML('afterbegin', navHtml);

  // Replace footer after page fully loaded
  window.addEventListener('load', function() {
    var existingFooter = document.querySelector('footer');
    if (existingFooter) {
      existingFooter.outerHTML = footerHtml;
    } else {
      document.body.insertAdjacentHTML('beforeend', footerHtml);
    }
  });

  // Hamburger toggle
  var btn = document.getElementById('egroup-hamburger');
  var menu = document.getElementById('egroup-mobile-menu');
  if (btn && menu) {
    btn.addEventListener('click', function() {
      btn.classList.toggle('open');
      menu.classList.toggle('open');
      document.body.style.overflow = menu.classList.contains('open') ? 'hidden' : '';
    });
    menu.querySelectorAll('a').forEach(function(a) {
      a.addEventListener('click', function() {
        btn.classList.remove('open');
        menu.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }
})();
