# Builds the standalone Trip Expenses page (claude.ai artifact copy) and its GitHub web app.
# Usage: python3 expenses_build.py [repo dir]
#   reads ../expenses.json and the itinerary build (../out/japan-hong-kong-final-itinerary.html) for fonts and styles
#   writes out/trip-expenses.html (publish to claude.ai) and <repo>/expenses/ (GitHub Pages web app)
import sys, os, re, json, asyncio, hashlib
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/japan-trip'
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
         '.rules li::before{content:"";position:absolute;left:0;top:.55em;width:.45rem;height:.45rem;background:var(--ink)}')
body = f'''<header class="wrap cover"><div class="exband" aria-hidden="true"><i class="pat pat-s"></i><i class="pat pat-k"></i><i class="pat pat-g"></i><i class="pat pat-h"></i></div>
<h1>Trip Expenses <span>Japan &amp; Hong Kong</span></h1>
<p class="sub">Shared costs for G and Cynthia, 16 to 31 October 2026. Updated by Claude as you go.</p></header>
<main class="wrap"><section class="costs" id="costs">
<div class="cost-sum" id="costsum"></div>
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
    return (f'<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
            f'<title>Japan &amp; Hong Kong Trip Expenses</title>\n{head_extra}<style>{style}{extra}</style>\n</head>\n<body>\n{body}\n<script>\n(function(){{\n {js}\n}})();\n</script>\n{tail}</body>\n</html>\n')
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
open(os.path.join(DST, 'sw.js'), 'w').write("""// Network first, cached copy when offline.
const C = 'ex-""" + ver + """';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('ex-') && k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match('index.html'))));
});
""")
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
