from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# The masthead div has lost its class — find it and restore it
# The div contains mh-overlay as its first child
# It currently looks like: <div class=""><div class="mh-overlay">
# or possibly just: <div ><div class="mh-overlay">

print("checking variants:")
print('class=""><div class="mh-overlay"' in html)
print('class=" "><div class="mh-overlay"' in html)
print('<div ><div class="mh-overlay"' in html)
print('<div><div class="mh-overlay"' in html)