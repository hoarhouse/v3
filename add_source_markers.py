from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/settings.html')
html = p.read_text(encoding='utf-8')

# Mark settings fields as SOURCE for shared data
replacements = [
    # Parish name field
    ('name="parish_name"', 'name="parish_name" <!-- SOURCE: feeds $parish->name → profile.html, website.html -->'),
    # Location
    ('name="parish_city"', 'name="parish_city" <!-- SOURCE: feeds $parish->city → profile p-loc, website header -->'),
    # Hero image upload
    ('name="hero_image"', 'name="hero_image" <!-- SOURCE: feeds $parish->hero_image → profile masthead, website hero -->'),
    # Tags/focus areas
    ('name="parish_tags"', 'name="parish_tags" <!-- SOURCE: feeds $parish->tags → profile p-tags, website -->'),
    # Email
    ('name="contact_email"', 'name="contact_email" <!-- SOURCE: feeds $parish->email → profile ct-row, website contact -->'),
    # Address
    ('name="contact_address"', 'name="contact_address" <!-- SOURCE: feeds $parish->address → profile ct-row, website contact -->'),
    # Donation goal
    ('name="donation_goal"', 'name="donation_goal" <!-- SOURCE: feeds $parish->donation_goal → profile don-am, website donate -->'),
    # Stripe key
    ('name="stripe_key"', 'name="stripe_key" <!-- SOURCE: feeds $parish->stripe_key → profile donate button, website donate -->'),
    # Founded year
    ('name="founded_year"', 'name="founded_year" <!-- SOURCE: feeds $parish->founded → profile p-stats -->'),
    # Family count
    ('name="family_count"', 'name="family_count" <!-- SOURCE: feeds $parish->family_count → profile p-stats -->'),
]

count = 0
for old, new in replacements:
    if old in html:
        html = html.replace(old, new, 1)
        count += 1

p.write_text(html, encoding='utf-8')
print(f"Done. {count} of {len(replacements)} markers placed in settings.html")