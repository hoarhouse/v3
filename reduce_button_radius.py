#!/usr/bin/env python3
from pathlib import Path
import subprocess

def reduce_button_radius_in_file(file_path):
    """Reduce button pill radius in a single file"""
    print(f"\n{'='*60}")
    print(f"PROCESSING: {file_path.name}")
    print(f"{'='*60}")
    
    # Read the file
    content = file_path.read_text(encoding='utf-8')
    original_content = content
    
    print("\n1. BEFORE - Checking current --r-pill values:")
    print("-" * 45)
    pill_count_before = content.count("--r-pill")
    print(f"  --r-pill occurrences: {pill_count_before}")
    
    # Define replacements
    replacements = [
        ('--r-pill: 100px', '--r-pill: 8px'),
        ('--r-pill:100px', '--r-pill:8px'),
    ]
    
    print("\n2. APPLYING REPLACEMENTS:")
    print("-" * 30)
    
    total_replacements = 0
    for old, new in replacements:
        count = content.count(old)
        if count > 0:
            content = content.replace(old, new)
            print(f"  ✓ {old} → {new} ({count} times)")
            total_replacements += count
    
    if total_replacements == 0:
        print("  No --r-pill replacements needed")
    
    # Write the updated content back
    if content != original_content:
        file_path.write_text(content, encoding='utf-8')
        print(f"\n✅ Updated {file_path.name} ({total_replacements} replacements)")
        changes_made = True
    else:
        print(f"\n⚠ No changes were made to {file_path.name}")
        changes_made = False
    
    return changes_made

def verify_pill_changes(file_path):
    """Verify --r-pill changes using grep"""
    print(f"\n3. VERIFICATION for {file_path.name}:")
    print("-" * 35)
    
    try:
        result = subprocess.run([
            'grep', '-c', '--r-pill', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            count = int(result.stdout.strip())
            print(f"  ✓ --r-pill occurrences: {count}")
        else:
            print("  ✓ No --r-pill occurrences found")
            count = 0
        
        return count
    except Exception as e:
        print(f"  ❌ Error during grep verification: {e}")
        return -1

def check_hardcoded_button_radius(file_path):
    """Check for hardcoded border-radius on buttons > 8px"""
    print(f"\n4. CHECKING HARDCODED BUTTON RADIUS for {file_path.name}:")
    print("-" * 55)
    
    try:
        # Find lines with "btn" and "border-radius"
        result = subprocess.run([
            'grep', '-n', 'btn', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            btn_lines = result.stdout.strip().split('\n')
            
            # Filter for lines that also contain border-radius
            problematic_lines = []
            for line in btn_lines:
                if 'border-radius' in line:
                    # Check if it has a px value > 8
                    import re
                    matches = re.findall(r'border-radius[:\s]*(\d+)px', line)
                    for match in matches:
                        if int(match) > 8:
                            problematic_lines.append(line)
                            break
            
            if problematic_lines:
                print("  ❌ FOUND HARDCODED BUTTON RADIUS > 8px:")
                for line in problematic_lines[:5]:  # Show first 5
                    print(f"    {line}")
                return len(problematic_lines)
            else:
                print("  ✅ No hardcoded button border-radius > 8px found")
                return 0
        else:
            print("  ✅ No button elements found")
            return 0
            
    except Exception as e:
        print(f"  ❌ Error during button check: {e}")
        return -1

# Main execution
print("BUTTON PILL RADIUS REDUCTION")
print("=" * 60)

v3_dir = Path("/Users/christopherhoar/Desktop/v3")
files_to_process = [
    "communio.html",
    "communio-register.html", 
    "parish-profile.html",
    "communio-dashboard.html"
]

results = []

for filename in files_to_process:
    file_path = v3_dir / filename
    
    if not file_path.exists():
        print(f"❌ {filename} not found!")
        continue
    
    # Reduce button radius
    changes_made = reduce_button_radius_in_file(file_path)
    
    # Verify changes
    pill_count = verify_pill_changes(file_path)
    
    # Check for hardcoded button radius
    hardcoded_count = check_hardcoded_button_radius(file_path)
    
    print(f"\n📝 SUMMARY FOR {filename}:")
    print(f"   Changes made: {'Yes' if changes_made else 'No'}")
    print(f"   --r-pill count: {pill_count}")
    print(f"   Hardcoded btn radius > 8px: {hardcoded_count}")
    print(f"   Ready to commit: {'Yes' if changes_made else 'No'}")
    
    results.append({
        'file': filename,
        'changes': changes_made,
        'pill_count': pill_count,
        'hardcoded': hardcoded_count
    })

print(f"\n{'='*60}")
print("COMPLETION STATUS")
print(f"{'='*60}")
print("✅ All four Communio files processed for button radius reduction")
print("📋 Commit order in GitHub Desktop:")
print("   1. communio.html          — 'Reduce button radius — communio'")
print("   2. communio-register.html — 'Reduce button radius — register'") 
print("   3. parish-profile.html    — 'Reduce button radius — profile'")
print("   4. communio-dashboard.html — 'Reduce button radius — dashboard'")

# Summary table
print(f"\n📊 SUMMARY TABLE:")
print("-" * 70)
print(f"{'File':<25} {'Changes':<8} {'--r-pill':<10} {'Hardcoded>8px':<12}")
print("-" * 70)
for result in results:
    print(f"{result['file']:<25} {'Yes' if result['changes'] else 'No':<8} {result['pill_count']:<10} {result['hardcoded']:<12}")
print("-" * 70)