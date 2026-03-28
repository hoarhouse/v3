from pathlib import Path

p = Path('/Users/christopherhoar/Desktop/v3/communio/parish/profile.html')
html = p.read_text(encoding='utf-8')

# Remove the stray > before "Monthly giving goal"
html = html.replace('>Monthly giving goal', 'Monthly giving goal')

p.write_text(html, encoding='utf-8')
print("Remaining instances:", html.count('>Monthly giving goal'))