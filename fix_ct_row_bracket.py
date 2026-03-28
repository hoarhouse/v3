from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Find the exact text around the contact row with the stray >
# It's the first ct-row, before info@stmarysnyc.org
html = html.replace('class="ct-row">>', 'class="ct-row">')

# Also try alternate forms
html = html.replace('class="ct-row"><>', 'class="ct-row">')

p.write_text(html, encoding='utf-8')

# Confirm what's actually there
import re
matches = re.findall('.{30}ct-row.{50}', html)
for m in matches[:3]:
    print(repr(m))