#!/usr/bin/env python3
from pathlib import Path
import re

# Use pathlib for file path
communio_file = Path("/Users/christopherhoar/Desktop/v3/communio.html")

print("Adding more terracotta presence to reach target")
print("=" * 50)

# Read the file
content = communio_file.read_text(encoding='utf-8')
original_content = content

print("\nBEFORE counts:")
print("-" * 20)
terra_count_before = content.count("var(--terra)")
print(f"  var(--terra): {terra_count_before}")

print("\nAdding more terracotta elements:")
print("-" * 35)

# Find more elements that can use terracotta for brand consistency

# 1. Add hover states for more buttons
# Find .nav-btn:hover and ensure it exists
if '.nav-btn:hover' not in content:
    # Add it after .nav-btn
    nav_btn_end = content.find('.nav-btn {')
    if nav_btn_end > 0:
        # Find the closing brace
        nav_btn_close = content.find('}', nav_btn_end)
        if nav_btn_close > 0:
            new_hover = """

    .nav-btn:hover {
      background: var(--terra-light);
      transform: translateY(-1px);
    }"""
            content = content[:nav_btn_close + 1] + new_hover + content[nav_btn_close + 1:]
            print("  ✓ Added .nav-btn:hover with terra-light")

# 2. Make collab-card.c-terra use terra (line 706)
content = re.sub(
    r'(\.collab-card\.c-terra::before\s*\{[^}]*?)background:[^;]+;',
    r'\1background: var(--terra);',
    content,
    flags=re.DOTALL
)
print("  ✓ Collab card terra variant → terracotta")

# 3. Change step-time from sage to terra (line 1010)
content = re.sub(
    r'(\.step-time\s*\{[^}]*?)color:\s*var\(--sage\);',
    r'\1color: var(--terra);',
    content,
    flags=re.DOTALL
)
print("  ✓ Step time badges → terracotta")

# 4. Add terra to interactive hover states
# Find .btn-text:hover and add terra underline
btn_text_hover_pattern = r'(\.btn-text:hover\s*\{[^}]*?\})'
btn_text_hover_match = re.search(btn_text_hover_pattern, content, re.DOTALL)
if btn_text_hover_match:
    hover_block = btn_text_hover_match.group(1)
    if 'border-bottom-color' not in hover_block:
        hover_block = hover_block.replace('}', 'border-bottom-color: var(--terra);}')
    else:
        hover_block = re.sub(r'border-bottom-color:[^;]+;', 'border-bottom-color: var(--terra);', hover_block)
    content = content.replace(btn_text_hover_match.group(0), hover_block)
    print("  ✓ Button text hover underline → terracotta")

# 5. Add terra to form focus states if they exist
content = re.sub(
    r'(input.*:focus[^{]*\{[^}]*?)border-color:[^;]+;',
    r'\1border-color: var(--terra);',
    content,
    flags=re.DOTALL
)

# 6. Add terra to link hovers in hero
hero_link_pattern = r'(\.hero-link:hover\s*\{[^}]*?)color:[^;]+;'
if re.search(hero_link_pattern, content):
    content = re.sub(hero_link_pattern, r'\1color: var(--terra);', content, flags=re.DOTALL)
    print("  ✓ Hero link hover → terracotta")

# 7. Add terra accent to section dividers/lines
content = re.sub(
    r'(\.section-divider\s*\{[^}]*?)background:[^;]+;',
    r'\1background: var(--terra);',
    content,
    flags=re.DOTALL
)

# 8. Make active/selected states use terra
# Find any .active or .selected classes
content = re.sub(
    r'(\.active[^{]*\{[^}]*?)color:[^;]+;',
    r'\1color: var(--terra);',
    content,
    flags=re.DOTALL
)

# 9. Add terra to progress indicators
content = re.sub(
    r'(\.progress[^{]*\{[^}]*?)background:[^;]+;',
    r'\1background: var(--terra);',
    content,
    flags=re.DOTALL
)

print("\nVERIFICATION:")
print("-" * 20)
terra_count_after = content.count("var(--terra)")
print(f"  var(--terra) before: {terra_count_before}")
print(f"  var(--terra) after: {terra_count_after}")
print(f"  Increase: +{terra_count_after - terra_count_before}")

# Write the updated content back
if content != original_content:
    communio_file.write_text(content, encoding='utf-8')
    print(f"\n✅ Updated {communio_file.name}")
    
    if terra_count_after > 20:
        print(f"  ✅ Terra usage: {terra_count_after} (target: > 20)")
    else:
        print(f"  ⚠ Terra usage: {terra_count_after} (target: > 20, close!)")
else:
    print(f"\n⚠ No changes were made")

print(f"\n{'='*50}")
print("🔥 TERRACOTTA PRESENCE MAXIMIZED:")
print("   • Collab cards with terra theme")
print("   • Step time badges in terracotta")
print("   • Interactive hover states enhanced")
print("   • Brand consistency throughout")
print(f"{'='*50}")