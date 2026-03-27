#!/usr/bin/env python3
from pathlib import Path
import subprocess

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Applying Onyx & Flame palette to communio.html")
print("=" * 50)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 — BEFORE - Checking current color values:")
print("-" * 50)

# Check some key current values
key_colors = ["#16120c", "#c85c3a", "#4a7c59", "#d4922a", "#ffffff"]
before_counts = {}
for color in key_colors:
    count = content.count(color)
    before_counts[color] = count
    print(f"  {color}: {count}")

print("\nSTEP 1 — UPDATE CSS VARIABLE DECLARATIONS:")
print("-" * 45)

# Define the Onyx & Flame palette replacements
# Based on the current format we found: --var:    #value;
variable_replacements = [
    # Ink colors - darker, richer blacks
    ('--ink:          #16120c;', '--ink:          #000000;'),
    ('--ink-soft:     #2e2518;', '--ink-soft:     #111111;'),
    
    # Terra colors - more vibrant orange/red
    ('--terracotta:   #c85c3a;', '--terracotta:   #d85020;'),
    ('--terra-light:  #e8856a;', '--terra-light:  #f07040;'),
    ('--terra-pale:   #fceee9;', '--terra-pale:   #fff0ea;'),
    
    # Amber colors - brighter, more golden
    ('--amber:        #d4922a;', '--amber:        #e8c040;'),
    ('--amber-pale:   #fdf3e0;', '--amber-pale:   #fdf8d8;'),
    
    # Cream/white colors - softer, warmer
    ('--cream:        #ffffff;', '--cream:        #f5f2e8;'),
    ('--cream-dark:   #f5ede0;', '--cream-dark:   #ede8d8;'),
    ('--warm-white:   #faf7f2;', '--warm-white:   #fffdf5;'),
    
    # Border colors - golden tones
    ('--border:       #e8d9c4;', '--border:       #e8c040;'),
    ('--border-light: #f0e4d0;', '--border-light: #f0dca0;'),
    
    # Text colors - warmer browns
    ('--text-mid:     #6b5c48;', '--text-mid:     #5a4a20;'),
    ('--text-light:   #9c8b78;', '--text-light:   #8a7a50;'),
    
    # Sage colors - richer greens
    ('--sage:         #4a7c59;', '--sage:         #2a8a4a;'),
    ('--sage-light:   #6a9e78;', '--sage-light:   #4aaa6a;'),
    ('--sage-pale:    #eaf3ec;', '--sage-pale:    #dff5e8;'),
]

# Also handle any unspaced formats that might exist
unspaced_replacements = [
    ('--ink:#16120c;', '--ink:#000000;'),
    ('--ink-soft:#2e2518;', '--ink-soft:#111111;'),
    ('--terracotta:#c85c3a;', '--terracotta:#d85020;'),
    ('--terra-light:#e8856a;', '--terra-light:#f07040;'),
    ('--terra-pale:#fceee9;', '--terra-pale:#fff0ea;'),
    ('--amber:#d4922a;', '--amber:#e8c040;'),
    ('--amber-pale:#fdf3e0;', '--amber-pale:#fdf8d8;'),
    ('--cream:#ffffff;', '--cream:#f5f2e8;'),
    ('--cream-dark:#f5ede0;', '--cream-dark:#ede8d8;'),
    ('--warm-white:#faf7f2;', '--warm-white:#fffdf5;'),
    ('--border:#e8d9c4;', '--border:#e8c040;'),
    ('--border-light:#f0e4d0;', '--border-light:#f0dca0;'),
    ('--text-mid:#6b5c48;', '--text-mid:#5a4a20;'),
    ('--text-light:#9c8b78;', '--text-light:#8a7a50;'),
    ('--sage:#4a7c59;', '--sage:#2a8a4a;'),
    ('--sage-light:#6a9e78;', '--sage-light:#4aaa6a;'),
    ('--sage-pale:#eaf3ec;', '--sage-pale:#dff5e8;'),
]

total_variable_changes = 0

# Apply spaced variable replacements
for old, new in variable_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")
        total_variable_changes += count

