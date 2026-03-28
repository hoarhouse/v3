from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Phase 1: PHP comment markers on all shared data fields

# 1. Hero image
html = html.replace(
    'class="masthead"',
    '<!-- SHARED: hero_image | <?php echo $parish->hero_image; ?> -->class="masthead"'
)

# 2. Parish name
html = html.replace(
    'class="p-name"',
    '<!-- SHARED: parish_name | <?php echo $parish->name; ?> -->class="p-name"'
)

# 3. Location
html = html.replace(
    'class="p-loc"',
    '<!-- SHARED: location | <?php echo $parish->city . ", " . $parish->country; ?> -->class="p-loc"'
)

# 4. Tags
html = html.replace(
    'class="p-tags"',
    '<!-- SHARED: tags | <?php foreach($parish->tags as $tag): ?> ... <?php endforeach; ?> -->class="p-tags"'
)

# 5. Stats bar
html = html.replace(
    'class="p-stats"',
    '<!-- SHARED: stats | $parish->founded, $parish->family_count, $parish->project_count, $parish->sister_count, $parish->visitor_count -->class="p-stats"'
)

# 6. Events loop
html = html.replace(
    'class="e-row"',
    '<!-- SHARED: events | <?php foreach($parish->events as $event): ?> -->class="e-row"',
    1  # only first occurrence — marks loop start
)

# 7. Donations
html = html.replace(
    'class="don-am"',
    '<!-- SHARED: donations | $parish->donation_current, $parish->donation_goal, $parish->stripe_key -->class="don-am"'
)

# 8. Contact rows
html = html.replace(
    'class="ct-row"',
    '<!-- SHARED: contact | $parish->email / $parish->website_url / $parish->address -->class="ct-row"',
    1  # first occurrence
)

# 9. Sister parishes loop
html = html.replace(
    'class="sp-row"',
    '<!-- SHARED: sister_parishes | <?php foreach($parish->sister_parishes as $sp): ?> -->class="sp-row"',
    1
)

# Phase 3: Visible "Shared from Settings" notices
# Add notice inside the donations support card
html = html.replace(
    'class="don-gl"',
    'class="don-gl"><a href="/v3/communio/dashboard/settings.html" class="shared-notice">⚙ Shared from Settings — edit in Settings →</a'
)

# Add notice inside contact card
html = html.replace(
    'class="ct-row"',
    'class="ct-row"><span class="shared-notice">⚙ Shared from Settings — edit in Settings →</span',
    1
)

p.write_text(html, encoding='utf-8')
print("Done. Verify with: grep -c 'SHARED:' " + str(p))