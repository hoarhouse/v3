#!/usr/bin/env python3
from pathlib import Path
import subprocess

def check_palette_in_file(file_path):
    """Check Roma palette state in a single file"""
    print(f"\n{'='*60}")
    print(f"CHECKING: {file_path.name}")
    print(f"{'='*60}")
    
    print("\n1. ink: values (first 5 lines):")
    print("-" * 35)
    try:
        result = subprocess.run([
            'grep', '-n', 'ink:', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[:5]
            for line in lines:
                print(f"  {line}")
        else:
            print("  No 'ink:' found")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n2. warm-white values (first 5 lines):")
    print("-" * 40)
    try:
        result = subprocess.run([
            'grep', '-n', 'warm-white', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[:5]
            for line in lines:
                print(f"  {line}")
        else:
            print("  No 'warm-white' found")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n3. cream: values (first 5 lines):")
    print("-" * 35)
    try:
        result = subprocess.run([
            'grep', '-n', 'cream:', str(file_path)
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            lines = result.stdout.strip().split('\n')[:5]
            for line in lines:
                print(f"  {line}")
        else:
            print("  No 'cream:' found")
    except Exception as e:
        print(f"  Error: {e}")
    
    print("\n4. SPECIFIC COLOR VERIFICATION:")
    print("-" * 35)
    
    content = file_path.read_text(encoding='utf-8')
    
    # Check for new Roma colors
    new_ink = content.count("#1e1a14")
    new_warm_white_cream = content.count("#faf7f2")
    
    # Check for old colors
    old_ink = content.count("#1a1208")
    old_warm_white = content.count("#fffdf9")
    old_cream = content.count("#faf6f0")
    
    print(f"  NEW ROMA COLORS:")
    print(f"    #1e1a14 (new ink):         {new_ink}")
    print(f"    #faf7f2 (new warm/cream):  {new_warm_white_cream}")
    
    print(f"  OLD COLORS:")
    print(f"    #1a1208 (old ink):         {old_ink}")
    print(f"    #fffdf9 (old warm-white):  {old_warm_white}")
    print(f"    #faf6f0 (old cream):       {old_cream}")
    
    # Determine palette state
    has_new_colors = new_ink > 0 and new_warm_white_cream > 0
    has_old_colors = old_ink > 0 or old_warm_white > 0 or old_cream > 0
    
    if has_new_colors and not has_old_colors:
        palette_status = "✅ ROMA PALETTE APPLIED"
    elif has_old_colors and not has_new_colors:
        palette_status = "❌ OLD PALETTE STILL PRESENT"
    elif has_new_colors and has_old_colors:
        palette_status = "⚠️ MIXED PALETTE (INCOMPLETE CONVERSION)"
    else:
        palette_status = "❓ UNKNOWN STATE"
    
    print(f"\n  STATUS: {palette_status}")

# Main execution
print("ROMA PALETTE STATE CHECK")
print("=" * 60)

v3_dir = Path("/Users/christopherhoar/Desktop/v3")
files_to_check = [
    "communio.html",
    "communio-register.html", 
    "parish-profile.html",
    "communio-dashboard.html"
]

for filename in files_to_check:
    file_path = v3_dir / filename
    
    if not file_path.exists():
        print(f"❌ {filename} not found!")
        continue
    
    check_palette_in_file(file_path)

print(f"\n{'='*60}")
print("ADDITIONAL CHECKS")
print(f"{'='*60}")