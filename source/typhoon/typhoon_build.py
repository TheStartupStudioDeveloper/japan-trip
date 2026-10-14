# Kyoto & Tokyo Typhoon Backup. A separate page, not part of the Master Itinerary.
# Reuses the master's styles and place cards from the built itinerary (../../index.html),
# writes typhoon/index.html (GitHub web copy) and source/typhoon/typhoon-backup.html (claude.ai copy).
# Run: python3 source/typhoon/typhoon_build.py   (from the repo root)
import json, re, html, os, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
E = html.escape
master = open(os.path.join(ROOT, 'index.html'), encoding='utf-8').read()

# ---------- borrow the master's styles and place cards ----------
STYLES = ''.join(re.findall(r'<style>.*?</style>', master, re.S)[:2])
i = master.find('var P=') + 6
P, _ = json.JSONDecoder().raw_decode(master[i:])

def add(key, n, l, w, t, m):
    P[key] = dict(n=n, l=l, w=w, t=t, m=m)

add('mercure', 'Mercure Tokyo Hibiya', 'メルキュール東京日比谷',
    'The backup hotel for Friday 23 only, a few minutes from the Blossom Hibiya. If the typhoon threatens Saturday\'s train, you come to Tokyo a day early and sleep here, then move to the Blossom on Saturday.',
    'King Privilege Room, booked direct on the Mercure website. Check-in 14:00, checkout 11:00. Free cancellation until 18:00 Japan time on Thu 22.', 'Mercure Tokyo Hibiya')
add('gekkeikan', 'Gekkeikan Okura Sake Museum', '月桂冠大倉記念館',
    'An old sake brewery in Fushimi, Kyoto\'s brewing district, turned into a small museum. Wooden tools, the brewing story, and a tasting at the end. The canal and black timber warehouses around it are the prettiest part of Fushimi.',
    'Opens 09:30. Two stops south of Fushimi Inari on the Keihan line, get off at Chūshojima. Check the hours the night before.', 'Gekkeikan Okura Sake Museum Kyoto')
add('honganji', 'Higashi Hongan-ji', '東本願寺',
    'One of the largest wooden buildings in the world, a huge temple hall right on Karasuma-dōri between the hotel and Kyoto Station. Free, quiet and fully under cover.',
    'Shoes off inside. Ten minutes is enough to feel the scale.', 'Higashi Honganji Kyoto')
add('daiichi', 'Honke Daiichi Asahi', '本家 第一旭 たかばし本店',
    'Kyoto-style ramen: clear soy and pork broth, thin noodles and a pile of Kujō green onion. Five minutes from Kyoto Station, quick turnover.',
    'Closed Thursdays, open Friday. Expect a short queue.', 'Honke Daiichi Asahi Takabashi Kyoto')
add('jidai', 'Jidai Matsuri', '時代祭',
    'Kyoto\'s big costume parade. About 2,000 people in dress from a thousand years of Kyoto history walk from the Imperial Palace to Heian Shrine.',
    'Thu 22 from about 12:00. Expect road closures and slow taxis in the centre until mid afternoon.', 'Jidai Matsuri Kyoto parade')
add('ramenst', 'Tokyo Ramen Street', '東京ラーメンストリート',
    'A row of well known ramen shops in the basement on the Yaesu side of Tokyo Station, all under one roof.',
    'Queues are shorter before 11:30. Pick by the photo menus outside.', 'Tokyo Ramen Street Tokyo Station')
add('charst', 'Tokyo Character Street', '東京キャラクターストリート',
    'Thirty or so character shops in the basement of Tokyo Station: Pokémon, Ghibli, Snoopy, Kirby and more. Next door to Ramen Street.',
    'All under cover, connected underground.', 'Tokyo Character Street')
add('midtown', 'Tokyo Midtown Hibiya', '東京ミッドタウン日比谷',
    'A glass tower of shops, cafes and restaurants across the road from Hibiya Park, a short walk from both hotels. The 6th floor Park View Garden looks over the park.',
    'The garden terrace is outdoors. The rest is under cover.', 'Tokyo Midtown Hibiya')
add('starbar', 'Star Bar Ginza', 'スタア・バー・ギンザ',
    'A basement bar in Ginza famous for precise, classic cocktails made by bartenders in white jackets.',
    'Closed Mondays, open Friday. Small and quiet.', 'Star Bar Ginza')
add('highfive', 'Bar High Five', 'バー ハイファイブ',
    'A famous Ginza cocktail bar with no menu. Say what you like and they make it for you.',
    'Closed Sundays, open Friday. Small, so expect a short wait.', 'Bar High Five Ginza')
add('yotsutsuji', 'Yotsutsuji crossing', '四ツ辻',
    'The halfway point up Mount Inari, about 40 minutes up through the gates, with a view back over Kyoto. Most people turn back here.',
    'Skip it if cloud hides the view. The best gates are below it anyway.', 'Yotsutsuji Fushimi Inari')
add('railmuseum', 'Kyoto Railway Museum', '京都鉄道博物館',
    'A big, mostly indoor museum of Japanese trains, from steam engines to early Shinkansen, about 20 minutes on foot or a short bus ride west of Kyoto Station.',
    'Check the hours and closed days before going.', 'Kyoto Railway Museum')
P['teamlab'] = dict(P['teamlab'], t='Booked for 08:30 on Monday 26. The booking can change date or time up to three times, so it can move to a wet Saturday 24 if the fireworks are off.')

used = set()
def L(key, text=None):
    if key not in P:
        sys.exit('No place card for ' + key)
    used.add(key)
    return f'<a class="pl" href="#" role="button" data-p="{key}">{E(text or P[key]["n"])}</a>'

