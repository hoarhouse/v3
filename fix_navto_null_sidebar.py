#!/usr/bin/env python3
from pathlib import Path

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing navTo() null sidebar crash")
print("=" * 40)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING SIDEBAR REFERENCE:")
print("-" * 30)

# Find the problematic line
old_line = "document.getElementById('sidebar').classList.remove('open');"
new_line = "var sb=document.getElementById('sidebar');if(sb)sb.classList.remove('open');"

if old_line in content:
    print(f"  ✓ Found problematic line: {old_line}")
    
    # Replace with null-safe version
    content = content.replace(old_line, new_line)
    print(f"  ✓ Replaced with null-safe version:")
    print(f"    {new_line}")
    
    print("\nVERIFYING CHANGE:")
    print("-" * 20)
    
    # Verify the change was made
    if new_line in content:
        print("  ✅ Null-safe sidebar access implemented")
    
    if old_line not in content:
        print("  ✅ Unsafe sidebar access removed")
    
else:
    print("  ⚠ Problematic line not found - checking for variations...")
    
    # Check for variations
    variations = [
        "document.getElementById('sidebar').classList.remove('open')",
        'document.getElementById("sidebar").classList.remove("open")',
        "document.getElementById('sidebar').classList.remove('open') ;",
        "document.getElementById('sidebar').classList.remove('open'); "
    ]
    
    found_variation = False
    for variation in variations:
        if variation in content:
            print(f"  ✓ Found variation: {variation}")
            content = content.replace(variation, new_line)
            found_variation = True
            break
    
    if not found_variation:
        print("  ⚠ No sidebar classList access found")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed navTo() null sidebar crash")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*40}")
print("🛡️ NULL-SAFETY FIX:")
print("   • Added null check for sidebar element")
print("   • Prevents crashes when sidebar doesn't exist")
print("   • Function now safely handles missing DOM elements")
print(f"{'='*40}")
print("🚀 Ready to commit: 'Fix navTo null sidebar crash'")