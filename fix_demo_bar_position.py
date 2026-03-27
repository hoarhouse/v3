#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing demo bar position to sit under top nav")
print("=" * 55)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - FIX DEMO BAR TOP POSITION:")
print("-" * 40)

# Fix demo bar top position from 94px to 58px
old_demo_bar = ".demo-bar{position:fixed;top:94px;"
new_demo_bar = ".demo-bar{position:fixed;top:58px;"

if old_demo_bar in content:
    content = content.replace(old_demo_bar, new_demo_bar)
    print("  ✓ Fixed demo-bar top: 94px → 58px")
else:
    # Check for variations
    alt_patterns = [
        (".demo-bar{position:fixed;top: 94px;", ".demo-bar{position:fixed;top: 58px;"),
        (".demo-bar { position: fixed; top: 94px;", ".demo-bar { position: fixed; top: 58px;")
    ]
    
    found = False
    for old_pattern, new_pattern in alt_patterns:
        if old_pattern in content:
            content = content.replace(old_pattern, new_pattern)
            print(f"  ✓ Fixed demo-bar top (variation): {old_pattern} → {new_pattern}")
            found = True
            break
    
    if not found:
        print("  ⚠ Demo bar CSS not found")

print("\nSTEP 2 - FIX ALL CONTENT OFFSETS:")
print("-" * 38)

# Replace padding-top values from 94px to 93px
padding_replacements = [
    ("padding-top:94px", "padding-top:93px"),
    ("padding-top: 94px", "padding-top: 93px"),
    ("padding:94px", "padding:93px")
]

for old_padding, new_padding in padding_replacements:
    count = content.count(old_padding)
    if count > 0:
        content = content.replace(old_padding, new_padding)
        print(f"  ✓ Fixed {old_padding} → {new_padding} ({count} times)")

# Fix main-content specific padding
main_content_replacements = [
    ("padding:86px 24px 100px", "padding:93px 24px 100px"),
    ("padding:78px 16px 100px", "padding:93px 16px 100px"),
    ("padding: 86px 24px 100px", "padding: 93px 24px 100px"),
    ("padding: 78px 16px 100px", "padding: 93px 16px 100px")
]

print("\nSTEP 3 - FIX MAIN-CONTENT PADDING:")
print("-" * 38)

for old_main, new_main in main_content_replacements:
    count = content.count(old_main)
    if count > 0:
        content = content.replace(old_main, new_main)
        print(f"  ✓ Fixed main-content: {old_main} → {new_main} ({count} times)")

print("\nSTEP 4 - SIDEBAR CONFIRMATION:")
print("-" * 35)
print("  ℹ Sidebar stays at top:94px (correct - not changed)")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed demo bar and content positioning")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*55}")
print("🎯 DEMO BAR POSITIONING FIX:")
print("   • Demo bar: top:58px (under nav)")
print("   • Content: padding:93px (nav + demo bar)")
print("   • Sidebar: top:94px (unchanged)")
print("   • Total offset: 58px nav + 35px demo = 93px")
print(f"{'='*55}")
print("🔍 Ready for verification with grep commands")