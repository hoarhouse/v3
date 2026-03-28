from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/website.html')
h = f.read_text(encoding='utf-8')

old = """function scrollToSection(id) {
  var containers = ['pv-wrap', 'pm-body'];
  containers.forEach(function(cid) {
    var c = document.getElementById(cid);
    if (!c) return;
    var t = c.querySelector('#ws-' + id);
    if (!t) return;
    c.scrollTo({top: t.offsetTop - 48, behavior: 'smooth'});
  });
}"""

new = """function scrollToSection(id) {
  var containers = ['pv-wrap', 'pm-body'];
  containers.forEach(function(cid) {
    var c = document.getElementById(cid);
    if (!c) return;
    var t = c.querySelector('#ws-' + id);
    if (!t) return;
    var cRect = c.getBoundingClientRect();
    var tRect = t.getBoundingClientRect();
    var offset = tRect.top - cRect.top + c.scrollTop - 48;
    c.scrollTo({top: offset, behavior: 'smooth'});
  });
}"""

if old in h:
    h = h.replace(old, new)
    f.write_text(h, encoding='utf-8')
    print('Fixed scrollToSection')
else:
    print('Pattern not found - check whitespace')