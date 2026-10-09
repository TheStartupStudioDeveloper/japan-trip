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

blocks = []
for Lg in LEGS:
    rows = ''.join(
        f'<div class="grow"><a class="gday" href="#{d}">{E(lbl)}</a>' +
        ''.join(f'<div class="gc{" gf" if s=="f" else " gb" if s=="b" else ""}{" ge" if not t else ""}">{lk(t)}</div>' for t, s in cells) +
        '</div>' for d, lbl, cells in Lg['days'])
    shift = ''.join(f'<li>{lk(x)}</li>' for x in Lg['shift'])
    ext = ''.join(f'<a href="{EXTRAS}#{k}">{E(n)}</a>' for k, n in Lg['extras'])
    blocks.append(f'''<article class="sl">
 <i class="pat pat-{Lg["pat"]} slband"></i>
 <div class="slh"><p class="kanji">{Lg["kanji"]}</p><div>
  <p class="legno">{Lg["leg"]} · {E(Lg["dates"])} · {E(Lg["nights"])} · {E(Lg["sun"])}</p>
  <h3>{E(Lg["name"])}</h3>
  <p class="meta">{pl(Lg["hotel"], {p["key"]: p for p in PLACES}[Lg["hotel"]]["n"])}</p></div></div>
 <div class="grid"><div class="ghead"><span></span><span>Morning</span><span>Afternoon</span><span>Evening</span></div>{rows}</div>
 <div class="slf">
  <div><h4>Can shift</h4><ul>{shift}</ul></div>
  <div class="screen"><h4>Extras</h4><p class="xt">{ext}</p></div>
 </div>
</article>''')

section = f'''<section class="summ" id="summary">
 <h2 class="sec">Itinerary Summary</h2>
 <p class="sum">The trip in four stays: what is fixed, and what can move. Tap any underlined name for its card.</p>
 <p class="skey"><span><i class="kf"></i>Fixed or booked</span><span><i class="kb"></i>Still to book</span><span><i class="kx"></i>Flexible</span></p>
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
