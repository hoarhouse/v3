from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

html = html.replace(
    '.btn-hero{font-family:var(--f-body);font-size:13px;font-weight:600;padding:8px 18px;',
    '.btn-hero{font-family:var(--f-body);font-size:13px;font-weight:600;line-height:20.8px;padding:8px 18px;'
)

p.write_text(html, encoding='utf-8')
print("Done:", html.count('line-height:20.8px'))