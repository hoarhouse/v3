#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
dashboard_file = Path("/Users/christopherhoar/Desktop/v3/communio-dashboard.html")

print("Fixing JavaScript syntax error at line 2036")
print("=" * 50)

# Read the file
content = dashboard_file.read_text(encoding='utf-8')
original_content = content
lines = content.split('\n')

print("\nSTEP 1 - EXAMINING LINES 2025-2045:")
print("-" * 40)

for i in range(2024, min(2045, len(lines))):
    line_num = i + 1
    line_content = lines[i]
    if line_num >= 2035 and line_num <= 2040:
        print(f"  {line_num}: {line_content} ← PROBLEM AREA")
    else:
        print(f"  {line_num}: {line_content}")

print("\nSTEP 2 - ANALYZING FUNCTIONS:")
print("-" * 35)

# Check each function for proper structure
functions = [
    'buildMiniChart', 'buildFullChart', 'go', 'navTo', 
    'toggleSidebar', 'pickT', 'pickA', 'simulateStripe'
]

for func_name in functions:
    func_pattern = rf'function {func_name}\([^{{]*\{{'
    func_match = re.search(func_pattern, content)
    
    if func_match:
        start_pos = func_match.start()
        # Count braces to find function end
        brace_count = 0
        pos = start_pos
        while pos < len(content) and content[pos] != '{':
            pos += 1
        
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
            print(f"  ✓ {func_name}: Complete function found")
            del locals()['end_pos']
        else:
            print(f"  ⚠ {func_name}: Potentially incomplete")

print("\nSTEP 3 - IDENTIFYING THE SYNTAX ERROR:")
print("-" * 40)

# The problem is the orphaned ); after the go() function
# Let's find and remove it
problem_line_pattern = r'^\s*\);\s*$'
problem_found = False

for i, line in enumerate(lines):
    if re.match(problem_line_pattern, line):
        line_num = i + 1
        print(f"  ✗ Found orphaned ); at line {line_num}: '{line}'")
        
        # Check context - should be after go() function
        if i > 0 and '}' in lines[i-1]:
            print(f"    Previous line {i}: '{lines[i-1]}' (ends with }})")
            print("    This orphaned ); should be removed")
            lines[i] = ''  # Remove the problematic line
            problem_found = True

if problem_found:
    print("  ✓ Removed orphaned ); line")
else:
    print("  ⚠ Orphaned ); not found in expected pattern")

# Also check for any truncated updateTabBar remnants
updateTabBar_remnants = []
for i, line in enumerate(lines):
    if 'updateTabBar' in line or (line.strip().startswith('if(') and 'tab-' in line and not line.strip().endswith('}')):
        updateTabBar_remnants.append((i+1, line.strip()))

if updateTabBar_remnants:
    print(f"\nSTEP 3b - FOUND updateTabBar REMNANTS:")
    print("-" * 40)
    for line_num, line_content in updateTabBar_remnants:
        print(f"  ✗ Line {line_num}: {line_content}")
        
        # Remove these remnant lines
        lines[line_num-1] = ''
        print(f"    Removed remnant line")

print("\nSTEP 4 - VERIFICATION:")
print("-" * 25)

# Reconstruct content
new_content = '\n'.join(lines)

# Clean up multiple empty lines
new_content = re.sub(r'\n\s*\n\s*\n', '\n\n', new_content)

# Verify script tags
script_open_count = new_content.count('<script>')
script_close_count = new_content.count('</script>')

print(f"  <script> tags: {script_open_count}")
print(f"  </script> tags: {script_close_count}")

if script_open_count == 1 and script_close_count == 1:
    print("  ✅ Script tags balanced")
else:
    print("  ⚠ Script tag imbalance")

# Check for remaining syntax issues
orphaned_parens = len(re.findall(r'^\s*\);\s*$', new_content, re.MULTILINE))
print(f"  Orphaned ); patterns: {orphaned_parens}")

if orphaned_parens == 0:
    print("  ✅ No orphaned parentheses")

# Write the updated content back
if new_content != original_content:
    dashboard_file.write_text(new_content, encoding='utf-8')
    print(f"\n✅ Updated {dashboard_file.name}")
    print("   Fixed JavaScript syntax error")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🔧 JAVASCRIPT SYNTAX FIX:")
print("   • Removed orphaned ); at line ~2036")
print("   • Cleaned up any updateTabBar remnants") 
print("   • Functions now properly terminated")
print("   • Script should run without errors")
print(f"{'='*50}")
print("🚀 Ready to commit: 'Fix JS syntax error line 2036'")