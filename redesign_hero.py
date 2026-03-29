from pathlib import Path
import re

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

# ── 1. REPLACE ENTIRE HERO SECTION ──────────────────────────────────────────
old_hero_start = '<section class="hero"'
old_hero_end = '</section>'

# Find and replace the hero section content
hero_pattern = re.compile(r'<section class="hero".*?</section>', re.DOTALL)

new_hero = '''<section class="hero-v2">
<div class="hero-v2-left">
  <div class="hero-badge"><div class="hero-badge-dot"><svg width="10" height="10" viewBox="0 0 10 10" fill="none"><path d="M2 5l2 2 4-4" stroke="white" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"></path></svg></div><span class="hero-badge-text">Free to join &middot; Approved by DCF</span></div>
  <h1 class="hero-h1">Your parish.<br>A global community.<br><span class="sage-word">One voice.</span></h1>
  <p class="hero-sub">Give your parish a presence online, a website, and a donation page — free, live in days.</p>
  <div class="hero-feats">
    <div class="hero-feat"><div class="hero-feat-icon"><svg viewBox="0 0 14 14" fill="none" width="14" height="14"><circle cx="7" cy="5" r="2.5" stroke="#c85c3a" stroke-width="1.3"/><path d="M2 13c0-2.76 2.24-5 5-5s5 2.24 5 5" stroke="#c85c3a" stroke-width="1.3" stroke-linecap="round"/></svg></div><div><strong>Your parish profile</strong><span>A beautiful public page, live the moment you\'re approved</span></div></div>
    <div class="hero-feat"><div class="hero-feat-icon"><svg viewBox="0 0 14 14" fill="none" width="14" height="14"><rect x="1.5" y="2.5" width="11" height="9" rx="1.5" stroke="#c85c3a" stroke-width="1.3"/><path d="M4 6.5h6M4 9h4" stroke="#c85c3a" stroke-width="1.3" stroke-linecap="round"/></svg></div><div><strong>Your parish website</strong><span>Full site at yourparish.communio.org — no developer needed</span></div></div>
    <div class="hero-feat"><div class="hero-feat-icon"><svg viewBox="0 0 14 14" fill="none" width="14" height="14"><path d="M7 1.5v11M3.5 5l3.5-3.5L10.5 5" stroke="#c85c3a" stroke-width="1.3" stroke-linecap="round" stroke-linejoin="round"/></svg></div><div><strong>Accept donations worldwide</strong><span>One-off or recurring, direct to your bank account</span></div></div>
  </div>
  <div class="hero-actions">
    <a href="register.html" class="btn-main">Join free &rarr;</a>
    <a href="parish/profile.html" class="btn-ghost">View demo</a>
  </div>
  <div class="hero-trust">
    <div class="hero-tp"><div class="hero-tick"><svg viewBox="0 0 10 10" fill="none" width="10" height="10"><path d="M2 5l2.5 2.5L8 3" stroke="#3a8f56" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span>Live on approval</span></div>
    <div class="hero-tp"><div class="hero-tick"><svg viewBox="0 0 10 10" fill="none" width="10" height="10"><path d="M2 5l2.5 2.5L8 3" stroke="#3a8f56" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span>No credit card</span></div>
    <div class="hero-tp"><div class="hero-tick"><svg viewBox="0 0 10 10" fill="none" width="10" height="10"><path d="M2 5l2.5 2.5L8 3" stroke="#3a8f56" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span>Under 10 minutes</span></div>
    <div class="hero-tp"><div class="hero-tick"><svg viewBox="0 0 10 10" fill="none" width="10" height="10"><path d="M2 5l2.5 2.5L8 3" stroke="#3a8f56" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span>DCF verified</span></div>
    <div class="hero-tp"><div class="hero-tick"><svg viewBox="0 0 10 10" fill="none" width="10" height="10"><path d="M2 5l2.5 2.5L8 3" stroke="#3a8f56" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round"/></svg></div><span>Free forever</span></div>
  </div>
</div>
<div class="hero-v2-right">
  <img src="assets/smhero.jpg" alt="Communio parish profile page" class="hero-v2-img">
</div>
</section>'''

