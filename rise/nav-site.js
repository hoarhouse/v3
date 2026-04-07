// E-Group Site Nav — single source of truth
// Usage: <script src="../nav-site.js"></script> or <script src="nav-site.js"></script>
// Add data-page="thinking" (or intelligence/rise/about) on <body> to highlight active link

(function() {
  const page = document.body.dataset.page || '';

  const nav = document.createElement('nav');
  nav.id = 'site-nav';
  nav.innerHTML = `
    <a href="index.html" class="nav-logo">
      <div class="logo-e">E</div>
      <span class="nav-logo-text">E-Group</span>
    </a>
    <ul class="nav-links">
      <li><a href="intelligence.html" data-nav="intelligence">Intelligence</a></li>
      <li><a href="rise.html" data-nav="rise">Rise</a></li>
      <li><a href="thinking.html" data-nav="thinking">Thinking</a></li>
      <li><a href="about.html" data-nav="about">About</a></li>
    </ul>
    <a href="index.html#contact" class="nav-cta">Work With Us</a>
  `;

  // Highlight active page
  if (page) {
    const active = nav.querySelector(`[data-nav="${page}"]`);
    if (active) active.classList.add('active');
  }

  // Insert as first child of body
  document.body.insertBefore(nav, document.body.firstChild);

  // Cursor tracking for nav hover
  const navEl = document.getElementById('site-nav');
  navEl.addEventListener('mouseenter', () => {
    const ring = document.getElementById('cursorRing');
    if (ring) { ring.style.width = '48px'; ring.style.height = '48px'; }
  });
})();