# ---------- page parts ----------
def tag(s):
    return {'b': ' <span class="tag tag-b">Booked</span>',
            'tb': ' <span class="tag tag-tb">To book</span>',
            'ch': ' <span class="tag tag-tb">Change booking</span>',
            'tbc': ' <span class="tag tag-tb">To confirm</span>'}.get(s, '')

def R(t, p, n='', s=''):
    return (t, p, n, s)

def rows(rs):
    out = []
    for t, p, n, s in rs:
        cls = 'row is-b' if s == 'b' else 'row'
        out.append(f'<li class="{cls}"><span class="t">{t}</span><div class="w"><p class="p">{p}{tag(s)}</p>'
                   + (f'<p class="n">{n}</p>' if n else '') + '</div></li>')
    return '<ol class="rows">' + ''.join(out) + '</ol>'

def notes(ns):
    return '<dl class="notes">' + ''.join(f'<div><dt>{a}</dt><dd>{b}</dd></div>' for a, b in ns) + '</dl>'

def day(num, dow, where, legs, title, summ, rs, ns=()):
    band = ''.join(f'<i class="pat pat-{l}"></i>' for l in legs)
    return (f'<article class="day"><div class="band">{band}</div><header class="dh"><div class="date"><span class="num">{num}</span>'
            f'<span class="dow">{dow}<br><span class="where">{where}</span></span></div><h3>{title}</h3></header>'
            f'<p class="sum">{summ}</p>{rows(rs)}' + (notes(ns) if ns else '') + '</article>')

# ---------- shared blocks ----------
NOZOMI13 = R('07:55', f'{L("shinkansen", "Nozomi 13")} to Kyoto', 'Car 9, seats 16-C and 16-D. Fuji on the right at about 08:30.', 'b')
KYOTO10 = R('10:00', f'{L("kyoto-st")}', '', 'b')
BAGS = R('10:15', f'Bags to {L("crosta")} for hotel delivery',
         'Level B1 below the JR Central Gate. Ask for delivery to sequence KYOTO GOJO: ¥1,500 a bag, drop by 14:00, delivered after 17:00. '
         'You will not be back before the counter shuts at 20:00, so storage won\'t work tonight. Take passports, chargers and valuables out first.', 'tbc')

KYOTO_PROPER = [
    R('06:45', 'Leave the hotel', f'One {L("subway-k", "subway")} stop or a 15 minute walk to {L("kyoto-st")}, then the JR Sagano line to Saga-Arashiyama.'),
    R('07:20', f'{L("bamboo", "Bamboo grove")}', 'Genuinely empty before eight.'),
    R('08:30', f'{L("tenryuji")} as it opens', 'The pond garden backs onto the bamboo.'),
    R('09:30', f'{L("okochi")}, or {L("togetsukyo")} and the river path', 'Pick one. The villa includes matcha.'),
    R('10:15', f'Coffee and a snack in {L("arashiyama")}', 'Lunch is early.'),
    R('10:45', 'Back to the centre', 'Hankyu line to Karasuma, changing at Katsura. About 40 minutes.'),
    R('11:30', f'{L("nishiki")} lunch', 'Ahead of the lunch crush. Eat at the stall.'),
    R('12:30', f'Optional: the {L("jidai")} parade', 'It passes along Kawaramachi and Sanjō in the early afternoon, a few minutes from the east end of Nishiki. Watch for ten minutes, then walk to the hotel.'),
    R('13:15', 'Hotel and rest', 'Two hours with your feet up.'),
    R('15:15', f'Taxi to {L("kiyomizu")}', 'About 10 minutes, the parade has cleared by now. The stage view over the city is the thing. Closes 18:00.'),
    R('16:30', f'Down through {L("sannenzaka")}', 'Downhill, steep stone steps. Shops start closing about 17:30.'),
    R('17:10', f'{L("yasaka-pagoda")} at sunset', ''),
    R('17:30', f'{L("yasaka")}, then down into {L("gion")}', f'Lanterns lit. {L("hanamikoji")} and the {L("shirakawa", "Shirakawa canal")}.'),
    R('18:30', f'Dinner in {L("gion")}', 'The one special dinner in Kyoto, now on Thursday. Book it before you fly.', 'tb'),
    R('20:30', f'Optional: a drink in {L("pontocho")}', 'Five minutes over the bridge. Pontochō dinner went to Osaka on Wednesday, so this is your look at it.'),
]

def sat():
    return day(24, 'Saturday', 'Tokyo, typhoon day', ['g'], 'Typhoon day in Tokyo, under cover',
        f'Heavy rain all day on tenki.jp, about 81 mm, heaviest in the afternoon. Stay walkable or underground, keep away from {L("odaiba")} and the {L("yurikamome")}, and move hotels by taxi.',
        [R('08:30', 'Slow breakfast, stay in', 'Watch the news and the JMA warnings. Nothing today needs an early start.'),
         R('10:45', f'Check out of the {L("mercure", "Mercure")}, taxi to {L("blossom")}', 'Checkout is 11:00. Ask the Blossom to hold the bags, or check in early if a room is ready. Two minutes by taxi.'),
         R('11:30', f'{L("tokyo-st")} underground', f'{L("ramenst")} for lunch, then {L("charst")} and the Gransta shops. Connected underground from Yūrakuchō, so barely a step outside.'),
         R('13:30', f'{L("teamlab")}, moved from Monday', f'Hibiya line from Hibiya to {L("kamiyacho")}, which connects straight into Azabudai Hills. About two hours inside. Change the booking from the confirmation email.', 'ch'),
         R('15:45', 'Check in at the Blossom and rest', ''),
         R('17:00', f'Head spa or massage', f'{L("headspa-zen")} or {L("buasai")}, both close to the hotel. Book a day ahead.'),
         R('19:00', 'Dinner', f'If the Hilton still serves the {L("seascape")} dinner and the trains are running, go. Otherwise a sit-down dinner in {L("ginza")} or {L("shimbashi")}, five minutes from the hotel.')],
        [('If the fireworks go ahead', f'The typhoon has missed. Keep the morning as above, skip teamLab, check in at 15:00, and leave for {L("hilton", "the Hilton")} at 16:00 as booked. teamLab stays on Monday.'),
         ('Monday 26 if teamLab moves', 'Monday starts in Asakusa about 10:00, already written into the master as the wet-weather shape.'),
         ('Safety', 'The Yurikamome and other open-air lines stop in strong wind. Stock up on water and snacks at a convenience store on Friday night.')])

