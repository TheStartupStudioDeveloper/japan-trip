# Builds J&HK Extras: the standalone "up our sleeve" reference (claude.ai artifact copy) and its GitHub web app.
# Usage: python3 extras_build.py [repo dir]
#   reads extras.json, plus the itinerary build (../out/japan-hong-kong-final-itinerary.html) for fonts, styles, place cards
#   and which places are already scheduled in the day plans. Scheduled places drop off this list automatically.
#   writes out/jhk-extras.html (publish to claude.ai) and <repo>/extras/ (GitHub Pages web app)
import sys, os, re, json, asyncio, hashlib, html as H
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/japan-trip'
MASTER_URL = 'https://thestartupstudiodeveloper.github.io/japan-trip/'
data = json.load(open(os.path.join(HERE, 'extras.json'), encoding='utf-8'))
master = open(os.path.join(ROOT, 'out', 'japan-hong-kong-final-itinerary.html'), encoding='utf-8').read()
style = re.search(r'<style>(.*?)</style>', master, re.S).group(1)
tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()

# place cards: master cards plus Extras-only cards
m = re.search(r'var P=', master); P, _ = json.JSONDecoder().raw_decode(master, m.end())
for k, c in data['cards'].items():
    P[k] = c

# scheduled = linked inside a time row of any day plan in the master
sched = set()
for body in re.findall(r'<article[^>]*class="day[^"]*"[^>]*>(.*?)</article>', master, re.S):
    for r in re.findall(r'<li class="row[^"]*">(.*?)</li>', body, re.S):
        sched |= set(re.findall(r'data-p="([^"]+)"', r))

def pl(k, label=None):
    return f'<a class="pl" href="#" role="button" data-p="{k}">{H.escape(label or P[k]["n"])}</a>'

def tag(x):
    cls = ' tag-b' if x == 'Book now' else ' tag-tb' if x == 'Book' else ''
    return f'<span class="tag{cls}">{H.escape(x)}</span>'

dropped, areas_html, counts = [], [], {}
for a in data['areas']:
    items = [i for i in a['items'] if i['key'] not in sched]
    dropped += [(a['name'], i['key']) for i in a['items'] if i['key'] in sched]
    counts[a['key']] = len(items)
    rows, cur = [], None
    for i in items:
        if i['group'] != cur:
            rows.append(f'<li class="ugrp">{H.escape(i["group"])}</li>'); cur = i['group']
        rows.append(f'<li class="row urow"><span class="t">{H.escape(i["time"])}</span><div class="w"><p class="p">{pl(i["key"])} '
                    f'{"".join(tag(x) for x in i["tags"])}<span class="uwhat">{H.escape(i["one"])}</span></p>'
                    f'<p class="n ufit"><b>Fits</b> {H.escape(i["fits"])}</p></div></li>')
    must = ''.join(f'<li><b>{H.escape(x["dish"])}</b><span>{H.escape(x["line"])}</span><em>Try it: {pl(x["where"])}</em></li>' for x in a.get('must', []))
    days = ' '.join(f'<a href="{MASTER_URL}#{d}">{t}</a>' for d, t in a['days'])
    areas_html.append(f'''<section class="area" id="{a["key"]}">
 <div class="band"><i class="pat pat-{a["pat"]}"></i></div>
 <div class="ah"><p class="kanji">{a["kanji"]}</p><div><h2>{H.escape(a["name"])}</h2><p class="meta">{H.escape(a["meta"])}</p>
  <p class="udays"><span>In the itinerary:</span> {days}</p></div></div>
 {f'<p class="unote"><b>Good to know</b>{H.escape(a["notes"])}</p>' if a.get('notes') else ''}
 {f'<div class="must"><p class="ugrp">Must try here</p><ul>{must}</ul></div>' if must else ''}
 <ol class="rows">{"".join(rows)}</ol>
</section>''')

built = {a['key'] for a in data['areas']}
chips = ''.join(
    (f'<a class="achip" href="#{k}" data-a="{k}"><i class="pat pat-{p}"></i>{n}<small>{counts[k]}</small></a>' if k in built else
     f'<span class="achip off"><i class="pat pat-{p}"></i>{n}<small>Soon</small></span>')
    for k, n, p in data['planned'])

