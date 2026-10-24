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
# Thu 22 12:53: skipped Daruma. Straight to Namba from Janjan-Yokochō.
D[22]['rows'] = [x for x in D[22]['rows'] if not x[1].startswith('Kushikatsu lunch')]
_set('Shinsekai', '11:45')
_set('Midōsuji line to Namba', '12:55', 'Walk Janjan-Yokochō away from Tsūtenkaku to the end of the covered lane: the Dōbutsuen-mae stairs (red M, 動物園前) are at the junction. Buy the Enjoy Eco Card, about ¥820, then two stops towards Umeda to Namba.')
D[22]['rows'].sort(key=lambda x: x[0])

# Thu 22 14:42: Umeda Sky moved to last thing, at night, on the way to JR Osaka. Street eats slipped in before Dōtonbori.
_k = next(i for i, x in enumerate(D[22]['rows']) if x[1].startswith('KOMEHYO'))
D[22]['rows'] = D[22]['rows'][:_k+1] + [
 R('15:15', 'Amerikamura and Triangle Park', 'Five minutes west of Shinsaibashi-suji. Street fashion, murals and street food. Takoyaki at Kōgaryū by Triangle Park.'),
 R('16:00', 'Kuromon Market street eats', 'About 20 minutes on foot, or a short taxi. Wagyu skewers, tamagoyaki, fruit and mochi. Skip the big seafood platters. Most stalls wind down by about 17:00.'),
 R('17:15', 'Dōtonbori as the lights come on', 'Sunset about 17:05. The Glico Running Man, takoyaki at Kukuru, and the Tombori River Cruise once it is dark (How-to 15). Suitcase: Don Quijote by the ferris wheel has cheap ones.'),
 R('18:15', 'Hōzenji Yokochō', 'Two streets back. Stone lanes, lanterns and the moss-covered Mizukake Fudō. Splash a ladle of water on the statue.'),
 R('18:30', 'Okonomiyaki dinner: Mizuno', 'Osaka\'s savoury pancake of pork and cabbage, cooked on the griddle. Open to 22:00.'),
 R('19:30', 'Taxi to Osaka Castle', 'About 15 minutes, about ¥1,800. Ask for Ōsaka-jō, Ōtemon (大阪城 大手門).'),
 R('19:45', 'Osaka Castle light show, SINFONIA', 'Free projection mapping on the south face of the keep. About six minutes, repeating until 22:00. Standing only.'),
 R('20:30', 'Taxi to Umeda Sky', 'About 15 minutes, about ¥2,000. Ask for Umeda Sky Building (梅田スカイビル).'),
 R('20:45', 'Umeda Sky deck at night', 'Tickets at the counter about ¥2,000, or book online to skip the line. Open to 22:00, go up by 21:30. The open-air roof deck over the city lights.'),
 R('21:30', 'Walk to JR Osaka, special rapid home', 'About 15 minutes on foot. Special rapid to Kyoto, about 30 minutes, then one subway stop to Gojō. Back about 22:20.'),
]
D[22]['notes'] = [
 ('Running late', 'Drop Kuromon first, then Amerikamura. Protect Dōtonbori at dusk, the light show and Umeda Sky by 21:30.'),
 ('Walking', 'About 10 to 11 km with the taxis.'),
 ('Left out', 'The morning castle walk, Daruma kushikatsu, and the Horie browsing.')]
# Thu 22 14:45: left Bic Camera Namba. Lion head next, then KOMEHYO, then Amerikamura's vintage and retro streets. Kuromon dropped (stalls close about 17:00).
_r22 = D[22]['rows']
_set('Rikuro cheesecake', '13:15')
_set('Namba Yasaka Shrine', '14:50', 'The giant lion head. About 10 minutes on foot west of Namba. Ten minutes there is enough. Closes about 17:00.')
_set('KOMEHYO Shinsaibashi', '15:30', 'The flagship pre-owned luxury store, several floors. Open 11:00 to 20:00. About 15 minutes on foot from Namba Yasaka, or a taxi. Passports for tax-free.')
_set('Amerikamura and Triangle Park', '16:30', 'Five minutes west of KOMEHYO across Midōsuji. Vintage and retro shops, street fashion, murals and street food. Takoyaki at Kōgaryū by Triangle Park.')
D[22]['rows'] = [x for x in D[22]['rows'] if not x[1].startswith('Kuromon Market')]
D[22]['rows'].sort(key=lambda x: x[0])
D[22]['notes'] = [
 ('Running late', 'Shorten KOMEHYO first, then Amerikamura. Protect Dōtonbori at dusk, the light show and Umeda Sky by 21:30.'),
 ('Walking', 'About 10 km with the taxis.'),
 ('Left out', 'The morning castle walk, Daruma kushikatsu, Kuromon Market and the Horie browsing.')]
# Thu 22 15:34: free time in Namba, Shinsaibashi and Dōtonbori until the castle.
_set('Namba Yasaka Shrine', '14:50')
for _i, _x in enumerate(D[22]['rows']):
    if _x[1].startswith('Namba Yasaka Shrine') or _x[1].startswith('Rikuro') or _x[1].startswith('Midōsuji line to Namba'):
        D[22]['rows'][_i] = R(*_x[:3], DN)
_keep = [x for x in D[22]['rows'] if not any(x[1].startswith(t) for t in ('KOMEHYO', 'Amerikamura', 'Dōtonbori as the lights', 'Hōzenji', 'Okonomiyaki dinner'))]
_i = next(i for i, x in enumerate(_keep) if x[1].startswith('Taxi to Osaka Castle'))
D[22]['rows'] = _keep[:_i] + [
 R('15:30', 'Free time: Shinsaibashi, Amerikamura and Dōtonbori', 'Shopping, street eats and the lights coming on at sunset (about 17:05). Ideas: KOMEHYO (to 20:00), Amerikamura and Kōgaryū takoyaki, the Glico Running Man from Ebisu Bridge, takoyaki at Kukuru, Don Quijote with the ferris wheel (cheap suitcases), the Tombori River Cruise once dark (How-to 15), Hōzenji Yokochō, and okonomiyaki at Mizuno for dinner (open to 22:00). Taxi to the castle about 19:30.'),
] + _keep[_i:]
# Thu 22 15:39: free time as one bucket-list block.
for _i, _x in enumerate(D[22]['rows']):
    if _x[1].startswith('Free time'):
        D[22]['rows'][_i] = R('15:30', 'Free time: the Dōtonbori bucket list',
         'Any order. 1. The Glico Running Man from Ebisu Bridge. 2. Don Quijote ferris wheel, Ebisu Tower: ¥1,000, about 15 minutes, best after dark. 3. Tombori River Cruise, about 20 minutes, once it is dark. 4. Okonomiyaki dinner at Mizuno, the best in Osaka, open to 22:00. 5. Takoyaki at Kukuru under the giant octopus. 6. The big signs: the moving Kani Dōraku crab and the Kuidaore Tarō drummer. 7. Hōzenji Yokochō and the mossy Mizukake Fudō. 8. KOMEHYO, to 20:00. 9. Amerikamura and Kōgaryū takoyaki. 10. A cheap suitcase at Don Quijote. Taxi to the castle about 19:30.')
# Thu 22 16:14: Hōzenji Yokochō back in as its own item, after dark, before the castle.
D[22]['rows'].append(R('19:00', 'Hōzenji Yokochō, lit up', 'The stone lane with lanterns, one street south of the Dōtonbori main street near Nakaza Cuidaore. Splash water on the moss-covered Mizukake Fudō. A minute from Mizuno, so pair it with dinner.'))
D[22]['rows'].sort(key=lambda x: x[0])
# Thu 22 19:47: Glico done, at Hōzenji Yokochō now. Evening pushed about 35 minutes; castle and Umeda Sky still on.
for _i, _x in enumerate(D[22]['rows']):
    if _x[1].startswith('Free time'):
        D[22]['rows'][_i] = R('15:30', _x[1], _x[2], DN)