def fri_tokyo_evening(arrive):
    return [
        R(arrive, f'Taxi to the {L("mercure", "Mercure Tokyo Hibiya")}, check in', 'Check-in from 14:00. From the Yaesu taxi rank, about 10 minutes.', 'b'),
        R('16:30' if arrive < '16:00' else '', f'{L("midtown")}' if arrive < '16:00' else '', 'Across from Hibiya Park, shops and cafes under cover. Pick up water and snacks for Saturday on the way back.' if arrive < '16:00' else ''),
        R('19:00' if arrive < '18:00' else '19:30', f'{L("yurakucho")} izakayas under the arches', 'The spare-night idea from the master. Sheltered by the tracks, five minutes from the hotel.'),
        R('21:00', f'Optional: {L("starbar")} or {L("highfive")}', 'Both open on Fridays, both a short walk.'),
    ]

def clean(rs):
    return [r for r in rs if r[1]]

# ---------- scenario 1 ----------
S1 = dict(id='s1', no='Scenario 1', name='Kyoto first, Osaka at night',
    pick='Recommended',
    idea=f'Nara on Wednesday with Osaka\'s night-time highlights straight after, Kyoto proper on dry Thursday, {L("fushimi")} in the rain on Friday morning, and Tokyo by mid afternoon.',
    best='The most Kyoto for the least risk. Friday leaves at about the same time Saturday\'s train would have.',
    cost='Osaka by day: the castle, Umeda Sky, Kuromon and the Horie shopping. Nigatsu-dō in Nara. A very long Wednesday.',
    leave='Fri, about 11:30 to 12:00',
    glance=['Nara, then Osaka at night', 'Arashiyama, Nishiki, Higashiyama, Gion', 'Inari in the rain, Tokyo by 14:30', 'Typhoon day, under cover'],
    days=[
        day(21, 'Wednesday', 'Nara, then Osaka', ['k'], 'Nara, then Osaka at night',
            'The first day of the leg does double duty. Nara runs as planned until mid afternoon, then a direct train drops you in Namba for the lion head, Shinsekai at dusk and Dōtonbori after dark.',
            [NOZOMI13, KYOTO10, BAGS,
             R('10:45', 'Train to Nara', 'Kintetsu from Kyoto Station, about 45 minutes, and it arrives closest to the park.'),
             R('11:30', f'Lunch on Sanjō-dōri', f'{L("kakinoha")} is fast, then {L("nakatanido")} for the mochi pounding.'),
             R('12:15', f'{L("narapark")} and the deer, {L("kasuga")}', f'{L("deer-crackers", "Deer crackers")} about ¥200. Up the lantern path to the shrine front.'),
             R('13:45', f'{L("todaiji")}', 'Wet afternoon? Do this first, it is under cover.'),
             R('14:45', f'Walk down to {L("kintetsu-nara")}', 'About 20 minutes downhill. Nigatsu-dō is the cut.'),
             R('15:20', f'Kintetsu direct to {L("namba")}', 'About 40 minutes, no change.'),
             R('16:10', f'{L("namba-yasaka")}', 'The giant lion head. Closes about 17:00.'),
             R('16:45', f'{L("janjan")} into {L("shinsekai")}', f'Taxi, about 10 minutes. Sunset 17:05. {L("kushikatsu")} under Tsūtenkaku, kept to a snack.'),
             R('18:30', f'{L("dotonbori")}', f'Buy {L("tombori")} tickets, then takoyaki standing up. The {L("glico")} photo platform is at Nanohana, opposite the sign.'),
             R('20:15', f'{L("hozenji")}', 'Lanterns, the mossy Fudō and a quiet drink.'),
             R('21:00', 'Home', f'Midōsuji line to Umeda, {L("jr-rapid")} to Kyoto, one {L("subway-k", "subway")} stop to Gojō. At the hotel about 22:15, with the bags waiting.')],
            [('Lighter version', 'Nara as written in the master, Nigatsu-dō included, back by 17:25 and Pontochō for dinner. Osaka drops out completely.'),
             ('Weather', 'JMA has 50% for Nara in the afternoon, about 4 mm on one model. Tōdai-ji first if it is wet.'),
             ('Left out of Osaka', 'The castle, Umeda Sky, Kuromon and the Horie run. Ginza on Sunday is already the fallback for resale shopping.')]),
        day(22, 'Thursday', 'Kyoto', ['k'], 'Kyoto proper, the dry day',
            'The master\'s Friday, moved up a day onto the one dry day of the leg. tenki.jp has 20% all day with no measurable rain.',
            KYOTO_PROPER,
            [('Bookings', 'The Gion dinner moves to Thursday 18:30. Book it for Thursday now, as all three scenarios use it.')]),
        day(23, 'Friday', 'Kyoto to Tokyo', ['k', 'g'], 'Inari in the rain, Tokyo by mid afternoon',
            'The master\'s Saturday morning, a day early. Rain from early morning in Kyoto, about 17 mm on tenki.jp and up to 84 mm on one model. The room is yours all day, so there is no checkout rush.',
            clean([R('07:00', f'To {L("kyoto-st")}, {L("inari-st")}', 'Two stops, about 5 minutes. A taxi from the hotel is 10 minutes if it is pouring.'),
             R('07:15', f'{L("fushimi")}', f'The gate tunnels give some shelter and the rain keeps people away. In light rain go up to {L("yotsutsuji")}. If it is heavy, do the first gates and back, about 45 minutes. Steps are slippery.'),
             R('09:00', 'Back to the hotel', 'Breakfast, shower, pack slowly.'),
             R('10:45', f'Taxi to {L("kyoto-st")} with the bags', 'Not a day to walk Karasuma-dōri with suitcases.'),
             R('11:00', f'Ramen at {L("daiichi")}, or an ekiben', 'Five minutes from the station, open Fridays.'),
             R('11:30', f'{L("shinkansen", "Nozomi")} to Tokyo', 'Target 11:30 to 12:00, Green Car with the oversized baggage area. Train details go here once booked.', 'tb'),
             R('14:00', f'{L("tokyo-st")}', 'Yaesu side for the taxi rank.')] + fri_tokyo_evening('14:30')),
            [('Go earlier if', 'Thursday night\'s forecast brings the typhoon into Friday, or JR Central announces planned suspensions. Skip Inari and take a morning train.')]),
        sat()])

