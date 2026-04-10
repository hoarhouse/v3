(function() {
  var path = window.location.pathname;
  var inRecord = path.includes('/record/');
  var base = inRecord ? '../' : '';
  var current = path.split('/').pop() || 'index.html';
  function active(page) { return current === page ? 'color:#C8A96E;' : ''; }

  var html = '<style>' +
    '@media(max-width:768px){.nav-desktop{display:none!important;}.nav-hamburger{display:flex!important;}}' +
    '.nav-hamburger{display:none;flex-direction:column;gap:5px;cursor:pointer;background:none;border:none;padding:4px;}' +
    '.nav-hamburger span{display:block;width:22px;height:1px;background:#EFEFEF;transition:all 0.3s;}' +
    '.nav-hamburger.open span:nth-child(1){transform:rotate(45deg) translate(4px,4px);}' +
    '.nav-hamburger.open span:nth-child(2){opacity:0;}' +
    '.nav-hamburger.open span:nth-child(3){transform:rotate(-45deg) translate(4px,-4px);}' +
    '.mob-menu{display:none;position:fixed;inset:0;background:rgba(8,8,8,0.98);z-index:999;flex-direction:column;align-items:center;justify-content:center;padding:40px 32px;gap:0;}' +
    '.mob-menu.open{display:flex;}' +
    '.mob-main{font-family:Syne,sans-serif;font-size:28px;font-weight:700;color:#EFEFEF;text-decoration:none;padding:16px 0;border-bottom:1px solid #1a1a1a;width:100%;text-align:center;}' +
    '.mob-divider{font-family:DM Mono,monospace;font-size:10px;letter-spacing:2px;color:#333;padding:20px 0 8px;text-transform:uppercase;}' +
    '.mob-record{font-family:DM Sans,sans-serif;font-size:15px;color:#555;text-decoration:none;padding:10px 0;border-bottom:1px solid #1a1a1a;}' +
    '.mob-cta{margin-top:32px;font-family:DM Mono,monospace;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:#EFEFEF;text-decoration:none;padding:14px 24px;border:1px solid #EFEFEF;text-align:center;}' +
    '.ndrop{display:none;position:absolute;top:100%;left:0;background:#0A0A0A;border:1px solid #1a1a1a;border-top:2px solid #C8A96E;min-width:240px;padding:8px 0;z-index:999;}' +
    '.nav-rec:hover .ndrop{display:block;}' +
  '</style>' +

  '<nav style="position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:20px 48px;background:rgba(8,8,8,0.97);backdrop-filter:blur(8px);border-bottom:1px solid #1a1a1a;">' +
    '<a href="' + base + 'index.html" style="display:flex;align-items:center;gap:12px;text-decoration:none;">' +
      '<div style="width:28px;height:28px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:14px;">E</div>' +
      '<span style="font-family:Syne,sans-serif;font-weight:700;font-size:14px;color:#EFEFEF;letter-spacing:1px;">E-Group</span>' +
    '</a>' +
    '<div class="nav-desktop" style="display:flex;align-items:center;gap:36px;">' +
      '<a href="' + base + 'intelligence.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('intelligence.html') + '">The Work</a>' +
      '<a href="' + base + 'rise.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('rise.html') + '">What\'s Next</a>' +
      '<a href="' + base + 'thinking.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('thinking.html') + '">Thinking</a>' +
      '<a href="' + base + 'about.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('about.html') + '">About</a>' +
      '<div class="nav-rec" style="position:relative;">' +
        '<a href="' + base + 'record/index.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;cursor:pointer;">Record ▾</a>' +
        '<div class="ndrop">' +
          '<a href="' + base + 'record/index.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Overview</a>' +
          '<a href="' + base + 'record/ipcei-cis.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">IPCEI-CIS — FedEU.ai</a>' +
          '<a href="' + base + 'record/kau.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">KAÜ — National Identity</a>' +
          '<a href="' + base + 'record/helix.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">HeliX + FedX</a>' +
          '<a href="' + base + 'record/eidas.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">eIDAS 2.0 — MyD Wallet</a>' +
          '<a href="' + base + 'record/medical-ai.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Medical AI — GRaDPaLM</a>' +
          '<a href="' + base + 'record/peter-antal.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Dr. Péter Antal</a>' +
          '<a href="' + base + 'record/press.html" style="display:block;padding:10px 18px;font-family:DM Mono,monospace;font-size:10px;letter-spacing:1px;text-transform:uppercase;color:#666;text-decoration:none;">Press Kit</a>' +
        '</div>' +
      '</div>' +
    '</div>' +
    '<a href="' + base + 'index.html#contact" class="nav-desktop" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#C8A96E;border:1px solid rgba(200,169,110,0.4);padding:10px 20px;text-decoration:none;">Work With Us</a>' +
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
    '<a href="' + base + 'record/ipcei-cis.html" class="mob-record">IPCEI-CIS — FedEU.ai</a>' +
    '<a href="' + base + 'record/kau.html" class="mob-record">KAÜ — National Identity</a>' +
    '<a href="' + base + 'record/helix.html" class="mob-record">HeliX + FedX</a>' +
    '<a href="' + base + 'record/eidas.html" class="mob-record">eIDAS 2.0 — MyD Wallet</a>' +
    '<a href="' + base + 'record/medical-ai.html" class="mob-record">Medical AI — GRaDPaLM</a>' +
    '<a href="' + base + 'record/peter-antal.html" class="mob-record">Dr. Péter Antal</a>' +
    '<a href="' + base + 'record/press.html" class="mob-record">Press Kit</a>' +
    '<a href="' + base + 'index.html#contact" class="mob-cta">Work With Us</a>' +
  '</div>';

  document.body.insertAdjacentHTML('afterbegin', html);

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
