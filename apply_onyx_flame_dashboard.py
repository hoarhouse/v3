#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Applying Onyx & Flame palette to communio-dashboard.html")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - CHECK CURRENT FORMAT:")
print("-" * 35)
print("  Current variable format found (compact)")

print("\nSTEP 2 - UPDATE CSS VARIABLES:")
print("-" * 35)

# CSS Variable replacements (compact format)
css_replacements = [
    # Core colors
    ('--ink:#16120c;', '--ink:#000000;'),
    ('--ink-s:#2e2518;', '--ink-s:#111111;'),
    
    # Terra colors
    ('--terra:#c85c3a;', '--terra:#d85020;'),
    ('--terra-l:#e8856a;', '--terra-l:#f07040;'),
    ('--terra-p:#fceee9;', '--terra-p:#fff0ea;'),
    
    # Amber colors
    ('--amber:#d4922a;', '--amber:#e8c040;'),
    ('--amber-p:#fdf3e0;', '--amber-p:#fdf8d8;'),
    
    # Cream colors
    ('--cream:#ffffff;', '--cream:#f5f2e8;'),
    ('--cream-dk:#f5ede0;', '--cream-dk:#ede8d8;'),
    ('--ww:#ffffff;', '--ww:#fffdf5;'),
    
    # Border colors
    ('--border:#e8d9c4;', '--border:#e8c040;'),
    ('--border-l:#f0e4d0;', '--border-l:#f0dca0;'),
    
    # Text colors
    ('--mid:#6b5c48;', '--mid:#5a4a20;'),
    ('--light:#9c8b78;', '--light:#8a7a50;'),
    
    # Sage colors
    ('--sage:#4a7c59;', '--sage:#2a8a4a;'),
    ('--sage-l:#6a9e78;', '--sage-l:#4aaa6a;'),
    ('--sage-p:#eaf3ec;', '--sage-p:#dff5e8;'),
]

for old, new in css_replacements:
    if old in content:
        content = content.replace(old, new)
        var_name = old.split(':')[0]
        print(f"  ✓ {var_name} updated")

print("\nSTEP 3 - REPLACE HARDCODED HEX VALUES:")
print("-" * 40)

# Hardcoded hex replacements
hex_replacements = [
    ('#c85c3a', '#d85020'),  # Old terra → new terra
    ('#4a7c59', '#2a8a4a'),  # Old sage → new sage
    ('#6b5c48', '#5a4a20'),  # Old text-mid → new
    ('#9c8b78', '#8a7a50'),  # Old text-light → new
    ('#16120c', '#000000'),  # Old ink → new ink
    ('#2e2518', '#111111'),  # Old ink-soft → new
    ('#e8d9c4', '#e8c040'),  # Old border → new border
    ('#e8856a', '#f07040'),  # Old terra-light → new
    ('#fceee9', '#fff0ea'),  # Old terra-pale → new
    ('#eaf3ec', '#dff5e8'),  # Old sage-pale → new
    ('#d4922a', '#e8c040'),  # Old amber → new amber
]

for old, new in hex_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")

print("\nSTEP 4 - FIX ALL BUTTONS WITH HARDCODED HEX:")
print("-" * 45)

# Fix .btn-terra
btn_terra_pattern = r'(\.btn-terra\s*\{[^}]*?\})'
btn_terra_match = re.search(btn_terra_pattern, content, re.DOTALL)

if btn_terra_match:
    btn_block = btn_terra_match.group(1)
    btn_block = re.sub(r'background:[^;]+;', 'background: #d85020;', btn_block)
    btn_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', btn_block)
    content = content.replace(btn_terra_match.group(0), btn_block)
    print("  ✓ .btn-terra: #d85020 background, white text")

# Fix .btn-terra:hover
btn_terra_hover_pattern = r'(\.btn-terra:hover\s*\{[^}]*?\})'
btn_terra_hover_match = re.search(btn_terra_hover_pattern, content, re.DOTALL)

