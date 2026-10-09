# Shared by the four web apps: the Download PDF and Save offline bar, and PDF rendering.
# Each build script imports this from <repo>/source.
import asyncio, html as _H

BASE = 'https://thestartupstudiodeveloper.github.io/japan-trip/'

CSS = '''<style>
.jt-bar{display:flex;flex-wrap:wrap;gap:.45rem;align-items:center;justify-content:flex-end;max-width:52rem;margin:0 auto;padding:.6rem 1.1rem 0;font:500 .82rem/1.2 "Instrument","Helvetica Neue",Arial,sans-serif;color:#000}
.jt-bar a,.jt-bar button{appearance:none;-webkit-appearance:none;display:inline-flex;align-items:center;gap:.35rem;font:600 .8rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;color:#000;background:#fff;border:1.5px solid #000;border-radius:0;padding:.45rem .65rem;text-decoration:none;cursor:pointer}
.jt-bar a:hover,.jt-bar button:hover{background:#000;color:#fff}
.jt-bar svg{width:.95rem;height:.95rem;fill:none;stroke:currentColor;stroke-width:2;stroke-linecap:round;stroke-linejoin:round}
.jt-bar .jt-st{flex-basis:100%;text-align:right;font-size:.74rem;color:#444;min-height:1em}
.jt-bar button[disabled]{opacity:.55;cursor:default}
.jt-bar .jt-off[hidden]{display:none}
@media print{.jt-bar{display:none!important}}
</style>'''

ICON_DL = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 4v11M7 10l5 5 5-5M5 20h14"/></svg>'
ICON_OFF = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M7 18a5 5 0 0 1-.6-10A6 6 0 0 1 18 9a4.5 4.5 0 0 1-.5 9z"/><path d="M12 11v6M9.5 14.5 12 17l2.5-2.5"/></svg>'


def bar(app, pdf, files, label):
    """app: folder under BASE ('' for the itinerary), pdf: file name, files: list of paths to save offline
    (relative to the app folder), label: name used in the status line."""
    url = BASE + (app + '/' if app else '')
    key = 'jt-off-' + (app or 'itinerary')
    js = '''<script>
(function(){
 var BASE=%s,KEY=%s,FILES=%s,LABEL=%s;
 var bar=document.querySelector('.jt-bar'); if(!bar) return;
 var dl=bar.querySelector('.jt-dl'), btn=bar.querySelector('.jt-off'), st=bar.querySelector('.jt-st');
 var here=/github\\.io$/.test(location.hostname);
 if(here){dl.href=dl.getAttribute('data-pdf');dl.setAttribute('download','');dl.removeAttribute('target');}
 if(!here||!('caches' in window)){btn.hidden=true;return}
 function get(){try{return localStorage.getItem(KEY)}catch(e){return null}}
 function put(v){try{localStorage.setItem(KEY,v)}catch(e){}}
 function fmt(t){var d=new Date(+t);return d.getDate()+' '+['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'][d.getMonth()]+' '+String(d.getHours()).padStart(2,'0')+':'+String(d.getMinutes()).padStart(2,'0')}
 var t=get(); if(t) caches.has(KEY).then(function(ok){st.textContent=ok?LABEL+' saved for offline, '+fmt(t)+'. Tap again to refresh.':''});
 btn.addEventListener('click',function(){
  if(!navigator.onLine){st.textContent='You are offline. Connect, then tap again.';return}
  btn.disabled=true;st.textContent='Saving\\u2026';
  caches.open(KEY).then(function(c){return Promise.all(FILES.map(function(f){return fetch(f,{cache:'reload'}).then(function(r){if(!r.ok)throw new Error(f);return c.put(f,r)})}))})
   .then(function(){var n=Date.now();put(n);st.textContent=LABEL+' saved for offline, '+fmt(n)+'. Tap again to refresh.'})
   .catch(function(){st.textContent='Could not save everything. Check the connection and try again.'})
   .then(function(){btn.disabled=false});
 });
})();
</script>''' % tuple(map(lambda v: _json(v), (url, key, files, label)))
    return (CSS + f'<div class="jt-bar" role="toolbar" aria-label="Download and offline">'
            f'<a class="jt-dl" href="{_H.escape(url + pdf)}" data-pdf="{_H.escape(pdf)}" target="_blank" rel="noopener">{ICON_DL}Download PDF</a>'
            f'<button type="button" class="jt-off">{ICON_OFF}Save offline</button><span class="jt-st" aria-live="polite"></span></div>'), js


def _json(v):
    import json
    return json.dumps(v, ensure_ascii=False).replace('</', '<\\/')


def inject(html, app, pdf, files, label):
    top, js = bar(app, pdf, files, label)
    import re
    html = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + '\n' + top, html, count=1)
    return html.replace('</body>', js + '\n</body>', 1)


def render_pdf(src_html_path, pdf_path, footer):
    from playwright.async_api import async_playwright
    async def go():
        async with async_playwright() as p:
            b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 1100, 'height': 900})
            await pg.goto('file://' + src_html_path); await pg.wait_for_timeout(600)
            await pg.emulate_media(media='print')
            await pg.pdf(path=pdf_path, format='A4', print_background=True, prefer_css_page_size=True, display_header_footer=True,
                         header_template='<span></span>',
                         footer_template=f'<div style="font-size:7.5pt;font-family:Helvetica,Arial,sans-serif;width:100%;padding:0 13mm;display:flex;justify-content:space-between;color:#000"><span>{_H.escape(footer)}</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')
            await b.close()
    asyncio.run(go())


def sw(prefix, files):
    """Service worker: network first, cached copy when offline. Keeps the Save offline cache and other apps' caches."""
    import json
    return ("""// Network first, so updates show straight away; cached copy when offline.
const C = '""" + prefix + """';
const FILES = """ + json.dumps(files) + """;
const MINE = '""" + prefix.split('-')[0] + """-';
self.addEventListener('install', e => { e.waitUntil(caches.open(C).then(c => c.addAll(FILES)).then(() => self.skipWaiting())); });
self.addEventListener('activate', e => { e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k.startsWith(MINE) && k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())); });
self.addEventListener('fetch', e => {
  if (e.request.method !== 'GET' || new URL(e.request.url).origin !== location.origin) return;
  e.respondWith(fetch(e.request).then(r => { const copy = r.clone(); caches.open(C).then(c => c.put(e.request, copy)); return r; })
    .catch(() => caches.match(e.request, {ignoreSearch: true}).then(m => m || caches.match('index.html'))));
});
""")