_set('Hōzenji Yokochō', '19:45')
_set('Taxi to Osaka Castle', '20:05', 'About 15 to 20 minutes, about ¥1,800. Ask for Ōsaka-jō, Ōtemon (大阪城 大手門). Then about 10 minutes on foot to the keep.')
_set('Osaka Castle light show', '20:30', 'Free projection mapping on the south face of the keep. About six minutes, repeating until 22:00. Standing only. Watch one or two rounds.')
_set('Taxi to Umeda Sky', '21:00', 'Taxi rank on the road outside Ōtemon. About 15 to 20 minutes, about ¥2,000. Ask for Umeda Sky Building (梅田スカイビル).')
_set('Umeda Sky deck at night', '21:20', 'Tickets at the counter about ¥2,000. Last entry about 22:00, closes 22:30. The open-air roof deck over the city lights. Drop it if the castle runs over.')
_set('Walk to JR Osaka', '22:00', 'About 15 minutes on foot. Special rapid to Kyoto, about 30 minutes, then one subway stop to Gojō. Back about 22:50.')
D[22]['rows'].sort(key=lambda x: x[0])
D[22]['notes'] = [
 ('Running late', 'Drop Umeda Sky first. Protect the castle light show (runs until 22:00).'),
 ('Walking', 'About 10 km with the taxis.'),
 ('Left out', 'The morning castle walk, Daruma kushikatsu, Kuromon Market and the Horie browsing.')]
# Thu 22 19:50: skipped Hōzenji Yokochō, taxi to the castle now.
D[22]['rows'] = [x for x in D[22]['rows'] if not x[1].startswith('Hōzenji Yokochō')]
_set('Taxi to Osaka Castle', '19:50')
_set('Osaka Castle light show', '20:15')
_set('Taxi to Umeda Sky', '20:45')
_set('Umeda Sky deck at night', '21:05')
_set('Walk to JR Osaka', '21:45', 'About 15 minutes on foot. Special rapid to Kyoto, about 30 minutes, then one subway stop to Gojō. Back about 22:30.')
D[22]['rows'].sort(key=lambda x: x[0])
# Thu 22 20:16: bucket list all done except the Tombori cruise. First taxi went to Tsūtenkaku by mistake; second taxi to the castle now.
for _i, _x in enumerate(D[22]['rows']):
    if _x[1].startswith('Free time'):
        D[22]['rows'][_i] = R('15:30', _x[1], _x[2] + ' Done: all except the Tombori River Cruise.', DN)
    if _x[1].startswith('Taxi to Osaka Castle'):
        D[22]['rows'][_i] = R('19:50', _x[1], _x[2] + ' Note: the first taxi went to Tsūtenkaku (the Hitachi tower) by mistake. Second taxi from Shinsekai about 20:15.', DN)
_set('Osaka Castle light show', '20:40')
_set('Taxi to Umeda Sky', '21:10')
_set('Umeda Sky deck at night', '21:30')
_set('Walk to JR Osaka', '22:05', 'About 15 minutes on foot. Special rapid to Kyoto, about 30 minutes, then one subway stop to Gojō. Back about 22:50.')
D[22]['rows'].sort(key=lambda x: x[0])
# Thu 22 20:49: light show done. Umeda Sky skipped. Home by train from Osakajōkōen.
for _i, _x in enumerate(D[22]['rows']):
    if _x[1].startswith('Osaka Castle light show'):
        D[22]['rows'][_i] = R('20:40', _x[1], _x[2], DN)
D[22]['rows'] = [x for x in D[22]['rows'] if not any(x[1].startswith(t) for t in ('Taxi to Umeda Sky', 'Umeda Sky deck', 'Walk to JR Osaka'))]
D[22]['rows'] += [
 R('20:50', 'Walk to JR Osakajōkōen station', 'From the keep, head north-east over Gokuraku-bashi bridge and out past the Aoyamon gate, about 15 minutes. Station: 大阪城公園駅 (Ōsakajōkōen).'),
 R('21:05', 'JR Loop line to Osaka, then the special rapid to Kyoto', '1. Loop line (大阪環状線) toward Kyōbashi and Osaka (大阪), 4 stops, about 10 minutes. 2. At Osaka, follow the JR Kyoto line (京都線) signs and take the special rapid (新快速) to Kyoto, about 30 minutes. 3. At Kyoto, Karasuma subway line toward Kokusaikaikan (国際会館), one stop to Gojō. All on Suica.'),
 R('22:15', 'Back at the hotel', 'Gojō Exit 2, about 3 minutes on foot.'),
]
D[22]['rows'].sort(key=lambda x: x[0])
D[22]['notes'] = [
 ('Walking', 'About 10 km with the taxis.'),
 ('Left out', 'The morning castle walk, Daruma kushikatsu, Kuromon Market, the Horie browsing, the Tombori cruise, Hōzenji Yokochō and Umeda Sky.')]
# Thu 22 20:52: clearer directions home, with the castle exit.
_set('Walk to JR Osakajōkōen station', '20:50', 'Leave the keep by the north side over Gokuraku-bashi (極楽橋), turn right along the moats, out through Aoyamon gate (青屋門), then east past Osaka-jō Hall to JR 大阪城公園駅. About 15 minutes. Directions under ⓘ.')
_set('JR Loop line to Osaka', '21:05', '1. Platform for 京橋・大阪方面 (outer loop, 外回り), 4 stops to Osaka, about 10 minutes. 2. At Osaka, stay inside the gates, follow 京都線 signs (usually platform 7 or 8) and take the 新快速 to 京都, about 30 minutes. 3. At Kyoto, Karasuma subway toward 国際会館, one stop to Gojō. 4. Exit for Karasuma-dōri, 2 to 3 minutes to the hotel. All on Suica.')
_set('Back at the hotel', '22:15', 'sequence KYOTO GOJO.')
# Thu 22 21:13: walked out to Temmabashi instead. Home on the Keihan line, no changes.
D[22]['rows'] = [x for x in D[22]['rows'] if not any(x[1].startswith(t) for t in ('Walk to JR Osakajōkōen', 'JR Loop line to Osaka'))]
D[22]['rows'] += [
 R('20:50', 'Walk to Temmabashi', 'From the castle out to Temmabashi station.', DN),
 R('21:15', 'Keihan line to Kyoto', '1. Keihan Temmabashi (京阪 天満橋), platform for 京都・出町柳 (Kyoto, Demachiyanagi). 2. Take the 特急 (limited express), about 45 minutes, to 七条 (Shichijō). 3. Taxi about 5 minutes, about ¥800, or walk 18 minutes west along Shichijō then up Karasuma. All on Suica.'),
]
D[22]['rows'].sort(key=lambda x: x[0])