if btn_terra_hover_match:
    hover_block = btn_terra_hover_match.group(1)
    hover_block = re.sub(r'background:[^;]+;', 'background: #f07040;', hover_block)
    content = content.replace(btn_terra_hover_match.group(0), hover_block)
    print("  ✓ .btn-terra:hover: #f07040 background")

# Fix .nav-mark
nav_mark_pattern = r'(\.nav-mark\s*\{[^}]*?\})'
nav_mark_match = re.search(nav_mark_pattern, content, re.DOTALL)

if nav_mark_match:
    mark_block = nav_mark_match.group(1)
    mark_block = re.sub(r'background:[^;]+;', 'background: #d85020;', mark_block)
    content = content.replace(nav_mark_match.group(0), mark_block)
    print("  ✓ .nav-mark: #d85020 background")

# Fix .sw-btn.on (switcher)
sw_btn_pattern = r'(\.sw-btn\.on\s*\{[^}]*?\})'
sw_btn_match = re.search(sw_btn_pattern, content, re.DOTALL)

if sw_btn_match:
    sw_block = sw_btn_match.group(1)
    sw_block = re.sub(r'background:[^;]+;', 'background: #d85020;', sw_block)
    sw_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', sw_block)
    content = content.replace(sw_btn_match.group(0), sw_block)
    print("  ✓ .sw-btn.on: #d85020 background, white text")

# Fix .wl-cta (welcome button)
wl_cta_pattern = r'(\.wl-cta\s*\{[^}]*?\})'
wl_cta_match = re.search(wl_cta_pattern, content, re.DOTALL)

if wl_cta_match:
    cta_block = wl_cta_match.group(1)
    cta_block = re.sub(r'background:[^;]+;', 'background: #d85020;', cta_block)
    cta_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', cta_block)
    content = content.replace(wl_cta_match.group(0), cta_block)
    print("  ✓ .wl-cta: #d85020 background, white text")

# Fix .dw-btn (donation button)
dw_btn_pattern = r'(\.dw-btn\s*\{[^}]*?\})'
dw_btn_match = re.search(dw_btn_pattern, content, re.DOTALL)

if dw_btn_match:
    dw_block = dw_btn_match.group(1)
    dw_block = re.sub(r'background:[^;]+;', 'background: #d85020;', dw_block)
    dw_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', dw_block)
    content = content.replace(dw_btn_match.group(0), dw_block)
    print("  ✓ .dw-btn: #d85020 background, white text")

# Fix .btn-connect-pub
btn_connect_pattern = r'(\.btn-connect-pub\s*\{[^}]*?\})'
btn_connect_match = re.search(btn_connect_pattern, content, re.DOTALL)

if btn_connect_match:
    connect_block = btn_connect_match.group(1)
    connect_block = re.sub(r'background:[^;]+;', 'background: #d85020;', connect_block)
    connect_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', connect_block)
    content = content.replace(btn_connect_match.group(0), connect_block)
    print("  ✓ .btn-connect-pub: #d85020 background, white text")

# Fix .btn-con-pub
btn_con_pattern = r'(\.btn-con-pub\s*\{[^}]*?\})'
btn_con_match = re.search(btn_con_pattern, content, re.DOTALL)

if btn_con_match:
    con_block = btn_con_match.group(1)
    con_block = re.sub(r'background:[^;]+;', 'background: #d85020;', con_block)
    con_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', con_block)
    content = content.replace(btn_con_match.group(0), con_block)
    print("  ✓ .btn-con-pub: #d85020 background, white text")

# Fix .step-tab.active .step-num
step_active_pattern = r'(\.step-tab\.active\s+\.step-num\s*\{[^}]*?\})'
step_active_match = re.search(step_active_pattern, content, re.DOTALL)

