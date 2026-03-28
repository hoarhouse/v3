from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

html = html.replace(
    'class="don-gl">',
    'class="don-gl">Monthly giving goal'
)

p.write_text(html, encoding='utf-8')
print("Done")