# Post-build for the master itinerary (20 Oct): day maps inside each day, search, place card map buttons, ticks and day notes.
# Run after build.py, before site.py:  python3 post.py
# Day maps come from mapview/map_build.py in embed mode (JT_EMBED=1), which reads the built master.
import os, re, json, subprocess, html as H
ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, 'out', 'japan-hong-kong-final-itinerary.html')
env = dict(os.environ, JT_EMBED='1')
subprocess.run(['python3', os.path.join(ROOT, 'mapview', 'map_build.py'), '/home/claude/japan-trip'], check=True, cwd=ROOT, env=env, stdout=subprocess.DEVNULL)
E = json.load(open(os.path.join(ROOT, 'mapview', 'out', 'embed.json'), encoding='utf-8'))
out = open(OUT, encoding='utf-8').read()
assert 'id="jt-post"' not in out, 'post.py already ran on this file'

# ---------- map CSS, every rule scoped to the overlay
def scope(css):
    keep, o = [], []
    for line in css.strip().split('\n'):
        s = line.strip()
        if not s or s.startswith('@media print') or s.startswith('body') or s.startswith('.mtop') or s.startswith('.dchip') or s.startswith('.mwrap') or s.startswith('.jt-bar'):
            continue
        if s.startswith(':root') or s.startswith('@media (prefers'):
            o.append(s); continue
        for rule in re.findall(r'([^{}]+)\{([^{}]*)\}', s):
            sel = ','.join('.dmapov ' + x.strip() for x in rule[0].split(','))
            o.append(sel + '{' + rule[1] + '}')
    return '\n'.join(o)
mapcss = scope(E['css'])
js = E['js']
setup = js[js.index('function setup(win){'):js.index("\n document.querySelectorAll('.mwin').forEach(setup);")]