# Thu 22 21:50: Sat morning cleared for a sleep in, packing and a slow breakfast. The bamboo grove moves to Fri 23, first thing. Nijō back in. Lunch options. Hotel stop optional.
D[23]['title'] = 'Kyoto: bamboo grove, Golden Pavilion, Nijō, Inari, Higashiyama'
D[23]['cal'] = 'Bamboo, Inari, Gion'
D[23]['sum'] = 'West to east across Kyoto: the bamboo grove while it is quiet, the Golden Pavilion, Nijō Castle in daylight, lunch on the way, Fushimi Inari in the afternoon light, then Kiyomizu-dera at sunset, gyoza and Pontochō.'
D[23]['foot'] = 'Dry by day, up to about 21°C. Light rain from about 21:00: umbrella for Pontochō. About 13 km on foot, the taxis do the long legs.'
_eve = [x for x in D[23]['rows'] if x[0] >= '15:30']
D[23]['rows'] = [
 R('07:00', 'Taxi to the bamboo grove', 'About 25 minutes, about ¥3,500. Show the driver 嵐山 竹林の小径 (Arashiyama bamboo grove), drop at Nonomiya Shrine (野宮神社). Or JR Sagano line from Kyoto to Saga-Arashiyama, about 45 minutes door to door.'),
 R('07:30', 'Bamboo grove', 'Nearly empty this early. Walk the path up to the Ōkōchi Sansō gate and back, about 30 minutes.'),
 R('08:30', 'Tenryū-ji garden', 'Opens 08:30. The north gate is on the bamboo path. Pond garden with the hills behind, about 40 minutes. About ¥500 each.'),
 R('09:15', 'Togetsukyō bridge and % Arabica', 'Out of Tenryū-ji\'s main gate, 5 minutes to the river. Coffee to take away (opens 09:00), drink it on the riverbank looking at the bridge.'),
 R('09:45', 'Taxi to Kinkaku-ji', 'From the rank by Togetsukyō or the main street, about 20 minutes, about ¥2,500. Show 金閣寺.'),
 R('10:05', 'Kinkaku-ji, the Golden Pavilion', 'The gold pavilion on its pond. One-way garden loop, about 45 minutes. Open 09:00 to 17:00. About ¥500 each.'),
 R('11:00', 'Taxi to Nijō Castle', 'About 15 minutes, about ¥2,000. Show 二条城 東大手門 (the east main gate).'),
 R('11:15', 'Nijō Castle', 'The shōgun\'s palace in daylight: the Ninomaru Palace with its nightingale floors, then the gardens and the keep walls. About 75 minutes. About ¥1,300 each. Last entry 16:00.'),
 R('12:30', 'Lunch: pick one', 'Near Nijō: Soba Tatsuichi (hand-made soba and duck soba, 5 minutes east, name on the list, to 16:00) or Sarashina (tiny family soba and curry udon, cash only, to 18:00). On the way back: Kyosaimi Nomura (obanzai, a dozen Kyoto home-style small dishes, to 14:00) or Ichiran Kyoto Karasuma (ramen in a booth, to 22:00). At Kyoto Station: Katsugyu Yodobashi (beef cutlet on a hot stone, to 23:00).'),
 R('13:30', 'Optional: hotel to change and refresh', 'Taxi from Nijō about 10 minutes, or the subway: Tōzai line from Nijōjō-mae to Karasuma Oike, then the Karasuma line two stops to Gojō. The taxi is simpler. Skip it if you are running late and go straight to Inari.'),
 R('14:15', 'JR Nara line to Inari', 'From the hotel: subway one stop to Kyoto, then the JR Nara line (奈良線), two stops, about 5 minutes. The shrine gate faces the platform.'),
 R('14:30', 'Fushimi Inari', 'Up through the thousand gates to the Yotsutsuji lookout over Kyoto and back, about 90 minutes. Or the short loop through the first gates, about 45 minutes. Golden light late afternoon. Open 24 hours.'),
 R('16:15', 'Keihan to Kiyomizu-Gojō, then up the hill', 'Keihan Fushimi-Inari station is 3 minutes from the shrine gate. Local train (普通) toward 出町柳, 3 stops to Kiyomizu-Gojō. Then a taxi up, about 5 minutes, or 20 minutes on foot up Gojōzaka. Or a taxi straight from Inari, about 15 minutes, about ¥2,000.'),
]
_kiyo = [
 R('16:45', 'Kiyomizu-dera', 'The wooden stage over the trees at sunset (about 17:10). Open to 18:00. About ¥500 each.'),
 R('17:30', 'Down through Sannenzaka and Ninenzaka', 'Downhill from Kiyomizu, the old stone lanes. Shops start closing about 18:00.'),
 R('17:50', 'Yasaka Pagoda at dusk', 'Two minutes off Ninenzaka. The five storey pagoda above the lane roofs.'),
 R('18:10', 'Yasaka shrine, then down into Gion', 'Lanterns lit. Then Hanamikoji and the Shirakawa canal.'),
 R('19:00', 'Chao Chao gyoza, Sanjō Kiyamachi', 'About 15 minutes north from Gion over Shijō Bridge. Kyoto\'s famous crispy dumplings, small shop, short queue.'),
 R('20:00', 'Pontochō alley', 'The lantern lane of small bars and izakayas by the river. Wander and pick one for a drink.'),
 R('20:45', 'Optional: Menami', 'Kyoto home-style small plates at a counter, since 1939. On Kiyamachi, back near Chao Chao. Taxi home after, about 10 minutes.'),
]
D[23]['rows'] += _kiyo
D[23]['rows'].sort(key=lambda x: x[0])
D[23]['notes'] = [
 ('Running late', 'Drop the hotel stop first, then shorten Inari to the first gates. Protect Kiyomizu by 17:30 (closes 18:00).'),
 ('Getting around', 'Taxis for the long cross-town legs: Arashiyama to Kinkaku-ji to Nijō. Trains for Inari and Kiyomizu.'),
 ('Autumn colour', "Late October is green and early gold, not red. Kyoto's maples turn mid to late November.")]
D[24]['title'] = 'Slow Kyoto morning, back to Tokyo, fireworks night'
D[24]['cal'] = 'Fireworks'
D[24]['sum'] = 'A sleep in, packing and a slow breakfast while it rains, the train back to Tokyo, an hour at the hotel, then fireworks over the bay from Odaiba. Dinner comes after the show, so the trains have cleared by the time you leave.'
D[24]['foot'] = 'Rain most of the morning, light (1 to 2 mm an hour), clearing mid-afternoon. Taxi with the bags. Work back from the 12:01: on the platform by 11:45, at the station by 11:15, check out about 10:45.'
_aft = [x for x in D[24]['rows'] if x[0] >= '11:15']
D[24]['rows'] = [
 R('08:30', 'Sleep in, pack', 'No alarm. Most of the packing before breakfast so the morning stays slow.'),
 R('09:00', 'Slow breakfast: pick one', 'Inoda Coffee main shop (Kyoto\'s classic coffee house, the Kyoto breakfast set, from 07:00, taxi about 10 minutes). Smart Coffee (1930s café, pancakes and French toast, from 08:00, Teramachi arcade). Kyosaimi Nomura (obanzai breakfast set, from 07:00, 10 minutes\' walk up Karasuma). Breakfast Udon Express (light udon, 07:00 to 10:00 only, near Shijō-Karasuma).'),
 R('10:15', 'Back to the hotel, finish packing', ''),
 R('10:45', 'Check out, taxi to Kyoto Station', 'About 5 minutes with the bags in the rain. Walking is 15 minutes in the dry (How-to 16).'),
] + _aft

