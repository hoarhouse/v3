(function() {
  const currentPage = window.location.pathname.split('/').pop() || 'briefing.html';

  const nav = document.createElement('div');
  nav.id = 'vigil-topbar';
  nav.style.cssText = 'background:#0A0A0A;border-bottom:1px solid #1A1A1A;padding:0 32px;display:flex;align-items:center;justify-content:space-between;height:52px;position:sticky;top:0;z-index:100;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Arial,sans-serif';

  const links = [
    { href: 'briefing.html', label: 'Briefing' },
    { href: 'network.html',  label: 'Network' },
    { href: 'intelligence.html', label: 'Intelligence' },
    { href: 'pipeline.html', label: 'Pipeline' },
  ];

  const navLinks = links.map(l => {
    const active = currentPage === l.href;
    return `<a href="${l.href}" style="padding:6px 12px;font-size:12px;letter-spacing:1px;text-transform:uppercase;color:${active ? '#C8A96E' : '#555'};text-decoration:none;border-radius:4px;transition:color 0.2s" onmouseover="this.style.color='${active ? '#C8A96E' : '#999'}'" onmouseout="this.style.color='${active ? '#C8A96E' : '#555'}'">${l.label}</a>`;
  }).join('');

  nav.innerHTML = `
    <div style="display:flex;align-items:center;gap:24px">
      <div>
        <div style="font-size:18px;font-weight:900;color:#C8A96E;letter-spacing:-0.5px;line-height:1.1">VIGIL</div>
        <div style="font-size:9px;letter-spacing:3px;text-transform:uppercase;color:#444">E-Group Intelligence</div>
      </div>
      <nav style="display:flex;gap:4px">${navLinks}</nav>
    </div>
    <div id="vigil-nav-right"></div>
  `;

  document.body.insertBefore(nav, document.body.firstChild);
  // Hide any legacy header elements from old page versions
  const legacyHeader = document.querySelector('.header');
  if (legacyHeader) legacyHeader.style.display = 'none';
})();