# ---------- scenario 2 ----------
S2 = dict(id='s2', no='Scenario 2', name='Straight to Osaka',
    pick='Inari on the dry day',
    idea=f'Off the Shinkansen and straight on to Osaka for a full city day, Umeda Sky at night included. Dry Thursday takes {L("fushimi")} at sunrise, then Nara, then Higashiyama and Gion. {L("arashiyama")} moves to Friday morning, the part of Kyoto that copes best with rain.',
    best='Osaka almost complete. Inari, the climb that suffers most in rain, gets the dry morning.',
    cost='Nishiki Market (it can slot into Friday). Thursday is the biggest day on foot of the trip: a mountain, then Nara, then Higashiyama.',
    leave='Fri, about 12:30',
    glance=['Osaka, castle to Umeda Sky at night', 'Inari at sunrise, Nara, Higashiyama, Gion', 'Arashiyama in the rain, Tokyo by 15:15', 'Typhoon day, under cover'],
    days=[
        day(21, 'Wednesday', 'Osaka', ['k'], 'Straight on to Osaka',
            'Most of the master\'s Osaka day, started at Kyoto Station. Wednesday has showers about on some models, and the arcades are covered.',
            [NOZOMI13, KYOTO10, BAGS,
             R('10:30', f'{L("jr-rapid")} to Osaka', 'About 30 minutes, then the Osaka Loop Line to Osakajōkōen.'),
             R('11:15', f'{L("castle")}, up close', f'Through the park to the foot of the tower. Buy the {L("ecocard")} at Tanimachi 4-chōme afterwards.'),
             R('12:30', f'{L("kuromon")} lunch', 'Sennichimae line to Nippombashi, two stops. Lunch, not a snack stop.'),
             R('13:45', f'{L("horie")}', 'The vintage and resale run. Passports for tax-free.'),
             R('15:45', f'{L("namba-yasaka")}', 'Closes about 17:00.'),
             R('16:30', f'{L("janjan")} into {L("shinsekai")}', f'In at dusk as the signs come on. Sunset 17:05. {L("kushikatsu")}, kept to a snack.'),
             R('18:15', f'{L("dotonbori")}', f'{L("tombori")} after dark, takoyaki, the {L("glico")} platform.'),
             R('20:00', f'{L("hozenji")}', 'A quiet drink.'),
             R('20:45', f'{L("umeda")} at night', 'Midōsuji line to Umeda. Open to 22:30. The night deck replaces the morning one.'),
             R('21:45', 'Home', f'{L("jr-rapid")} from Osaka Station, then one {L("subway-k", "subway")} stop. At the hotel about 22:45.')],
            [('Check the day', 'The master\'s closure notes are for a Thursday. Check Google Maps for Wednesday hours at Kuromon and anywhere you plan to eat.'),
             ('Swap the deck', 'If the evening clears, Umeda Sky at night. If it is clouded in, go home straight from Hōzenji.')]),
        day(22, 'Thursday', 'Inari, Nara, Kyoto', ['k'], 'Inari at sunrise, Nara, Higashiyama',
            'The dry day carries the two things rain would hurt most: the Inari climb and the open lawns of Nara. Higashiyama and Gion finish it as in every scenario.',
            [R('06:00', f'Taxi to {L("fushimi")}', 'About 10 minutes. Sunrise is about 06:10.'),
             R('06:15', f'{L("fushimi")}', f'Up to {L("yotsutsuji")} for the view over the city and back, about two hours. Empty at this hour.'),
             R('08:30', f'{L("inari-st")} on to Nara', 'The JR Nara line runs from the platform facing the gate. About an hour, some trains need a change. Breakfast from a convenience store on the way.'),
             R('09:30', f'{L("todaiji")}', 'Open from 07:30, ahead of most school groups.'),
             R('10:30', f'{L("narapark")}, {L("kasuga")}', f'{L("deer-crackers", "Deer crackers")}, then the lantern path.'),
             R('12:00', 'Lunch on Sanjō-dōri', f'{L("kakinoha")}, then {L("nakatanido")}.'),
             R('12:45', f'Kintetsu from {L("kintetsu-nara")} to Kyoto', 'About 45 minutes. One subway stop to Gojō.'),
             R('13:45', 'Hotel and rest', f'The {L("jidai")} parade is on in the centre until mid afternoon.'),
             R('15:15', f'Taxi to {L("kiyomizu")}', 'Closes 18:00.'),
             R('16:30', f'Down through {L("sannenzaka")}', ''),
             R('17:10', f'{L("yasaka-pagoda")} at sunset', ''),
             R('17:30', f'{L("yasaka")}, then into {L("gion")}', f'{L("hanamikoji")}, the {L("shirakawa", "Shirakawa canal")}.'),
             R('18:30', f'Dinner in {L("gion")}', 'Book for Thursday.', 'tb')],
            [('Shorter Inari', 'If the legs are needed for Nara, stop at the first gate tunnels and the lower loop, about 45 minutes, and catch an earlier train.')]),
        day(23, 'Friday', 'Kyoto to Tokyo', ['k', 'g'], 'Arashiyama in the rain, Tokyo by mid afternoon',
            'The bamboo grove is a short, flat walk that stays beautiful in the rain and empties out. Nishiki on the way back, which is covered.',
            clean([R('07:00', 'Leave the hotel', f'Taxi or {L("subway-k", "subway")} to {L("kyoto-st")}, JR Sagano line to Saga-Arashiyama.'),
             R('07:30', f'{L("bamboo", "Bamboo grove")}', 'Ten to fifteen minutes end to end. Umbrellas up, very few people.'),
             R('08:30', f'{L("tenryuji")} as it opens', 'The garden in the rain is the reward.'),
             R('09:15', f'Coffee in {L("arashiyama")}', ''),
             R('09:45', f'Hankyu to Karasuma, {L("nishiki")}', 'Covered all the way. Brunch at the stalls from about 10:30.'),
             R('11:15', 'Walk to the hotel, shower and pack', 'About 15 minutes south.'),
             R('12:00', f'Taxi to {L("kyoto-st")}', ''),
             R('12:30', f'{L("shinkansen", "Nozomi")} to Tokyo', 'Target about 12:30. Train details go here once booked.', 'tb'),
             R('14:45', f'{L("tokyo-st")}', '')] + fri_tokyo_evening('15:15')),
            [('Go earlier if', 'The typhoon speeds up. Drop Arashiyama, do Nishiki at 10:00 and take a morning train.')]),
        sat()])

