from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/settings.html')
html = p.read_text(encoding='utf-8')

# Target fields by their unique hardcoded values + label text proximity
# Since all inputs share class="form-input", we anchor to unique content

replacements = [
    # Parish name field — unique value
    (
        '>St. Mary\'s Parish<',
        '>St. Mary\'s Parish<!-- SOURCE: $parish->name → profile p-name, website header --><'
    ),
    # City field
    (
        '>New York<',
        '>New York<!-- SOURCE: $parish->city → profile p-loc, website --><'
    ),
    # Description textarea
    (
        'St. Mary\'s Parish has been serving the L',
        'St. Mary\'s Parish has been serving the L<!-- SOURCE: $parish->description → profile about, website -->'
    ),
    # Contact person
    (
        '>Fr. James O\'Brien<',
        '>Fr. James O\'Brien<!-- SOURCE: $parish->contact_name → profile ct-row --><'
    ),
    # Email
    (
        '>info@stmarysnyc.org<',
        '>info@stmarysnyc.org<!-- SOURCE: $parish->email → profile ct-row, website contact --><'
    ),
    # Phone
    (
        '>+1 (212) 555-0182<',
        '>+1 (212) 555-0182<!-- SOURCE: $parish->phone → profile ct-row, website contact --><'
    ),
    # Address
    (
        '>15 Mott Street, New York, NY 10013<',
        '>15 Mott Street, New York, NY 10013<!-- SOURCE: $parish->address → profile ct-row, website contact --><'
    ),
    # Focus areas label — mark the whole form-group
    (
        '>Focus areas<',
        '>Focus areas<!-- SOURCE: $parish->tags → profile p-tags, website --><'
    ),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print(f"NOT FOUND: {old[:50]}")

p.write_text(html, encoding='utf-8')
print(f"Done. {count} of {len(replacements)} markers placed in settings.html")