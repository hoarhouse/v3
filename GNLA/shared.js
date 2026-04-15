/* ═══════════════════════════════════════════════════
   GNLA SHARED JS — nav inject, footer inject,
   hamburger, scroll, reveal
════════════════════════════════════════════════════ */
(function(){

  /* ── Inject Nav ── */
  const NAV_HTML = `
<nav id="gnla-nav" class="always-solid">
  <a href="index.html" class="nav-brand"><span class="nav-brand-top">GNLA</span><span class="nav-brand-sub">Global Nobel Laureates Assembly</span></a>
  <ul class="nav-desktop">
    <li><a href="about.html">About <span class="caret">▾</span></a><div class="nav-dropdown"><a href="about.html">The Assembly</a><a href="rome-declaration.html">The Rome Declaration</a><a href="institutions.html">Institutions &amp; Partners</a></div></li>
    <li><a href="speakers.html">Speakers</a></li>
    <li><a href="programme.html">Programme</a></li>
    <li><a href="venue.html">Venue</a></li>
    <li><a href="news.html">Media <span class="caret">▾</span></a><div class="nav-dropdown"><a href="news.html">News &amp; Updates</a><a href="media.html">Press &amp; Media Kit</a></div></li>
    <li><a href="faq.html">FAQ</a></li>
  </ul>
  <a href="register.html" class="nav-cta">Accept Invitation</a>
  <button class="nav-hamburger" id="gnla-burger" aria-label="Menu"><span></span><span></span><span></span></button>
</nav>
<div class="nav-drawer" id="gnla-drawer">
  <div class="nav-drawer-inner">
    <div class="drawer-section"><span class="drawer-section-label">About</span><a href="about.html" class="drawer-link">The Assembly</a><a href="rome-declaration.html" class="drawer-link">The Rome Declaration</a><a href="institutions.html" class="drawer-link">Institutions &amp; Partners</a></div>
    <div class="drawer-section"><span class="drawer-section-label">Event</span><a href="speakers.html" class="drawer-link">Speakers &amp; Participants</a><a href="programme.html" class="drawer-link">Programme</a><a href="venue.html" class="drawer-link">Venue</a></div>
    <div class="drawer-section"><span class="drawer-section-label">Media &amp; Info</span><a href="news.html" class="drawer-link">News &amp; Updates</a><a href="media.html" class="drawer-link">Press &amp; Media Kit</a><a href="faq.html" class="drawer-link">FAQ</a><a href="contact.html" class="drawer-link">Contact</a></div>
    <a href="register.html" class="drawer-cta">Accept Invitation</a>
  </div>
</div>`;

  /* ── Inject Footer ── */
  const FOOTER_HTML = `
<footer id="gnla-footer">
  <div class="footer-top">
    <div class="footer-brand-col"><div class="footer-brand-name">Global Nobel Laureates Assembly on Artificial Intelligence and Nuclear War</div><div class="footer-brand-meta">Borgo Laudato Si' · Castel Gandolfo, Vatican<br>14–16 July 2026<br>Organized by Domus Communis Foundation</div></div>
    <div><span class="footer-col-title">About</span><ul class="footer-col-links"><li><a href="about.html">The Assembly</a></li><li><a href="rome-declaration.html">The Rome Declaration</a></li><li><a href="institutions.html">Institutions &amp; Partners</a></li></ul></div>
    <div><span class="footer-col-title">Event</span><ul class="footer-col-links"><li><a href="speakers.html">Speakers &amp; Participants</a></li><li><a href="programme.html">Programme</a></li><li><a href="venue.html">Venue</a></li></ul></div>
    <div><span class="footer-col-title">Engage</span><ul class="footer-col-links"><li><a href="register.html">Accept Invitation</a></li><li><a href="news.html">News &amp; Updates</a></li><li><a href="media.html">Press &amp; Media</a></li><li><a href="faq.html">FAQ</a></li><li><a href="contact.html">Contact</a></li></ul></div>
  </div>
  <div class="footer-bottom"><span class="footer-copy">© 2026 Domus Communis Foundation · All rights reserved · Confidential</span><ul class="footer-legal"><li><a href="#">Privacy Policy</a></li><li><a href="#">Terms of Use</a></li><li><a href="contact.html">Contact</a></li></ul></div>
</footer>`;

  /* ── Insert nav before body content ── */
  document.body.insertAdjacentHTML('afterbegin', NAV_HTML);

  /* ── Insert footer at end of body ── */
  document.body.insertAdjacentHTML('beforeend', FOOTER_HTML);

  /* ── Homepage: nav transparent on load ── */
  const nav = document.getElementById('gnla-nav');
  const isHome = (window.location.pathname.split('/').pop() || 'index.html') === 'index.html';
  if(isHome){
    nav.classList.remove('always-solid');
    const onScroll = () => nav.classList.toggle('solid', window.scrollY > 50);
    window.addEventListener('scroll', onScroll, {passive:true});
    onScroll();
  }

  /* ── Hamburger ── */
  const burger = document.getElementById('gnla-burger');
  const drawer = document.getElementById('gnla-drawer');
  if(burger && drawer){
    burger.addEventListener('click', () => {
      const open = burger.classList.toggle('open');
      drawer.classList.toggle('open', open);
      document.body.style.overflow = open ? 'hidden' : '';
    });
    drawer.querySelectorAll('a').forEach(a => {
      a.addEventListener('click', () => {
        burger.classList.remove('open');
        drawer.classList.remove('open');
        document.body.style.overflow = '';
      });
    });
  }

  /* ── Active nav link ── */
  const currentPage = window.location.pathname.split('/').pop() || 'index.html';
  document.querySelectorAll('.nav-desktop a, .drawer-link').forEach(a => {
    const href = a.getAttribute('href') || '';
    if(href === currentPage || (currentPage === 'index.html' && href === 'index.html')){
      a.classList.add('active');
    }
  });

  /* ── Intersection reveal ── */
  const io = new IntersectionObserver((entries) => {
    entries.forEach(e => {
      if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); }
    });
  }, {threshold:.08, rootMargin:'0px 0px -30px 0px'});
  document.querySelectorAll('.r,.r2,.r3').forEach(el => io.observe(el));

})();