# Thu 22 22:47: Fri 23 lightened (about 7 to 7.5 km): bamboo one way into Tenryū-ji, no Nijō (optional Sat morning), lunch near the hotel, a long hotel rest, Inari short loop only, taxi Inari to Kiyomizu, no Yasaka shrine, taxi Gion to Chao Chao. Start 07:30 after the late night.
D[23]['title'] = 'Kyoto: bamboo grove, Golden Pavilion, Inari, Higashiyama'
D[23]['cal'] = 'Bamboo, Inari, Gion'
D[23]['sum'] = 'An easier day, about 7 km: the bamboo grove and Tenryū-ji early, the Golden Pavilion, lunch and a long rest at the hotel, a short loop at Fushimi Inari, then Kiyomizu-dera at sunset, Gion, gyoza and Pontochō. Taxis do the hills.'
D[23]['foot'] = 'Dry by day, up to about 21°C. Light rain from about 21:00: umbrella for Pontochō. About 7 km, roughly 10,000 steps.'
D[23]['rows'] = [
 R('07:30', 'Taxi to the bamboo grove', 'About 25 minutes, about ¥3,500. Show the driver 嵐山 竹林の小径、野宮神社 (Arashiyama bamboo grove, Nonomiya Shrine). Leave at 07:00 if you are up for a quieter grove.'),
 R('08:00', 'Bamboo grove, one way', 'From Nonomiya Shrine along the bamboo path to Tenryū-ji\'s north gate, the best stretch, flat. Take your time for photos. Add-on: carry on up to the Ōkōchi Sansō gate and back, about 15 minutes, gently uphill.'),
 R('08:30', 'Tenryū-ji garden', 'Opens 08:30. In by the north gate on the bamboo path. Flat pond garden with the hills behind, about 40 minutes. About ¥500 each.'),
 R('09:15', 'Togetsukyō bridge and % Arabica', 'Out of Tenryū-ji\'s main gate, 5 minutes to the river. Coffee to take away (opens 09:00), on the riverbank looking at the bridge.'),
 R('09:45', 'Taxi to Kinkaku-ji', 'From the main street by Togetsukyō, about 20 minutes, about ¥2,500. Show 金閣寺.'),
 R('10:05', 'Kinkaku-ji, the Golden Pavilion', 'The gold pavilion on its pond. One-way garden loop, gentle, about 45 minutes. Open 09:00 to 17:00. About ¥500 each.'),
 R('11:00', 'Taxi to lunch', 'About 20 minutes to the centre. See the lunch options.'),
 R('11:30', 'Lunch: pick one', 'Near the hotel: Kyosaimi Nomura (obanzai, a dozen Kyoto home-style small dishes, to 14:00) or Ichiran Kyoto Karasuma (ramen in a booth, to 22:00). At Kyoto Station: Katsugyu Yodobashi (beef cutlet on a hot stone, to 23:00). Or on the way, near Nijō: Soba Tatsuichi (hand-made and duck soba, to 16:00) or Sarashina (tiny family soba and curry udon, cash only).'),
 R('12:30', 'Hotel, feet up', 'A proper rest, about two hours. Change for the evening.'),
 R('14:45', 'JR Nara line to Inari', 'Subway one stop to Kyoto, then the JR Nara line (奈良線), two stops, about 5 minutes. Or a taxi from the hotel, about 15 minutes, about ¥2,000. The shrine gate faces the platform.'),
 R('15:00', 'Fushimi Inari, short loop', 'Through the main shrine into the Senbon Torii, the thousand gates, up to the Okusha Hōhaisho and back, about 45 minutes. Keep climbing a little past it for quieter gates. Open 24 hours.'),
 R('16:00', 'Taxi to Kiyomizu-dera', 'From the road in front of the shrine gate, about 15 minutes, about ¥2,000. Show 清水寺. Saves the hill.'),
 R('16:20', 'Kiyomizu-dera', 'The wooden stage over the trees, stay for sunset (about 17:10). Open to 18:00. About ¥500 each.'),
 R('17:30', 'Down through Sannenzaka and Ninenzaka', 'Downhill all the way, the old stone lanes. Shops start closing about 18:00.'),
 R('17:50', 'Yasaka Pagoda at dusk', 'Two minutes off Ninenzaka. The five storey pagoda above the lane roofs.'),
 R('18:10', 'Hanamikoji and Gion', 'From the pagoda down to Hanamikoji, the old teahouse lane, lanterns lit. Yasaka Shrine is skipped to save the legs.'),
 R('18:45', 'Taxi to Chao Chao', 'From Shijō-dōri, about 5 minutes. Show 餃子 ChaoChao 三条木屋町.'),
 R('19:00', 'Chao Chao gyoza, Sanjō Kiyamachi', 'Kyoto\'s famous crispy dumplings, small shop, short queue.'),
 R('20:00', 'Pontochō alley', 'The lantern lane of small bars and izakayas by the river, a two minute walk. Wander and pick one for a drink.'),
 R('20:45', 'Optional: Menami', 'Kyoto home-style small plates at a counter, since 1939. On Kiyamachi, near Chao Chao. Taxi home after, about 10 minutes.'),
]
D[23]['notes'] = [
 ('Steps', 'About 7 km, roughly 10,000 steps. Add-ons if the legs are good: the bamboo path up to Ōkōchi Sansō (about 800 steps), Yasaka Shrine at dusk (about 1,000 steps).'),
 ('Running late', 'Shorten the hotel rest. Protect Kiyomizu by 17:30 (closes 18:00).'),
 ('Autumn colour', "Late October is green and early gold, not red. Kyoto's maples turn mid to late November.")]
_aft = [x for x in D[24]['rows'] if x[0] >= '11:15']
D[24]['rows'] = [
 R('08:00', 'Sleep in, pack', 'No alarm. Most of the packing before breakfast so the morning stays slow.'),
 R('08:30', 'Optional: Nijō Castle, palace only', 'Only if you want it. Taxi about 10 minutes, show 二条城 東大手門. Opens 08:45. In through the east gate, the Ninomaru Palace with its nightingale floors (shoes off, indoors, good in the rain), straight back out. About 45 minutes, flat. About ¥1,300 each. Then breakfast at Inoda, 10 minutes by taxi.'),
 R('09:00', 'Slow breakfast: pick one', 'Inoda Coffee main shop (Kyoto\'s classic coffee house, the Kyoto breakfast set, from 07:00). Smart Coffee (1930s café, pancakes and French toast, from 08:00, covered arcade). Kyosaimi Nomura (obanzai breakfast set, from 07:00, 10 minutes\' walk up Karasuma). Breakfast Udon Express (light udon, 07:00 to 10:00 only). With Nijō, breakfast is about 09:45.'),
 R('10:15', 'Back to the hotel, finish packing', ''),
 R('10:45', 'Check out, taxi to Kyoto Station', 'About 5 minutes with the bags in the rain. Walking is 15 minutes in the dry (How-to 16).'),
] + _aft

# Thu 22 23:18: the Big 5 starred: bamboo grove, Golden Pavilion, Fushimi Inari, Kiyomizu-dera, Yasaka Pagoda.
_BIG5 = ('Bamboo grove', 'Kinkaku-ji', 'Fushimi Inari', 'Kiyomizu-dera', 'Yasaka Pagoda')
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith(_BIG5):
        D[23]['rows'][_i] = R(_x[0], '★ ' + _x[1], *_x[2:])
D[23]['notes'] = [('The Big 5 (★)', 'The bamboo grove, the Golden Pavilion, Fushimi Inari, Kiyomizu-dera and the Yasaka Pagoda. Protect these; everything else can bend.')] + D[23]['notes']
D[23]['sum'] = 'The Big 5 in one easier day, about 7 km: the bamboo grove early, the Golden Pavilion, lunch and a long rest, Fushimi Inari, then Kiyomizu-dera at sunset and the Yasaka Pagoda at dusk. Gion, gyoza and Pontochō to finish.'

# Fri 23 07:43: leaving the hotel at 08:00. Morning shifted about 30 minutes; rest is shorter, afternoon unchanged.
def _set23(title_start, t, txt=None):
    for _i, _x in enumerate(D[23]['rows']):
        if _x[1].startswith(title_start):
            D[23]['rows'][_i] = R(t, _x[1], txt if txt is not None else _x[2], *_x[3:]); return
