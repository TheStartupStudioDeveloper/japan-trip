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
.inote{margin-top:.35rem}.inote[hidden]{display:none}
.inote textarea{width:100%;box-sizing:border-box;font:400 .9rem/1.4 var(--body);color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);padding:.4rem .5rem;border-radius:0;resize:vertical}
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
 // ---------- ticks and day notes (saved on this device)
 var TK=store('jt-ticks-v1')||{},NT=store('jt-notes-v1')||{};
 var IN=store('jt-inotes-v1')||{};
 function rowKey(d,li){var t=(li.querySelector('.t')||{}).textContent||'',p=ptext(li).slice(0,40);return d+'|'+t+'|'+p}
 function paint(li,v){li.classList.toggle('tk-y',v==='y');li.classList.toggle('tk-n',v==='n');li.querySelectorAll('.tk button').forEach(function(b){b.setAttribute('aria-pressed',b.dataset.v===v?'true':'false')})}
 document.querySelectorAll('article.day').forEach(function(a){var d=a.id.slice(1);
  a.querySelectorAll('ol.rows > li.row').forEach(function(li){var k=rowKey(d,li),w=li.querySelector('.w');if(!w)return;
   var s=document.createElement('span');s.className='tk';s.innerHTML='<button type="button" data-v="y" aria-label="Done">&#10003;</button><button type="button" data-v="n" aria-label="Skipped">&#10007;</button>';s.insertAdjacentHTML('beforeend','<button type="button" class="tkn" aria-expanded="false" aria-label="Note">&#9998; Note</button>');w.appendChild(s);var nb=s.querySelector('.tkn'),nw=document.createElement('div');nw.className='inote';nw.hidden=true;nw.innerHTML='<textarea rows="2" placeholder="Note for this one"></textarea>';w.appendChild(nw);var nta=nw.querySelector('textarea'),ntm;nta.value=IN[k]||'';function mark(){nb.classList.toggle('has',!!nta.value.trim())}mark();nb.onclick=function(e){e.stopPropagation();nw.hidden=!nw.hidden;nb.setAttribute('aria-expanded',!nw.hidden);if(!nw.hidden)nta.focus()};nta.oninput=function(){clearTimeout(ntm);ntm=setTimeout(function(){if(nta.value.trim())IN[k]=nta.value;else delete IN[k];store('jt-inotes-v1',IN);mark()},300)};
   var v=TK[k]==='-'?'':(TK[k]||(li.classList.contains('is-d')?'y':''));paint(li,v);
   s.onclick=function(e){var b=e.target.closest('button');if(!b||!b.dataset.v)return;var cv=li.classList.contains('tk-y')?'y':li.classList.contains('tk-n')?'n':'';var nv=cv===b.dataset.v?'':b.dataset.v;TK[k]=nv||'-';paint(li,nv);store('jt-ticks-v1',TK)}});
  var last=a.querySelectorAll('ol.rows');last=last[last.length-1];if(!last)return;
  var n=document.createElement('div');n.className='dnotes';
  n.innerHTML='<label for="dn-'+d+'">Notes for the day</label><textarea id="dn-'+d+'" placeholder="What happened, what to change, what to remember"></textarea><div class="dnb"><button type="button" class="dnc">Copy for Claude</button><button type="button" class="dnsh">Share</button><span class="dns" aria-live="polite"></span></div>';
  last.parentNode.insertBefore(n,last.nextSibling);
  var ta=n.querySelector('textarea'),st=n.querySelector('.dns'),tm;ta.value=NT[d]||'';
  ta.oninput=function(){clearTimeout(tm);tm=setTimeout(function(){NT[d]=ta.value;store('jt-notes-v1',NT);st.textContent='Saved on this device'},400)};
  function text(){var L=[a.querySelector('.dow').firstChild.textContent+' '+d+' Oct: '+a.querySelector('h3').textContent];
   a.querySelectorAll('ol.rows > li.row').forEach(function(li){var x=li.classList.contains('tk-y')?'[done]':li.classList.contains('tk-n')?'[skipped]':'[ ]';L.push(x+' '+((li.querySelector('.t')||{}).textContent||'')+' '+((li.querySelector('.p')||{}).textContent||'').trim());var it=li.querySelector('.inote textarea');if(it&&it.value.trim())L.push('    note: '+it.value.trim())});
   if(ta.value.trim())L.push('Notes: '+ta.value.trim());return L.join('\n')}
  n.querySelector('.dnc').onclick=function(){var t=text();(navigator.clipboard?navigator.clipboard.writeText(t):Promise.reject()).then(function(){st.textContent='Copied. Paste it into the itinerary chat.'},function(){ta.value=ta.value;window.prompt('Copy this for Claude',t)})};
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
