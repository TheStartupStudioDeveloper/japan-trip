# Actuals: days already lived are rewritten to what happened, marked Done. Original plan: /baseline/original-plan/
DN = 'd'
D[17]['sum'] = 'What happened. Landed almost three hours late, so the day ran later than planned, but nearly everything got done, plus MEGA Don Quijote and a late night out. Times are approximate.'
D[17]['rows'] = [
 R('09:35', 'Landed at Narita, late', 'CX524, about 2 hours 45 minutes late (planned 06:50).', DN),
 R('11:15', 'Narita Express to Shibuya', '', DN),
 R('12:30', 'Wheeled the bags to the hotel', 'Left them at the desk on 4F.', DN),
 R('13:00', 'Coffee and açaí bowls under Miyashita Park', 'The shopping mall below the rooftop park.', DN),
 R('13:45', 'Miyashita Park rooftop', '', DN),
 R('14:15', 'Cat Street and Omotesando', 'On foot.', DN),
 R('15:30', 'Back to the hotel, luggage, change', '', DN),
 R('16:00', 'Shibuya Sky', 'The booked slot. The Monday and Tuesday backups were not needed.', DN),
 R('18:30', 'Checked in', '', DN),
 R('19:30', 'Dinner at Shibuya Yokochō', 'Tōkai Shokuichi, Nagoya food and beer.', DN),
 R('21:00', 'Scramble Crossing and the Shibuya streets', 'Found a great small-counter ramen spot.', DN),
 R('22:00', 'MEGA Don Quijote', 'Back at the hotel about midnight.', DN),
]
_rs = D[18]['rows']
def _done(t):
    i = _row(18, t); r = _rs[i]; _rs[i] = R(r[0], r[1], r[2], DN)