_set23('Taxi to the bamboo grove', '08:00', 'About 25 minutes, about ¥3,500. Show the driver 嵐山 竹林の小径、野宮神社 (Arashiyama bamboo grove, Nonomiya Shrine). Or the JR Sagano line from Kyoto to Saga-Arashiyama, about 40 minutes door to door, about ¥450 for two.')
_set23('★ Bamboo grove', '08:25')
_set23('Tenryū-ji garden', '08:55')
_set23('Togetsukyō bridge', '09:40')
_set23('Taxi to Kinkaku-ji', '10:05')
_set23('★ Kinkaku-ji', '10:25')
_set23('Taxi to lunch', '11:15')
_set23('Lunch: pick one', '11:45')
_set23('Hotel, feet up', '12:45', 'A rest, about two hours. Change for the evening.')
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 09:54: Inari straight after Kinkaku-ji, then Ichiran, then the hotel to rest and pack rain gear, then Kiyomizu and walk down to dinner.
_drop = ('Taxi to lunch', 'Lunch: pick one', 'Hotel, feet up', 'JR Nara line to Inari', '★ Fushimi Inari', 'Taxi to Kiyomizu-dera', '★ Kiyomizu-dera', 'Taxi to Chao Chao')
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith(_drop)]
D[23]['rows'] += [
 R('11:15', 'Taxi to Kyoto Station', 'From the Kinkaku-ji taxi rank, about 25 minutes, about ¥3,000. Show 京都駅 八条口 or 京都駅 烏丸口. A taxi straight to Inari is about ¥5,000 and saves about 15 minutes.'),
 R('11:45', 'JR Nara line to Inari', 'JR Nara line (奈良線), any train, two stops, about 5 minutes. All on Suica. The shrine gate faces the platform.'),
 R('12:00', '★ Fushimi Inari, short loop', 'Through the main shrine into the Senbon Torii, the thousand gates, up to the Okusha Hōhaisho and back, about 45 minutes. Busiest at the bottom at midday, quieter as you climb. Snack on the approach street: inari sushi, yakitori, taiyaki.'),
 R('13:00', 'JR back to Kyoto, subway to Shijō', 'JR Nara line two stops to Kyoto, then the Karasuma subway two stops north to Shijō (四条). All on Suica.'),
 R('13:30', 'Lunch: Ichiran Kyoto Karasuma', 'Rich pork-bone ramen in your own booth. Ticket machine at the door, then fill in the order sheet. Open 10:00 to 22:00.'),
 R('14:15', 'Hotel: rest, freshen up, pack rain gear', 'Ten minutes on foot down Karasuma-dōri, or one subway stop to Gojō. Umbrellas or raincoats for the evening: light rain likely from about 21:00.'),
 R('15:45', 'Taxi to Kiyomizu-dera', 'From the hotel, about 10 minutes, about ¥1,500. Show 清水寺. Drops at the top, so the rest of the day is downhill.'),
 R('16:00', '★ Kiyomizu-dera', 'The wooden stage over the trees, stay for sunset (about 17:10). Open to 18:00. About ¥500 each.'),
 R('18:40', 'Walk to Chao Chao', 'From Gion west along Shijō-dōri over Shijō Bridge, then right up Kiyamachi-dōri by the little canal. About 15 minutes, flat.'),
]
D[23]['rows'].sort(key=lambda x: x[0])
D[23]['notes'] = [n for n in D[23]['notes'] if n[0] != 'Running late'] + [('Running late', 'Shorten the hotel rest. Protect Kiyomizu by 17:30 (closes 18:00).')]

# Fri 23 10:28: Kinkaku-ji done early (very busy, rushed). To Kyoto Station now, coffee and a bite there, then Inari. Afternoon pulled earlier.
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith('★ Kinkaku-ji'):
        D[23]['rows'][_i] = R('10:05', _x[1], _x[2] + ' Note: very busy, rushed through it. Not really worth it.', DN)
    if _x[1].startswith('Taxi to Kinkaku-ji'):
        D[23]['rows'][_i] = R(_x[0], _x[1], _x[2], DN)
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith('Taxi to Kyoto Station')]
D[23]['rows'] += [
 R('10:30', 'Bus or taxi to Kyoto Station', 'Bus 205 from the Kinkakuji-michi stop (金閣寺道), 5 minutes\' walk from the gate, toward 京都駅, about 40 minutes, about ¥230 each on Suica. Or a taxi from the Kinkaku-ji rank, about 25 minutes, about ¥3,000.'),
 R('11:10', 'Coffee and a bite at Kyoto Station', 'Plenty in the station and Porta underground. Keep it light, Ichiran is lunch.'),
]
_set23('JR Nara line to Inari', '11:35')
_set23('★ Fushimi Inari', '11:45')
_set23('JR back to Kyoto', '12:45')
_set23('Lunch: Ichiran', '13:15')
_set23('Hotel: rest', '14:00')
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 11:50: arrived at Fushimi Inari.
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith(('Bus or taxi to Kyoto Station', 'Coffee and a bite at Kyoto Station', 'JR Nara line to Inari')):
        D[23]['rows'][_i] = R(_x[0], _x[1], _x[2], DN)
_set23('★ Fushimi Inari', '11:50')
_set23('JR back to Kyoto', '12:50')
_set23('Lunch: Ichiran', '13:20')
_set23('Hotel: rest', '14:05')
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 12:12: leaving Inari. Hotel first to put the washing on, then walk to Ichiran.
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith('★ Fushimi Inari'):
        D[23]['rows'][_i] = R(_x[0], _x[1], _x[2], DN)
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith(('JR back to Kyoto', 'Hotel: rest'))]
D[23]['rows'] += [
 R('12:20', 'JR to Kyoto, subway to Gojō', 'JR Nara line two stops to Kyoto, then the Karasuma subway one stop north to Gojō (五条). All on Suica.'),
 R('12:45', 'Hotel: washing on', 'Quick stop.'),
 R('13:50', 'Hotel: rest, freshen up, pack rain gear', 'Ten minutes back down Karasuma-dōri from Ichiran. Washing out. Umbrellas or raincoats for the evening: light rain likely from about 21:00.'),
]
_set23('Lunch: Ichiran', '13:00', 'Ten minutes on foot north up Karasuma-dōri from the hotel. Rich pork-bone ramen in your own booth. Ticket machine at the door, then fill in the order sheet. Open 10:00 to 22:00.')
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 12:22: straight to Ichiran from Inari, then the hotel.
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith(('JR to Kyoto, subway to Gojō', 'Hotel: washing on', 'Hotel: rest'))]
D[23]['rows'] += [
 R('12:25', 'JR back to Kyoto, subway to Shijō', 'JR Nara line two stops to Kyoto, then the Karasuma subway two stops north to Shijō (四条). All on Suica.'),
 R('13:40', 'Hotel: washing on, rest, pack rain gear', 'Ten minutes on foot down Karasuma-dōri from Ichiran. Umbrellas or raincoats for the evening: light rain likely from about 21:00.'),
]
_set23('Lunch: Ichiran', '12:50', 'A minute from Shijō station on Karasuma-dōri. Rich pork-bone ramen in your own booth. Ticket machine at the door, then fill in the order sheet. Open 10:00 to 22:00.')
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 16:25: G's note for Kiyomizu-dera.
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith('★ Kiyomizu-dera'):
        D[23]['rows'][_i] = R(_x[0], _x[1], _x[2] + ' Note: if it is busy, don\'t go in. Take the loop down the driveway for a quiet, peaceful walk back down.', *_x[3:])

# Fri 23 17:44: Higashiyama done. Chao Chao and Menami dropped; chicken katsu curry and beer at Katsuda near the hotel instead.
for _i, _x in enumerate(D[23]['rows']):
    if _x[1].startswith(('★ Kiyomizu-dera', 'Taxi to Kiyomizu-dera', 'Down through Sannenzaka', '★ Yasaka Pagoda', 'Hanamikoji and Gion', 'Pontochō alley', 'Lunch: Ichiran', 'JR back to Kyoto', 'Hotel: washing on')):
        D[23]['rows'][_i] = R(_x[0], _x[1], _x[2], DN)
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith(('Walk to Chao Chao', 'Chao Chao', 'Optional: Menami'))]
D[23]['rows'] += [
 R('17:50', 'Hankyu from Kyoto-Kawaramachi to Karasuma', 'Kyoto-Kawaramachi station is at the Shijō end of Pontochō. Hankyu line one stop to 烏丸 (Karasuma), about 2 minutes, on Suica.'),
 R('18:00', 'Dinner: Kyoto Tonkatsu Katsuda, Shijō-Karasuma', 'Chicken katsu curry and a beer. Katsu fried to order at the counter, curry sauce, unlimited rice. Try the chicken with cheese, or the matcha beer. Open to 22:00, short queue likely.'),
 R('19:15', 'Walk back to the hotel', 'About 6 minutes south down Karasuma-dōri.'),
]
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 17:49: taxi to Katsuda instead of the Hankyu.
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith('Hankyu from Kyoto-Kawaramachi')]
D[23]['rows'].append(R('17:50', 'Taxi to Katsuda', 'From Shijō-dōri, about 5 to 10 minutes, about ¥1,000. Show 京都とんかつ かつ田 四条烏丸店.'))
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 19:38: FamilyMart katsu curry in the end, back at the hotel, coin laundry and a quiet night.
D[23]['rows'] = [x for x in D[23]['rows'] if not x[1].startswith(('Taxi to Katsuda', 'Dinner: Kyoto Tonkatsu Katsuda', 'Walk back to the hotel'))]
D[23]['rows'] += [
 R('18:00', 'Back to the hotel, FamilyMart katsu curry', '', DN),
 R('19:30', 'Coin laundry and a quiet night in', '', DN),
]
D[23]['rows'].sort(key=lambda x: x[0])

