# V2.1 amendments. Applied on top of V2.0. Content only.
LEGS['s']['sum'] = 'An easy first day on foot, a shrine and festival Sunday with Street Kart, the stores and Shinjuku after dark on Monday, old Tokyo at Asakusa and the waterfront at Yokohama, then an early Shinkansen to Kyoto.'

# ---------- Sun 18 ----------
D[18].update(cal='Meiji, Street Kart', title='Meiji Jingū, Harajuku, the festival, Street Kart',
 sum='A light day on foot. The shrine and Harajuku in the morning, the festival on the walk home, then karting over the bay at golden hour.')
D[18]['rows'][1:4] = [
 R('09:45', 'Meiji Jingū', '15 minutes\' walk from the hotel. Forest paths and the big torii.'),
 R('11:00', 'Takeshita Street and the Harajuku back lanes', 'Busy on a Sunday. Walk it once, then duck into the lanes behind.'),
 R('12:15', 'Lunch in Harajuku'),
 R('13:15', 'Cat Street back into the festival streets', 'Dōgenzaka, Bunkamura-dori, 109. The streets close for stages on Sunday. Dip in and out rather than chasing set times.'),
]

# ---------- Mon 19 ----------
SHINJUKU[:] = [
 R('09:30', 'Late breakfast', 'A slow start. Nothing is booked today.'),
 R('11:00', 'Omotesando and Aoyama vintage luxury', 'Until 14:00. The secondhand luxury boutiques either side of the avenue. Some open at 11:00 and some at 12:00, so start with the early ones. Physical passports for tax-free.'),
 R('14:00', 'Lunch in Omotesando'),
 R('15:00', 'Back to the hotel', 'A 20 minute walk. Drop the bags, feet up.'),
 R('16:45', 'Shinjuku: the 3D cat at the east exit', 'JR Yamanote from Shibuya, about 7 minutes. The giant cat billboard at dusk.'),
 R('17:30', 'Omoide Yokochō', 'Yakitori and a drink, grazing across two or three counters before they fill (How-to 15).'),
 R('18:45', 'Godzilla head, Kabukichō and Kabukichō Tower', 'Through the underpass to the east side. Neon at full strength.'),
 R('20:00', 'Hanazono Shrine, then Golden Gai', 'The shrine is beside Golden Gai, lit at night, five minutes. Then tiny bars, some with cover charges. Hop around.'),
 R('21:30', 'Fukutoshin line home', 'From Shinjuku-sanchōme, the closest station to Golden Gai. Direct to Shibuya, about 5 minutes.'),
]
D[19].update(title='Omotesando stores, Shinjuku after dark', cal='Stores, Shinjuku')
a = D[19]['alts']
a[0]['sum'] = 'A slow start, the stores, a rest at the hotel, then Shinjuku after dark, west to east. Rain barely touches this day.'
a[0]['foot'] = 'Weather rule: the better day of Monday and Tuesday gets Asakusa and Yokohama, and the other gets this day. On a wet morning teamLab can move here (How-to 11), or try the Sumo show in Shibuya, times to check. Of interest if plans change: the Government Building deck about 16:15 for dusk, and the Isetan food hall.'
a[1]['list'] = ['Leave the stores by 14:00, then lunch and bags to the hotel as planned.',
                'Shibuya Sky about 16:15, the booked sunset slot.',
                'Then JR to Shinjuku about 17:45 and pick the plan up at Omoide Yokochō. The 3D cat comes after dinner.']
a[2]['sum'] = 'Monday and Tuesday swap. Today becomes the Asakusa and Yokohama day, exactly as written for Tuesday, and the Shinjuku day moves to Tuesday.'

# ---------- Tue 20 ----------
a = D[20]['alts']
a[0]['sum'] = 'Old Tokyo in the morning with the Skytree in view, kitchenware street, then down the bay to Yokohama for the waterfront and Chinatown. Home in time to pack. This is the outdoor day, so give it the better weather of Monday and Tuesday.'
a[2]['list'] = ['Today runs as written for Monday: late breakfast, the stores from 11:00, lunch at 14:00.',
                'Back to the hotel about 15:00 to pack for Wednesday, then Shibuya Sky at 16:00, the booked backup slot.',
                'JR to Shinjuku about 18:00 for Omoide Yokochō, the 3D cat, Kabukichō and Golden Gai.',
                'Train back by about 21:30. It is a 05:55 wake for the Shinkansen.']

# ---------- appendix ----------
HOWTO.append(('Omoide Yokochō, Mon 19', [
 'Memory Lane: two narrow alleys beside the west exit of Shinjuku Station, with about 60 tiny yakitori counters and bars under red lanterns.',
 'Arrive about 17:30. By 19:00 the popular counters are full.',
 'Pick any counter with two free seats. Order a drink each and a few skewers, then move on. Two or three places is the normal way to do it.',
 'Many counters add a small seating charge, a few hundred yen each, which comes with a small snack.',
 'Carry cash. Some counters do not take cards.',
 'It is smoky from the grills, and some counters allow smoking.',
 'This is the place to eat. Golden Gai, later, is tiny bars for drinking.']))
