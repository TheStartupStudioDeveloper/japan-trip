# Turns typhoon/index.html into the "J&HK Typhoon" home-screen web app: manifest, service worker, icons.
# Run after typhoon_build.py, from the repo root: python3 source/typhoon/typhoon_app.py
import os, sys, re, json, asyncio, hashlib
REPO = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
DST = os.path.join(REPO, 'typhoon')
sys.path[:0] = [os.path.join(REPO, 'source')]
import apptools
OFF = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png']
p = os.path.join(DST, 'index.html')
html = open(p, encoding='utf-8').read()
html = html.replace('<link rel="apple-touch-icon" href="../icon-180.png">\n<link rel="icon" type="image/png" href="../icon-192.png">\n',
    '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
    '<meta name="apple-mobile-web-app-title" content="J&amp;HK Typhoon">\n<link rel="manifest" href="manifest.webmanifest">\n'
    '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" type="image/png" href="icon-192.png">\n')
assert 'manifest.webmanifest' in html
html = html.replace('</body>', "<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){})})}</script></body>", 1)
open(p, 'w', encoding='utf-8').write(html)
ver = hashlib.md5(html.encode()).hexdigest()[:10]
json.dump({"name": "Kyoto & Tokyo Typhoon Backup", "short_name": "J&HK Typhoon", "start_url": "./", "scope": "./",
           "display": "standalone", "background_color": "#ffffff", "theme_color": "#000000",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"},
                     {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write(apptools.sw('ty-' + ver, OFF))

if os.path.exists(os.path.join(DST, 'icon-512.png')) and '--icon' not in sys.argv:
    print('app files written, icon kept'); sys.exit()
# Icon: same family as the other apps. White, a black inset frame, the weather-map typhoon symbol,
# and a band in the Kyoto stripes and the Tokyo centre bar only, the two legs this plan covers.
ff = os.path.join(REPO, 'index.html')
FONT = ''.join(re.findall(r'@font-face\s*\{.*?\}', open(ff, encoding='utf-8').read(), flags=re.S))
ic = '''<!doctype html><html><head><meta charset="utf-8"><style>''' + FONT + '''
html,body{margin:0;background:#fff}
.i{width:512px;height:512px;background:#fff;color:#000;font-family:"Bricolage",Helvetica,sans-serif;display:flex;flex-direction:column;justify-content:center;padding:0 64px;box-sizing:border-box;box-shadow:inset 0 0 0 22px #000}
svg{width:178px;height:178px;margin-left:-6px}
.a{font-weight:800;font-size:96px;line-height:.9;letter-spacing:-3px;margin-top:8px}
.c{font-size:32px;margin-top:14px}
.band{display:flex;height:26px;margin-top:26px}.band i{flex:1;box-shadow:inset 0 0 0 3px #000}
.k{background:repeating-linear-gradient(90deg,#000 0 6px,#fff 6px 12px)}
.g{background:linear-gradient(#fff 0 30%,#000 30% 70%,#fff 70%)}
</style></head><body><div class="i">
<svg viewBox="0 0 40 40"><circle cx="20" cy="20" r="6.5" fill="none" stroke="#000" stroke-width="4"/>
<path d="M20 13.5C21 6 26 3 33 3" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round"/>
<path d="M20 26.5C19 34 14 37 7 37" fill="none" stroke="#000" stroke-width="4" stroke-linecap="round"/></svg>
<div class="a">Typhoon</div><div class="c">Kyoto &amp; Tokyo backup</div>
<div class="band"><i class="k"></i><i class="g"></i></div></div></body></html>'''
tmp = '/tmp/claude-0/ticon.html'; os.makedirs('/tmp/claude-0', exist_ok=True)
open(tmp, 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as pw:
        b = await pw.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file://' + tmp); await pg.wait_for_timeout(500)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('app and icon written, version', ver)
