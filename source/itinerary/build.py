import base64, glob, hashlib, html, json

def b64(p):
    return base64.b64encode(open(glob.glob(p)[0], 'rb').read()).decode()

E = html.escape
B, TB = 'b', 'tb'   # booked or fixed, to book

LEGS = {
 's': dict(n=1, name='Shibuya, Shinjuku and Yokohama', short='Shibuya', kanji='渋谷', dates='Sat 17 to Wed 21 October', hotel='Sequence Miyashita Park, 4 nights', pat='Solid',
           sum='An easy first day on foot, a festival weekend with Street Kart, a big Shinjuku night, old Tokyo at Asakusa and the waterfront at Yokohama, then an early Shinkansen to Kyoto.'),
 'k': dict(n=2, name='Kyoto, Nara and Osaka', short='Kyoto', kanji='京都', dates='Wed 21 to Sat 24 October', hotel='sequence KYOTO GOJO, 3 nights', pat='Stripes',
           sum='One clear idea a day. Nara on arrival, a full day in Osaka, Kyoto proper on Friday, and Fushimi Inari before the train back to Tokyo.'),
 'g': dict(n=3, name='Tokyo: Hibiya and Ginza', short='Hibiya', kanji='銀座', dates='Sat 24 to Tue 27 October', hotel='Hotel The Blossom Hibiya, 3 nights', pat='Centre bar',
           sum='Fireworks on arrival night, a slow Sunday that turns into a full Ginza day, teamLab first thing Monday, a casual last night in Shimbashi, and an early run to Haneda.'),
 'h': dict(n=4, name='Hong Kong', short='Hong Kong', kanji='香港', dates='Tue 27 to Sat 31 October', hotel='Sheraton Hong Kong Hotel & Towers, 3 nights. Harbour view king with club lounge',
           pat='Diagonal',
           sum='Pool time in the sunny hours and evenings in the city. Thursday is the Big Buddha day and Friday is a pool day at the W before the 00:30 flight home. Wednesday, Thursday and Friday can swap to suit the weather.'),
}

def R(t, p, n='', s=''):
    return (t, p, n, s)