css = mapcss + r'''
.dmapb,.jt-search{appearance:none;font:600 .82rem var(--body);background:var(--paper);color:var(--ink);border:1.5px solid var(--ink);padding:.4rem .7rem;cursor:pointer;display:inline-flex;align-items:center;gap:.35rem}
.dmapb{position:absolute;top:0;right:0;margin:0;background:var(--ink)!important;color:var(--paper)!important;font-weight:700!important}
article.day header.dh{position:relative;padding-right:7.5rem}
.t .tdn{display:inline-block;margin:.3rem 0 0;font-size:.62rem;padding:.08rem .3rem;text-decoration:none}
.row.is-d .t .tdn{text-decoration:none}.dmapb:hover,.jt-search:hover{background:var(--ink);color:var(--paper)}
.dmapov,.jtsov{position:fixed;inset:0;z-index:40;background:var(--paper);overflow:auto;-webkit-overflow-scrolling:touch}
.dmapov[hidden],.jtsov[hidden]{display:none}
.dmtop,.jtstop{position:sticky;top:0;z-index:2;background:var(--paper);border-bottom:1.5px solid var(--ink);padding:calc(.6rem + env(safe-area-inset-top,0px)) 16px .6rem;display:flex;justify-content:space-between;align-items:center;gap:.8rem}
.dmtop b{font:800 1.1rem/1.15 var(--display)}.dmtop small{display:block;font:600 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--mute)}
.dmx{appearance:none;flex:none;font:600 .85rem var(--body);background:var(--paper);color:var(--ink);border:1.5px solid var(--ink);padding:.45rem .7rem;cursor:pointer}
.dmbody{max-width:52rem;margin:0 auto;padding:1rem 16px calc(2rem + env(safe-area-inset-bottom,0px))}
.dmapov .mstops{list-style:none;padding:0;margin:.8rem 0 0;display:grid;gap:.15rem}
.dmapov .mstops li{display:flex;gap:.6rem;align-items:baseline;padding:.4rem .3rem;border-bottom:1px solid var(--line,#ccc);cursor:pointer;font-size:.92rem}
.dmapov .mstops li.on{background:var(--water)}
.dmapov .mstops i{font-style:normal;flex:none;display:inline-grid;place-items:center;width:1.6rem;height:1.6rem;border-radius:50%;border:2px solid var(--ink);font:700 .76rem/1 var(--body)}
.dmapov .mstops li.dn i{background:var(--ink);color:var(--paper)}
.dmapov .mstops li.dn span::after{content:"  \2713";font-weight:700}
.jtsin{flex:1;font:500 1.05rem var(--body);padding:.6rem .7rem;border:2px solid var(--ink);background:var(--paper);color:var(--ink);border-radius:0;min-width:0}
.jtsres{max-width:52rem;margin:0 auto;padding:.4rem 16px calc(2rem + env(safe-area-inset-bottom,0px));list-style:none}
.jtsres li{border-bottom:1px solid var(--line,#ccc)}
.jtsres a,.jtsres button{display:block;width:100%;text-align:left;appearance:none;background:none;border:0;color:var(--ink);font:inherit;padding:.65rem 0;cursor:pointer;text-decoration:none}
.jtsres .k{display:block;font:600 .7rem var(--body);letter-spacing:.08em;text-transform:uppercase;color:var(--mute);margin-bottom:.15rem}
.jtsres .x{display:block;font-size:.84rem;color:var(--mute);margin-top:.15rem}
.jtsres b{font-weight:700}.jtsres mark{background:var(--ink);color:var(--paper);padding:0 .1em}
.jtsres .gm a{font-weight:600;text-decoration:underline}
.jtsnote{max-width:52rem;margin:0 auto;padding:.6rem 16px 0;font-size:.8rem;color:var(--mute)}
.tk{display:inline-flex;gap:.3rem;margin:.35rem 0 0}
.tk button{appearance:none;width:2rem;height:1.8rem;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .9rem/1 var(--body);cursor:pointer;padding:0}
.tk button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.tk .tkn{width:auto;padding:0 .5rem;font:600 .74rem var(--body)}
.tk .tkn.has{background:var(--ink);color:var(--paper)}
.row.added{border:1.5px dashed var(--ink);padding-left:.5rem;padding-right:.5rem;margin:.3rem 0}
.tag-add{border:1.5px dashed var(--ink);background:var(--paper);color:var(--ink)}
.row.moved{background:var(--line);transition:background .9s}
.tk .tkmv{touch-action:none;cursor:grab;font-size:1.05rem}.tk .tkbin{display:inline-flex;align-items:center;justify-content:center}.tk .tkbin.sure{width:auto;padding:0 .5rem;font:600 .74rem var(--body);background:var(--ink);color:var(--paper)}
.row.dragging{background:var(--paper);box-shadow:0 0 0 2px var(--ink),0 6px 18px rgba(0,0,0,.18);position:relative;z-index:3}.row.dragging .tkmv{cursor:grabbing;background:var(--ink);color:var(--paper)}
.qarst{appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .85rem var(--body);padding:.5rem .8rem;cursor:pointer;margin-left:.5rem}.qarst[hidden]{display:none}
.qadd{margin:.8rem 0 0}.qahint{font-size:.78rem;color:var(--mute);margin:0 0 .45rem}
.qab,.qabtn button{appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .85rem var(--body);padding:.5rem .8rem;cursor:pointer}
.qabtn button[type=submit]{background:var(--ink);color:var(--paper)}
.qaf{border:1.5px solid var(--ink);padding:.7rem}.qaf[hidden],.qab[hidden]{display:none}
.qaf label{display:block;font:700 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;margin:0 0 .6rem}
.qar{display:flex;gap:.6rem}.qar label{flex:0 0 auto}.qar .qaa{flex:1 1 auto}
.qaf input,.qaf textarea{display:block;width:100%;box-sizing:border-box;margin-top:.3rem;font:400 1rem/1.4 var(--body);color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);padding:.45rem .5rem;border-radius:0;text-transform:none;letter-spacing:0}
.qabtn{display:flex;gap:.5rem}
.inote textarea,.dnotes textarea,.qaf input,.qaf textarea{outline:none!important;box-shadow:none}.inote textarea{border-width:2.5px!important}.dnotes textarea:focus,.qaf input:focus,.qaf textarea:focus{border-width:2.5px!important;border-color:var(--ink)!important}
.inote{margin:.6rem 0 .75rem}.inote[hidden]{display:none}
.tv{display:inline-block;cursor:text;border:1.5px dashed var(--ink);outline:none;padding:.1rem .3rem;min-width:3.2rem;text-align:center;font-variant-numeric:tabular-nums}.tv:focus{background:var(--ink);color:var(--paper);border-style:solid}.tv.ed{border-style:solid;border-width:2px}@media (min-width:640px){.row .tk,.row .inote{grid-column:2/-1;justify-self:stretch}.row .tk{justify-self:start}.row.added{padding-left:.6rem;padding-right:.6rem}}@media print{.tk,.inote,.qadd,.dnotes,.tv{border:0!important}.tk,.inote,.qadd,.dnotes{display:none!important}}.tk button{flex:0 0 auto}
.inote textarea{width:100%;min-height:8.5rem;box-sizing:border-box;font:400 1rem/1.45 var(--body);color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);padding:.4rem .5rem;border-radius:0;resize:vertical}
.row.tk-n .p,.row.tk-n .n{opacity:.45;text-decoration:line-through;text-decoration-thickness:1px}
.dnotes{margin:1rem 0 .4rem;border:1.5px solid var(--ink);padding:.7rem}
.dnotes label{display:block;font:700 .72rem var(--body);letter-spacing:.08em;text-transform:uppercase;margin-bottom:.4rem}
.dnotes textarea{width:100%;min-height:5.5rem;font:400 .95rem/1.45 var(--body);color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);padding:.5rem;border-radius:0;resize:vertical;box-sizing:border-box}
.dnotes .dnb{display:flex;flex-wrap:wrap;gap:.4rem;margin-top:.5rem;align-items:center}
.dnotes .dnb button{appearance:none;font:600 .82rem var(--body);background:var(--ink);color:var(--paper);border:1.5px solid var(--ink);padding:.45rem .7rem;cursor:pointer}
.dnotes .dnb button+button{background:var(--paper);color:var(--ink)}
.dnotes .dns{font-size:.78rem;color:var(--mute)}
.row.jtflash{animation:hflash 1.8s ease-out}
@media print{.dmapb,.tk,.dnotes,.jt-search{display:none!important}}
'''

