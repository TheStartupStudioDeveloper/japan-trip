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
_js = '''<script>
(function(){
 // Fast smooth scroll for in-page links: how-to links, calendar, day bar, summary days, top bar.
 var reduce=window.matchMedia&&matchMedia('(prefers-reduced-motion: reduce)').matches, run=0;
 function go(t,flash){
  var root=document.documentElement, pad=parseFloat(getComputedStyle(root).scrollPaddingTop)||0;
  var y0=scrollY, y1=Math.max(0,t.getBoundingClientRect().top+scrollY-pad), d=y1-y0;
  var dur=reduce?0:Math.min(480,220+Math.abs(d)/40), t0=null, id=++run;
  root.style.scrollBehavior='auto';
  function step(ts){
   if(id!==run) return;
   if(t0===null) t0=ts;
   var p=dur?Math.min(1,(ts-t0)/dur):1, e=p<.5?4*p*p*p:1-Math.pow(-2*p+2,3)/2;
   scrollTo(0,y0+d*e);
   if(p<1) requestAnimationFrame(step); else { root.style.scrollBehavior=''; if(flash){t.classList.remove('hflash');void t.offsetWidth;t.classList.add('hflash')} }
  }
  requestAnimationFrame(step);
 }
 document.addEventListener('click',function(e){
  var a=e.target.closest('a[href^="#"]'); if(!a||a.classList.contains('pl')) return;
  var h=a.getAttribute('href'); if(h.length<2) return;
  var t=document.getElementById(h.slice(1)); if(!t) return;
  e.preventDefault();
  try{history.pushState(null,'',h)}catch(x){}
  go(t, a.classList.contains('hl'));
 });
})();
</script>'''
out = out.replace('</body>', _js + '</body>', 1)
out = out.replace('</style>', '@keyframes hflash{0%{box-shadow:0 0 0 4px var(--ink)}100%{box-shadow:0 0 0 0 transparent}}.hflash{animation:hflash 1.6s ease-out}</style>', 1)
print('how-to links:', _n_h)