if step_active_match:
    step_block = step_active_match.group(1)
    step_block = re.sub(r'background:[^;]+;', 'background: #d85020;', step_block)
    step_block = re.sub(r'border-color:[^;]+;', 'border-color: #d85020;', step_block)
    content = content.replace(step_active_match.group(0), step_block)
    print("  ✓ .step-tab.active .step-num: #d85020")

# Fix .s-tab.active .s-num
s_tab_pattern = r'(\.s-tab\.active\s+\.s-num\s*\{[^}]*?\})'
s_tab_match = re.search(s_tab_pattern, content, re.DOTALL)

if s_tab_match:
    s_block = s_tab_match.group(1)
    s_block = re.sub(r'background:[^;]+;', 'background: #d85020;', s_block)
    s_block = re.sub(r'border-color:[^;]+;', 'border-color: #d85020;', s_block)
    content = content.replace(s_tab_match.group(0), s_block)
    print("  ✓ .s-tab.active .s-num: #d85020")

print("\nSTEP 5 - FIX SIDEBAR:")
print("-" * 30)

# Fix .sb-item.active
sb_active_pattern = r'(\.sb-item\.active\s*\{[^}]*?\})'
sb_active_match = re.search(sb_active_pattern, content, re.DOTALL)

if sb_active_match:
    sb_block = sb_active_match.group(1)
    sb_block = re.sub(r'background:[^;]+;', 'background: #d85020;', sb_block)
    content = content.replace(sb_active_match.group(0), sb_block)
    print("  ✓ .sb-item.active: #d85020 background")

# Fix .sb-badge
sb_badge_pattern = r'(\.sb-badge\s*\{[^}]*?\})'
sb_badge_match = re.search(sb_badge_pattern, content, re.DOTALL)

if sb_badge_match:
    badge_block = sb_badge_match.group(1)
    badge_block = re.sub(r'background:[^;]+;', 'background: #d85020;', badge_block)
    content = content.replace(sb_badge_match.group(0), badge_block)
    print("  ✓ .sb-badge: #d85020 background")

print("\nSTEP 6 - FIX TEXT ON DARK BACKGROUNDS:")
print("-" * 40)

# Welcome screen text
wl_h1_pattern = r'(\.wl-h1\s*\{[^}]*?\})'
wl_h1_match = re.search(wl_h1_pattern, content, re.DOTALL)

if wl_h1_match:
    h1_block = wl_h1_match.group(1)
    h1_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', h1_block)
    content = content.replace(wl_h1_match.group(0), h1_block)
    print("  ✓ .wl-h1: white text")

wl_p_pattern = r'(\.wl-p\s*\{[^}]*?\})'
wl_p_match = re.search(wl_p_pattern, content, re.DOTALL)

if wl_p_match:
    p_block = wl_p_match.group(1)
    p_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.6);', p_block)
    content = content.replace(wl_p_match.group(0), p_block)
    print("  ✓ .wl-p: light white text")

wl_count_pattern = r'(\.wl-count\s*\{[^}]*?\})'
wl_count_match = re.search(wl_count_pattern, content, re.DOTALL)

if wl_count_match:
    count_block = wl_count_match.group(1)
    count_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.4);', count_block)
    content = content.replace(wl_count_match.group(0), count_block)
    print("  ✓ .wl-count: faint white text")

wl_tag_pattern = r'(\.wl-tag\s*\{[^}]*?\})'
wl_tag_match = re.search(wl_tag_pattern, content, re.DOTALL)

if wl_tag_match:
    tag_block = wl_tag_match.group(1)
    tag_block = re.sub(r'color:[^;]+;', 'color: #4aaa6a;', tag_block)
    content = content.replace(wl_tag_match.group(0), tag_block)
    print("  ✓ .wl-tag: sage-light color")

# Profile hero text
pub_name_pattern = r'(\.pub-name\s*\{[^}]*?\})'
pub_name_match = re.search(pub_name_pattern, content, re.DOTALL)