tpl = ''.join(f'<template id="dm-{d}">{v}</template>' for d, v in E['days'].items() if v)
ov = ('<div class="dmapov" id="dmapov" hidden role="dialog" aria-modal="true" aria-label="Day map"><div class="dmtop"><div><small id="dm-k"></small><b id="dm-t"></b></div>'
      '<button type="button" class="dmx" id="dm-x">Close</button></div><div class="dmbody" id="dm-b"></div></div>'
      '<div class="jtsov" id="jtsov" hidden role="dialog" aria-modal="true" aria-label="Search"><div class="jtstop"><input class="jtsin" id="jts-i" type="search" placeholder="Search places, food, days, how-tos" autocomplete="off" enterkeyhint="search">'
      '<button type="button" class="dmx" id="jts-x">Close</button></div><p class="jtsnote" id="jts-n">Searches every place card, every day of the plan and the how-tos. Works offline.</p><ul class="jtsres" id="jts-r"></ul></div>')

script = r'''
(function(){
 var G=__GEO__;window.__JTG=G;
 function esc(s){return String(s==null?'':s).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function store(k,v){try{if(v===undefined)return JSON.parse(localStorage.getItem(k)||'null');localStorage.setItem(k,JSON.stringify(v))}catch(e){return null}}
 // ---------- day maps
 var ov=document.getElementById('dmapov'),body=document.getElementById('dm-b'),cur=null,lastY=0;
 function select(n){if(!cur)return;
  cur.querySelectorAll('.pin').forEach(function(g){g.classList.toggle('on',+g.dataset.n===n)});
  cur.querySelectorAll('.leg').forEach(function(l){l.classList.toggle('on',+l.dataset.to===n)});
  cur.querySelectorAll('.mstops li').forEach(function(li,i){li.classList.toggle('on',i+1===n)});
  var li=cur.querySelectorAll('.mstops li')[n-1];if(li)li.scrollIntoView({block:'nearest',behavior:'smooth'});
 }
 __SETUP__
 function openMap(d){var t=document.getElementById('dm-'+d);if(!t)return;var a=document.getElementById('d'+d);
  document.getElementById('dm-t').textContent=a?a.querySelector('h3').textContent:'';
  document.getElementById('dm-k').textContent=a?(a.querySelector('.dow').firstChild.textContent+' '+d+' October'):'';
  body.innerHTML='';body.appendChild(t.content.cloneNode(true));cur=body;lastY=window.scrollY;ov.hidden=false;document.documentElement.style.overflow='hidden';
  body.querySelectorAll('.mwin').forEach(setup);
  body.querySelectorAll('.mstops li').forEach(function(li,i){li.onclick=function(){select(i+1);var g=body.querySelector('.pin[data-n="'+(i+1)+'"]');if(g){var w=g.closest('.mwin');w.focusOn(+g.dataset.x,+g.dataset.y)}}});
 }
 function closeMap(){ov.hidden=true;body.innerHTML='';cur=null;document.documentElement.style.overflow=''}
 document.getElementById('dm-x').onclick=closeMap;
 window.addEventListener('resize',function(){if(cur)cur.querySelectorAll('.mwin').forEach(function(w){w.redraw&&w.redraw()})});
 document.querySelectorAll('article.day').forEach(function(a){var d=a.id.slice(1);if(!document.getElementById('dm-'+d))return;
  var hd=a.querySelector('header.dh');if(!hd)return;var b=document.createElement('button');b.type='button';b.className='dmapb';b.innerHTML='&#10530; Route map';b.setAttribute('aria-label','Open the route map for this day');b.onclick=function(){openMap(d)};hd.appendChild(b)});
 // ---------- ticks, notes, editable times, quick add (saved on this device)
 var TK=store('jt-ticks-v1')||{},NT=store('jt-notes-v1')||{};
 var IN=store('jt-inotes-v1')||{},TM=store('jt-times-v1')||{},AD=store('jt-adds-v1')||{},RM=store('jt-removed-v1')||{},OR=store('jt-order-v1')||{};
 var BIN='<svg viewBox="0 0 24 24" aria-hidden="true" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>';
 function olId(ol){var a=ol.closest('article.day'),L=[].slice.call(a.querySelectorAll('ol.rows'));return a.id+'|'+L.indexOf(ol)}
 function saveOrder(ol){OR[olId(ol)]=[].slice.call(ol.querySelectorAll(':scope > li.row')).map(function(li){return li.dataset.k});store('jt-order-v1',OR)}
 function applyOrder(ol){var o=OR[olId(ol)];if(!o)return false;var L=[].slice.call(ol.querySelectorAll(':scope > li.row')),pos={};o.forEach(function(k,i){pos[k]=i});L.map(function(li,i){return {li:li,p:(li.dataset.k in pos)?pos[li.dataset.k]:o.length+i}}).sort(function(a,b){return a.p-b.p}).forEach(function(x){ol.appendChild(x.li)});return true}
 function timeWins(ol){if(OR[olId(ol)]){delete OR[olId(ol)];store('jt-order-v1',OR)}sortOl(ol,true)}
 function flash(li){li.classList.add('moved');setTimeout(function(){li.classList.remove('moved')},900)}
 function startDrag(li,h,e){e.preventDefault();var ol=li.parentNode,lastY=e.clientY;li.classList.add('dragging');
  function place(y){var sib=[].slice.call(ol.querySelectorAll(':scope > li.row:not(.dragging)')).filter(function(x){return !x.hidden}),before=null;for(var i=0;i<sib.length;i++){var r=sib[i].getBoundingClientRect();if(y<r.top+r.height/2){before=sib[i];break}}if(before){if(li.nextElementSibling!==before)ol.insertBefore(li,before)}else if(ol.lastElementChild!==li)ol.appendChild(li)}
  function move(ev){lastY=ev.clientY;place(lastY)}
  var tmr=setInterval(function(){if(lastY<80)scrollBy(0,-14);else if(lastY>innerHeight-80)scrollBy(0,14);else return;place(lastY)},30);
  function up(){clearInterval(tmr);window.removeEventListener('pointermove',move);window.removeEventListener('pointerup',up);window.removeEventListener('pointercancel',up);li.classList.remove('dragging');saveOrder(ol);flash(li)}
  window.addEventListener('pointermove',move,{passive:true});window.addEventListener('pointerup',up);window.addEventListener('pointercancel',up)}
 function rowKey(d,li){var t=(li.querySelector('.t')||{}).textContent||'',p=ptext(li).slice(0,40);return d+'|'+t+'|'+p}
 function paint(li,v){li.classList.toggle('tk-y',v==='y');li.classList.toggle('tk-n',v==='n');li.querySelectorAll('.tk button[data-v]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.v===v?'true':'false')})}
 function esc(x){return String(x).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function mins(t){var m=/^(\d{1,2})[:.](\d{2})/.exec(t||'');if(!m)return NaN;var h=+m[1];if(h<4)h+=24;return h*60+ +m[2]}
 function sortOl(ol,force){var L=[].slice.call(ol.querySelectorAll(':scope > li.row'));if(!force&&!L.some(function(li){return li.classList.contains('added')||li.querySelector('.tv.ed')}))return;var last=-1;
  var K=L.map(function(li,i){var tv=li.querySelector('.tv'),m=mins(tv?tv.textContent.trim():'');if(isNaN(m))m=last;last=m;return {li:li,m:m,i:i}});
  K.sort(function(a,b){return a.m-b.m||a.i-b.i});K.forEach(function(o){ol.appendChild(o.li)})}
 function setupRow(d,li,k,ad){var w=li.querySelector('.w');if(!w)return;li.dataset.k=k;if(!ad&&RM[k]){li.hidden=true;li.classList.add('rmv')}
  var te=li.querySelector('.t'),tn=te&&te.firstChild;
  if(tn&&tn.nodeType===3){var t0=tn.textContent.trim(),tv=document.createElement('span');tv.className='tv';tv.contentEditable='true';tv.spellcheck=false;tv.setAttribute('inputmode','numeric');tv.setAttribute('aria-label','Time, tap to change');li.dataset.t0=ad?'':t0;tv.textContent=ad?ad.t:(TM[k]||t0);te.replaceChild(tv,tn);if(!ad&&TM[k])tv.classList.add('ed');
   tv.onfocus=function(){setTimeout(function(){var r=document.createRange();r.selectNodeContents(tv);var se=getSelection();se.removeAllRanges();se.addRange(r)},0)};tv.onkeydown=function(e){if(e.key==='Enter'){e.preventDefault();tv.blur()}};
   tv.onblur=function(){var v=tv.textContent.trim();
    if(ad){if(!v){tv.textContent=ad.t;return}ad.t=v;store('jt-adds-v1',AD)}
    else{if(!v||v===t0){delete TM[k];tv.textContent=t0}else TM[k]=v;tv.classList.toggle('ed',!!TM[k]);store('jt-times-v1',TM)}
    timeWins(li.parentNode);flash(li)}}
  var s=document.createElement('span');s.className='tk';s.innerHTML='<button type="button" class="tkmv" aria-label="Drag to move">&#10303;</button><button type="button" data-v="y" aria-label="Done">&#10003;</button><button type="button" data-v="n" aria-label="Skipped">&#10007;</button><button type="button" class="tkn" aria-expanded="false" aria-label="Note">&#9998; Note</button>'+'<button type="button" class="tkbin" aria-label="Remove from the itinerary">'+BIN+'</button>';w.appendChild(s);s.querySelector('.tkmv').addEventListener('pointerdown',function(e){startDrag(li,this,e)});
  var nb=s.querySelector('.tkn'),nw=document.createElement('div');nw.className='inote';nw.hidden=true;nw.innerHTML='<textarea rows="5" placeholder="Note for this one"></textarea>';w.appendChild(nw);var nta=nw.querySelector('textarea'),ntm;nta.value=IN[k]||'';
  function mark(){nb.classList.toggle('has',!!nta.value.trim())}mark();
  nb.onclick=function(e){e.stopPropagation();nw.hidden=!nw.hidden;nb.setAttribute('aria-expanded',!nw.hidden);if(!nw.hidden)nta.focus()};
  nta.oninput=function(){clearTimeout(ntm);ntm=setTimeout(function(){if(nta.value.trim())IN[k]=nta.value;else delete IN[k];store('jt-inotes-v1',IN);mark()},300)};
  var v=TK[k]==='-'?'':(TK[k]||(li.classList.contains('is-d')?'y':''));paint(li,v);
  s.onclick=function(e){var b=e.target.closest('button');if(!b)return;
   if(b.classList.contains('tkmv'))return;
   if(b.classList.contains('tkbin')){if(b.dataset.sure){if(ad){AD[d]=(AD[d]||[]).filter(function(x){return x!==ad});store('jt-adds-v1',AD);delete TK[k];delete IN[k];store('jt-ticks-v1',TK);store('jt-inotes-v1',IN);li.remove()}else{RM[k]=1;store('jt-removed-v1',RM);li.hidden=true;li.classList.add('rmv')}var ar=li.closest('article.day');ar&&ar.dispatchEvent(new Event('jtrm'))}else{b.dataset.sure='1';b.classList.add('sure');b.innerHTML='Tap again to remove';setTimeout(function(){if(b.isConnected){delete b.dataset.sure;b.classList.remove('sure');b.innerHTML=BIN}},3000)}return}
   if(!b.dataset.v)return;var cv=li.classList.contains('tk-y')?'y':li.classList.contains('tk-n')?'n':'';var nv=cv===b.dataset.v?'':b.dataset.v;TK[k]=nv||'-';paint(li,nv);store('jt-ticks-v1',TK)}}
 function addRow(d,ol,ad){var li=document.createElement('li');li.className='row added';
  li.innerHTML='<span class="t">'+esc(ad.t)+'</span><div class="w"><p class="p">'+esc(ad.a)+' <span class="tag tag-add">Added</span></p>'+(ad.n?'<p class="n">'+esc(ad.n)+'</p>':'')+'</div>';
  ol.appendChild(li);setupRow(d,li,'add|'+ad.id,ad);return li}
 document.querySelectorAll('article.day').forEach(function(a){var d=a.id.slice(1);
  a.querySelectorAll('ol.rows > li.row').forEach(function(li){setupRow(d,li,rowKey(d,li),null)});
  var ols=a.querySelectorAll('ol.rows'),last=ols[ols.length-1];if(!last)return;
  (AD[d]||[]).forEach(function(ad){addRow(d,last,ad)});
  ols.forEach(function(ol){if(!applyOrder(ol))sortOl(ol)});
  var qa=document.createElement('div');qa.className='qadd';
  qa.innerHTML='<p class="qahint">Tap a time to change it, or hold &#10303; and drag to move. The bin removes an item, &#10007; means you missed it.</p><button type="button" class="qab">+ Add an item</button><button type="button" class="qarst" hidden></button><form class="qaf" hidden><div class="qar"><label>Time<input type="time" name="t" required></label><label class="qaa">Activity<input type="text" name="a" required placeholder="What you did or will do"></label></div><label>Note<textarea name="n" rows="3" placeholder="Optional"></textarea></label><div class="qabtn"><button type="submit">Save</button><button type="button" class="qac">Cancel</button></div></form>';
  last.parentNode.insertBefore(qa,last.nextSibling);
  var qf=qa.querySelector('form'),qb=qa.querySelector('.qab'),qr=qa.querySelector('.qarst');
  function rmCount(){var n=a.querySelectorAll('li.row.rmv').length;qr.hidden=!n;qr.textContent='Restore removed ('+n+')'}rmCount();a.addEventListener('jtrm',rmCount);
  qr.onclick=function(){a.querySelectorAll('li.row.rmv').forEach(function(li){delete RM[li.dataset.k];li.hidden=false;li.classList.remove('rmv');flash(li)});store('jt-removed-v1',RM);rmCount()};
  qb.onclick=function(){qf.hidden=false;qb.hidden=true;qf.t.focus()};
  qa.querySelector('.qac').onclick=function(){qf.reset();qf.hidden=true;qb.hidden=false};
  qf.onsubmit=function(e){e.preventDefault();var ad={id:Date.now().toString(36),t:qf.t.value.trim(),a:qf.a.value.trim(),n:qf.n.value.trim()};if(!ad.t||!ad.a)return;
   (AD[d]=AD[d]||[]).push(ad);store('jt-adds-v1',AD);var li=addRow(d,last,ad);timeWins(last);qf.reset();qf.hidden=true;qb.hidden=false;li.classList.add('moved');li.scrollIntoView({block:'center',behavior:'smooth'});setTimeout(function(){li.classList.remove('moved')},900)};
  var n=document.createElement('div');n.className='dnotes';
  n.innerHTML='<label for="dn-'+d+'">Notes for the day</label><textarea id="dn-'+d+'" placeholder="What happened, what to change, what to remember"></textarea><div class="dnb"><button type="button" class="dnc">Copy for Claude</button><button type="button" class="dnchat">Copy and chat</button><button type="button" class="dnsh">Share</button><span class="dns" aria-live="polite"></span></div>';
  qa.parentNode.insertBefore(n,qa.nextSibling);
  var ta=n.querySelector('textarea'),st=n.querySelector('.dns'),tm;ta.value=NT[d]||'';
  ta.oninput=function(){clearTimeout(tm);tm=setTimeout(function(){NT[d]=ta.value;store('jt-notes-v1',NT);st.textContent='Saved on this device'},400)};
  function text(){var L=[a.querySelector('.dow').firstChild.textContent+' '+d+' Oct: '+a.querySelector('h3').textContent];
   a.querySelectorAll('ol.rows > li.row').forEach(function(li){var x=li.classList.contains('tk-y')?'[done]':li.classList.contains('tk-n')?'[skipped]':'[ ]';var tv=li.querySelector('.tv'),tt=tv?tv.textContent.trim():((li.querySelector('.t')||{}).textContent||''),t0=li.dataset.t0;
    if(li.classList.contains('rmv'))x='[removed]';L.push((li.classList.contains('added')?'[added] ':'')+x+' '+tt+(t0&&tt!==t0?' (was '+t0+')':'')+' '+ptext(li));
    if(li.classList.contains('added')){var dn=li.querySelector('.n');if(dn)L.push('    detail: '+dn.textContent.trim())}
    var it=li.querySelector('.inote textarea');if(it&&it.value.trim())L.push('    note: '+it.value.trim())});
   if([].some.call(a.querySelectorAll('ol.rows'),function(o){return OR[olId(o)]}))L.splice(1,0,'(Order changed by hand: listed in the new order)');
   if(ta.value.trim())L.push('Notes: '+ta.value.trim());return L.join('\n')}
  n.querySelector('.dnc').onclick=function(){var t=text();(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){st.textContent='Copied. Paste it into the itinerary chat.'},function(){ta.value=ta.value;window.prompt('Copy this for Claude',t)})};
  n.querySelector('.dnchat').onclick=function(){var t=text(),u='https://claude.ai/code/session_01CKsUni8riBnC7mPCEPMiGS';if(navigator.clipboard)navigator.clipboard.writeText(t).then(function(){st.textContent='Copied. Paste it into the chat.'},function(){});var w=window.open(u,'_blank');if(!w)location.href=u};
  var shb=n.querySelector('.dnsh');if(!navigator.share)shb.hidden=true;shb.onclick=function(){navigator.share({text:text()}).catch(function(){})};
 });
 // ---------- search
 var sov=document.getElementById('jtsov'),inp=document.getElementById('jts-i'),res=document.getElementById('jts-r'),note=document.getElementById('jts-n'),IDX=null;
 function ptext(li){var p=li.querySelector('.p');if(!p)return '';var c=p.cloneNode(true);c.querySelectorAll('.tag').forEach(function(t){t.remove()});return c.textContent.trim()}
 function norm(s){return String(s||'').toLowerCase().normalize('NFD').replace(/[̀-ͯ]/g,'')}
 function build(){IDX=[];var P=window.__JTP||{};
  Object.keys(P).forEach(function(k){var d=P[k];IDX.push({ty:'p',k:k,h:d.n,s:d.w,f:norm([d.n,d.l,d.w,d.t].join(' '))})});
  document.querySelectorAll('article.day').forEach(function(a){var lab=a.querySelector('.dow').firstChild.textContent.slice(0,3)+' '+a.id.slice(1);
   a.querySelectorAll('ol.rows > li.row').forEach(function(li){var t=(li.querySelector('.t')||{}).textContent||'',p=ptext(li),n=((li.querySelector('.n')||{}).textContent||'').trim();IDX.push({ty:'r',el:li,h:p,k:lab+' · '+t,s:n,f:norm(p+' '+n+' '+lab)})})});
  document.querySelectorAll('[id^="h"] > h4').forEach(function(h){var s=h.parentNode;if(!/^h\d+$/.test(s.id))return;IDX.push({ty:'h',id:s.id,h:h.textContent,s:'',f:norm(s.textContent)})});
 }
 function hl(t,q){var i=norm(t).indexOf(q);if(i<0||!q)return esc(t);return esc(t.slice(0,i))+'<mark>'+esc(t.slice(i,i+q.length))+'</mark>'+esc(t.slice(i+q.length))}
 function run(){var q=norm(inp.value.trim());res.innerHTML='';if(!q){note.hidden=false;return}note.hidden=true;if(!IDX)build();
  var ws=q.split(/\s+/),hits=IDX.filter(function(x){return ws.every(function(w){return x.f.indexOf(w)>=0})});
  hits.sort(function(a,b){var o={p:0,r:1,h:2};var at=norm(a.h).indexOf(ws[0])>=0?0:1,bt=norm(b.h).indexOf(ws[0])>=0?0:1;return at-bt||o[a.ty]-o[b.ty]});
  var h=hits.slice(0,60).map(function(x,i){
   if(x.ty==='p')return '<li><a class="pl" href="#" role="button" data-p="'+esc(x.k)+'"><span class="k">Place</span><b>'+hl(x.h,ws[0])+'</b><span class="x">'+esc((x.s||'').slice(0,110))+'</span></a></li>';
   if(x.ty==='r')return '<li><button type="button" data-i="'+IDX.indexOf(x)+'"><span class="k">'+esc(x.k)+'</span><b>'+hl(x.h,ws[0])+'</b>'+(x.s?'<span class="x">'+esc(x.s.slice(0,110))+'</span>':'')+'</button></li>';
   return '<li><a href="#'+x.id+'" class="jtsh"><span class="k">How-to</span><b>'+hl(x.h,ws[0])+'</b></a></li>'}).join('');
  h+='<li class="gm"><a href="https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(inp.value.trim())+'" target="_blank" rel="noopener"><span class="k">Not here?</span>Search Google Maps for &ldquo;'+esc(inp.value.trim())+'&rdquo;</a></li>';
  if(!hits.length)h='<li><span class="x">Nothing in the itinerary matches.</span></li>'+h;res.innerHTML=h}
 var tq;inp.addEventListener('input',function(){clearTimeout(tq);tq=setTimeout(run,120)});
 function openS(){sov.hidden=false;document.documentElement.style.overflow='hidden';setTimeout(function(){inp.focus()},30)}
 function closeS(){sov.hidden=true;document.documentElement.style.overflow=''}
 document.getElementById('jts-x').onclick=closeS;
 res.addEventListener('click',function(e){var b=e.target.closest('button[data-i]');if(b){var x=IDX[+b.dataset.i];closeS();x.el.scrollIntoView({block:'center'});x.el.classList.remove('jtflash');void x.el.offsetWidth;x.el.classList.add('jtflash');return}
  if(e.target.closest('.jtsh'))closeS();if(e.target.closest('.pl'))setTimeout(closeS,0)});
 var bar=document.querySelector('.jt-bar');if(bar){var sb=document.createElement('button');sb.type='button';sb.className='jt-search';sb.innerHTML='&#9906; Search';sb.onclick=openS;bar.insertBefore(sb,bar.firstChild)}
 document.addEventListener('keydown',function(e){if(e.key==='Escape'){if(!sov.hidden)closeS();if(!ov.hidden)closeMap()}});
})();
'''.replace('__GEO__', json.dumps(E['geo'], separators=(',', ':'))).replace('__SETUP__', setup)

