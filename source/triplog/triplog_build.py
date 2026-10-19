import html, sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from triplog_data import DAYS
E = html.escape
GH = 'https://thestartupstudiodeveloper.github.io/japan-trip/'
LAB = {'done': 'Done', 'changed': 'Plan changed', 'plan': 'As planned'}
def ul(xs): return '<ul>' + ''.join(f'<li>{E(x)}</li>' for x in xs) + '</ul>'
cards = []
for d in DAYS:
    right = 'What happened' if d['status'] == 'done' else 'New plan'
    cards.append(f'''<article class="day s-{d['status']}"><header><h2><span>{E(d['d'])}</span> {E(d['title'])}</h2><b class="st">{LAB[d['status']]}</b></header>
<div class="cols"><section><h3>Original plan</h3>{ul(d['orig'])}</section><section><h3>{right}</h3>{ul(d['actual'])}</section></div>
<section class="ch"><h3>What changed</h3>{ul(d['changes'])}</section></article>''')
page = f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<title>J&amp;HK Trip Log</title><style>
:root{{--ink:#000;--paper:#fff;--mute:#555}}*{{box-sizing:border-box}}
body{{margin:0;background:var(--paper);color:var(--ink);font:15px/1.45 -apple-system,BlinkMacSystemFont,"Helvetica Neue",Arial,sans-serif}}
main{{max-width:52rem;margin:0 auto;padding:1.4rem 16px 3rem}}
h1{{font-size:2rem;line-height:1.05;margin:.2rem 0 .4rem;letter-spacing:-.02em}}
.lede{{color:var(--mute);margin:0 0 1rem}}
.nav{{display:flex;flex-wrap:wrap;gap:.45rem;margin:0 0 1.4rem}}
.nav a{{font-weight:600;font-size:.85rem;color:var(--ink);text-decoration:none;border:1.5px solid var(--ink);padding:.45rem .65rem}}.nav a:hover{{background:var(--ink);color:var(--paper)}}
.day{{border-top:3px solid var(--ink);padding:.8rem 0 1.2rem}}
.day header{{display:flex;justify-content:space-between;align-items:baseline;gap:.6rem}}
h2{{font-size:1.2rem;margin:0}}h2 span{{display:inline-block;background:var(--ink);color:var(--paper);padding:.1rem .4rem;margin-right:.3rem;font-size:.95rem}}
.st{{font-size:.72rem;border:1.5px solid var(--ink);padding:.2rem .4rem;white-space:nowrap}}.s-done .st{{background:var(--ink);color:var(--paper)}}.s-changed .st{{border-style:dashed}}
.cols{{display:grid;grid-template-columns:1fr 1fr;gap:1rem;margin-top:.6rem}}@media (max-width:640px){{.cols{{grid-template-columns:1fr}}}}
h3{{font-size:.75rem;text-transform:uppercase;letter-spacing:.08em;margin:.4rem 0 .3rem;color:var(--mute)}}
ul{{margin:0;padding-left:1.1rem}}li{{margin:.15rem 0}}
.cols section:first-child li{{color:var(--mute)}}
.ch{{margin-top:.6rem;border-left:3px solid var(--ink);padding-left:.7rem}}
.back{{position:sticky;top:0;z-index:9;display:block;background:var(--ink,#000);color:var(--paper,#fff);font:600 .95rem/1 var(--body,system-ui);padding:calc(.8rem + env(safe-area-inset-top,0px)) 16px .8rem;text-decoration:none;margin:0 -16px 1rem}}
</style></head><body><main><a class="back" href="{GH}">&larr; Back to the itinerary</a>
<h1>Trip log</h1><p class="lede">The original plan, frozen on Fri 16 Oct before the trip, against what actually happened and what changed. Updated as we go.</p>
<nav class="nav"><a href="{GH}">Live itinerary</a><a href="{GH}baseline/original-plan/">Original plan (full page)</a></nav>
{''.join(cards)}
</main></body></html>'''
out = sys.argv[1] if len(sys.argv) > 1 else 'out'
os.makedirs(out, exist_ok=True)
open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(page)
print('ok', len(page))