extra = '''
header.cover{padding:2.4rem 1.1rem 0}.exband{display:flex;height:12px;margin-bottom:1.6rem}.exband i{flex:1}
.achips{position:sticky;top:0;z-index:5;background:var(--paper);border-bottom:1.5px solid var(--ink);margin-top:1.6rem;padding-top:env(safe-area-inset-top,0px)}
.achips div{display:flex;gap:6px;overflow-x:auto;padding:.55rem 1.1rem;scrollbar-width:none;max-width:52rem;margin:0 auto}.achips div::-webkit-scrollbar{display:none}
.achip{flex:0 0 auto;display:grid;grid-template-columns:1.1rem auto;grid-template-rows:auto auto;column-gap:.45rem;align-items:center;text-decoration:none;border:1.5px solid var(--ink);padding:.35rem .6rem .35rem .45rem;font:700 .92rem/1.1 var(--display);color:var(--ink)}
.achip i{grid-row:1/3;width:1.1rem;height:1.6rem}.achip small{font:400 .68rem var(--body);color:var(--mute)}
.achip.on{background:var(--ink);color:var(--paper)}.achip.on small{color:var(--paper)}.achip.on i{box-shadow:inset 0 0 0 1.5px #fff}
.achip.off{border-color:var(--line);color:var(--mute)}.achip.off i{opacity:.35}
.area{margin-top:2rem;border:1.5px solid var(--ink);scroll-margin-top:calc(env(safe-area-inset-top,0px) + 4.6rem)}
.area .band{height:12px}.area>*:not(.band){margin-left:1rem;margin-right:1rem}
.ah{display:flex;gap:.9rem;align-items:center;margin-top:.9rem}
.ah .kanji{writing-mode:horizontal-tb;font-size:2.5rem;line-height:1;letter-spacing:0;white-space:nowrap}
.ah h2{font:800 1.6rem/1.1 var(--display);letter-spacing:-.02em}.ah .meta{margin-top:.15rem;font-size:.9rem}
.udays{margin-top:.35rem;font-size:.82rem;color:var(--mute)}.udays a{display:inline-block;margin:0 .15rem .2rem 0;padding:.12rem .4rem;border:1.5px solid var(--ink);color:var(--ink);text-decoration:none;font-weight:700;font-size:.76rem}
.must{margin-top:1rem}.must li{display:grid;padding:.6rem 0;border-bottom:1px solid var(--line)}
.must b{font:700 1rem/1.25 var(--display)}.must span{color:var(--mute);font-size:.92rem}.must em{font-style:normal;font-size:.86rem;margin-top:.15rem}
.area .rows{margin-top:1rem;margin-bottom:1.2rem}
.unote{margin-top:1rem;padding:.65rem .8rem;border:1.5px dashed var(--ink);font-size:.88rem;line-height:1.45}.unote b{display:block;font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;margin-bottom:.15rem}
.ugrp{font:700 .72rem var(--body);text-transform:uppercase;letter-spacing:.08em;padding:1rem 0 .35rem;border-bottom:1.5px solid var(--ink)}
.must .ugrp,.rows .ugrp:first-child{padding-top:.4rem}
.urow:has(+ .ugrp),.rows .urow:last-child,.must li:last-child{border-bottom:0}.rows .ugrp:not(:first-child){padding-top:1.6rem}.area .rows{margin-bottom:.4rem}.must+.rows{margin-top:1.4rem}
.uwhat{display:block;font-weight:400;margin-top:.15rem}.ufit b{font-size:.68rem;text-transform:uppercase;letter-spacing:.06em;margin-right:.25rem;color:var(--ink)}
@media (min-width:640px){.area>*:not(.band){margin-left:1.5rem;margin-right:1.5rem}.must li{grid-template-columns:9.5rem 1fr 1fr;gap:.8rem;align-items:baseline}.must em{margin-top:0}}
@media print{
 .achips{display:none!important}header.cover{padding:0}
 .area{break-before:page;margin-top:0;border:1.5px solid #000}main>.area:first-child{break-before:auto;margin-top:6mm}.area .band{height:3.5mm}.area>*:not(.band){margin-left:5mm;margin-right:5mm}
 .ah{margin-top:2.5mm;gap:4mm}.ah .kanji{font-size:24pt}.ah h2{font-size:16pt}.ah .meta{font-size:8.6pt}
 .udays{font-size:8pt}.udays a{border:0;padding:0;font-weight:400;font-size:8pt}
 .must{margin-top:2.5mm}.must li{grid-template-columns:30mm 1fr 1fr;gap:4mm;padding:1.1mm 0;break-inside:avoid}.must b{font-size:9.5pt}.must span,.must em{font-size:8.6pt}
 .area .rows{margin-top:2.5mm;margin-bottom:4mm}.unote{margin-top:2.5mm;padding:1.6mm 2.5mm;font-size:8.4pt;break-inside:avoid}.unote b{font-size:6.8pt}
 .ugrp{font-size:7pt;padding:2.5mm 0 .8mm;break-after:avoid}.rows .ugrp:not(:first-child){padding-top:4.5mm}.must+.rows{margin-top:4mm}
 .urow{grid-template-columns:20mm 1fr 1.25fr;padding:1.3mm 0}.urow .p,.urow .t{font-size:9.5pt}.urow .n{font-size:8.6pt}
}'''