# ---------- scenario 3 ----------
S3 = dict(id='s3', no='Scenario 3', name='Kyoto to the last, late train',
    pick='Most time in Kyoto',
    idea=f'Wednesday and Thursday as in Scenario 1, then a full wet-weather Friday in Kyoto: {L("fushimi")}, the sake district, {L("sanjusangendo")}, the covered arcades and a massage, with a train at about 16:00.',
    best='Uses the Kyoto room you have already paid for, and every Friday stop is under cover or works in rain.',
    cost='The most exposure to the typhoon. Later trains are the first to be suspended or packed with people moving Saturday travel forward. Tokyo has 41 mm forecast on Friday too.',
    leave='Fri, about 16:00',
    glance=['Nara, then Osaka at night', 'Arashiyama, Nishiki, Higashiyama, Gion', 'Inari, sake, Sanjūsangen-dō, Tokyo by 18:30', 'Typhoon day, under cover'],
    days=[
        day(21, 'Wednesday', 'Nara, then Osaka', ['k'], 'Nara, then Osaka at night',
            'Exactly as Scenario 1.',
            [NOZOMI13, KYOTO10, BAGS,
             R('10:45', 'Train to Nara', 'Kintetsu, about 45 minutes.'),
             R('11:30', f'{L("nara")}', 'Lunch, deer, Kasuga Taisha, Tōdai-ji. Down to Kintetsu Nara by 15:05.'),
             R('15:20', f'Kintetsu direct to {L("namba")}', ''),
             R('16:10', f'{L("namba-yasaka")}, {L("shinsekai")} at dusk', ''),
             R('18:30', f'{L("dotonbori")}, then {L("hozenji")}', ''),
             R('21:00', 'Home', 'At the hotel about 22:15.')],
            [('Lighter version', 'Nara as written in the master, then Pontochō. Worth considering here, as Friday is also a full day.')]),
        day(22, 'Thursday', 'Kyoto', ['k'], 'Kyoto proper, the dry day',
            'Exactly as Scenario 1.',
            KYOTO_PROPER),
        day(23, 'Friday', 'Kyoto to Tokyo', ['k', 'g'], 'A wet Kyoto day under cover, then the late train',
            'Inari first, then a run of indoor and covered stops south and east of the station, and back to the room you still have.',
            clean([R('07:00', f'{L("inari-st")}', ''),
             R('07:15', f'{L("fushimi")}', 'As in Scenario 1. The short version if it is heavy.'),
             R('09:15', f'Keihan to Chūshojima, the {L("gekkeikan", "Fushimi sake district")}', f'Two stops. {L("gekkeikan")} opens 09:30 with a tasting. The canal and warehouses are the pretty part.'),
             R('11:00', f'Keihan to Shichijō, {L("sanjusangendo")}', '1,001 golden Kannon statues in one long hall. Indoors, shoes off. Five minutes from the station.'),
             R('12:15', f'Lunch in the {L("teramachi")}', 'Keihan to Gion-Shijō, then a 10 minute walk west. Covered arcades with plenty of places to eat.'),
             R('13:30', f'Massage at {L("yumemishi")}', 'Ten minutes west along Shijō. Or the room for a nap.'),
             R('14:45', 'Hotel, shower and pack', ''),
             R('15:30', f'Taxi to {L("kyoto-st")}', 'Ekiben for dinner on the train.'),
             R('16:00', f'{L("shinkansen", "Nozomi")} to Tokyo', 'Target about 16:00. Train details go here once booked.', 'tb'),
             R('18:15', f'{L("tokyo-st")}', '')] + fri_tokyo_evening('18:30')),
            [('Other covered stops', f'{L("honganji")} on the walk to the station, the {L("teramachi")}, the {L("railmuseum")}, or {L("kyoto-st-building", "the Kyoto Station building")}.'),
             ('Fall back to Scenario 1', 'If JR Central flags suspensions or heavy rain limits for the afternoon, cut after Inari and take a late morning train.')]),
        sat()])

