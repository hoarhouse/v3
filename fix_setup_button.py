from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/setup.html')
h = f.read_text(encoding='utf-8')

# Fix "Preview first" button - should go to website editor not public profile
h = h.replace(
    '<a href="../parish/profile.html" class="btn btn-secondary btn-sm">Preview first</a>',
    '<a href="website.html" class="btn btn-secondary btn-sm">Edit website</a>'
)

f.write_text(h, encoding='utf-8')
print('Fixed')
print('Verify:', '../parish/profile.html' in f.read_text(encoding='utf-8').split('Preview public profile')[1][:50] if 'Preview public profile' in f.read_text(encoding='utf-8') else 'check manually')