from pathlib import Path

f = Path('/Users/christopherhoar/Desktop/v3/communio/dashboard/website.html')
h = f.read_text(encoding='utf-8')

# 1 — Add section IDs to the generated HTML sections
h = h.replace(
    "'<div style=\"background:' + p.navBg + ';border-bottom:2px solid ' + p.navBorder",
    "'<div id=\"ws-top\" style=\"background:' + p.navBg + ';border-bottom:2px solid ' + p.navBorder"
)
h = h.replace(
    "+'<div style=\"background:' + heroStyle + ';position:relative;'",
    "+'<div id=\"ws-hero\" style=\"background:' + heroStyle + ';position:relative;'"
)
h = h.replace(
    "+ '<div style=\"display:grid;grid-template-columns:1fr 1fr;gap:' + g",
    "+ '<div id=\"ws-mass\" style=\"display:grid;grid-template-columns:1fr 1fr;gap:' + g"
)
h = h.replace(
    "+ '<div style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'",
    "+ '<div id=\"ws-about\" style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'",
    1
)
h = h.replace(
    "+ '<div style=\"background:#000;border-radius:10px;padding:' + cp",
    "+ '<div id=\"ws-donate\" style=\"background:#000;border-radius:10px;padding:' + cp"
)
h = h.replace(
    "+ '<div style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'   + '<div style=\"font-size:8px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:' + p.lblClr + ';margin-bottom:8px;\">Contact",
    "+ '<div id=\"ws-contact\" style=\"background:' + p.cardBg + ';border:1px solid ' + p.cardBorder + ';border-radius:10px;padding:' + cp + ';\">'   + '<div style=\"font-size:8px;font-weight:700;letter-spacing:.07em;text-transform:uppercase;color:' + p.lblClr + ';margin-bottom:8px;\">Contact"
)

# 2 — Make nav links call scrollToSection
h = h.replace(
    "'<span style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);\">About</span>'",
    "'<span onclick=\"scrollToSection(\\'about\\')\" style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);cursor:pointer;\">About</span>'"
)
h = h.replace(
    "'<span style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);\">Mass</span>'",
    "'<span onclick=\"scrollToSection(\\'mass\\')\" style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);cursor:pointer;\">Mass</span>'"
)
h = h.replace(
    "'<span style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);\">Contact</span>'",
    "'<span onclick=\"scrollToSection(\\'contact\\')\" style=\"font-size:' + (full?'12px':'9px') + ';color:rgba(255,255,255,0.5);cursor:pointer;\">Contact</span>'"
)
h = h.replace(
    "'<div style=\"font-size:' + (full?'11px':'8px') + ';font-weight:700;background:#d85020;color:#fff;padding:' + (full?'6px 14px':'3px 8px') + ';border-radius:5px;\">Donate</div>'",
    "'<div onclick=\"scrollToSection(\\'donate\\')\" style=\"font-size:' + (full?'11px':'8px') + ';font-weight:700;background:#d85020;color:#fff;padding:' + (full?'6px 14px':'3px 8px') + ';border-radius:5px;cursor:pointer;\">Donate</div>'"
)
h = h.replace(
    "'<div style=\"font-size:' + (full?'12px':'9px') + ';font-weight:700;background:' + p.btnBg + ';color:' + p.btnClr + ';padding:' + (full?'8px 16px':'4px 9px') + ';border-radius:5px;\">Join us Sunday →</div>'",
    "'<div onclick=\"scrollToSection(\\'mass\\')\" style=\"font-size:' + (full?'12px':'9px') + ';font-weight:700;background:' + p.btnBg + ';color:' + p.btnClr + ';padding:' + (full?'8px 16px':'4px 9px') + ';border-radius:5px;cursor:pointer;\">Join us Sunday →</div>'"
)

# 3 — Add scrollToSection function before the closing </script>
scroll_fn = """
function scrollToSection(id) {
  var containers = ['pv-wrap', 'pm-body'];
  containers.forEach(function(cid) {
    var c = document.getElementById(cid);
    if (!c) return;
    var t = c.querySelector('#ws-' + id);
    if (!t) return;
    c.scrollTo({top: t.offsetTop - 48, behavior: 'smooth'});
  });
}
"""
h = h.replace('document.getElementById(\'pm\').addEventListener', scroll_fn + '\ndocument.getElementById(\'pm\').addEventListener')

f.write_text(h, encoding='utf-8')
print('Done - scrollToSection added')