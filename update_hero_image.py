#!/usr/bin/env python3
import os

v3_dir = "/Users/christopherhoar/Desktop/v3"
communio_file = os.path.join(v3_dir, "communio.html")

print(f"Updating hero image in communio.html")
print("-" * 50)

# Read the file
with open(communio_file, 'r', encoding='utf-8') as f:
    content = f.read()

# Define old and new values
old_url = "https://images.unsplash.com/photo-1548449112-96a38a643324?auto=format&fit=crop&w=900&q=85"
new_url = "https://images.unsplash.com/photo-1531572753322-ad063cecc140?auto=format&fit=crop&w=900&q=85"

old_alt = "St. Stephen's Basilica, Budapest"
new_alt = "St. Peter's Basilica, Vatican City"

# Count occurrences before replacement
url_count = content.count(old_url)
alt_count = content.count(old_alt)

print(f"Found {url_count} occurrence(s) of old URL")
print(f"Found {alt_count} occurrence(s) of old alt text")
print()

# Replace URL
if url_count > 0:
    content = content.replace(old_url, new_url)
    print(f"✓ Replaced image URL with new Vatican image")
else:
    print("⚠ Old URL not found")

# Replace alt text
if alt_count > 0:
    content = content.replace(old_alt, new_alt)
    print(f"✓ Replaced alt text with 'St. Peter's Basilica, Vatican City'")
else:
    print("⚠ Old alt text not found")

# Write the updated content back
with open(communio_file, 'w', encoding='utf-8') as f:
    f.write(content)

print()
print("Update complete!")
print()

# Verify the changes
with open(communio_file, 'r', encoding='utf-8') as f:
    updated_content = f.read()

new_url_count = updated_content.count(new_url)
new_alt_count = updated_content.count(new_alt)

print("Verification:")
print(f"- New URL found: {new_url_count} time(s)")
print(f"- New alt text found: {new_alt_count} time(s)")
print(f"- Old URL remaining: {updated_content.count(old_url)} (should be 0)")
print(f"- Old alt text remaining: {updated_content.count(old_alt)} (should be 0)")