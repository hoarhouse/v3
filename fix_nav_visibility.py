#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Fixing navigation text visibility in communio.html")
print("=" * 55)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nCHANGE 1: Making nav text white by default")
print("-" * 45)

# Change 1.1: .nav-name color to white
old_nav_name = "color: var(--ink);"
new_nav_name = "color: var(--white);"

if old_nav_name in content:
    # Find the .nav-name rule and replace the color
    nav_name_pattern = r'(\.nav-name\s*\{[^}]*?)color:\s*var\(--ink\);([^}]*\})'
    nav_name_match = re.search(nav_name_pattern, content, re.DOTALL)
    
    if nav_name_match:
        new_nav_name_rule = nav_name_match.group(1) + "color: var(--white);" + nav_name_match.group(2)
        content = content.replace(nav_name_match.group(0), new_nav_name_rule)
        print("✓ Updated .nav-name color to var(--white)")
    else:
        print("⚠ .nav-name rule pattern not found, trying simple replacement")
        content = content.replace(old_nav_name, new_nav_name, 1)
        print("✓ Applied simple replacement for .nav-name color")

# Change 1.2: .nav-link color to white
old_nav_link = "color: var(--text-mid);"
new_nav_link = "color: rgba(255,253,249,0.75);"

nav_link_pattern = r'(\.nav-link\s*\{[^}]*?)color:\s*var\(--text-mid\);([^}]*\})'
nav_link_match = re.search(nav_link_pattern, content, re.DOTALL)

if nav_link_match:
    new_nav_link_rule = nav_link_match.group(1) + "color: rgba(255,253,249,0.75);" + nav_link_match.group(2)
    content = content.replace(nav_link_match.group(0), new_nav_link_rule)
    print("✓ Updated .nav-link color to rgba(255,253,249,0.75)")
else:
    # Try simple replacement
    content = content.replace(old_nav_link, new_nav_link, 1)
    print("✓ Applied simple replacement for .nav-link color")

# Change 1.3: .nav-link:hover color to white
old_nav_link_hover = "color: var(--ink);"
new_nav_link_hover = "color: var(--white);"

nav_link_hover_pattern = r'(\.nav-link:hover\s*\{[^}]*?)color:\s*var\(--ink\);([^}]*\})'
nav_link_hover_match = re.search(nav_link_hover_pattern, content, re.DOTALL)

if nav_link_hover_match:
    new_nav_link_hover_rule = nav_link_hover_match.group(1) + "color: var(--white);" + nav_link_hover_match.group(2)
    content = content.replace(nav_link_hover_match.group(0), new_nav_link_hover_rule)
    print("✓ Updated .nav-link:hover color to var(--white)")
else:
    print("⚠ .nav-link:hover rule not found as expected")

print("\nCHANGE 2: Adding dark text styles for scrolled state")
print("-" * 50)

# Find the .nav.scrolled rule
nav_scrolled_pattern = r'(\.nav\.scrolled\s*\{[^}]*?box-shadow:[^;]*;)([^}]*\})'
nav_scrolled_match = re.search(nav_scrolled_pattern, content, re.DOTALL)

if nav_scrolled_match:
    # Add color property after box-shadow
    new_nav_scrolled = nav_scrolled_match.group(1) + "\n  color: var(--ink);" + nav_scrolled_match.group(2)
    content = content.replace(nav_scrolled_match.group(0), new_nav_scrolled)
    print("✓ Added color: var(--ink) to .nav.scrolled")
    
    # Add the new rules after .nav.scrolled
    additional_rules = """

.nav.scrolled .nav-name {
  color: var(--ink);
}

.nav.scrolled .nav-link {
  color: var(--text-mid);
}

.nav.scrolled .nav-link:hover {
  color: var(--ink);
}"""
    
    # Insert after the closing brace of .nav.scrolled
    scrolled_end = content.find('}', content.find('.nav.scrolled'))
    if scrolled_end != -1:
        content = content[:scrolled_end + 1] + additional_rules + content[scrolled_end + 1:]
        print("✓ Added .nav.scrolled .nav-name rule")
        print("✓ Added .nav.scrolled .nav-link rule")
        print("✓ Added .nav.scrolled .nav-link:hover rule")
    else:
        print("❌ Could not find position to insert additional rules")
else:
    print("❌ Could not find .nav.scrolled rule")

print("\nCHANGE 3: Leaving .nav-btn alone (already has white text)")
print("-" * 60)
print("✓ .nav-btn unchanged (white text on terracotta background)")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    print("📝 Changes applied:")
    print("   - Nav text now white by default (visible on dark hero)")
    print("   - Nav text switches to dark when scrolled (readable on light bg)")
    print("   - Nav button unchanged (already properly styled)")
else:
    print(f"\n⚠ No changes were made to {communio_file.name}")

print(f"\n{'='*55}")
print("VERIFICATION COMMANDS:")
print("Run these to confirm changes:")
print("  grep -n 'nav-name' communio.html")
print("  grep -n 'nav-link' communio.html") 
print("  grep -n 'nav.scrolled' communio.html")
print(f"{'='*55}")
print("🚀 Ready to commit and test at hoarhouse.github.io/v3/communio.html")