# Fri 23 19:40: Sun 25 gets the Imperial Palace gardens and Kappabashi (Sunday-open shops only), then Ginza car-free and the stores when the rain comes. Mon 26: teamLab, the Asakusa sumo show at 12:00 with chanko lunch, Sensō-ji, dinner under the train tracks.
D[25]['title'] = 'Palace gardens, Kappabashi, then Ginza car-free'
D[25]['sum'] = 'The Imperial Palace East Gardens first thing, Kappabashi kitchen street for knives and ceramics, then back to Ginza for the car-free afternoon and into the department stores when the rain comes.'
_keep = [x for x in D[25]['rows'] if x[1].startswith(('Slow breakfast', 'Imperial Palace East Gardens')) or x[0] in ('Afternoon', 'Late arvo', 'Evening', '19:30', 'When done')]
D[25]['rows'] = _keep + [
 R('10:45', 'Tokyo Station, then JR to Ueno and the Ginza line to Tawaramachi', 'The red brick Marunouchi façade on the way out of the gardens. JR Yamanote or Keihin-Tōhoku line to Ueno, about 7 minutes, then the Ginza line two stops to Tawaramachi (田原町). Or a taxi from the gardens, about 20 minutes, about ¥2,500.'),
 R('11:30', 'Kappabashi kitchenware street', 'Sunday: many shops are shut, so go for the ones that open. Knives: Kama-asa (11:00 to 17:30, free engraving) and Kamata Hakensha (10:00 to 18:00). Ceramics: Dengama (10:00 to 18:00, upstairs closes about 15:00). Fake food: Ganso food samples (10:00 to 17:30). Niimi is closed Sundays, but its giant chef head is on the roof at the south end.'),
 R('13:00', 'Lunch in Asakusa', 'Ten minutes east on foot. Keep it casual.'),
 R('14:00', 'Ginza line from Asakusa to Ginza', 'Direct, about 18 minutes. Out at Ginza onto Chūō-dōri.'),
 R('14:30', 'Ginza car-free', 'Chūō-dōri is pedestrian only until 17:00. Walk it while it is dry, then into the stores when the rain arrives.'),
]
D[25]['rows'].sort(key=lambda x: (x[0][0].isdigit() is False, x[0]) if x[0] not in ('Afternoon','Late arvo','Evening','When done') else (False, {'Afternoon':'15:00','Late arvo':'16:30','Evening':'18:00','When done':'23:00'}[x[0]]))
D[25]['foot'] = 'Rain expected in the afternoon: the gardens and Kappabashi in the dry, then the department stores. Browse before about 20:00 and eat after. Many smaller Ginza bars and restaurants close on Sundays.'
D[26]['title'] = 'teamLab, sumo show in Asakusa, dinner under the tracks'
D[26]['sum'] = 'teamLab Borderless first thing, a sumo show with chanko hotpot lunch in Asakusa, Sensō-ji and the Skytree at dusk, then yakitori and beer in the lanes under the train tracks.'
_r = [x for x in D[26]['rows'] if not x[1].startswith(('Sky Room Café', 'Hibiya line, then Ginza line', 'Kappabashi', 'Shimbashi, no booking'))]
D[26]['rows'] = _r + [
 R('10:45', 'Hibiya line, then the Ginza line to Asakusa', 'From Kamiyachō, Hibiya line to Ginza, change to the Ginza line to Asakusa (浅草), about 35 minutes.'),
 R('12:00', 'Asakusa Sumo Club: show and chanko lunch', 'About two hours. Former wrestlers explain and demonstrate sumo, with audience try-outs, and an all-you-can-eat chanko hotpot (the wrestlers\' stew) and a drink. About ¥16,000 each. Beside Don Quijote Asakusa. Sessions 12:00, 15:00, 18:00, 20:30.', TB),
 R('19:00', 'Dinner under the train tracks, Yūrakuchō', 'The Gādo-shita lanes under the JR tracks between Yūrakuchō and Shimbashi, five minutes from the hotel. Yakitori, beer, the trains rumbling overhead. No booking; wander and pick one. Shimbashi\'s lanes are the overflow.'),
]
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))
for _i, _x in enumerate(D[26]['rows']):
    if _x[1].startswith('Sensō-ji'):
        D[26]['rows'][_i] = R('14:15', _x[1], 'A few minutes from the sumo club. Kaminarimon gate, Nakamise street, the main hall. If Nakamise is jammed, take the side lanes.', *_x[3:])
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))

# Sat 24 18:05: Kappabashi is mostly shut on Sundays, so it goes back to Mon 26. The sumo show moves to Sun 25 at 12:00 (G to book).
D[25]['title'] = 'Palace gardens, sumo show, then Ginza car-free'
D[25]['sum'] = 'The Imperial Palace East Gardens first thing, a sumo show with chanko hotpot lunch in Asakusa, then back to Ginza for the car-free afternoon and into the department stores when the rain comes.'
D[25]['rows'] = [x for x in D[25]['rows'] if not x[1].startswith(('Tokyo Station, then JR to Ueno', 'Kappabashi', 'Lunch in Asakusa', 'Ginza line from Asakusa', 'Ginza car-free'))] + [
 R('11:00', 'Gardens to Asakusa', 'From the Ōtemon gate, walk to Tokyo Station, JR one stop to Kanda (神田), then the Ginza line to Asakusa (浅草), about 30 minutes. Or a taxi from the gardens, about 20 minutes, about ¥2,500.'),
 R('12:00', 'Asakusa Sumo Club: show and chanko lunch', 'About two hours. Former wrestlers explain and demonstrate sumo, with audience try-outs, and an all-you-can-eat chanko hotpot (the wrestlers\' stew) and a drink. About ¥16,000 each. Beside Don Quijote Asakusa. Sessions 12:00, 15:00, 18:00, 20:30.', TB),
 R('14:15', 'Ginza line from Asakusa to Ginza', 'Direct, about 18 minutes. Out at Ginza onto Chūō-dōri.'),
 R('14:45', 'Ginza car-free', 'Chūō-dōri is pedestrian only until 17:00. Walk it while it is dry, then into the stores when the rain arrives.'),
]
D[25]['rows'].sort(key=lambda x: (False, x[0]) if x[0][0].isdigit() else (False, {'Afternoon':'15:00','Late arvo':'16:30','Evening':'18:00','When done':'23:00'}.get(x[0], '23:30')))
D[25]['foot'] = 'Rain expected in the afternoon: the gardens in the dry, the sumo show indoors, then the department stores. Browse before about 20:00 and eat after. Many smaller Ginza bars and restaurants close on Sundays.'
D[26]['title'] = 'teamLab, Kappabashi and Asakusa, dinner under the tracks'
D[26]['sum'] = 'teamLab Borderless first thing, Kappabashi kitchen street while the shops are open, lunch in Asakusa, Sensō-ji and the Skytree at dusk, then yakitori and beer in the lanes under the train tracks.'
D[26]['rows'] = [x for x in D[26]['rows'] if not x[1].startswith(('Hibiya line, then the Ginza line', 'Asakusa Sumo Club'))] + [
 R('10:45', 'Hibiya line, then the Ginza line to Tawaramachi', 'From Kamiyachō, Hibiya line to Ginza, change to the Ginza line to Tawaramachi (田原町), about 30 minutes.'),
 R('11:15', 'Kappabashi kitchenware street', 'Weekday, so the shops are open, most until about 17:00. Knives: Kama-asa (free engraving) and Kamata Hakensha. Ceramics: Dengama. Fake food: Ganso food samples. Niimi\'s giant chef head at the south end. Knives fly in checked bags only.'),
 R('13:00', 'Lunch in Asakusa', 'Ten minutes east on foot. Keep it casual.'),
]
for _i, _x in enumerate(D[26]['rows']):
    if _x[1].startswith('Sensō-ji'):
        D[26]['rows'][_i] = R('14:15', _x[1], 'A few minutes from lunch. Kaminarimon gate, Nakamise street, the main hall. If Nakamise is jammed, take the side lanes.', *_x[3:])
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))

