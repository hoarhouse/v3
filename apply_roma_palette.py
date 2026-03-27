#!/usr/bin/env python3
from pathlib import Path

def apply_roma_palette_to_file(file_path):
    """Apply Roma color palette to a single file"""
    print(f"\n{'='*60}")
    print(f"PROCESSING: {file_path.name}")
    print(f"{'='*60}")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    print("\n1. BEFORE - Checking old color counts:")
    print("-" * 40)
    old_counts = {}
    old_colors = ["#1a1208", "#fffdf9", "#faf6f0", "#e8943a", "#3d3020", "#f2ebe0", "#fef3e8", "#e8ddd0", "#f0e8dc"]
    for color in old_colors:
        count = content.count(color)
        old_counts[color] = count
        print(f"  {color}: {count}")
    
    # CSS Variable replacements (with spaces)
    css_var_replacements = [
        ('--ink:          #1a1208', '--ink:          #1e1a14'),
        ('--ink-soft:     #3d3020', '--ink-soft:     #3a3228'),
        ('--cream:        #faf6f0', '--cream:        #faf7f2'),
        ('--cream-dark:   #f2ebe0', '--cream-dark:   #f2ece2'),
        ('--warm-white:   #fffdf9', '--warm-white:   #faf7f2'),
        ('--amber:        #e8943a', '--amber:        #e0a23a'),
        ('--amber-pale:   #fef3e8', '--amber-pale:   #fdf3e0'),
        ('--border:       #e8ddd0', '--border:       #ede4d6'),
        ('--border-light: #f0e8dc', '--border-light: #f5ede4'),
        ('--text-mid:     #6b5c48', '--text-mid:     #6b5c48'),  # No change
        ('--text-light:   #9c8b78', '--text-light:   #9c8b78'),  # No change
    ]
    
    # CSS Variable replacements (no spaces)
    css_var_no_spaces = [
        ('--ink:#1a1208', '--ink:#1e1a14'),
        ('--ink-soft:#3d3020', '--ink-soft:#3a3228'),
        ('--cream:#faf6f0', '--cream:#faf7f2'),
        ('--cream-dark:#f2ebe0', '--cream-dark:#f2ece2'),
        ('--warm-white:#fffdf9', '--warm-white:#faf7f2'),
        ('--amber:#e8943a', '--amber:#e0a23a'),
        ('--amber-pale:#fef3e8', '--amber-pale:#fdf3e0'),
        ('--border:#e8ddd0', '--border:#ede4d6'),
        ('--border-light:#f0e8dc', '--border-light:#f5ede4'),
    ]
    
    # Hardcoded hex replacements
    hex_replacements = [
        ('#1a1208', '#1e1a14'),
        ('#3d3020', '#3a3228'),
        ('#faf6f0', '#faf7f2'),
        ('#f2ebe0', '#f2ece2'),
        ('#fffdf9', '#faf7f2'),
        ('#e8943a', '#e0a23a'),
        ('#fef3e8', '#fdf3e0'),
        ('#e8ddd0', '#ede4d6'),
        ('#f0e8dc', '#f5ede4'),
    ]
    
    # RGBA replacements
    rgba_replacements = [
        ('rgba(26,18,8,', 'rgba(30,26,20,'),
    ]
    
    print("\n2. APPLYING REPLACEMENTS:")
    print("-" * 30)
    
    total_replacements = 0
    
    # Apply CSS variable replacements (with spaces)
    for old, new in css_var_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ CSS var (spaced): {old} → {new} ({count} times)")
            total_replacements += count
    
    # Apply CSS variable replacements (no spaces)
    for old, new in css_var_no_spaces:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ CSS var (no space): {old} → {new} ({count} times)")
            total_replacements += count
    
    # Apply hardcoded hex replacements
    for old, new in hex_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ Hardcoded hex: {old} → {new} ({count} times)")
            total_replacements += count
    
    # Apply RGBA replacements
    for old, new in rgba_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ RGBA: {old} → {new} ({count} times)")
            total_replacements += count
    
    if total_replacements == 0:
        print("  No replacements needed")
    
    print("\n3. AFTER - Checking new color counts:")
    print("-" * 40)
    new_counts = {}
    new_colors = ["#1e1a14", "#faf7f2", "#e0a23a", "#3a3228", "#f2ece2", "#fdf3e0", "#ede4d6", "#f5ede4"]
    for color in new_colors:
        count = content.count(color)
        new_counts[color] = count
        print(f"  {color}: {count}")
    
    # Write the updated content back
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"\n✅ Updated {file_path.name} ({total_replacements} replacements)")
        return True
    else:
        print(f"\n⚠ No changes were made to {file_path.name}")
        return False

def verify_palette_changes(file_path):
    """Verify that old colors are gone and new colors are present"""
    print(f"\n4. VERIFICATION for {file_path.name}:")
    print("-" * 30)
    
    content = file_path.read_text(encoding='utf-8')
    
    # Check old colors should be 0
    old_checks = [
        ("#1a1208", "should be 0"),
        ("#fffdf9", "should be 0"),
        ("#faf6f0", "should be 0"),
        ("#e8943a", "should be 0")
    ]
    
    # Check new colors should be > 0
    new_checks = [
        ("#1e1a14", "should be > 0"),
        ("#faf7f2", "should be > 0")
    ]
    
    verification_passed = True
    
    for color, expectation in old_checks:
        count = content.count(color)
        status = "✅" if count == 0 else "❌"
        print(f"  {status} {color}: {count} ({expectation})")
        if count != 0:
            verification_passed = False
    
    for color, expectation in new_checks:
        count = content.count(color)
        status = "✅" if count > 0 else "❌"
        print(f"  {status} {color}: {count} ({expectation})")
        if count == 0:
            verification_passed = False
    
    print(f"\n  Overall verification: {'PASS' if verification_passed else 'FAIL'}")
    return verification_passed

# Main execution
print("ROMA COLOR PALETTE APPLICATION")
print("=" * 60)

v3_dir = Path("/Users/christopherhoar/Desktop/v3")
files_to_process = [
    "communio.html",
    "communio-register.html", 
    "parish-profile.html",
    "communio-dashboard.html"
]

for filename in files_to_process:
    file_path = v3_dir / filename
    
    if not file_path.exists():
        print(f"❌ {filename} not found!")
        continue
    
    # Apply palette changes
    changes_made = apply_roma_palette_to_file(file_path)
    
    # Verify results
    verification_passed = verify_palette_changes(file_path)
    
    print(f"\n📝 SUMMARY FOR {filename}:")
    print(f"   Changes made: {'Yes' if changes_made else 'No'}")
    print(f"   Verification: {'PASS' if verification_passed else 'FAIL'}")
    print(f"   Ready to commit: {'Yes' if verification_passed else 'No'}")

print(f"\n{'='*60}")
print("COMPLETION STATUS")
print(f"{'='*60}")
print("✅ All four Communio files processed with Roma palette")
print("📋 Next steps:")
print("   1. Commit communio.html with message: 'Apply Roma palette — communio.html'")
print("   2. Commit communio-register.html with message: 'Apply Roma palette — communio-register.html'") 
print("   3. Commit parish-profile.html with message: 'Apply Roma palette — parish-profile.html'")
print("   4. Commit communio-dashboard.html with message: 'Apply Roma palette — communio-dashboard.html'")
print("   5. Test at hoarhouse.github.io/v3/communio.html after 3-5 minutes")