sheet = tpl[tpl.index('<aside class="sheet"'):tpl.index('</aside>') + 8]
i = tpl.index("(function(){\n var P=/*PLACES*/"); j = tpl.index('})();', i) + 5
cardjs = tpl[i:j].replace('/*PLACES*/', json.dumps(P, ensure_ascii=False).replace('</', '<\\/'))
chipjs = '''(function(){
 var chips=[].slice.call(document.querySelectorAll('a.achip'));
 if(!('IntersectionObserver' in window))return;
 var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){var id=e.target.id;
  chips.forEach(function(c){var on=c.dataset.a===id;c.classList.toggle('on',on);if(on){var bx=c.parentNode,l=c.offsetLeft-bx.offsetLeft;if(l<bx.scrollLeft||l+c.offsetWidth>bx.scrollLeft+bx.clientWidth)bx.scrollLeft=l-16}})}})},{rootMargin:'-30% 0px -60% 0px'});
 document.querySelectorAll('.area').forEach(function(a){io.observe(a)});
})();'''
total = sum(counts.values())
body = f'''<header class="wrap cover"><div class="exband" aria-hidden="true"><i class="pat pat-s"></i><i class="pat pat-k"></i><i class="pat pat-g"></i><i class="pat pat-h"></i></div>
<h1>J&amp;HK Extras <span>Up our sleeve</span></h1>
<p class="sub">Everything worth doing that is not in the day plans, by area. Places to eat and drink, the food to try, and things to swap in if the plan moves or something is missed. When a place goes into the itinerary it leaves this list, and when one comes out it lands back here. <span class="screen">Tap any underlined name for its card.</span></p></header>
<nav class="achips" aria-label="Jump to an area"><div>{chips}</div></nav>
<main class="wrap">
{''.join(areas_html)}
<p class="end">J&amp;HK Extras, companion to the Japan &amp; Hong Kong Master Itinerary V2. {total} ideas so far. Ask Claude to add, move or book anything.</p>
</main>
{sheet}'''

def page(head_extra='', tail=''):
    return (f'<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>J&amp;HK Extras</title>\n{head_extra}<style>{style}{extra}</style>\n</head>\n<body>\n{body}\n<script>\n{cardjs}\n{chipjs}\n</script>\n{tail}</body>\n</html>\n')

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
open(os.path.join(HERE, 'out', 'jhk-extras.html'), 'w', encoding='utf-8').write(page())

# GitHub web app
DST = os.path.join(REPO, 'extras'); os.makedirs(DST, exist_ok=True)
head = ('<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#000000">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="J&amp;HK Extras">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" type="image/png" href="icon-192.png">\n')
sw = "<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){})})}</script>\n"
html = page(head, sw); ver = hashlib.md5(html.encode()).hexdigest()[:10]
open(os.path.join(DST, 'index.html'), 'w', encoding='utf-8').write(html)
json.dump({"name": "J&HK Extras", "short_name": "J&HK Extras", "start_url": "./", "scope": "./",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#000000",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write("""// Network first, cached copy when offline.
const C = 'xt-""" + ver + """';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('xt-') && k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match('index.html'))));
});
""")

# icon: white tile, a black card slipping out of a sleeve, leg band underneath
fonts = ''.join(re.findall(r'@font-face\s*\{.*?\}', style, flags=re.S))
pats = re.search(r'\.pat-k\{[^}]*\}', style).group(0) + re.search(r'\.pat-h\{[^}]*\}', style).group(0)
ic = f'''<!doctype html><html><head><meta charset="utf-8"><style>{fonts}{pats}
html,body{{margin:0}}
.i{{width:512px;height:512px;background:#fff;position:relative;overflow:hidden;font-family:"Bricolage"}}
.card{{position:absolute;left:118px;top:58px;width:250px;height:330px;background:#000;border-radius:22px;transform:rotate(-12deg);box-shadow:0 0 0 8px #fff}}
.card b{{position:absolute;left:28px;top:6px;color:#fff;font-weight:800;font-size:120px;line-height:1}}
.card s{{position:absolute;right:26px;bottom:20px;color:#fff;font-weight:800;font-size:64px;line-height:1;text-decoration:none;transform:rotate(180deg)}}
.sleeve{{position:absolute;left:0;right:0;top:268px;height:244px;background:#fff;border-top:10px solid #000}}
.t{{position:absolute;left:38px;top:300px;font-weight:800;font-size:92px;line-height:1;letter-spacing:-3px}}
.s{{position:absolute;left:42px;top:398px;font-family:"Instrument";font-size:30px}}
.band{{position:absolute;left:0;right:0;bottom:0;height:40px;display:flex}}.band i{{flex:1;display:block}}
.ps{{background:#000}}.pg{{background:linear-gradient(#fff 33%,#000 33% 67%,#fff 67%)}}
</style></head><body><div class="i"><div class="card"><b>+</b></div><div class="sleeve"></div>
<div class="t">Extras</div><div class="s">Japan &amp; Hong Kong</div>
<div class="band"><i class="ps"></i><i class="pat-k"></i><i class="pg"></i><i class="pat-h"></i></div></div></body></html>'''
open('/tmp/xicon.html', 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file:///tmp/xicon.html'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('extras written', ver, 'items', total, 'dropped as scheduled:', dropped)
