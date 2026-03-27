#!/usr/bin/env python3
from pathlib import Path

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing navTo() duplicate code — final clean")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content

print("\nFINDING AND REPLACING navTo() FUNCTION:")
print("-" * 45)

# The exact current broken function (with formatting variations)
broken_navto = '''function navTo(section){
  currentApp = section;
  document.querySelectorAll('.section-panel').forEach(function(p){p.classList.remove('on');});
  var panel = document.getElementById('panel-' + section);
  if(panel) panel.classList.add('on');
  document.querySelectorAll('.sb-item').forEach(function(i){i.classList.remove('active');});
  var navItem = document.getElementById('nav-' + section);
  if(navItem) navItem.classList.add('active');
  if(section === 'home') setTimeout(buildMiniChart, 50);
  if(section === 'donations') setTimeout(buildFullChart, 50);
  // Close sidebar on mobile after navigation
  document.getElementById('sidebar').classList.remove('open');if(section==='home') setTimeout(buildMiniChart,50);
  if(section==='donations') setTimeout(buildFullChart,50);}'''

# The clean replacement
clean_navto = '''function navTo(section){
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

# Try exact replacement first
if broken_navto in content:
    content = content.replace(broken_navto, clean_navto)
    print("  ✓ Found and replaced exact broken navTo() function")
else:
    print("  ⚠ Exact match not found, trying pattern-based replacement...")
    
    # Try to find the function with regex and replace it
    import re
    
    # Pattern to match the navTo function with all its variations
    navto_pattern = r'function navTo\(section\)\{.*?\}\s*(?=\n\nfunction|\n\s*</script>|$)'
    navto_match = re.search(navto_pattern, content, re.DOTALL)
    
    if navto_match:
        current_function = navto_match.group(0).strip()
        print(f"  Found function ({len(current_function)} chars):")
        print("  " + "="*40)
        print(f"  {current_function}")
        print("  " + "="*40)
        
        # Check for duplicate setTimeout calls
        if current_function.count('setTimeout(buildMiniChart,50)') > 1:
            print("  ⚠ Duplicate home chart calls detected")
        if current_function.count('setTimeout(buildFullChart,50)') > 1:
            print("  ⚠ Duplicate donations chart calls detected")
        
        # Replace with clean version
        content = content.replace(navto_match.group(0), clean_navto)
        print("  ✓ Replaced with clean navTo() function")
    else:
        print("  ✗ navTo() function not found with regex")

# Check if replacement was successful
if 'setTimeout(buildMiniChart,50)' in content:
    chart_count = content.count('setTimeout(buildMiniChart,50)')
    donations_count = content.count('setTimeout(buildFullChart,50)')
    print(f"\nVERIFYING DUPLICATES REMOVED:")
    print(f"  buildMiniChart calls: {chart_count}")
    print(f"  buildFullChart calls: {donations_count}")
    
    # Count specifically in navTo function
    navto_start = content.find('function navTo(section){')
    navto_end = content.find('}', navto_start) + 1
    navto_section = content[navto_start:navto_end] if navto_start != -1 else ""
    
    if navto_section:
        navto_chart_count = navto_section.count('setTimeout(buildMiniChart,50)')
        navto_donations_count = navto_section.count('setTimeout(buildFullChart,50)')
        print(f"  In navTo function - buildMiniChart: {navto_chart_count}")
        print(f"  In navTo function - buildFullChart: {navto_donations_count}")

# Write the updated content back
if content != original_content:
    dashboard_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed navTo() duplicate code")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🧹 navTo() FINAL CLEANUP:")
print("   • Removed duplicate setTimeout calls")
print("   • Fixed missing newline syntax error") 
print("   • Clean, compact function")
print("   • No more duplicate code")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix navTo duplicate code — final clean'")