from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/settings.html')
html = p.read_text(encoding='utf-8')

replacements = [
    (
        'value="New York">',
        'value="New York"><!-- SOURCE: $parish->city → profile p-loc, website -->'
    ),
    (
        'value="Fr. James O\'Brien">',
        'value="Fr. James O\'Brien"><!-- SOURCE: $parish->contact_name → profile ct-row -->'
    ),
    (
        'value="info@stmarysnyc.org">',
        'value="info@stmarysnyc.org"><!-- SOURCE: $parish->email → profile ct-row, website contact -->'
    ),
    (
        'value="+1 (212) 555-0182">',
        'value="+1 (212) 555-0182"><!-- SOURCE: $parish->phone → profile ct-row, website contact -->'
    ),
    (
        'value="15 Mott Street, New York, NY 10013">',
        'value="15 Mott Street, New York, NY 10013"><!-- SOURCE: $parish->address → profile ct-row, website contact -->'
    ),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print(f"NOT FOUND: {old[:60]}")

p.write_text(html, encoding='utf-8')
print(f"Done. {count} of {len(replacements)} markers placed. Total SOURCE markers now:")
import subprocess
result = subprocess.run(['grep', '-c', 'SOURCE:', str(p)], capture_output=True, text=True)
print(result.stdout.strip())