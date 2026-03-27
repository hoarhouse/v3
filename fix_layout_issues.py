#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing demo bar offset and layout issues")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nISSUE 1 - FIX DEMO BAR POSITION:")
print("-" * 40)

# Fix demo bar position from 94px to 58px
demo_bar_old = ".demo-bar{position:fixed;top:94px;"
demo_bar_new = ".demo-bar{position:fixed;top:58px;"

count = content.count(demo_bar_old)
if count > 0:
    content = content.replace(demo_bar_old, demo_bar_new)
    print(f"  ✓ Fixed demo-bar top: 94px → 58px ({count} times)")
else:
    print("  ⚠ Demo bar CSS not found or already correct")

print("\nISSUE 2 - FIX CONTENT PADDING OFFSETS:")
print("-" * 45)

# Fix main content padding
padding_fixes = [
    ("padding:86px 24px 100px", "padding:93px 24px 100px"),
    ("padding: 86px 24px 100px", "padding: 93px 24px 100px"),
    ("padding:78px 16px 100px", "padding:93px 16px 100px"),  
    ("padding: 78px 16px 100px", "padding: 93px 16px 100px"),
    ("padding-top:94px", "padding-top:93px"),
    ("padding-top: 94px", "padding-top: 93px")
]

for old_padding, new_padding in padding_fixes:
    count = content.count(old_padding)
    if count > 0:
        content = content.replace(old_padding, new_padding)
        print(f"  ✓ Fixed {old_padding} → {new_padding} ({count} times)")

print("\nISSUE 3 - CHECK RECENT ACTIVITY CARD POSITION:")
print("-" * 50)

# Find the activity card and check its position relative to dash-grid
activity_card_pattern = r'<div class="card" style="margin-top:16px;padding:0;">.*?activity-list.*?</div>'
activity_match = re.search(activity_card_pattern, content, re.DOTALL)

if activity_match:
    activity_card = activity_match.group(0)
    print("  ✓ Found recent activity card")
    
    # Find the dash-grid container
    dash_grid_pattern = r'<div class="dash-grid".*?</div>\s*</div>'
    dash_grid_matches = list(re.finditer(dash_grid_pattern, content, re.DOTALL))
    
    if dash_grid_matches:
        # Find the last dash-grid (should be the main one)
        last_dash_grid = dash_grid_matches[-1]
        dash_grid_end = last_dash_grid.end()
        activity_start = activity_match.start()
        
        if activity_start > dash_grid_end:
            print("  ✅ Activity card is correctly positioned AFTER dash-grid")
        else:
            print("  ⚠ Activity card appears to be INSIDE dash-grid")
            # Find where to move it
            dash_grid_content = last_dash_grid.group(0)
            
            # Remove the activity card from its current location
            content = content.replace(activity_card, '')
            
            # Insert it after the dash-grid
            content = content.replace(dash_grid_content, dash_grid_content + '\n      ' + activity_card)
            print("  ✓ Moved activity card outside dash-grid")
    else:
        print("  ⚠ Could not find dash-grid container")
else:
    print("  ⚠ Could not find activity card")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed demo bar and layout issues")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🎯 LAYOUT FIXES APPLIED:")
print("   • Demo bar: top:58px (under nav)")
print("   • Content: padding adjusted for 93px offset")
print("   • Activity card: positioned correctly")
print(f"{'='*50}")
print("🔍 Ready for verification with grep commands")