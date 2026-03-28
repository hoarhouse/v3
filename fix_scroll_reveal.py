from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

# Fix scroll reveal — trigger immediately on entry, not 40px late
html = html.replace(
    "threshold: 0.1, rootMargin: '0px 0px -40px 0px'",
    "threshold: 0, rootMargin: '0px'"
)

# Also speed up the reveal transition — currently too slow
html = html.replace(
    '.reveal { opacity: 0; transform: translateY(24px); transition: opacity 0.7s ease, transform 0.7s ease; }',
    '.reveal { opacity: 0; transform: translateY(16px); transition: opacity 0.45s ease, transform 0.45s ease; }'
)

p.write_text(html, encoding='utf-8')
print("threshold fixed:", html.count("threshold: 0, rootMargin: '0px'"))