from pathlib import Path
import re

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Show exactly what's around don-gl
matches = re.findall('.{0,20}don-gl.{0,150}', html)
for m in matches[:3]:
    print(repr(m))