from pathlib import Path

base = Path('/Users/christopherhoar/Desktop/v3/communio')
dashboard = base / 'dashboard'

pages = [
    'home.html','messages.html','network.html','projects.html',
    'website.html','donations.html','settings.html','setup.html','welcome.html'
]

# ── CHANGE 1 & 3: Add Profile to sidebar nav + fix nav pill link ──
# Add Profile nav item after Network in every dashboard page sidebar
# Also fix nav-pill to link to profile instead of settings

profile_nav_item_home = '''      <a href="profile.html"    class="sb-item">
        <svg viewBox="0 0 16 16" fill="none"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13z" stroke="currentColor" stroke-width="1.3"/><path d="M2 13c0-2.76 2.24-5 5-5s5 2.24 5 5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/><circle cx="8" cy="6" r="2" stroke="currentColor" stroke-width="1.3"/></svg>
        <span class="sb-item-lbl">My Profile</span>
      </a>'''

# Each page has slightly different active states, so we patch the Network link line
# and insert Profile after it

for page_name in pages:
    page = dashboard / page_name
    if not page.exists():
        print(f'SKIP (not found): {page_name}')
        continue

    h = page.read_text(encoding='utf-8')

    # ── 1. Add Profile to sidebar after Network link ──
    # Find the network sb-item and insert Profile after it
    # The network item ends with </a> then Projects starts
    # We look for the projects link and insert before it
    if 'sb-item-lbl">My Profile' not in h:
        # Insert after the Network link, before Projects
        old_projects = '<a href="projects.html"'
        if old_projects in h:
            # Determine correct relative path based on page
            h = h.replace(
                '<a href="projects.html"',
                '<a href="../parish/profile.html" class="sb-item">\n        <svg viewBox="0 0 16 16" fill="none"><path d="M8 1.5a6.5 6.5 0 100 13 6.5 6.5 0 000-13z" stroke="currentColor" stroke-width="1.3"/><path d="M2 13c0-2.76 2.24-5 5-5s5 2.24 5 5" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/><circle cx="8" cy="6" r="2" stroke="currentColor" stroke-width="1.3"/></svg>\n        <span class="sb-item-lbl">My Profile</span>\n      </a>\n      <a href="projects.html"',
                1
            )
            print(f'  Added My Profile nav: {page_name}')
        else:
            print(f'  WARNING: projects link not found in {page_name}')

    # ── 2. Fix nav-pill to link to profile ──
    # Currently: <a href="settings.html" class="nav-pill">
    h = h.replace(
        '<a href="settings.html" class="nav-pill">',
        '<a href="../parish/profile.html" class="nav-pill">'
    )

    # ── 3. Remove the now-redundant sb-bottom "View public profile" link ──
    # Keep the sb-bottom div but replace its content with a settings link instead
    h = h.replace(
        '<a href="../parish/profile.html" class="sb-profile-link">',
        '<a href="settings.html" class="sb-profile-link">'
    )
    h = h.replace(
        '<span>View public profile →</span>',
        '<span>Settings →</span>'
    )

    page.write_text(h, encoding='utf-8')

print()
print('Verifying...')
for page_name in pages:
    page = dashboard / page_name
    if not page.exists(): continue
    h = page.read_text(encoding='utf-8')
    has_profile = 'My Profile' in h
    has_pill_fix = '../parish/profile.html" class="nav-pill"' in h
    print(f'  {page_name}: profile_nav={has_profile} pill_fix={has_pill_fix}')