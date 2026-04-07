/**
 * Rise — Shared Navigation
 * Single source of truth. Update this file to update nav on every page.
 * To add a new journal entry: add it to JOURNAL_ENTRIES below.
 * To add a new demo: add it to DEMOS below.
 */

const RISE_NAV = {

  DEMOS: [
    { num: '01', label: 'Manual',  href: 'risedemo.html' },
    { num: '02', label: 'Auto',    href: 'autodemo.html' },
    { num: '03', label: 'Brain',   href: 'braindemo.html' },
    { num: '04', label: 'Essence', href: 'essencedemo.html' },
    { num: '05', label: 'COO',     href: 'coodemo.html' },
  ],

  JOURNAL_ENTRIES: [
    { num: '01', label: 'Entry 01', href: 'entry-01.html' },
    { num: '02', label: 'Entry 02', href: 'entry-02.html' },
    { num: '03', label: 'Entry 03', href: 'entry-03.html' },
    { num: '04', label: 'Entry 04', href: 'entry-04.html' },
  ],

  DOCS: [
    { label: 'Scope V5',  href: 'Rise_Scope_V5.pdf' },
    { label: 'Tech Arch', href: 'Rise_Technical_Architecture_V1.pdf' },
    { label: 'Prompts',   href: 'Rise_Prompt_Architecture_V1.pdf' },
  ],

  LINKS: {
    egroup:    '../rise/index.html',   // from journal/
    journal:   '../journal/',          // from demos/
    documents: '../documents/',        // from demos/
  }
};

/**
 * Inject the shared nav into the page.
 * @param {string} type      - 'demo' | 'journal'
 * @param {string} activePage - filename of current page e.g. 'entry-03.html' or 'braindemo.html'
 */
function injectNav(type, activePage) {

  // Determine path prefix based on page type
  const isDemo    = type === 'demo';
  const isJournal = type === 'journal';

  // Relative paths from each location
  const demoBase  = '';           // demos are in /rise/demos/ — hrefs relative to here
  const journalBase = '';         // journal pages in /journal/
  const toRise    = isDemo ? '../' : '../rise/';
  const toJournal = isDemo ? '../../journal/' : '';
  const toDocs    = isDemo ? '../documents/' : '../rise/documents/';
  const toEgroup  = isDemo ? '../index.html' : '../rise/index.html';

  const CSS = `
  <style id="rise-nav-style">
  .rnav {
    height: 48px;
    background: #0A0A0A;
    border-bottom: 1px solid #1E1E1E;
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 0 24px;
    position: sticky;
    top: 0;
    z-index: 1000;
    flex-shrink: 0;
    font-family: 'DM Sans', sans-serif;
    box-sizing: border-box;
  }
  .rnav * { box-sizing: border-box; }
  .rnav-logo {
    display: flex; align-items: center; gap: 10px;
    text-decoration: none; flex-shrink: 0;
  }
  .rnav-mark {
    width: 26px; height: 26px; background: #D4FF00;
    display: flex; align-items: center; justify-content: center;
    font-family: 'Syne', sans-serif; font-weight: 800;
    font-size: 13px; color: #080808;
  }
  .rnav-name {
    font-family: 'Syne', sans-serif; font-weight: 800;
    font-size: 15px; color: #EEEEEE;
  }
  .rnav-sep { width: 1px; height: 16px; background: #252525; margin: 0 6px; }
  .rnav-centre { display: flex; align-items: center; gap: 2px; }
  .rnav-item {
    font-family: 'DM Mono', monospace; font-size: 10px;
    letter-spacing: 1px; text-transform: uppercase;
    padding: 5px 11px; border-radius: 5px;
    border: 1px solid transparent; color: #555;
    text-decoration: none; transition: all .15s; white-space: nowrap;
  }
  .rnav-item:hover { color: #AAAAAA; background: #161616; border-color: #252525; }
  .rnav-item.active { color: #EEEEEE; background: #1A1A1A; border-color: #333; }
  .rnav-item .rnav-num { opacity: .5; margin-right: 4px; }
  .rnav-right { display: flex; align-items: center; gap: 4px; }
  .rnav-link {
    font-family: 'DM Mono', monospace; font-size: 9px;
    letter-spacing: 1px; text-transform: uppercase;
    padding: 4px 9px; border-radius: 4px;
    border: 1px solid #1E1E1E; color: #444;
    text-decoration: none; transition: all .15s; white-space: nowrap;
  }
  .rnav-link:hover { color: #AAAAAA; border-color: #333; }
  .rnav-link.doc { border-color: rgba(78,201,255,.15); color: rgba(78,201,255,.6); }
  .rnav-link.doc:hover { color: #4EC9FF; border-color: rgba(78,201,255,.4); }
  </style>`;

  // Build centre links
  const items = isDemo ? RISE_NAV.DEMOS : RISE_NAV.JOURNAL_ENTRIES;
  const centreLinks = items.map(item => {
    const cls = item.href === activePage ? 'rnav-item active' : 'rnav-item';
    return `<a href="${item.href}" class="${cls}"><span class="rnav-num">${item.num}</span>${item.label}</a>`;
  }).join('\n    ');

  // Build right links
  const egroupLink = `<a href="${toEgroup}" class="rnav-link">eGroup</a>`;
  const journalLink = isDemo ? `<a href="${toJournal}" class="rnav-link">Journal</a>` : '';
  const demosLink   = isJournal ? `<a href="../rise/demos/risedemo.html" class="rnav-link">Demos</a>` : '';
  const docLinks = RISE_NAV.DOCS.map(d =>
    `<a href="${toDocs}${d.href}" target="_blank" class="rnav-link doc">${d.label}</a>`
  ).join('\n    ');

  const navHTML = `${CSS}
<nav class="rnav" id="rise-nav">
  <a href="${toRise}index.html" class="rnav-logo">
    <div class="rnav-mark">R</div>
    <span class="rnav-name">Rise</span>
  </a>
  <div class="rnav-sep"></div>
  <div class="rnav-centre">
    ${centreLinks}
  </div>
  <div class="rnav-right">
    ${egroupLink}
    ${journalLink}
    ${demosLink}
    ${docLinks}
  </div>
</nav>`;

  // Inject at top of body, removing any existing nav
  const existing = document.getElementById('rise-nav');
  if (existing) existing.parentElement.removeChild(existing);
  const existingStyle = document.getElementById('rise-nav-style');
  if (existingStyle) existingStyle.parentElement.removeChild(existingStyle);

  document.body.insertAdjacentHTML('afterbegin', navHTML);
}
