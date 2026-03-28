from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

replacements = [
    # Hero heading
    ('.hero-h1 {', '.hero-h1 { color: var(--ink);'),
    # Hero subtext
    ('.hero-sub {', '.hero-sub { color: rgba(14,10,6,0.65);'),
    # Nav brand name
    ('.nav-name {', '.nav-name { color: var(--ink);'),
    # Ghost button — white outline won't work on cream
    ('btn-ghost', 'btn-ghost'),  # placeholder — let's check first
    # hero-h1 highlight (green accent — keep as is, it works)
]

count = 0
# Fix hero-h1
if '.hero-h1 {' in html and 'color: var(--ink)' not in html.split('.hero-h1 {')[1][:50]:
    html = html.replace('.hero-h1 {', '.hero-h1 { color: var(--ink);', 1)
    count += 1
    print("hero-h1 fixed")
else:
    print("hero-h1 NOT FOUND or already fixed")

# Fix hero-sub
if '.hero-sub {' in html:
    html = html.replace('.hero-sub {', '.hero-sub { color: rgba(14,10,6,0.65);', 1)
    count += 1
    print("hero-sub fixed")
else:
    print("hero-sub NOT FOUND")

# Fix nav-name
if '.nav-name {' in html:
    html = html.replace('.nav-name {', '.nav-name { color: var(--ink);', 1)
    count += 1
    print("nav-name fixed")
else:
    print("nav-name NOT FOUND")

# Fix btn-ghost — white border/text won't work on cream
html = html.replace(
    '.btn-ghost { border: 1.5px solid rgba(255,255,255,0.4); color: rgba(255,255,255,0.85);',
    '.btn-ghost { border: 1.5px solid rgba(14,10,6,0.3); color: rgba(14,10,6,0.75);'
)

p.write_text(html, encoding='utf-8')
print(f"Done — {count} fixes applied")