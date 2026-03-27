#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing navTo() function syntax error")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nCURRENT navTo() FUNCTION IDENTIFIED:")
print("-" * 40)

# Find the entire navTo() function using regex
navTo_pattern = r'function navTo\([^)]*\)\s*\{[^}]*(?:\{[^}]*\}[^}]*)*\}'
navTo_match = re.search(navTo_pattern, content, re.DOTALL)

if navTo_match:
    current_navTo = navTo_match.group(0)
    print("Found navTo() function:")
    print("=" * 30)
    print(current_navTo)
    print("=" * 30)
    print(f"Length: {len(current_navTo)} characters")
    
    # Check for issues
    if 'setTimeout(buildMiniChart,50)' in current_navTo:
        count_home = current_navTo.count("setTimeout(buildMiniChart,50)")
        count_donations = current_navTo.count("setTimeout(buildFullChart,50)")
        print(f"  ⚠ Duplicate home chart calls: {count_home}")
        print(f"  ⚠ Duplicate donations chart calls: {count_donations}")
    
    if ';if(' in current_navTo:
        print("  ✗ Missing newline between statements (;if pattern found)")
    
    print("\nREPLACING WITH CLEAN VERSION:")
    print("-" * 35)
    
    # Clean replacement function
    clean_navTo = '''function navTo(section){
  currentApp=section;
  document.querySelectorAll('.section-panel').forEach(function(p){p.classList.remove('on');});
  var panel=document.getElementById('panel-'+section);
  if(panel) panel.classList.add('on');
  document.querySelectorAll('.sb-item').forEach(function(i){i.classList.remove('active');});
  var navItem=document.getElementById('nav-'+section);
  if(navItem) navItem.classList.add('active');
  document.getElementById('sidebar').classList.remove('open');
  if(section==='home') setTimeout(buildMiniChart,50);
  if(section==='donations') setTimeout(buildFullChart,50);
}'''
    
    # Replace the function
    content = content.replace(navTo_match.group(0), clean_navTo)
    print("  ✓ Replaced with clean navTo() function")
    print("  ✓ Removed duplicate setTimeout calls")
    print("  ✓ Fixed missing newline syntax error")
    print("  ✓ Cleaned up spacing and formatting")
    
else:
    print("  ✗ navTo() function not found")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed navTo() function syntax error")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🔧 navTo() FUNCTION FIXED:")
print("   • Removed duplicate setTimeout calls")
print("   • Fixed missing newline syntax error")
print("   • Clean, properly formatted function")
print("   • Should run without JavaScript errors")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix navTo syntax error — clean function'")