(function() {
  var path = window.location.pathname;
  var page = path.split('/').pop() || 'index.html';
  var deliveredPages = ['index.html','mavir.html','kau.html','helix.html','eidas.html','corpex.html','ipcei-cis.html','ambiti8n.html','proofx.html','genesis.html','coios.html','repox.html','press.html','delivered.html'];
  var peoplePages = ['people.html','peter-antal.html'];
  var sciencePages = ['science.html','medical-ai.html'];
  var recognitionPages = ['recognition.html'];
  var factsPages = ['facts.html'];
  var section = deliveredPages.includes(page) ? 'delivered' : peoplePages.includes(page) ? 'people' : sciencePages.includes(page) ? 'science' : recognitionPages.includes(page) ? 'recognition' : factsPages.includes(page) ? 'facts' : 'delivered';
  function a(label, href, key) {
    var active = section === key;
    return '<a href="' + href + '" style="font-family:\'DM Mono\',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;text-decoration:none;padding:8px 0;border-bottom:2px solid ' + (active ? '#C8A96E' : 'transparent') + ';color:' + (active ? '#C8A96E' : '#666') + ';transition:color 0.2s;">' + label + '</a>';
  }
  var html = '<div id="record-subnav" style="position:fixed;top:72px;left:0;right:0;z-index:999;background:rgba(8,8,8,0.97);border-bottom:1px solid #1a1a1a;display:flex;align-items:center;justify-content:center;gap:40px;padding:0 48px;height:40px;">'
    + a('Delivered', 'delivered.html', 'delivered')
    + a('The People', 'people.html', 'people')
    + a('The Science', 'science.html', 'science')
    + a('Recognition', 'recognition.html', 'recognition')
    + a('The Facts', 'facts.html', 'facts')
    + '</div>'
    + '<div style="height:40px;"></div>';
  document.currentScript
    ? document.currentScript.insertAdjacentHTML('afterend', html)
    : document.addEventListener('DOMContentLoaded', function() {
        var nav = document.getElementById('record-subnav');
        if (!nav) document.body.insertAdjacentHTML('afterbegin', html);
      });
})();
