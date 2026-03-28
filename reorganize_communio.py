from pathlib import Path

base = Path('/Users/christopherhoar/Desktop/v3')

# ── FIX communio/index.html ──
f = base / 'communio/index.html'
h = f.read_text(encoding='utf-8')
h = h.replace('communio-register.html', 'register.html')
h = h.replace('communio-dashboard.html', 'dashboard/home.html')
h = h.replace('/v3/communio.html', '/v3/communio/index.html')
h = h.replace('href="communio.html"', 'href="index.html"')
f.write_text(h, encoding='utf-8')
print('Fixed communio/index.html')

# ── FIX communio/register.html ──
f = base / 'communio/register.html'
h = f.read_text(encoding='utf-8')
h = h.replace('href="communio.html"', 'href="index.html"')
h = h.replace('communio.html#how-it-works', 'index.html#how-it-works')
h = h.replace('communio.html#features', 'index.html#features')
h = h.replace('communio.html#pricing', 'index.html#pricing')
h = h.replace('communio.html', 'index.html')
f.write_text(h, encoding='utf-8')
print('Fixed communio/register.html')

# ── FIX register.html (main v3 site) ──
f = base / 'register.html'
h = f.read_text(encoding='utf-8')
h = h.replace('href="communio.html"', 'href="communio/index.html"')
h = h.replace('href="communio-register.html"', 'href="communio/register.html"')
h = h.replace('communio.html', 'communio/index.html')
f.write_text(h, encoding='utf-8')
print('Fixed register.html')

# ── FIX parish-profile.html (main v3 site) ──
f = base / 'parish-profile.html'
h = f.read_text(encoding='utf-8')
h = h.replace('href="communio.html"', 'href="communio/index.html"')
h = h.replace('href="communio-register.html"', 'href="communio/register.html"')
h = h.replace('communio.html', 'communio/index.html')
f.write_text(h, encoding='utf-8')
print('Fixed parish-profile.html')

# ── DELETE old files ──
old1 = base / 'communio.html'
old2 = base / 'communio-dashboard.html'
if old1.exists(): old1.unlink(); print('Deleted communio.html')
if old2.exists(): old2.unlink(); print('Deleted communio-dashboard.html')

print('ALL DONE')