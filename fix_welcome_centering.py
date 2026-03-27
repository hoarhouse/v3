#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Checking and fixing welcome screen centering in communio-dashboard.html")
print("=" * 70)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')

print("\n1. CURRENT .wl CSS BLOCK:")
print("-" * 30)

# Find and print the current .wl block
wl_pattern = r'\.wl\s*\{[^}]+\}'
wl_match = re.search(wl_pattern, content, re.DOTALL)
if wl_match:
    print(wl_match.group(0))
else:
    print("❌ .wl block not found!")

print("\n2. CURRENT #v-welcome CSS BLOCK:")
print("-" * 30)

# Find and print the current #v-welcome block  
welcome_pattern = r'#v-welcome\s*\{[^}]+\}'
welcome_match = re.search(welcome_pattern, content)
if welcome_match:
    welcome_block = welcome_match.group(0)
    print(welcome_block)
    
    # Check if required properties are present
    has_align_items = 'align-items:center' in welcome_block
    has_justify_content = 'justify-content:center' in welcome_block
    
    print(f"\n   ✓ align-items:center: {'PRESENT' if has_align_items else 'MISSING'}")
    print(f"   ✓ justify-content:center: {'PRESENT' if has_justify_content else 'MISSING'}")
else:
    print("❌ #v-welcome block not found!")

print("\n3. CHECKING .wl REQUIRED PROPERTIES:")
print("-" * 40)

# Check if .wl has all required properties
if wl_match:
    wl_content = wl_match.group(0)
    required_props = [
        'position:relative',
        'z-index:1', 
        'max-width:460px',
        'width:100%',
        'text-align:center',
        'margin-left:auto',
        'margin-right:auto'
    ]
    
    missing_props = []
    for prop in required_props:
        if prop not in wl_content:
            missing_props.append(prop)
    
    if not missing_props:
        print("✅ All required properties are present in .wl block!")
    else:
        print(f"❌ Missing properties: {missing_props}")
        
        # Build the complete .wl block with all properties
        new_wl_block = """.wl {
  position: relative;
  z-index: 1;
  max-width: 460px;
  width: 100%;
  text-align: center;
  margin-left: auto;
  margin-right: auto;
}"""
        
        # Replace the existing .wl block
        content = re.sub(wl_pattern, new_wl_block, content, flags=re.DOTALL)
        
        # Write the updated content back
        dashboard_file.write_text(content, encoding='utf-8')
        
        print(f"✅ Updated .wl block with missing properties")

print("\n4. CHECKING #v-welcome REQUIRED PROPERTIES:")
print("-" * 45)

if welcome_match and (not has_align_items or not has_justify_content):
    print("❌ Missing flex centering properties in #v-welcome")
    
    # Add missing properties
    welcome_content = welcome_match.group(0)
    if not has_align_items:
        welcome_content = welcome_content.replace('}', 'align-items:center;}')
    if not has_justify_content:
        welcome_content = welcome_content.replace('}', 'justify-content:center;}')
    
    # Replace in main content
    content = content.replace(welcome_match.group(0), welcome_content)
    dashboard_file.write_text(content, encoding='utf-8')
    
    print("✅ Added missing flex centering properties")
elif welcome_match:
    print("✅ All required properties are present in #v-welcome!")

print("\n5. FINAL VERIFICATION:")
print("-" * 25)

# Re-read and verify
final_content = dashboard_file.read_text(encoding='utf-8')

# Check final .wl block
final_wl = re.search(wl_pattern, final_content, re.DOTALL)
if final_wl:
    print("FINAL .wl BLOCK:")
    print(final_wl.group(0))

print("\n✅ Welcome screen centering check complete!")
print("The file is ready for commit in GitHub Desktop.")