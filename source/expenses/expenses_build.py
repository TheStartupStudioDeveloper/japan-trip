# Builds the standalone Trip Expenses page (claude.ai artifact copy) and its GitHub web app.
# Usage: python3 expenses_build.py [repo dir]
#   reads ../expenses.json and the itinerary build (../out/japan-hong-kong-final-itinerary.html) for fonts and styles
#   writes out/trip-expenses.html (publish to claude.ai) and <repo>/expenses/ (GitHub Pages web app)
import sys, os, re, json, asyncio, hashlib, shutil
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/japan-trip'
sys.path[:0] = [os.path.join(REPO, 'source'), ROOT]
import apptools
PDF = None  # online only for now; set to 'JHK-Expenses.pdf' to bring the PDF back
OFF = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png'] + ([PDF] if PDF else [])
data = json.load(open(os.path.join(ROOT, 'expenses.json'), encoding='utf-8'))
master = open(os.path.join(ROOT, 'out', 'japan-hong-kong-final-itinerary.html'), encoding='utf-8').read()
style = re.search(r'<style>(.*?)</style>', master, re.S).group(1)
tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
i = tpl.index("(function(){\n  var el=document.getElementById('costdata')"); j = tpl.index('})();', i) + 5
js = tpl[i:j]
js = re.sub(r"\n  if\(window\.claude.*?\}\)\}\)\}\n", "\n", js, flags=re.S)
extra = ('.costs{margin-top:0}header.cover{padding:2.4rem 1.1rem 0}.exband{display:flex;height:12px;margin-bottom:1.6rem}.exband i{flex:1}'
         '.rules{margin-top:2rem;border:1.5px solid var(--ink);padding:1rem;display:grid;gap:.45rem;font-size:.92rem}'
         '.rules h4{font:700 1.1rem/1.2 var(--display)}.rules li{padding-left:1.1rem;position:relative}'
         '.rules li::before{content:"";position:absolute;left:0;top:.55em;width:.45rem;height:.45rem;background:var(--ink)}'
         '.logbox{border:1.5px solid var(--ink);padding:1rem;margin:0 0 1.4rem}.logbox h2{font:800 1.25rem/1.15 var(--display);margin:0 0 .2rem}.logbox .lsub{font-size:.85rem;color:var(--mute);margin:0 0 .8rem}.lgrid{display:grid;grid-template-columns:1fr 1fr;gap:.5rem}.lgrid .full{grid-column:1/-1}.lgrid label{display:grid;gap:.2rem;font-size:.74rem;color:var(--mute)}.lgrid input,.lgrid select{font:500 1rem/1.2 var(--body);color:var(--ink);background:var(--paper);border:1.5px solid var(--ink);border-radius:0;padding:.55rem .6rem;width:100%;box-sizing:border-box;-webkit-appearance:none;appearance:none}.lamt{display:grid;grid-template-columns:4.2rem 1fr;gap:.35rem}.seg{display:grid;grid-template-columns:repeat(3,1fr);border:1.5px solid var(--ink)}.seg button{font:600 .9rem/1 var(--body);padding:.6rem 0;border:0;border-right:1.5px solid var(--ink);background:var(--paper);color:var(--ink)}.seg button:last-child{border-right:0}.seg button[aria-pressed="true"]{background:var(--ink);color:var(--paper)}#lpay.seg{display:grid;grid-template-columns:repeat(3,1fr);gap:0;align-items:stretch;border:1.5px solid var(--ink)}#lpay.seg button{width:100%;min-height:2.6rem;cursor:pointer;display:block;margin:0;border-radius:0;box-sizing:border-box;-webkit-appearance:none;appearance:none;padding:.6rem .2rem}.lgrid input:focus,.lgrid select:focus{outline:none!important;border-width:2.5px}.lbtn{font:700 .95rem/1 var(--body);padding:.7rem 1rem;border:1.5px solid var(--ink);border-radius:0;background:var(--ink);color:var(--paper);cursor:pointer}.lbtn.alt{background:var(--paper);color:var(--ink)}.lacts{display:flex;flex-wrap:wrap;gap:.5rem;margin-top:.8rem}.llist{list-style:none;margin:1rem 0 0;padding:0;border-top:1.5px solid var(--ink)}.llist li{display:grid;grid-template-columns:1fr auto auto;gap:.6rem;align-items:center;padding:.55rem 0;border-bottom:1px solid var(--line);font-size:.92rem}.llist small{display:block;color:var(--mute);font-size:.75rem}.llist .lv{font-variant-numeric:tabular-nums;font-weight:600;text-align:right}.llist .lx{border:1.5px solid var(--ink);background:var(--paper);width:1.9rem;height:1.9rem;font:700 1rem/1 var(--body);cursor:pointer}.lempty{color:var(--mute);font-size:.9rem;margin:.8rem 0 0}.lmsg{font-size:.8rem;color:var(--mute);min-height:1em;margin:.5rem 0 0}.lcopy{width:100%;box-sizing:border-box;margin-top:.6rem;font:.85rem/1.4 var(--body);border:1px solid var(--line);padding:.5rem;min-height:5rem}.llist li.sent{color:var(--mute)}.llist li.sent .lv{font-weight:500}.lbtn[disabled]{opacity:.45;cursor:default}.logbox [hidden]{display:none!important}@media print{.logbox{display:none}}')
