# Run at the end of build.py. Fixes how-to numbers that went stale when the how-tos were reordered,
# then turns every "How-to N" mention outside the how-to headings into a link to that section (#hN).
import re as _re_h, html as _html_h

# The how-to each mention should point to, by its title. Keyed by text just before the mention.
_HT = {t: i for i, (t, _s) in enumerate(HOWTO, 1)}
_FIX = [
    ('except Casanova at 12:00 (How-to ', 'Omotesando and Aoyama store hours'),
    ('G has his own options (How-to ', 'While the stores are on, for G'),
    ('counters before they fill (How-to ', 'Omoide Yokochō, Mon 19'),
]
for _ctx, _title in _FIX:
    out = _re_h.sub(_re_h.escape(_ctx) + r'\d+\)', lambda m: _ctx + str(_HT[_title]) + ')', out)

# Link mentions, but not inside the how-to headings, tags, scripts or styles
_hs = out.index('id="howto"')
_head, _tail = out[:_hs], out[_hs:]
def _lnk(seg):
    parts = _re_h.split(r'(<script.*?</script>|<style.*?</style>|<[^>]+>)', seg, flags=_re_h.S)
    for k in range(0, len(parts), 2):
        parts[k] = _re_h.sub(r'How-to (\d+)', lambda m: f'<a class="hl" href="#h{m.group(1)}">How-to {m.group(1)}</a>', parts[k])
    return ''.join(parts)
out = _lnk(_head) + _tail
_n_h = len(_re_h.findall(r'class="hl" href="#h\d+"', out))
_bad = [x for x in _re_h.findall(r'href="#h(\d+)"', out) if not 1 <= int(x) <= len(HOWTO)]
assert not _bad, ('how-to links to missing sections', _bad)
out = out.replace('</style>', '.hl{color:inherit;text-decoration:none;border-bottom:1.5px solid var(--ink);white-space:nowrap}.hl:hover{background:var(--ink);color:var(--paper)}@media print{.hl{border:0}}</style>', 1)
print('how-to links:', _n_h)
