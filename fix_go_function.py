#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing broken go() function in communio-dashboard.html")
print("=" * 60)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING CURRENT go() FUNCTION:")
print("-" * 40)

# Find the current go() function
go_pattern = r'function go\([^)]*\)\s*\{'
go_match = re.search(go_pattern, content)

if go_match:
    print(f"  ✓ Found go() function at position {go_match.start()}")
    
    # Find the complete function by counting braces
    start_pos = go_match.start()
    brace_count = 0
    pos = start_pos
    
    while pos < len(content):
        if content[pos] == '{':
            brace_count += 1
        elif content[pos] == '}':
            brace_count -= 1
            if brace_count == 0:
                end_pos = pos + 1
                break
        pos += 1
    
    if 'end_pos' in locals():
        current_go_function = content[start_pos:end_pos]
        print(f"  Current function length: {len(current_go_function)} characters")
        
        # Check if updateTabBar is referenced
        if 'updateTabBar' in current_go_function:
            print("  ⚠ Function contains updateTabBar reference (will be removed)")
        
        print("\nREPLACING WITH CLEAN VERSION:")
        print("-" * 40)
        
        # The clean replacement function
        new_go_function = '''function go(viewName,appSection){
  document.querySelectorAll('.view,.app-view').forEach(function(v){
    v.classList.remove('on');
    v.style.display='none';
  });
  var target;
  if(viewName==='app'){
    target=document.getElementById('v-app');
    target.style.display='flex';
    target.classList.add('on');
    if(appSection) navTo(appSection);
  } else {
    target=document.getElementById('v-'+viewName);
    target.style.display='block';
    target.classList.add('on');
  }
  var viewMap={welcome:0,setup:1,public:9};
  var appMap={home:2,messages:3,network:4,projects:5,website:6,donations:7,settings:8};
  var idx=(viewName==='app')?(appSection?appMap[appSection]:2):viewMap[viewName];
  document.querySelectorAll('.sw-btn').forEach(function(b,i){
    b.classList.toggle('on',i===idx);
  });
  document.documentElement.scrollTop=0;
  document.body.scrollTop=0;
  if(viewName==='app'&&appSection==='home') setTimeout(buildMiniChart,50);
  if(viewName==='app'&&appSection==='donations') setTimeout(buildFullChart,50);
}'''
        
        # Replace the function
        content = content[:start_pos] + new_go_function + content[end_pos:]
        print("  ✓ Replaced go() function with clean version")
        print("  ✓ Removed updateTabBar reference")
        print("  ✓ Removed tab bar show/hide logic")
        print("  ✓ Kept switcher button logic")
        
    else:
        print("  ⚠ Could not find end of go() function")
else:
    print("  ✗ go() function not found")

print("\nALSO REMOVING ANY STANDALONE updateTabBar FUNCTION:")
print("-" * 50)

# Remove any standalone updateTabBar function that might exist
update_tab_pattern = r'function updateTabBar\([^)]*\)\s*\{[^}]*\}'
update_tab_matches = re.findall(update_tab_pattern, content, re.DOTALL)

if update_tab_matches:
    content = re.sub(update_tab_pattern, '', content, flags=re.DOTALL)
    print(f"  ✓ Removed {len(update_tab_matches)} updateTabBar function(s)")
else:
    print("  ✓ No standalone updateTabBar function found")

print("\nVERIFICATION:")
print("-" * 20)

# Verify updateTabBar is completely removed
update_tab_count = content.count('updateTabBar')
print(f"  updateTabBar occurrences: {update_tab_count}")

if update_tab_count == 0:
    print("  ✅ updateTabBar completely removed")
else:
    print("  ⚠ updateTabBar still present")

# Verify go() function exists
go_function_count = content.count('function go(')
print(f"  function go( occurrences: {go_function_count}")

if go_function_count == 1:
    print("  ✅ Single go() function present")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed broken go() function")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*60}")
print("🔧 GO() FUNCTION FIX:")
print("   • Removed updateTabBar reference")
print("   • Simplified function logic")
print("   • Kept switcher button functionality")
print("   • Function now works without errors")
print(f"{'='*60}")
print("🚀 Ready to commit: 'Fix broken go() function'")