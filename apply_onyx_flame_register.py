#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
register_file = Path("/Users/christopherhoar/Desktop/v3/communio-register.html")

print("Applying Onyx & Flame palette to communio-register.html")
print("=" * 60)

# Read the file
content = register_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - UPDATE CSS VARIABLES:")
print("-" * 35)

# CSS Variable replacements (based on current format)
css_replacements = [
    # Core colors
    ('--ink:          #16120c;', '--ink:          #000000;'),
    ('--ink-soft:     #2e2518;', '--ink-soft:     #111111;'),
    
    # Terra colors
    ('--terracotta:   #c85c3a;', '--terracotta:   #d85020;'),
    ('--terra-light:  #e8856a;', '--terra-light:  #f07040;'),
    ('--terra-pale:   #fceee9;', '--terra-pale:   #fff0ea;'),
    
    # Amber colors
    ('--amber:        #d4922a;', '--amber:        #e8c040;'),
    ('--amber-pale:   #fdf3e0;', '--amber-pale:   #fdf8d8;'),
    
    # Cream colors
    ('--cream:        #ffffff;', '--cream:        #f5f2e8;'),
    ('--cream-dark:   #f5ede0;', '--cream-dark:   #ede8d8;'),
    ('--warm-white:   #ffffff;', '--warm-white:   #fffdf5;'),
    
    # Border colors
    ('--border:       #e8d9c4;', '--border:       #e8c040;'),
    ('--border-light: #f0e4d0;', '--border-light: #f0dca0;'),
    
    # Text colors
    ('--text-mid:     #6b5c48;', '--text-mid:     #5a4a20;'),
    ('--text-light:   #9c8b78;', '--text-light:   #8a7a50;'),
    
    # Sage colors
    ('--sage:         #4a7c59;', '--sage:         #2a8a4a;'),
    ('--sage-light:   #6a9e78;', '--sage-light:   #4aaa6a;'),
    ('--sage-pale:    #eaf3ec;', '--sage-pale:    #dff5e8;'),
    
    # Success (update to new sage)
    ('--success:        #4a7c59;', '--success:        #2a8a4a;'),
]

for old, new in css_replacements:
    if old in content:
        content = content.replace(old, new)
        var_name = old.split(':')[0]
        print(f"  ✓ {var_name} updated")

print("\nSTEP 2 - REPLACE HARDCODED HEX VALUES:")
print("-" * 40)

# Hardcoded hex replacements
hex_replacements = [
    ('#c85c3a', '#d85020'),  # Old terra → new terra
    ('#4a7c59', '#2a8a4a'),  # Old sage → new sage
    ('#6b5c48', '#5a4a20'),  # Old text-mid → new
    ('#9c8b78', '#8a7a50'),  # Old text-light → new
]

for old, new in hex_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")

print("\nSTEP 3 - FIX ALL BUTTONS WITH HARDCODED HEX:")
print("-" * 45)

# Fix .btn-primary
btn_primary_pattern = r'(\.btn-primary\s*\{[^}]*?\})'
btn_primary_match = re.search(btn_primary_pattern, content, re.DOTALL)

if btn_primary_match:
    btn_block = btn_primary_match.group(1)
    btn_block = re.sub(r'background:[^;]+;', 'background: #d85020;', btn_block)
    if 'color:' not in btn_block:
        btn_block = btn_block.replace('}', '  color: #ffffff;\n    }')
    else:
        btn_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', btn_block)
    content = content.replace(btn_primary_match.group(0), btn_block)
    print("  ✓ .btn-primary: #d85020 background, white text")

# Fix .btn-submit
btn_submit_pattern = r'(\.btn-submit\s*\{[^}]*?\})'
btn_submit_match = re.search(btn_submit_pattern, content, re.DOTALL)

if btn_submit_match:
    submit_block = btn_submit_match.group(1)
    submit_block = re.sub(r'background:[^;]+;', 'background: #000000;', submit_block)
    submit_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', submit_block)
    content = content.replace(btn_submit_match.group(0), submit_block)
    print("  ✓ .btn-submit: black background, white text")

# Fix .btn-primary:hover
btn_hover_pattern = r'(\.btn-primary:hover\s*\{[^}]*?\})'
btn_hover_match = re.search(btn_hover_pattern, content, re.DOTALL)

if btn_hover_match:
    hover_block = btn_hover_match.group(1)
    hover_block = re.sub(r'background:[^;]+;', 'background: #f07040;', hover_block)
    content = content.replace(btn_hover_match.group(0), hover_block)
    print("  ✓ .btn-primary:hover: #f07040 background")

# Fix .nav-btn
nav_btn_pattern = r'(\.nav-btn\s*\{[^}]*?\})'
nav_btn_match = re.search(nav_btn_pattern, content, re.DOTALL)

