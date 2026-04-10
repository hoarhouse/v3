(function() {
  var path = window.location.pathname;
  var inRecord = path.includes('/record/');
  var base = inRecord ? '../' : '';
  var current = path.split('/').pop() || 'index.html';
  function a(page) { return current === page ? ' class="active"' : ''; }

  var html = '<nav style="position:fixed;top:0;left:0;right:0;z-index:100;display:flex;align-items:center;justify-content:space-between;padding:24px 48px;background:rgba(8,8,8,0.97);backdrop-filter:blur(8px);border-bottom:1px solid #1a1a1a;font-family:DM Mono,monospace;">' +
    '<a href="' + base + 'index.html" style="display:flex;align-items:center;gap:12px;text-decoration:none;">' +
      '<div style="width:28px;height:28px;background:#C8A96E;color:#080808;display:flex;align-items:center;justify-content:center;font-family:Syne,sans-serif;font-weight:800;font-size:14px;">E</div>' +
      '<span style="font-family:Syne,sans-serif;font-weight:700;font-size:14px;color:#EFEFEF;letter-spacing:1px;">E-Group</span>' +
    '</a>' +
    '<div style="display:flex;align-items:center;gap:32px;">' +
      '<a href="' + base + 'intelligence.html"' + a('intelligence.html') + ' style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#777;text-decoration:none;">The Work</a>' +
      '<a href="' + base + 'rise.html"' + a('rise.html') + ' style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#777;text-decoration:none;">What\'s Next</a>' +
      '<a href="' + base + 'thinking.html"' + a('thinking.html') + ' style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#777;text-decoration:none;">Thinking</a>' +
      '<a href="' + base + 'about.html"' + a('about.html') + ' style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#777;text-decoration:none;">About</a>' +
      '<a href="' + base + 'record/index.html" style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#777;text-decoration:none;">Record</a>' +
    '</div>' +
    '<a href="' + base + 'index.html#contact" style="font-size:11px;letter-spacing:1.5px;text-transform:uppercase;color:#C8A96E;border:1px solid rgba(200,169,110,0.4);padding:10px 20px;text-decoration:none;">Work With Us</a>' +
  '</nav>' +
  '<div style="height:76px;"></div>';

  document.body.insertAdjacentHTML('afterbegin', html);
})();
