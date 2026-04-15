/* ═══════════════════════════════════════════════════
   GNLA SHARED JS — nav, hamburger, reveal
════════════════════════════════════════════════════ */
(function(){

  /* ── Nav scroll solid ── */
  const nav = document.getElementById('gnla-nav');
  if(nav && !nav.classList.contains('always-solid')){
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
    // Close on link click
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