_rs[_row(18, '08:00')] = R('08:00', 'Breakfast at Premier Mai', 'PATH was temporarily closed. The hidden café in Tomigaya instead, a hit (How-to 26).', DN)
for _t in ('09:30', '10:15', '11:00'): _done(_t)
_i = [k for k, r in enumerate(_rs) if r[1] == "Cynthia's shopping afternoon"][0]
_rs[_i] = R('11:30', "Cynthia's shopping afternoon", 'Pre-owned shops: Brand Collect, Brand Collect Omotesando 2, Kindal Harajuku, RAGTAG Harajuku, ALLU, Brand Collect Shibuya.', DN)
_i = [k for k, r in enumerate(_rs) if r[1] == "G's free time"][0]
_rs[_i] = R('11:30', "G's free time", 'ZARA Harajuku was closed. Booked tonight\'s massage at Mominotakumi in person, then ZARA Shibuya Kōen-dōri, H&M Udagawachō and Nintendo Tokyo. Egg sando from 7-Eleven for lunch.', DN)
# Sun 18 evening, logged 22:03
for _t in ('14:20', '14:45', '16:00', '18:30', '20:30'): _done(_t)
_rs[_row(18, '19:30')] = R('19:15', 'Dinner at Mihachi Shibuya Ekimae', 'Izakaya in the basement of the Dōgenzaka Building, by the station. Sauce yakisoba, negi-shio cucumber, menchi katsu, zha cai. ¥3,971 for two, including a ¥550 cover charge each.', DN)
_rs.insert(_row(18, '20:30') + 1, R('22:00', 'Welcome drink at the hotel lobby bar', 'Sequence Miyashita Park, 4F. Then back to the room.', DN))
# Mon 19 08:22: Hibiya line delay, walked from Ginza. Day retimed about 30 minutes later
D[19]['rows'] = [
 R('07:00', 'Left the hotel, Ginza line to Ginza', '', DN),
 R('08:10', 'Hibiya line delayed, walked from Ginza instead', 'Underground passage east towards Higashi-ginza, Exit A1, then along Harumi-dōri past Kabukiza. About 15 minutes, and a good way to arrive.', DN),
 R('08:30', 'Tsukiji Outer Market breakfast', 'Small bites only: pancakes are lunch. Tamagoyaki, grilled scallop, strawberry daifuku. Cash.'),
 R('09:30', 'Namiyoke Inari shrine', 'The little shrine on the market\'s south-east edge, with the giant lion heads. A 10 minute stop.'),
 R('09:40', 'Walk to Shimbashi, JR to Kamakura', 'About 15 minutes west along Harumi-dōri, then left to JR Shimbashi. Yokosuka line (blue and cream) direct to Kamakura, about 55 minutes. Not the Tōkaidō line (How-to 27).'),
 R('11:00', 'Tsurugaoka Hachimangū, Komachi-dōri', 'The shrine up the long approach, then the snack and shop street back to the station. Keep it to about an hour.'),
 R('12:10', 'Enoden to Hase', 'The little seaside train, 3 stops, about 5 minutes. Sit on the left.'),
 R('12:20', 'Fluffy pancakes, A la Mode Kamakura', 'In Hase, looking out at the sea. Open to 18:30.'),
 R('13:20', 'Hase-dera, then the Great Buddha', 'Hase-dera on the hillside with sea views, then 5 minutes on foot to the Great Buddha. Last entry 16:45.'),
 R('14:40', 'A quick look at Yuigahama', 'About 10 minutes downhill. Skip it if running late.'),
 R('15:00', 'To Yokohama', 'Enoden back to Kamakura, JR Yokosuka line to Yokohama, about 25 minutes, then the Negishi line one stop to Sakuragichō (How-to 27).'),
 R('16:15', 'Air Cabin, then Cosmo World', 'Air Cabin from outside Sakuragichō east exit, ¥1,000, 5 minutes. The Diving Coaster Vanish, about ¥1,000 each, cash only. Cosmo Clock 21 at sunset, about 17:05 (How-to 28). Cosmo World closes 20:00.'),
 R('17:45', 'Harbour walk to Chinatown', 'Red Brick Warehouses and Yamashita Park, about 30 minutes.'),
 R('18:30', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:45', 'Foot massage, Kyūryū SPA', 'Chinatown, 2F on a pedestrian lane. 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00 (How-to 28).'),
 R('21:00', 'Train home from Motomachi-Chūkagai', 'Straight through to Shibuya, about 40 minutes, no change. Back about 21:45.'),
]
D[19]['foot'] = D[19]['foot'] + ' Retimed at 08:22 after the Hibiya line delay: everything about 30 minutes later.'
# Mon 19 08:58: left Tsukiji early. Pancakes first in Hase, lunch later in Kamakura town
_r = D[19]['rows']
_keep = [r for r in _r if r[0] in ('16:15', '17:45', '18:30', '19:45', '21:00')]
D[19]['rows'] = _r[:2] + [
 R('08:30', 'Tsukiji Outer Market', 'Small bites.', DN),
 R('09:00', 'Walk to Shimbashi, JR to Kamakura', 'About 15 minutes to JR Shimbashi. Blue Yokosuka line signs downstairs to the underground platforms, towards Yokohama, Ōfuna, Zushi or Kurihama. Direct to Kamakura, about 55 minutes. Not the Tōkaidō line upstairs (How-to 27).'),
 R('10:15', 'Enoden straight to Hase', 'Stay inside Kamakura Station for the Enoden platform on the west side. 3 stops, about 5 minutes.'),
 R('10:30', 'Pancakes and coffee, A la Mode Kamakura', 'Breakfast with a sea view, 5 minutes from Hase Station towards the sea. Fluffy pancakes, Greek yoghurt ice cream, real maple syrup.'),
 R('11:30', 'Hase-dera, then the Great Buddha', 'Hase-dera on the hillside with sea views, then 5 minutes on foot to the Great Buddha.'),
 R('12:45', 'A quick look at Yuigahama', 'About 10 minutes downhill from the Buddha. Skip it if running late.'),
 R('13:00', 'Enoden back to Kamakura', 'About 5 minutes.'),
 R('13:15', 'Lunch on Komachi-dōri: shirasu-don', 'Kamakura\'s local dish, a rice bowl of tiny fresh whitebait. Something different after the pancakes.'),
 R('14:15', 'Tsurugaoka Hachimangū', 'Up the long approach from Komachi-dōri, about 10 minutes, open to 20:00.'),
 R('15:15', 'To Yokohama', 'JR Yokosuka line from Kamakura to Yokohama, about 25 minutes, then the Negishi line one stop to Sakuragichō (How-to 27).'),
] + _keep
# Mon 19 11:17: at A la Mode Kamakura, on track
_r = D[19]['rows']
_r[_row(19, '09:00')] = R('09:00', 'JR Shimbashi to Kamakura', 'Yokosuka line from the underground platforms, direct.', DN)
_r[_row(19, '10:15')] = R('10:15', 'Enoden to Hase', '', DN)
_r[_row(19, '10:30')] = R('10:30', 'Pancakes and coffee, A la Mode Kamakura', 'Breakfast with a sea view. Lovely.', DN)
HOWTO.append(('Getting around, Mon 19 from Hase to home', [
 'A la Mode to Hase-dera, 7 minutes: walk inland up the main road (Hase-dōri) to the traffic light by Hase Station, turn left, and the gate is straight ahead at the end of the road. ¥400, open to 17:00. Go up the steps to the lookout terrace for the sea view.',
 'Hase-dera to the Great Buddha, 7 minutes: back down to the main road, turn left (inland) and walk up it. Kōtoku-in is on the left. ¥300, last entry 16:45.',
 'Optional Yuigahama: from the Great Buddha walk back down the main road past Hase Station to the sea, about 12 minutes. Back to Hase Station is 5 minutes.',
 'Hase to Kamakura: Enoden from Hase Station, platform for Kamakura (鎌倉方面), 3 stops, about 5 minutes. Kamakura is the end of the line.',
 'Kamakura Station to lunch: walk through to the JR east exit. Komachi-dōri starts at the red torii arch on the left of the plaza. Shirasu-don at Wasai Yakura, 2-7-28 Komachi, 2F, open 11:00 to 21:00, about halfway up on the left side.',
 'Komachi-dōri to Tsurugaoka Hachimangū: walk to the far end of Komachi-dōri (about 8 minutes), turn right, and the shrine grounds are ahead. Up the big stone steps to the main hall. Free.',
 'Hachimangū back to the station: down the central raised path (Dankazura) on Wakamiya-ōji, about 10 minutes, straight to Kamakura Station east exit.',
 'Kamakura to Yokohama: JR Yokosuka line, platform for Yokohama and Tokyo (横浜・東京方面), about 25 minutes. At Yokohama, change to the JR Negishi line (light blue, 根岸線) towards Ōfuna or Isogo, one stop to Sakuragichō.',
 'Air Cabin: out of Sakuragichō east exit, the cable car station is right there on the plaza. ¥1,000 one way, about 5 minutes, lands at Unga Park beside Cosmo World. If it is stopped for wind, walk 10 minutes along the Kishamichi promenade instead.',
 'Cosmo World: Diving Coaster Vanish and the Cosmo Clock 21 ferris wheel. Buy tickets at the machines, cash only. Lockers by the coaster.',
 'Harbour walk to Chinatown, about 30 minutes: east from Cosmo World along the Kishamichi promenade to the Red Brick Warehouses, then along the water past Ōsanbashi Pier into Yamashita Park. Leave the park at its middle and walk inland about 5 minutes into Chinatown.',
 'Kyūryū SPA (Kirin Kowloon): Yamashitachō 148, 2F, on a pedestrian lane inside Chinatown. Open to 22:00. Ask for the 60-minute foot course with the foot bath. Backup: Kaisokukan, open to 23:00.',
 'Home: Motomachi-Chūkagai Station (Minatomirai line) is at the Yamashita Park end of Chinatown. Any train towards Shibuya (渋谷方面), express (急行) or limited express (特急) is fastest, about 40 minutes. If it carries on past Shibuya, get off at Shibuya.',
 'Shibuya to the hotel: the Tōyoko line platforms are deep underground. Follow signs up and out towards Miyashita Park, about 7 to 10 minutes to the hotel.']))
_r = D[19]['rows']
_i = _row(19, '11:30')
_r[_i] = R(_r[_i][0], _r[_i][1], _r[_i][2] + ' Directions for the rest of the day: How-to 30.', *_r[_i][3:])
# Mon 19 13:41 actual: Hase-dera and the Great Buddha done, lunch and Yuigahama dropped. New afternoon: Yokohama Station department stores
_r = D[19]['rows']
_done_rows = [r for r in _r if r[0] in ('07:00', '08:10', '08:30', '09:00', '10:15', '10:30')]
D[19]['rows'] = _done_rows + [
 R('11:30', 'Hase-dera', 'Hillside temple with the sea view.', DN),
 R('13:00', 'The Great Buddha, matcha ice cream on Hase-dōri', 'Ice cream on the way out. Lunch and the Yuigahama walk dropped, not needed.', DN),
 R('13:40', 'Enoden Hase to Kamakura', 'About 5 minutes, Kamakura is the end of the line.'),
 R('13:55', 'JR Yokosuka line Kamakura to Yokohama', 'Platform for Yokohama and Tokyo (横浜・東京方面). About 25 minutes, direct.'),
 R('14:20', 'Yokohama Station department stores', 'Takashimaya on the west side and Sogo on the east side, both attached to the station. Open to 20:00. Passports for tax-free.'),
 R('15:30', 'To Minato Mirai', 'Minatomirai line one stop to Minatomirai, or JR Negishi line one stop to Sakuragichō. Optional: Landmark Plaza and MARK IS on the way (How-to 30).'),
 R('16:15', 'Air Cabin to Unga Park', 'From outside Sakuragichō east exit, ¥1,000, about 5 minutes. If stopped for wind, walk the Kishamichi promenade.'),
 R('16:30', 'Cosmo World: Diving Coaster Vanish', 'About ¥1,000 each, cash only, pockets into the lockers. Open to 20:00.'),
 R('17:00', 'Cosmo Clock 21 ferris wheel at sunset', 'Sunset about 17:05. About 15 minutes round.'),
 R('17:30', 'Harbour walk to Yamashita Park', 'Past the Red Brick Warehouses and Ōsanbashi Pier, about 30 minutes.'),
 R('18:15', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:30', 'Foot massage, Kyūryū SPA (Kirin Kowloon)', 'Chinatown, 2F on a pedestrian lane. 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00.'),
 R('20:45', 'Train home from Motomachi-Chūkagai', 'Direct to Shibuya, about 40 minutes, no change. Back about 21:30 (How-to 30).'),
]
D[19]['foot'] = 'Alternative: skip the department stores, stay on the JR train to Sakuragichō and spend the extra hour at the Minato Mirai malls (Landmark Plaza, MARK IS) and the Red Brick Warehouses. Checked for Monday: Takashimaya and Sogo 10:00 to 20:00, Landmark Plaza 11:00 to 20:00, MARK IS 10:00 to 20:00, Air Cabin 10:00 to 21:00, Cosmo World 11:00 to 20:00 (cash only), Kyūryū SPA 10:00 to 22:00.'
D[19]['sum'] = 'Tsukiji for breakfast, then Kamakura: pancakes in Hase, Hase-dera and the Great Buddha. Yokohama from the afternoon: the station department stores, the Air Cabin, the Vanish coaster and the ferris wheel at sunset, the harbour walk, dinner in Chinatown and a foot massage.'
# Mon 19 14:04: department stores skipped, straight to Minato Mirai. Red Brick Warehouses at dusk
_r = D[19]['rows']
_keep = [r for r in _r if r[3] == DN] if len(_r[0]) > 3 else []
_keep = [r for r in _r if len(r) > 3 and r[3] == DN]
D[19]['rows'] = _keep + [
 R('14:07', 'Shōnan-Shinjuku line Kamakura to Yokohama', 'Platform 2, the train to Utsunomiya. About 25 minutes. Get off at Yokohama: it carries on to Shibuya.', DN),
 R('14:30', 'Minatomirai line one stop to Minatomirai', 'Tap out of JR at Yokohama, follow the Minatomirai Line signs underground. Any train towards Motomachi-Chūkagai, about 3 minutes.'),
 R('14:45', 'Queen\'s Square and Landmark Plaza: ZARA', 'The station opens straight into Queen\'s Square, where ZARA is. Landmark Plaza is joined on, MARK IS across the road. Open to 20:00 (Landmark from 11:00).'),
 R('15:50', 'Walk to Sakuragichō, Air Cabin to Unga Park', 'Through Landmark Plaza and down the moving walkway, about 10 minutes. Air Cabin from outside the east exit, ¥1,000, about 5 minutes.'),
 R('16:15', 'Cosmo World: Diving Coaster Vanish', 'About ¥1,000 each, cash only, pockets into the lockers. Open to 20:00.'),
 R('17:00', 'Cosmo Clock 21 ferris wheel at sunset', 'Sunset about 17:05. About 15 minutes round.'),
 R('17:20', 'Red Brick Warehouses at dusk', 'About 10 minutes along the Kishamichi promenade. Two 1910s customs warehouses on the water, now small shops, cafés and craft beer, lit up after dark. Building 1 open to 19:00.'),
 R('18:10', 'Harbour walk to Chinatown', 'Along the water past Ōsanbashi Pier into Yamashita Park, then inland into Chinatown, about 30 minutes.'),
 R('18:40', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:50', 'Foot massage, Kyūryū SPA (Kirin Kowloon)', 'Chinatown, 2F on a pedestrian lane. 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00.'),
 R('21:05', 'Train home from Motomachi-Chūkagai', 'Direct to Shibuya, about 40 minutes, no change. Back about 21:50 (How-to 30).'),
]
D[19]['foot'] = 'Yokohama Station department stores skipped for Minato Mirai. Checked for Monday: Queen\'s Square 11:00 to 20:00, Landmark Plaza 11:00 to 20:00, MARK IS 10:00 to 20:00, Air Cabin 10:00 to 21:00, Cosmo World 11:00 to 20:00 (cash only), Red Brick Warehouse 1 10:00 to 19:00, Kyūryū SPA 10:00 to 22:00.'
D[19]['sum'] = 'Tsukiji for breakfast, then Kamakura: pancakes in Hase, Hase-dera and the Great Buddha. Yokohama from the afternoon: shopping at Queen\'s Square and Landmark Plaza, the Air Cabin, the Vanish coaster, the ferris wheel at sunset, the Red Brick Warehouses at dusk, dinner in Chinatown and a foot massage.'
# Mon 19 20:09 actuals: Yokohama afternoon and evening (plus notes from the notes chat)
_r = D[19]['rows']
_keep = [r for r in _r if len(r) > 3 and r[3] == DN and r[0] < '14:00']
D[19]['rows'] = _keep + [
 R('14:19', 'Kamakura to Yokohama, first double-decker train', 'Nearly boarded the wrong train. Sat in the Green Car by accident for a few stops and got moved back to an ordinary car.', DN),
 R('14:45', 'Minatomirai line, off one stop early at Shin-Takashima', 'Walked or rode on to Minatomirai.', DN),
 R('15:00', 'Queen\'s Square and Landmark Plaza, ZARA', '', DN),
 R('16:30', 'Air Cabin to Unga Park', '', DN),
 R('17:00', 'Cosmo Clock 21 ferris wheel and the Diving Coaster Vanish', 'All done by 17:45.', DN),
 R('17:50', 'Red Brick Warehouses', '', DN),
 R('18:30', 'Dinner: Yokohama Sichuan Mapo, Chinatown', 'Mapo tofu.', DN),
 R('19:45', 'Foot massage, Kyūryū SPA (Kirin Kowloon)', 'An hour, to 20:45.', DN),
 R('20:50', 'Train home from Motomachi-Chūkagai', 'Direct to Shibuya, about 40 minutes. Back about 21:40 (How-to 30).'),
]
D[19]['foot'] = 'Skipped: Yokohama Station department stores, Tsurugaoka Hachimangū, Yuigahama, lunch. Checked for Monday: Queen\'s Square 11:00 to 20:00, Air Cabin 10:00 to 21:00, Cosmo World 11:00 to 20:00, Red Brick Warehouse 1 10:00 to 19:00, Kyūryū SPA 10:00 to 22:00.'
# 20 Oct 00:00: no skipped or dropped notes on days already done. The log keeps those.
D[19]['foot'] = ''
_r = D[19]['rows']
for _k, _x in enumerate(_r):
    if _x[0] == '13:00':
        _r[_k] = R(_x[0], _x[1], 'Ice cream on the way out.', *_x[3:])
_r = D[17]['rows']
for _k, _x in enumerate(_r):
    if _x[0] == '16:00':
        _r[_k] = R(_x[0], _x[1], 'The booked slot.', *_x[3:])
# Fri 16 actuals, from G's Copy for Claude paste (20 Oct 06:38): every row done
DAY16['rows'] = [R(r[0], r[1], r[2], DN) for r in DAY16['rows']]
# Tue 20 actuals to 11:36, from G's Copy for Claude paste. Hotel stop and suitcase taken out. Tochō deck added before lunch.
_t = D[20]['rows']
_k = _row(20, '13:30')
D[20]['rows'] = [
 R('07:45', 'Train to Nakameguro, walk up the river to the Roastery', '', DN),
 R('08:00', 'Breakfast at the Starbucks Reserve Roastery', '', DN),
 R('09:00', 'Meguro River walk to Nakameguro', '', DN),
 R('09:30', 'Tōkyū Tōyoko line straight through to Harajuku', 'Meiji-jingūmae, no change.', DN),
 R('10:00', 'Harajuku streets', 'Toy vending machines, clear umbrellas.', DN),
 R('11:45', 'JR Yamanote line Harajuku to Shinjuku', 'Two stops, about 5 minutes. West exit, then about 12 minutes on foot to Tochō.'),
 R('12:00', 'Government Building deck, North Observation Deck', 'Free, 45th floor, bag check then the lift. Open to 17:30; the South deck is closed on Tuesdays. Mt Fuji to the west on a clear day. Leave by 13:05.'),
 R('13:05', 'Walk to NEWoMan, New South Exit', 'About 15 minutes back past Shinjuku Station. Tokyo Ten is on 2F.'),
] + _t[_k:]
_t = D[20]['rows']
_i = _row(20, '21:45')
_t[_i] = R(_t[_i][0], _t[_i][1], _t[_i][2] + ' Pack tonight.', *_t[_i][3:])
D[20]['foot'] = 'Tochō North Observation Deck open 09:30 to 17:30 today, South deck closed Tuesdays. Wednesday is the 05:55 wake.'

# Tue 20 actuals, from G's Copy for Claude paste (22:02). Whole day done.
_t = D[20]['rows']
_k = _row(20, '11:45')
D[20]['rows'] = _t[:_k] + [
 R('11:45', 'JR Yamanote line Harajuku to Shinjuku', 'Then the underground moving walkways through the tunnel to Tochō.', DN),
 R('12:00', 'Government Building deck, North Observation Deck', 'Free, 45th floor.', DN),
 R('13:05', 'Walk to NEWoMan, New South Exit', '', DN),
 R('13:30', 'Omakase lunch: Sushi Tokyo Ten Shinjuku', 'Massive, all seafood. The abalone followed by liver got a laugh. The highlight was the egg and the grapes at the end.', DN),
 R('15:00', 'Takashimaya rooftop', 'The open-air rooftop at Takashimaya. FamilyMart takeaway coffee and a grey jumper.', DN),
 R('16:00', 'Shinjuku Gyoen stroll', 'Made it in just before the gates closed.', DN),
 R('17:00', 'Cynthia at RAGTAG Shinjuku', 'G walked the blocks around and bought a toy car.', DN),
 R('17:30', 'Foot massage, Suosoukan Shinjuku South Exit', 'Half an hour each, next door to RAGTAG.', DN),
 R('18:00', 'Shinjuku: the 3D cat at the east exit', '', DN),
 R('18:15', 'Godzilla head, Kabukichō and Kabukichō Tower', '', DN),
 R('19:00', 'Golden Gai: Anchor', 'First Asahi, and a ninja highball for Cynthia.', DN),
 R('19:45', 'Omoide Yokochō', 'Dinner and the first sake.', DN),
 R('20:45', 'JR Yamanote line home to Shibuya', 'Platform 14, East exit, walk up Meiji-dōri.', DN),
]
D[20]['foot'] = ''

# Kyoto replan, agreed in chat 20 Oct 22:42. Casual food, light on seafood. Inari stays Sat (rain gear), Wed dusk is the heavy-rain backup.
_r = D[21]['rows']
_r[_row(21, '19:00')] = R('19:15', 'Dinner: Ichiran Kyoto Karasuma', 'Ramen in the solo booths. About 10 minutes north of the hotel up Karasuma-dōri, at Shijō. Open to 22:00.')
_r[_row(21, '20:30')] = R('20:30', 'Optional: Pontochō and the Kamo River', 'About 15 minutes east along Shijō-dōri. A drink in the lantern alley, then a taxi home.')
D[21]['foot'] = 'Check the Saturday forecast this afternoon. Heavy rain due: take the JR Nara line from JR Nara to Inari instead of Kintetsu, about an hour, and walk the gates at dusk. Then 5 minutes on to Kyoto Station for the bags. Stags are pushy: feed the does.'
_r = D[22]['rows']
_r[_row(22, '12:00')] = R('12:00', 'Okonomiyaki lunch: Mizuno, Dōtonbori', 'Midōsuji line down to Namba. Osaka\'s savoury pancake of pork and cabbage, cooked on the griddle in front of you. The queue moves. Open 11:00 to 22:00.')
_i = _row(22, '13:15'); _x = _r[_i]
_r[_i] = R(_x[0], _x[1], _x[2] + ' Cynthia\'s bigger suitcase: Don Quijote Dōtonbori has big ones at normal prices.', *_x[3:])
_r = D[23]['rows']
_k = _row(23, '15:30')
D[23]['rows'] = _r[:_row(23, '10:15')] + [
 R('10:15', 'Coffee by the river', 'Arabica by Togetsukyō bridge. Lunch is at 11:00.'),
 R('11:00', 'Lunch: Gyukatsu Kyoto Katsugyu', 'Crumbed beef cutlet you finish on a hot stone. Beside the bamboo grove.'),
 R('11:45', 'Taxi to Kinkaku-ji', 'About 25 minutes.'),
 R('12:15', 'Kinkaku-ji, the Golden Pavilion', 'The gold pavilion on its pond. One-way garden loop, about 45 minutes. Open 09:00 to 17:00.'),
 R('13:15', 'Optional: Nijō Castle', 'Taxi about 15 minutes. The squeaky nightingale floors. Last entry 16:00.'),
 R('14:30', 'Hotel, short rest', 'Taxi about 10 minutes.'),
] + _r[_k:]
_r = D[23]['rows']
_r[_row(23, '15:30')] = R('15:30', 'Kiyomizu-dera', 'Taxi from the hotel at 15:15, about 10 minutes. The top of Higashiyama, the old eastern hills. The stage view over the city is the thing. Closes 18:00.')
_i = _row(23, '18:30')
D[23]['rows'] = _r[:_i] + [
 R('18:30', 'Chao Chao gyoza, Sanjō Kiyamachi', 'About 15 minutes north from Gion over Shijō Bridge. Kyoto\'s famous crispy dumplings, small shop, short queue.'),
 R('19:30', 'Pontochō alley', 'The lantern lane of small bars and izakayas by the river, just south. Wander and pick one or two.'),
 R('20:30', 'Optional: Menami', 'Kyoto home-style small plates at a counter, since 1939. On Kiyamachi, back near Chao Chao.'),
] + _r[_i+1:]
_r = D[24]['rows']; _i = _row(24, '07:15'); _x = _r[_i]
_r[_i] = R(_x[0], _x[1], _x[2] + ' Heavy rain: just the lower double row of gates, about 40 minutes. Steps get slippery.', *_x[3:])
for _g in CHECK:
    _g[1][:] = [(l, t) for (l, t) in _g[1] if 'Gion dinner' not in t and 'Gion or Pontochō' not in t]
D[23]['notes'] = [n for n in D[23]['notes'] if n[0] != 'Dinner swap']
GOOD['k'][3] = ('Decided', 'No Universal. Thursday is the Osaka day. Thursday and Friday can swap if they must.')
D[22]['notes'] = [(h, b.replace('Protect lunch at Kuromon', 'Protect the okonomiyaki lunch')) for (h, b) in D[22]['notes']]
# 20 Oct 23:34: Inari stays Sat whatever the weather (no Wed backup). Thu: Osaka Castle SINFONIA light show at night (free, 15 to 25 Oct, 19:00 to 22:00), so the castle moves from the morning to the end of the day and home is by JR from Osakajōkōen.
D[21]['foot'] = 'Stags are pushy: feed the does.'
_r = D[22]['rows']
_keep = {t: _r[_row(22, t)] for t in ('13:15', '15:30', '16:15')}
D[22]['rows'] = [
 R('08:30', 'To Kyoto Station, then JR to Osaka', 'One subway stop or a 15 minute walk. JR special rapid to Osaka Station, about 30 minutes. A later start: the castle is tonight.'),
 R('09:30', 'Umeda Sky deck', 'Two towers joined by a floating escalator. About 10 minutes on foot from Osaka Station through the underpass. Open from 09:30.'),
 R('10:45', 'Midōsuji line down to Namba', 'Buy the one-day Enjoy Eco Card at the metro station, about ¥820. It covers the Osaka Metro all day, including tonight\'s ride to the castle.'),
 R('11:00', 'Okonomiyaki lunch: Mizuno, Dōtonbori', 'Osaka\'s savoury pancake of pork and cabbage, cooked on the griddle in front of you. In at the 11:00 opening, before the queue.'),
 R('12:15', *_keep['13:15'][1:]),
 _keep['15:30'], _keep['16:15'],
 R('17:45', 'Dōtonbori', 'Buy Tombori River Cruise tickets when you arrive and ride after dark (How-to 15). The Glico Running Man photo platform is at the Nanohana cosmetics shop, directly opposite the sign. Eat standing up.'),
 R('18:45', 'Hōzenji Yokochō', 'Two streets back. Stone lanes, lanterns and the mossy Mizukake Fudō. A quick look.'),
 R('19:15', 'Metro to Osaka Castle', 'Sennichimae line from Namba to Tanimachi 9-chōme, then the Tanimachi line two stops to Tanimachi 4-chōme. About 20 minutes, then 15 minutes on foot to the keep.'),
 R('20:00', 'Osaka Castle light show, SINFONIA', 'Free projection mapping on the south face of the keep. About six minutes, repeating 19:00 to 22:00. Standing only. Can be cancelled in bad weather.'),
 R('20:45', 'Home by JR from Osakajōkōen', 'About 15 minutes through the park to the station. Loop line to Osaka, about 10 minutes, then the special rapid to Kyoto, about 30. One subway stop to Gojō. Back about 22:00.'),
]
D[22]['notes'] = [(h, b.replace('Shorten the castle first, then the shops.', 'Shorten the shops first.').replace('Protect the okonomiyaki lunch', 'Protect the castle light show')) for (h, b) in D[22]['notes']]
D[22]['title'] = 'Osaka, Dōtonbori to the castle light show'
# 20 Oct 23:37: keep the castle in the morning as well as the light show at night.
_r = D[22]['rows']
D[22]['rows'] = [
 R('07:00', 'To Kyoto Station, then JR to Osaka', 'One subway stop or a 15 minute walk. JR special rapid to Osaka Station, about 30 minutes, then the Osaka Loop Line to Osakajōkōen for the castle (How-to 14).'),
 R('08:30', 'Osaka Castle, up close', 'In by Aoya-mon to Gokuraku-bashi: the tower over the inner moat walls. Then to its foot, not inside. Takeaway breakfast on a bench. Back tonight for the light show.'),
 R('09:35', 'Tanimachi line to Higashi-Umeda', 'From Tanimachi 4-chōme, on the west side of the castle. Buy the one-day Enjoy Eco Card at the metro station, about ¥820. It covers the Osaka Metro all day, including tonight\'s ride back to the castle, not JR.'),
 R('10:15', 'Umeda Sky deck', 'Two towers joined by a floating escalator. About 15 minutes on foot from Higashi-Umeda.'),
 R('12:00', 'Okonomiyaki lunch: Mizuno, Dōtonbori', 'Midōsuji line down to Namba. Osaka\'s savoury pancake of pork and cabbage, cooked on the griddle in front of you. The queue moves.'),
 R('13:15', *_r[_row(22, '12:15')][1:]),
] + _r[_row(22, '15:30'):]
D[22]['title'] = 'Osaka, castle by day and by night'

# 21 Oct 08:09: weather swap. Fri 23 dry by day (rain likely evening), Sat 24 heavy rain all morning. Fushimi Inari moves to Fri morning, the bamboo grove to a short Sat rain morning. Nozomi 16 at 12:01 protected.
D[23]['title'] = 'Kyoto: Fushimi Inari, the Golden Pavilion, Higashiyama'
_r = D[23]['rows']
D[23]['rows'] = [
 R('06:30', 'To Kyoto Station, then JR Nara line to Inari', 'One subway stop or a 15 minute walk to the station. Inari is two stops, about 5 minutes, and the shrine gate faces the platform.'),
 R('07:00', 'Fushimi Inari', 'Dry and quiet this morning. Up through the gates to the Yotsutsuji viewpoint, about 45 minutes, for the view over Kyoto, then back down. A crush by ten. Open 24 hours.'),
 R('09:15', 'JR back to Kyoto Station', 'Two stops. Coffee at the station.'),
 R('09:30', 'Taxi to Kinkaku-ji', 'From the rank on the Karasuma side, about 30 minutes.'),
 R('10:00', 'Kinkaku-ji, the Golden Pavilion', 'The gold pavilion on its pond. One-way garden loop, about 45 minutes. Open 09:00 to 17:00.'),
 R('11:00', 'Optional: Nijō Castle', 'Taxi about 15 minutes. The squeaky nightingale floors. Open from 08:45.'),
 R('12:30', 'Lunch: Katsugyu Yodobashi', 'Taxi about 15 minutes. Crumbed beef cutlet you finish on a hot stone, Yodobashi Kyoto 6F. Open 11:00 to 23:00.'),
 R('13:30', 'Hotel, rest', 'Ten minutes on foot up Karasuma-dōri.'),
] + _r[_row(23, '15:30'):]
D[23]['foot'] = 'Dry by day, rain likely from the evening (about 70%). Umbrellas for Gion and Pontochō.'
D[24]['title'] = 'Bamboo grove in the rain, back to Tokyo, fireworks night'
_r = D[24]['rows']
D[24]['rows'] = [
 R('06:30', 'To Kyoto Station, then the JR Sagano line', 'Taxi to the station in the rain, about 5 minutes, or one subway stop. JR Sagano line to Saga-Arashiyama, about 15 minutes.'),
 R('07:05', 'Bamboo grove', 'About 10 minutes on foot from the station. A short, flat, paved path that suits rain, and nearly empty this early. Keep it short.'),
 R('08:30', 'Optional: Tenryū-ji as it opens', 'Opens 08:30, the north gate is at the end of the bamboo path. Only if the rain is light. The villa, the river path and lunch are dropped today.'),
 R('09:05', 'JR back to Kyoto, then the hotel', 'About 15 minutes on the train, then a taxi or one subway stop. Back by about 09:40.'),
 R('09:40', 'Shower and repack', ''),
 R('10:30', 'Check out, taxi to Kyoto Station', 'About 5 minutes with the bags in the rain. Walking is 15 minutes in the dry (How-to 16).'),
] + _r[_row(24, '11:15'):]
D[24]['foot'] = 'Wet morning: raincoats and good shoes. If the rain is very heavy, skip Arashiyama and have a slow breakfast near the hotel instead. Work back from the 12:01: on the platform by 11:45, at the station by 11:15, check out 10:30.'
D[23]['cal'] = 'Inari, Gion'
D[24]['cal'] = 'Bamboo, fireworks'
D[23]['sum'] = 'Fushimi Inari first thing while it is dry and quiet, the Golden Pavilion, a beef cutlet lunch and a rest, Higashiyama in the late light, then gyoza and Pontochō.'
D[24]['sum'] = 'A short, early bamboo grove walk in the rain, the train back to Tokyo, an hour at the hotel, then fireworks over the bay from Odaiba. Dinner comes after the show, so the trains have cleared by the time you leave.'
LEGS['k']['sum'] = 'One clear idea a day. Nara on arrival, a full day in Osaka, Fushimi Inari and Higashiyama on Friday, and a short bamboo grove morning before the train back to Tokyo.'
# 21 Oct 09:48: step by step for Kyoto Station, bags and the train to Nara (How-to 31)
HOWTO.append(('Kyoto Station, bags and the train to Nara, Wed 21', [
 'Off the train (10:00): take the escalator down from the platform and go through the Shinkansen gates. Tap the same Suica you tapped in with, or put your tickets in. You are now on the south side of the station. Follow the signs for Central Gate (中央口) and the Karasuma side, along the upper walkway that crosses over the tracks. About 7 minutes with bags.',
 'Drop the bags at Crosta (about 10:15): from the Central Gate take the escalator down to B1. The Crosta Kyoto baggage counter is behind the escalators, signed for baggage. Map: https://www.google.com/maps/search/?api=1&query=Crosta+Kyoto+baggage',
 'Before the bags go over the counter, take out: passports, wallets and cards, phones, chargers and power bank, medication, umbrellas, and a light layer for the evening rain. Valuables are not accepted. ¥1,000 per bag, open until 20:00. Keep the receipt: you need it to collect.',
 'Walk to the Kintetsu line (about 10:30): back up the escalator and south through the station\'s central passage to the Kintetsu gates (近鉄), about 10 minutes. Signs say Kintetsu Line, in red and white. Map: https://www.google.com/maps/search/?api=1&query=Kintetsu+Kyoto+Station',
 'Buy the ticket: at the Kintetsu machines tap English. Buy Kintetsu-Nara (近鉄奈良) with a limited express seat (特急), about ¥1,280 each, 35 minutes, reserved seats.',
 'Check the destination on the ticket: some limited expresses go to Kashiharajingū-mae (橿原神宮前), which is not Nara. Yours must say 近鉄奈良, Kintetsu-Nara.',
 'No seats left: take the Express (急行) to Nara on Suica instead. ¥760, about 45 minutes, no ticket needed.',
 'Board (about 10:40): ticket through the gate, find the platform on the board, and the car and seat on the ticket. The limited express is the smart cream or red train with numbered cars. Get off at the end of the line, Kintetsu-Nara.',
 'In Nara (about 11:15): take the exit for Higashimuki (東向), which comes straight up into the covered Higashimuki arcade. Walk through to Sanjō-dōri, then about 10 minutes east to lunch at Kamameshi Shizuka.',
 'Coming back (about 16:45): Kintetsu limited express from Kintetsu-Nara back to Kyoto, about 35 minutes, arriving about 17:20. Walk to the Central Gate, down to B1, and collect the bags with the receipt.',
 'To the hotel: walk about 15 minutes straight up Karasuma-dōri (exit on the Kyoto Tower side), or the Karasuma subway one stop to Gojō. In the rain with bags, a taxi from the north rank, about 5 minutes.',
]))
_HN = len(HOWTO)
_r = D[21]['rows']
_i = _row(21, '10:00'); _r[_i] = R(_r[_i][0], _r[_i][1], ('Step by step: How-to %d.' % _HN), *_r[_i][3:])
for _t in ('10:15', '10:40', '16:45'):
    _i = _row(21, _t); _r[_i] = R(_r[_i][0], _r[_i][1], _r[_i][2] + (' Step by step: How-to %d.' % _HN), *_r[_i][3:])
# Wed 21 actuals to 11:23: on the 11:25 Kintetsu to Nara, about 45 minutes late. Day retimed.
_r = D[21]['rows']
for _t in ('05:55', '06:30', '07:00', '07:55', '10:00', '10:15'):
    _i = _row(21, _t); _r[_i] = R(_r[_i][0], _r[_i][1], _r[_i][2], DN)
_i = _row(21, '10:40'); _r[_i] = R('11:25', 'Kintetsu to Nara', 'Boarded the 11:25. Kintetsu-Nara about 12:10 (How-to 31).', DN)
_new = {
 '11:15': ('12:10', 'Kintetsu Nara, up into Higashimuki arcade', 'Exit for Higashimuki (東向). Covered to Sanjō-dōri. Nakatanidō mochi pounding at the end.'),
 '11:30': ('12:25', 'Lunch: Kamameshi Shizuka', 'Iron-pot rice cooked to order, about 20 minutes. Ten minutes east, beside Isuien. Long queue: a kakinoha sushi box instead.'),
 '12:45': ('13:30', 'Into Nara Park for the deer', 'Straight onto the lawns towards Kasuga. Deer crackers about ¥200.'),
 '13:35': ('14:15', 'Kasuga Taisha and the lantern path', 'Up through the stone lanterns to the shrine front. No need to pay to go inside.'),
 '14:25': ('15:00', 'Tōdai-ji and the Great Buddha', 'Twenty minutes north along the hill, in through the Nandaimon gate. Open until 17:30.'),
 '15:30': ('15:50', 'Optional: Nigatsu-dō', 'Ten minutes uphill behind the main hall. Skip it if the rain has started (from about 16:00).'),
 '16:15': ('16:30', 'Walk down to Kintetsu Nara', 'About 20 minutes downhill. In rain: a taxi from the Tōdai-ji gate.'),
 '16:45': ('17:00', 'Kintetsu back to Kyoto', 'Limited express about 35 minutes, Express (急行) on Suica about 45. Kyoto about 17:40. Collect the bags (How-to 31).'),
 '17:25': ('17:45', 'Kyoto Station building', 'Quick look at the lit staircase on the way through, or skip it in the rain.'),
 '17:45': ('18:00', 'To sequence KYOTO GOJO, check in', 'Taxi from the north rank in the rain, about 5 minutes. Or walk 15 minutes up Karasuma-dōri, or one subway stop to Gojō.'),
}
for _o, _v in _new.items():
    _i = _row(21, _o); _r[_i] = R(_v[0], _v[1], _v[2], *_r[_i][3:])
D[21]['rows'] = [x for x in D[21]['rows'] if not (x[0] == '17:45' and x[1].startswith('Walk to sequence'))]
_r = D[21]['rows']; _i = _row(21, '18:00')
_r.insert(_i, R('17:45', 'Kyoto Station building', 'Quick look at the lit staircase on the way through, or skip it in the rain.'))
# 21 Oct 11:34: bags sent from Crosta to the hotel, arriving 17:00. No collection at the station.
_r = D[21]['rows']
_i = _row(21, '10:15'); _r[_i] = R('10:15', 'Bags sent to the hotel from Crosta Kyoto', 'Delivered to sequence KYOTO GOJO by 17:00.', DN)
_i = _row(21, '17:00'); _r[_i] = R('17:00', 'Kintetsu back to Kyoto', 'Limited express about 35 minutes, Express (急行) on Suica about 45. Kyoto about 17:40. No bags to collect: they are at the hotel.', *_r[_i][3:])
_i = _row(21, '18:00'); _r[_i] = R('18:00', 'To sequence KYOTO GOJO, check in', 'The bags are waiting there. One subway stop to Gojō, or 15 minutes on foot up Karasuma-dōri, or a short taxi in the rain.', *_r[_i][3:])
# 21 Oct 11:41: Wed evening. Ramen at the station, Kyoto Tower, check in, then two options: nearby (first choice) or Pontochō if dry.
_r = D[21]['rows']
_k = _row(21, '17:45')
D[21]['rows'] = _r[:_k] + [
 R('17:40', 'Ramen: Honke Daiichi Asahi', 'Five minutes east of Kyoto Station. The queue moves fast. Closed Thursdays, so tonight is the night.'),
 R('18:30', 'Kyoto Tower at night', 'Opposite the station, north side. ¥900, open to 21:00, last entry 20:30.'),
 R('19:15', 'To sequence KYOTO GOJO, check in', 'The bags are waiting there. One subway stop to Gojō, or 15 minutes on foot up Karasuma-dōri, or a short taxi in the rain.'),
 R('20:00', 'Option A, nearby (first choice): massage and the Teramachi arcades', 'Covered and close, so fine in rain. A foot or body massage at YUMEMISHI (to 21:00) or Hannari (to 22:00), both at Shijō-Karasuma, 10 minutes north. Book ahead for about 20:00. The Teramachi and Shinkyōgoku arcades are 10 minutes further east.'),
 R('20:00', "Option B, if it is dry: Pontochō and Bee's Knees", "Short taxi to Shijō-Kawaramachi. Walk the Pontochō alley, then a cocktail at Bee's Knees, walk-in. Doing it tonight covers a wet Friday night."),
]
D[21]['foot'] = 'Light rain likely from about 16:00. Stags are pushy: feed the does.'
# 21 Oct 11:48: plan kept. Taxi options added, rain now from about 15:00.
_r = D[21]['rows']
def _add(t, extra):
    _i = _row(21, t); _r[_i] = R(_r[_i][0], _r[_i][1], _r[_i][2] + ' ' + extra, *_r[_i][3:])
_add('12:10', 'Taxi option: rank outside the station, about 5 minutes to lunch.')
_add('14:15', 'Taxi option: Kasuga Taisha has a rank by the car park, and the GO app works in Nara.')
_add('15:00', 'Rain from about 15:00, so the big hall is a good place to be.')
_i = _row(21, '15:50'); _r[_i] = R('15:50', 'Optional: Nigatsu-dō', 'Ten minutes uphill behind the main hall, steep stone steps. Skip it in the rain.', *_r[_i][3:])
_i = _row(21, '16:30'); _r[_i] = R('16:30', 'Back to Kintetsu Nara', 'About 20 minutes on foot, or a taxi from the Tōdai-ji gate, about 5 minutes, in the rain.', *_r[_i][3:])
D[21]['foot'] = 'Sunny and about 30° until 14:00, light rain from about 15:00 into the evening. Stags are pushy: feed the does.'

# Wed 21 actuals, from G's Copy for Claude paste (21:48). Whole day done.
_o = {x[0]: x for x in D[21]['rows']}
D[21]['rows'] = [
 R('05:55', 'Wake, final pack, check out by 06:20', '', DN),
 R('06:30', 'Taxi to Shinagawa, Kōnan exit', '', DN),
 R('07:00', 'Shinagawa, ekiben and coffee', '', DN),
 R('07:55', 'Nozomi 13 to Kyoto', 'Car 9, seats 16-C and 16-D, Green Car.', B, DN) if False else R('07:55', 'Nozomi 13 to Kyoto', 'Car 9, seats 16-C and 16-D, Green Car.', DN),
 R('10:00', 'Kyoto Station', 'Step by step: How-to 31.', DN),
 R('10:30', 'Bags sent to the hotel from Crosta Kyoto', 'Delivered to sequence KYOTO GOJO by 17:00.', DN),
 R('11:25', 'Kintetsu to Nara', '', DN),
 R('12:10', 'Kintetsu Nara, up into Higashimuki arcade', '', DN),
 R('13:30', 'Into Nara Park for the deer', 'No crackers for us. Watched the deer harass everyone else.', DN),
 R('14:15', 'Kasuga Taisha and the lantern path', '', DN),
 R('14:30', 'Wakakusa-yama, first peak lookout', 'Amazing views over Nara, and an ice-cold beer from the hut at the top.', DN),
 R('15:30', 'Nigatsu-dō', '', DN),
 R('16:00', 'Tōdai-ji and the Great Buddha', 'Past the Isuien garden for photos on the way.', DN),
 R('16:30', 'Back to Kintetsu Nara', 'Maccas pit stop: burgers, chips and soft serve.', DN),
 R('17:00', 'Kintetsu back to Kyoto', '', DN),
 R('18:40', 'AEON Mall Kyoto', 'New runners for Cynthia.', DN),
 R('19:15', 'Ramen: Honke Daiichi Asahi', 'Queue outside, tickets from the machine inside.', DN),
 R('20:15', 'Yodobashi Kyoto', 'Suitcase hunt: Gran Sac\'s on 5F.', DN),
 R('21:00', 'To sequence KYOTO GOJO, check in', '', DN),
]
D[21]['foot'] = ''

# 22 Oct 00:22: Thu 22 rebuilt. Shitennō-ji flea market (22nd of the month) in the morning, Osaka's best food, KOMEHYO only for shopping, Umeda Sky at sunset, castle by night only.
D[22]['title'] = 'Osaka: flea market, Shinsekai, Dōtonbori, castle by night'
D[22]['sum'] = 'The Shitennō-ji flea market first thing, kushikatsu in Shinsekai, Namba snacks and KOMEHYO, Umeda Sky at sunset, then Dōtonbori, okonomiyaki and the castle lit up.'
D[22]['rows'] = [
 R('07:30', 'To Kyoto Station, then JR to Tennōji', 'One subway stop or 15 minutes on foot. JR special rapid to Osaka, about 30 minutes, then the Osaka Loop line to Tennōji, about 20 minutes. Suica covers it all.'),
 R('08:45', 'Shitennō-ji flea market', 'On the 21st and 22nd of every month, from 08:30. Kimono and yukata, pottery, vintage toys and records, masks, food stalls. Breakfast from the stalls. Free. Cash and a tote bag.'),
 R('10:30', 'Shinsekai: Tsūtenkaku and Janjan-Yokochō', 'About 15 minutes on foot west of the temple. The retro neon district under the tower.'),
 R('11:00', 'Kushikatsu lunch: Daruma Shinsekai', 'Osaka\'s fried skewers. In at the 11:00 opening, before the queue. No double-dipping in the shared sauce.'),
 R('12:00', 'Midōsuji line to Namba', 'From Dōbutsuen-mae, two stops, about 5 minutes. Buy the one-day Enjoy Eco Card at the machine, about ¥820. It covers the Osaka Metro all day.'),
 R('12:15', 'Rikuro cheesecake and 551 Hōrai pork buns', 'The jiggly cheesecake: take the freshly baked line for a warm one. 551 Hōrai\'s pork buns are a minute away.'),
 R('12:45', 'Namba Yasaka Shrine', 'The giant lion head. About 10 minutes on foot. Ten minutes there is enough.'),
 R('13:30', 'KOMEHYO Shinsaibashi', 'The flagship pre-owned luxury store, several floors. Open 11:00 to 20:00. Passports for tax-free.'),
 R('14:45', 'Takoyaki in Dōtonbori, then coffee and a sit-down', 'Octopus balls at Kukuru or any of the stands on the canal. Let them cool first.'),
 R('16:15', 'Umeda Sky deck at sunset', 'Midōsuji line Shinsaibashi to Umeda, about 7 minutes, then 15 minutes on foot. Sunset about 17:05. Open to 22:30.'),
 R('17:45', 'Midōsuji line back to Namba', 'About 10 minutes.'),
 R('18:15', 'Dōtonbori and the Tombori River Cruise', 'Buy cruise tickets when you arrive and ride after dark (How-to 15). The Glico Running Man photo spot is opposite the sign.'),
 R('18:45', 'Okonomiyaki dinner: Mizuno', 'Osaka\'s savoury pancake of pork and cabbage, cooked on the griddle. Open to 22:00. Then a quick look at Hōzenji Yokochō, two streets back.'),
 R('20:00', 'Taxi to Osaka Castle', 'About 15 minutes, about ¥1,800. Ask for Ōsaka-jō, Ōtemon (大阪城 大手門).'),
 R('20:30', 'Osaka Castle light show, SINFONIA', 'Free projection mapping on the south face of the keep. About six minutes, repeating until 22:00. Standing only. Can be cancelled in bad weather.'),
 R('21:15', 'Home: taxi to JR Osaka, then the special rapid', 'Taxi about 15 minutes, about ¥2,000. Special rapid to Kyoto about 30 minutes, then one subway stop to Gojō. Back about 22:15.'),
]
D[22]['notes'] = [
 ('Running late', 'Drop Umeda Sky first, then Shinsekai. Protect the flea market before noon, Daruma at opening and the light show.'),
 ('Walking', 'About 11 to 12 km with the two taxis. Skipping Umeda Sky saves about 2.5 km.'),
 ('Left out', 'The morning castle walk, the Horie and Amerikamura browsing, and Kuromon Market.')]
D[22]['foot'] = ''
# Thu 22 12:13: arrived at Daruma 12:12, about 70 minutes behind. Same plan, afternoon retimed; Umeda Sky still for sunset.
_r = D[22]['rows']
_i = _row(22, '07:30'); _r[_i] = R(*_r[_i][:3], DN)
_i = _row(22, '08:45'); _r[_i] = R(*_r[_i][:3], DN)
_new = [
 ('10:30', '11:45', None, DN),
 ('11:00', '12:15', None, None),
 ('12:00', '13:00', None, None),
 ('12:15', '13:15', "The jiggly cheesecake: take the freshly baked line for a warm one. 551 Hōrai's pork buns are a minute away. Suitcase: Bic Camera Namba is close by for a quick look, buy later.", None),
 ('12:45', '13:45', None, None),
 ('13:30', '14:15', None, None),
 ('14:45', '15:30', 'Octopus balls at Kukuru or any of the stands on the canal. A shorter sit-down today, leave by 16:10 for Umeda.', None),
]
for _o, _t, _txt, _st in _new:
    _i = _row(22, _o); _x = _r[_i]
    _r[_i] = R(_t, _x[1], _txt if _txt is not None else _x[2], *( [_st] if _st else list(_x[3:]) ))
_i = _row(22, '18:15'); _x = _r[_i]
_r[_i] = R(_x[0], _x[1], _x[2] + ' Suitcase: Don Quijote by the ferris wheel has cheap ones. The taxis can take it.', *_x[3:])
# fix the retime by title (time lookups collided)
def _set(title_start, t, txt=None):
    for _i, _x in enumerate(D[22]['rows']):
        if _x[1].startswith(title_start):
            D[22]['rows'][_i] = R(t, _x[1], txt if txt is not None else _x[2], *_x[3:]); return
_set('Kushikatsu lunch', '12:15', 'Osaka\'s fried skewers. No double-dipping in the shared sauce.')
_set('Rikuro cheesecake', '13:15', "The jiggly cheesecake: take the freshly baked line for a warm one. 551 Hōrai's pork buns are a minute away. Suitcase: Bic Camera Namba is close by for a quick look, buy later.")
D[22]['rows'].sort(key=lambda x: x[0])
