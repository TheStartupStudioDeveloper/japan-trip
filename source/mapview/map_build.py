# Builds J&HK Map View (Map Itinerary): one zoomable map per day, built from the Master Itinerary's own day plans and place cards.
# Usage: python3 mapview/map_build.py [repo dir]
#   reads ../out/japan-hong-kong-final-itinerary.html (rows, cards, styles) and mapview/geo.py (coordinates, base map)
#   writes mapview/out/jhk-map.html (claude.ai) and <repo>/map/ (GitHub Pages web app)
import sys, os, re, json, math, html as H, hashlib, asyncio
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
REPO = sys.argv[1] if len(sys.argv) > 1 else '/home/claude/japan-trip'
sys.path[:0] = [HERE, os.path.join(REPO, 'source'), ROOT]
import apptools, geo
from routes import ROUTES
from urllib.parse import quote as _q
MASTER_URL = 'https://thestartupstudiodeveloper.github.io/japan-trip/'
OFF = ['./', 'index.html', 'manifest.webmanifest', 'icon-180.png', 'icon-192.png', 'icon-512.png']
master = open(os.path.join(ROOT, 'out', 'japan-hong-kong-final-itinerary.html'), encoding='utf-8').read()
style = re.search(r'<style>(.*?)</style>', master, re.S).group(1)
tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
m = re.search(r'var P=', master); P, _ = json.JSONDecoder().raw_decode(master, m.end())
GEO, GENERIC = geo.GEO, geo.GENERIC
TRANSIT = re.compile(r'\b(train|line|Nozomi|Express|Taxi|Yurikamome|Lift|cable car down|Back to the centre|Star Ferry|departs|Land |Land$|Boarding|Red urban taxi)\b', re.I)
HOTELISH = re.compile(r'\b(hotel|check in|check out|collect bags|pack)\b', re.I)

def dist(a, b):
    la = math.radians((a[0] + b[0]) / 2)
    return math.hypot((a[0] - b[0]) * 111320, (a[1] - b[1]) * 111320 * math.cos(la))

def fixlinks(h):
    h = re.sub(r'href="#h(\d+)"', lambda m: f'href="{MASTER_URL}#h{m.group(1)}" target="_blank" rel="noopener"', h)
    return re.sub(r'\(<a class="hl"', '(<a class="hl"', h)

# ---------- read the days from the master
days = []
for art, d in re.findall(r'(<article[^>]*id="d(\d+)"[^>]*>.*?</article>)', master, re.S):
    d = int(d)
    cls = re.search(r'class="day([^"]*)"', art).group(1)
    band = re.search(r'<div class="band">.*?</div>', art, re.S).group(0)
    dow = re.search(r'<span class="dow">(.*?)<br>', art, re.S).group(1)
    where = re.search(r'<span class="where">(.*?)</span>', art, re.S).group(1)
    title = re.search(r'<h3>(.*?)</h3>', art, re.S).group(1)
    rows = []
    for li_cls, r in re.findall(r'<li class="row([^"]*)">(.*?)</li>', art, re.S):
        t = re.search(r'<span class="t">(.*?)</span>', r, re.S).group(1)
        p = re.search(r'<p class="p">(.*?)</p>', r, re.S).group(1)
        n = re.search(r'<p class="n">(.*?)</p>', r, re.S)
        n = n.group(1) if n else ''
        ptxt = H.unescape(re.sub(r'<[^>]+>', '', p)).strip()
        tk = [k for k in re.findall(r'data-p="([^"]+)"', p) if k in GEO]
        spec = [k for k in tk if k not in GENERIC]
        transit = bool(TRANSIT.search(ptxt))
        key = spec[0] if spec else (tk[0] if tk and not transit else None)
        if not key and HOTELISH.search(ptxt) and geo.HOTEL.get(d) and not re.search(r'Cathay|airport', ptxt, re.I):
            key = geo.HOTEL_AM.get(d, geo.HOTEL[d]) if t[:2].isdigit() and int(t[:2]) < 12 else geo.HOTEL[d]
        opt = bool(re.match(r'(Optional|Or )', ptxt))
        rows.append(dict(t=t, p=fixlinks(p), n=fixlinks(n), txt=ptxt, key=key, opt=opt, transit=transit, cls=li_cls.strip()))
    days.append(dict(d=d, cls=cls, band=band, dow=dow, where=where, title=title, rows=rows))

# ---------- panels: group pinned stops that sit within 5 km of each other
for day in days:
    panels = []
    for i, r in enumerate(day['rows']):
        if not r['key']: continue
        c = GEO[r['key']]
        for pn in panels:
            cen = (sum(GEO[day['rows'][j]['key']][0] for j in pn) / len(pn), sum(GEO[day['rows'][j]['key']][1] for j in pn) / len(pn))
            if dist(c, cen) < 5000: pn.append(i); break
        else: panels.append([i])
    day['panels'] = panels
    n = 0
    for r in day['rows']:
        if r['key']: n += 1; r['num'] = n

W = 760
def region(lat, lng):
    return min(geo.REGIONS, key=lambda x: dist((lat, lng), (x[1], x[2])))[0]