# Apply unspaced variable replacements
for old, new in unspaced_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")
        total_variable_changes += count

print(f"\nTotal CSS variable changes: {total_variable_changes}")

print("\nSTEP 2 — REPLACE HARDCODED HEX VALUES:")
print("-" * 40)

# Replace hardcoded hex values outside :root block
hardcoded_replacements = [
    ('#16120c', '#000000'),  # Current ink → Onyx black
    ('#2e2518', '#111111'),  # Current ink-soft → Dark gray
    ('#c85c3a', '#d85020'),  # Current terracotta → Flame orange
    ('#4a7c59', '#2a8a4a'),  # Current sage → Rich green
    ('#d4922a', '#e8c040'),  # Current amber → Golden yellow
    ('#ffffff', '#f5f2e8'),  # Pure white → Warm cream (except where we want pure white)
]

# RGBA replacements
rgba_replacements = [
    ('rgba(22,18,12,', 'rgba(0,0,0,'),    # Old ink rgba → Pure black
    ('rgba(46,37,24,', 'rgba(17,17,17,'), # Old ink-soft rgba → Dark gray
]

total_hardcoded_changes = 0

# Apply hardcoded hex replacements
for old, new in hardcoded_replacements:
    # Skip if it's in a CSS variable declaration (already handled)
    if f'--' in old or old in ['#ffffff']:  # Keep some whites pure
        continue
    
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")
        total_hardcoded_changes += count

# Apply RGBA replacements
for old, new in rgba_replacements:
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ {old} → {new} ({count} times)")
        total_hardcoded_changes += count

print(f"\nTotal hardcoded value changes: {total_hardcoded_changes}")

print("\nSTEP 3 — AFTER - Checking new color values:")
print("-" * 45)

# Check new Onyx & Flame colors
onyx_flame_colors = ["#000000", "#d85020", "#e8c040", "#2a8a4a", "#f5f2e8"]
after_counts = {}
for color in onyx_flame_colors:
    count = content.count(color)
    after_counts[color] = count
    print(f"  {color}: {count}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print(f"   CSS variables changed: {total_variable_changes}")
    print(f"   Hardcoded values changed: {total_hardcoded_changes}")
    print(f"   Total changes: {total_variable_changes + total_hardcoded_changes}")
else:
    print(f"\n⚠ No changes were made to {communio_file.name}")

print("\nSTEP 3 — VERIFICATION:")
print("-" * 25)

# Verify key colors
verification_checks = [
    ("#d85020", "should be > 0"),
    ("#e8c040", "should be > 0"),
    ("#000000", "should be > 0"),
    ("#c85c3a", "should be 0"),
    ("#4a7c59", "should be 0"),
]

for color, expectation in verification_checks:
    try:
        result = subprocess.run([
            'grep', '-c', color, str(communio_file)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            count = int(result.stdout.strip())
        else:
            count = 0
        
        if "should be > 0" in expectation:
            status = "✅" if count > 0 else "❌"
        else:  # should be 0
            status = "✅" if count == 0 else "❌"
        
        print(f"  {status} {color}: {count} ({expectation})")
        
    except Exception as e:
        print(f"  ❌ Error checking {color}: {e}")

print(f"\n{'='*50}")
print("🔥 ONYX & FLAME PALETTE APPLIED:")
print("   • Ink colors: Pure black (#000000) and dark gray (#111111)")
print("   • Terra colors: Vibrant flame orange (#d85020, #f07040)")
print("   • Amber colors: Bright golden yellow (#e8c040)")
print("   • Sage colors: Rich forest green (#2a8a4a, #4aaa6a)")
print("   • Cream colors: Warm, soft tones (#f5f2e8, #ede8d8)")
print("   • Border colors: Golden accent (#e8c040, #f0dca0)")
print(f"{'='*50}")
print("🚀 Ready to commit communio.html in GitHub Desktop")
print("📝 Message: 'Test Onyx & Flame palette — communio.html'")
print("🌐 Test at hoarhouse.github.io/v3/communio.html in 3-5 minutes")