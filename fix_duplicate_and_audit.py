from pathlib import Path

base = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard')

# ── FIX duplicate profile card in home.html ──
f = base / 'home.html'
h = f.read_text(encoding='utf-8')

count = h.count('View my public profile')
print(f'Profile cards found: {count}')

if count > 1:
    # Remove the SECOND occurrence by finding both and keeping only first
    first = h.find('View my public profile')
    second = h.find('View my public profile', first + 1)
    # Find the start of the second qa-card block (search backwards from second)
    card_start = h.rfind('<div class="qa-card"', 0, second)
    # Find its closing </div> (4 levels deep - need to count)
    pos = second
    depth = 0
    while pos < len(h):
        if h[pos:pos+5] == '<div ':
            depth += 1
        elif h[pos:pos+6] == '</div>':
            if depth == 0:
                card_end = pos + 6
                break
            depth -= 1
        pos += 1
    h = h[:card_start] + h[card_end:]
    f.write_text(h, encoding='utf-8')
    print('Duplicate removed')
else:
    print('No duplicate found')

# ── VERIFY all 4 changes across all pages ──
print()
print('=== FULL AUDIT ===')
pages = ['home.html','messages.html','network.html','projects.html',
         'website.html','donations.html','settings.html']

for name in pages:
    page = base / name
    h = page.read_text(encoding='utf-8')
    has_profile_nav  = 'My Profile' in h
    has_pill_link    = '../parish/profile.html" class="nav-pill"' in h
    has_settings_btn = '>Settings →</span>' in h
    print(f'{name}: nav={"✅" if has_profile_nav else "❌"} pill={"✅" if has_pill_link else "❌"} settings_btn={"✅" if has_settings_btn else "❌"}')

# Check home specifically for profile card
h = (base / 'home.html').read_text(encoding='utf-8')
card_count = h.count('View my public profile')
print(f'\nhome.html profile cards: {card_count} (should be 1)')

# Check network for strip
h = (base / 'network.html').read_text(encoding='utf-8')
print(f'network.html profile strip: {"✅" if "Your public profile" in h else "❌"}')