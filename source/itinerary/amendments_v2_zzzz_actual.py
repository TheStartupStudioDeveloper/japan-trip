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
 R('15:00', 'To Yokohama', 'Enoden back to Kamakura, JR Yokosuka line to Yokohama, about 25 minutes, then the Negishi line two stops to Sakuragichō (How-to 27).'),
 R('16:15', 'Air Cabin, then Cosmo World', 'Air Cabin from outside Sakuragichō east exit, ¥1,000, 5 minutes. The Diving Coaster Vanish, about ¥1,000 each, cash only. Cosmo Clock 21 at sunset, about 17:05 (How-to 28). Cosmo World closes 20:00.'),
 R('17:45', 'Harbour walk to Chinatown', 'Red Brick Warehouses and Yamashita Park, about 30 minutes.'),
 R('18:30', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:45', 'Foot massage, Kyūryū SPA', 'Chinatown, 2F on a pedestrian lane. 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00 (How-to 28).'),
 R('21:00', 'Train home from Motomachi-Chūkagai', 'Straight through to Shibuya, about 40 minutes, no change. Back about 21:45.'),
]
D[19]['foot'] = D[19]['foot'] + ' Retimed at 08:22 after the Hibiya line delay: everything about 30 minutes later.'
