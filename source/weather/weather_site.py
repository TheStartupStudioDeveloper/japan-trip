# Builds the GitHub Pages copy of the Trip Weather page into <repo>/weather/.
# Usage: python3 weather_site.py <weather.html from the claude.ai artifact> [repo dir]
import sys, os, re, json, asyncio, hashlib
SRC = sys.argv[1]; REPO = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/japan-trip'
DST = os.path.join(REPO, 'weather'); os.makedirs(DST, exist_ok=True)
html = open(SRC, encoding='utf-8').read()
ver = hashlib.md5(html.encode()).hexdigest()[:10]
head = ('<meta name="robots" content="noindex, nofollow"><meta name="theme-color" content="#ffffff">'
        '<meta name="apple-mobile-web-app-capable" content="yes"><meta name="mobile-web-app-capable" content="yes">'
        '<meta name="apple-mobile-web-app-title" content="J&amp;HK Weather"><link rel="manifest" href="manifest.webmanifest">'
        '<link rel="apple-touch-icon" href="icon-180.png"><link rel="icon" type="image/png" href="icon-192.png">')
html = re.sub(r'(<meta name=viewport[^>]*>)', lambda m: m.group(1) + head, html, count=1)
assert 'manifest.webmanifest' in html
html = html.replace('</body>', "<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){})})}</script></body>", 1)
open(os.path.join(DST, 'index.html'), 'w', encoding='utf-8').write(html)
json.dump({"name": "Japan & Hong Kong Trip Weather", "short_name": "J&HK Weather", "start_url": "./", "scope": "./",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#ffffff",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write("""// Network first, cached copy when offline.
const C = 'wx-""" + ver + """';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith('wx-') && k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET') return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match('index.html'))));
});
""")
fonts = ''
ic = '''<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="file:///dev/null"><style>
html,body{margin:0;background:#fff}
.i{width:512px;height:512px;background:#fff;color:#000;font-family:FONT,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:0 56px;box-sizing:border-box;border:0}
svg{width:190px;height:190px;margin-left:-8px}
.a{font-weight:800;font-size:98px;line-height:.9;letter-spacing:-3px;margin-top:6px}
.c{font-size:34px;margin-top:16px}
.band{display:flex;height:26px;margin-top:28px}.band i{flex:1;box-shadow:inset 0 0 0 3px #000}
.s{background:#000}.k{background:repeating-linear-gradient(90deg,#000 0 6px,#fff 6px 12px)}
.g{background:linear-gradient(#fff 0 30%,#000 30% 70%,#fff 70%)}.h{background:repeating-linear-gradient(45deg,#000 0 4px,#fff 4px 12px)}
</style></head><body><div class="i">
<svg viewBox="0 0 32 32"><circle cx="12" cy="11" r="5" fill="#000"/><g stroke="#000" stroke-width="2" stroke-linecap="round" fill="none"><path d="M12 2v2.5M3 11h2.5M5.6 4.6l1.8 1.8M18.4 4.6l-1.8 1.8"/></g><path d="M10 26h15a5 5 0 0 0 0-10 7 7 0 0 0-13 2.2A4 4 0 0 0 10 26z" fill="#fff" stroke="#000" stroke-width="2.2" stroke-linejoin="round"/></svg>
<div class="a">Weather</div><div class="c">Japan &amp; HK trip</div>
<div class="band"><i class="s"></i><i class="k"></i><i class="g"></i><i class="h"></i></div></div></body></html>'''
_ff = os.path.join(REPO, 'source', 'itinerary', 'out', 'japan-hong-kong-final-itinerary.html')
FONT = ''.join(re.findall(r'@font-face\s*\{.*?\}', open(_ff, encoding='utf-8').read(), flags=re.S)) if os.path.exists(_ff) else ''
ic = ic.replace('<link rel="stylesheet" href="file:///dev/null">', '<style>' + FONT + '</style>').replace('FONT', '"Bricolage"' if FONT else 'Helvetica')
open('/tmp/wicon.html', 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file:///tmp/wicon.html'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('weather site written to', DST, 'version', ver)
