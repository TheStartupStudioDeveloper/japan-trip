# Hong Kong leg (Claude is not available in Hong Kong): Grok drives the LIVE apps.
# Grok edits only the small data files in grok/data/. This script rebuilds the four live apps (itinerary, extras,
# weather, expenses at the usual URLs) from them, using the master's own build scripts in a scratch folder.
#
#   python3 source/grok/grok_build.py          rebuild grok/ from grok/data/ (the GitHub Action runs this on every push)
#   python3 source/grok/grok_build.py --dump   one-off: write the master's current data out as grok/data/ (done 25 Oct 2026)
#
# Needs: python3, playwright with chromium, pillow.
import os, sys, re, json, glob, shutil, subprocess, tempfile, hashlib, datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
DATA = os.path.join(REPO, 'grok', 'data')
OUTG = os.path.join(REPO, 'grok')
BASE = 'https://thestartupstudiodeveloper.github.io/japan-trip/'
GBASE = BASE + 'grok/'
DUMP = '--dump' in sys.argv


def rd(p):
    return json.load(open(p, encoding='utf-8'))


def wr(p, v):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    json.dump(v, open(p, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    open(p, 'a').write('\n')


def run(cmd, cwd, env=None):
    r = subprocess.run(cmd, cwd=cwd, env=dict(os.environ, **(env or {})), capture_output=True, text=True)
    if r.returncode:
        sys.stderr.write(r.stdout[-3000:] + r.stderr[-6000:])
        raise SystemExit(f'failed: {" ".join(cmd)} in {cwd}')
    return r.stdout


W = tempfile.mkdtemp(prefix='grokbuild-')
IT = os.path.join(W, 'itinerary')
FR = os.path.join(W, 'repo')  # a stand-in repo the master scripts write their apps into
shutil.copytree(os.path.join(REPO, 'source', 'itinerary'), IT, ignore=shutil.ignore_patterns('out', '__pycache__'))
os.makedirs(os.path.join(IT, 'out'))
os.makedirs(os.path.join(IT, 'mapview', 'out'), exist_ok=True)
for f in glob.glob(os.path.join(REPO, 'source', 'mapview', '*.py')):
    if not os.path.exists(os.path.join(IT, 'mapview', os.path.basename(f))):
        shutil.copy(f, os.path.join(IT, 'mapview'))
os.makedirs(os.path.join(FR, 'source', 'expenses'))
shutil.copy(os.path.join(REPO, 'source', 'expenses', 'log_synced.json'), os.path.join(FR, 'source', 'expenses'))

# apptools for the live apps under Grok: same links and storage as always, chat button opens Grok, no PDF rendering
at = open(os.path.join(REPO, 'source', 'apptools.py'), encoding='utf-8').read()
at = re.sub(r"(CHAT = \{.*?\n\})", "CHAT = {'': 'https://grok.com/', 'extras': 'https://grok.com/', 'weather': 'https://grok.com/', 'expenses': 'https://grok.com/'}", at, flags=re.S)
at = at.replace('Chat with Claude', 'Open Grok')
at = at.replace("def render_pdf(src_html_path, pdf_path, footer):",
              "def render_pdf(src_html_path, pdf_path, footer):\n    open(pdf_path, 'wb').write(b'%PDF-1.4'); return\n\ndef _render_pdf_unused(src_html_path, pdf_path, footer):")
open(os.path.join(FR, 'source', 'apptools.py'), 'w', encoding='utf-8').write(at)

# itinerary build: point it at the stand-in repo and add the Grok overlay after the last amendments file
b = open(os.path.join(IT, 'build.py'), encoding='utf-8').read()
hook = "exec(open('amendments_v2_zzzz_actual.py').read())"
assert hook in b, 'master build changed: overlay hook not found'
b = b.replace(hook, hook + f"\nexec(open({os.path.join(HERE, 'overlay.py')!r}, encoding='utf-8').read())", 1)
b = b.replace("'/home/claude/japan-trip/source'", repr(os.path.join(FR, 'source')))
open(os.path.join(IT, 'build.py'), 'w', encoding='utf-8').write(b)
p = open(os.path.join(IT, 'post.py'), encoding='utf-8').read().replace("'/home/claude/japan-trip'", repr(FR))
open(os.path.join(IT, 'post.py'), 'w', encoding='utf-8').write(p)

if DUMP:
    # ---------- one-off export of the master's current data ----------
    if os.path.exists(DATA):
        raise SystemExit('grok/data already exists. Delete it first if you really want a fresh export from the master.')
    run(['python3', 'build.py'], IT, {'JHK_GROK_DUMP': DATA})
    shutil.copy(os.path.join(REPO, 'source', 'itinerary', 'expenses.json'), os.path.join(DATA, 'expenses.json'))
    ex = rd(os.path.join(REPO, 'source', 'extras', 'extras.json'))
    wr(os.path.join(DATA, 'extras', 'cards.json'), ex['cards'])
    wr(os.path.join(DATA, 'extras', 'planned.json'), ex['planned'])
    for i, a in enumerate(ex['areas'], 1):
        wr(os.path.join(DATA, 'extras', 'areas', f'{i:02d}-{a["key"]}.json'), a)
    os.makedirs(os.path.join(DATA, 'extras', 'cards-new'), exist_ok=True)
    open(os.path.join(DATA, 'extras', 'cards-new', '.keep'), 'w').write('')
    wh = open(os.path.join(REPO, 'source', 'weather', 'weather.html'), encoding='utf-8').read()
    wx = json.loads(re.search(r'<script type="application/json" id="wx">(.*?)</script>', wh, re.S).group(1))
    for d in wx.pop('days'):
        wr(os.path.join(DATA, 'weather', 'days', f'{d["d"]:02d}.json'), d)
    wr(os.path.join(DATA, 'weather', 'meta.json'), wx)
    shutil.rmtree(W)
    print('Grok data written to', DATA)
    raise SystemExit(0)

# ---------- guard: a Claude weather chat may still update source/weather/weather.html. If its check is newer, take it ----------
try:
    _wh = open(os.path.join(REPO, 'source', 'weather', 'weather.html'), encoding='utf-8').read()
    _wx = json.loads(re.search(r'<script type="application/json" id="wx">(.*?)</script>', _wh, re.S).group(1))
    _gm = rd(os.path.join(DATA, 'weather', 'meta.json'))
    if datetime.datetime.fromisoformat(_wx['checked']) > datetime.datetime.fromisoformat(_gm['checked']):
        for _d in _wx.pop('days'):
            wr(os.path.join(DATA, 'weather', 'days', f'{int(_d["d"]):02d}.json'), _d)
        _wx['watch'] = _wx.get('watch') or []
        wr(os.path.join(DATA, 'weather', 'meta.json'), _wx)
        print('weather: took the newer check from source/weather/weather.html', _wx['checkedLabel'])
except Exception as _e:
    print('weather guard skipped:', _e)

# ---------- check every data file first, with a plain-English error that names the file ----------
_bad = []
for f in sorted(glob.glob(os.path.join(DATA, '**', '*.json'), recursive=True)):
    try:
        v = json.load(open(f, encoding='utf-8'))
    except Exception as e:
        _bad.append(f'{os.path.relpath(f, REPO)}: not valid JSON ({e})'); continue
    rel = os.path.relpath(f, DATA)
    if rel.startswith('days' + os.sep):
        for k in ('d', 'title', 'rows'):
            if k not in v: _bad.append(f'{os.path.relpath(f, REPO)}: missing "{k}"')
        for i, r in enumerate(v.get('rows') or [], 1):
            if not isinstance(r, dict) or 'time' not in r or 'what' not in r:
                _bad.append(f'{os.path.relpath(f, REPO)}: row {i} needs "time" and "what"')
            elif str(r.get('status', '')).strip().lower() not in ('', 'done', 'booked', 'to book', 'skipped'):
                _bad.append(f'{os.path.relpath(f, REPO)}: row {i} status must be "", "done", "booked", "to book" or "skipped"')
    if rel == 'expenses.json':
        for i, e in enumerate(v, 1):
            for k in ('id', 'date', 'item', 'payer', 'aud', 'status'):
                if k not in e: _bad.append(f'grok/data/expenses.json: entry {i} missing "{k}"')
if _bad:
    open(os.path.join(OUTG, 'build-error.txt'), 'w').write('The Grok apps were NOT rebuilt. Fix these, then commit again:\n' + '\n'.join(_bad) + '\n')
    print('\n'.join(_bad)); raise SystemExit(1)
if os.path.exists(os.path.join(OUTG, 'build-error.txt')):
    os.remove(os.path.join(OUTG, 'build-error.txt'))

# ---------- assemble the data the master scripts expect ----------
shutil.copy(os.path.join(DATA, 'expenses.json'), os.path.join(IT, 'expenses.json'))
os.makedirs(os.path.join(IT, 'extras')); os.makedirs(os.path.join(IT, 'expenses'))
ex = {'cards': rd(os.path.join(DATA, 'extras', 'cards.json')), 'areas': [], 'planned': rd(os.path.join(DATA, 'extras', 'planned.json'))}
for f in sorted(glob.glob(os.path.join(DATA, 'extras', 'cards-new', '*.json'))):
    c = rd(f); ex['cards'].update(c if 'n' not in c else {os.path.splitext(os.path.basename(f))[0]: c})
for f in sorted(glob.glob(os.path.join(DATA, 'extras', 'areas', '*.json'))):
    ex['areas'].append(rd(f))
wr(os.path.join(IT, 'extras', 'extras.json'), ex)
for f in ('extras_build.py',):
    s = open(os.path.join(REPO, 'source', 'extras', f), encoding='utf-8').read().replace(f"MASTER_URL = '{BASE}'", f"MASTER_URL = '{GBASE}'")
    open(os.path.join(IT, 'extras', f), 'w', encoding='utf-8').write(s)
shutil.copy(os.path.join(REPO, 'source', 'expenses', 'expenses_build.py'), os.path.join(IT, 'expenses'))
wx = rd(os.path.join(DATA, 'weather', 'meta.json'))
wx['days'] = sorted((rd(f) for f in glob.glob(os.path.join(DATA, 'weather', 'days', '*.json'))), key=lambda d: int(d['d']))
wh = open(os.path.join(REPO, 'source', 'weather', 'weather.html'), encoding='utf-8').read()
wxs = json.dumps(wx, ensure_ascii=False).replace('</', '<\\/')
wh = re.sub(r'(<script type="application/json" id="wx">).*?(</script>)', lambda m: m.group(1) + wxs + m.group(2), wh, count=1, flags=re.S)
open(os.path.join(W, 'weather.html'), 'w', encoding='utf-8').write(wh)

# ---------- build ----------
run(['python3', 'build.py'], IT, {'JHK_GROK_DATA': DATA})
open(os.path.join(IT, 'out', 'Japan-Hong-Kong-Master-Itinerary-V2.pdf'), 'wb').write(b'%PDF-1.4\n')
run(['python3', os.path.join(REPO, 'source', 'itinerary', 'site.py'), FR], IT)
run(['python3', 'extras_build.py', FR], os.path.join(IT, 'extras'))
run(['python3', 'expenses_build.py', FR], os.path.join(IT, 'expenses'))
run(['python3', os.path.join(REPO, 'source', 'weather', 'weather_site.py'), os.path.join(W, 'weather.html'), FR], W)

# ---------- publish into the LIVE apps (the ones on G's home screen) ----------
# Since Mon 26 Oct 2026, Grok drives the live apps from grok/data/. Same URLs, same storage keys (ticks and notes kept),
# same icons and PDFs. Only index.html, manifest and sw.js are replaced. Backups: archive/ss3-2026-10-26, branch backup-before-grok-live-2026-10-26.
hk = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=8))).strftime('%a %d %b %H:%M')
for app in ('', 'extras', 'weather', 'expenses'):
    src = os.path.join(FR, app) if app else FR
    dst = os.path.join(REPO, app) if app else REPO
    h = open(os.path.join(src, 'index.html'), encoding='utf-8').read()
    h = re.sub(r'https://claude\.ai/(?:code/session_|chat/)[\w-]+', 'https://grok.com/', h)
    h = h.replace('Paste it into the itinerary chat', 'Paste it into Grok').replace('Paste it into the chat', 'Paste it into Grok').replace('Copy for Claude', 'Copy for Grok').replace('Chat with Claude', 'Open Grok')
    assert len(h) > 20000, 'built page looks empty: ' + (app or 'itinerary')
    open(os.path.join(dst, 'index.html'), 'w', encoding='utf-8').write(h)
    shutil.copy(os.path.join(src, 'manifest.webmanifest'), os.path.join(dst, 'manifest.webmanifest'))
    shutil.copy(os.path.join(src, 'sw.js'), os.path.join(dst, 'sw.js'))
wr(os.path.join(OUTG, 'build.json'), {'built_hkt': hk, 'built_utc': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
                                      'target': 'live apps', 'data_hash': hashlib.md5(''.join(open(f, 'rb').read().hex() for f in sorted(glob.glob(os.path.join(DATA, '**', '*.json'), recursive=True))).encode()).hexdigest()[:10]})
shutil.rmtree(W)
print('Live apps built from grok/data', hk)