def label_at(pts_xy):
    # middle segment, angle kept readable
    k = max(0, len(pts_xy) // 2 - 1); (x1, y1), (x2, y2) = pts_xy[k], pts_xy[min(k + 1, len(pts_xy) - 1)]
    ang = math.degrees(math.atan2(y2 - y1, x2 - x1))
    if ang > 90: ang -= 180
    if ang < -90: ang += 180
    return (x1 + x2) / 2, (y1 + y2) / 2, ang, math.hypot(x2 - x1, y2 - y1)

def span(pts, kx):
    la0, la1 = min(p[0] for p in pts), max(p[0] for p in pts)
    lo0, lo1 = min(p[1] for p in pts), max(p[1] for p in pts)
    return la0, la1, lo0, lo1, max((lo1 - lo0) * kx, 0.008) * 1.5, max(la1 - la0, 0.008) * 1.5

def panel_svg(day, idx, pn, title=None, pkind='area', areas=None):
    pts = [GEO[day['rows'][i]['key']] for i in pn]
    areas = areas or [pn]
    kx = math.cos(math.radians((min(p[0] for p in pts) + max(p[0] for p in pts)) / 2))
    la0, la1, lo0, lo1, sx, sy = span(pts, kx)
    # room to zoom out: the whole map is at least three times the biggest area
    big = max(max(span([GEO[day['rows'][i]['key']] for i in a], kx)[4:]) for a in areas)
    sx, sy = max(sx, big * 3), max(sy, big * 3)
    Hh = 900
    if sx / sy > W / Hh: sy = sx * Hh / W
    else: sx = sy * W / Hh
    cla, clo = (la0 + la1) / 2, (lo0 + lo1) / 2
    LA0, LA1 = cla - sy / 2, cla + sy / 2
    LO0, LO1 = clo - sx / kx / 2, clo + sx / kx / 2
    def pj(a, b): return ((b - LO0) / (LO1 - LO0) * W, (LA1 - a) / (LA1 - LA0) * Hh)
    def inb(a, b, m=1.6):
        dy, dx = (LA1 - LA0) * m, (LO1 - LO0) * m
        return LA0 - dy <= a <= LA1 + dy and LO0 - dx <= b <= LO1 + dx
    mpu = sx * 111320 / W
    views = []
    for a in areas:
        a0, a1, b0, b1, ax, ay = span([GEO[day['rows'][i]['key']] for i in a], kx)
        if ax / ay > W / Hh: ay = ax * Hh / W
        else: ax = ay * W / Hh
        cx, cy = pj((a0 + a1) / 2, (b0 + b1) / 2); w = ax * 111320 / mpu; h = w * Hh / W
        views.append((region((a0 + a1) / 2, (b0 + b1) / 2), f'{cx - w / 2:.1f} {cy - h / 2:.1f} {w:.1f} {h:.1f}', len(a)))
    first = next((v for v in views if v[2] >= 2), views[0])
    o = [f'<svg class="map" viewBox="{first[1]}" data-init="{first[1]}" data-mpu="{mpu:.3f}" data-w="{W}" data-h="{Hh}" role="img" aria-label="Map: {H.escape(region(cla, clo))}">',
         f'<defs><pattern id="ht{day["d"]}{idx}" width="8" height="8" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><line x1="0" y1="0" x2="0" y2="8" class="hatch"/></pattern>'
         f'<pattern id="wt{day["d"]}{idx}" width="10" height="5" patternUnits="userSpaceOnUse"><path d="M0 3 Q2.5 1 5 3 T10 3" class="wave"/></pattern></defs>',
         f'<rect x="-2000" y="-2000" width="{W + 4000}" height="{Hh + 4000}" class="ground"/>']
    feats = [f for f in geo.F if any(inb(a, b) for a, b in f[2])]
    lay = {'water': [], 'park': [], 'bldg': [], 'road2c': [], 'road1c': [], 'road2': [], 'road1': [], 'rail': [], 'metro': [], 'cable': [], 'labels': []}
    for kind, name, ps in feats:
        xy = [pj(a, b) for a, b in ps]; sp = ' '.join(f'{x:.1f},{y:.1f}' for x, y in xy)
        if kind in ('water', 'park', 'bldg'):
            fill = f'url(#wt{day["d"]}{idx})' if kind == 'water' else f'url(#ht{day["d"]}{idx})' if kind == 'park' else ''
            lay[kind].append(f'<polygon points="{sp}" class="{kind}"' + (f' style="fill:{fill}"' if fill else '') + '/>')
            cx, cy = sum(x for x, y in xy) / len(xy), sum(y for x, y in xy) / len(xy)
            if -W < cx < 2 * W and -Hh < cy < 2 * Hh:
                lay['labels'].append(f'<text class="al lod{1 if kind != "bldg" else 2}" x="{cx:.0f}" y="{cy:.0f}" text-anchor="middle">{H.escape(name)}</text>')
        else:
            k = kind if kind != 'road2' else 'road2'
            if kind in ('road1', 'road2'): lay[kind + 'c'].append(f'<polyline points="{sp}" class="{kind}c"/>')
            lay[kind].append(f'<polyline points="{sp}" class="{kind}"/>' + (f'<polyline points="{sp}" class="railt"/>' if kind == 'rail' else ''))
            x, y, ang, ln = label_at(xy)
            if ln > 40 and -W < x < 2 * W and -Hh < y < 2 * Hh:
                lod = 1 if kind in ('road1', 'rail', 'cable') else 2
                lay['labels'].append(f'<text class="sl {kind}l lod{lod}" x="{x:.0f}" y="{y:.0f}" text-anchor="middle" transform="rotate({ang:.0f} {x:.0f} {y:.0f})">{H.escape(name)}</text>')
    for k in ('water', 'park', 'bldg', 'road2c', 'road1c', 'road2', 'road1', 'metro', 'rail', 'cable'): o += lay[k]
    for n, a, b in geo.STATIONS:
        if inb(a, b, 1.2):
            x, y = pj(a, b); o.append(f'<g class="stn sc" data-x="{x:.1f}" data-y="{y:.1f}"><rect x="-7" y="-5" width="14" height="10" rx="2"/><text class="stl lod1" x="0" y="18" text-anchor="middle">{H.escape(n)}</text></g>')
    for n, a, b in geo.LANDMARKS:
        if inb(a, b, 1.2):
            x, y = pj(a, b); o.append(f'<g class="lmk sc" data-x="{x:.1f}" data-y="{y:.1f}"><rect x="-3.5" y="-3.5" width="7" height="7"/><text class="ll lod2" x="8" y="4">{H.escape(n)}</text></g>')
    o += lay['labels']
    # route legs: consecutive non-optional stops in this panel
    seq = [i for i in pn if not day['rows'][i]['opt']]
    legs = []
    for a, b in zip(seq, seq[1:]):
        ka, kb = day['rows'][a]['key'], day['rows'][b]['key']
        if ka == kb: continue
        (x1, y1), (x2, y2) = pj(*GEO[ka]), pj(*GEO[kb])
        far = dist(GEO[ka], GEO[kb]) > 2200 or day['rows'][b]['transit']
        legs.append(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" class="leg{" far" if far else ""}" data-to="{day["rows"][b]["num"]}"/>')
    o += legs
    # pins, offset where several share a spot
    seen = {}
    for i in pn:
        r = day['rows'][i]; x, y = pj(*GEO[r['key']]); c = seen.get(r['key'], 0); seen[r['key']] = c + 1
        ang = c * 1.1; dx, dy = (math.cos(ang) * 26 * (c > 0), math.sin(ang) * 26 * (c > 0))
        o.append(f'<g class="pin sc{" opt" if r["opt"] else ""}" data-n="{r["num"]}" data-x="{x + dx:.1f}" data-y="{y + dy:.1f}" tabindex="0" role="button" aria-label="Stop {r["num"]}: {H.escape(r["txt"])}"><circle r="13"/><text y="4.5" text-anchor="middle">{r["num"]}</text></g>')
    o.append('</svg>')
    if day['d'] in ROUTES:
        gl = '<p class="glinks gnamed">' + ''.join(
            f'<a href="https://www.google.com/maps/dir/?api=1&origin={_q(o)}&destination={_q(d)}' + (f'&waypoints={_q("|".join(w))}' if w else '') + f'&travelmode={m}" target="_blank" rel="noopener">Google Maps: {H.escape(lbl)}</a>'
            for lbl, o, d, w, m in ROUTES[day['d']]) + '</p><p class="gnote">Opens in the Google Maps app with every stop as a named place. Train legs have their own link.</p>'
    else:
        gl = gm_links(day, [i for i in pn if not day['rows'][i]['opt']], 'Whole day')
    if len(areas) > 1 and day['d'] not in ROUTES:
        gl += ''.join(gm_links(day, [i for i in a if not day['rows'][i]['opt']], 'These stops', v[0]) for a, v in zip(areas, views) if v[2] >= 2)
    btns = ''.join(f'<button type="button" class="ab" data-v="{v[1]}"{" aria-pressed=true" if v is first else ""}>{H.escape(v[0])}</button>' for v in views) if len(views) > 1 else ''
    return f'<div class="mp"><div class="mhead"><b>Map</b><span class="abs">{btns}<button type="button" class="ab" data-v="0 0 {W} {Hh}">Zoom out to the whole day</button></span></div><div class="mwin">{"".join(o)}<div class="zoom"><button type="button" class="zin" aria-label="Zoom in">+</button><button type="button" class="zout" aria-label="Zoom out">−</button><button type="button" class="zfit" aria-label="Back to the start view">⤢</button></div><div class="north" aria-hidden="true">▲<br>N</div><div class="scale" aria-hidden="true"><i></i><span>500 m · 7 min</span></div></div>{gl}</div>'

def gm_links(day, idxs, label, area=None):
    pts = []
    for i in idxs:
        c = GEO[day['rows'][i]['key']]
        if not pts or pts[-1][1] != c: pts.append((day['rows'][i]['num'], c))
    if len(pts) < 2: return ''
    parts, out = [], []
    k = 0
    while k < len(pts) - 1:
        ch = pts[k:k + 10]; parts.append(ch); k += len(ch) - 1
    for ch in parts:
        o, d, w = ch[0][1], ch[-1][1], ch[1:-1]
        url = (f'https://www.google.com/maps/dir/?api=1&origin={o[0]},{o[1]}&destination={d[0]},{d[1]}'
               + (('&waypoints=' + '%7C'.join(f'{a},{b}' for _, (a, b) in w)) if w else '') + ('' if label == 'Whole day' else '&travelmode=walking'))
        rng = f'stops {ch[0][0]} to {ch[-1][0]}'
        nm = f'{area} stops' if area else label
        out.append(f'<a href="{url}" target="_blank" rel="noopener">{nm} in Google Maps{", " + rng if len(parts) > 1 else ""}</a>')
    return '<p class="glinks">' + ''.join(out) + '</p>'

def gmaps_dir(a, b, mode):
    return f'https://www.google.com/maps/dir/?api=1&origin={a[0]},{a[1]}&destination={b[0]},{b[1]}&travelmode={mode}'

sections, chips = [], []
for day in days:
    AIR = ('narita', 'haneda', 'hkia', 'mel', 'hkg-transfer', 'plaza-premium')
    near = [i for i, r in enumerate(day['rows']) if r['key'] and r['key'] not in AIR]
    areas = [[i for i in pn if i in near] for pn in day['panels']]
    areas = [a for a in areas if a]
    maps = [panel_svg(day, 0, near, None, 'all', areas)] if len({day['rows'][j]['key'] for j in near}) >= 2 else []
    singles = []
    rows_html = []; prev = None; prevn = 0
    for r in day['rows']:
        num = f'<button type="button" class="rn{" opt" if r["opt"] else ""}" data-n="{r["num"]}" aria-label="Show stop {r["num"]} on the map">{r["num"]}</button>' if r['key'] else '<span class="rn none"></span>'
        acts = ''
        if r['key']:
            c = GEO[r['key']]
            if prev and prev != c and not r['opt']:
                far = dist(prev, c) > 2200 or r['transit']
                acts += f'<a href="{gmaps_dir(prev, c, "transit" if far else "walking")}" target="_blank" rel="noopener">Directions from stop {prevn} · {"train or taxi" if far else str(max(1, round(dist(prev, c) * 1.25 / 75))) + " min walk"}</a>'
            acts += f'<a href="https://www.google.com/maps/search/?api=1&query={c[0]},{c[1]}" target="_blank" rel="noopener">Pin in Maps</a>'
            if not r['opt']: prev, prevn = c, r['num']
        rows_html.append(f'<li class="row{(" " + r["cls"]) if r["cls"] else ""}"><span class="t">{r["t"]}</span>{num}<div class="w"><p class="p">{r["p"]}</p>{f"<p class=n>{r[chr(110)]}</p>" if r["n"] else ""}{f"<p class=racts>{acts}</p>" if acts else ""}</div></li>')
    note = ''
    if not maps:
        note = '<p class="nomap">A travel day: airports and flights, no walking map. Tap a place for its card.</p>'
    elif singles:
        nm = ', '.join(region(*GEO[day['rows'][pn[0]]['key']]) for pn in singles)
        note = f'<p class="nomap">Also today, without a map: {H.escape(nm)}. Use Pin in Maps on those rows.</p>'
    d = day['d']
    sections.append(f'''<section class="mday{day["cls"]}" id="d{d}" data-d="{d}" hidden>
 {day["band"]}<header class="dh"><div class="date"><span class="num">{d}</span><span class="dow">{day["dow"]}<br><span class="where">{day["where"]}</span></span></div><h3>{day["title"]}</h3></header>
 <p class="toit"><a href="{MASTER_URL}#d{d}" target="_blank" rel="noopener">This day in the Itinerary</a></p>
 {"".join(maps)}{note}
 <ol class="rows">{"".join(rows_html)}</ol>
</section>''')
    chips.append(f'<button type="button" class="dchip{day["cls"]}" data-d="{d}"><b>{d}</b><span>{day["dow"][:3]}</span></button>')

extra = r'''
:root{--water:#e9e9e9}
@media (prefers-color-scheme: dark){:root:not([data-theme="light"]){--water:#232323}}
:root[data-theme="dark"]{--water:#232323}
body{overflow-x:hidden}
.mtop{position:sticky;top:env(safe-area-inset-top,0px);z-index:20;background:var(--paper);border-bottom:1.5px solid var(--ink)}
.mtop .in{max-width:52rem;margin:0 auto;padding:.5rem max(16px,env(safe-area-inset-right,0px)) .5rem max(16px,env(safe-area-inset-left,0px))}
.mtop .ttl{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}
.mtop .ttl b{font:800 1.05rem/1.1 "Bricolage","Helvetica Neue",Arial,sans-serif;letter-spacing:-.01em}
.mtop .ttl a{font-size:.78rem;color:var(--ink)}
.dchips{display:flex;gap:.35rem;overflow-x:auto;padding:.45rem 0 .1rem;scrollbar-width:none}.dchips::-webkit-scrollbar{display:none}
.dchip{appearance:none;flex:0 0 auto;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);min-width:2.9rem;padding:.3rem .35rem;display:grid;place-items:center;cursor:pointer;font:inherit;line-height:1}
.dchip b{font-size:1rem}.dchip span{font-size:.62rem;text-transform:uppercase;letter-spacing:.06em;margin-top:.15rem}
.dchip[aria-current="true"]{background:var(--ink);color:var(--paper)}
.dchip.today{outline:2px dashed var(--ink);outline-offset:2px}
.mwrap{max-width:52rem;margin:0 auto;padding-block:1rem 3rem;padding-left:max(16px,env(safe-area-inset-left,0px));padding-right:max(16px,env(safe-area-inset-right,0px))}
.mday .dh{margin-top:.6rem}
.toit{margin:.4rem 0 .8rem;font-size:.85rem}.toit a{color:var(--ink)}
.mp{margin:0 0 1rem}
.mhead{display:flex;justify-content:space-between;align-items:baseline;border:1.5px solid var(--ink);border-bottom:0;padding:.4rem .6rem;font-size:.82rem}
.mhead span{color:var(--mute);font-variant-numeric:tabular-nums}
.mwin{position:relative;border:1.5px solid var(--ink);overflow:hidden;touch-action:none;background:var(--paper);aspect-ratio:760/900;max-height:72vh;max-width:100%}
.mwin svg{display:block;width:100%;height:100%;user-select:none;-webkit-user-select:none;cursor:grab}
.mwin svg.drag{cursor:grabbing}
.ground{fill:var(--paper)}.hatch{stroke:var(--line,#cfcfcf);stroke-width:2}.wave{fill:none;stroke:var(--mute);stroke-width:.8;opacity:.6}
.water{fill:var(--water);stroke:var(--mute);stroke-width:1;vector-effect:non-scaling-stroke}
.park{stroke:var(--mute);stroke-width:1;stroke-dasharray:3 3;vector-effect:non-scaling-stroke}
.bldg{fill:var(--water);stroke:var(--mute);stroke-width:1;vector-effect:non-scaling-stroke}
.road1c{fill:none;stroke:var(--mute);stroke-width:12;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.road1{fill:none;stroke:var(--paper);stroke-width:9;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.road2c{fill:none;stroke:var(--mute);stroke-width:7;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke;opacity:.7}
.road2{fill:none;stroke:var(--paper);stroke-width:4.5;stroke-linecap:round;stroke-linejoin:round;vector-effect:non-scaling-stroke}
.rail{fill:none;stroke:var(--ink);stroke-width:6;vector-effect:non-scaling-stroke}.railt{fill:none;stroke:var(--paper);stroke-width:3.5;stroke-dasharray:12 12;vector-effect:non-scaling-stroke}
.metro{fill:none;stroke:var(--ink);stroke-width:2;stroke-dasharray:1 5;stroke-linecap:round;vector-effect:non-scaling-stroke}
.cable{fill:none;stroke:var(--ink);stroke-width:2.5;stroke-dasharray:10 4 2 4;vector-effect:non-scaling-stroke}
.leg{stroke:var(--ink);stroke-width:4;stroke-dasharray:9 6;stroke-linecap:round;vector-effect:non-scaling-stroke}
.leg.far{stroke-width:2.5;stroke-dasharray:2 7}
.leg.on{stroke-width:7;stroke-dasharray:none}.leg.far.on{stroke-width:4;stroke-dasharray:2 7}
.mwin text{font-family:"Instrument","Helvetica Neue",Arial,sans-serif;paint-order:stroke;stroke:var(--paper);stroke-linejoin:round}
.sl{font-size:calc(11px*var(--k,1));font-weight:600;fill:var(--mute);stroke-width:calc(3.5px*var(--k,1))}
.road1l,.raill{fill:var(--ink)}
.al{font-size:calc(12px*var(--k,1));font-style:italic;font-weight:600;fill:var(--mute);stroke-width:calc(3.5px*var(--k,1))}
.stl{font-size:11px;font-weight:700;fill:var(--ink);text-transform:uppercase;letter-spacing:.04em;stroke-width:3.5px}
.ll{font-size:11.5px;font-weight:700;fill:var(--ink);stroke-width:3.5px}
.stn rect{fill:var(--ink)}.lmk rect{fill:var(--ink)}
.lod2{display:none}.z2 .lod2{display:inline}
.pin{cursor:pointer}.pin circle{fill:var(--paper);stroke:var(--ink);stroke-width:3}.pin text{font:700 13px "Instrument","Helvetica Neue",Arial,sans-serif;fill:var(--ink);stroke:none}
.pin.opt circle{stroke-dasharray:4 3}
.pin.on circle{fill:var(--ink)}.pin.on text{fill:var(--paper)}
.pin:focus{outline:none}.pin:focus-visible circle{stroke-width:5}
.zoom{position:absolute;right:calc(8px + env(safe-area-inset-right,0px) * 0);top:8px;display:flex;flex-direction:column;border:1.5px solid var(--ink);background:var(--paper)}
.zoom button{appearance:none;border:0;background:var(--paper);color:var(--ink);font:700 1.25rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;width:2.75rem;height:2.75rem;cursor:pointer}
.zoom button+button{border-top:1.5px solid var(--ink)}
.zoom button:focus-visible{outline:2px solid var(--ink);outline-offset:-5px}
.north{position:absolute;left:10px;top:8px;font:700 .72rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;text-align:center;background:var(--paper);padding:.3rem .35rem;border:1px solid var(--ink)}
.scale{position:absolute;left:10px;bottom:8px;background:var(--paper);padding:.3rem .45rem;font:600 .7rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;border:1px solid var(--ink)}
.scale i{display:block;height:6px;border:2px solid var(--ink);border-top:0;margin-bottom:.25rem;width:60px}
.mday .rows .row{grid-template-columns:3.4rem 2rem minmax(0,1fr)}
.rn{appearance:none;display:inline-grid;place-items:center;width:1.7rem;height:1.7rem;border-radius:50%;border:2px solid var(--ink);background:var(--paper);color:var(--ink);font:700 .78rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;cursor:pointer;padding:0}
.rn.opt{border-style:dashed}.rn.none{border:0;cursor:default}
.rn[aria-current="true"]{background:var(--ink);color:var(--paper)}
.row.hl{background:var(--water)}
.racts{display:flex;flex-wrap:wrap;gap:.35rem;margin:.35rem 0 0}
.racts a{font-size:.74rem;font-weight:600;color:var(--ink);text-decoration:none;border:1.2px solid var(--ink);padding:.28rem .45rem}
.racts a:hover{background:var(--ink);color:var(--paper)}
.z0 .sl,.z0 .stl,.z0 .ll{display:none}.z0 .al{opacity:.8}
.mhead{flex-wrap:wrap;gap:.4rem}.abs{display:flex;flex-wrap:wrap;gap:.3rem}.ab{appearance:none;border:1.2px solid var(--ink);background:var(--paper);color:var(--ink);font:600 .74rem/1 "Instrument","Helvetica Neue",Arial,sans-serif;padding:.35rem .5rem;cursor:pointer}.ab[aria-pressed="true"]{background:var(--ink);color:var(--paper)}
.glinks{display:flex;flex-wrap:wrap;gap:.35rem;margin:.45rem 0 0}.glinks a{font-size:.78rem;font-weight:600;color:var(--paper);background:var(--ink);text-decoration:none;padding:.4rem .6rem}
.gnote{font-size:.76rem;color:var(--mute);margin:.3rem 0 0}
.nomap{font-size:.86rem;color:var(--mute);border-left:3px solid var(--ink);padding-left:.7rem;margin:.6rem 0 1rem}
.mfoot{font-size:.78rem;color:var(--mute);border-top:1px solid var(--line,#ccc);padding-top:.8rem;margin-top:2rem}
.jt-bar{max-width:52rem}
@media print{.mtop,.zoom{display:none}.mday[hidden]{display:block!important}}
'''

js = r'''
(function(){
 var days=[].slice.call(document.querySelectorAll('.mday')),chips=[].slice.call(document.querySelectorAll('.dchip'));
 function setup(win){
  var svg=win.querySelector('svg'),W=+svg.dataset.w,Hh=+svg.dataset.h,MPU=+svg.dataset.mpu,iv=svg.dataset.init.split(' ').map(Number),vb={x:iv[0],y:iv[1],w:iv[2],h:iv[3]},pts={},pinch=null,last=null,moved=0,MINW=250/MPU;
  var mp=win.closest('.mp'),scaleI=win.querySelector('.scale i'),scaleT=win.querySelector('.scale span');
  function apply(){
   vb.w=Math.max(MINW,Math.min(W*1.15,vb.w));vb.h=vb.w*Hh/W;
   var mx=W*.08,my=Hh*.08;vb.x=Math.max(-mx,Math.min(W+mx-vb.w,vb.x));vb.y=Math.max(-my,Math.min(Hh+my-vb.h,vb.y));
   svg.setAttribute('viewBox',vb.x+' '+vb.y+' '+vb.w+' '+vb.h);
   var k=vb.w/(svg.clientWidth||W);svg.style.setProperty('--k',k);var vm=vb.w*MPU;svg.classList.toggle('z2',vm<1700);svg.classList.toggle('z0',vm>6500);
   svg.querySelectorAll('.sc').forEach(function(g){g.setAttribute('transform','translate('+g.dataset.x+' '+g.dataset.y+') scale('+k+')')});
   var cw=svg.clientWidth||W,S=[[100,'100 m · 1 min'],[500,'500 m · 7 min'],[1000,'1 km · 14 min'],[5000,'5 km'],[10000,'10 km']],px=0,lab='';
   for(var q=0;q<S.length;q++){px=S[q][0]/MPU*cw/vb.w;lab=S[q][1];if(px>=40)break}
   scaleI.style.width=Math.round(px)+'px';scaleT.textContent=lab;
  }
  function zoomAt(f,cx,cy){var nw=Math.max(MINW,Math.min(W*1.15,vb.w*f));var r=nw/vb.w;vb.x=cx-(cx-vb.x)*r;vb.y=cy-(cy-vb.y)*r;vb.w=nw;apply()}
  function toSvg(e){var r=svg.getBoundingClientRect();return {x:vb.x+(e.clientX-r.left)/r.width*vb.w,y:vb.y+(e.clientY-r.top)/r.height*vb.h}}
  win.querySelector('.zin').onclick=function(){zoomAt(.6,vb.x+vb.w/2,vb.y+vb.h/2)};
  win.querySelector('.zout').onclick=function(){zoomAt(1/.6,vb.x+vb.w/2,vb.y+vb.h/2)};
  function setv(t){var a=t.split(' ').map(Number);vb={x:a[0],y:a[1],w:a[2],h:a[3]};apply()}
  win.querySelector('.zfit').onclick=function(){setv(iv.join(' '))};
  mp.querySelectorAll('.ab').forEach(function(b){b.onclick=function(){mp.querySelectorAll('.ab').forEach(function(x){x.setAttribute('aria-pressed',x===b)});setv(b.dataset.v)}});
  svg.addEventListener('wheel',function(e){e.preventDefault();var p=toSvg(e);zoomAt(e.deltaY>0?1.15:1/1.15,p.x,p.y)},{passive:false});
  svg.addEventListener('pointerdown',function(e){svg.setPointerCapture(e.pointerId);pts[e.pointerId]={x:e.clientX,y:e.clientY};moved=0;var ids=Object.keys(pts);
   if(ids.length===2){var a=pts[ids[0]],b=pts[ids[1]];pinch={d:Math.hypot(a.x-b.x,a.y-b.y),w:vb.w}}else{last={x:e.clientX,y:e.clientY}}});
  svg.addEventListener('pointermove',function(e){if(!pts[e.pointerId])return;pts[e.pointerId]={x:e.clientX,y:e.clientY};var ids=Object.keys(pts),r=svg.getBoundingClientRect();
   if(ids.length===2&&pinch){var a=pts[ids[0]],b=pts[ids[1]],d=Math.hypot(a.x-b.x,a.y-b.y);var mid=toSvg({clientX:(a.x+b.x)/2,clientY:(a.y+b.y)/2});zoomAt((pinch.w*pinch.d/d)/vb.w,mid.x,mid.y);moved+=5}
   else if(last){var dx=e.clientX-last.x,dy=e.clientY-last.y;moved+=Math.abs(dx)+Math.abs(dy);if(moved>4)svg.classList.add('drag');vb.x-=dx/r.width*vb.w;vb.y-=dy/r.height*vb.h;last={x:e.clientX,y:e.clientY};apply()}});
  function up(e){delete pts[e.pointerId];if(Object.keys(pts).length<2)pinch=null;if(!Object.keys(pts).length){last=null;svg.classList.remove('drag')}}
  svg.addEventListener('pointerup',up);svg.addEventListener('pointercancel',up);
  svg.addEventListener('click',function(e){if(moved>6){e.stopPropagation();return}var g=e.target.closest('.pin');if(g)select(+g.dataset.n,true)},true);
  svg.addEventListener('keydown',function(e){var g=e.target.closest('.pin');if(g&&(e.key==='Enter'||e.key===' ')){e.preventDefault();select(+g.dataset.n,true)}});
  win.focusOn=function(x,y){if(vb.w*MPU>2500){vb.w=1500/MPU}vb.x=x-vb.w/2;vb.y=y-vb.w*Hh/W/2;apply()};
  win.redraw=apply;apply();
 }
 document.querySelectorAll('.mwin').forEach(setup);
 window.addEventListener('resize',function(){document.querySelectorAll('.mwin').forEach(function(w){w.redraw&&w.redraw()})});
 var curDay=null;
 function select(n,fromMap){
  var sec=curDay;if(!sec)return;
  sec.querySelectorAll('.pin').forEach(function(g){g.classList.toggle('on',+g.dataset.n===n)});
  sec.querySelectorAll('.leg').forEach(function(l){l.classList.toggle('on',+l.dataset.to===n)});
  sec.querySelectorAll('.rn').forEach(function(b){b.setAttribute('aria-current',+b.dataset.n===n?'true':'false')});
  sec.querySelectorAll('.row').forEach(function(r){r.classList.remove('hl')});
  var b=sec.querySelector('.rn[data-n="'+n+'"]');
  if(fromMap&&b){var row=b.closest('.row');row.classList.add('hl');row.scrollIntoView({block:'nearest',behavior:'smooth'})}
  if(!fromMap){var g=sec.querySelector('.pin[data-n="'+n+'"]');if(g){var win=g.closest('.mwin');win.focusOn(+g.dataset.x,+g.dataset.y);win.scrollIntoView({block:'nearest',behavior:'smooth'})}}
 }
 document.addEventListener('click',function(e){var b=e.target.closest('.rn[data-n]');if(b)select(+b.dataset.n,false)});
 function show(d){
  days.forEach(function(s){s.hidden=+s.dataset.d!==d;if(!s.hidden)curDay=s});
  chips.forEach(function(c){c.setAttribute('aria-current',+c.dataset.d===d?'true':'false');if(+c.dataset.d===d)c.scrollIntoView({inline:'center',block:'nearest'})});
  try{history.replaceState(null,'','#d'+d)}catch(e){}
  if(curDay)curDay.querySelectorAll('.mwin').forEach(function(w){w.redraw&&w.redraw()});
  window.scrollTo(0,0);
 }
 chips.forEach(function(c){c.onclick=function(){show(+c.dataset.d)}});
 var n=new Date(),iso=n.getFullYear()*10000+(n.getMonth()+1)*100+n.getDate(),start=17;
 if(iso>=20261016&&iso<=20261031){var dd=iso-20261000;start=Math.min(30,dd);var c=document.querySelector('.dchip[data-d="'+dd+'"]');if(c)c.classList.add('today')}
 var h=/^#d(\d+)$/.exec(location.hash);if(h&&document.getElementById('d'+h[1]))start=+h[1];
 show(start);
 window.addEventListener('hashchange',function(){var h=/^#d(\d+)$/.exec(location.hash);if(h&&document.getElementById('d'+h[1]))show(+h[1])});
})();
'''

sheet = tpl[tpl.index('<aside class="sheet"'):tpl.index('</aside>') + 8]
i = tpl.index("(function(){\n var P=/*PLACES*/"); j = tpl.index('})();', i) + 5
cardjs = tpl[i:j].replace('/*PLACES*/', json.dumps(P, ensure_ascii=False).replace('</', '<\\/'))

body = f'''<div class="mtop"><div class="in"><div class="ttl"><b>Map Itinerary</b><a href="{MASTER_URL}" target="_blank" rel="noopener">Open the Itinerary</a></div>
<div class="dchips" role="tablist" aria-label="Choose a day">{"".join(chips)}</div></div></div>
<main class="mwrap">
{"".join(sections)}
<p class="mfoot">J&amp;HK Map View, companion to the Japan &amp; Hong Kong Master Itinerary V2, built from its day plans. Maps are drawn by hand from approximate coordinates to get your bearings: streets and landmarks are close, not exact. Pinch or use + and − to zoom; smaller streets and landmark names appear as you zoom in. Tap a number to find it, tap a place name for its card. Walk and Pin in Maps need a connection; the maps, plans and cards work offline once saved.</p>
</main>
{sheet}'''

def page(head_extra='', tail=''):
    h = (f'<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
         f'<title>Map Itinerary</title>\n<meta name="claude:viewport-fit-sides" content="cover">\n{head_extra}<style>{style}{extra}</style>\n</head>\n<body>\n{body}\n<script>\n{cardjs}\n{js}\n</script>\n{tail}</body>\n</html>\n')
    h = apptools.inject(h, 'map', 'none.pdf', OFF, 'Map View')
    return re.sub(r'<a class="jt-dl".*?</a>', '', h, count=1, flags=re.S)

os.makedirs(os.path.join(HERE, 'out'), exist_ok=True)
open(os.path.join(HERE, 'out', 'jhk-map.html'), 'w', encoding='utf-8').write(page())

DST = os.path.join(REPO, 'map'); os.makedirs(DST, exist_ok=True)
head = ('<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#000000">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="J&amp;HK Map View">\n<link rel="manifest" href="manifest.webmanifest">\n'
        '<link rel="apple-touch-icon" href="icon-180.png">\n<link rel="icon" type="image/png" href="icon-192.png">\n')
sw = "<script>if('serviceWorker' in navigator){addEventListener('load',function(){navigator.serviceWorker.register('sw.js').catch(function(){})})}</script>\n"
html = page(head, sw); ver = hashlib.md5(html.encode()).hexdigest()[:10]
open(os.path.join(DST, 'index.html'), 'w', encoding='utf-8').write(html)
json.dump({"name": "J&HK Map View", "short_name": "J&HK Map View", "start_url": "./", "scope": "./", "display": "standalone",
           "background_color": "#ffffff", "theme_color": "#000000",
           "icons": [{"src": "icon-192.png", "sizes": "192x192", "type": "image/png"}, {"src": "icon-512.png", "sizes": "512x512", "type": "image/png"}]},
          open(os.path.join(DST, 'manifest.webmanifest'), 'w'), indent=1)
open(os.path.join(DST, 'sw.js'), 'w').write(apptools.sw('mv-' + ver, OFF))

# icon: white tile, a folded black map with a dashed route and a pin, leg band underneath
fonts = ''.join(re.findall(r'@font-face\s*\{.*?\}', style, flags=re.S))
pats = re.search(r'\.pat-k\{[^}]*\}', style).group(0) + re.search(r'\.pat-h\{[^}]*\}', style).group(0)
ic = f'''<!doctype html><html><head><meta charset="utf-8"><style>{fonts}{pats}
html,body{{margin:0}}.i{{width:512px;height:512px;background:#fff;position:relative;overflow:hidden;font-family:"Bricolage"}}
.t{{position:absolute;left:38px;top:300px;font-weight:800;font-size:92px;line-height:1;letter-spacing:-3px}}
.s{{position:absolute;left:42px;top:398px;font-family:"Instrument";font-size:30px}}
.band{{position:absolute;left:0;right:0;bottom:0;height:40px;display:flex}}.band i{{flex:1;display:block}}
.ps{{background:#000}}.pg{{background:linear-gradient(#fff 33%,#000 33% 67%,#fff 67%)}}
</style></head><body><div class="i">
<svg width="512" height="300" viewBox="0 0 512 300" style="position:absolute;left:0;top:0">
<polygon points="70,70 190,40 320,70 442,40 442,250 320,280 190,250 70,280" fill="#000"/>
<line x1="190" y1="40" x2="190" y2="250" stroke="#fff" stroke-width="6"/><line x1="320" y1="70" x2="320" y2="280" stroke="#fff" stroke-width="6"/>
<path d="M110 230 C160 200 170 140 230 150 S300 210 350 160 S390 110 400 100" fill="none" stroke="#fff" stroke-width="10" stroke-dasharray="20 14" stroke-linecap="round"/>
<circle cx="110" cy="230" r="16" fill="#fff"/>
<path d="M400 120 C380 92 372 80 372 66 a28 28 0 0 1 56 0 c0 14 -8 26 -28 54z" fill="#fff" stroke="#000" stroke-width="6"/><circle cx="400" cy="66" r="10" fill="#000"/>
</svg>
<div class="t">Map</div><div class="s">Japan &amp; Hong Kong</div>
<div class="band"><i class="ps"></i><i class="pat-k"></i><i class="pg"></i><i class="pat-h"></i></div></div></body></html>'''
open('/tmp/micon.html', 'w', encoding='utf-8').write(ic)
from playwright.async_api import async_playwright
async def go():
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={'width': 512, 'height': 512})
        await pg.goto('file:///tmp/micon.html'); await pg.wait_for_timeout(400)
        await pg.screenshot(path=os.path.join(DST, 'icon-512.png')); await b.close()
asyncio.run(go())
from PIL import Image
im = Image.open(os.path.join(DST, 'icon-512.png')).convert('RGB')
im.resize((192, 192), Image.LANCZOS).save(os.path.join(DST, 'icon-192.png'))
im.resize((180, 180), Image.LANCZOS).save(os.path.join(DST, 'icon-180.png'))
print('map written', ver, {d['d']: (len(d['panels']), sum(1 for r in d['rows'] if r['key'])) for d in days})