KAMAKURA = [
 R('08:00', 'JR Shōnan-Shinjuku line to Kamakura', 'About an hour, direct.'),
 R('09:15', 'Tsurugaoka Hachimangū, Komachi-dōri'),
 R('11:00', 'Enoden to Hase', 'The little seaside train.'),
 R('11:15', 'Hase-dera, then the Great Buddha'),
 R('12:30', 'Lunch in Hase or Kamakura'),
 R('14:00', 'JR to Yokohama', 'About 25 minutes.'),
 R('14:45', 'Minato Mirai waterfront', 'Red Brick Warehouses, the harbour, the skyline.'),
 R('17:30', 'Chinatown dinner'),
 R('19:30', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change.'),
]

EAST = [
 R('08:30', 'Ginza line from Shibuya to Asakusa', 'Direct, about 35 minutes.'),
 R('09:05', 'Sensō-ji, Kaminarimon, Nakamise street', 'The gate and its lantern, the shopping street, then the temple.'),
 R('10:15', 'Skytree views, no deck', 'Free 8th floor terrace at the Asakusa Culture Tourist Information Centre, opposite Kaminarimon. Then Azuma-bashi bridge, five minutes away.'),
 R('10:45', 'Kappabashi kitchenware street', 'Ten minutes west of the temple. Knives, ceramics, plastic food models. Buy only what fits in a daypack.'),
 R('12:30', 'Lunch in Asakusa'),
 R('13:30', 'Asakusa line from Asakusa towards Yokohama', 'About 50 minutes. Usually one change, at Sengakuji or Shinagawa, then one JR stop to Sakuragichō.'),
 R('14:45', 'Sakuragichō, Air Cabin, Minato Mirai waterfront', 'The cable car across the harbour, Red Brick Warehouses, the skyline.'),
 R('17:30', 'Chinatown dinner'),
 R('19:30', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change.'),
]

SHINJUKU = [
 R('09:00', 'Meiji Jingū', '15 minutes\' walk from the hotel. Quietest early.'),
 R('10:30', 'Yoyogi Park', 'The park side of Harajuku.'),
 R('12:00', 'Lunch, then to Shinjuku', 'JR Yamanote, a few minutes.'),
 R('13:30', 'Tokyo Metropolitan Government Building', 'Free observation deck in Kenzo Tange\'s twin towers. Check which deck is open.'),
 R('15:00', 'Shinjuku streets and shopping', 'Isetan, the east side, a rest stop.'),
 R('17:30', 'Omoide Yokochō', 'Yakitori in the smoky alleys.'),
 R('19:30', 'Kabukichō, Godzilla head'),
 R('21:00', 'Golden Gai', 'Tiny bars, some with cover charges. Hop around.'),
 R('Late', 'Taxi back to Shibuya', 'About 15 minutes.'),
]

DAYS = [
 dict(d=17, dow='Saturday', legs='s', cal='Land, Shibuya Sky', title='Arrive and wander Shibuya',
  sum='No trains after the airport and no schedule, just a slow loop on foot from the hotel while you wait for the room. Two fixed points: the landing and Shibuya Sky.',
  rows=[
   R('06:50', 'Land at Narita', 'Visit Japan Web QR codes ready. Allow about an hour to clear. Buy Suica cards at the airport.', B),
   R('Morning', 'Narita Express to Shibuya, bags to the hotel', 'Leave the bags at Sequence Miyashita Park and ask about early check-in. Then just head out the door.'),
   R('Late morning', 'Miyashita Park and Cat Street', 'Start on the rooftop park above the hotel, where the festival will be on. Then drift down Cat Street: vintage, streetwear, small cafés.'),
   R('Lunch', 'Harajuku and Omotesando', 'Up into the leafy avenue. Eat wherever looks good. Omotesando Hills, Tod\'s, Dior and Prada Aoyama are the architecture to look up at.'),
   R('Early arvo', 'Wander back into Shibuya', 'Hachikō, the Scramble Crossing, the side streets of Center-gai. Everything is within a 15 minute walk of the hotel.'),
   R('Mid arvo', 'Check in and rest', 'Shower, feet up.'),
   R('16:00', 'Shibuya Sky', 'Seven minutes\' walk. Up in daylight, sunset about 17:00, then the city lights come on.', B),
   R('Evening', 'Dinner close by', 'Nonbei Yokochō or Dōgenzaka, then an early night.'),
  ],
  sky=True),
 dict(d=18, dow='Sunday', legs='s', cal='Festival, Street Kart', title='Daikanyama, the festival, Street Kart',
  sum='A neighbourhood morning, the festival in full swing, then karting over the bay at golden hour.',
  rows=[
   R('09:00', 'Slow breakfast'),
   R('10:00', 'Daikanyama', 'One stop or a 15 minute walk. T-Site, the small streets and design shops.'),
   R('12:00', 'Lunch in Daikanyama or Ebisu'),
   R('13:15', 'Festival streets', 'Dōgenzaka, Bunkamura-dori, 109. The streets close for stages on Sunday. Dip in and out rather than chasing set times.'),
   R('14:45', 'Head to the Street Kart meeting point', 'Check the location on the booking and allow the travel time.'),
   R('15:30', 'Arrive 30 minutes early', 'International Driving Permit and passport in hand.'),
   R('16:00', 'Street Kart, Rainbow Bridge route', 'Golden hour over the bay.', B),
   R('Evening', 'Back to Shibuya, nice dinner', 'The festival will still have Shibuya buzzing.'),
  ],
  extra=('If Street Kart can\'t run today', [
   ('Today', 'Spend the extra time in Shibuya. Stay on the festival streets through the afternoon, then dinner as planned.'),
   ('Backup', 'Rebook for the following Sunday, 25 October, when you are staying in Hibiya. It is on that side of town, so it slots into the Ginza day. See Sunday 25.')])),
 dict(d=19, dow='Monday', legs='s', cal='Meiji, Shinjuku night', title='Meiji, Shinjuku, late night', group='sky',
  tabs=['Saturday', 'Monday', 'Tuesday'], tablabel='Shibuya Sky is on',
  alts=[dict(ttl='The Shinjuku day', show='0 1',
   sum='The big urban day. Shrine and park in the morning, Shinjuku in the afternoon, and let the night get progressively louder.',
   rows=SHINJUKU),
   dict(ttl='If Shibuya Sky is on Monday', show='1',
   sum='Same day, with a sunset break back in Shibuya. Three changes:',
   list=['Drop the 13:30 Government Building deck. The view comes at sunset instead.',
         'Come back to Shibuya about 16:15 for the booked sunset slot.',
         'Then JR back to Shinjuku, five minutes, for Omoide Yokochō, Kabukichō and Golden Gai as planned.']),
   dict(ttl='If Shibuya Sky is on Tuesday', show='2',
   sum='Monday and Tuesday swap. Today becomes the Asakusa and Yokohama day, exactly as written for Tuesday, and the Shinjuku day moves to Tuesday. The early start is easier after a moderate Sunday night.',
   rows=EAST, rows_noprint=True)]),
 dict(d=20, dow='Tuesday', legs='s', cal='Asakusa, Yokohama', title='Asakusa, Kappabashi and Yokohama', group='sky',
  tabs=['Saturday', 'Monday', 'Tuesday'], tablabel='Shibuya Sky is on',
  alts=[dict(ttl='The Asakusa and Yokohama day', show='0 1',
   sum='Old Tokyo in the morning with the Skytree in view, kitchenware street, then down the bay to Yokohama for the waterfront and Chinatown. Home in time to pack.',
   rows=EAST + [R('20:30', 'Pack', 'Tomorrow is an early start.')]),
   dict(ttl='Alternative morning: Kamakura', show='0 1',
   sum='Swap the Asakusa morning for the coast, temples and the Great Buddha. Join the plan above at 14:45.',
   list=['08:00 JR Shōnan-Shinjuku line to Kamakura, about an hour, direct.',
         '09:15 Tsurugaoka Hachimangū and Komachi-dōri.',
         '11:00 Enoden, the little seaside train, to Hase for Hase-dera and the Great Buddha.',
         '12:30 Lunch in Hase or Kamakura.',
         '14:00 JR to Yokohama, about 25 minutes.']),
   dict(ttl='If Shibuya Sky is on Tuesday', show='2',
   sum='Monday and Tuesday swap. Asakusa and Yokohama moves to Monday, and today becomes the Shinjuku day as written for Monday. Four changes:',
   list=['Shinjuku Gyoen is open on Tuesdays (not Mondays), so after lunch you can do the garden or the Government Building deck.',
         'Back to the hotel about 14:30 to pack for Wednesday, then Shibuya Sky at 16:00, the booked backup slot.',
         'JR to Shinjuku about 18:00 for Omoide Yokochō, Kabukichō and Golden Gai.',
         'Taxi back about 22:30. It is a 06:30 wake for the Shinkansen.'],
   rows=SHINJUKU, rows_noprint=True)]),
 dict(d=21, dow='Wednesday', legs='sk', cal='Shinkansen, Nara', title='Shibuya to Kyoto, straight out to Nara',
  sum='An early start with the bags on the train. Then Nara, which is flat, outdoors and forgiving, which is what a travel day wants.',
  rows=[
   R('06:30', 'Wake, final pack, check out'),
   R('07:00', 'Taxi to Shinagawa', 'About 20 to 25 minutes. Skip the train with bags at weekday rush hour.'),
   R('07:30', 'Shinagawa, ekiben and coffee', 'Breakfast on the train.'),
   R('07:55', 'Nozomi 13 to Kyoto', 'Car 9, seats 16-C and 16-D, Green Car with oversized baggage area. Fuji on the right at about 08:30.', B),
   R('10:00', 'Kyoto Station', '', B),
   R('10:15', 'Bags to Sagawa, Hachijō exit', 'Forwarded to sequence KYOTO GOJO. Don\'t detour there yourself, it costs you the afternoon.'),
   R('10:45', 'JR Nara line rapid', '45 minutes.'),
   R('11:30', 'Nara', 'Deer within five minutes of the station.'),
   R('12:00', 'Lunch on Sanjō-dōri, then into Nara Park'),
   R('13:00', 'Tōdai-ji and the Great Buddha', 'The one unmissable thing here.'),
   R('14:30', 'Kasuga Taisha, up through the lantern path', 'Quieter, wooded, and the better half of Nara.'),
   R('15:30', 'Isuien garden, or Nigatsu-dō', 'Pick one. Nigatsu-dō has the view back over the city.'),
   R('16:30', 'Train back', 'Kyoto by 17:15.'),
   R('17:30', 'Check in, then dinner around Pontochō or Shijō', 'From the hotel, Pontochō is about 15 minutes north on foot, or two stops on the Keihan line.'),
  ],
  foot='Skip Hōryū-ji and the western temples. Nara Park, Tōdai-ji, Kasuga Taisha and the deer is a full half day already.'),
 dict(d=22, dow='Thursday', legs='k', cal='Osaka day', title='Osaka, north to south to centre',
  sum='A whole day in Osaka, no Universal. Umeda Sky as it opens, Abeno Harukas at sunset, Dōtonbori at night. No backtracking.',
  rows=[
   R('07:15', 'JR special rapid from Kyoto', 'About 30 minutes. Get off at Osaka Station.'),
   R('08:15', 'Breakfast in Nakazakichō', 'cafe BONICO or Flinders Lane. Old wooden houses turned into cafes, ten minutes east of Umeda.'),
   R('09:10', 'Walk across to Umeda Sky Building', 'About 20 minutes, through Umeda and under the tracks.'),
   R('09:30', 'Umeda Sky deck as it opens', 'Two towers joined by a floating escalator. First in means the open-air deck before the tour groups. Check the opening time the night before.'),
   R('10:45', 'Nakanoshima', 'Central Public Hall in red brick, the Nakanoshima Museum of Art, and Tadao Ando\'s Children\'s Book Forest, which is free and worth it for the room alone.'),
   R('12:30', 'Kuromon Ichiba', 'Midōsuji line down to Namba. Grilled scallops, uni, tuna cut in front of you. This is lunch, not a snack stop.'),
   R('13:45', 'Shinsaibashi, Amerikamura and Horie', 'The vintage and secondhand luxury run: Kindal Horie, ALLU, KOMEHYO. Orange Street for furniture, design shops and coffee when you want it calmer.'),
   R('15:45', 'Shinsekai and Tsūtenkaku', 'A 1910s vision of the future, gone gloriously to seed. Kushikatsu under the tower, but keep it to a snack.'),
   R('16:30', 'Abeno Harukas 300', 'Ten minutes on foot from Shinsekai. Be on the deck by 16:40 for the 17:05 sunset and stay while the lights come on.', TB),
   R('18:30', 'Dōtonbori', 'Midōsuji line, Tennōji to Namba, 7 minutes. Eat standing up. Then Hōzenji Yokochō two streets back, stone lanes and lanterns, for a quiet drink after the noise.'),
   R('21:30', 'Midōsuji line to Umeda, train back to Kyoto', 'Trains run late, so there\'s no hard curfew.'),
  ],
  notes=[('Harukas ticket', 'Buy a dated ticket ahead if you can. If it\'s sold out or the sky is grey, skip it and take longer in Shinsekai. You\'ve already had a deck in the morning.'),
         ('Running late', 'Shorten Nakanoshima first, then Shinsekai. Protect lunch at Kuromon, the 16:40 deck and Dōtonbori.'),
         ('Left out', 'Osaka Castle, and Namba Yasaka Shrine with its giant lion head. The shrine is five minutes and fits before Shinsekai if you\'re ahead of time.')]),
 dict(d=23, dow='Friday', legs='k', cal='Arashiyama, Gion', title='Kyoto, west to east',
  sum='Arashiyama at dawn while it\'s empty, Higashiyama in the afternoon light, Gion for dinner.',
  rows=[
   R('06:45', 'Leave the hotel', 'Walk or short taxi to Kyoto Station, then the JR Sagano line to Saga-Arashiyama. About 30 minutes door to door.'),
   R('07:20', 'Bamboo grove', 'Genuinely empty before eight. This is the whole reason for the early start.'),
   R('08:30', 'Tenryū-ji as it opens', 'The pond garden backs onto the bamboo and most people walk straight past it.'),
   R('09:30', 'Ōkōchi Sansō villa, or Togetsukyō bridge and the river path', 'Pick one. The villa includes matcha.'),
   R('10:30', 'Proper breakfast in Arashiyama'),
   R('11:15', 'Back to the centre, lunch near Shijō'),
   R('14:15', 'Kiyomizu-dera', 'Uphill from the hotel, 20 minutes on foot. No transport needed. The stage view over the city is the thing.'),
   R('15:00', 'Down through Sannenzaka and Ninenzaka', 'Downhill from Kiyomizu, not uphill from Gion. Steep stone steps, slippery in rain. Or swap in Sanjūsangen-dō and its 1001 statues (closes 17:00), or Kōdai-ji, five minutes from Ninenzaka.'),
   R('16:15', 'Yasaka shrine, then down into Gion', 'Hanamikoji as the lanterns come on. Sunset is 17:10.'),
   R('18:30', 'Dinner in Gion or Pontochō', 'Book before you leave Melbourne. Friday walk-ins here are hard.', TB),
  ],
  notes=[('Gojo works in your favour', 'The hotel sits at the bottom of the Kiyomizu approach, so the whole afternoon is on foot. Arashiyama in the morning is the only leg that needs a train.'),
         ('Further north instead', 'Taxi to Ginkaku-ji at 13:30, walk the first stretch of the Philosopher\'s Path and duck into Hōnen-in, then pick up a taxi to Kiyomizu around 15:00. You lose an hour at Kiyomizu but gain the best garden of the three.'),
         ('Autumn colour', 'Late October is green and early gold, not red. Kyoto\'s maples turn mid to late November.')]),
 dict(d=24, dow='Saturday', legs='kg', cal='Inari, fireworks', title='Fushimi Inari, back to Tokyo, fireworks night',
  sum='Fushimi Inari at first light, the train back to Tokyo, an hour at the hotel, then fireworks over the bay from Odaiba. Dinner comes after the show, so the trains have cleared by the time you leave.',
  rows=[
   R('06:45', 'Keihan from Kiyomizu-Gojo to Fushimi Inari', 'Direct, about 8 minutes, no change. Sunrise is around 06:10.'),
   R('07:15', 'Fushimi Inari', 'Walk far enough up the mountain to lose everyone. A crush by ten.'),
   R('09:45', 'Back to the hotel, shower and repack'),
   R('10:45', 'Check out with the bags'),
   R('11:15', 'Kyoto Station. Ekiben and coffee', 'Lunch on the train buys you the morning. Fair trade.'),
   R('12:01', 'Nozomi 16 to Tokyo Station', 'Car 9, seats 1-C and 1-D, Green Car with the oversized baggage area. Seat D is the Fuji side, on your left this time.', B),
   R('14:15', 'Tokyo Station, Yaesu side taxi rank', 'Allow 15 minutes to clear the station. Saturday afternoon is busy. Ten to fifteen minutes to the hotel, roughly ¥1,500 to ¥2,000.', B),
   R('15:00', 'Check in at Hotel The Blossom Hibiya', 'An hour to shower, change and unpack. Take a layer, the bay is cool after dark.'),
   R('16:00', 'Walk to Shimbashi, Yurikamome to Daiba', 'About 15 minutes on the train. Go early, it gets crowded by 17:00. Sit at the front for the Rainbow Bridge loop.'),
   R('16:30', 'Hilton Tokyo Odaiba', 'Next to Daiba station. Collect the wristbands and find the viewing area before it fills. Sunset is about 16:55.'),
   R('17:30', 'Fireworks from the Hilton\'s private viewing area', 'Until 19:00. Seascape package, wristband needed.', B),
   R('19:30', 'Seascape dinner buffet', 'Until 21:15.', B),
   R('21:15', 'Optional: Odaiba Statue of Liberty', 'A few minutes\' walk from the Hilton on the waterfront, lit up with Rainbow Bridge behind it. Skip it if you are done.'),
   R('21:45', 'Yurikamome back to Shimbashi, walk to the hotel', 'The post-show rush is over by the time dinner ends. A taxi is quick if the platform is packed.'),
  ],
  foot='A long day: 06:45 start, back about 22:30. The hour at the hotel and a seated dinner are what make it work, so don\'t trade either away.'),
 dict(d=25, dow='Sunday', legs='g', cal='Gardens, Ginza', title='Slow start, gardens, then Ginza until you\'re done',
  sum='A sleep in, the gardens and Tokyo Station before midday, then the rest of the day and night in Ginza at your own pace. No bookings.',
  rows=[
   R('08:30', 'Slow breakfast near the hotel'),
   R('09:15', 'Imperial Palace East Gardens', 'About 15 minutes\' walk. Opens 09:00, free. Old castle keep foundations and the Ninomaru garden. Take your time.'),
   R('10:45', 'Tokyo Station, Marunouchi side', 'The red brick façade. KITTE\'s rooftop garden looks straight down on it. Coffee or a bite in the station.'),
   R('11:30', 'Tokyo International Forum', 'On the walk from the station into Ginza. Free to walk through the glass hall. Go up to the top walkway.'),
   R('12:00', 'Ginza goes car-free', 'Chūō-dōri is pedestrian only until 17:00. You\'re already into the shopping.'),
   R('Afternoon', 'Department stores and shopping', 'Mitsukoshi, Ginza Six, Matsuya, Dover Street Market, Itoya, vintage luxury resale. Maison Hermès, Mikimoto Ginza 2 and the Wakō clock tower as you go.'),
   R('Late arvo', 'Rooftop gardens', 'Ginza Six\'s rooftop garden and Mitsukoshi\'s rooftop terrace. A good break as the light goes.'),
   R('Evening', 'Eat in the complexes', 'Restaurant floors trade later than the shops. No booking, eat wherever appeals.'),
   R('When done', 'Walk back to the hotel', 'Five to ten minutes.'),
  ],
  foot='Browse the big stores before about 20:00 and eat after. Sunday restaurant floors queue around 18:30 to 19:30, so eat a touch earlier or later. Many smaller Ginza bars and restaurants close on Sundays. If it is wet, drop the gardens and start in Ginza earlier.',
  extra=('If Street Kart moved to today', [
   ('The backup for Sunday 18', 'Aim for the same 16:00 golden hour slot. Leave the Ginza shopping a little early, about 14:45, and arrive 30 minutes ahead with International Driving Permit and passports. Adjust to the slot you get.'),
   ('Afterwards', 'Back to Ginza for the late shops and dinner in the complexes. Shop floors close about 20:00 and the restaurant floors trade later. The rooftop gardens at dusk are what you give up.')])),
 dict(d=26, dow='Monday', legs='g', cal='teamLab, Shimbashi', title='teamLab first thing, a quiet afternoon, Shimbashi',
  sum='First slot at teamLab, coffee 33 floors up next to Tokyo Tower, a wander back via the temple, then an easy afternoon before a casual last night.',
  rows=[
   R('07:50', 'Stroll south from the Blossom', 'About 25 minutes via Toranomon. Or grab coffee near the hotel first. Taxi if it is wet.'),
   R('08:15', 'Coffee at Azabudai Hills', '% Arabica opens at 08:00. Pastries go fast.'),
   R('08:30', 'teamLab Borderless, first slot', 'Arrive a little early to be among the first in. Allow 2 to 2.5 hours. Monday 26 runs late, so a later slot works too if plans shift.', TB),
   R('10:45', 'Sky Room Café & Bar, 33F', 'Coffee with Tokyo Tower right alongside. The 33rd floor is only open to customers of Sky Room, Dining 33 or Hills House.'),
   R('11:45', 'Wander Azabudai Hills', 'The gardens and the precinct.'),
   R('12:15', 'Zōjō-ji and Shiba Park', 'About 10 minutes\' walk. The temple gate with Tokyo Tower behind it.'),
   R('13:00', 'Lunch nearby'),
   R('14:00', 'Back to the hotel', 'A 25 minute walk, or a short taxi.'),
   R('14:30', 'Chill, half pack'),
   R('18:00', 'Shimbashi, no booking', 'Five minutes from the hotel. Wander the lanes around the tracks, eat wherever looks good. Weeknights are when it\'s liveliest.'),
   R('20:00', 'Back to the hotel', 'Finish packing, settle the bill, book the 06:45 taxi at the front desk.'),
  ]),
 dict(d=27, dow='Tuesday', legs='gh', cal='Fly to Hong Kong', title='Haneda to Hong Kong, harbour night',
  sum='An early run to Haneda with the bags, then the first Hong Kong night on the harbour: a junk boat cruise timed for the 20:00 Symphony of Lights. No pool today, because the sun is nearly gone by check-in.',
  rows=[
   R('06:00', 'Wake, shower, final pack'),
   R('06:45', 'Taxi to Haneda Terminal 3', 'About 25 minutes at that hour. Keep some yen handy.'),
   R('07:15', 'Check in at the Cathay desks', 'Three hours before departure.'),
   R('07:45', 'Security and immigration', 'Usually quick, but allow for a queue.'),
   R('08:15', 'Breakfast airside', 'Spend leftover yen and IC card balance here.'),
   R('09:40', 'Boarding'),
   R('10:10', 'CX543 departs Haneda', 'Hong Kong is one hour behind Tokyo.', B),
   R('14:25', 'Land in Hong Kong', 'Allow 45 to 60 minutes for immigration, bags and customs.', B),
   R('15:20', 'Red urban taxi to the Sheraton', '20 Nathan Road, Tsim Sha Tsui. 35 to 45 minutes, roughly HK$300 to 350 with tolls and bag fees. Carry some cash.'),
   R('16:15', 'Check in at the Sheraton', 'Ask three things at the desk: whether pool sessions need booking, the club lounge hours, and a late checkout for Friday.'),
   R('17:15', 'Club lounge', 'Drinks and canapés as the harbour lights come on. Sunset is about 17:50.'),
   R('18:50', 'Walk to Tsim Sha Tsui Public Pier 1', 'Ten minutes from the hotel, behind the Cultural Centre. Queue early for the best seats.'),
   R('19:30', 'Aqua Luna harbour cruise', '45 minutes on a red-sail junk, one drink included.', TB),
   R('20:00', 'A Symphony of Lights', 'The nightly harbour light show. Lasers, searchlights and LED screens on the towers along both shores, set to music, for about ten minutes. You watch it from the boat.'),
   R('20:20', 'Avenue of Stars', 'Off the boat and along the Tsim Sha Tsui promenade. Handprints, the Bruce Lee statue and the full Island skyline.'),
   R('20:45', 'Dinner in Tsim Sha Tsui', 'Close to the promenade and the hotel.'),
   R('Late', 'Bar, or Temple Street night market', 'Only if you have the energy.'),
  ],
  notes=[('Latest safe timing in Tokyo', 'A 07:15 taxi gets you to Haneda by about 07:45, which is still 2.5 hours before departure.'),
         ('Instead of the taxi in Hong Kong', 'Airport Express to Kowloon Station, then a 5 to 10 minute taxi. For two people it costs about the same, with more bag handling.'),
         ('If the show has ended or the cruise is full', 'Watch from the Tsim Sha Tsui promenade, five minutes from the hotel. It faces the Hong Kong Island towers, which is the better side. Your harbour view room faces the same way.')]),
 dict(d=28, dow='Wednesday', legs='h', cal='Pool, the Peak', title='Pool, Hong Kong Island and the Peak',
  sum='The main Island day and the main night out. The Peak is timed for sunset.',
  rows=[
   R('09:00', 'Lounge breakfast'),
   R('09:45', 'Sheraton pool until about 14:00', 'Read, tan, swim. Light lunch at the hotel.'),
   R('14:30', 'Star Ferry to Central', 'Ten minutes across the harbour.'),
   R('15:00', 'Tai Kwun, PMQ, Mid-Levels escalator', 'Design and architecture, all within a few blocks.'),
   R('16:45', 'Peak Tram up', 'Prebook. Walk Lugard Road for the best free view.', TB),
   R('17:50', 'Sunset at the Peak', 'Stay while the city lights come on.'),
   R('19:30', 'Dinner in Central or SoHo', 'The big dinner of the trip. Book ahead.', TB),
   R('Late', 'Bars in Central', 'Taxi back through the tunnel, or a late train to the hotel. The MTR from Central to Tsim Sha Tsui is two stops and runs until after midnight.'),
   R('Optional', 'Or the old tram and the Star Ferry home', 'Instead of the taxi or train: ride the old tram from Central to Wan Chai, upper deck, about 15 minutes with the neon on. Then take the Star Ferry home from Wan Chai. It adds about half an hour. The last ferry from Wan Chai is 23:00, so leave the bars by about 22:15.'),
  ]),
 dict(d=29, dow='Thursday', legs='h', cal='Big Buddha, city', title='Ngong Ping cable car, Big Buddha, then the city',
  sum='Out to Lantau for the first cable car, back to the Island for lunch and the Sheung Wan shops, a rest at the hotel, then Temple Street at night.',
  rows=[
   R('08:00', 'Lounge breakfast'),
   R('08:45', 'Train to Tung Chung', 'About 50 minutes, one change.'),
   R('10:00', 'Ngong Ping 360 cable car up', 'First car, shortest queues. 25 minutes over the water and hills.', TB),
   R('10:30', 'Big Buddha, Po Lin Monastery, Wisdom Path', '268 steps up. Skip most of the village.'),
   R('12:45', 'Cable car down'),
   R('13:20', 'Train to Hong Kong Station, Central', 'About 30 minutes.'),
   R('14:00', 'Lunch in Central or Sheung Wan'),
   R('15:00', 'Sheung Wan shops', 'Hollywood Road, Cat Street antiques, vintage and resale. Don\'t forget Man Mo Temple, on Hollywood Road as you pass. Ten minutes inside.'),
   R('16:15', 'Egg tart and coffee stop'),
   R('17:00', 'Star Ferry from Central to Tsim Sha Tsui', 'On the water close to sunset, about 17:50.'),
   R('17:30', 'Rest at the hotel', 'Lounge drinks if you like.'),
   R('19:30', 'Temple Street dinner and night market', 'Claypot rice or street-side seafood, then browse the stalls. A 15 minute walk from the hotel.'),
   R('21:30', 'Back at the hotel', 'Or a bar nearby.'),
  ],
  extra=('Notes and optionals for Thursday', [
   ('If you skip the cable car and Big Buddha', 'Sleep in, then relax at the Sheraton pool until about 14:00, or take the Star Ferry across late morning and wander Central. Join the plan at lunch or at the Sheung Wan shops at 15:00.'),
   ('Weather', 'The cable car stops in high wind and the views vanish in low cloud. Check the forecast the night before and book as late as you can.'),
   ('Gentler start', 'Leave at 09:45 for an 11:00 cable car. Queues are longer, lunch moves to about 15:00 and the Sheung Wan shops shrink to an hour.'),
   ('Old tram', 'If you didn\'t ride it on Wednesday night, swap it in after the egg tart stop and take the ferry home from Wan Chai.')])),
 dict(d=30, dow='Friday', legs='h', cal='W pool, fly home', title='W pool day and departure',
  sum='Bags stay at the Sheraton, you shower at the W, and a taxi at 20:45 gets you to the airport three hours before the flight.',
  rows=[
   R('09:00', 'Lounge breakfast, pack', 'Day bag: swim gear, flight clothes, a plastic bag for wet things.'),
   R('12:00', 'Check out', 'Suitcases go to the Sheraton concierge.', B),
   R('12:30', 'W Hong Kong, WET pool deck, 76th floor', 'A 5 to 10 minute taxi. Day pass HK$750 per person on weekdays. Confirm the price and inclusions when booking.', TB),
   R('Afternoon', 'Pool, sun, reading, jacuzzi', 'Lunch poolside.'),
   R('17:50', 'Sunset from the deck'),
   R('18:15', 'Shower and change at the W', 'Changing rooms are part of the pass.'),
   R('18:45', 'Dinner', 'Near the W, or back in Tsim Sha Tsui close to the bags.'),
   R('20:30', 'Collect bags at the Sheraton', 'Repack the day bag in the lobby.'),
   R('20:45', 'Taxi to the airport', '30 to 40 minutes at that hour.'),
   R('21:30', 'Check in at the Cathay desks', 'Three hours before departure.'),
   R('00:30', 'CX105 departs for Melbourne', 'Saturday 31 October.', B),
  ],
  notes=[('Latest safe timing', 'A taxi at 21:15 puts you at the airport by 22:00, which is 2.5 hours before departure.'),
         ('If the Sheraton gives a late checkout', 'A 14:00 checkout means you can start the day at the Sheraton pool. A paid extension to 18:00 means you come back from the W at 17:00 and shower in your own room.'),
         ('If Friday is wet or grey', 'Skip the W. M+ and the West Kowloon waterfront is the indoor option, or take the Star Ferry across and wander Central. Checkout at 12:00 and the 20:45 taxi stay the same.')]),
]

SWAPS = [
 ('Ngong Ping on Friday, instead of Thursday', 'Replaces Friday morning. Check out by 08:00, first cable car at 10:00, at the W by about 15:00.', 'Costs the Friday sleep-in and about two hours of W pool time. A big day before a red-eye.'),
 ('Dragon\'s Back hike, then Shek O or Big Wave Bay beach', 'Replaces the Big Buddha on Thursday morning, from 08:30 to about 14:30.', 'Costs the cable car. Join Thursday\'s plan at the Sheung Wan shops at 15:00.'),
 ('W pool on Wednesday', 'Replaces that day\'s Sheraton pool block.', 'Costs nothing. Use this if Friday\'s forecast is cloudy, then swim at the Sheraton on Friday morning.'),
 ('M+ and West Kowloon waterfront', 'Replaces any pool block on a wet or grey day.', 'Costs pool time. It sits next to the W.'),
]

GOOD = {
 's': [('Light', 'Sunset about 17:00.'), ('Festival', 'Shibuya Music Festival on Sat 17 and Sun 18. Miyashita Park, right on top of the hotel, is one of the venues. Street stages on Sunday around Dōgenzaka, Bunkamura-dori and 109.'),
       ('Golden Gai', 'Many bars charge a small cover. Some are regulars only, so look for English signs.'),
       ('Getting around', 'Saturday is all on foot. Everything else is a short JR ride or walk from Shibuya.')],
 'k': [('Light', 'Sunrise about 06:10, sunset about 17:10. In Osaka on Thursday, 17:05.'),
       ('Fuji seats', 'Seat D is the Fuji side in both directions. The letters don\'t flip. Outbound it\'s on your right, return it\'s on your left.'),
       ('Closing times', 'Kiyomizu-dera 18:00. Sanjūsangen-dō 17:00. Ginkaku-ji 17:00. Abeno Harukas 22:00. Umeda Sky 22:30.'),
       ('Decided', 'No Universal. Thursday is the Osaka city day.')],
 'g': [('Light', 'Sunset about 16:55.'), ('Ginza car-free', 'Chūō-dōri closes to cars on weekends from 12:00 to 17:00.'),
       ('East Gardens', 'Closed Mondays and Fridays, so Sunday is the only day they fit.'),
       ('Spare night idea', 'Yūrakuchō\'s izakayas under the arches can take any Tokyo night.'),
       ('Getting around', 'Everything this leg is walkable or a 10 minute taxi from the hotel.')],
 'h': [('Weather', 'Late October is usually dry and in the mid to high 20s. Sunset is about 17:50.'),
       ('Best pool sun', 'Roughly 10:00 to 14:00. The Sheraton deck loses the sun by late afternoon.'),
       ('Light show', 'A Symphony of Lights runs nightly at 20:00 but is being retired in the second half of 2026, with no final date announced. Check it is still on in the week you fly. The cruise is worth doing either way.'),
       ('Races', 'Happy Valley is not running on Wed 28. That night\'s meeting is at Sha Tin, which is further out.'),
       ('Getting around', 'Red taxis cover Kowloon and Hong Kong Island, keep some cash on you. The Star Ferry, MTR and trams all take Octopus. Tsim Sha Tsui to Central is ten minutes by ferry.')],
}

CHECK = [
 ('Before you fly', [
  ('s', 'International Driving Permit, 1949 Geneva Convention version, for Street Kart'),
  ('s', 'Visit Japan Web registered for both of you'),
  ('s', 'Street Kart meeting point and arrival time, from the booking'),
  ('s', 'Street Kart: check the change and rebooking terms, in case Sun 18 is called off and it moves to Sun 25'),
  ('s', 'Shibuya Sky Monday and Tuesday slots: check the cancellation or change terms'),
  ('k', 'Abeno Harukas 300 sunset ticket for Thu 22'),
  ('k', 'Gion or Pontochō dinner for Fri 23, 18:30'),
  ('g', 'Confirm where and when the Seascape wristbands are collected on Sat 24'),
  ('g', 'teamLab Borderless for Mon 26, 08:30 first slot. Check the official calendar for that date'),
  ('h', 'Confirm CX543 and CX105 times in the Cathay app'),
  ('h', 'Hong Kong dollars for the airport taxi on arrival'),
  ('h', 'Aqua Luna Symphony of Lights cruise for Tue 27, 19:30 from Tsim Sha Tsui Pier 1'),
  ('h', 'Dinner booking in Central for Wed 28, 19:30'),
  ('h', 'Set up an Octopus card for ferries, trains and trams'),
  ('h', 'W Hong Kong WET day pass: price, inclusions, towels and showers, and whether it is tied to a date'),
 ]),
 ('Once you have seen the Hong Kong forecast', [
  ('h', 'Peak Tram tickets, around 16:45 on the clearest evening (Wed 28 by default)'),
  ('h', 'W pool day pass for the sunniest day (Fri 30 by default)'),
  ('h', 'Ngong Ping 360 cable car tickets, first car at 10:00 on Thu 29'),
 ]),
 ('On the ground', [
  ('s', 'Suica cards at Narita on arrival'),
  ('s', 'Ask Sequence Miyashita Park about early check-in on Sat 17'),
  ('g', 'Ask the Blossom about guest laundry, a week into the trip'),
  ('g', 'Settle the bill on Monday night for a quick checkout'),
  ('g', 'Book the 06:45 taxi to Haneda for Tue 27'),
  ('h', 'Sheraton: do pool sessions need booking? If so, book Wednesday morning'),
  ('h', 'Sheraton: club lounge hours for breakfast and evening drinks'),
  ('h', 'Sheraton: late checkout on Friday, 14:00 free or a paid extension to 18:00'),
  ('h', 'Sheraton: confirm the concierge will hold bags on Friday until 20:30'),
 ]),
]

exec(open('amendments_v2.py').read())
exec(open('amendments_v21.py').read())
exec(open('amendments_v22.py').read())
exec(open('amendments_v23.py').read())
exec(open('amendments_v24.py').read())
exec(open('amendments_v27.py').read())
exec(open('amendments_v2_master.py').read())
exec(open('amendments_v2_tsukiji.py').read())
exec(open('amendments_v2_ykyoto.py').read())
exec(open('amendments_v2_zflights.py').read())
exec(open('amendments_v2_zmore.py').read())

# ---------- render ----------
def tag(s):
    if s == B: return '<span class="tag tag-b">Booked</span>'
    if s == TB: return '<span class="tag tag-tb">To book</span>'
    return ''

def rows(rs):
    o = ['<ol class="rows">']
    for t, p, n, s in rs:
        cls = 'row' + (' is-b' if s == B else '')
        o.append(f'<li class="{cls}"><span class="t">{E(t)}</span><div class="w"><p class="p">{E(p)} {tag(s)}</p>' + (f'<p class="n">{E(n)}</p>' if n else '') + '</div></li>')
    o.append('</ol>')
    return ''.join(o)

def notes(ns):
    return '<dl class="notes">' + ''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in ns) + '</dl>'

def band(legs):
    return '<div class="band">' + ''.join(f'<i class="pat pat-{l}"></i>' for l in (legs or ['home'])) + '</div>'

def day(d):
    legs = d['legs']; last = legs[-1] if legs else 'home'
    where = d.get('where') or ' to '.join(LEGS[l]['short'] for l in legs)
    o = [f'<article class="day{" alt" if "alts" in d else ""}{" dense" if len(d.get("rows") or [])>14 else ""} leg-{last}" id="d{d["d"]}" data-date="2026-10-{d["d"]}">', band(legs),
         f'<header class="dh"><div class="date"><span class="num">{d["d"]}</span><span class="dow">{d["dow"]}<br><span class="where">{E(where)}</span></span></div><h3>{E(d["title"])}</h3></header>']
    if 'alts' in d:
        o.insert(1,'<div class="keep">')
        if d.get('pre'): o.append(f'<p class="sum">{E(d["pre"])}</p>')
        g = d['group']
        alts = [x if isinstance(x, dict) else dict(lab=x[0], ttl=x[1], sum=x[2], rows=x[3], foot=x[4], show=str(i)) for i, x in enumerate(d['alts'])]
        tabs = d.get('tabs') or [x['lab'] for x in alts]
        for i, x in enumerate(alts):
            vis = True
            inner = f'<h4><span class="pday">{d["dow"]} {d["d"]}. </span>{E(x["ttl"])}</h4><p class="sum">{E(x["sum"])}</p>'
            if x.get('list'): inner += '<ul class="changes">' + ''.join(f'<li>{E(t)}</li>' for t in x['list']) + '</ul>'
            if x.get('rows') and not x.get('rows_noprint'): inner += rows(x['rows'])
            if x.get('foot'): inner += f'<p class="foot">{E(x["foot"])}</p>'
            o.append(f'<section class="panel" data-group="{g}" data-show="{x["show"]}"{"" if vis else " hidden"}>{inner}</section>' + ('</div>' if i==0 else ''))
    else:
        o.append(f'<p class="sum">{E(d["sum"])}</p>{rows(d["rows"])}')
        if d.get('foot'): o.append(f'<p class="foot">{E(d["foot"])}</p>')
    if d.get('notes'): o.append(notes(d['notes']))
    o.append('</article>')
    sky = ''
    if d.get('sky'):
        sky = ('<section class="decide block"><h4>Which day is Shibuya Sky?</h4><p class="sum">Three slots are booked: Saturday 16:00, plus Monday and Tuesday sunsets as backups. Check the forecast on arrival and pick one, then see whether the other two can be cancelled or changed. That one choice sets Monday and Tuesday. If Sky stays on Saturday, the better weather day of the two goes to Tsukiji and Yokohama.</p>'
                 '<table><thead><tr><th>Shibuya Sky is on</th><th>Monday 19</th><th>Tuesday 20</th></tr></thead><tbody>'
                 '<tr><th>Saturday<span>Clear on arrival. The default</span></th><td>Shinjuku, or swap for weather</td><td>Tsukiji and Yokohama, or swap for weather</td></tr>'
                 '<tr><th>Monday<span>Saturday is out, Monday is clear</span></th><td>Shinjuku, with a sunset break for Shibuya Sky</td><td>Tsukiji and Yokohama</td></tr>'
                 '<tr><th>Tuesday<span>Only Tuesday works</span></th><td>Tsukiji and Yokohama</td><td>Shinjuku, with a sunset break for Shibuya Sky</td></tr>'
                 '</tbody></table></section>')
    if d.get('extra'):
        sky += f'<section class="decide block"><h4>{E(d["extra"][0])}</h4>{notes(d["extra"][1])}</section>'
    return ''.join(o) + sky

def chapter(k):
    L = LEGS[k]
    return (f'<header class="chap leg-{k}" id="leg-{k}"><div class="chap-top"><i class="pat pat-{k} swatch"></i><span class="legno">Leg {L["n"]} of 4</span></div>'
            f'<div class="chap-main"><span class="kanji" lang="ja" aria-hidden="true">{L["kanji"]}</span><div><h2>{E(L["name"])}</h2><p class="meta">{E(L["dates"])}<br>{E(L["hotel"])}</p></div></div>'
            f'<p class="lede">{E(L["sum"])}</p></header>')

def good(k):
    return f'<section class="good leg-{k}"><h4>Good to know in {E(LEGS[k]["short"])}</h4>{notes(GOOD[k])}</section>'

body = []
order = {'s': [17, 18, 19, 20], 'k': [21, 22, 23], 'g': [24, 25, 26], 'h': [27, 28, 29, 30]}
bd = {d['d']: d for d in DAYS}
body.append('<section class="leg pre">' + day(DAY16) + '</section>')
for k in 'skgh':
    body.append(f'<section class="leg">{chapter(k)}{good(k)}')
    for n in order[k]:
        body.append(day(bd[n]))
    if k == 'h':
        body.append('<section class="swaps leg-h"><h4>Optional swaps in Hong Kong</h4><p class="sum">The plan above is the default. Wednesday, Thursday and Friday are interchangeable, so match them to the forecast once you arrive. Put the Peak and the Big Buddha on the clearest days. Put the pool time on the hottest ones. Only the bookings tie a plan to a day.</p><ul>' +
                    ''.join(f'<li><strong>{E(a)}</strong><span>{E(b)}</span><span>{E(c)}</span></li>' for a, b, c in SWAPS) + '</ul></section>')
    body.append('</section>')

lp=['<section class="legsprint"><h2 class="sec">The four legs</h2>']
for k in 'skgh':
    L=LEGS[k]
    lp.append(f'<article class="lp leg-{k}"><i class="pat pat-{k}"></i><div class="lph"><span class="kanji" lang="ja" aria-hidden="true">{L["kanji"]}</span><div><p class="legno">Leg {L["n"]} of 4. {E(L["pat"])} pattern</p><h3>{E(L["name"])}</h3><p class="meta">{E(L["dates"])}. {E(L["hotel"])}</p></div></div><p class="lede">{E(L["sum"])}</p>{notes(GOOD[k])}</article>')
lp.append('</section>')
# calendar
cal = []
for d in [DAY16] + DAYS:
    booked = any(r[3] == B for r in (d.get('rows') or (d['alts'][0]['rows'] if isinstance(d['alts'][0], dict) else d['alts'][0][3])))
    cal.append(f'<a class="cell" href="#d{d["d"]}" data-date="2026-10-{d["d"]}">{band(d["legs"])}<span class="cd">{d["dow"][:3]} <b>{d["d"]}</b></span><span class="ct">{E(d["cal"])}</span>' + ('<span class="dot" title="Has a booked or fixed time"></span>' if booked else '<span class="dot dot-o"></span>') + '</a>')
cal.append(f'<a class="cell" href="#d30" data-date="2026-10-31">{band("h")}<span class="cd">Sat <b>31</b></span><span class="ct">00:30 to Melbourne</span><span class="dot"></span></a>')

nav = ''.join(f'<a href="#d{d["d"]}" class="leg-{d["legs"][-1] if d["legs"] else "home"}" data-date="2026-10-{d["d"]}"><small>{d["dow"][:2]}</small>{d["d"]}</a>' for d in [DAY16] + DAYS)

checks = []
ci = 0
for ttl, items in CHECK:
    checks.append(f'<h4>{E(ttl)}</h4><ul class="checks">')
    for k, txt in items:
        ci += 1
        nm = LEGS[k]['short'] if k else 'All'; pk = k or 'home'
        chip = f'<i class="pat pat-{k} leg-{k} chip" title="{E(nm)}"></i>' if k else ''
        lead = f'<b class="cleg">{E(nm)}. </b>' if k else ''
        checks.append(f'<li{"" if k else ' class="nochip"'}><label><input type="checkbox" data-k="k{hashlib.md5(txt.encode()).hexdigest()[:8]}"><span class="box"></span>{chip}<span class="ctext">{lead}{E(txt)}</span></label></li>')
    checks.append('</ul>')

route = [('Melbourne', '', ''), ('Shibuya', 's', '4 nights'), ('Kyoto', 'k', '3 nights'), ('Hibiya', 'g', '3 nights'), ('Hong Kong', 'h', '3 nights'), ('Melbourne', '', '')]
hops = ['CX524, lands 06:50 Sat 17', 'Nozomi 13, 07:55 Wed 21', 'Nozomi 16, 12:01 Sat 24', 'CX543, 10:10 Tue 27', 'CX105, 00:30 Sat 31']
rt = ['<ol class="route">']
for i, (nm, k, nights) in enumerate(route):
    rt.append(f'<li class="stop {"leg-"+k if k else "home"}">' + (f'<i class="pat pat-{k}"></i>' if k else '<i class="pat pat-home"></i>') + f'<b>{nm}</b>' + (f'<span>{nights}</span>' if nights else '') + '</li>')
    if i < len(hops): rt.append(f'<li class="hop">{hops[i]}</li>')
rt.append('</ol>')

tips = ('<section class="more tips" id="tips"><h2 class="sec">Tips</h2><p class="sum">Small things that make the days easier, in the order you will need them. Japan first, Hong Kong at the end.</p><dl class="notes tipgrid">'
        + ''.join(f'<div><dt>{E(a)}</dt><dd>{E(b)}</dd></div>' for a, b in TIPS) + '</dl></section>')
howto = ('<section class="more howtos" id="howto"><h2 class="sec">Appendix: how-to</h2><p class="sum">Step by step, for the moments with bags, tickets or a clock. The day pages point here by number.</p><div class="hgrid">'
         + ''.join(f'<section class="decide block" id="h{i}"><h4>How-to {i}. {E(t)}</h4><ul class="changes">' + ''.join(f'<li>{E(x)}</li>' for x in steps) + '</ul></section>' for i, (t, steps) in enumerate(HOWTO, 1))
         + '</div></section>')

tpl = open('template.html').read()
out = (tpl.replace('/*F1*/', b64('*bricolage*/package/files/*latin-wght-normal.woff2'))
          .replace('/*F2*/', b64('*bricolage*/package/files/*latin-ext-wght-normal.woff2'))
          .replace('/*F3*/', b64('*instrument*/package/files/*latin-wght-normal.woff2'))
          .replace('/*F4*/', b64('*instrument*/package/files/*latin-ext-wght-normal.woff2'))
          .replace('<!--ROUTE-->', ''.join(rt)).replace('<!--CAL-->', ''.join(cal)).replace('<!--NAV-->', nav).replace('<!--LEGS-->', ''.join(lp))
          .replace('<!--BODY-->', ''.join(body)).replace('<!--CHECKS-->', ''.join(checks)).replace('<!--TIPS-->', tips).replace('<!--HOWTO-->', howto).replace('/*COSTS*/', json.dumps(json.load(open('expenses.json', encoding='utf-8')), ensure_ascii=False).replace('</', '<\\/')))
# ---------- interactive place cards (online only, the PDF ignores them) ----------
exec(open('places.py').read())
import json as _json, re as _re2
_B = r'A-Za-z0-9À-ɏ'
def _link(seg, daynum):
    toks = _re2.split(r'(<[^>]+>)', seg)
    skip = 0; live = []
    for n, tk in enumerate(toks):
        if tk.startswith('<'):
            m = _re2.match(r'<(/?)(h3|h4|header|button|dt|th|script|style)\b', tk)
            if m: skip += -1 if m.group(1) else 1
        elif skip == 0 and tk.strip():
            live.append(n)
    for n in live:
        for k, ig in enumerate(IGNORE):
            toks[n] = toks[n].replace(ig, f'\x01{k}\x01')
    hits = []
    for pl in sorted(PLACES, key=lambda p: -max(len(a) for a in p['aliases'])):
        if pl['days'] is not None and daynum not in pl['days']: continue
        for n in live:
            while True:
                best = None
                for a in pl['aliases']:
                    m = _re2.search(r'(?<![' + _B + r'])' + _re2.escape(a) + r'(?![' + _B + r'])', toks[n])
                    if m and (best is None or m.start() < best[0]): best = (m.start(), m.end(), a)
                if not best: break
                s, e, a = best
                hits.append((pl['key'], a))
                toks[n] = toks[n][:s] + f'\x00{len(hits)-1}\x00' + toks[n][e:]
    seg = ''.join(toks)
    for k, (key, a) in enumerate(hits):
        seg = seg.replace(f'\x00{k}\x00', f'<a class="pl" href="#" role="button" data-p="{key}">{a}</a>')
    for k, ig in enumerate(IGNORE):
        seg = seg.replace(f'\x01{k}\x01', ig)
    return seg, len(hits)
_marks = [(m.start(), int(m.group(1))) for m in _re2.finditer(r'<article class="day[^"]*" id="d(\d+)"', out)]
_lp = out.index('<section class="legsprint">'); _sw = out.index('<section class="swaps'); _end = out.index('<section class="list"')
_cuts = [(_lp, 0)] + _marks + [(_sw, 99), (_end, None)]
_pieces = [out[:_lp]]; _n = 0
for (s, d), (e, _d2) in zip(_cuts, _cuts[1:]):
    seg, c = _link(out[s:e], d); _pieces.append(seg); _n += c
_ts = out.rindex('<section', 0, out.index('id="tips"')); _cs = out.index('<section class="costs')
_pieces.append(out[_end:_ts]); seg, c = _link(out[_ts:_cs], None); _pieces.append(seg); _n += c
_pieces.append(out[_cs:]); out = ''.join(_pieces)
_data = {p['key']: dict(n=p['n'], l=p['l'], w=p['w'], t=p['t'], m=p['m']) for p in PLACES}
out = out.replace('/*PLACES*/', _json.dumps(_data, ensure_ascii=False))
print('place links:', _n, 'cards:', len(PLACES))
assert '—' not in out and '--' not in out.split('</style>')[1].split('<script>')[0].replace('<!--', '').replace('-->', '')
open('out/japan-hong-kong-final-itinerary.html', 'w').write(out)
print(len(out))
