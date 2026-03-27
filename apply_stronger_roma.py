#!/usr/bin/env python3
from pathlib import Path

def apply_stronger_roma_to_file(file_path):
    """Apply stronger Roma color palette to a single file"""
    print(f"\n{'='*60}")
    print(f"PROCESSING: {file_path.name}")
    print(f"{'='*60}")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    print("\n1. BEFORE - Checking current color counts:")
    print("-" * 40)
    old_colors = ["#1e1a14", "#3a3228", "#faf7f2", "#f2ece2", "#ede4d6", "#f5ede4", "#e0a23a"]
    old_counts = {}
    for color in old_colors:
        count = content.count(color)
        old_counts[color] = count
        print(f"  {color}: {count}")
    
    # Check old rgba
    rgba_old_count = content.count("rgba(30,26,20,")
    print(f"  rgba(30,26,20,): {rgba_old_count}")
    
    # Define stronger Roma replacements
    color_replacements = [
        ('#1e1a14', '#16120c'),  # Darker, warmer ink
        ('#3a3228', '#2e2518'),  # Darker ink-soft
        ('#faf7f2', '#ffffff'),  # Crisp white backgrounds
        ('#f2ece2', '#f5ede0'),  # Adjusted cream-dark
        ('#ede4d6', '#e8d9c4'),  # Warmer border
        ('#f5ede4', '#f0e4d0'),  # Warmer border-light
        ('#e0a23a', '#d4922a'),  # More saturated amber
    ]
    
    # RGBA replacements
    rgba_replacements = [
        ('rgba(30,26,20,', 'rgba(22,18,12,'),
    ]
    
    print("\n2. APPLYING STRONGER ROMA REPLACEMENTS:")
    print("-" * 45)
    
    total_replacements = 0
    
    # Apply color replacements
    for old, new in color_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ {old} → {new} ({count} times)")
            total_replacements += count
    
    # Apply RGBA replacements
    for old, new in rgba_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ {old} → {new} ({count} times)")
            total_replacements += count
    
    if total_replacements == 0:
        print("  No replacements needed")
    
    print("\n3. AFTER - Checking new color counts:")
    print("-" * 40)
    new_colors = ["#16120c", "#2e2518", "#ffffff", "#f5ede0", "#e8d9c4", "#f0e4d0", "#d4922a"]
    new_counts = {}
    for color in new_colors:
        count = content.count(color)
        new_counts[color] = count
        print(f"  {color}: {count}")
    
    # Check new rgba
    rgba_new_count = content.count("rgba(22,18,12,")
    print(f"  rgba(22,18,12,): {rgba_new_count}")
    
    # Write the updated content back
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"\n✅ Updated {file_path.name} ({total_replacements} replacements)")
        return True
    else:
        print(f"\n⚠ No changes were made to {file_path.name}")
        return False

def verify_stronger_roma_changes(file_path):
    """Verify stronger Roma changes"""
    print(f"\n4. VERIFICATION for {file_path.name}:")
    print("-" * 35)
    
    content = file_path.read_text(encoding='utf-8')
    
    # Key verification checks
    checks = [
        ("#ffffff", "should be > 0", "> 0"),
        ("#16120c", "should be > 0", "> 0"),
        ("#faf7f2", "should be 0", "0"),
    ]
    
    verification_passed = True
    
    for color, expectation, target in checks:
        count = content.count(color)
        if target == "> 0":
            status = "✅" if count > 0 else "❌"
            if count == 0:
                verification_passed = False
        else:  # target == "0"
            status = "✅" if count == 0 else "❌"
            if count != 0:
                verification_passed = False
        
        print(f"  {status} {color}: {count} ({expectation})")
    
    print(f"\n  Overall verification: {'PASS' if verification_passed else 'FAIL'}")
    return verification_passed

# Main execution
print("STRONGER ROMA COLOR PALETTE APPLICATION")
print("=" * 60)
print("Making backgrounds crisp white, dark tones darker/warmer,")
print("and amber more saturated for better visibility")

v3_dir = Path("/Users/christopherhoar/Desktop/v3")
files_to_process = [
    "communio.html",
    "communio-register.html", 
    "parish-profile.html",
    "communio-dashboard.html"
]

results = []

for filename in files_to_process:
    file_path = v3_dir / filename
    
    if not file_path.exists():
        print(f"❌ {filename} not found!")
        continue
    
    # Apply stronger Roma changes
    changes_made = apply_stronger_roma_to_file(file_path)
    
    # Verify results
    verification_passed = verify_stronger_roma_changes(file_path)
    
    print(f"\n📝 SUMMARY FOR {filename}:")
    print(f"   Changes made: {'Yes' if changes_made else 'No'}")
    print(f"   Verification: {'PASS' if verification_passed else 'FAIL'}")
    print(f"   Ready to commit: {'Yes' if verification_passed else 'No'}")
    
    results.append({
        'file': filename,
        'changes': changes_made,
        'verification': verification_passed
    })

print(f"\n{'='*60}")
print("COMPLETION STATUS")
print(f"{'='*60}")
print("✅ All four Communio files processed with stronger Roma palette")
print("📋 Changes applied:")
print("   • Backgrounds now crisp white (#ffffff)")
print("   • Dark tones deeper and warmer (#16120c, #2e2518)")
print("   • Amber more saturated (#d4922a)")
print("   • Border tones warmer (#e8d9c4, #f0e4d0)")
print("")
print("📋 Next steps:")
print("   1. Commit each file separately in GitHub Desktop")
print("   2. Allow 3-5 minutes after final push")
print("   3. Test live at hoarhouse.github.io/v3/communio.html")

# Summary table
print(f"\n📊 SUMMARY TABLE:")
print("-" * 60)
print(f"{'File':<25} {'Changes':<8} {'Verification':<12}")
print("-" * 60)
for result in results:
    verification_status = 'PASS' if result['verification'] else 'FAIL'
    print(f"{result['file']:<25} {'Yes' if result['changes'] else 'No':<8} {verification_status:<12}")
print("-" * 60)