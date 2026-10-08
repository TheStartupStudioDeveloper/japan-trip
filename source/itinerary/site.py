# Builds the GitHub Pages copy of the online itinerary into ../../japan-trip (or argv[1]).
import sys, os, re, json, asyncio, hashlib, shutil
SRC = 'out/japan-hong-kong-final-itinerary.html'
DST = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/japan-trip'
html = open(SRC, encoding='utf-8').read()
ver = hashlib.md5(html.encode()).hexdigest()[:10]
head = ('<meta name="robots" content="noindex, nofollow">\n'
        '<meta name="theme-color" content="#000000">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n'
        '<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-status-bar-style" content="default">\n'
        '<meta name="apple-mobile-web-app-title" content="J&amp;HK Itinerary">\n'
        '<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="apple-touch-icon" href="icon-180.png">\n'
        '<link rel="icon" type="image/png" href="icon-192.png">\n')
html = html.replace('</title>\n', '</title>\n' + head, 1)
sw = ("<script>if('serviceWorker' in navigator){addEventListener('load',function(){"
      "navigator.serviceWorker.register('sw.js').catch(function(){})})}</script>\n</body>")
html = html.replace('</body>', sw, 1)
os.makedirs(DST, exist_ok=True)
open(os.path.join(DST, 'index.html'), 'w', encoding='utf-8').write(html)
json.dump({"name": "Japan & Hong Kong", "short_name": "J&HK Itinerary", "start_url": "./", "scope": "./",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#000000",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write("""// Network first, so updates show straight away; cached copy when offline.
const C = 'jhk-""" + ver + """';
const FILES = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png'];
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request).then(m => m || caches.match('index.html'))));
});
""")
open(os.path.join(DST, '.nojekyll'), 'w').write('')
# icon, drawn with the itinerary's own fonts
fonts = ''.join(re.findall(r'@font-face\s*\{.*?\}', html, flags=re.S))
ic = f'''<!doctype html><html><head><meta charset="utf-8"><style>{fonts}
html,body{{margin:0;background:#000}}
.i{{width:512px;height:512px;background:#000;color:#fff;font-family:"Bricolage";display:flex;flex-direction:column;justify-content:center;padding:0 56px;box-sizing:border-box}}
.a{{font-weight:800;font-size:150px;line-height:.9;letter-spacing:-4px}}.b{{font-weight:800;font-size:96px;line-height:1;letter-spacing:-2px;margin-top:8px}}
.c{{font-family:"Instrument";font-size:34px;margin-top:22px;opacity:.85}}
.band{{display:flex;height:26px;margin-top:30px;gap:0}}.band i{{flex:1}}
.s{{background:#fff}}.k{{background:repeating-linear-gradient(90deg,#fff 0 6px,#000 6px 12px);border:3px solid #fff}}
.g{{background:linear-gradient(#fff 0 30%,#000 30% 70%,#fff 70%);border:3px solid #fff}}.h{{background:repeating-linear-gradient(45deg,#fff 0 6px,#000 6px 12px);border:3px solid #fff}}
</style></head><body><div class="i"><div class="a">Japan</div><div class="b">&amp; HK</div><div class="c">16 to 31 Oct 2026</div>
<div class="band"><i class="s"></i><i class="k"></i><i class="g"></i><i class="h"></i></div></div></body></html>'''
open('/tmp/icon.html', 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file:///tmp/icon.html'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('site written to', DST, 'version', ver)