SCEN = [S1, S2, S3]

def glance():
    rowsd = [('Wed 21', 0), ('Thu 22', 1), ('Fri 23', 2), ('Sat 24', 3)]
    h = '<div class="gl"><div class="glh"><span></span>' + ''.join(f'<a href="#{s["id"]}" data-go="{s["id"]}"><b>{s["no"][-1]}</b>{E(s["name"])}</a>' for s in SCEN) + '</div>'
    for lab, i in rowsd:
        h += f'<div class="glr"><span class="gld">{lab}</span>' + ''.join(f'<span class="glc">{E(s["glance"][i])}</span>' for s in SCEN) + '</div>'
    h += '<div class="glr glx"><span class="gld">Leave Kyoto</span>' + ''.join(f'<span class="glc">{E(s["leave"])}</span>' for s in SCEN) + '</div></div>'
    return h

def panel(s, first):
    return (f'<section class="scen" id="{s["id"]}" data-s="{s["id"]}"{"" if first else " hidden"} aria-labelledby="t-{s["id"]}">'
            f'<div class="sbox"><p class="eyebrow">{s["no"]} <span class="pick">{E(s["pick"])}</span></p><h2>{E(s["name"])}</h2>'
            f'<p class="lede">{s["idea"]}</p><dl class="notes"><div><dt>Why</dt><dd>{s["best"]}</dd></div><div><dt>What it costs</dt><dd>{s["cost"]}</dd></div></dl></div>'
            + ''.join(s['days']) + '</section>')

EXTRA_CSS = '''<style>
.tb-cover{padding-block:2.2rem .4rem}
.tb-cover .band{height:12px}
.tb-cover h1{margin-top:1.4rem}
.tb-sub{margin-top:1rem;color:var(--mute);font-size:1.02rem;max-width:40rem}
.draft{display:inline-block;margin-top:.9rem;font:700 .72rem var(--body);text-transform:uppercase;letter-spacing:.08em;border:1.5px dashed var(--ink);padding:.3rem .5rem}
.eyebrow{font:700 .72rem var(--body);text-transform:uppercase;letter-spacing:.09em}
.sit{margin-top:1.6rem;border:1.5px solid var(--ink)}
.sit>.band{height:10px}
.sitin{padding:1rem;display:grid;gap:.9rem}
.wx{display:grid;gap:.45rem}
.wx li{display:grid;grid-template-columns:4.2rem minmax(0,1fr);gap:.6rem;font-size:.92rem;line-height:1.4;border-top:1px solid var(--line);padding-top:.45rem}
.wx li b{font-variant-numeric:tabular-nums}
.wx li span{min-width:0}
.todo{display:grid;gap:.45rem;font-size:.92rem}
.todo li{padding-left:1.1rem;position:relative;line-height:1.4}
.todo li::before{content:"";position:absolute;left:0;top:.45em;width:.5rem;height:.5rem;border:1.5px solid var(--ink)}
.tl{display:grid;gap:0;font-size:.92rem}
.tl li{display:grid;grid-template-columns:5.6rem minmax(0,1fr);gap:.7rem;padding:.5rem 0;border-top:1px solid var(--line)}
.tl li b{font-variant-numeric:tabular-nums}
.gl{margin-top:1rem;border:1.5px solid var(--ink);font-size:.82rem;line-height:1.3}
.glh,.glr{display:grid;grid-template-columns:3.6rem repeat(3,minmax(0,1fr))}
.glh a{display:grid;gap:.15rem;padding:.55rem .5rem;text-decoration:none;font-weight:600;border-left:1.5px solid var(--ink);background:var(--paper)}
.glh a b{font:800 1.5rem/1 var(--display)}
.glh a:hover{background:var(--ink);color:var(--paper)}
.glr{border-top:1px solid var(--line)}
.gld{padding:.5rem .4rem .5rem .5rem;font-weight:700}
.glc{padding:.5rem;border-left:1.5px solid var(--ink);min-width:0}
.glx{border-top:1.5px solid var(--ink);font-weight:600}
.stabs{position:sticky;top:env(safe-area-inset-top,0px);z-index:6;background:var(--paper);border-bottom:1.5px solid var(--ink);margin-top:2.4rem}
.stabs div{max-width:52rem;margin:0 auto;padding:.5rem 1.1rem;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:4px}
.stabs button{appearance:none;border:1.5px solid var(--ink);background:var(--paper);color:var(--ink);padding:.45rem .5rem .5rem;text-align:left;cursor:pointer;font:600 .78rem/1.2 var(--body);display:grid;gap:.1rem;min-width:0}
.stabs button b{font:800 1.05rem/1.1 var(--display)}
.stabs button[aria-selected="true"]{background:var(--ink);color:var(--paper)}
.sbox{margin-top:1.6rem;padding:1.1rem 1rem 1.2rem;border:3px solid var(--ink);display:grid;gap:.6rem}
.sbox h2{font:800 clamp(1.9rem,7.5vw,2.8rem)/1 var(--display);letter-spacing:-.03em;text-wrap:balance}
.sbox .lede{margin-top:.2rem;font-size:1.04rem}
.sbox .notes{margin-top:.2rem}
.pick{display:inline-block;margin-left:.4rem;background:var(--ink);color:var(--paper);padding:.15rem .4rem;letter-spacing:.06em}
.qa{margin-top:3rem;padding-top:1rem;border-top:3px solid var(--ink)}
.qa h2{font:800 1.7rem/1.1 var(--display);letter-spacing:-.02em}
.qa article{margin-top:1.2rem;border:1.5px solid var(--ink);padding:1rem 1rem 1.1rem;display:grid;gap:.5rem}
.qa h3{font:700 1.15rem/1.25 var(--display)}
.qa p{color:var(--mute);font-size:.94rem;max-width:42rem}
.qa p b{color:var(--ink)}
.train{border-style:dashed!important}
.end{margin:3rem 0 3.5rem;font-size:.82rem;color:var(--mute)}
.lnk{font-size:.86rem;margin-top:.5rem}
@media (min-width:640px){.sitin{padding:1.2rem 1.5rem}.glh,.glr{grid-template-columns:5rem repeat(3,minmax(0,1fr))}.stabs button{font-size:.86rem}.sbox{padding:1.3rem 1.5rem 1.4rem}}
</style>'''

