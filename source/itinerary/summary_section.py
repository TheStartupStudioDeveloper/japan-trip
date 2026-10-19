# Itinerary Summary: replaces the old four legs page. Run from build.py after linking (names are linked here).
# Data in summary_data.py. Expects: out, E, P-free (uses places.py for card names).
import re as _r2s, html as _Hs
from summary_data import LEGS, EXTRAS
E = _Hs.escape
re = _r2s
def pl(k, label):
    return f'<a class="pl" href="#" role="button" data-p="{k}">{E(label)}</a>'
from places import PLACES
EXTRA = {'Melbourne': 'mel', 'Narita': 'narita', "N'EX": 'nex', 'Hong Kong stopover': 'hkg-transfer', 'Nozomi': 'shinkansen',
         'Crosta': 'crosta', 'Kasuga': 'kasuga', 'Horie': 'horie', 'Nishiki': 'nishiki', 'Yasaka': 'yasaka', 'East Gardens': 'eastgardens',
         'Land 14:25': 'hkia', 'Kamakura': 'kamakura'}
AL = sorted([(a.replace('&#x27;', "'").replace('&amp;', '&'), p['key']) for p in PLACES for a in p['aliases']] + list(EXTRA.items()), key=lambda x: -len(x[0]))
def lk(t):
    used = [None] * len(t); spans = []
    for a, k in AL:
        for mm in re.finditer(r'(?<![\w])' + re.escape(a) + r'(?![\w])', t):
            if all(u is None for u in used[mm.start():mm.end()]):
                spans.append((mm.start(), mm.end(), k))
                for i in range(mm.start(), mm.end()): used[i] = 1
    spans.sort(); o = ''; p0 = 0
    for a0, a1, k in spans:
        o += E(t[p0:a0]) + pl(k, t[a0:a1]); p0 = a1
    return o + E(t[p0:])


def _part(t, prev):
    m = re.match(r'(\d\d):(\d\d)', t or '')
    if not m:
        tl = (t or '').lower()
        if 'morning' in tl or 'early' in tl: return 'Morning'
        if 'afternoon' in tl or 'arvo' in tl or 'lunch' in tl: return 'Afternoon'
        if 'evening' in tl or 'late' in tl or 'night' in tl: return 'Evening'
        return prev or 'Morning'
    h = int(m.group(1))
    return 'Morning' if h < 12 else 'Afternoon' if h < 17 else 'Evening'
def _short(p):
    p = re.sub(r'^(Optional|Idea):\s*', '', p.strip())
    p = re.split(r'[,:(]| then ', p)[0].strip()
    return p if len(p) <= 30 else p[:29].rsplit(' ', 1)[0] + '\u2026'
def strip(dn):
    rs = (D.get(dn) or {}).get('rows') or []
    if not rs:
        cells = next((c for L in LEGS for dd, _, c in L['days'] if dd == f'd{dn}'), [])
        return ''.join(f'<span class="sb{" sbf" if st == "f" else ""}"><b>{pt}</b>{lk(t)}</span>' for (t, st), pt in zip(cells, ('Morning', 'Afternoon', 'Evening')) if t)
    o, prev = [], None
    for r in rs:
        t, pp, st = r[0], r[1], (r[3] if len(r) > 3 else '')
        pt = _part(t, prev)
        if pt != prev:
            o.append(f'<span class="gpt">{pt}</span>'); prev = pt
        cls = ' sbf' if st == 'B' else ' sbb' if st == 'TB' else ' sbd' if st == 'd' else ''
        if re.match(r'(Optional|Idea)', pp.strip()): cls += ' sbo'
        o.append(f'<span class="sb{cls}"><b>{E(t)}</b>{lk(_short(pp))}</span>')
    return ''.join(o)

