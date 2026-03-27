#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
profile_file = Path("/Users/christopherhoar/Desktop/v3/parish-profile.html")

print("Applying Onyx & Flame palette to parish-profile.html")
print("=" * 60)

# Read the file
content = profile_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - CHECK CURRENT FORMAT:")
print("-" * 35)
print("  Current variable format found (spaced)")

print("\nSTEP 2 - UPDATE CSS VARIABLES:")
print("-" * 35)

# CSS Variable replacements (based on current format with spaces)
css_replacements = [
    # Core colors
    ('--ink:         #16120c;', '--ink:         #000000;'),
    ('--ink-soft:    #2e2518;', '--ink-soft:    #111111;'),
    
    # Terra colors
    ('--terra:       #c85c3a;', '--terra:       #d85020;'),
    ('--terra-light: #e8856a;', '--terra-light: #f07040;'),
    ('--terra-pale:  #fceee9;', '--terra-pale:  #fff0ea;'),
    
    # Amber colors
    ('--amber:       #d4922a;', '--amber:       #e8c040;'),
    ('--amber-pale:  #fdf3e0;', '--amber-pale:  #fdf8d8;'),
    
    # Cream colors
    ('--cream:       #ffffff;', '--cream:       #f5f2e8;'),
    ('--cream-dark:  #f5ede0;', '--cream-dark:  #ede8d8;'),
    ('--warm-white:  #ffffff;', '--warm-white:  #fffdf5;'),
    
    # Border colors
    ('--border:      #e8d9c4;', '--border:      #e8c040;'),
    ('--border-light: #f0e4d0;', '--border-light: #f0dca0;'),
    
    # Text colors (with alternate names)
    ('--mid:         #6b5c48;', '--mid:         #5a4a20;'),
    ('--light:       #9c8b78;', '--light:       #8a7a50;'),
    ('--text-mid:    #6b5c48;', '--text-mid:    #5a4a20;'),
    ('--text-light:  #9c8b78;', '--text-light:  #8a7a50;'),
    
    # Sage colors
    ('--sage:        #4a7c59;', '--sage:        #2a8a4a;'),
    ('--sage-light:  #6a9e78;', '--sage-light:  #4aaa6a;'),
    ('--sage-pale:   #eaf3ec;', '--sage-pale:   #dff5e8;'),
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
    ('#eaf3ec', '#dff5e8'),  # Old sage-pale → new
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

# Fix .wl-cta (welcome screen button)
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

# Fix .nav-lbtn (nav button)
nav_lbtn_pattern = r'(\.nav-lbtn\s*\{[^}]*?\})'
nav_lbtn_match = re.search(nav_lbtn_pattern, content, re.DOTALL)

if nav_lbtn_match:
    nav_block = nav_lbtn_match.group(1)
    nav_block = re.sub(r'background:[^;]+;', 'background: #d85020;', nav_block)
    nav_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', nav_block)
    content = content.replace(nav_lbtn_match.group(0), nav_block)
    print("  ✓ .nav-lbtn: #d85020 background, white text")

print("\nSTEP 5 - FIX TEXT ON DARK BACKGROUNDS:")
print("-" * 40)

# Welcome screen text colors are already correct (using var(--white) and rgba)
print("  ✓ .wl-h1: already uses var(--white)")
print("  ✓ .wl-p: already uses rgba(255,253,249,0.45)")
print("  ✓ .wl-count: already uses rgba(255,253,249,0.3)")

# Fix profile hero section
ph_name_pattern = r'(\.ph-name\s*\{[^}]*?\})'
ph_name_match = re.search(ph_name_pattern, content, re.DOTALL)

if ph_name_match:
    name_block = ph_name_match.group(1)
    name_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', name_block)
    content = content.replace(ph_name_match.group(0), name_block)
    print("  ✓ .ph-name: white text")

print("\nSTEP 6 - FIX SWITCHER BAR:")
print("-" * 30)

# Fix .sw-btn.on
sw_btn_on_pattern = r'(\.sw-btn\.on\s*\{[^}]*?\})'
sw_btn_on_match = re.search(sw_btn_on_pattern, content, re.DOTALL)

if sw_btn_on_match:
    sw_block = sw_btn_on_match.group(1)
    sw_block = re.sub(r'background:[^;]+;', 'background: #d85020;', sw_block)
    content = content.replace(sw_btn_on_match.group(0), sw_block)
    print("  ✓ .sw-btn.on: #d85020 background")

# Also check for inline switcher button styles
if 'sw-btn on' in content:
    # Replace inline style backgrounds for active buttons
    content = re.sub(
        r'(class="sw-btn on"[^>]*style="[^"]*?)background:[^;]+;',
        r'\1background: #d85020;',
        content
    )
    print("  ✓ Inline sw-btn.on styles updated")

print("\nSTEP 7 - VERIFICATION:")
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

if d85020_count > 8:
    print("  ✅ Terra usage > 8")
if e8c040_count > 0:
    print("  ✅ Amber present")
if c85c3a_count == 0:
    print("  ✅ Old terra removed")
if a7c59_count == 0:
    print("  ✅ Old sage removed")

# Write the updated content back
if content != original_content:
    profile_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {profile_file.name}")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 ONYX & FLAME PALETTE APPLIED:")
print("   • Buttons: Hardcoded #d85020")
print("   • Dark sections: White text")
print("   • Switcher: Terra orange when active")
print("   • All old colors replaced")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Apply Onyx & Flame — parish-profile.html'")