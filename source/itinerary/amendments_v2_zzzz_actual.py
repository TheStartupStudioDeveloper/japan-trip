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