blocks = []
for Lg in LEGS:
    rows = ''.join(
        f'<div class="grow2"><a class="gday" href="#{d}">{E(lbl)}</a><div class="gstrip">{strip(int(d[1:]))}</div></div>' for d, lbl, cells in Lg['days'])
    shift = ''.join(f'<li>{lk(x)}</li>' for x in Lg['shift'])
    ext = ''.join(f'<a href="{EXTRAS}#{k}">{E(n)}</a>' for k, n in Lg['extras'])
    blocks.append(f'''<article class="sl">
 <i class="pat pat-{Lg["pat"]} slband"></i>
 <div class="slh"><p class="kanji">{Lg["kanji"]}</p><div>
  <p class="legno">{Lg["leg"]} · {E(Lg["dates"])} · {E(Lg["nights"])} · {E(Lg["sun"])}</p>
  <h3>{E(Lg["name"])}</h3>
  <p class="meta">{pl(Lg["hotel"], {p["key"]: p for p in PLACES}[Lg["hotel"]]["n"])}</p></div></div>
 <div class="grid">{rows}</div>
 <div class="slf">
  <div><h4>Can shift</h4><ul>{shift}</ul></div>
  <div class="screen"><h4>Extras</h4><p class="xt">{ext}</p></div>
 </div>
</article>''')

section = f'''<section class="summ" id="summary">
 <h2 class="sec">Itinerary Summary</h2>
 <p class="sum">The trip in four stays, one block per activity in time order: what is fixed, and what can move. Tap any underlined name for its card.</p>
 <p class="skey"><span><i class="kx kfx"></i>Fixed or booked</span><span><i class="kb"></i>Still to book</span><span><i class="kx"></i>Flexible</span><span><i class="kx kd"></i>Done</span></p>
 {''.join(blocks)}
</section>'''

