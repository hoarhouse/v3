from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/website.html')
html = p.read_text(encoding='utf-8')

# Mark website.html fields that pull from shared parish record
replacements = [
    # Hero section display
    ('class="hero-preview"', '<!-- SHARED: hero_image | <?php echo $parish->hero_image; ?> -->class="hero-preview"'),
    # Parish name in preview
    ('class="preview-name"', '<!-- SHARED: parish_name | <?php echo $parish->name; ?> -->class="preview-name"'),
    # Events tab — events list
    ('id="tab-events"', '<!-- SHARED: events | <?php foreach($parish->events as $event): ?> ... <?php endforeach; ?> -->id="tab-events"'),
    # Donations tab — stripe/goal config
    ('id="tab-settings"', '<!-- SHARED: stripe_key, donation_goal | $parish->stripe_key, $parish->donation_goal -->id="tab-settings"'),
    # SEO tab — parish name used in meta
    ('id="tab-seo"', '<!-- SHARED: parish_name used in meta title/description | $parish->name -->id="tab-seo"'),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1

p.write_text(html, encoding='utf-8')
print(f"Done. {count} of {len(replacements)} markers placed in website.html")