if hero_pattern.search(html):
    html = hero_pattern.sub(new_hero, html, count=1)
    print("Hero replaced ✓")
else:
    print("Hero section NOT FOUND")

# ── 2. REMOVE TICKER BAR ────────────────────────────────────────────────────
ticker_pattern = re.compile(r'<div class="marquee-strip".*?</div>\s*</div>', re.DOTALL)
if ticker_pattern.search(html):
    html = ticker_pattern.sub('', html, count=1)
    print("Ticker removed ✓")
else:
    # Try broader match
    ticker_pattern2 = re.compile(r'<div[^>]*marquee[^>]*>.*?</div>\s*</div>\s*</div>', re.DOTALL)
    if ticker_pattern2.search(html):
        html = ticker_pattern2.sub('', html, count=1)
        print("Ticker removed (broad match) ✓")
    else:
        print("Ticker NOT FOUND — remove manually")

# ── 3. REMOVE ALL 221K REFERENCES ───────────────────────────────────────────
replacements = [
    ('221,000 parishes. One network.', 'A growing global network.'),
    ('>221,000+<', '>Growing<'),
    ('221,000+ parishes worldwide', 'A growing global network'),
    ('There are over 221,000 Catholic parishes in the world.', 'There are hundreds of thousands of Catholic parishes in the world.'),
    ('221+', 'Global'),
    ('221,000 parishes', 'thousands of parishes'),
    ('221,000', 'thousands'),
    ('gives 221,000', 'gives thousands of'),
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"Replaced: {old[:40]} ✓")

# ── 4. ADD NEW HERO CSS ──────────────────────────────────────────────────────
hero_css = '''
.hero-v2{background:#f5f0e8;display:grid;grid-template-columns:5fr 7fr;min-height:100vh;align-items:stretch;padding-top:58px}
.hero-v2-left{padding:60px 48px 60px 64px;display:flex;flex-direction:column;justify-content:center;gap:0}
.hero-v2-right{overflow:hidden;position:relative}
.hero-v2-img{width:100%;height:100%;object-fit:cover;object-position:top;display:block}
.hero-feats{display:flex;flex-direction:column;gap:14px;margin:20px 0 28px}
.hero-feat{display:flex;align-items:flex-start;gap:10px}
.hero-feat-icon{width:26px;height:26px;border-radius:7px;background:rgba(200,92,58,0.1);display:flex;align-items:center;justify-content:center;flex-shrink:0;margin-top:2px}
.hero-feat strong{display:block;font-size:13px;font-weight:700;color:#0e0a06;margin-bottom:2px}
.hero-feat span{font-size:12px;color:rgba(14,10,6,0.55);line-height:1.4}
.hero-trust{display:flex;flex-wrap:wrap;gap:10px 20px;margin-top:20px}
.hero-tp{display:flex;align-items:center;gap:6px;font-size:12px;color:rgba(14,10,6,0.6)}
.hero-tick{width:16px;height:16px;border-radius:50%;background:rgba(58,143,86,0.12);border:0.5px solid rgba(58,143,86,0.3);display:flex;align-items:center;justify-content:center;flex-shrink:0}
@media(max-width:860px){.hero-v2{grid-template-columns:1fr;min-height:auto}.hero-v2-right{height:280px}.hero-v2-left{padding:48px 24px 40px}}
'''

html = html.replace('</style>', hero_css + '</style>', 1)
print("CSS added ✓")

# ── 5. UPDATE PAGE TITLE ─────────────────────────────────────────────────────
html = html.replace(
    '<title>Communio — One parish. 221,000 voices.</title>',
    '<title>Communio — Your parish. A global community.</title>'
)
print("Title updated ✓")

p.write_text(html, encoding='utf-8')
print("\nDone. File saved.")