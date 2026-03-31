// ── PARISH DATA — Single source of truth ──────────────────────
// Edit values here. They update everywhere automatically.
// When Supabase is connected, this file is replaced by an API call.

const PARISH = {

  // ── Core identity ──────────────────────────────────────────
  name:           "St. Mary's Parish",
  shortName:      "St. Mary's",
  tagline:        "A vibrant Catholic community in the heart of New York's Lower East Side, serving our neighbours since 1887.",
  founded:        "1887",
  diocese:        "Archdiocese of New York",

  // ── Contact ────────────────────────────────────────────────
  address:        "123 Rivington Street",
  city:           "New York",
  state:          "NY",
  zip:            "10002",
  phone:          "(212) 555-0123",
  email:          "info@stmarysnyc.org",
  mapsUrl:        "https://maps.google.com/?q=123+Rivington+Street+New+York+NY+10002",

  // ── Office hours ───────────────────────────────────────────
  officeHours: {
    weekday:  "Mon–Fri 9:00 AM – 5:00 PM",
    saturday: "Saturday 10:00 AM – 2:00 PM",
    sunday:   "After 11:00 AM Mass"
  },

  // ── Pastor ─────────────────────────────────────────────────
  pastor: {
    name:   "Fr. Michael O'Brien",
    email:  "pastor@stmarysnyc.org",
    since:  "2015"
  },

  // ── Mass times ─────────────────────────────────────────────
  massTimes: {
    weekday:    "Mon–Fri 9:00 AM · Tue & Thu 6:45 PM",
    saturday:   "10:00 AM · Vigil 5:00 PM",
    sunday:     "7:00 · 9:00 · 11:00 AM · 1:00 PM (Español) · 6:00 PM",
    confession: "Saturday 3:30–4:30 PM or by appointment"
  },

  // ── Stats ──────────────────────────────────────────────────
  stats: {
    families:     "1,200+",
    sundayMasses: "7",
    founded:      "Est. 1887"
  },

  // ── Social media ───────────────────────────────────────────
  social: {
    facebook:  "https://facebook.com",
    instagram: "https://instagram.com",
    youtube:   "https://youtube.com",
    spotify:   "https://spotify.com"
  },

  // ── Website ────────────────────────────────────────────────
  websiteUrl:    "https://stmarysnyc.communio.org",
  communioUrl:   "https://communio.org",

  // ── Copyright ──────────────────────────────────────────────
  copyrightYear: new Date().getFullYear()

};

// ── Auto-inject into DOM ───────────────────────────────────────
// Any element with data-parish="key" gets its text replaced.
// Any element with data-parish-href="key" gets its href replaced.
// Nested keys use dot notation: data-parish="massTimes.sunday"

document.addEventListener('DOMContentLoaded', function(){

  function getVal(key) {
    return key.split('.').reduce(function(obj, k){ return obj && obj[k]; }, PARISH);
  }

  // Text injection
  document.querySelectorAll('[data-parish]').forEach(function(el){
    var val = getVal(el.getAttribute('data-parish'));
    if(val !== undefined) el.textContent = val;
  });

  // Href injection
  document.querySelectorAll('[data-parish-href]').forEach(function(el){
    var val = getVal(el.getAttribute('data-parish-href'));
    if(val !== undefined) el.href = val;
  });

  // Copyright year
  document.querySelectorAll('[data-parish-year]').forEach(function(el){
    el.textContent = PARISH.copyrightYear;
  });

  // Social links
  document.querySelectorAll('[data-parish-social]').forEach(function(el){
    var network = el.getAttribute('data-parish-social');
    if(PARISH.social[network]) el.href = PARISH.social[network];
  });

});
