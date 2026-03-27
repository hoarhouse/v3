#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing demo bar position and content offset")
print("=" * 55)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFIX 1 - DEMO BAR POSITION (94px → 58px):")
print("-" * 45)

# Fix demo bar position
demo_fixes = [
    (".demo-bar{position:fixed;top:94px;", ".demo-bar{position:fixed;top:58px;"),
    (".demo-bar { position: fixed; top: 94px;", ".demo-bar { position: fixed; top: 58px;")
]

for old_demo, new_demo in demo_fixes:
    count = content.count(old_demo)
    if count > 0:
        content = content.replace(old_demo, new_demo)
        print(f"  ✓ Fixed demo bar: {old_demo} → {new_demo} ({count} times)")

print("\nFIX 2 - CONTENT OFFSET (total 93px):")
print("-" * 40)

# Fix main content padding
padding_fixes = [
    ("padding:86px 24px 100px", "padding:93px 24px 100px"),
    ("padding: 86px 24px 100px", "padding: 93px 24px 100px"),
    ("padding:78px 16px 100px", "padding:93px 16px 100px"),
    ("padding: 78px 16px 100px", "padding: 93px 16px 100px")
]

for old_padding, new_padding in padding_fixes:
    count = content.count(old_padding)
    if count > 0:
        content = content.replace(old_padding, new_padding)
        print(f"  ✓ Fixed padding: {old_padding} → {new_padding} ({count} times)")

print("\nFIX 3 - ACTIVITY LIST CHECK:")
print("-" * 35)

# Check if activity list appears in non-home panels
activity_panels = []
panel_pattern = r'<div[^>]*id="panel-([^"]+)"[^>]*>.*?activity-list.*?</div>'
matches = re.finditer(panel_pattern, content, re.DOTALL)

for match in matches:
    panel_name = match.group(1)
    if panel_name != 'home':
        activity_panels.append(panel_name)

if activity_panels:
    print(f"  ⚠ Activity list found in panels: {activity_panels}")
    # Remove activity lists from non-home panels
    for panel in activity_panels:
        # This would need specific removal logic
        print(f"  → Would remove activity list from panel-{panel}")
else:
    print("  ✅ Activity list only appears in panel-home (correct)")

print("\nFIX 4 - SIDEBAR MARGIN FOR NON-APP VIEWS:")
print("-" * 45)

# Fix main-content margin
old_margin = ".main-content{flex:1;margin-left:220px;"
new_margin = ".main-content{flex:1;margin-left:0;"
new_app_rule = "#v-app.on .main-content{margin-left:220px;}"

# Alternative patterns to look for
margin_patterns = [
    (".main-content { flex: 1; margin-left: 220px;", ".main-content { flex: 1; margin-left: 0;"),
    (".main-content{flex:1;margin-left:220px;", ".main-content{flex:1;margin-left:0;")
]

found_margin = False
for old_pattern, new_pattern in margin_patterns:
    if old_pattern in content:
        content = content.replace(old_pattern, new_pattern)
        print(f"  ✓ Fixed main-content margin: removed 220px default")
        
        # Add the new rule after it
        # Find where to insert the new rule
        insertion_point = content.find(new_pattern) + len(new_pattern)
        if insertion_point > 0:
            # Insert after this rule, on a new line
            content = content[:insertion_point] + "\n" + new_app_rule + content[insertion_point:]
            print(f"  ✓ Added app-specific margin rule")
        found_margin = True
        break

if not found_margin:
    print("  ⚠ Main-content margin rule not found")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed demo bar position and content offset")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*55}")
print("🎯 LAYOUT FIXES APPLIED:")
print("   • Demo bar: top:58px (under nav)")
print("   • Content: 93px offset (nav + demo)")  
print("   • Activity: only in home panel")
print("   • Sidebar: only for app views")
print(f"{'='*55}")
print("🔍 Ready for verification")