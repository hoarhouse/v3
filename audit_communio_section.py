#!/usr/bin/env python3
from pathlib import Path
import re
import subprocess

# File paths
base_dir = Path("/Users/christopherhoar/Desktop/v3")
files = [
    "communio.html",
    "communio-register.html", 
    "parish-profile.html",
    "communio-dashboard.html"
]

print("COMMUNIO SECTION AUDIT")
print("=" * 80)

results = []
passed = 0
failed = 0
warnings = 0

def add_result(status, file_name, check, detail):
    global passed, failed, warnings
    results.append((status, file_name, check, detail))
    if status == "PASS":
        passed += 1
    elif status == "FAIL":
        failed += 1
    elif status == "WARNING":
        warnings += 1

def grep_count(file_path, pattern):
    """Get count of pattern matches in file"""
    try:
        content = file_path.read_text(encoding='utf-8')
        return len(re.findall(pattern, content))
    except:
        return 0

def grep_lines(file_path, pattern):
    """Get lines matching pattern"""
    try:
        content = file_path.read_text(encoding='utf-8')
        lines = []
        for i, line in enumerate(content.split('\n'), 1):
            if re.search(pattern, line):
                lines.append(f"{i}:{line.strip()}")
        return lines
    except:
        return []

print("\n1. FILE EXISTENCE")
print("-" * 40)

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        add_result("PASS", file_name, "File exists", f"Found {file_name}")
        print(f"  ✓ {file_name}")
    else:
        add_result("FAIL", file_name, "File exists", f"Missing {file_name}")
        print(f"  ✗ {file_name}")

print("\n2. ONYX & FLAME PALETTE - CORE COLORS")
print("-" * 40)

# Colors that SHOULD be present
required_colors = {
    "#d85020": "flame orange/terracotta",
    "#e8c040": "gold/amber", 
    "#000000": "pure black ink",
    "#f5f2e8": "warm white cream"
}

# Colors that should be GONE
forbidden_colors = {
    "#c85c3a": "old terracotta",
    "#4a7c59": "old sage",
    "#1a1208": "old ink",
    "#faf6f0": "old cream",
    "#faf7f2": "Roma cream", 
    "#1e1a14": "Roma ink",
    "#e0a23a": "old amber",
    "#d4922a": "previous amber"
}

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        # Check required colors
        for color, desc in required_colors.items():
            count = grep_count(file_path, re.escape(color))
            if count > 0:
                add_result("PASS", file_name, f"Required color {color}", f"{count} occurrences of {desc}")
                print(f"    ✓ {color} ({desc}): {count}")
            else:
                add_result("FAIL", file_name, f"Required color {color}", f"Missing {desc}")
                print(f"    ✗ {color} ({desc}): 0")
        
        # Check forbidden colors
        for color, desc in forbidden_colors.items():
            count = grep_count(file_path, re.escape(color))
            if count == 0:
                add_result("PASS", file_name, f"Forbidden color {color}", f"Correctly removed {desc}")
            else:
                add_result("FAIL", file_name, f"Forbidden color {color}", f"Still contains {count} instances of {desc}")
                print(f"    ✗ {color} ({desc}): {count} (should be 0)")

print("\n3. BUTTON BACKGROUNDS - HARDCODED HEX CHECK")
print("-" * 40)

button_patterns = [
    "btn-main", "btn-terra", "btn-primary", "nav-btn", 
    "nav-back", "wl-cta", "dw-btn"
]

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        for pattern in button_patterns:
            lines = grep_lines(file_path, f"{pattern}.*background")
            if lines:
                for line in lines:
                    if "var(--terra)" in line:
                        add_result("WARNING", file_name, f"Button {pattern}", f"Uses var(--terra): {line}")
                        print(f"    ⚠ {pattern}: uses var(--terra)")
                    elif "transparent" in line or "rgba(0,0,0,0)" in line:
                        add_result("FAIL", file_name, f"Button {pattern}", f"Transparent background: {line}")
                        print(f"    ✗ {pattern}: transparent background")
                    elif "#d85020" in line:
                        add_result("PASS", file_name, f"Button {pattern}", f"Hardcoded #d85020: {line}")
                        print(f"    ✓ {pattern}: hardcoded #d85020")