css = '''<style>
.summ .sum{max-width:40rem}
.skey{display:flex;flex-wrap:wrap;gap:.4rem 1.2rem;margin-top:.8rem;font-size:.82rem;color:var(--mute)}.skey span{display:flex;align-items:center;gap:.4rem}
.skey i{width:1.1rem;height:.8rem;border:1.5px solid var(--ink)}.skey .kf{background:var(--ink)}.skey .kb{border-style:dashed}
.sl{margin-top:1.6rem;border:1.5px solid var(--ink)}.slband{height:12px}.sl>*:not(.slband){margin-left:1rem;margin-right:1rem}
.slh{display:flex;gap:.9rem;align-items:center;margin-top:.9rem}
.slh .kanji{writing-mode:horizontal-tb;font-size:2.6rem;line-height:1;letter-spacing:0;white-space:nowrap}
.slh h3{font:800 1.45rem/1.1 var(--display);letter-spacing:-.02em;margin-top:.1rem}.slh .legno{font-size:.78rem;font-weight:600}.slh .meta{margin-top:.15rem;font-size:.9rem}
.grid{margin-top:.9rem;display:grid;gap:3px}
.ghead,.grow{display:grid;grid-template-columns:3.4rem repeat(3,1fr);gap:3px}
.ghead span{font:700 .64rem var(--body);text-transform:uppercase;letter-spacing:.06em;color:var(--mute);padding:0 .1rem}
.gday{font:700 .82rem/1.15 var(--display);text-decoration:none;padding:.35rem 0;align-self:start}
.gc{font-size:.74rem;line-height:1.25;padding:.35rem .4rem;border:1.5px solid var(--line);min-height:2.4rem}
.gc .pl{border-bottom-width:1px}.gc.gf .pl{border-bottom-color:var(--paper)}.gc.gf{background:var(--ink);color:var(--paper);border-color:var(--ink);font-weight:600}.gc.gf .pl{border-bottom-color:var(--paper)}.gc.gf .pl:hover,.gc.gf .pl[aria-expanded="true"]{background:var(--paper);color:var(--ink)}
.gc.gb{border:1.5px dashed var(--ink)}
.gc.ge{border-color:transparent}
.slf{display:grid;gap:.9rem;margin-top:1rem;margin-bottom:1.1rem;font-size:.86rem}
.slf h4{font:700 .68rem var(--body);text-transform:uppercase;letter-spacing:.06em;margin-bottom:.25rem}
.slf li{padding-left:.9rem;position:relative;color:var(--mute);margin-top:.15rem}.slf li::before{content:"";position:absolute;left:0;top:.5em;width:.4rem;height:.4rem;background:var(--ink)}
.bk{display:flex;flex-wrap:wrap;gap:.3rem}.bk .tag{margin:0}.none{color:var(--mute)}
.xt{display:flex;flex-wrap:wrap;gap:.3rem}.xt a{font:700 .76rem var(--body);text-decoration:none;border:1.5px solid var(--ink);padding:.15rem .45rem}
.grow2{display:grid;grid-template-columns:3.4rem minmax(0,1fr);gap:3px;padding:.35rem 0;border-top:1px solid var(--line)}
.gstrip{display:flex;flex-wrap:wrap;gap:4px;align-items:stretch}
.gpt{flex:0 0 auto;align-self:center;font:700 .56rem var(--body);text-transform:uppercase;letter-spacing:.08em;color:var(--mute);padding:0 .1rem 0 .3rem;border-left:2px solid var(--ink)}
.gpt:first-child{border-left:0;padding-left:0}
.sb{display:inline-flex;flex-direction:column;font-size:.72rem;line-height:1.15;padding:.2rem .38rem .24rem;border:1.5px solid var(--line);background:var(--paper);max-width:100%}
.sb b{font:600 .62rem/1.1 var(--body);color:var(--mute);letter-spacing:.02em;margin-bottom:.1rem}
.sb .pl{border-bottom-width:1px}
.sb.sbf{border-color:var(--ink);border-left-width:5px}.sb.sbf b{color:var(--ink);font-weight:800}
.sb.sbb{border:1.5px dashed var(--ink)}
.sb.sbo{color:var(--mute)}
.sb.sbd{opacity:.55}.sb.sbd b::after{content:"  \\2713";color:var(--ink);font-weight:800}
.skey .kfx{border-left-width:5px}.skey .kd{opacity:.55;border-color:var(--line)}
@media (min-width:640px){.grow2{grid-template-columns:4.2rem minmax(0,1fr)}.sb{font-size:.82rem}}
@media print{.grow2{grid-template-columns:13mm 1fr;padding:.6mm 0}.sb{font-size:7.2pt;padding:.5mm 1mm;border-width:1px}.sb.sbf{border-left-width:2mm}.gpt{font-size:5.6pt}}
@media (min-width:640px){
 .sl>*:not(.slband){margin-left:1.5rem;margin-right:1.5rem}
 .ghead,.grow{grid-template-columns:4.2rem repeat(3,1fr)}.gc{font-size:.84rem}.gday{font-size:.92rem}
 .slf{grid-template-columns:3fr 1fr;gap:1.5rem}
}
@media print{
 .summ{break-before:page}.summ .sec{margin:0}.summ .sum{font-size:8.6pt;display:inline}.skey{font-size:7.2pt;margin-top:1mm}.skey i{width:4mm;height:2.6mm}
 .sl{margin-top:3.2mm;break-inside:avoid}.slband{height:2.4mm}.sl>*:not(.slband){margin-left:3.5mm;margin-right:3.5mm}
 .slh{margin-top:1.2mm;gap:3mm}.slh .kanji{font-size:20pt}.slh h3{font-size:12pt;display:inline;margin-right:2mm}.slh .legno{font-size:7pt}.slh .meta{font-size:7.4pt;display:inline;margin:0}
 .slh>div{display:flex;flex-wrap:wrap;align-items:baseline;column-gap:2mm}.slh .legno{order:2;font-weight:400;color:var(--mute)}.slh .meta{order:3}
 .grid{margin-top:1.2mm;gap:.5mm}.ghead,.grow{grid-template-columns:13mm repeat(3,1fr);gap:.5mm}
 .ghead span{font-size:5.8pt}.gday{font-size:8.2pt;padding:.9mm 0}.gc{font-size:7.7pt;padding:.9mm 1.3mm;min-height:0;line-height:1.18;border-width:1px}.gc.gb{border-width:1px}
 .slf{grid-template-columns:1fr;gap:4mm;margin:1.6mm 3.5mm 2mm;font-size:7.6pt;line-height:1.25}.slf h4{font-size:5.8pt;margin-bottom:.3mm}.slf li{margin-top:.15mm}
 .bk{gap:.8mm}.bk .tag{font-size:6pt;padding:.4mm 1mm}
}
</style>'''
_a = out.index('<section class="legsprint">'); _b = out.index('</section>', _a) + len('</section>')
out = out[:_a] + section + out[_b:]
out = out.replace('</style>', css.replace('<style>', '').replace('</style>', '') + '</style>', 1)
out = out.replace('<h2 class="sec">The fortnight at a glance</h2>', '<h2 class="sec">Trip calendar</h2>')
out = out.replace('<a class="more" href="#list">Checklist</a>', '<a class="more" href="#summary">Summary</a><a class="more" href="#list">Checklist</a>', 1)
