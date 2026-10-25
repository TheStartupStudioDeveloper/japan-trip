# Grok copy: swaps the master's day data for the files in grok/data.
# Exec'd by the Grok build inside a scratch copy of source/itinerary, straight after the last amendments file.
#   JHK_GROK_DUMP=<dir>   write the current master data out as the Grok data files (one-off, done 25 Oct 2026)
#   JHK_GROK_DATA=<dir>   read the Grok data files and replace the master data with them
import os as _go, json as _gj, glob as _gg
_ST = {B: 'booked', TB: 'to book', 'd': 'done', '': ''}
_TS = {v: k for k, v in _ST.items()}
_TS.update({'book': TB, 'tobook': TB, 'to-book': TB, 'fixed': B, 'yes': 'd', 'x': 'd'})
def _alld():
    return [DAY16] + DAYS
def _rows_out(rs):
    return [{'time': r[0], 'what': r[1], 'detail': r[2], 'status': _ST.get(r[3], '')} for r in rs]
def _rows_in(rs):
    o = []
    for r in rs:
        st = str(r.get('status') or '').strip().lower()
        if st == 'skipped': continue  # kept in the data for the record, not shown
        o.append((str(r.get('time', '')), str(r.get('what', '')), str(r.get('detail', '') or ''), _TS.get(st, '')))
    return o
if _go.environ.get('JHK_GROK_DUMP'):
    _dd = _go.environ['JHK_GROK_DUMP']; _go.makedirs(_go.path.join(_dd, 'days'), exist_ok=True)
    for d in _alld():
        x = {'d': d['d'], 'dow': d['dow'], 'where': d.get('where') or '', 'title': d['title'], 'cal': d.get('cal', ''),
             'summary': d.get('sum', '') or d.get('pre', ''), 'rows': _rows_out(d.get('rows') or []), 'footnote': d.get('foot', ''),
             'notes': [list(n) for n in (d.get('notes') or [])]}
        if 'alts' in d and not d.get('rows'):
            a = d['alts'][0]; a = a if isinstance(a, dict) else dict(ttl=a[1], sum=a[2], rows=a[3], foot=a[4])
            x['summary'] = a.get('sum', ''); x['rows'] = _rows_out(a.get('rows') or []); x['footnote'] = a.get('foot', '')
        _gj.dump(x, open(_go.path.join(_dd, 'days', f"{d['d']:02d}.json"), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _gj.dump([{'title': t, 'steps': list(s)} for t, s in HOWTO], open(_go.path.join(_dd, 'howto.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _gj.dump([{'title': a, 'text': b} for a, b in TIPS], open(_go.path.join(_dd, 'tips.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _gj.dump([{'title': t, 'items': [{'leg': k or '', 'text': x} for k, x in items]} for t, items in CHECK], open(_go.path.join(_dd, 'checklist.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _gj.dump({k: {'name': LEGS[k]['name'], 'dates': LEGS[k]['dates'], 'hotel': LEGS[k]['hotel'], 'summary': LEGS[k]['sum'],
                  'good_to_know': [list(n) for n in GOOD[k]]} for k in 'skgh'}, open(_go.path.join(_dd, 'legs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    _gj.dump([{'swap': a, 'replaces': b, 'costs': c} for a, b, c in SWAPS], open(_go.path.join(_dd, 'hk-swaps.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
if _go.environ.get('JHK_GROK_DATA'):
    _dd = _go.environ['JHK_GROK_DATA']
    _byd = {d['d']: d for d in _alld()}
    for _f in sorted(_gg.glob(_go.path.join(_dd, 'days', '*.json'))):
        x = _gj.load(open(_f, encoding='utf-8')); d = _byd.get(int(x['d']))
        if d is None: continue
        for k_from, k_to in (('title', 'title'), ('cal', 'cal'), ('where', 'where'), ('summary', 'sum'), ('footnote', 'foot')):
            if k_from in x: d[k_to] = x[k_from] or ''
        if 'rows' in x:
            d['rows'] = _rows_in(x['rows']); d.pop('alts', None); d.pop('pre', None)
        if 'notes' in x: d['notes'] = [tuple(n) for n in x['notes']]
    _p = _go.path.join(_dd, 'howto.json')
    if _go.path.exists(_p): HOWTO[:] = [(h['title'], list(h['steps'])) for h in _gj.load(open(_p, encoding='utf-8'))]
    _p = _go.path.join(_dd, 'tips.json')
    if _go.path.exists(_p): TIPS[:] = [(t['title'], t['text']) for t in _gj.load(open(_p, encoding='utf-8'))]
    _p = _go.path.join(_dd, 'checklist.json')
    if _go.path.exists(_p): CHECK[:] = [(c['title'], [(i.get('leg') or None, i['text']) for i in c['items']]) for c in _gj.load(open(_p, encoding='utf-8'))]
    _p = _go.path.join(_dd, 'legs.json')
    if _go.path.exists(_p):
        for k, v in _gj.load(open(_p, encoding='utf-8')).items():
            if k in LEGS:
                LEGS[k].update({'name': v.get('name', LEGS[k]['name']), 'dates': v.get('dates', LEGS[k]['dates']), 'hotel': v.get('hotel', LEGS[k]['hotel']), 'sum': v.get('summary', LEGS[k]['sum'])})
                if 'good_to_know' in v: GOOD[k] = [tuple(n) for n in v['good_to_know']]
    _p = _go.path.join(_dd, 'hk-swaps.json')
    if _go.path.exists(_p): SWAPS[:] = [(s['swap'], s['replaces'], s['costs']) for s in _gj.load(open(_p, encoding='utf-8'))]