body = f'''<header class="wrap cover"><div class="exband" aria-hidden="true"><i class="pat pat-s"></i><i class="pat pat-k"></i><i class="pat pat-g"></i><i class="pat pat-h"></i></div>
<h1>Trip Expenses <span>Japan &amp; Hong Kong</span></h1>
<p class="sub">Shared costs for G and Cynthia, 16 to 31 October 2026. Updated by Claude as you go.</p></header>
<main class="wrap"><section class="costs" id="costs">
<div class="cost-sum" id="costsum"></div>
<section class="logbox" id="log" aria-labelledby="logh"><h2 id="logh">Log as you go</h2>
<p class="lsub">Add costs here as they happen, then copy and paste them into the expenses chat. Each copy only takes items not sent before. Saved on this device only.</p>
<form id="lform" class="lgrid" autocomplete="off">
<label class="full">Item<input id="litem" required placeholder="e.g. Lunch at Nishiki Market"></label>
<label>Amount<span class="lamt"><select id="lcur" aria-label="Currency"><option>¥</option><option>AU$</option><option>HK$</option></select><input id="lamt" required inputmode="decimal" placeholder="0"></span></label>
<label>Date<input id="ldate" type="date"></label>
<div class="full"><span style="display:block;font-size:.74rem;color:var(--mute);margin-bottom:.2rem">Who paid</span><div class="seg" id="lpay" role="group" aria-label="Who paid"><button type="button" data-v="G" aria-pressed="true">G</button><button type="button" data-v="Cynthia" aria-pressed="false">Cynthia</button><button type="button" data-v="Not sure" aria-pressed="false">Not sure</button></div></div>
<div class="full lacts"><button class="lbtn" type="submit">Add</button></div></form>
<ul class="llist" id="llist"></ul><p class="lempty" id="lempty">Nothing logged yet.</p>
<div class="lacts" id="lacts" hidden><button class="lbtn" type="button" id="lcp">Copy for Claude</button><button class="lbtn alt" type="button" id="lclr">Clear sent</button></div>
<p class="lmsg" id="lmsg" aria-live="polite"></p><textarea class="lcopy" id="ltxt" readonly hidden aria-label="Text to paste"></textarea></section>
<script>
(function(){{
 var KEY='jhk-expense-log-v1',items=[],payer='G',$=function(i){{return document.getElementById(i)}};
 try{{items=JSON.parse(localStorage.getItem(KEY)||'[]')||[]}}catch(e){{items=[]}}
 function save(){{try{{localStorage.setItem(KEY,JSON.stringify(items))}}catch(e){{}}}}
 function iso(d){{return d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0')}}
 function day(s){{if(!s)return '';var p=s.split('-'),d=new Date(+p[0],+p[1]-1,+p[2]);return ['Sun','Mon','Tue','Wed','Thu','Fri','Sat'][d.getDay()]+' '+(+p[2])}}
 function amt(it){{var n=Number(it.amt);var f=it.cur==='¥'?n.toLocaleString('en-AU',{{maximumFractionDigits:0}}):n.toLocaleString('en-AU',{{minimumFractionDigits:2,maximumFractionDigits:2}});return it.cur+f}}
 function esc(s){{return String(s).replace(/[&<>"]/g,function(c){{return {{'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}}[c]}})}}
 function fresh(){{return items.filter(function(it){{return !it.sent}})}}
 function text(){{return fresh().map(function(it){{return day(it.date)+' | '+it.item+' | '+amt(it)+' | paid by '+it.payer}}).join(String.fromCharCode(10))}}
 function draw(){{
  $('llist').innerHTML=items.map(function(it,i){{return '<li'+(it.sent?' class="sent"':'')+'><span>'+esc(it.item)+'<small>'+esc(day(it.date))+' · paid by '+esc(it.payer)+(it.sent?' · sent':'')+'</small></span><span class="lv">'+esc(amt(it))+'</span><button class="lx" type="button" data-i="'+i+'" aria-label="Remove '+esc(it.item)+'">×</button></li>'}}).join('');
  $('lempty').hidden=items.length>0;$('lacts').hidden=!items.length;if(!items.length)$('ltxt').hidden=true;
  var n=fresh().length;$('lcp').disabled=!n;$('lcp').textContent=n?'Copy '+n+' new for Claude':'Nothing new to send';$('lclr').hidden=!items.some(function(it){{return it.sent}});
 }}
 $('ldate').value=iso(new Date());
 $('lpay').addEventListener('click',function(e){{var b=e.target.closest('button');if(!b)return;payer=b.dataset.v;[].forEach.call(this.children,function(x){{x.setAttribute('aria-pressed',x===b?'true':'false')}})}});
 $('lform').addEventListener('submit',function(e){{e.preventDefault();
  var it=$('litem').value.trim(),a=$('lamt').value.replace(/[^0-9.]/g,'');
  if(!it||!a){{$('lmsg').textContent='Add an item and an amount.';return}}
  items.push({{item:it,amt:Number(a),cur:$('lcur').value,date:$('ldate').value||iso(new Date()),payer:payer}});save();draw();
  $('lform').reset();$('ldate').value=iso(new Date());$('lcur').selectedIndex=0;payer='G';[].forEach.call($('lpay').children,function(x){{x.setAttribute('aria-pressed',x.dataset.v==='G'?'true':'false')}});$('lmsg').textContent='Added. '+(fresh().length>1?fresh().length+' items':'1 item')+' waiting to send.';$('litem').focus();
 }});
 $('llist').addEventListener('click',function(e){{var b=e.target.closest('.lx');if(!b)return;items.splice(+b.dataset.i,1);save();draw();$('lmsg').textContent='Removed.'}});
 $('lcp').addEventListener('click',function(){{
  var go=fresh();if(!go.length)return;var t=text(),box=$('ltxt');box.value=t;
  function done(msg){{items=items.filter(function(it){{return !it.sent}});items.forEach(function(it){{it.sent=1}});save();draw();box.hidden=false;$('lmsg').textContent=msg}}
  function fallback(){{box.hidden=false;box.focus();box.select();var ok=false;try{{ok=document.execCommand('copy')}}catch(e){{}}
   done(ok?'Copied '+go.length+'. Paste into the expenses chat. They are now marked sent.':'Select the text below and copy it. These are now marked sent.')}}
  if(navigator.clipboard&&navigator.clipboard.writeText){{navigator.clipboard.writeText(t).then(function(){{done('Copied '+go.length+'. Paste into the expenses chat. They are now marked sent and will not be copied again.')}},fallback)}}else fallback();
 }});
 var armed=0;$('lclr').addEventListener('click',function(){{
  if(!armed){{armed=1;this.textContent='Tap again to clear';var b=this;setTimeout(function(){{armed=0;b.textContent='Clear sent'}},4000);return}}
  items=items.filter(function(it){{return !it.sent}});save();draw();armed=0;this.textContent='Clear sent';$('ltxt').hidden=true;$('lmsg').textContent='Sent items cleared.';
 }});
 draw();
}})();
</script>
<div class="cost-wrap"><table class="cost"><thead><tr><th>Date</th><th>Item</th><th class="amt">G</th><th class="amt">Cynthia</th></tr></thead><tbody id="costrows"></tbody><tfoot id="costfoot"></tfoot></table></div>
<p class="foot" id="costnote"></p>
<script type="application/json" id="costdata">{json.dumps(data, ensure_ascii=False)}</script>
</section>
<section class="rules"><h4>How this ledger works</h4><ul>
<li>Shared costs only. Personal spending stays out.</li>
<li>Amounts in AUD as charged to the card.</li>
<li>Flights are left out: you each paid your own.</li>
<li>Fees sit under the booking they belong to.</li>
<li>In trip order. Pending bookings are counted already, estimates are updated once paid.</li></ul></section>
<p class="end">Japan &amp; Hong Kong Trip Expenses. Tell Claude a new expense and this page updates.</p></main>'''
def page(head_extra='', tail=''):
    return apptools.inject(f'<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>Japan &amp; Hong Kong Trip Expenses</title>\n{head_extra}<style>{style}{extra}</style>\n</head>\n<body>\n{body}\n<script>\n(function(){{\n {js}\n}})();\n</script>\n{tail}</body>\n</html>\n', 'expenses', PDF, OFF, 'Expenses')
