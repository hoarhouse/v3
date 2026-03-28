from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

# 1. Hero background: ink → cream
html = html.replace(
    'background: var(--ink);\n      display: grid;',
    'background: var(--cream);\n      display: grid;'
)

# 2. Nav background when scrolled — currently dark, make it cream
html = html.replace(
    '.nav.scrolled { background: rgba(14,10,6,0.95); backdrop-filter: blur(12px); box-shadow: 0 1px 0 rgba(255,255,255,0.06); }',
    '.nav.scrolled { background: rgba(245,240,232,0.97); backdrop-filter: blur(12px); box-shadow: 0 1px 0 rgba(0,0,0,0.08); }'
)

# 3. Nav base — make text ink coloured not white
html = html.replace(
    '.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 0 32px; height: 58px; display: flex; align-items: center; justify-content: space-between; transition: all 0.3s ease; }',
    '.nav { position: fixed; top: 0; left: 0; right: 0; z-index: 100; padding: 0 32px; height: 58px; display: flex; align-items: center; justify-content: space-between; transition: all 0.3s ease; background: var(--cream); }'
)

# 4. Nav links — white → ink
html = html.replace(
    '.nav-link { color: rgba(255,255,255,0.7);',
    '.nav-link { color: var(--ink);'
)
html = html.replace(
    '.nav-link:hover { color: white; }',
    '.nav-link:hover { color: var(--terra); }'
)

# 5. Nav brand name — white → ink  
html = html.replace(
    '.nav-name { font-size: 17px; font-weight: 700; color: white;',
    '.nav-name { font-size: 17px; font-weight: 700; color: var(--ink);'
)

# 6. Hero heading and sub text — these use white, change to ink
html = html.replace(
    '.hero-heading { font-size: clamp(42px,6vw,76px); font-weight: 800; line-height: 1.0; letter-spacing: -0.03em; color: white;',
    '.hero-heading { font-size: clamp(42px,6vw,76px); font-weight: 800; line-height: 1.0; letter-spacing: -0.03em; color: var(--ink);'
)
html = html.replace(
    '.hero-sub { font-size: 18px; line-height: 1.6; color: rgba(255,255,255,0.7);',
    '.hero-sub { font-size: 18px; line-height: 1.6; color: rgba(14,10,6,0.65);'
)

p.write_text(html, encoding='utf-8')
print("Done")
# Verify key changes
print("cream hero:", html.count('background: var(--cream);\n      display: grid;'))
print("ink heading:", html.count('color: var(--ink);\n      margin:'))