# place card: Photos, Google Maps, Apple Maps
a = '<a class="pri" id="sh-p" target="_blank" rel="noopener">See photos</a><a id="sh-m" target="_blank" rel="noopener">Open in Maps</a>'
assert a in out
out = out.replace(a, '<a class="pri" id="sh-p" target="_blank" rel="noopener">Photos</a><a id="sh-m" target="_blank" rel="noopener">Google Maps</a><a id="sh-a" target="_blank" rel="noopener">Apple Maps</a>', 1)
b = "document.getElementById('sh-m').href='https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(d.m);"
assert b in out
out = out.replace(b, b + "var gg=(window.__JTG||{})[b.dataset.p];document.getElementById('sh-a').href='https://maps.apple.com/?q='+encodeURIComponent(d.l||d.n)+(gg?'&sll='+gg[0]+','+gg[1]+'&z=17':'');", 1)
c = 'function shut(){sheet.hidden=true;'
assert c in out
out = out.replace(c, 'window.__JTP=P;' + c, 1)

out = out.replace('</style>', css + '</style>', 1)
i = out.rindex('</body>')
out = out[:i] + tpl + ov + '<script id="jt-post">' + script + '</script>\n' + out[i:]
def _mv(m):
    li = m.group(0)
    tg = '<span class="tag tag-d">Done</span>'
    if tg not in li: return li
    li = li.replace(' ' + tg, '').replace(tg, '')
    return re.sub(r'(<span class="t">[^<]*)(</span>)', lambda x: x.group(1) + x.group(2).replace('</span>', '') + '<br><span class="tag tag-d tdn">Done</span></span>', li, count=1)
out = re.sub(r'<li class="row[^"]*">.*?</li>', _mv, out, flags=re.S)
open(OUT, 'w', encoding='utf-8').write(out)
print('post: day maps', len([v for v in E['days'].values() if v]), 'size', len(out))
