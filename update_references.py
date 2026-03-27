#!/usr/bin/env python3
import os

v3_dir = "/Users/christopherhoar/Desktop/v3"

# Replace communio-v2.html with communio.html in communio-register.html
register_file = os.path.join(v3_dir, "communio-register.html")
print(f"Processing {register_file}")

with open(register_file, 'r', encoding='utf-8') as f:
    content = f.read()

old_ref = "communio-v2.html"
new_ref = "communio.html"
occurrences = content.count(old_ref)
print(f"Found {occurrences} occurrences of '{old_ref}'")

if occurrences > 0:
    content = content.replace(old_ref, new_ref)
    with open(register_file, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Replaced all occurrences with '{new_ref}'")
else:
    print("No replacements needed")

print("\nDone!")