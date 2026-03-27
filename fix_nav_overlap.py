#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing nav overlap on all dashboard sections")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nSTEP 1 - FIX APP-VIEW CSS RULE:")
print("-" * 35)

# Find and check current .app-view.on rule
app_view_pattern = r'(\.app-view\.on\{[^}]*?\})'
app_view_match = re.search(app_view_pattern, content, re.DOTALL)

if app_view_match:
    app_view_block = app_view_match.group(1)
    print(f"Current rule: {app_view_block}")
    
    if 'padding-top:' in app_view_block:
        # Update existing padding-top
        new_block = re.sub(r'padding-top:[^;]+;', 'padding-top:58px;', app_view_block)
        print("  ✓ Updated existing padding-top to 58px")
    else:
        # Add padding-top
        new_block = app_view_block.replace('}', 'padding-top:58px;}')
        print("  ✓ Added padding-top:58px")
    
    content = content.replace(app_view_block, new_block)
else:
    print("  ⚠ .app-view.on rule not found")

print("\nSTEP 2 - FIX MAIN-CONTENT CSS RULE:")
print("-" * 35)

# Find and update .main-content rule
main_content_pattern = r'(\.main-content\{[^}]*?\})'
main_content_match = re.search(main_content_pattern, content, re.DOTALL)

if main_content_match:
    main_content_block = main_content_match.group(1)
    print(f"Current rule: {main_content_block}")
    
    if 'padding:28px' in main_content_block:
        # Change padding from 28px to 86px on top
        new_block = main_content_block.replace('padding:28px 24px 100px;', 'padding:86px 24px 100px;')
        print("  ✓ Changed padding-top from 28px to 86px (58px nav + 28px breathing room)")
        content = content.replace(main_content_block, new_block)
    else:
        print("  ⚠ Expected padding:28px pattern not found")
        print(f"    Found: {main_content_block}")

print("\nSTEP 3 - FIX SETUP STRIP POSITION:")
print("-" * 35)

# Check if setup-strip has position and top properties
setup_strip_pattern = r'(\.setup-strip\{[^}]*?\})'
setup_strip_match = re.search(setup_strip_pattern, content, re.DOTALL)

if setup_strip_match:
    setup_strip_block = setup_strip_match.group(1)
    print(f"Current rule: {setup_strip_block}")
    
    if 'position:' not in setup_strip_block:
        # Add position sticky and top
        new_block = setup_strip_block.replace('}', 'position:sticky;top:58px;}')
        print("  ✓ Added position:sticky and top:58px")
        content = content.replace(setup_strip_block, new_block)
    elif 'top:' not in setup_strip_block:
        # Add top property
        new_block = setup_strip_block.replace('}', 'top:58px;}')
        print("  ✓ Added top:58px")
        content = content.replace(setup_strip_block, new_block)
    else:
        # Update existing top value
        new_block = re.sub(r'top:[^;]+;', 'top:58px;', setup_strip_block)
        print("  ✓ Updated top to 58px")
        content = content.replace(setup_strip_block, new_block)

print("\nSTEP 4 - VERIFY SIDEBAR TOP OFFSET:")
print("-" * 35)

# Check sidebar rule (should already be correct)
sidebar_pattern = r'(\.sidebar\{[^}]*?\})'
sidebar_match = re.search(sidebar_pattern, content, re.DOTALL)

if sidebar_match:
    sidebar_block = sidebar_match.group(1)
    if 'top:58px' in sidebar_block:
        print("  ✓ Sidebar already has correct top:58px")
    else:
        print(f"  Current sidebar: {sidebar_block}")
        if 'top:' in sidebar_block:
            # Update existing top
            new_block = re.sub(r'top:[^;]+;', 'top:58px;', sidebar_block)
            print("  ✓ Updated sidebar top to 58px")
            content = content.replace(sidebar_block, new_block)

print("\nSTEP 5 - VERIFICATION:")
print("-" * 25)

# Verify changes
if '.app-view.on{display:flex;min-height:100dvh;padding-top:58px;}' in content:
    print("  ✓ .app-view.on has padding-top:58px")

if 'padding:86px 24px 100px' in content:
    print("  ✓ .main-content has padding-top:86px")

if 'top:58px' in content:
    top_count = content.count('top:58px')
    print(f"  ✓ Found {top_count} elements with top:58px")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed nav overlap on all dashboard sections")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🎯 NAV OVERLAP FIXES:")
print("   • .app-view.on: padding-top 58px")
print("   • .main-content: padding-top 86px (58px + 28px)")
print("   • .setup-strip: sticky position, top 58px")
print("   • .sidebar: top 58px (already correct)")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix nav overlap on all dashboard sections'")