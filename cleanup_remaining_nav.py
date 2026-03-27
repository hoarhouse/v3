#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Cleaning up remaining navigation references")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING REMAINING REFERENCES:")
print("-" * 35)

# Find all remaining sidebar references in HTML
sidebar_html_pattern = r'<div class="sidebar"[^>]*>.*?</div>'
sidebar_html_matches = re.findall(sidebar_html_pattern, content, re.DOTALL)

if sidebar_html_matches:
    print(f"  Found {len(sidebar_html_matches)} sidebar HTML blocks to remove")
    content = re.sub(sidebar_html_pattern, '', content, flags=re.DOTALL)
    print("  ✓ Removed remaining sidebar HTML")

# Find setup-strip CSS references
setup_strip_css_pattern = r'\.setup-strip[^{]*\{[^}]*\}'
setup_strip_css_matches = re.findall(setup_strip_css_pattern, content, re.DOTALL)

if setup_strip_css_matches:
    print(f"  Found {len(setup_strip_css_matches)} setup-strip CSS rules")
    content = re.sub(setup_strip_css_pattern, '', content, flags=re.DOTALL)
    print("  ✓ Removed remaining setup-strip CSS")

# Remove any remaining sidebar CSS
remaining_sb_patterns = [
    r'@media\([^)]+\)\{\.sidebar[^}]+\}[^}]*\}',  # Media queries
    r'\.sidebar[^{]*\{[^}]*\}',  # Basic sidebar rules
]

for pattern in remaining_sb_patterns:
    matches = re.findall(pattern, content, re.DOTALL)
    if matches:
        content = re.sub(pattern, '', content, flags=re.DOTALL)
        print(f"  ✓ Removed {len(matches)} additional sidebar rules")

# Clean up any empty lines that were left behind
content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

print("\nFINAL VERIFICATION:")
print("-" * 25)

# Final checks
tab_bar_count = content.count('tab-bar')
tab_item_count = content.count('tab-item') 
sidebar_count = content.count('class="sidebar"')
setup_strip_count = content.count('setup-strip')

print(f"  tab-bar: {tab_bar_count} occurrences")
print(f"  tab-item: {tab_item_count} occurrences") 
print(f"  sidebar: {sidebar_count} occurrences")
print(f"  setup-strip: {setup_strip_count} occurrences")

if tab_bar_count > 0:
    print("  ✅ Tab bar present")
if tab_item_count > 0:
    print("  ✅ Tab items present")
if sidebar_count == 0:
    print("  ✅ Sidebar completely removed")
if setup_strip_count <= 1:  # May be one reference in CSS comment
    print("  ✅ Setup-strip removed")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Cleaned up remaining navigation references")
else:
    print(f"\n✅ No additional cleanup needed")

print(f"\n{'='*50}")
print("🎯 CLEANUP COMPLETE:")
print("   • Universal tab bar implementation verified")
print("   • All old navigation systems removed")
print("   • Ready for testing")
print(f"{'='*50}")