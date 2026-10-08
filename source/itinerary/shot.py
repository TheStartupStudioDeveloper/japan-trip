import asyncio
from playwright.async_api import async_playwright
U='file:///tmp/claude-0/-home-claude/f96e2d08-84c7-5d2f-8bfa-bb192a8f0b3c/scratchpad/master_v2/out/japan-hong-kong-final-itinerary.html'
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':390,'height':844},device_scale_factor=1)
        await pg.goto(U); await pg.wait_for_timeout(500)
        await pg.screenshot(path='m1.png'); 
        await pg.evaluate("document.getElementById('leg-k').scrollIntoView()"); await pg.wait_for_timeout(300)
        await pg.screenshot(path='m2.png')
        await pg.evaluate("document.getElementById('d29').scrollIntoView()"); await pg.wait_for_timeout(300)
        await pg.screenshot(path='m3.png')
        pg2=await b.new_page(viewport={'width':1100,'height':900})
        await pg2.goto(U); await pg2.screenshot(path='d1.png')
        await pg2.emulate_media(media='print')
        await pg2.pdf(path='out/Japan-Hong-Kong-Master-Itinerary-V2.pdf',format='A4',print_background=True,prefer_css_page_size=True,display_header_footer=True,
          header_template='<span></span>',
          footer_template='<div style="font-size:7.5pt;font-family:Helvetica,Arial,sans-serif;width:100%;padding:0 13mm;display:flex;justify-content:space-between;color:#000"><span>Japan &amp; Hong Kong Master Itinerary V2</span><span>Page <span class="pageNumber"></span> of <span class="totalPages"></span></span></div>')
        await b.close()
asyncio.run(main())
