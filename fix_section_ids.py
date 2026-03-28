from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/website.html')
h = f.read_text(encoding='utf-8')

# Fix hero ID — find the hero div and add id
h = h.replace(
    "+'<div style=\"background:' + heroStyle + ';position:relative;\">'+",
    "+'<div id=\"ws-hero\" style=\"background:' + heroStyle + ';position:relative;\">'+",
    1
)

# Fix contact ID — the last cardBg card before the footer
# Find "Contact us" label and add id to its parent div
old = "'<div style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'"
new = "'<div id=\"ws-contact\" style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'"
# Only replace the LAST occurrence (the contact section)
idx = h.rfind(old)
if idx != -1:
    h = h[:idx] + new + h[idx+len(old):]
    print('Fixed contact ID')
else:
    print('Contact pattern not found - check manually')

f.write_text(h, encoding='utf-8')

# Verify
h2 = f.read_text(encoding='utf-8')
print('ws-hero count:', h2.count('ws-hero'))
print('ws-contact count:', h2.count('ws-contact'))