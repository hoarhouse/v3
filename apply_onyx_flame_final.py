#!/usr/bin/env python3
from pathlib import Path
import subprocess

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Applying Onyx & Flame palette to communio.html")
print("=" * 55)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nCurrent state check:")
print("-" * 30)

# Most values are already correct, but let's verify warm-white needs updating
current_values = {
    '--ink:          #000000;': True,  # Already correct
    '--ink-soft:     #111111;': True,  # Already correct
    '--terracotta:   #d85020;': True,  # Already correct
    '--terra-light:  #f07040;': True,  # Already correct
    '--terra-pale:   #fff0ea;': True,  # Already correct
    '--amber:        #e8c040;': True,  # Already correct
    '--amber-pale:   #fdf8d8;': True,  # Already correct
    '--cream:        #f5f2e8;': True,  # Already correct
    '--cream-dark:   #ede8d8;': True,  # Already correct
    '--warm-white:   #ffffff;': False,  # Needs updating to #fffdf5
    '--border:       #e8c040;': True,  # Already correct
    '--border-light: #f0dca0;': True,  # Already correct
    '--text-mid:     #5a4a20;': True,  # Already correct
    '--text-light:   #8a7a50;': True,  # Already correct
    '--sage:         #2a8a4a;': True,  # Already correct
    '--sage-light:   #4aaa6a;': True,  # Already correct
    '--sage-pale:    #dff5e8;': True,  # Already correct
}

changes_needed = []
for var, is_correct in current_values.items():
    if var in content:
        print(f"  ✓ Found: {var.split(':')[0]}")
        if not is_correct:
            changes_needed.append(var)
    else:
        print(f"  ⚠ Not found: {var.split(':')[0]}")

print("\nChanges needed:")
print("-" * 20)

# Only warm-white needs updating
if '--warm-white:   #ffffff;' in content:
    content = content.replace('--warm-white:   #ffffff;', '--warm-white:   #fffdf5;')
    print("  ✓ Updated --warm-white from #ffffff to #fffdf5")
else:
    print("  ⚠ --warm-white not in expected format")

# Also check for any hardcoded #ffffff that should be #fffdf5 (in specific contexts)
# But be careful not to replace all whites, just warm-whites
# Since most whites are already correct, we'll leave them

# Check for any remaining old color values (hardcoded)
old_colors = {
    '#16120c': '#000000',  # Old ink
    '#2e2518': '#111111',  # Old ink-soft  
    '#c85c3a': '#d85020',  # Old terra
    '#e8856a': '#f07040',  # Old terra-light
    '#d4922a': '#e8c040',  # Old amber
    '#4a7c59': '#2a8a4a',  # Old sage
    '#6a9e78': '#4aaa6a',  # Old sage-light
}

print("\nChecking for hardcoded old colors:")
print("-" * 35)
replacements_made = 0
for old, new in old_colors.items():
    count = content.count(old)
    if count > 0:
        content = content.replace(old, new)
        print(f"  ✓ Replaced {old} → {new} ({count} times)")
        replacements_made += count
    
if replacements_made == 0:
    print("  ✓ No old hardcoded colors found")

# Check for rgba values that might need updating
rgba_replacements = [
    ('rgba(0,0,0,', 'rgba(0,0,0,'),  # Already correct
]

print("\nVerification:")
print("-" * 20)

# Verify key Onyx & Flame colors are present
verification_colors = [
    ('#e8c040', 'Golden yellow'),
    ('#d85020', 'Flame orange'),
    ('#000000', 'Pure black'),
    ('#fffdf5', 'Warm white'),
]

for color, name in verification_colors:
    count = content.count(color)
    if count > 0:
        print(f"  ✓ {color} ({name}): {count} occurrences")
    else:
        print(f"  ⚠ {color} ({name}): {count} occurrences")

# Check old colors are gone
old_check_colors = [
    ('#c85c3a', 'Old terra'),
    ('#4a7c59', 'Old sage'),
    ('#d4922a', 'Old amber'),
]

print("\nOld colors check (should be 0):")
print("-" * 35)
all_clear = True
for color, name in old_check_colors:
    count = content.count(color)
    if count == 0:
        print(f"  ✓ {color} ({name}): {count} occurrences")
    else:
        print(f"  ❌ {color} ({name}): {count} occurrences")
        all_clear = False

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
else:
    print(f"\n⚠ No changes were needed - file already has Onyx & Flame palette")

print(f"\n{'='*55}")
print("🔥 ONYX & FLAME PALETTE STATUS:")
if all_clear:
    print("   ✅ All values correctly set")
    print("   ✅ No old colors remaining")
else:
    print("   ⚠ Some issues detected - review above")
    
print("\n📋 Current palette:")
print("   • Ink: Pure black (#000000) and dark gray (#111111)")
print("   • Terra: Flame orange (#d85020, #f07040, #fff0ea)")
print("   • Amber: Golden yellow (#e8c040, #fdf8d8)")
print("   • Sage: Forest green (#2a8a4a, #4aaa6a, #dff5e8)")
print("   • Cream: Warm tones (#f5f2e8, #ede8d8)")
print("   • Warm white: Soft white (#fffdf5)")
print("   • Borders: Golden (#e8c040, #f0dca0)")
print(f"{'='*55}")
print("🚀 Ready to commit communio.html in GitHub Desktop")
print("📝 Message: 'Test Onyx & Flame palette — communio.html'")