from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/communio.css')
css = p.read_text(encoding='utf-8')

# Find the btn-hero rule and add line-height to it
css = css.replace(
    '.btn-hero{',
    '.btn-hero{line-height:20.8px;'
)

p.write_text(css, encoding='utf-8')
print("Done:", css.count('line-height:20.8px'))