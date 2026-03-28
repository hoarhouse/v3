from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/index.html')
html = p.read_text(encoding='utf-8')

# Force all hero text to dark — override everything at end of first style block
override = (
  '.hero-h1{color:#0e0a06!important}'
  '.hero-sub{color:rgba(14,10,6,0.65)!important}'
  '.hero-actions .btn-ghost{color:#0e0a06!important;border-color:rgba(14,10,6,0.3)!important}'
  '.hero-trust{color:rgba(14,10,6,0.55)!important}'
  '.hero-trust strong{color:#0e0a06!important}'
  '.nav-name{color:#0e0a06!important}'
  '.nav-link{color:#0e0a06!important}'
)

html = html.replace('</style>', override + '</style>', 1)

p.write_text(html, encoding='utf-8')
print("Done. Override blocks added:", html.count('!important'))