print("\n4. STALE BRAND REFERENCES")
print("-" * 40)

stale_refs = {
    "parish-register-v3.html": 0,
    "communio-v2.html": 0,
    "DCF Global Parish Network": 0,
    "Cormorant Garamond": 0,
    "Jost": 0,
    "--navy": 0,
    "--gold": 0
}

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        for ref, expected in stale_refs.items():
            count = grep_count(file_path, re.escape(ref))
            if count == expected:
                add_result("PASS", file_name, f"Stale ref {ref}", f"Correctly {count} occurrences")
                print(f"    ✓ {ref}: {count}")
            else:
                add_result("FAIL", file_name, f"Stale ref {ref}", f"Found {count}, expected {expected}")
                print(f"    ✗ {ref}: {count} (should be {expected})")

print("\n5. FONT CONSISTENCY")
print("-" * 40)

fonts = {"Outfit": "> 0", "Lora": "> 0"}

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        for font, expected in fonts.items():
            count = grep_count(file_path, font)
            if count > 0:
                add_result("PASS", file_name, f"Font {font}", f"{count} occurrences")
                print(f"    ✓ {font}: {count}")
            else:
                add_result("FAIL", file_name, f"Font {font}", f"Missing {font} font")
                print(f"    ✗ {font}: 0 (should be > 0)")

print("\n6. NAVIGATION CONSISTENCY") 
print("-" * 40)

nav_checks = {
    "communio.html": ("nav-btn", "> 0"),
    "communio-register.html": ("nav-back", "> 0"),
    "parish-profile.html": ("sw-btn", "> 0"),
    "communio-dashboard.html": [
        ("tab-bar", "> 0"),
        ("class=\"sidebar\"", "= 0"),
        ("setup-strip", "= 0")
    ]
}

for file_name, checks in nav_checks.items():
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        if isinstance(checks, tuple):
            checks = [checks]
        
        for pattern, expected in checks:
            count = grep_count(file_path, pattern)
            if expected == "> 0" and count > 0:
                add_result("PASS", file_name, f"Navigation {pattern}", f"{count} occurrences")
                print(f"    ✓ {pattern}: {count}")
            elif expected == "= 0" and count == 0:
                add_result("PASS", file_name, f"Navigation {pattern}", f"Correctly removed")
                print(f"    ✓ {pattern}: 0 (correctly removed)")
            else:
                add_result("FAIL", file_name, f"Navigation {pattern}", f"Found {count}, expected {expected}")
                print(f"    ✗ {pattern}: {count} (expected {expected})")

print("\n7. PHP MARKERS")
print("-" * 40)

php_files = ["communio-register.html", "communio-dashboard.html"]

for file_name in php_files:
    file_path = base_dir / file_name
    if file_path.exists():
        count = grep_count(file_path, "PHP:")
        if count > 0:
            add_result("PASS", file_name, "PHP markers", f"{count} PHP markers found")
            print(f"  ✓ {file_name}: {count} PHP markers")
        else:
            add_result("FAIL", file_name, "PHP markers", "No PHP markers found")
            print(f"  ✗ {file_name}: 0 PHP markers (should be > 0)")

print("\n8. MOBILE VIEWPORT")
print("-" * 40)

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        count = grep_count(file_path, "viewport")
        if count == 1:
            add_result("PASS", file_name, "Viewport", "Single viewport meta tag")
            print(f"  ✓ {file_name}: 1 viewport")
        else:
            add_result("FAIL", file_name, "Viewport", f"Found {count}, expected 1")
            print(f"  ✗ {file_name}: {count} viewport tags (should be 1)")

print("\n9. EIN REFERENCE")
print("-" * 40)

ein_files = ["communio.html", "communio-register.html"]

for file_name in ein_files:
    file_path = base_dir / file_name
    if file_path.exists():
        count = grep_count(file_path, "99-1778616")
        if count > 0:
            add_result("PASS", file_name, "EIN reference", f"{count} EIN references")
            print(f"  ✓ {file_name}: {count} EIN references")
        else:
            add_result("FAIL", file_name, "EIN reference", "No EIN references found")
            print(f"  ✗ {file_name}: 0 EIN references (should be > 0)")