os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
open(os.path.join(HERE, 'out', 'trip-expenses.html'), 'w', encoding='utf-8').write(page())
# GitHub web app
DST = os.path.join(REPO, 'expenses'); os.makedirs(DST, exist_ok=True)
head = ('<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#000000">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="J&amp;HK Expenses">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" type="image/png" href="icon-192.png">\n')
sw = "<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){})})}</script>\n"
html = page(head, sw); ver = hashlib.md5(html.encode()).hexdigest()[:10]
open(os.path.join(DST, 'index.html'), 'w', encoding='utf-8').write(html)
json.dump({"name": "Japan & Hong Kong Trip Expenses", "short_name": "J&HK Expenses", "start_url": "./", "scope": "./",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#000000",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write(apptools.sw('ex-' + ver, OFF))
if PDF:
    apptools.render_pdf(os.path.join(HERE, 'out', 'trip-expenses.html'), os.path.join(HERE, 'out', PDF), 'J&HK Expenses')
    shutil.copy(os.path.join(HERE, 'out', PDF), os.path.join(DST, PDF))
fonts = ''.join(re.findall(r'@font-face\s*\{.*?\}', style, flags=re.S))
ic = f'''<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0}}
.i{{width:512px;height:512px;box-sizing:border-box;background:repeating-linear-gradient(45deg,#000 0 18px,#fff 18px 36px);display:flex;align-items:center;justify-content:center}}
.c{{width:400px;height:400px;background:#fff;border:10px solid #000;box-sizing:border-box;display:flex;flex-direction:column;justify-content:center;padding:0 34px;font-family:"Bricolage"}}
.a{{font-weight:800;font-size:150px;line-height:.85;letter-spacing:-6px}}.b{{font-weight:800;font-size:66px;line-height:1;letter-spacing:-2px;margin-top:14px}}
.d{{font-family:"Instrument";font-size:28px;margin-top:10px}}
</style></head><body><div class="i"><div class="c"><div class="a">¥ $</div><div class="b">Expenses</div><div class="d">Japan &amp; HK trip</div></div></div></body></html>'''
open('/tmp/eicon.html', 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file:///tmp/eicon.html'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('expenses page and web app written', ver)