SHEET = master[master.find('<aside class="sheet"'):master.find('</aside>', master.find('<aside class="sheet"')) + 8]

body = f'''
<main>
<header class="wrap tb-cover">
 <div class="band" aria-hidden="true"><i class="pat pat-k"></i><i class="pat pat-g"></i></div>
 <h1>Kyoto &amp; Tokyo<span>Typhoon Backup</span></h1>
 <p class="tb-sub">If a typhoon threatens Saturday 24, you travel to Tokyo on Friday 23 instead, sleep at the {L("mercure", "Mercure Tokyo Hibiya")} and give up the last Kyoto night. Three ways to run Wednesday 21 to Saturday 24. Separate from the Master Itinerary, which stays as it is.</p>
 <p class="draft">Draft, Thu 15 October 2026</p>

 <section class="sit" aria-labelledby="sith">
  <div class="band" aria-hidden="true"><i class="pat pat-k"></i><i class="pat pat-g"></i></div>
  <div class="sitin">
   <p class="eyebrow" id="sith">Why there is a backup</p>
   <ul class="wx">
    <li><b>Wed 21</b><span>Nara: cloud and sun, afternoon showers possible, 0 to 4 mm.</span></li>
    <li><b>Thu 22</b><span><strong>The dry day.</strong> Kyoto 20%, Osaka 40%, no measurable rain.</span></li>
    <li><b>Fri 23</b><span>Kyoto rain from early morning: about 17 mm on tenki.jp, up to 84 mm on one model. Tokyo about 41 mm.</span></li>
    <li><b>Sat 24</b><span>Tokyo heavy rain all day, about 81 mm, possibly Typhoon No. 30. Kyoto dry in the morning. The track firms up from about Mon 19.</span></li>
   </ul>
   <p class="lnk">From the Trip Weather check, Thu 15 Oct, 07:50. <a href="https://thestartupstudiodeveloper.github.io/japan-trip/weather/">Open Trip Weather</a></p>
  </div>
 </section>

 <h2 class="sec">At a glance</h2>
 {glance()}
</header>

<nav class="stabs" aria-label="Scenarios"><div role="tablist">
 {''.join(f'<button type="button" role="tab" id="t-{s["id"]}" aria-controls="{s["id"]}" aria-selected="{"true" if n == 0 else "false"}" data-s="{s["id"]}"><b>{s["no"]}</b>{E(s["name"])}</button>' for n, s in enumerate(SCEN))}
</div></nav>

<div class="wrap">
 {''.join(panel(s, n == 0) for n, s in enumerate(SCEN))}

 <section class="qa" aria-labelledby="qah">
  <h2 id="qah">Deciding</h2>
  <article>
   <h3>Do before you fly</h3>
   <ul class="todo">
    <li>Book the Gion dinner for <b>Thursday 22</b>, 18:30. Every scenario has it on Thursday, and so does the weather swap if you don't leave early.</li>
    <li>Ask sequence KYOTO GOJO whether it accepts Crosta bag deliveries on Wed 21.</li>
    <li>Keep the Hilton's reply on the fireworks and Seascape dinner terms with this page.</li>
    <li>For the insurance claim on the lost Kyoto night: the Booking.com terms, screenshots of JMA warnings, and any JR Central suspension notice.</li>
   </ul>
  </article>
  <article>
   <h3>When to decide</h3>
   <ul class="tl">
    <li><b>Mon 19</b><span>The typhoon's track should firm up. Check Trip Weather.</span></li>
    <li><b>Wed 21, 10:00</b><span>Pick Wednesday's shape at Kyoto Station: Nara then Osaka, straight to Osaka, or the lighter Nara and Pontochō. It decides whether the bags go to the hotel. The Osaka night costs nothing if you end up staying.</span></li>
    <li><b>Thu 22, 18:00</b><span>Go or stay. Cancel the Mercure by now if staying. If going, book Friday's Nozomi and cancel Saturday's.</span></li>
    <li><b>Thu 22, night</b><span>Last look at the forecast and JR Central. Move the Friday train earlier if needed.</span></li>
   </ul>
  </article>
  <article>
   <h3>Fushimi Inari or the bamboo grove on the dry morning?</h3>
   <p><b>Inari is the bigger experience</b>: two hours up a mountain through thousands of gates, on stone steps, with a view from {L("yotsutsuji")}. It is also the one rain hurts most, because the steps get slippery and cloud takes the view. <b>The bamboo grove</b> is ten to fifteen minutes on a flat path and holds up well in rain, often better, with fewer people.</p>
   <p>So the safer use of dry Thursday is Inari, which is Scenario 2. The case for Scenarios 1 and 3 is distance: Inari is five minutes from Kyoto Station, which makes it the easy thing to fit before a train, while Arashiyama is 35 minutes out. In light rain Inari is still lovely. If Friday firms up as the 84 mm version, lean to Scenario 2.</p>
  </article>
  <article>
   <h3>Do we still do Nara?</h3>
   <p>Yes, in all three. Scenarios 1 and 3 keep it on Wednesday and trim the end. Scenario 2 moves it to Thursday morning, straight from Inari on the same train line.</p>
  </article>
  <article>
   <h3>If you stay after all</h3>
   <p>Wednesday and Thursday play out the same either way. In Scenarios 1 and 3, Friday becomes a wet day of your choice: the covered stops from Scenario 3, or Osaka's arcades and Kuromon. In Scenario 2 it becomes Arashiyama and Nishiki with a free afternoon. Saturday keeps Nozomi 16 at 12:01 as booked, and with Inari already done, the morning is free.</p>
  </article>
  <article class="train">
   <h3>Bullet train backup</h3>
   <p>To come. The Friday Nozomi options, seats and the Saturday cancellation go here once a scenario is picked.</p>
  </article>
 </section>
 <p class="end">Kyoto &amp; Tokyo Typhoon Backup. Draft, 15 October 2026. Times are targets, not commitments, unless marked booked.</p>
</div>
</main>
'''