print("\n10. JAVASCRIPT FUNCTIONS")
print("-" * 40)

js_checks = {
    "parish-profile.html": [
        ("function sw\\(", "> 0"),
        ("DOMContentLoaded", "> 0")
    ],
    "communio-dashboard.html": [
        ("function go\\(", "> 0"),
        ("function navTo\\(", "> 0"), 
        ("function updateTabBar\\(", "> 0"),
        ("DOMContentLoaded", "> 0")
    ]
}

for file_name, checks in js_checks.items():
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        for pattern, expected in checks:
            count = grep_count(file_path, pattern)
            if count > 0:
                add_result("PASS", file_name, f"JS function {pattern}", f"{count} occurrences")
                print(f"    ✓ {pattern}: {count}")
            else:
                add_result("FAIL", file_name, f"JS function {pattern}", f"Missing function")
                print(f"    ✗ {pattern}: 0 (should be > 0)")

print("\n11. BORDER RADIUS")
print("-" * 40)

for file_name in files:
    file_path = base_dir / file_name
    if file_path.exists():
        print(f"\n  {file_name}:")
        
        lines = grep_lines(file_path, "border-radius")
        high_radius_found = False
        
        for line in lines:
            # Skip allowed patterns
            if any(pattern in line for pattern in ["50%", "var(", "pill"]):
                continue
            
            # Extract radius values
            radius_matches = re.findall(r'border-radius:[^;]*?(\d+)px', line)
            for radius in radius_matches:
                if int(radius) > 10:
                    add_result("FAIL", file_name, "Border radius", f"Value {radius}px > 10px: {line}")
                    print(f"    ✗ border-radius: {radius}px (> 10px)")
                    high_radius_found = True
        
        if not high_radius_found:
            add_result("PASS", file_name, "Border radius", "All values ≤ 10px")
            print(f"    ✓ All border-radius values ≤ 10px")

print("\n" + "=" * 80)
print("AUDIT SUMMARY")
print("=" * 80)

print(f"\n{'STATUS':<8} | {'FILE':<20} | {'CHECK':<25} | DETAIL")
print("-" * 80)

for status, file_name, check, detail in results:
    print(f"{status:<8} | {file_name:<20} | {check:<25} | {detail}")

print(f"\n" + "=" * 80)
print(f"FINAL SCORE: {passed} passed, {failed} failed, {warnings} warnings")
print("=" * 80)

# List Python fixes needed for failures
if failed > 0:
    print(f"\nPYTHON FIXES NEEDED:")
    print("-" * 40)
    
    fixes = []
    for status, file_name, check, detail in results:
        if status == "FAIL":
            if "Required color" in check:
                color = check.split()[-1]
                fixes.append(f"Add {color} to {file_name}: Use find/replace or CSS variable updates")
            elif "Forbidden color" in check:
                color = check.split()[-1] 
                fixes.append(f"Remove {color} from {file_name}: content.replace('{color}', 'new_color')")
            elif "Button" in check and "transparent" in detail:
                fixes.append(f"Fix button in {file_name}: Replace transparent with #d85020")
            elif "Stale ref" in check:
                ref = check.replace("Stale ref ", "")
                fixes.append(f"Remove '{ref}' from {file_name}")
            elif "Font" in check:
                font = check.split()[-1]
                fixes.append(f"Add {font} font import to {file_name}")
            elif "Navigation" in check:
                pattern = check.split()[-1]
                if "= 0" in detail:
                    fixes.append(f"Remove {pattern} from {file_name}")
                else:
                    fixes.append(f"Add {pattern} to {file_name}")
            elif "PHP markers" in check:
                fixes.append(f"Add PHP: comments to {file_name}")
            elif "Viewport" in check:
                fixes.append(f"Fix viewport meta tag in {file_name}")
            elif "EIN reference" in check:
                fixes.append(f"Add EIN 99-1778616 to {file_name}")
            elif "JS function" in check:
                func = check.replace("JS function ", "")
                fixes.append(f"Add {func} to {file_name}")
            elif "Border radius" in check:
                fixes.append(f"Reduce border-radius values > 10px in {file_name}")
    
    for i, fix in enumerate(fixes, 1):
        print(f"{i}. {fix}")

print(f"\n🎯 Audit complete!")