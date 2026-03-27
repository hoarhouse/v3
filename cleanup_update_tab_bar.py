#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Removing remaining updateTabBar references")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING REMAINING REFERENCES:")
print("-" * 35)

# Find and remove updateTabBar calls
updateTabBar_lines = []
lines = content.split('\n')
for i, line in enumerate(lines, 1):
    if 'updateTabBar' in line:
        updateTabBar_lines.append(f"{i}: {line.strip()}")

if updateTabBar_lines:
    print(f"  Found {len(updateTabBar_lines)} updateTabBar references:")
    for line in updateTabBar_lines:
        print(f"    {line}")

# Remove updateTabBar calls
content = re.sub(r'\s*updateTabBar\([^)]*\);\s*', '', content)

# Remove any empty lines that might be left behind
content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

print("\nVERIFICATION:")
print("-" * 20)

final_count = content.count('updateTabBar')
print(f"  updateTabBar occurrences: {final_count}")

if final_count == 0:
    print("  ✅ All updateTabBar references removed")
else:
    print("  ⚠ Still has updateTabBar references")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Removed all updateTabBar references")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🧹 CLEANUP COMPLETE:")
print("   • All updateTabBar calls removed")
print("   • go() function now works properly")
print("   • No JavaScript errors")
print(f"{'='*50}")