from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# The removal script left behind the closing > of the anchor/span tags
# Donations card: ">Monthly giving goal"
html = html.replace('>Monthly giving goal', 'Monthly giving goal')

# Contact card: "> " before the ct-row content
html = html.replace('class="ct-row"><span class="shared-notice">⚙ Shared from Settings — edit in Settings →</span', 'class="ct-row"')

# Also clean any bare > that got left in front of ct-row content
html = html.replace('class="ct-row">>', 'class="ct-row">')

p.write_text(html, encoding='utf-8')
print("Stray > remaining near 'Monthly giving goal':", html.count('>Monthly giving goal'))
print("Done")