used_P = {k: P[k] for k in sorted(used)}
SCRIPT = '''<script>
(function(){
 var P=%s,sheet=document.getElementById('sheet'),cur=null;
 function shut(){sheet.hidden=true;if(cur){cur.setAttribute('aria-expanded','false');cur=null}}
 document.addEventListener('click',function(e){
  var b=e.target.closest('.pl');
  if(b){e.preventDefault();var d=P[b.dataset.p];if(!d)return;
   if(cur===b){shut();return}
   if(cur)cur.setAttribute('aria-expanded','false');
   cur=b;b.setAttribute('aria-expanded','true');
   document.getElementById('sh-n').textContent=d.n;document.getElementById('sh-l').textContent=d.l;
   document.getElementById('sh-w').textContent=d.w;document.getElementById('sh-t').textContent=d.t||'';document.getElementById('sh-tb').hidden=!d.t;
   document.getElementById('sh-p').href='https://www.google.com/search?tbm=isch&q='+encodeURIComponent(d.m);
   document.getElementById('sh-m').href='https://www.google.com/maps/search/?api=1&query='+encodeURIComponent(d.m);
   sheet.hidden=false;sheet.scrollTop=0;return}
  if(e.target.closest('#sh-x')||!e.target.closest('.sheet'))shut();
 });
 document.addEventListener('keydown',function(e){if(e.key==='Escape')shut()});

 var KEY='jhk-typhoon-tab',tabs=[].slice.call(document.querySelectorAll('.stabs button')),panels=[].slice.call(document.querySelectorAll('.scen'));
 function show(id,scroll){
  if(!document.getElementById(id))return;
  tabs.forEach(function(t){t.setAttribute('aria-selected',t.dataset.s===id?'true':'false')});
  panels.forEach(function(p){p.hidden=p.dataset.s!==id});
  try{localStorage.setItem(KEY,id)}catch(e){}
  if(scroll){var nav=document.querySelector('.stabs');window.scrollTo({top:nav.getBoundingClientRect().top+scrollY-(parseFloat(getComputedStyle(nav).top)||0),behavior:'smooth'})}
 }
 tabs.forEach(function(t){t.addEventListener('click',function(){show(t.dataset.s,true)})});
 document.querySelectorAll('[data-go]').forEach(function(a){a.addEventListener('click',function(e){e.preventDefault();show(a.dataset.go,true)})});
 var h=(location.hash||'').slice(1),saved=null;try{saved=localStorage.getItem(KEY)}catch(e){}
 if(/^s[123]$/.test(h))show(h,false);else if(saved)show(saved,false);
})();
</script>''' % json.dumps(used_P, ensure_ascii=False).replace('</', '<\\/')

TITLE = 'Kyoto &amp; Tokyo Typhoon Backup'
fragment = f'<title>{TITLE}</title>\n' + STYLES + EXTRA_CSS + body + SHEET + SCRIPT
page = ('<!doctype html>\n<html lang="en-AU">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
        f'<title>{TITLE}</title>\n<meta name="robots" content="noindex, nofollow">\n<meta name="theme-color" content="#000000">\n'
        '<link rel="apple-touch-icon" href="../icon-180.png">\n<link rel="icon" type="image/png" href="../icon-192.png">\n'
        + STYLES + EXTRA_CSS + '\n</head>\n<body>' + body + SHEET + SCRIPT + '\n</body>\n</html>\n')

for bad in ['—', '--']:
    txt = re.sub(r'<style>.*?</style>|<script>.*?</script>', '', body, flags=re.S)
    if bad in txt:
        sys.exit('Found a dash: ' + bad)

os.makedirs(os.path.join(ROOT, 'typhoon'), exist_ok=True)
open(os.path.join(ROOT, 'typhoon', 'index.html'), 'w', encoding='utf-8').write(page)
open(os.path.join(ROOT, 'source', 'typhoon', 'typhoon-backup.html'), 'w', encoding='utf-8').write(fragment)
print('ok', len(page), 'bytes,', len(used_P), 'place cards')
