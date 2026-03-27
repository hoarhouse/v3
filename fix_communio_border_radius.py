#!/usr/bin/env python3
from pathlib import Path
import subprocess
import re

# File paths
v3_dir = Path("/Users/christopherhoar/Desktop/v3")
files_to_fix = ["communio.html", "communio-register.html"]

def analyze_border_radius(file_path):
    """Analyze current border-radius values in a file"""
    print(f"\n{'='*60}")
    print(f"ANALYZING: {file_path.name}")
    print(f"{'='*60}")
    
    content = file_path.read_text(encoding='utf-8')
    
    # Count circle values (50%)
    circles = content.count('border-radius:50%') + content.count('border-radius: 50%')
    print(f"Circle avatars (50%): {circles}")
    
    # Find all px values
    px_patterns = re.findall(r'border-radius:\s*(\d+)px', content)
    if px_patterns:
        px_counts = {}
        for val in px_patterns:
            px_counts[f"{val}px"] = px_counts.get(f"{val}px", 0) + 1
        
        print("Current px values:")
        for val, count in sorted(px_counts.items(), key=lambda x: int(x[0][:-2]), reverse=True):
            print(f"  {val}: {count} occurrences")
    else:
        print("No hardcoded px values found")

def apply_border_radius_fixes(file_path):
    """Apply border-radius reduction to a file"""
    print(f"\nAPPLYING FIXES TO: {file_path.name}")
    print("-" * 40)
    
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    # 1. Update CSS variable declarations
    css_var_replacements = [
        # Don't change --r-sm: 6px (keep as is)
        ('--r-md: 12px', '--r-md: 8px'),
        ('--r-md:12px', '--r-md:8px'),  # Handle no spaces
        ('--r-lg: 20px', '--r-lg: 12px'),
        ('--r-lg:20px', '--r-lg:12px'),  # Handle no spaces
        ('--r-xl: 32px', '--r-xl: 16px'),
        ('--r-xl:32px', '--r-xl:16px'),  # Handle no spaces
        # Don't change --r-pill: 100px (keep as is)
    ]
    
    print("CSS Variable replacements:")
    for old, new in css_var_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ {old} → {new} ({count} times)")
    
    # 2. Replace hardcoded border-radius values (without spaces)
    hardcoded_replacements = [
        ('border-radius:20px', 'border-radius:10px'),
        ('border-radius:18px', 'border-radius:10px'),
        ('border-radius:17px', 'border-radius:10px'),
        ('border-radius:16px', 'border-radius:10px'),
        ('border-radius:14px', 'border-radius:8px'),
        ('border-radius:13px', 'border-radius:8px'),
        ('border-radius:12px', 'border-radius:8px'),
        ('border-radius:11px', 'border-radius:6px'),
        ('border-radius:10px', 'border-radius:6px'),
        ('border-radius:9px', 'border-radius:6px'),
    ]
    
    # 3. Replace hardcoded border-radius values (with spaces)
    spaced_replacements = [
        ('border-radius: 20px', 'border-radius: 10px'),
        ('border-radius: 18px', 'border-radius: 10px'),
        ('border-radius: 16px', 'border-radius: 10px'),
        ('border-radius: 14px', 'border-radius: 8px'),
        ('border-radius: 13px', 'border-radius: 8px'),
        ('border-radius: 12px', 'border-radius: 8px'),
        ('border-radius: 11px', 'border-radius: 6px'),
        ('border-radius: 10px', 'border-radius: 6px'),
        ('border-radius: 9px', 'border-radius: 6px'),
    ]
    
    all_replacements = hardcoded_replacements + spaced_replacements
    
    print("Hardcoded value replacements:")
    total_replacements = 0
    for old, new in all_replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ {old} → {new} ({count} times)")
            total_replacements += count
    
    if total_replacements == 0:
        print("  No hardcoded values needed replacement")
    
    # Write back if changes were made
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"\n✅ Updated {file_path.name}")
    else:
        print(f"\n⚠️ No changes needed for {file_path.name}")
    
    return content != original_content

def verify_border_radius(file_path):
    """Verify no problematic border-radius values remain"""
    print(f"\nVERIFYING: {file_path.name}")
    print("-" * 30)
    
    # Run grep command to find problematic values
    try:
        result = subprocess.run([
            'grep', '-n', 'border-radius', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')
            problematic = []
            
            for line in lines:
                # Skip 50% (circles), var() calls, and pill references
                if '50%' in line or 'var(' in line or 'pill' in line:
                    continue
                
                # Look for px values > 10
                matches = re.findall(r'border-radius:\s*(\d+)px', line)
                for match in matches:
                    if int(match) > 10:
                        problematic.append(line)
                        break
            
            if problematic:
                print("❌ PROBLEMATIC VALUES FOUND:")
                for line in problematic[:5]:  # Show first 5
                    print(f"  {line}")
                return False
            else:
                print("✅ All border-radius values are ≤ 10px (excluding circles/vars)")
                return True
        else:
            print("✅ No border-radius declarations found")
            return True
            
    except Exception as e:
        print(f"Error during verification: {e}")
        return False

# Main execution
print("BORDER-RADIUS REDUCTION FOR COMMUNIO FILES")
print("=" * 60)

for filename in files_to_fix:
    file_path = v3_dir / filename
    
    if not file_path.exists():
        print(f"❌ {filename} not found!")
        continue
    
    # Analyze current state
    analyze_border_radius(file_path)
    
    # Apply fixes
    changes_made = apply_border_radius_fixes(file_path)
    
    # Verify results
    verification_passed = verify_border_radius(file_path)
    
    # Final analysis
    if changes_made:
        analyze_border_radius(file_path)
    
    print(f"\n📝 SUMMARY FOR {filename}:")
    print(f"   Changes made: {'Yes' if changes_made else 'No'}")
    print(f"   Verification: {'PASS' if verification_passed else 'FAIL'}")
    print(f"   Ready to commit: {'Yes' if verification_passed else 'No'}")

print(f"\n{'='*60}")
print("COMPLETION STATUS")
print(f"{'='*60}")
print("✅ Both files processed")
print("📋 Next steps:")
print("   1. Commit communio.html first in GitHub Desktop")
print("   2. Commit communio-register.html second in GitHub Desktop")
print("   3. Verify changes in browser if needed")