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
.row.added{border:0;border-top:1.5px dashed var(--ink);border-bottom:1.5px dashed var(--ink);padding-left:0;padding-right:0;margin:0}
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
#jtmode{position:fixed;right:calc(24px + env(safe-area-inset-right));bottom:calc(14px + env(safe-area-inset-bottom));z-index:15;appearance:none;-webkit-appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .85rem/1 var(--body);padding:.7rem 1rem;border-radius:999px;box-shadow:0 3px 12px rgba(0,0,0,.18);cursor:pointer}#jtmode.on{background:var(--ink);color:var(--paper)}@media print{#jtmode{display:none}}.inv{margin:.35rem 0 0;font-size:.85rem;font-style:italic;color:var(--ink);white-space:pre-wrap}.inv::before{content:'Note: ';font-style:normal;font-weight:700}body:not(.jt-clean) .inv{display:none}.jt-clean .tk,.jt-clean .inote,.jt-clean .qadd,.jt-clean .dnotes{display:none!important}.jt-clean .tv{border-color:transparent!important;padding-left:0;padding-right:0;min-width:0;text-align:left;pointer-events:none}@media (min-width:640px){.row .inv{grid-column:2/-1}}
.gob{display:flex;align-items:center;justify-content:center;width:1.9rem;height:1.9rem;margin:.45rem 0 0;appearance:none;-webkit-appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 1.05rem/1 var(--body);padding:0;cursor:pointer;white-space:nowrap;text-decoration:none}.gob[aria-expanded="true"]{background:var(--ink);color:var(--paper)}.row .t{display:flex;flex-direction:column;align-items:flex-start}.row .t .gob{margin-top:auto}.row .t .tdn{margin-bottom:.45rem}.row:has(.gobox:not([hidden])) .t .gob{margin-top:.45rem}.gobox{margin:.6rem 0 .3rem;border-left:3px solid var(--ink);padding:.15rem 0 .15rem .75rem}.gobox[hidden]{display:none}.gobox ol{margin:0;padding-left:1.1rem;display:grid;gap:.4rem;font-size:.9rem;line-height:1.4}.gobox a{font-weight:700;text-decoration:underline;margin-right:.7rem;white-space:nowrap}@media (min-width:640px){.row .gobox{grid-column:2/-1}}@media print{.gob{display:none}}
.row[hidden],li.row.rmv{display:none!important}.tkc{display:flex;flex-wrap:wrap;align-items:center;gap:.4rem .5rem;margin:.5rem 0 0;padding:.5rem .6rem;border:1.5px solid var(--ink);font:600 .85rem var(--body)}.tkc span{flex:1 1 100%}.tkc button{appearance:none;-webkit-appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .85rem var(--body);padding:.45rem .8rem;cursor:pointer}.tkc .tkyes{background:var(--ink);color:var(--paper)}.jt-clean .tkc{display:none}@media (min-width:640px){.row .tkc{grid-column:2/-1;justify-self:start}}
.row .t .gob{order:3}.jt-clean .row.tk-y:not(.is-d) .t::after,.jt-clean .row.tk-n .t::after{order:2;display:inline-flex;align-items:center;justify-content:center;width:1.45rem;height:1.45rem;margin:.4rem 0 0;font:700 .85rem/1 var(--body);border:1.5px solid var(--ink)}.jt-clean .row.tk-y:not(.is-d) .t::after{content:'\2713';background:var(--ink);color:var(--paper)}.jt-clean .row.tk-n .t::after{content:'\2717';background:var(--paper);color:var(--ink)}
.nowm{list-style:none;position:relative;height:0;margin:0;border-top:2px solid var(--ink);z-index:1}.nowm span{position:absolute;left:0;top:-.72rem;background:var(--ink);color:var(--paper);font:700 .68rem/1 var(--body);padding:.25rem .45rem;letter-spacing:.04em}@media print{.nowm{display:none}}
.sheet .acts{flex-wrap:nowrap!important;gap:.4rem!important}.sheet .acts a{flex:1 1 0!important;min-width:0;padding:.7rem .25rem!important;font-size:.84rem!important;white-space:nowrap}
.inote{margin:.6rem 0 .75rem}.inote[hidden]{display:none}
.tv{position:relative;display:inline-block;cursor:pointer;border:1.5px dashed var(--ink);padding:.1rem .3rem;min-width:3.2rem;text-align:center;font-variant-numeric:tabular-nums}.tv:focus-within{background:var(--ink);color:var(--paper);border-style:solid}.tvi{position:absolute;inset:0;width:100%;height:100%;opacity:0;border:0;margin:0;padding:0;font-size:16px;cursor:pointer;-webkit-appearance:none;appearance:none}.jt-clean .tvi{display:none!important}.tv.ed{border-style:solid;border-width:2px}@media (min-width:640px){.row .tk,.row .inote{grid-column:2/-1;justify-self:stretch}.row .tk{justify-self:start}}@media print{.tk,.inote,.qadd,.dnotes,.tv{border:0!important}.tk,.inote,.qadd,.dnotes{display:none!important}}.tk button{flex:0 0 auto}
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
 document.addEventListener('click',function(e){var g=e.target.closest('.gob');if(!g)return;e.preventDefault();var bx=document.getElementById(g.getAttribute('aria-controls'));if(!bx)return;bx.hidden=!bx.hidden;g.setAttribute('aria-expanded',bx.hidden?'false':'true')});
 // ---------- clean / edit mode (saved on this device, clean by default)
 (function(){var m;try{m=localStorage.getItem('jt-mode')}catch(e){}var ed=m==='edit';document.body.classList.toggle('jt-clean',!ed);
  var b=document.createElement('button');b.type='button';b.id='jtmode';
  function lab(){var on=!document.body.classList.contains('jt-clean');b.innerHTML=on?'&#10003; Done editing':'&#9998; Edit';b.setAttribute('aria-pressed',on?'true':'false');b.classList.toggle('on',on)}lab();
  b.onclick=function(){var rows=document.querySelectorAll('li.row,article.day header'),anc=null,top=0,cy=60;for(var i=0;i<rows.length;i++){var r=rows[i].getBoundingClientRect();if(r.top>=cy&&r.height){anc=rows[i];top=r.top;break}}var on=document.body.classList.toggle('jt-clean');if(anc){var de=document.documentElement;de.style.scrollBehavior='auto';var fix=function(){var nt=anc.getBoundingClientRect().top;if(Math.abs(nt-top)>1)window.scrollTo(0,window.pageYOffset+(nt-top))};fix();requestAnimationFrame(function(){fix();requestAnimationFrame(function(){fix();de.style.scrollBehavior=''})})}try{localStorage.setItem('jt-mode',on?'clean':'edit')}catch(e){}if(on&&document.activeElement&&document.activeElement.blur)document.activeElement.blur();lab()};
  document.body.appendChild(b)})();
 // ---------- ticks, notes, editable times, quick add (saved on this device)
 var TK=store('jt-ticks-v1')||{},NT=store('jt-notes-v1')||{};
 var IN=store('jt-inotes-v1')||{},TM=store('jt-times-v1')||{},AD=store('jt-adds-v1')||{},RM=store('jt-removed-v1')||{},OR=store('jt-order-v1')||{};
 var EA=store('jt-edit-at-v1')||{};
 function touched(d){EA[d]=Date.now();store('jt-edit-at-v1',EA)}
 (function(){var ch=false;document.querySelectorAll('article.day[data-synced]').forEach(function(a){var d=a.id.slice(1),syn=+a.dataset.synced;if((EA[d]||0)>syn)return;
   var pre=d+'|',any=false;
   [TK,IN,TM,RM].forEach(function(o){Object.keys(o).forEach(function(k){if(k.indexOf(pre)===0){delete o[k];any=true}})});
   (AD[d]||[]).forEach(function(x){delete TK['add|'+x.id];delete IN['add|'+x.id];any=true});if(AD[d]){delete AD[d];any=true}
   Object.keys(OR).forEach(function(k){if(k.indexOf('d'+d+'|')===0){delete OR[k];any=true}});
   if(NT[d]){delete NT[d];any=true}
   if(any){delete EA[d];ch=true}});
  if(ch){store('jt-ticks-v1',TK);store('jt-inotes-v1',IN);store('jt-times-v1',TM);store('jt-removed-v1',RM);store('jt-adds-v1',AD);store('jt-order-v1',OR);store('jt-notes-v1',NT);store('jt-edit-at-v1',EA)}})();
 var BIN='<svg viewBox="0 0 24 24" aria-hidden="true" width="15" height="15" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M4 7h16M10 11v6M14 11v6M6 7l1 13h10l1-13M9 7V4h6v3"/></svg>';
 function olId(ol){var a=ol.closest('article.day'),L=[].slice.call(a.querySelectorAll('ol.rows'));return a.id+'|'+L.indexOf(ol)}
 function saveOrder(ol){OR[olId(ol)]=[].slice.call(ol.querySelectorAll(':scope > li.row')).map(function(li){return li.dataset.k});store('jt-order-v1',OR);var ar=ol.closest('article.day');if(ar)touched(ar.id.slice(1))}
 function applyOrder(ol){var o=OR[olId(ol)];if(!o)return false;var L=[].slice.call(ol.querySelectorAll(':scope > li.row')),pos={};o.forEach(function(k,i){pos[k]=i});L.map(function(li,i){return {li:li,p:(li.dataset.k in pos)?pos[li.dataset.k]:o.length+i}}).sort(function(a,b){return a.p-b.p}).forEach(function(x){ol.appendChild(x.li)});return true}
 function timeWins(ol){if(OR[olId(ol)]){delete OR[olId(ol)];store('jt-order-v1',OR)}sortOl(ol,true)}
 function flash(li){li.classList.add('moved');setTimeout(function(){li.classList.remove('moved')},900)}
 function startDrag(li,h,e){e.preventDefault();var ol=li.parentNode,lastY=e.clientY;li.classList.add('dragging');
  function place(y){var sib=[].slice.call(ol.querySelectorAll(':scope > li.row:not(.dragging)')).filter(function(x){return !x.hidden}),before=null;for(var i=0;i<sib.length;i++){var r=sib[i].getBoundingClientRect();if(y<r.top+r.height/2){before=sib[i];break}}if(before){if(li.nextElementSibling!==before)ol.insertBefore(li,before)}else if(ol.lastElementChild!==li)ol.appendChild(li)}
  function move(ev){lastY=ev.clientY;place(lastY)}
  var tmr=setInterval(function(){if(lastY<80)scrollBy(0,-14);else if(lastY>innerHeight-80)scrollBy(0,14);else return;place(lastY)},30);
  function up(){clearInterval(tmr);window.removeEventListener('pointermove',move);window.removeEventListener('pointerup',up);window.removeEventListener('pointercancel',up);li.classList.remove('dragging');saveOrder(ol);flash(li)}
  window.addEventListener('pointermove',move,{passive:true});window.addEventListener('pointerup',up);window.addEventListener('pointercancel',up)}
 function rowKey(d,li){var te=li.querySelector('.t'),t='';if(te){var c=te.cloneNode(true);c.querySelectorAll('.gob').forEach(function(x){x.remove()});t=c.textContent}p=ptext(li).slice(0,40);return d+'|'+t+'|'+p}
 function paint(li,v){li.classList.toggle('tk-y',v==='y');li.classList.toggle('tk-n',v==='n');li.querySelectorAll('.tk button[data-v]').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.v===v?'true':'false')})}
 function esc(x){return String(x).replace(/[&<>"]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]})}
 function mins(t){var m=/^(\d{1,2})[:.](\d{2})/.exec(t||'');if(!m)return NaN;var h=+m[1];if(h<4)h+=24;return h*60+ +m[2]}
 function sortOl(ol,force){var L=[].slice.call(ol.querySelectorAll(':scope > li.row'));if(!force&&!L.some(function(li){return li.classList.contains('added')||li.querySelector('.tv.ed')}))return;var last=-1;
  var K=L.map(function(li,i){var tv=li.querySelector('.tv'),m=mins(tv?tv.textContent.trim():'');if(isNaN(m))m=last;last=m;return {li:li,m:m,i:i}});
  K.sort(function(a,b){return a.m-b.m||a.i-b.i});K.forEach(function(o){ol.appendChild(o.li)})}
 function setupRow(d,li,k,ad){var w=li.querySelector('.w');if(!w)return;li.dataset.k=k;if(!ad&&RM[k]){li.hidden=true;li.classList.add('rmv')}
  var te=li.querySelector('.t'),tn=te&&te.firstChild;
  if(tn&&tn.nodeType===3){var t0=tn.textContent.trim(),tv=document.createElement('span');tv.className='tv';li.dataset.t0=ad?'':t0;var cur=ad?ad.t:(TM[k]||t0);
   var tx=document.createElement('span');tx.className='tvt';tx.textContent=cur;tv.appendChild(tx);te.replaceChild(tv,tn);if(!ad&&TM[k])tv.classList.add('ed');
   var ti=document.createElement('input');ti.type='time';ti.className='tvi';ti.setAttribute('aria-label','Change the time');
   function hm(v){var m=/^(\d{1,2}):(\d{2})/.exec(v||'');return m?('0'+m[1]).slice(-2)+':'+m[2]:''}ti.value=hm(cur);tv.appendChild(ti);
   function commit(){var v=hm(ti.value);
    if(ad){if(!v||v===ad.t)return;ad.t=v;tx.textContent=v;store('jt-adds-v1',AD);touched(d)}
    else{var was=TM[k]||t0;if(!v||v===hm(t0)){delete TM[k];tx.textContent=t0;ti.value=hm(t0)}else{TM[k]=v;tx.textContent=v}if((TM[k]||t0)===was)return;tv.classList.toggle('ed',!!TM[k]);store('jt-times-v1',TM);touched(d)}
    timeWins(li.parentNode);flash(li)}
   ti.addEventListener('blur',function(){setTimeout(commit,50)});ti.addEventListener('keydown',function(e){if(e.key==='Enter'){e.preventDefault();ti.blur()}})}
  var s=document.createElement('span');s.className='tk';s.innerHTML='<button type="button" class="tkmv" aria-label="Drag to move">&#10303;</button><button type="button" data-v="y" aria-label="Done">&#10003;</button><button type="button" data-v="n" aria-label="Skipped">&#10007;</button><button type="button" class="tkn" aria-expanded="false" aria-label="Note">&#9998; Note</button>'+'<button type="button" class="tkbin" aria-label="Remove from the itinerary">'+BIN+'</button>';w.appendChild(s);s.querySelector('.tkmv').addEventListener('pointerdown',function(e){startDrag(li,this,e)});
  var nb=s.querySelector('.tkn'),nw=document.createElement('div');nw.className='inote';nw.hidden=true;nw.innerHTML='<textarea rows="5" placeholder="Note for this one"></textarea>';w.appendChild(nw);var nta=nw.querySelector('textarea'),ntm;nta.value=IN[k]||'';
  var inv=document.createElement('p');inv.className='inv';w.insertBefore(inv,s);function mark(){var t=nta.value.trim();nb.classList.toggle('has',!!t);inv.textContent=t;inv.hidden=!t}mark();
  nb.onclick=function(e){e.stopPropagation();nw.hidden=!nw.hidden;nb.setAttribute('aria-expanded',!nw.hidden);if(!nw.hidden)nta.focus()};
  nta.oninput=function(){clearTimeout(ntm);ntm=setTimeout(function(){if(nta.value.trim())IN[k]=nta.value;else delete IN[k];store('jt-inotes-v1',IN);mark();touched(d)},300)};
  var v=TK[k]==='-'?'':(TK[k]||(li.classList.contains('is-d')?'y':''));paint(li,v);
  s.onclick=function(e){var b=e.target.closest('button');if(!b)return;
   if(b.classList.contains('tkmv'))return;
   if(b.classList.contains('tkbin')){var cf=w.querySelector('.tkc');if(cf){cf.remove();return}cf=document.createElement('div');cf.className='tkc';cf.innerHTML='<span>Remove this from the day?</span><button type="button" class="tkyes">Remove</button><button type="button" class="tkno">Cancel</button>';s.insertAdjacentElement('afterend',cf);
    cf.querySelector('.tkno').onclick=function(){cf.remove()};
    cf.querySelector('.tkyes').onclick=function(){cf.remove();if(ad){AD[d]=(AD[d]||[]).filter(function(x){return x!==ad});store('jt-adds-v1',AD);touched(d);delete TK[k];delete IN[k];store('jt-ticks-v1',TK);store('jt-inotes-v1',IN);li.remove()}else{RM[k]=1;store('jt-removed-v1',RM);touched(d);li.hidden=true;li.classList.add('rmv')}var ar=document.querySelector('article.day#d'+d);ar&&ar.dispatchEvent(new Event('jtrm'))};return}
   if(!b.dataset.v)return;var cv=li.classList.contains('tk-y')?'y':li.classList.contains('tk-n')?'n':'';var nv=cv===b.dataset.v?'':b.dataset.v;TK[k]=nv||'-';paint(li,nv);store('jt-ticks-v1',TK);touched(d)}}
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
   (AD[d]=AD[d]||[]).push(ad);store('jt-adds-v1',AD);touched(d);var li=addRow(d,last,ad);timeWins(last);qf.reset();qf.hidden=true;qb.hidden=false;li.classList.add('moved');li.scrollIntoView({block:'center',behavior:'smooth'});setTimeout(function(){li.classList.remove('moved')},900)};
  var n=document.createElement('div');n.className='dnotes';
  n.innerHTML='<label for="dn-'+d+'">Notes for the day</label><textarea id="dn-'+d+'" placeholder="What happened, what to change, what to remember"></textarea><div class="dnb"><button type="button" class="dnc">Copy for Claude</button><button type="button" class="dnchat">Copy and chat</button><button type="button" class="dnsh">Share</button><span class="dns" aria-live="polite"></span></div>';
  qa.parentNode.insertBefore(n,qa.nextSibling);
  var ta=n.querySelector('textarea'),st=n.querySelector('.dns'),tm;ta.value=NT[d]||'';
  ta.oninput=function(){clearTimeout(tm);tm=setTimeout(function(){NT[d]=ta.value;store('jt-notes-v1',NT);touched(d);st.textContent='Saved on this device'},400)};
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
 // ---------- now marker and remembered position
 (function(){var now=new Date();if(now.getFullYear()!==2026||now.getMonth()!==9)return;var a=document.getElementById('d'+now.getDate());if(!a)return;
  var m=document.createElement('li');m.className='nowm';m.setAttribute('aria-label','Now');
  function hm(t){var x=/^(\d{1,2})[:.](\d{2})/.exec(t||'');if(!x)return NaN;var h=+x[1];if(h<4)h+=24;return h*60+ +x[2]}
  function place(){var n=new Date(),cur=n.getHours()*60+n.getMinutes();if(n.getHours()<4)cur+=1440;m.innerHTML='<span>Now '+String(n.getHours()).padStart(2,'0')+':'+String(n.getMinutes()).padStart(2,'0')+'</span>';
   var rows=[].slice.call(a.querySelectorAll('ol.rows > li.row')).filter(function(r){return !r.hidden}),tgt=null;
   for(var i=0;i<rows.length;i++){var tv=rows[i].querySelector('.tv'),t=hm(tv?tv.textContent:(rows[i].querySelector('.t')||{}).textContent);if(!isNaN(t)&&t>cur){tgt=rows[i];break}}
   if(tgt)tgt.parentNode.insertBefore(m,tgt);else if(rows.length)rows[rows.length-1].parentNode.appendChild(m)}
  place();setInterval(place,60000);document.addEventListener('visibilitychange',function(){if(!document.hidden)place()})})();
 (function(){var KEY='jt-pos-v1';
  function anchor(){var L=document.querySelectorAll('li.row,article.day header.dh');for(var i=0;i<L.length;i++){var e=L[i];if(e.hidden||!e.offsetParent)continue;var r=e.getBoundingClientRect();if(r.bottom>70)return {e:e,top:r.top}}return null}
  function save(){var x=anchor();if(!x)return;var k=x.e.dataset&&x.e.dataset.k?'k:'+x.e.dataset.k:'d:'+(x.e.closest('article.day')||{}).id;store(KEY,{k:k,off:Math.round(x.top),y:Math.round(scrollY),at:Date.now()})}
  var tm;window.addEventListener('scroll',function(){clearTimeout(tm);tm=setTimeout(save,300)},{passive:true});
  document.addEventListener('visibilitychange',function(){if(document.hidden)save()});window.addEventListener('pagehide',save);
  function restore(){if(location.hash)return;var p=store(KEY);if(!p||Date.now()-p.at>7*864e5)return;var el=null;
   if(p.k.indexOf('k:')===0){var want=p.k.slice(2);var L=document.querySelectorAll('li.row');for(var i=0;i<L.length;i++){if(L[i].dataset.k===want){el=L[i];break}}}
   else{var a=document.getElementById(p.k.slice(2));el=a&&a.querySelector('header.dh')}
   var de=document.documentElement,sb=de.style.scrollBehavior;de.style.scrollBehavior='auto';
   if(el&&!el.hidden)window.scrollTo(0,el.getBoundingClientRect().top+window.pageYOffset-p.off);else window.scrollTo(0,p.y);
   de.style.scrollBehavior=sb}
  restore();if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){restore()});window.addEventListener('load',function(){setTimeout(restore,50)})})();
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
out = out.replace(b, "document.getElementById('sh-m').href='https://www.google.com/maps/search/?api=1&query='+encodeURIComponent((d.l?d.l+' ':'')+d.m);" + "var gg=(window.__JTG||{})[b.dataset.p];document.getElementById('sh-a').href='https://maps.apple.com/?q='+encodeURIComponent(d.l||d.n)+(gg?'&sll='+gg[0]+','+gg[1]+'&z=17':'');", 1)
# 25 Oct: exact Google place for cards that have a place id (g)
_pg = "encodeURIComponent((d.l?d.l+' ':'')+d.m);var gg"
assert _pg in out
out = out.replace(_pg, "encodeURIComponent((d.l?d.l+' ':'')+d.m)+(d.g?'&query_place_id='+d.g:'');var gg", 1)
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

