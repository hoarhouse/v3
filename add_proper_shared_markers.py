from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# All markers placed AFTER closing tags — never inside an opening tag
replacements = [
    # Hero masthead — after the opening div
    ('<div class="masthead">', '<div class="masthead"><!-- SHARED: $parish->hero_image -->'),
    # Parish name
    ('<div class="p-name">', '<div class="p-name"><!-- SHARED: $parish->name -->'),
    # Location
    ('<div class="p-loc">', '<div class="p-loc"><!-- SHARED: $parish->city, $parish->country -->'),
    # Tags
    ('<div class="p-tags">', '<div class="p-tags"><!-- SHARED: foreach $parish->tags -->'),
    # Stats bar
    ('<div class="p-stats">', '<div class="p-stats"><!-- SHARED: $parish->founded, family_count, project_count, sister_count, visitor_count -->'),
    # Donations amount
    ('<div class="don-am">', '<div class="don-am"><!-- SHARED: $parish->donation_current, $parish->donation_goal, $parish->stripe_key -->'),
    # Contact rows
    ('<div class="ct-row">', '<div class="ct-row"><!-- SHARED: $parish->email / $parish->phone / $parish->address -->', ),
    # Sister parishes
    ('<div class="sp-row">', '<div class="sp-row"><!-- SHARED: foreach $parish->sister_parishes -->'),
]

count = 0
for item in replacements:
    old, new = item[0], item[1]
    if old in html:
        html = html.replace(old, new, 1)
        count += 1
    else:
        print(f"NOT FOUND: {old}")

p.write_text(html, encoding='utf-8')
print(f"Done. {count} of {len(replacements)} markers placed.")
print(f"Total SHARED markers: {html.count('SHARED:')}")