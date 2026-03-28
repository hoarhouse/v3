from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Remove the broken inline comment from inside the tag
# and place it correctly BEFORE the opening div tag instead
html = html.replace(
    '<!-- SHARED: hero_image | <?php echo $parish->hero_image; ?> -->class="masthead"',
    'class="masthead"'
)

# Also fix any other markers we injected the same way (inside tags)
html = html.replace(
    '<!-- SHARED: parish_name | <?php echo $parish->name; ?> -->class="p-name"',
    'class="p-name"'
)
html = html.replace(
    '<!-- SHARED: location | <?php echo $parish->city . ", " . $parish->country; ?> -->class="p-loc"',
    'class="p-loc"'
)
html = html.replace(
    '<!-- SHARED: tags | <?php foreach($parish->tags as $tag): ?> ... <?php endforeach; ?> -->class="p-tags"',
    'class="p-tags"'
)
html = html.replace(
    '<!-- SHARED: stats | $parish->founded, $parish->family_count, $parish->project_count, $parish->sister_count, $parish->visitor_count -->class="p-stats"',
    'class="p-stats"'
)
html = html.replace(
    '<!-- SHARED: events | <?php foreach($parish->events as $event): ?> -->class="e-row"',
    'class="e-row"'
)
html = html.replace(
    '<!-- SHARED: donations | $parish->donation_current, $parish->donation_goal, $parish->stripe_key -->class="don-am"',
    'class="don-am"'
)
html = html.replace(
    '<!-- SHARED: contact | $parish->email / $parish->website_url / $parish->address -->class="ct-row"',
    'class="ct-row"'
)
html = html.replace(
    '<!-- SHARED: sister_parishes | <?php foreach($parish->sister_parishes as $sp): ?> -->class="sp-row"',
    'class="sp-row"'
)

p.write_text(html, encoding='utf-8')

# Verify masthead is clean
print("masthead check:", html.count('class="masthead"'), "occurrences")
print("broken markers remaining:", html.count('-->class='))