# 21 Oct: Directions button (ⓘ) under the time, with a drop-down of steps, from directions_data.py
_g = {}; exec(open('directions_data.py', encoding='utf-8').read(), _g); _GO = _g['GO']
def _steps_html(steps):
    def one(x):
        x = H.escape(x)
        x = re.sub(r'(https://www\.google\.com/maps/[^\s<]+)', r'<a href="\1" target="_blank" rel="noopener">Google Maps</a>', x)
        x = re.sub(r'(https://maps\.apple\.com/[^\s<]+)', r'<a href="\1" target="_blank" rel="noopener">Apple Maps</a>', x)
        return '<li>' + x + '</li>'
    return '<ol>' + ''.join(one(x) for x in steps) + '</ol>'
_gon = 0
def _go_article(m):
    global _gon
    day = int(m.group(1)); art = m.group(0); items = _GO.get(day)
    if not items: return art
    used = set()
    def _row(rm):
        global _gon
        li = rm.group(0)
        pm = re.search(r'<p class="p">(.*?)</p>', li, re.S)
        title = H.unescape(re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', pm.group(1)))).strip() if pm else ''
        for i, (k, steps) in enumerate(items):
            if i in used: continue
            if title.startswith(k) or k in title:
                used.add(i); _gon += 1; bid = 'go%d' % _gon
                li = li.replace('</span><div class="w">', '<button type="button" class="gob" aria-expanded="false" aria-controls="%s" aria-label="Directions" title="Directions">&#9432;</button></span><div class="w">' % bid, 1)
                li = li[:li.rfind('</div></li>')] + '<div class="gobox" id="%s" hidden>%s</div></div></li>' % (bid, _steps_html(steps))
                break
        return li
    return re.sub(r'<li class="row[^"]*">.*?</li>', _row, art, flags=re.S)
out = re.sub(r'<article class="day[^"]*" id="d(\d+)".*?</article>', _go_article, out, flags=re.S)
_sg = {}; exec(open('sync_data.py', encoding='utf-8').read(), _sg)
from datetime import datetime as _dt
for _d, _t in _sg['SYNCED'].items():
    _ms = int(_dt.fromisoformat(_t).timestamp() * 1000)
    out = re.sub(r'(<article class="day[^"]*" id="d%d")' % _d, r'\1 data-synced="%d"' % _ms, out, count=1)

print('directions:', _gon)
# 21 Oct: map URLs written into how-to steps become links
out = re.sub(r'(<section class="decide block" id="h\d+">.*?</section>)', lambda m: re.sub(r'(?<![="\'])(https://www\.google\.com/maps/[^\s<]+)', r'<a href="\1" target="_blank" rel="noopener">Google Maps</a>', m.group(1)), out, flags=re.S)
# 26 Oct: day bar fixed at the top from the start: moved above the cover, still sticky.
_m = re.search(r'<nav class="nav"[^>]*>.*?</nav>\s*', out, re.S)
if _m and out.find('<div class="wrap">') < _m.start():
    _nav = _m.group(0); out = out[:_m.start()] + out[_m.end():]
    _w = out.find('<div class="wrap">'); out = out[:_w] + _nav + out[_w:]
    out = out.replace('</style>', 'nav.nav{margin-top:0!important;top:0}@media screen{body > nav.nav{position:-webkit-sticky;position:sticky}}</style>', 1)
# 26 Oct: scroll to top button, bottom left, icon only, matches the Clean/Edit pill. Shows after scrolling down.
_tt_css = ('#jttop{position:fixed;left:calc(24px + env(safe-area-inset-left));bottom:calc(14px + env(safe-area-inset-bottom));z-index:15;'
           'appearance:none;-webkit-appearance:none;width:2.6rem;height:2.6rem;padding:0;display:flex;align-items:center;justify-content:center;'
           'border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);border-radius:999px;box-shadow:0 3px 12px rgba(0,0,0,.18);cursor:pointer;'
           'opacity:0;pointer-events:none;transition:opacity .2s}#jttop.show{opacity:1;pointer-events:auto}#jttop svg{width:1.1rem;height:1.1rem}@media print{#jttop{display:none}}')
_tt_html = ('<button type="button" id="jttop" aria-label="Back to top" title="Back to top">'
            '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M12 19V5M5 12l7-7 7 7"/></svg></button>'
            "<script>(function(){var b=document.getElementById('jttop');function f(){b.classList.toggle('show',window.scrollY>600)}"
            "addEventListener('scroll',f,{passive:true});f();b.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})})})();</script>")
if 'id="jttop"' not in out:
    out = out.replace('</style>', _tt_css + '</style>', 1)
    out = out.replace('</body>', _tt_html + '</body>', 1)
# 26 Oct: day bar jumps done in script so they land on the right day on iPhone: instant jump under the bar,
# then re-checked as maps and images load, and stopped as soon as you touch or scroll yourself.
_nj = ("<script>(function(){var nav=document.querySelector('nav.nav');if(!nav)return;"
       "function setCur(a){[].forEach.call(nav.querySelectorAll('a.cur'),function(x){if(x!==a)x.classList.remove('cur')});if(a)a.classList.add('cur')}"
       "function go(id,a){var el=document.getElementById(id);if(!el)return;var stop=false,n=0;"
       "window.__jtLock=Date.now()+1800;setCur(a);try{a.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'})}catch(x){}"
       "function off(){stop=true;window.__jtLock=0;removeEventListener('touchstart',off);removeEventListener('wheel',off)}"
       "function target(){return el.getBoundingClientRect().top+window.pageYOffset-nav.getBoundingClientRect().height-6}"
       "setTimeout(function(){addEventListener('touchstart',off,{passive:true});addEventListener('wheel',off,{passive:true})},50);"
       "window.scrollTo({top:target(),behavior:'smooth'});"
       "function fix(){if(stop)return;var y=target();if(Math.abs(window.pageYOffset-y)>3)window.scrollTo({top:y,behavior:n<1?'smooth':'auto'});"
       "if(++n<4)setTimeout(fix,500);else{window.__jtLock=0;removeEventListener('touchstart',off);removeEventListener('wheel',off)}}setTimeout(fix,900);"
       "try{history.replaceState(null,'','#'+id)}catch(e){}}"
       "nav.addEventListener('click',function(e){var a=e.target.closest('a[href^=\"#\"]');if(!a)return;e.preventDefault();e.stopImmediatePropagation();"
       "go(a.getAttribute('href').slice(1),a)},true);})();</script>")
if 'nav.addEventListener(\'click\'' not in out:
    out = out.replace('</body>', _nj + '</body>', 1)
# 26 Oct: day bar highlight follows the day on screen. Black = the day you are looking at; today keeps a thin outline when you are elsewhere.
_spy_css = ('nav.nav a.today{background:none;color:var(--ink);box-shadow:inset 0 0 0 1.5px var(--ink)}nav.nav a.today small{color:var(--mute)}'
            'nav.nav a.cur{background:var(--ink)!important;color:var(--paper)!important;box-shadow:none}nav.nav a.cur small{color:var(--paper)!important}')
_spy = ("<script>(function(){var nav=document.querySelector('nav.nav');if(!nav)return;var links=[].slice.call(nav.querySelectorAll('a[href^=\"#\"]'));"
        "var items=links.map(function(a){return {a:a,el:document.getElementById(a.getAttribute('href').slice(1))}}).filter(function(x){return x.el});"
        "var last=null,t=null;function upd(){t=null;if(window.__jtLock&&Date.now()<window.__jtLock){t=setTimeout(upd,150);return}last=nav.querySelector('a.cur');var lim=nav.getBoundingClientRect().bottom+40,cur=null;"
        "var best=-1e9;items.forEach(function(x){var tp=x.el.getBoundingClientRect().top;if(tp<=lim&&tp>best){best=tp;cur=x}});"
        "if(cur&&cur.el.getBoundingClientRect().bottom<nav.getBoundingClientRect().bottom)cur=null;"
        "var a=cur?cur.a:null;if(a===last)return;if(last)last.classList.remove('cur');if(a){a.classList.add('cur');"
        "var r=a.getBoundingClientRect();if(r.left<0||r.right>innerWidth){try{a.scrollIntoView({inline:'center',block:'nearest',behavior:'smooth'})}catch(e){}}}last=a}"
        "addEventListener('scroll',function(){if(!t)t=setTimeout(upd,80)},{passive:true});addEventListener('load',upd);upd();})();</script>")
if 'nav.nav a.cur' not in out:
    out = out.replace('</style>', _spy_css + '</style>', 1)
    out = out.replace('</body>', _spy + '</body>', 1)
open(OUT, 'w', encoding='utf-8').write(out)
print('post: day maps', len([v for v in E['days'].values() if v]), 'size', len(out))
