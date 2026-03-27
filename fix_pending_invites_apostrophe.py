#!/usr/bin/env python3
from pathlib import Path

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing pending invites apostrophe - removing backslash")
print("=" * 55)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING TARGET STRING:")
print("-" * 30)

# Find the exact problematic string
old_string = "(pendingInvites.length !== 1 ? \\'s' : '')"
new_string = "(pendingInvites.length !== 1 ? 's' : '')"

if old_string in content:
    print(f"  ✓ Found: {old_string}")
    
    # Replace with the fixed version
    content = content.replace(old_string, new_string)
    print(f"  ✓ Replaced with: {new_string}")
    
    print("\nVERIFYING CHANGE:")
    print("-" * 20)
    
    # Verify the change was made
    if new_string in content:
        print("  ✅ Clean apostrophe version found")
    
    if old_string not in content:
        print("  ✅ Escaped apostrophe version removed")
    
else:
    print(f"  ⚠ Target string not found: {old_string}")
    # Check for variations
    variations = [
        "(pendingInvites.length !== 1 ? \\'s' : \\'\\')",
        "(pendingInvites.length !== 1 ? \\'s\\' : \\'\\')",
        "(pendingInvites.length !== 1 ? \\'s' : '')"
    ]
    
    found_variation = False
    for variation in variations:
        if variation in content:
            print(f"  ✓ Found variation: {variation}")
            content = content.replace(variation, new_string)
            found_variation = True
            break
    
    if not found_variation:
        print("  ⚠ No variations found")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed pending invites apostrophe")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*55}")
print("🔧 APOSTROPHE FIX:")
print("   • Removed backslash before 's' in pending invites")
print("   • Clean apostrophe now safely in string")
print("   • JavaScript string concatenation fixed")
print(f"{'='*55}")
print("🚀 Ready to verify with grep and balance check")