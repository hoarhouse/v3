(function() {
  var path = window.location.pathname;
  var inRecord = path.includes('/record/');
  var base = inRecord ? '../' : '';
  var current = path.split('/').pop() || 'index.html';
  function active(page) { return current === page ? 'color:#C8A96E;' : ''; }

  var html = '<nav style="position:fixed;top:0;left:0;right:0;z-index:1000;display:flex;align-items:center;justify-content:space-between;padding:20px 48px;background:rgba(8,8,8,0.97);backdrop-filter:blur(8px);border-bottom:1px solid #1a1a1a;">' +
    '<a href="' + base + 'index.html" style="display:flex;align-items:center;gap:12px;text-decoration:none;">' +
      '<div style="width:28px;height:28px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:14px;">E</div>' +
      '<span style="font-family:Syne,sans-serif;font-weight:700;font-size:14px;color:#EFEFEF;letter-spacing:1px;">E-Group</span>' +
    '</a>' +
    '<div style="display:flex;align-items:center;gap:36px;">' +
      '<a href="' + base + 'intelligence.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('intelligence.html') + '">The Work</a>' +
      '<a href="' + base + 'rise.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('rise.html') + '">What\'s Next</a>' +
      '<a href="' + base + 'thinking.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('thinking.html') + '">Thinking</a>' +
      '<a href="' + base + 'about.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;' + active('about.html') + '">About</a>' +
      '<div style="position:relative;" onmouseenter="this.querySelector(\'.ndrop\').style.display=\'block\'" onmouseleave="this.querySelector(\'.ndrop\').style.display=\'none\'">' +
        '<a href="' + base + 'record/index.html" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;text-decoration:none;color:#777;cursor:pointer;">Record ▾</a>' +
        '<div class="ndrop" style="display:none;position:absolute;top:100%;left:0;background:#0A0A0A;border:1px solid #1a1a1a;border-top:2px solid #C8A96E;min-width:240px;padding:8px 0;z-index:999;">' +
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
    '<a href="' + base + 'index.html#contact" style="font-family:DM Mono,monospace;font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#C8A96E;border:1px solid rgba(200,169,110,0.4);padding:10px 20px;text-decoration:none;">Work With Us</a>' +
  '</nav>' +
  '<div style="height:72px;"></div>';

  document.body.insertAdjacentHTML('afterbegin', html);
})();
