from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/website.html')
h = f.read_text(encoding='utf-8')

# Fix hero ID — find the hero div and add id
h = h.replace(
    "+ '<div style=\"background:' + heroStyle + ';position:relative;'",
    "+ '<div id=\"ws-hero\" style=\"background:' + heroStyle + ';position:relative;'"
)

f.write_text(h, encoding='utf-8')

# Verify all IDs are present
h2 = f.read_text(encoding='utf-8')
ids = ['ws-top', 'ws-hero', 'ws-mass', 'ws-about', 'ws-donate', 'ws-contact']
for id in ids:
    count = h2.count(id)
    print(f'{id}: {count}')