# Sat 24 23:16: actual. Slow morning, Nijō and breakfast out skipped, the fireworks night as planned. AirPod left on the train, posted to the Blossom.
D[24]['sum'] = 'What happened. A sleep in and packing instead of Nijō and a breakfast out, the Nozomi back to Tokyo, then the fireworks and buffet at the Hilton Odaiba as planned.'
D[24]['rows'] = [r for r in D[24]['rows'] if not r[1].startswith(('Optional: Nijō Castle', 'Slow breakfast', 'Back to the hotel, finish packing'))]
for _i, _x in enumerate(D[24]['rows']):
    _n = _x[2]
    if _x[1].startswith('Nozomi 16'): _n = 'Lost one AirPod on the train. The hotel is posting it to the Blossom, due Sunday.'
    if _x[1].startswith('Yurikamome back to Shimbashi'): _n = 'Pizza near the hotel on the way back.'
    D[24]['rows'][_i] = R(_x[0], _x[1], _n, DN)

# Sun 25 08:05: sumo moves to Mon 26 at 17:00, Shibuya Sumo Club at Yoyogi (G to book). Sun 25: gardens, Ginza car-free, massages, bites in Ginza. Mon 26: teamLab, Sky Room coffee by Tokyo Tower, free afternoon, sumo, dinner under the tracks.
D[25]['title'] = 'Palace gardens, Ginza car-free, massages'
D[25]['sum'] = 'The Imperial Palace East Gardens first thing, then Ginza car-free from noon, the department stores and rooftops, massages, and bites around Ginza at night.'
D[25]['rows'] = [x for x in D[25]['rows'] if not x[1].startswith(('Gardens to Asakusa', 'Asakusa Sumo Club', 'Ginza line from Asakusa', 'Ginza car-free', 'Eat in the complexes', 'Optional: Tokyo Tower'))] + [
 R('08:15', 'AirPod at the front desk', 'The Kyoto hotel posted it, due today. Ask: 京都のホテルから荷物が届いていますか？ (Has a parcel arrived from the Kyoto hotel?)'),
 R('11:15', 'Walk to Ginza, early lunch', 'From the Ōtemon gate, about 20 minutes south, past Tokyo Station\'s red brick front and through Marunouchi. Keep lunch light.'),
 R('12:00', 'Ginza car-free', 'Chūō-dōri is pedestrian only from 12:00 to 17:00 on Sundays. Walk it while it is dry, then into the stores when the rain arrives.'),
 R('17:00', 'Massages', 'Book ahead or walk in. Body and foot: Buasai Ginza (Thai, Ginza 8-chōme, 5 minutes from the hotel, to midnight) or YURAGI (Ginza 7-chōme, from 13:00). Head spa: Head Spa ZEN (Ginza 2-chōme, to 23:00).', TB),
 R('Evening', 'Bites around Ginza', 'Graze rather than sit down: the department store food halls (depachika) before about 20:00, then yakitori or ramen around Yūrakuchō and the Ginza side streets. Many smaller places close on Sundays.'),
]
D[25]['rows'].sort(key=lambda x: (False, x[0]) if x[0][0].isdigit() else (False, {'Afternoon':'13:00','Late arvo':'15:30','Evening':'18:30','When done':'23:00'}.get(x[0], '23:30')))
D[25]['foot'] = 'Rain expected in the afternoon: the gardens in the dry, Ginza car-free early, then the department stores and the massages.'
D[26]['title'] = 'teamLab, coffee by Tokyo Tower, sumo show, dinner under the tracks'
D[26]['sum'] = 'teamLab Borderless first thing, coffee beside Tokyo Tower, a free afternoon, then the Shibuya Sumo Club show at 17:00 and yakitori under the train tracks.'
D[26]['rows'] = [x for x in D[26]['rows'] if x[1].startswith(('Leave the Blossom', 'teamLab Borderless', 'Back to the hotel'))] + [
 R('10:45', 'Sky Room Café & Bar, Mori JP Tower 34F', 'Coffee with Tokyo Tower right alongside. Open 09:00 to 21:00, no bookings. Same building complex as teamLab.'),
 R('11:45', 'Optional: Tokyo Tower and Zōjō-ji', 'About 10 minutes\' walk. The temple gate with the tower behind it.'),
 R('12:30', 'Free afternoon', 'Hotel rest, the Ginza stores, or Kappabashi if you still want knives or ceramics (Monday is the last weekday: Ginza line to Tawaramachi, back by 15:45).'),
 R('16:00', 'Ōedo line from Shiodome to Yoyogi', 'Ten minutes\' walk from the hotel to Shiodome (汐留), Toei Ōedo line toward 六本木・都庁前, direct to 代々木 (Yoyogi), about 20 minutes. Aim to arrive by 16:40.'),
 R('17:00', 'Shibuya Sumo Club: sumo show', 'About 90 minutes. Live bouts, English MC, Q&A, a chance to challenge a wrestler (lottery), photos with the wrestlers, one drink. Daiichi Silver Building B1F, Yoyogi Broadway, 1 minute from JR Yoyogi east exit. About AU$62 each on Klook.', TB),
 R('18:40', 'Ōedo line back to Shiodome', 'From Yoyogi, toward 六本木・大門, direct to 汐留 (Shiodome), about 20 minutes. Then 10 minutes\' walk to the lanes.'),
 R('19:15', 'Dinner under the train tracks, Yūrakuchō', 'The Gādo-shita lanes under the JR tracks between Yūrakuchō and Shimbashi, five minutes from the hotel. Yakitori, beer, the trains rumbling overhead. No booking; wander and pick one.'),
]
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))

# Sun 25 08:06: Kappabashi definitely in on Mon 26, between the Sky Room coffee and the sumo.
D[26]['title'] = 'teamLab, Tokyo Tower coffee, Kappabashi, sumo show, dinner under the tracks'
D[26]['sum'] = 'teamLab Borderless first thing, coffee beside Tokyo Tower, Kappabashi kitchen street while the shops are open, a drop-off at the hotel, then the Shibuya Sumo Club show at 17:00 and yakitori under the train tracks.'
D[26]['rows'] = [x for x in D[26]['rows'] if not x[1].startswith(('Optional: Tokyo Tower', 'Free afternoon', 'Sky Room Café'))] + [
 R('10:45', 'Sky Room Café & Bar, Mori JP Tower 34F', 'Coffee with Tokyo Tower right alongside. Open 09:00 to 21:00, no bookings. Keep it to about 40 minutes.'),
 R('11:30', 'Hibiya line, then the Ginza line to Tawaramachi', 'From Kamiyachō, Hibiya line to Ginza, change to the Ginza line to Tawaramachi (田原町), about 30 minutes.'),
 R('12:00', 'Kappabashi kitchenware street', 'Weekday, so the shops are open. Knives: Kama-asa (free engraving) and Kamata Hakensha. Ceramics: Dengama. Fake food: Ganso food samples. Niimi\'s giant chef head at the south end. Knives fly in checked bags only.'),
 R('13:30', 'Lunch near Kappabashi or Asakusa', 'Keep it casual. Sensō-ji\'s Kaminarimon gate is 10 minutes east if you want a quick look.'),
 R('14:45', 'Ginza line back, drop the shopping at the hotel', 'Tawaramachi to Ginza, about 15 minutes, then a 10 minute walk. Rest until 16:00.'),
]
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))