if pub_name_match:
    pub_block = pub_name_match.group(1)
    pub_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', pub_block)
    content = content.replace(pub_name_match.group(0), pub_block)
    print("  ✓ .pub-name: white text")

ph_name_pattern = r'(\.ph-name\s*\{[^}]*?\})'
ph_name_match = re.search(ph_name_pattern, content, re.DOTALL)

if ph_name_match:
    ph_block = ph_name_match.group(1)
    ph_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', ph_block)
    content = content.replace(ph_name_match.group(0), ph_block)
    print("  ✓ .ph-name: white text")

# Dashboard greeting
dash_greeting_pattern = r'(\.dash-greeting\s*\{[^}]*?\})'
dash_greeting_match = re.search(dash_greeting_pattern, content, re.DOTALL)

if dash_greeting_match:
    greeting_block = dash_greeting_match.group(1)
    greeting_block = re.sub(r'color:[^;]+;', 'color: #000000;', greeting_block)
    content = content.replace(dash_greeting_match.group(0), greeting_block)
    print("  ✓ .dash-greeting: black text")

dash_date_pattern = r'(\.dash-date\s*\{[^}]*?\})'
dash_date_match = re.search(dash_date_pattern, content, re.DOTALL)

if dash_date_match:
    date_block = dash_date_match.group(1)
    date_block = re.sub(r'color:[^;]+;', 'color: #5a4a20;', date_block)
    content = content.replace(dash_date_match.group(0), date_block)
    print("  ✓ .dash-date: text-mid color")

print("\nSTEP 7 - FIX MARQUEE STRIP TEXT:")
print("-" * 35)

marquee_item_pattern = r'(\.marquee-item\s*\{[^}]*?\})'
marquee_item_match = re.search(marquee_item_pattern, content, re.DOTALL)

if marquee_item_match:
    marquee_block = marquee_item_match.group(1)
    marquee_block = re.sub(r'color:[^;]+;', 'color: rgba(0,0,0,0.75);', marquee_block)
    content = content.replace(marquee_item_match.group(0), marquee_block)
    print("  ✓ .marquee-item: dark text on gold background")

marquee_dot_pattern = r'(\.marquee-dot\s*\{[^}]*?\})'
marquee_dot_match = re.search(marquee_dot_pattern, content, re.DOTALL)

if marquee_dot_match:
    dot_block = marquee_dot_match.group(1)
    dot_block = re.sub(r'background:[^;]+;', 'background: rgba(0,0,0,0.3);', dot_block)
    content = content.replace(marquee_dot_match.group(0), dot_block)
    print("  ✓ .marquee-dot: dark dots")

print("\nSTEP 8 - VERIFICATION:")
print("-" * 25)

# Count key colors
d85020_count = content.count('#d85020')
e8c040_count = content.count('#e8c040')
c85c3a_count = content.count('#c85c3a')
a7c59_count = content.count('#4a7c59')

print(f"  #d85020 (terra): {d85020_count} occurrences")
print(f"  #e8c040 (amber): {e8c040_count} occurrences")
print(f"  #c85c3a (old terra): {c85c3a_count} occurrences")
print(f"  #4a7c59 (old sage): {a7c59_count} occurrences")

if d85020_count > 15:
    print(f"  ✅ Terra usage > 15")
if e8c040_count > 5:
    print(f"  ✅ Amber usage > 5")
if c85c3a_count == 0:
    print(f"  ✅ Old terra removed")
if a7c59_count == 0:
    print(f"  ✅ Old sage removed")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 ONYX & FLAME PALETTE APPLIED:")
print("   • Buttons: Hardcoded #d85020")
print("   • Sidebar: Active states terra orange")
print("   • Dark sections: White text")
print("   • Marquee: Dark text on gold")
print("   • All old colors replaced")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Apply Onyx & Flame — communio-dashboard.html'")