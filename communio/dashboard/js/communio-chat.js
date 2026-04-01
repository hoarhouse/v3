(function(){
if(document.getElementById('cm-chat-root')) return;

var CSS = `
@keyframes cm-pulse{0%,100%{opacity:1;transform:scale(1)}50%{opacity:.6;transform:scale(.85)}}
@keyframes cm-toast-in{from{opacity:0;transform:translateY(8px)}to{opacity:1;transform:translateY(0)}}
@keyframes cm-panel-in{from{opacity:0;transform:translateY(10px) scale(.97)}to{opacity:1;transform:translateY(0) scale(1)}}
#cm-chat-root *{box-sizing:border-box;margin:0;padding:0;font-family:'Outfit',sans-serif}
#cm-chat-root{position:fixed;bottom:24px;right:24px;z-index:9999;display:flex;flex-direction:column;align-items:flex-end;gap:8px}
.cm-context-strip{background:#f0fdf4;border:1px solid #bbf7d0;border-radius:20px;padding:7px 14px;font-size:12px;font-weight:700;color:#15803d;display:none;align-items:center;gap:5px;cursor:pointer;white-space:nowrap}
.cm-context-strip.show{display:flex}
.cm-context-dot{width:6px;height:6px;border-radius:50%;background:#22c55e;animation:cm-pulse 2s infinite;flex-shrink:0}
.cm-btn{width:52px;height:52px;border-radius:50%;background:#d85020;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;position:relative;transition:background .15s;flex-shrink:0}
.cm-btn:hover{background:#c04418}
.cm-badge{position:absolute;top:-2px;right:-2px;min-width:18px;height:18px;border-radius:9px;background:#e24b4a;border:2px solid #faf8f4;font-size:10px;font-weight:800;color:white;display:none;align-items:center;justify-content:center;padding:0 4px}
.cm-badge.show{display:flex}
.cm-toast{background:white;border:1px solid #e8e2d6;border-radius:10px;padding:10px 12px;display:flex;align-items:center;gap:10px;box-shadow:0 4px 20px rgba(14,10,6,.12);max-width:280px;cursor:pointer;animation:cm-toast-in .2s ease;margin-bottom:2px}
.cm-toast:hover{border-color:#d85020}
.cm-toast-av{width:32px;height:32px;border-radius:8px;font-size:10px;font-weight:800;color:white;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cm-toast-body{flex:1;min-width:0}
.cm-toast-name{font-size:12px;font-weight:700;color:#0e0a06}
.cm-toast-msg{font-size:11px;color:#6b5c4e;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-style:italic}
.cm-toast-time{font-size:10px;color:#a89880;flex-shrink:0}
.cm-panel{width:360px;background:white;border:1px solid #e8e2d6;border-radius:14px;overflow:hidden;box-shadow:0 8px 32px rgba(14,10,6,.15);display:none;animation:cm-panel-in .18s ease;margin-bottom:4px}
.cm-panel.show{display:block}
.cm-hd{background:#d85020;padding:13px 16px;display:flex;align-items:center;gap:8px}
.cm-hd-icon{flex-shrink:0}
.cm-hd-title{font-size:14px;font-weight:800;color:white;flex:1}
.cm-hd-count{font-size:10px;font-weight:700;background:rgba(255,255,255,.25);color:white;padding:1px 6px;border-radius:10px}
.cm-hd-back{background:rgba(255,255,255,.15);border:none;border-radius:6px;width:28px;height:28px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cm-hd-back:hover{background:rgba(255,255,255,.28)}
.cm-hd-close{background:rgba(255,255,255,.15);border:none;border-radius:6px;width:28px;height:28px;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cm-hd-close:hover{background:rgba(255,255,255,.28)}
.cm-hd-av{width:30px;height:30px;border-radius:8px;font-size:10px;font-weight:800;color:white;display:flex;align-items:center;justify-content:center;flex-shrink:0;background:rgba(255,255,255,.2)}
.cm-hd-info{flex:1}
.cm-hd-name{font-size:13px;font-weight:700;color:white}
.cm-hd-status{font-size:10px;color:rgba(255,255,255,.8);display:flex;align-items:center;gap:4px}
.cm-online-dot{width:5px;height:5px;border-radius:50%;background:#22c55e}
.cm-tabs{display:flex;border-bottom:1px solid #f0ebe0}
.cm-tab{flex:1;font-size:12px;font-weight:700;color:#a89880;background:none;border:none;border-bottom:2px solid transparent;padding:10px 0;cursor:pointer;font-family:'Outfit',sans-serif;margin-bottom:-1px;transition:color .15s}
.cm-tab:hover{color:#0e0a06}
.cm-tab.on{color:#d85020;border-bottom-color:#d85020}
.cm-threads{max-height:260px;overflow-y:auto}
.cm-thread{display:flex;align-items:center;gap:12px;padding:13px 16px;cursor:pointer;border-bottom:1px solid #f8f5f0;transition:background .12s}
.cm-thread:hover{background:#fdf4f0}
.cm-thread-av{width:40px;height:40px;border-radius:10px;font-size:12px;font-weight:800;color:white;display:flex;align-items:center;justify-content:center;flex-shrink:0;position:relative}
.cm-thread-dot{position:absolute;bottom:-1px;right:-1px;width:9px;height:9px;border-radius:50%;border:1.5px solid white}
.cm-thread-body{flex:1;min-width:0}
.cm-thread-name{font-size:13px;font-weight:700;color:#0e0a06;margin-bottom:3px}
.cm-thread-prev{font-size:12px;color:#a89880;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;font-style:italic}
.cm-thread-right{text-align:right;flex-shrink:0}
.cm-thread-time{font-size:10px;color:#a89880}
.cm-thread-unread{font-size:9px;font-weight:800;background:#d85020;color:white;padding:1px 5px;border-radius:10px;margin-top:3px;display:inline-block}
.cm-msgs{padding:14px 16px;max-height:210px;overflow-y:auto;display:flex;flex-direction:column;gap:8px;background:#faf8f4}
.cm-msg{max-width:82%}
.cm-msg.them{align-self:flex-start}
.cm-msg.me{align-self:flex-end}
.cm-bubble{padding:10px 13px;border-radius:10px;font-size:13px;line-height:1.6;font-style:italic}
.cm-msg.them .cm-bubble{background:white;color:#0e0a06;border:1px solid #e8e2d6;border-radius:10px 10px 10px 2px}
.cm-msg.me .cm-bubble{background:#d85020;color:white;border-radius:10px 10px 2px 10px;font-style:normal}
.cm-msg-time{font-size:10px;color:#a89880;margin-top:3px;padding:0 2px;font-style:normal}
.cm-msg.me .cm-msg-time{text-align:right}
.cm-typing{display:flex;align-items:center;gap:6px;padding:6px 14px;font-size:11px;color:#a89880;font-style:italic;background:#faf8f4}
.cm-typing-dots{display:flex;gap:3px;align-items:center}
.cm-typing-dot{width:5px;height:5px;border-radius:50%;background:#c8bfb2;animation:cm-pulse 1.2s infinite}
.cm-typing-dot:nth-child(2){animation-delay:.2s}
.cm-typing-dot:nth-child(3){animation-delay:.4s}
.cm-compose{display:flex;align-items:center;gap:8px;padding:11px 14px;border-top:1px solid #f0ebe0;background:white}
.cm-compose-in{flex:1;border:1.5px solid #e8e2d6;border-radius:8px;padding:9px 12px;font-size:13px;font-family:'Outfit',sans-serif;color:#0e0a06;background:#faf8f4;outline:none;transition:border-color .2s}
.cm-compose-in:focus{border-color:#d85020;background:white}
.cm-attach{width:28px;height:28px;border-radius:6px;border:1.5px solid #e8e2d6;background:none;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0}
.cm-send{width:30px;height:30px;border-radius:7px;background:#d85020;border:none;cursor:pointer;display:flex;align-items:center;justify-content:center;flex-shrink:0;transition:background .15s}
.cm-send:hover{background:#c04418}
.cm-footer{padding:8px 14px;border-top:1px solid #f0ebe0;text-align:center;background:white}
.cm-footer a{font-size:11px;font-weight:700;color:#d85020;text-decoration:none}
.cm-footer a:hover{text-decoration:underline}
.cm-empty{padding:28px 20px;text-align:center;color:#a89880;font-size:12px;font-style:italic}
`;

var THREADS = [
  {id:'hs', name:'Holy Spirit, Accra', av:'HS', color:'#2a8a4a', online:true, time:'2m', unread:2,
   preview:'We agree with your survey approach…',
   messages:[
    {from:'them',text:'We suggest a shared form with anonymised parish IDs — this worked well for our diocesan survey.',time:'2 days ago'},
    {from:'me',text:'Great idea — should we share it in Resources too?',time:'1 day ago'},
    {from:'them',text:'Yes! I\'ll upload our template now.',time:'1 day ago'},
    {from:'them',text:'We agree with your survey approach for the methodology section.',time:'2 min ago'}
   ]},
  {id:'sb', name:'St. Benedek, Budapest', av:'SB', color:'#534AB7', online:true, time:'1h', unread:1,
   preview:'Uploaded the survey template…',
   messages:[
    {from:'them',text:'Uploaded Survey Template v1.xlsx to the Resources tab.',time:'2 hours ago'},
    {from:'me',text:'Perfect, thank you!',time:'1 hour ago'}
   ]},
  {id:'ss', name:'St. Stanislaw, Warsaw', av:'SS', color:'#185FA5', online:false, time:'3h', unread:0,
   preview:'Can we include cloud provider data?',
   messages:[
    {from:'them',text:'Can we include a question about which cloud providers parishes currently use?',time:'3 hours ago'}
   ]},
  {id:'sj', name:'San José, Manila', av:'SJ', color:'#BA7517', online:false, time:'1d', unread:0,
   preview:'Just joined the project!',
   messages:[
    {from:'them',text:'Just joined the Digital Sovereignty project. Looking forward to collaborating!',time:'Yesterday'}
   ]}
];

var PROJECT_THREADS = [
  {id:'proj1', name:'Digital Sovereignty Study', av:'DS', color:'#185FA5', online:false, time:'12m', unread:3,
   preview:'Survey methodology discussion…'},
  {id:'proj2', name:'Ethical AI Statement', av:'AI', color:'#D85A30', online:false, time:'1h', unread:0,
   preview:'247 parishes have now signed'},
  {id:'proj3', name:'Global Youth Formation', av:'YF', color:'#3B6D11', online:false, time:'2d', unread:0,
   preview:'New curriculum section uploaded'}
];

var state = { open:false, view:'inbox', activeTab:'direct', activeThread:null };

function inject() {
  var style = document.createElement('style');
  style.textContent = CSS;
  document.head.appendChild(style);

  var root = document.createElement('div');
  root.id = 'cm-chat-root';
  root.innerHTML = buildRoot();
  document.body.appendChild(root);
  wire();

  // Show context strip if on workspace page
  if(window.location.pathname.includes('project-workspace')) {
    document.getElementById('cm-ctx').classList.add('show');
  }

  // Simulate incoming toast after 5 seconds — just notifies, click to open
  setTimeout(function(){
    if(!state.open) showToast(THREADS[0]);
  }, 5000);
}

function buildRoot() {
  return '<div id="cm-ctx" class="cm-context-strip" onclick="cmOpen()">' +
    '<div class="cm-context-dot"></div><span>3 online in your project</span></div>' +
    '<div id="cm-toasts"></div>' +
    '<div id="cm-panel" class="cm-panel">' + buildPanel() + '</div>' +
    '<button class="cm-btn" id="cm-toggle" onclick="cmToggle()" aria-label="Messages">' +
    '<svg width="20" height="20" viewBox="0 0 16 16" fill="none"><path d="M2 3h12a1 1 0 011 1v7a1 1 0 01-1 1H4l-3 2V4a1 1 0 011-1z" stroke="white" stroke-width="1.4" stroke-linejoin="round"/></svg>' +
    '<div class="cm-badge show" id="cm-badge">3</div></button>';
}

function buildPanel() {
  if(state.view === 'inbox') return buildInbox();
  if(state.view === 'conv') return buildConv();
  return buildInbox();
}

function buildInbox() {
  var tabs = ['direct','projects','network'];
  var labels = ['Direct','Projects','Network'];
  var tabsHtml = tabs.map(function(t,i){
    return '<button class="cm-tab'+(state.activeTab===t?' on':'')+'" onclick="cmTab(\''+t+'\')">' + labels[i] + '</button>';
  }).join('');

  var threads = state.activeTab === 'projects' ? PROJECT_THREADS : THREADS;
  var threadsHtml = threads.length ? threads.map(function(t){
    return '<div class="cm-thread" onclick="cmOpenThread(\''+t.id+'\',\''+state.activeTab+'\')">'+
      '<div class="cm-thread-av" style="background:'+t.color+'">'+t.av+
      (t.online ? '<div class="cm-thread-dot" style="background:#22c55e"></div>' : '')+
      '</div><div class="cm-thread-body">'+
      '<div class="cm-thread-name">'+t.name+'</div>'+
      '<div class="cm-thread-prev">'+t.preview+'</div></div>'+
      '<div class="cm-thread-right"><div class="cm-thread-time">'+t.time+'</div>'+
      (t.unread ? '<div class="cm-thread-unread">'+t.unread+'</div>' : '')+
      '</div></div>';
  }).join('') : '<div class="cm-empty">No messages yet</div>';

  var pagePath = window.location.pathname;
  var msgPath = pagePath.includes('/dashboard/') ? 'messages.html' : 'dashboard/messages.html';

  return '<div class="cm-hd">'+
    '<svg class="cm-hd-icon" width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2 3h12a1 1 0 011 1v7a1 1 0 01-1 1H4l-3 2V4a1 1 0 011-1z" stroke="white" stroke-width="1.4" stroke-linejoin="round"/></svg>'+
    '<span class="cm-hd-title">Messages</span>'+
    '<span class="cm-hd-count" id="cm-total-badge">3 unread</span>'+
    '<button class="cm-hd-close" onclick="cmClose()">'+
    '<svg width="11" height="11" viewBox="0 0 16 16" fill="none"><path d="M3 3l10 10M13 3L3 13" stroke="white" stroke-width="1.6" stroke-linecap="round"/></svg></button></div>'+
    '<div class="cm-tabs">'+tabsHtml+'</div>'+
    '<div class="cm-threads">'+threadsHtml+'</div>'+
    '<div class="cm-footer"><a href="'+msgPath+'">Open full messages →</a></div>';
}

function buildConv() {
  var allThreads = THREADS.concat(PROJECT_THREADS);
  var t = allThreads.find(function(x){ return x.id === state.activeThread; });
  if(!t) return buildInbox();

  var msgsHtml = (t.messages||[]).map(function(m){
    return '<div class="cm-msg '+m.from+'"><div class="cm-bubble">'+m.text+'</div>'+
      '<div class="cm-msg-time">'+m.time+'</div></div>';
  }).join('');

  return '<div class="cm-hd">'+
    '<button class="cm-hd-back" onclick="cmBack()">'+
    '<svg width="12" height="12" viewBox="0 0 16 16" fill="none"><path d="M10 3L5 8l5 5" stroke="white" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/></svg></button>'+
    '<div class="cm-hd-av" style="background:'+t.color+'">'+t.av+'</div>'+
    '<div class="cm-hd-info"><div class="cm-hd-name">'+t.name+'</div>'+
    '<div class="cm-hd-status">'+(t.online?'<div class="cm-online-dot"></div>Active now':'Last active '+t.time+' ago')+'</div></div>'+
    '<button class="cm-hd-close" onclick="cmClose()">'+
    '<svg width="11" height="11" viewBox="0 0 16 16" fill="none"><path d="M3 3l10 10M13 3L3 13" stroke="white" stroke-width="1.6" stroke-linecap="round"/></svg></button></div>'+
    '<div class="cm-msgs" id="cm-msgs">'+msgsHtml+'</div>'+
    (t.online ? '<div class="cm-typing"><div class="cm-typing-dots"><div class="cm-typing-dot"></div><div class="cm-typing-dot"></div><div class="cm-typing-dot"></div></div>&nbsp;'+t.av+' is typing…</div>' : '')+
    '<div class="cm-compose">'+
    '<button class="cm-attach"><svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M13.5 7.5l-6 6a4 4 0 01-5.7-5.6l6-6a2.5 2.5 0 013.5 3.5l-6 6a1 1 0 01-1.4-1.4l5-5" stroke="#a89880" stroke-width="1.3" stroke-linecap="round"/></svg></button>'+
    '<input class="cm-compose-in" id="cm-input" type="text" placeholder="Message '+t.name.split(',')[0]+'…" onkeydown="cmKey(event)">'+
    '<button class="cm-send" onclick="cmSend()"><svg width="13" height="13" viewBox="0 0 16 16" fill="none"><path d="M14 2L2 7l5 2 2 5 5-12z" fill="white"/></svg></button>'+
    '</div>';
}

function rerender() {
  document.getElementById('cm-panel').innerHTML = buildPanel();
  if(state.view === 'conv') {
    var msgs = document.getElementById('cm-msgs');
    if(msgs) msgs.scrollTop = msgs.scrollHeight;
  }
}

function wire() {
  document.addEventListener('keydown', function(e){ if(e.key==='Escape' && state.open) cmClose(); });
}

function showToast(t) {
  var container = document.getElementById('cm-toasts');
  var toast = document.createElement('div');
  toast.className = 'cm-toast';
  toast.innerHTML = '<div class="cm-toast-av" style="background:'+t.color+'">'+t.av+'</div>'+
    '<div class="cm-toast-body"><div class="cm-toast-name">'+t.name+'</div>'+
    '<div class="cm-toast-msg">'+t.preview+'</div></div>'+
    '<div class="cm-toast-time">now</div>';
  toast.onclick = function(){ container.removeChild(toast); cmOpen(); };
  container.appendChild(toast);
  setTimeout(function(){ if(toast.parentNode) container.removeChild(toast); }, 5000);
}

window.cmToggle = function(){ state.open ? cmClose() : cmOpen(); };
window.cmOpen = function(){
  state.open = true;
  document.getElementById('cm-panel').classList.add('show');
};
window.cmClose = function(){
  state.open = false;
  document.getElementById('cm-panel').classList.remove('show');
};
window.cmTab = function(tab){
  state.activeTab = tab;
  state.view = 'inbox';
  rerender();
};
window.cmBack = function(){
  state.view = 'inbox';
  rerender();
};
window.cmOpenThread = function(id, tab){
  state.activeThread = id;
  state.view = 'conv';
  if(tab) state.activeTab = tab;
  if(!state.open) cmOpen();
  rerender();
  // Clear unread on this thread
  var allThreads = THREADS.concat(PROJECT_THREADS);
  var t = allThreads.find(function(x){ return x.id===id; });
  if(t) t.unread = 0;
  updateBadge();
};
window.cmSend = function(){
  var input = document.getElementById('cm-input');
  if(!input || !input.value.trim()) return;
  var allThreads = THREADS.concat(PROJECT_THREADS);
  var t = allThreads.find(function(x){ return x.id===state.activeThread; });
  if(t) { t.messages = t.messages || []; t.messages.push({from:'me', text:input.value.trim(), time:'Just now'}); }
  input.value = '';
  rerender();
};
window.cmKey = function(e){ if(e.key==='Enter') cmSend(); };

function updateBadge() {
  var total = THREADS.reduce(function(s,t){ return s+(t.unread||0); },0) +
    PROJECT_THREADS.reduce(function(s,t){ return s+(t.unread||0); },0);
  var badge = document.getElementById('cm-badge');
  var countBadge = document.getElementById('cm-total-badge');
  if(badge) { badge.textContent=total; if(total>0) badge.classList.add('show'); else badge.classList.remove('show'); }
  if(countBadge) countBadge.textContent = total + ' unread';
}

inject();
})();