# Sun 25 08:13: the sumo moves to the 12:00 show on Mon 26. Kappabashi after it, Sensō-ji at dusk, evening free for dinner under the tracks.
D[26]['title'] = 'teamLab, sumo show, Kappabashi, Sensō-ji at dusk, dinner under the tracks'
D[26]['sum'] = 'teamLab Borderless first thing, a quick coffee beside Tokyo Tower, the Shibuya Sumo Club show at noon, Kappabashi kitchen street in the afternoon, Sensō-ji as the lights come on, then yakitori under the train tracks.'
D[26]['rows'] = [x for x in D[26]['rows'] if x[1].startswith(('Leave the Blossom', 'teamLab Borderless', 'Back to the hotel', 'Sky Room Café', 'Dinner under the train tracks'))]
for _i, _x in enumerate(D[26]['rows']):
    if _x[1].startswith('Sky Room Café'):
        D[26]['rows'][_i] = R('10:40', _x[1], 'Coffee with Tokyo Tower right alongside. Open 09:00 to 21:00, no bookings. Quick one: leave by 11:15.')
D[26]['rows'] += [
 R('11:15', 'Ōedo line from Azabu-Jūban to Yoyogi', 'About 10 minutes\' walk to Azabu-Jūban (麻布十番), Toei Ōedo line toward 六本木・都庁前, direct to 代々木 (Yoyogi), about 12 minutes. Aim to arrive by 11:45.'),
 R('12:00', 'Shibuya Sumo Club: sumo show', 'About 90 minutes. Live bouts, English MC, Q&A, a chance to challenge a wrestler (lottery), photos with the wrestlers, one drink. Daiichi Silver Building B1F, Yoyogi Broadway, 1 minute from JR Yoyogi east exit. About AU$62 each on Klook.', TB),
 R('13:30', 'Quick lunch near Yoyogi', 'Something fast by the station so Kappabashi gets the time. Or eat at Kappabashi or Asakusa.'),
 R('14:00', 'Ōedo line, then the Ginza line to Tawaramachi', 'Ōedo line from Yoyogi to Aoyama-itchōme (青山一丁目), 3 stops, change to the Ginza line toward 浅草 to Tawaramachi (田原町). About 40 minutes.'),
 R('14:45', 'Kappabashi kitchenware street', 'Weekday, so the shops are open, most until about 17:00 to 17:30. Knives: Kama-asa (free engraving) and Kamata Hakensha. Ceramics: Dengama. Fake food: Ganso food samples. Niimi\'s giant chef head at the south end. Knives fly in checked bags only.'),
 R('17:00', 'Sensō-ji at dusk', 'Ten minutes east. Kaminarimon gate, Nakamise street and the main hall lit up after sunset, crowds thinning. The free terrace on 8F of the tourist centre opposite Kaminarimon for the Skytree.'),
 R('18:15', 'Ginza line back, drop the shopping at the hotel', 'Asakusa to Ginza, about 18 minutes, then a 10 minute walk.'),
]
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))

# Sun 25 08:20: sumo today instead. Shinjuku Sumo Club main venue, 17:30. Mon 26 back to teamLab, Tokyo Tower coffee, Kappabashi, Sensō-ji and the Skytree at dusk.
D[25]['title'] = 'Palace gardens, Ginza car-free, sumo in Shinjuku'
D[25]['sum'] = 'The Imperial Palace East Gardens first thing, Ginza car-free from noon and the stores while it is dry, the Shinjuku Sumo Club show at 17:30, dinner in Shinjuku, then a late massage back in Ginza.'
D[25]['rows'] = [x for x in D[25]['rows'] if not x[1].startswith(('Massages', 'Bites around Ginza', 'Walk back to the hotel'))]
for _i, _x in enumerate(D[25]['rows']):
    if _x[0] == 'Afternoon': D[25]['rows'][_i] = R('13:30', _x[1], _x[2], *_x[3:])
    if _x[0] == 'Late arvo': D[25]['rows'][_i] = R('15:30', _x[1], _x[2], *_x[3:])
D[25]['rows'] += [
 R('16:30', 'Marunouchi line from Ginza to Shinjuku-sanchōme', 'Direct, about 17 minutes. Then about 15 minutes on foot north through Kabukichō. Aim to arrive by 17:15.'),
 R('17:30', 'Shinjuku Sumo Club: sumo show', 'Main venue. About 75 to 90 minutes. Live bouts, English MC, Q&A, a chance to challenge a wrestler (lottery), photos, one drink. Address on the Klook voucher (main venue: SEKISAKU Bldg 2F, 2-5-22 Ōkubo). About AU$74 each.', TB),
 R('19:00', 'Dinner in Shinjuku', 'Omoide Yokochō for yakitori under the lanterns, or Kabukichō. Ichiran (east exit) if you want ramen.'),
 R('20:30', 'Marunouchi line back to Ginza', 'Shinjuku or Shinjuku-sanchōme to Ginza, about 17 minutes.'),
 R('21:00', 'Late massage', 'Buasai Ginza (Thai, Ginza 8-chōme, 5 minutes from the hotel, to midnight), YURAGI (Ginza 7-chōme, to midnight) or Head Spa ZEN (Ginza 2-chōme, to 23:00). Book ahead in the afternoon.', TB),
]
D[25]['rows'].sort(key=lambda x: x[0])
D[25]['foot'] = 'Rain expected in the afternoon: the gardens and car-free Ginza early, the stores when it rains, then indoors for the sumo.'
D[26]['title'] = 'teamLab, Tokyo Tower coffee, Kappabashi, Sensō-ji at dusk'
D[26]['sum'] = 'teamLab Borderless first thing, coffee beside Tokyo Tower, Kappabashi kitchen street while the shops are open, lunch in Asakusa, Sensō-ji and the Skytree at dusk, then yakitori under the train tracks.'
D[26]['rows'] = [x for x in D[26]['rows'] if x[1].startswith(('Leave the Blossom', 'teamLab Borderless', 'Back to the hotel', 'Dinner under the train tracks'))] + [
 R('10:45', 'Sky Room Café & Bar, Mori JP Tower 34F', 'Coffee with Tokyo Tower right alongside. Open 09:00 to 21:00, no bookings. Zōjō-ji, the temple below the tower, is 10 minutes\' walk if you want it.'),
 R('11:30', 'Hibiya line, then the Ginza line to Tawaramachi', 'From Kamiyachō, Hibiya line to Ginza, change to the Ginza line to Tawaramachi (田原町), about 30 minutes.'),
 R('12:00', 'Kappabashi kitchenware street', 'Weekday, so the shops are open. Knives: Kama-asa (free engraving) and Kamata Hakensha. Ceramics: Dengama. Fake food: Ganso food samples. Niimi\'s giant chef head at the south end. Knives fly in checked bags only.'),
 R('13:30', 'Lunch in Asakusa', 'Ten minutes east on foot.'),
 R('14:30', 'Sensō-ji, Kaminarimon, Nakamise street', 'Kaminarimon gate, Nakamise street, the main hall. If Nakamise is jammed, take the side lanes.'),
 R('16:15', 'Skytree views at dusk, no deck', 'The free 8F terrace of the tourist centre opposite Kaminarimon, then Azuma-bashi bridge for the Skytree across the river as it lights up.'),
 R('17:30', 'Ginza line back to Shimbashi', 'Asakusa to Shimbashi, about 20 minutes. Drop the shopping at the hotel.'),
 R('19:15', 'Dinner under the train tracks, Yūrakuchō', 'The Gādo-shita lanes under the JR tracks between Yūrakuchō and Shimbashi, five minutes from the hotel. Yakitori, beer, the trains rumbling overhead. No booking; wander and pick one.'),
]
D[26]['rows'] = [x for i, x in enumerate(D[26]['rows']) if not (x[1].startswith('Dinner under') and x[0] != '19:15')]
D[26]['rows'].sort(key=lambda x: (not x[0][0].isdigit(), x[0]))
_seen = set(); _rr = []
for _x in D[26]['rows']:
    if _x[1] in _seen: continue
    _seen.add(_x[1]); _rr.append(_x)
D[26]['rows'] = _rr

# Sun 25 08:30: Shinjuku Sumo Club 17:30 booked on Klook, 2 adults.
for _i, _x in enumerate(D[25]['rows']):
    if _x[1].startswith('Shinjuku Sumo Club'):
        D[25]['rows'][_i] = R(_x[0], _x[1], _x[2].replace('About AU$74 each.', 'Booked on Klook for 2, about AU$74 each. Free cancellation closed (under 24 hours).'), B)