if nav_btn_match:
    nav_block = nav_btn_match.group(1)
    nav_block = re.sub(r'background:[^;]+;', 'background: #d85020;', nav_block)
    nav_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', nav_block)
    content = content.replace(nav_btn_match.group(0), nav_block)
    print("  ✓ .nav-btn: #d85020 background, white text")

print("\nSTEP 4 - FIX TEXT ON DARK BACKGROUNDS:")
print("-" * 40)

# Fix header text colors
header_title_pattern = r'(\.header-title\s*\{[^}]*?\})'
header_title_match = re.search(header_title_pattern, content, re.DOTALL)

if header_title_match:
    title_block = header_title_match.group(1)
    title_block = re.sub(r'color:[^;]+;', 'color: #ffffff;', title_block)
    content = content.replace(header_title_match.group(0), title_block)
    print("  ✓ .header-title: white text")

header_desc_pattern = r'(\.header-desc\s*\{[^}]*?\})'
header_desc_match = re.search(header_desc_pattern, content, re.DOTALL)

if header_desc_match:
    desc_block = header_desc_match.group(1)
    desc_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.6);', desc_block)
    content = content.replace(header_desc_match.group(0), desc_block)
    print("  ✓ .header-desc: light white text")

# Fix header tag color
header_tag_pattern = r'(\.header-tag\s*\{[^}]*?\})'
header_tag_match = re.search(header_tag_pattern, content, re.DOTALL)

if header_tag_match:
    tag_block = header_tag_match.group(1)
    tag_block = re.sub(r'color:[^;]+;', 'color: #e8c040;', tag_block)
    content = content.replace(header_tag_match.group(0), tag_block)
    print("  ✓ .header-tag: gold color")

# Fix h-pill
h_pill_pattern = r'(\.h-pill\s*\{[^}]*?\})'
h_pill_match = re.search(h_pill_pattern, content, re.DOTALL)

if h_pill_match:
    pill_block = h_pill_match.group(1)
    pill_block = re.sub(r'color:[^;]+;', 'color: rgba(255,255,255,0.7);', pill_block)
    content = content.replace(h_pill_match.group(0), pill_block)
    print("  ✓ .h-pill: light white text")

# Progress bar fixes
prog_active_pattern = r'(\.prog-step\.active\s+\.prog-num\s*\{[^}]*?\})'
prog_active_match = re.search(prog_active_pattern, content, re.DOTALL)

if prog_active_match:
    prog_block = prog_active_match.group(1)
    prog_block = re.sub(r'background:[^;]+;', 'background: #d85020;', prog_block)
    content = content.replace(prog_active_match.group(0), prog_block)
    print("  ✓ .prog-step.active: #d85020 background")

print("\nSTEP 5 - FIX FOCUS/ACTIVE STATES:")
print("-" * 35)

# Fix input focus states
input_focus_pattern = r'(\.field\s+input:focus\s*\{[^}]*?\})'
input_focus_match = re.search(input_focus_pattern, content, re.DOTALL)

if input_focus_match:
    focus_block = input_focus_match.group(1)
    focus_block = re.sub(r'border-color:[^;]+;', 'border-color: #d85020;', focus_block)
    focus_block = re.sub(r'box-shadow:[^;]+;', 'box-shadow: 0 0 0 3px rgba(216,80,32,0.15);', focus_block)
    content = content.replace(input_focus_match.group(0), focus_block)
    print("  ✓ Input focus: #d85020 border")

# Fix checked radio/checkbox
checked_pattern = r'(\.focus-opt\s+input:checked\s*\+\s*label\s*\{[^}]*?\})'
checked_match = re.search(checked_pattern, content, re.DOTALL)

if checked_match:
    checked_block = checked_match.group(1)
    checked_block = re.sub(r'border-color:[^;]+;', 'border-color: #d85020;', checked_block)
    checked_block = re.sub(r'background:[^;]+;', 'background: #fff0ea;', checked_block)
    content = content.replace(checked_match.group(0), checked_block)
    print("  ✓ Checked inputs: #d85020 border, terra-pale bg")

print("\nSTEP 6 - VERIFICATION:")
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

if d85020_count > 5:
    print("  ✅ Terra usage > 5")
if e8c040_count > 0:
    print("  ✅ Amber present")
if c85c3a_count == 0:
    print("  ✅ Old terra removed")
if a7c59_count == 0:
    print("  ✅ Old sage removed")

# Write the updated content back
if content != original_content:
    register_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {register_file.name}")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔥 ONYX & FLAME PALETTE APPLIED:")
print("   • Buttons: Hardcoded #d85020 (no variables)")
print("   • Dark sections: White text")
print("   • Focus states: Terra orange")
print("   • All old colors replaced")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Apply Onyx & Flame — communio-register.html'")