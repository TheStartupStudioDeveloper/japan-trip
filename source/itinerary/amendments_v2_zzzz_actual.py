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
