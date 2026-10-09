# Saves a steady state: a frozen, date-stamped copy of all four apps, with its own permanent link.
# Usage: python3 source/snapshot.py "Short note" [repo dir]
#   Copies the live Itinerary, Extras, Weather and Expenses (pages and PDFs) into archive/ssN-YYYY-MM-DD/,
#   turns off service workers and Save offline in the copies, adds a banner, rebuilds archive/index.html,
#   and records it in archive/versions.json. Then commit, tag steady-ssN-YYYY-MM-DD and push.
import sys, os, re, json, shutil, datetime
NOTE = sys.argv[1] if len(sys.argv) > 1 else ''
REPO = sys.argv[2] if len(sys.argv) > 2 else '/home/claude/japan-trip'
BASE = 'https://thestartupstudiodeveloper.github.io/japan-trip/'
ARCH = os.path.join(REPO, 'archive'); os.makedirs(ARCH, exist_ok=True)
VJ = os.path.join(ARCH, 'versions.json')
versions = json.load(open(VJ)) if os.path.exists(VJ) else []
n = len(versions) + 1
now = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=11)))  # Melbourne, AEDT
slug = f'ss{n}-{now:%Y-%m-%d}'
label = f'Steady state {n}'
when = f'{now.day} {now:%b %Y}, {now:%H:%M}'
DST = os.path.join(ARCH, slug); os.makedirs(DST)
APPS = [('', 'Itinerary', 'Japan-Hong-Kong-Master-Itinerary-V2.pdf'), ('extras', 'Extras', 'JHK-Extras.pdf'),
        ('weather', 'Weather', 'JHK-Weather.pdf'), ('expenses', 'Expenses', 'JHK-Expenses.pdf')]
banner_css = ('<style>.ss-banner{background:#000;color:#fff;font:600 .82rem/1.35 "Instrument","Helvetica Neue",Arial,sans-serif;'
              'padding:.55rem 1.1rem;text-align:center}.ss-banner a{color:#fff}@media print{.ss-banner{display:none}}</style>')
kept = []
for app, name, pdf in APPS:
    src = os.path.join(REPO, app); out = os.path.join(DST, app or 'itinerary'); os.makedirs(out, exist_ok=True)
    h = open(os.path.join(src, 'index.html'), encoding='utf-8').read()
    h = re.sub(r"<script>if\('serviceWorker' in navigator\).*?</script>", '', h, flags=re.S)   # no service worker
    h = re.sub(r'<link rel="manifest"[^>]*>', '', h)
    h = re.sub(r'<button type="button" class="jt-off">.*?</button>', '', h, flags=re.S)       # no Save offline
    h = re.sub(r'<meta name="apple-mobile-web-app-title" content="[^"]*">', '', h)
    live = BASE + (app + '/' if app else '')
    ban = (f'<div class="ss-banner">{label}, saved {when}. A frozen copy for reference. '
           f'<a href="{live}">Open the live {name}</a> · <a href="../">All saved versions</a></div>')
    h = re.sub(r'(<body[^>]*>)', lambda m: m.group(1) + banner_css + ban, h, count=1)
    h = h.replace('<title>', '<title>' + label + ' · ', 1)
    open(os.path.join(out, 'index.html'), 'w', encoding='utf-8').write(h)
    for f in os.listdir(src):
        if f.endswith('.pdf') or f.startswith('icon-'):
            shutil.copy(os.path.join(src, f), os.path.join(out, f))
    kept.append(dict(app=name, path=(app or 'itinerary') + '/', pdf=pdf if os.path.exists(os.path.join(out, pdf)) else None))
versions.append(dict(n=n, slug=slug, label=label, when=when, date=f'{now:%Y-%m-%d}', note=NOTE, apps=kept))
json.dump(versions, open(VJ, 'w'), indent=1, ensure_ascii=False)

# archive index
def esc(s): return s.replace('&', '&amp;').replace('<', '&lt;')
rows = ''
for v in reversed(versions):
    links = ' '.join(f'<a href="{v["slug"]}/{a["path"]}">{a["app"]}</a>' + (f' <a class="pdf" href="{v["slug"]}/{a["path"]}{a["pdf"]}">PDF</a>' if a['pdf'] else '') for a in v['apps'])
    rows += f'<li><div class="vh"><b>{esc(v["label"])}</b><span>{esc(v["when"])}</span></div>{f"<p>{esc(v["note"])}</p>" if v["note"] else ""}<p class="ln">{links}</p></li>'
idx = f'''<!doctype html><html lang="en-AU"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow"><title>Saved Versions</title><style>
:root{{color-scheme:light}}body{{margin:0;background:#fff;color:#000;font:400 1rem/1.5 "Helvetica Neue",Arial,sans-serif}}
.w{{max-width:44rem;margin:0 auto;padding:2.2rem 1.1rem}}h1{{font-size:2.2rem;line-height:1;margin:0 0 .4rem;letter-spacing:-.02em}}
.sub{{color:#444;margin:0 0 1.6rem}}.live a,.ln a{{display:inline-block;margin:.2rem .25rem .2rem 0;padding:.3rem .55rem;border:1.5px solid #000;color:#000;text-decoration:none;font-weight:600;font-size:.86rem}}
.live a{{background:#000;color:#fff}}.ln a.pdf{{border-style:dashed;font-weight:400}}
ul{{list-style:none;padding:0;margin:1.4rem 0 0}}li{{border-top:1.5px solid #000;padding:.9rem 0}}.vh{{display:flex;justify-content:space-between;gap:1rem;flex-wrap:wrap}}
.vh span{{color:#444}}li p{{margin:.3rem 0 0}}h2{{font-size:1rem;text-transform:uppercase;letter-spacing:.06em;margin:2rem 0 0}}
</style></head><body><div class="w"><h1>Saved versions</h1><p class="sub">Frozen, date-stamped copies of the Japan and Hong Kong trip apps. The live apps keep changing; these never do.</p>
<p class="live"><a href="../">Live Itinerary</a><a href="../extras/">Live Extras</a><a href="../weather/">Live Weather</a><a href="../expenses/">Live Expenses</a></p>
<h2>Steady states</h2><ul>{rows}</ul></div></body></html>'''
open(os.path.join(ARCH, 'index.html'), 'w', encoding='utf-8').write(idx)
print(slug)
