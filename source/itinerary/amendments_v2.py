# V2.0 amendments. Applied on top of the V1.10 data in build.py.
# Content only. No change to structure, layout or styles.
D = {d['d']: d for d in DAYS}

# ---------- leg summaries ----------
LEGS['s']['sum'] = 'An easy first day on foot, a festival weekend with Street Kart, a shrine, vintage and Shinjuku day, old Tokyo at Asakusa and the waterfront at Yokohama, then an early Shinkansen to Kyoto.'
LEGS['g']['sum'] = 'Fireworks on arrival night, a slow Sunday that turns into a full Ginza day, teamLab first thing Monday then Tsukiji for lunch, a casual last night in Shimbashi, and an early train to Haneda.'
LEGS['h']['sum'] = 'Optional pool time in the sunny hours and evenings in the city. Thursday is the Big Buddha day. Friday is a pool day at the W or the Kerry, or a spare day, before the 00:30 flight. Wednesday, Thursday and Friday can swap to suit the weather.'

# ---------- Sat 17 ----------
D[17]['rows'] = [
 R('06:50', 'Land at Narita', 'Visit Japan Web QR codes ready. Allow about an hour to clear. Suica is already in your Apple Wallets.', B),
 R('Morning', 'Narita Express to Shibuya, bags to the hotel', 'Buy the ticket at Narita, on a train that stops at Shibuya (How-to 1). Walk from the Hachikō exit to the hotel, lobby on 4F (How-to 2). Leave the bags, ask about early check-in.'),
 R('Late morning', 'Miyashita Park and Cat Street', 'Start on the rooftop park above the hotel, where the festival will be on. Then drift down Cat Street: streetwear and small cafés. If you are shattered, stop here and rest.'),
 R('Lunch', 'Omotesando', 'Up into the leafy avenue. Eat wherever looks good. Omotesando Hills, Tod\'s and Dior are the architecture to look up at. Prada Aoyama is optional.'),
 R('Early arvo', 'Wander back into Shibuya', 'Hachikō, the Scramble Crossing, the side streets of Center-gai. Everything is within a 15 minute walk of the hotel.'),
 R('Mid arvo', 'Supplies, then check in and rest', 'MEGA Don Quijote Shibuya and the nearest 7-Eleven for room supplies. Then shower, feet up.'),
 R('16:00', 'Shibuya Sky', 'Seven minutes\' walk. Up in daylight, sunset about 17:00, then the city lights come on.', B),
 R('Evening', 'Dinner close by', 'Nonbei Yokochō or Dōgenzaka, then an early night.'),
]

# ---------- Sun 18 ----------
D[18]['extra'] = ('If Street Kart can\'t run today', [
 ('Today', 'Spend the extra time in Shibuya. Stay on the festival streets through the afternoon, then dinner as planned.'),
 ('Backup', 'Rebook for Sunday 25 or Monday 26 October, when you are staying in Hibiya. It is on that side of town. Sunday slots into the Ginza day and Monday into the free afternoon. See both days.')])

# ---------- Mon 19, the Shinjuku day ----------
SHINJUKU[:] = [
 R('09:00', 'Meiji Jingū', '15 minutes\' walk from the hotel. Quietest early.'),
 R('10:00', 'Takeshita Street, Harajuku', 'Straight out of the shrine gate. Loud, silly and fun for half an hour.'),
 R('11:00', 'Omotesando and Aoyama vintage luxury', 'Until 13:30. The secondhand luxury boutiques in the back streets either side of the avenue. Physical passports for tax-free.'),
 R('13:30', 'Lunch in Omotesando'),
 R('14:30', 'To Shinjuku: the 3D cat, then Isetan', 'JR Yamanote from Harajuku, a few minutes. The giant 3D cat billboard is outside the east exit. Then Isetan and the east side, with a rest stop.'),
 R('17:30', 'Omoide Yokochō', 'Yakitori in the smoky alleys. Bar Benfiddich is a few minutes away, open from 19:00, no booking. Only if you are passing.'),
 R('19:30', 'Kabukichō, Godzilla head'),
 R('21:00', 'Golden Gai', 'Tiny bars, some with cover charges. Hop around.'),
 R('22:30', 'Train back to Shibuya', 'JR Yamanote, about 7 minutes, or the Fukutoshin line from Shinjuku-sanchōme. Not a late one.'),
]
a = D[19]['alts']
a[0]['sum'] = 'The big urban day. The shrine and Harajuku first, vintage luxury in Omotesando and Aoyama, then Shinjuku for the afternoon and evening. Train home about 22:30.'
a[0]['foot'] = 'If it is wet on any day this leg, teamLab Borderless can take the morning (How-to 11), or try the Sumo show in Shibuya, times to check. Tsukiji Outer Market could also fit this morning. Monday and Tuesday can still swap as whole days.'
D[19]['title'] = 'Meiji, Omotesando, Shinjuku night'
D[19]['cal'] = 'Meiji, Shinjuku'
a[1]['list'] = ['Finish in Omotesando about 14:30 and take the afternoon gently. Shinjuku waits until the evening.',
                'Be back in Shibuya about 16:15 for the booked sunset slot.',
                'Then JR to Shinjuku, five minutes, for the 3D cat, Omoide Yokochō, Kabukichō and Golden Gai as planned.']

# ---------- Tue 20 ----------
a = D[20]['alts']
a[2]['list'] = ['The morning runs as written for Monday: Meiji Jingū, Takeshita Street, Omotesando and Aoyama, lunch at 13:30.',
                'Back to the hotel about 14:30 to pack for Wednesday, then Shibuya Sky at 16:00, the booked backup slot.',
                'JR to Shinjuku about 18:00 for the 3D cat, Omoide Yokochō, Kabukichō and Golden Gai. Isetan drops out.',
                'Train back by about 21:30. It is a 05:55 wake for the Shinkansen.']

# ---------- Wed 21 ----------
D[21]['rows'] = [
 R('05:55', 'Wake, final pack'),
 R('06:20', 'Check out'),
 R('06:30', 'Taxi to Shinagawa, Kōnan exit', 'About 20 to 25 minutes. Book it at the front desk the night before. The Yamanote line from Shibuya is the fallback (How-to 3).'),
 R('07:00', 'Shinagawa, ekiben and coffee', 'Breakfast on the train. Early on purpose: this is the train you cannot miss.'),
 R('07:55', 'Nozomi 13 to Kyoto', 'Car 9, seats 16-C and 16-D, Green Car with oversized baggage area. Fuji on the right at about 08:30.', B),
 R('10:00', 'Kyoto Station', '', B),
 R('10:15', 'Bags to the staffed luggage counter', 'Stored at Kyoto Station for the day, not forwarded. Check the closing time when you drop them (How-to 4).'),
 R('10:45', 'JR Nara line rapid', '45 minutes.'),
 R('11:30', 'Nara', 'Deer within five minutes of the station.'),
 R('12:00', 'Lunch on Sanjō-dōri, then into Nara Park'),
 R('13:00', 'Tōdai-ji and the Great Buddha', 'The one unmissable thing here.'),
 R('14:30', 'Kasuga Taisha, up through the lantern path', 'Quieter, wooded, and the better half of Nara.'),
 R('15:30', 'Isuien garden, or Nigatsu-dō', 'Pick one. Nigatsu-dō has the view back over the city.'),
 R('16:30', 'Train back', 'Kyoto by 17:15. Collect the bags.'),
 R('17:25', 'Walk to sequence KYOTO GOJO', '20 to 25 minutes with the bags (How-to 4).'),
 R('18:00', 'Check in, then dinner around Pontochō or Shijō', 'From the hotel, Pontochō is about 15 minutes north on foot, or two stops on the Keihan line.'),
]

# ---------- Thu 22, Osaka ----------
D[22]['title'] = 'Osaka, castle to Dōtonbori'
D[22]['sum'] = 'A whole day in Osaka, no Universal. The castle up close first, Umeda Sky mid morning, a market lunch, the shops, the lion head, Shinsekai at dusk and Dōtonbori at night. One deck, not two.'
D[22]['rows'] = [
 R('07:15', 'Keihan line from Kiyomizu-Gojō to Temmabashi', 'About 50 minutes, one change to a limited express. Confirm the train the night before (How-to 7).'),
 R('08:20', 'Osaka Castle, up close', 'Through the park to the foot of the tower. Not inside. The park is open around the clock. Takeaway breakfast on a bench.'),
 R('09:35', 'Tanimachi line to Higashi-Umeda', 'Buy the one-day Enjoy Eco Card at the metro station, about ¥820. It covers the Osaka Metro all day, not JR or Keihan.'),
 R('10:15', 'Umeda Sky deck', 'Two towers joined by a floating escalator. About 15 minutes on foot from Higashi-Umeda.'),
 R('12:00', 'Kuromon Ichiba', 'Midōsuji line down to Namba. Grilled scallops, uni, tuna cut in front of you. This is lunch, not a snack stop.'),
 R('13:15', 'Horie, Amerikamura and Shinsaibashi', 'The vintage and secondhand luxury run: Kindal Horie, ALLU, KOMEHYO. Orange Street for furniture, design shops and coffee when you want it calmer. Passports for tax-free.'),
 R('15:30', 'Namba Yasaka Shrine', 'The giant lion head. Ten minutes is enough. Closes about 17:00.'),
 R('16:15', 'Janjan-Yokochō into Shinsekai', 'In at dusk as the signs come on. Sunset is 17:05. Tsūtenkaku, and kushikatsu under the tower, kept to a snack.'),
 R('18:30', 'Dōtonbori', 'Buy Tombori River Cruise tickets when you arrive and ride after dark (How-to 14). The Glico Running Man photo platform is at the Nanohana cosmetics shop, directly opposite the sign. Eat standing up.'),
 R('20:30', 'Hōzenji Yokochō', 'Two streets back. Stone lanes, lanterns and the mossy Mizukake Fudō. A quiet drink after the noise.'),
 R('21:30', 'Home by Midōsuji line and Keihan', 'Namba to Yodoyabashi, then the Keihan limited express to Shichijō. Premium Car is about ¥500 extra. Walk 10 minutes, or one local stop to Kiyomizu-Gojō (How-to 7).'),
]
D[22]['notes'] = [
 ('Weather fallback', 'If the morning is clouded out, do Umeda Sky at night instead, open to 22:30. Or work Abeno Harukas 300 back in at sunset, ten minutes on foot from Shinsekai.'),
 ('Running late', 'Shorten the castle first, then the shops. Protect lunch at Kuromon, the lion head before 17:00 and Shinsekai at dusk.'),
 ('Left out', 'Nakazakichō, Nakanoshima and Abeno Harukas 300. Thursday and Friday can swap if they must. See The four legs.')]

# ---------- Fri 23 ----------
r = D[23]['rows']
i = [x[0] for x in r].index('11:15')
r[i] = R('11:15', 'Back to the centre, lunch at Nishiki Market', 'Five blocks of food stalls just off Shijō. You are right there.')
i = [x[0] for x in r].index('14:15')
r.insert(i, R('Afternoon', 'Higashiyama', 'The old eastern hills. The next three stops are the district, top to bottom. Tick it off.'))

# ---------- Sat 24 ----------
r = D[24]['rows']
i = [x[0] for x in r].index('10:45')
r[i] = R('10:30', 'Check out and walk to Kyoto Station', '20 to 25 minutes with the bags (How-to 5).')

# ---------- Sun 25 ----------
r = D[25]['rows']
i = [x[0] for x in r].index('Afternoon')
r[i] = R('Afternoon', 'Department stores and shopping', 'Mitsukoshi, Ginza Six, Matsuya, Dover Street Market, Itoya, vintage luxury resale, which is the fallback if the Omotesando run on Monday 19 fell short. Maison Hermès, Mikimoto Ginza 2 and the Wakō clock tower as you go. Passports.')
i = [x[0] for x in r].index('When done')
r.insert(i, R('19:30', 'Optional: Skytree lit up', 'Ginza line to Asakusa. Azumabashi bridge, then Sensō-ji lit. Or Monday after dinner.'))
D[25]['foot'] = D[25]['foot'].replace('If it is wet, drop the gardens and start in Ginza earlier.', 'If it is wet, drop the gardens and start in Ginza earlier, or move teamLab to this morning (How-to 11).')
D[25]['foot'] += ' Sushi Bus idea for lunch, not decided: 20 seats, ¥16,000 each, about 70 minutes from Kajibashi Parking Lot near Tokyo Station, sushi-bus.com.'
D[25]['extra'] = (D[25]['extra'][0], [
 ('One of two backups for Sunday 18', D[25]['extra'][1][0][1]),
 D[25]['extra'][1][1]])

# ---------- Mon 26 ----------
D[26].update(cal='teamLab, Tsukiji', title='teamLab first thing, Tsukiji for lunch, Shimbashi',
 sum='First session at teamLab, Tokyo Tower and the temple, two stops to Tsukiji Outer Market for lunch, a walk back through Ginza, then a free afternoon before a casual last night.',
 rows=[
  R('07:50', 'Leave the Blossom', 'About 25 minutes on foot via Toranomon to Azabudai Hills. Taxi if it is wet.'),
  R('08:30', 'teamLab Borderless, first session', 'Arrive a little early to be among the first in. Allow about two hours. The booking can change date or time up to three times.', B),
  R('10:50', 'Tokyo Tower and Zōjō-ji', 'About 10 minutes\' walk. The temple gate with the tower behind it. Coffee at Sky Room Café on 33F at Azabudai Hills first, if you like.'),
  R('11:40', 'Ōedo line from Daimon to Tsukijishijō', 'Two stops.'),
  R('12:00', 'Tsukiji Outer Market lunch', 'Arrive by 12:30, the stalls wind down early in the afternoon. Tamagoyaki, tuna, grilled scallop and uni, strawberry daifuku, then Namiyoke shrine. Eat at the stall, not walking.'),
  R('13:30', 'Walk back through Ginza', 'About 20 minutes to the hotel.'),
  R('14:00', 'Free afternoon', 'Rest and half pack, or more Ginza. Street Kart at 16:00 if it moved here.'),
  R('19:00', 'Shimbashi, no booking', 'Five minutes from the hotel. Wander the lanes around the tracks, eat wherever looks good. Weeknights are when it\'s liveliest.'),
  R('Optional', 'Skytree lit up', 'If you did not go on Sunday. Asakusa line from Shimbashi to Asakusa, about 10 minutes.'),
  R('Late', 'Back to the hotel', 'Finish packing and settle the bill. Tomorrow is the 06:38 train (How-to 6).'),
 ],
 notes=[
  ('Why Monday', 'The outer market is largely shut on Sundays and Wednesdays, and this is the only free morning on this side of town.'),
  ('The other way round', 'Market first at about 08:00, with teamLab moved to 13:30. That also makes room for a guided market tour.'),
  ('If teamLab was used earlier', 'As a wet weather move from Shibuya or Sunday, it frees this whole morning for the market.')],
 extra=('If Street Kart moved to today', [
  ('The other backup for Sunday 18', 'The 16:00 slot sits inside the free afternoon. Leave the hotel about 14:45 and arrive 30 minutes ahead with International Driving Permit and passports.'),
  ('Afterwards', 'Straight to Shimbashi for dinner. Pack before you go out.')]))

# ---------- Tue 27 ----------
D[27]['sum'] = D[27]['sum'].replace('An early run to Haneda with the bags', 'An early train to Haneda with the bags')
r = D[27]['rows']
r[0:2] = [
 R('05:45', 'Wake, shower, final pack'),
 R('06:22', 'Leave the hotel, walk to Shimbashi', 'About 8 minutes with the bags. Asakusa line, platform 1.'),
 R('06:38', 'Airport Rapid Limited Express to Haneda Terminal 3', 'Direct, about 25 minutes. The backup is the 06:45 Express. Avoid trains bound for Nishi-magome (How-to 6).'),
]
i = [x[0] for x in r].index('16:15')
r[i] = R('16:15', 'Check in at the Sheraton', 'Ask three things at the desk: whether pool sessions need booking, the club lounge hours, and where the emailed request for a late checkout or extra night on Friday landed.')
D[27]['notes'][0] = ('Taxi instead in Tokyo', 'The fallback if the train looks wrong on the day. About 25 minutes. Even a 07:15 taxi gets you to Haneda 2.5 hours before departure.')

# ---------- Wed 28 ----------
D[28]['sum'] = 'The main Island day and the main night out. Up the Peak early by tram, time at the top through sunset, taxi down.'
D[28]['rows'] = [
 R('09:00', 'Lounge breakfast'),
 R('09:45', 'Sheraton pool until about 13:00', 'Optional. This is the best block for sun. Read, tan, swim. Light lunch at the hotel.'),
 R('13:30', 'Star Ferry to Central', 'Ten minutes across the harbour.'),
 R('14:00', 'Graham Street Market, Tai Kwun, PMQ, Mid-Levels escalator', 'The old street market first, then design and architecture, all within a few blocks.'),
 R('15:45', 'Peak Tram up', 'Standard one-way ticket, prebooked. Sit on the right going up. Then Lugard Road for the best free view, and take your time at the top (How-to 13).', TB),
 R('17:50', 'Sunset at the Peak', 'Stay while the city lights come on.'),
 R('18:45', 'Taxi down', 'Tram seats face backwards on the way down, so skip it.'),
 R('19:30', 'Dinner in Central or SoHo', 'The big dinner of the trip. Book ahead.', TB),
] + D[28]['rows'][-2:]
D[28]['notes'] = [
 ('Fast Track', 'Klook\'s Peak Tram Fast Track only runs Friday to Sunday. If the Peak moves to Friday 30, that is the ticket to buy.')]

# ---------- Thu 29 ----------
r = D[29]['rows']
T = lambda t: [x[0] for x in r].index(t)
r[T('10:00')] = R('10:00', 'Ngong Ping 360 cable car up', 'Crystal cabin, Klook voucher (How-to 12). First car, shortest queues. 25 minutes.', TB)
r[T('14:00')] = R('14:00', 'Lunch in Central or Sheung Wan', 'Yum cha is the idea. Or swap a lounge breakfast for it.')
r[T('17:30')] = (R('18:15', 'Ozone at the Ritz-Carlton', 'Quick change first. 118th floor, short taxi to ICC. Low cloud: go Friday. Check hours.'))
e = D[29]['extra'][1]
e[1] = ('Weather', 'The cable car stops in high wind and the views vanish in low cloud. Check the forecast the night before. The Klook voucher moves freely between Wednesday, Thursday and Friday.')

# ---------- Fri 30 ----------
D[30]['title'] = 'Pool day or spare day, then departure'
D[30]['cal'] = 'Pool, fly home'
D[30]['sum'] = 'Bags stay at the Sheraton, you shower at the pool, and a taxi at 20:45 gets you to the airport three hours before the flight. The pool is optional. This is also the spare day for anything missed.'
r = D[30]['rows']
T = lambda t: [x[0] for x in r].index(t)
r[T('18:45')] = R('18:45', 'Dinner, or Ozone if Thursday was clouded out', 'Ozone is next door to the W in the ICC tower. Otherwise eat near the W, or back in Tsim Sha Tsui close to the bags.')
D[30]['notes'] = [
 D[30]['notes'][0],
 ('Kerry Hotel instead of the W', 'The Kerry\'s Revitalising Daycation in Hung Hom is the alternative pool day if the W deck is no good in the weather. Price and inclusions still to confirm.'),
 ('Late checkout', 'The Sheraton has been emailed about a late checkout, a day-use rate or an extra night. A 14:00 checkout means you can start at the Sheraton pool. Until 18:00 or later means you shower in your own room.'),
 ('If Friday is wet or grey', 'Skip the pool. M+ and the West Kowloon waterfront is the indoor option. Or use the spare day: Ngong Ping on the voucher, or the Peak with Klook Fast Track. Checkout and the 20:45 taxi stay the same.')]

SWAPS[0] = ('Ngong Ping on Friday, instead of Thursday', 'Replaces Friday morning. Check out by 08:00, first cable car at 10:00, at the pool by about 15:00. The Klook voucher moves with you.', SWAPS[0][2])

# ---------- good to know ----------
GOOD['k'][2] = ('Closing times', 'Kiyomizu-dera 18:00. Sanjūsangen-dō 17:00. Ginkaku-ji 17:00. Namba Yasaka Shrine about 17:00. Umeda Sky 22:30.')
GOOD['k'][3] = ('Decided', 'No Universal. Thursday is the Osaka day. Thursday and Friday can swap if they must, but Gion dinner is planned for Friday.')
GOOD['g'][4] = ('Getting around', 'Everything this leg is walkable or a 10 minute taxi from the hotel, plus two metro stops to Tsukiji on Monday.')
GOOD['h'][1] = ('Best pool sun', 'Roughly 10:00 to 14:00. Pool blocks are optional. The Sheraton deck loses the sun by late afternoon.')
GOOD['h'][4] = ('Getting around', 'Red taxis cover Kowloon and Hong Kong Island, keep some cash on you. The Star Ferry, MTR and trams all take Octopus. Tsim Sha Tsui to Central is ten minutes by ferry.')

# ---------- checklist ----------
CHECK[:] = [
 ('Before you fly', [
  ('s', 'International Driving Permit, 1949 Geneva Convention version, for Street Kart'),
  ('s', 'Visit Japan Web registered for both of you'),
  ('s', 'Street Kart meeting point and arrival time, from the booking'),
  ('s', 'Street Kart: check the rebooking terms, in case it moves to Sun 25 or Mon 26'),
  ('s', 'Shibuya Sky Monday and Tuesday slots: check the cancellation or change terms'),
  ('s', 'Suica in both Apple Wallets, set up and topped up'),
  ('s', 'Ubigi eSIM, one each. Install at home, switch on in Hong Kong on Fri 16'),
  ('k', 'Gion or Pontochō dinner for Fri 23, 18:30'),
  ('g', 'Confirm where and when the Seascape wristbands are collected on Sat 24'),
  ('h', 'Confirm CX543 and CX105 times in the Cathay app'),
  ('h', 'Hong Kong dollars for the airport taxi on arrival'),
  ('h', 'Aqua Luna Symphony of Lights cruise for Tue 27, 19:30 from Tsim Sha Tsui Pier 1'),
  ('h', 'Dinner booking in Central for Wed 28, 19:30'),
  ('h', 'Octopus in both Apple Wallets'),
  ('h', 'Ngong Ping 360 Crystal cabin vouchers on Klook, good to 31 October'),
  ('h', 'W Hong Kong WET day pass: price, inclusions, and whether it is tied to a date'),
  ('h', 'Kerry Hotel Daycation: price and inclusions, as backup to the W'),
  ('h', 'Sheraton: chase the late checkout or extra night email'),
 ]),
 ('Once you have seen the Hong Kong forecast', [
  ('h', 'Peak Tram one-way up, about 15:45 on the clearest evening (Wed 28 by default)'),
  ('h', 'W or Kerry pool day pass for the sunniest day (Fri 30 by default)'),
  ('h', 'Pick the Ngong Ping day for the voucher, first car at 10:00 (Thu 29 by default)'),
 ]),
 ('On the ground', [
  ('s', 'Narita Express tickets at Narita, on a train that stops at Shibuya'),
  ('s', 'Ask Sequence Miyashita Park about early check-in on Sat 17'),
  ('s', 'Book the 06:30 taxi to Shinagawa for Wed 21, the night before'),
  ('k', 'Confirm the 07:15 Keihan train to Osaka the night before Thu 22'),
  ('g', 'Ask the Blossom about guest laundry, a week into the trip'),
  ('g', 'Settle the bill on Monday night for a quick checkout'),
  ('g', 'Check the 06:38 Asakusa line train to Haneda the night before Tue 27'),
  ('h', 'Sheraton: do pool sessions need booking? If so, book Wednesday morning'),
  ('h', 'Sheraton: club lounge hours for breakfast and evening drinks'),
  ('h', 'Sheraton: late checkout on Friday, 14:00 free or a paid extension to 18:00'),
  ('h', 'Sheraton: confirm the concierge will hold bags on Friday until 20:30'),
 ]),
]

# ---------- new page: tips ----------
TIPS = [
 ('Passports', 'Carry the physical passports on shopping days: Sat 17, Mon 19, Thu 22 and Sun 25. A photo on the phone is not accepted for tax-free.'),
 ('Tax-free', '10% off, or 8% on food, when you spend over ¥5,000 in one store. Taken off at the till until 31 October. See How-to 10.'),
 ('Cash and coins', 'Small restaurants, shrines and market stalls are often cash only. Keep a coin purse. 7-Eleven ATMs take foreign cards around the clock.'),
 ('Money tray', 'Put cash or card on the small tray at the till, not into the hand. Change comes back the same way.'),
 ('No tipping in Japan', 'Not expected anywhere, and it can cause confusion. A thank you is enough.'),
 ('Ticket machine restaurants', 'Many ramen and casual places have a machine at the door. Pick, pay, then hand the ticket to the staff.'),
 ('Eating and walking', 'Eat at the stall or standing to one side, not on the move. Same on trains, other than the Shinkansen.'),
 ('Litter', 'Public bins are rare. Carry a small bag and take rubbish back to the hotel or a convenience store.'),
 ('Escalators', 'Stand on the left in Tokyo, on the right in Osaka, and on the right in Hong Kong.'),
 ('Trains', 'Phones on silent, no calls, bags off your back in a crowd. Queue on the platform markings and let people off first.'),
 ('Crossing', 'Wait for the green man, even on an empty street. Nobody jaywalks.'),
 ('Shoes', 'Off wherever there is a step up or a rack at the door: temples, some restaurants, fitting rooms. Wear good socks.'),
 ('Chopsticks', 'Never stand them upright in rice or pass food from chopstick to chopstick. Rest them on the holder.'),
 ('Shrines and temples', 'Bow once at the torii gate and walk to the side of the path, not down the middle. Rinse hands at the basin. At a shrine: bow twice, clap twice, bow once. At a temple, no clapping.'),
 ('The ¥5 coin', 'The lucky offering at a shrine. Keep a few aside.'),
 ('Bowing', 'A small nod back is all that is needed.'),
 ('Geisha and maiko', 'No photos in Gion without permission, and keep off the private lanes. There are fines.'),
 ('Nara deer', 'Buy the crackers, show empty hands when you run out, and keep maps and paper out of reach. They bow, and they also nip.'),
 ('Taxi doors', 'The rear left door opens and closes by itself in Japan. Leave it alone.'),
 ('Smoking', 'Only in marked smoking areas, not on the street.'),
 ('Umbrellas and wet gear', 'Use the umbrella stand or the plastic sleeve at shop doors. Clear umbrellas are cheap at any convenience store. Pack a light rain jacket each.'),
 ('Typhoon season', 'Late October is the tail end for both Japan and Hong Kong. Watch the forecast and use the wet weather swaps.'),
 ('Luggage and lockers', 'Coin lockers at every big station take Suica. Large sizes fill by mid morning, so use a staffed counter for suitcases.'),
 ('Cold lockers', 'Some stations and department stores have refrigerated lockers. Ask for an ice pack when buying food to carry.'),
 ('Maps on luggage days', 'Turn on the accessible or step-free route option in the maps app. It finds the lifts and avoids stairs.'),
 ('Flu season', 'It has started early in Japan this year. Consider masks on trains, carry hand sanitiser, be vigilant, and perhaps pack vitamins.'),
 ('Data', 'The eSIM gives 30GB at full speed, then slows right down. Use hotel wifi for photo backups. See How-to 8.'),
 ('Hong Kong: tipping', 'Restaurants add 10% service. Round up for taxis. Small notes for porters.'),
 ('Hong Kong: MTR', 'No eating or drinking past the gates. There are fines.'),
 ('Hong Kong: trams', 'Board at the back, pay with Octopus at the front as you get off. Upper deck, front seat.'),
]

# ---------- new pages: how-to appendix ----------
HOWTO = [
 ('Narita Express ticket, Sat 17', [
  'After customs, follow the signs for Railways down to the basement level.',
  'Buy at the JR East Travel Service Centre or a JR ticket machine with the N\'EX logo. Every seat is reserved, so the ticket gives you a car and seat. No need to book from home.',
  'Ask for Shibuya. Check the train on your ticket stops at Shibuya, as not every service does.',
  'About 75 to 80 minutes. Big bags go in the racks at the end of the car.',
  'Pay by card. Suica does not cover the express fare.']),
 ('Shibuya Station to the hotel, Sat 17', [
  'Leave by the Hachikō exit, the one for the dog statue and the Scramble Crossing.',
  'Keep the rail line on your right and walk north along it to Miyashita Park, the long building with the park on its roof.',
  'Sequence Miyashita Park is the tower at the far, northern end. About 7 minutes, flat.',
  'Take the lift to the lobby on the 4th floor. Leave the bags and ask about early check-in.']),
 ('Hotel to the Shinkansen, Wed 21', [
  'The night before: pack, settle the bill, and ask the front desk to book a taxi for 06:30.',
  '05:55 wake. 06:20 check out. 06:30 taxi to Shinagawa Station, Kōnan exit, which is the Shinkansen side. About 20 to 25 minutes.',
  'About 07:00 at Shinagawa. Buy ekiben and coffee inside the Shinkansen gates.',
  'On the platform by 07:40. Nozomi 13 leaves at 07:55. Car 9, seats 16-C and 16-D. Bags go in the oversized baggage space behind the last row.',
  'Fallback if no taxi comes: JR Yamanote line from Shibuya to Shinagawa, about 13 minutes, leaving by 06:45.']),
 ('Kyoto Station, bags and the walk, Wed 21', [
  'Off the Nozomi at 10:00. Take the suitcases to the staffed luggage counter in the station, not the Sagawa forwarding desk.',
  'Store them for the day. Keep the receipt and note the closing time.',
  'Nara and back as planned. Collect the bags about 17:15.',
  'Walk to sequence KYOTO GOJO: out the north side, the Kyoto Tower side, then north and east to Gojō. 20 to 25 minutes, flat.',
  'A taxi from the north rank is the easy alternative if you are tired.']),
 ('Kyoto back to Tokyo, Sat 24', [
  'Check out and leave the hotel at 10:30. Walk the same way back, 20 to 25 minutes.',
  '11:15 at Kyoto Station. Ekiben and coffee, then through the Shinkansen gates.',
  'Nozomi 16 leaves at 12:01. Car 9, seats 1-C and 1-D. Fuji is on the left.',
  '14:15 Tokyo Station. Follow the Yaesu exit signs to the taxi rank. Ten to fifteen minutes to the Blossom.']),
 ('Train to Haneda, Tue 27', [
  'Monday night: pack, settle the bill, and check the first trains in the maps app.',
  '05:45 wake. 06:22 leave the hotel and walk to Shimbashi Station, about 8 minutes. Go down to the Toei Asakusa line, platform 1.',
  '06:38 Airport Rapid Limited Express, direct to Haneda Airport Terminal 3. About 25 minutes. Suica works.',
  'Backup: the 06:45 Express, also direct.',
  'Do not board a train bound for Nishi-magome. It does not go to the airport.',
  'If anything looks wrong, take a taxi from the hotel rank. About 25 minutes.']),
 ('Osaka there and back, Thu 22', [
  'Out: Keihan line from Kiyomizu-Gojō towards Osaka. Change once to a limited express, usually at Shichijō or Tambabashi. Get off at Temmabashi. About 50 minutes.',
  'The castle is a 10 to 15 minute walk from Temmabashi.',
  'At the first metro station, buy the Enjoy Eco Card day pass from the ticket machine. About ¥820 on a weekday. It covers the Osaka Metro, not JR or Keihan.',
  'Back: Midōsuji line from Namba to Yodoyabashi, three stops. Change to the Keihan limited express for Kyoto.',
  'Premium Car is a reserved seat for about ¥500 extra. Buy it at the machine on the platform.',
  'Get off at Shichijō. Walk 10 minutes to the hotel, or take a local one stop to Kiyomizu-Gojō.',
  'Leaving Namba at 21:30 puts you home about 22:45.']),
 ('eSIM and wifi', [
  'Ubigi Best Asia Unlimited, 15 days, AU$78 each. One for each phone.',
  'Install at home on wifi. Switch it on when you land in Hong Kong on Fri 16 October at 21:45, so the 15 days cover the whole trip. Check the expiry date in the app.',
  'It covers Japan on KDDI and Docomo, and Hong Kong on Smartone. No change needed between countries.',
  '30GB at full speed, then 2 Mbps. Track usage in the Ubigi app.',
  'If you run low, top up in the app or buy a separate Hong Kong plan.',
  'Phone settings: Auto-Join on for hotel wifi, Wi-Fi Assist off, photo backup on wifi only.']),
 ('Suica and Octopus', [
  'Both are already in your Apple Wallets. Tap the phone at the gate, no need to unlock it with Express Mode on.',
  'Top up in Wallet with Apple Pay. Keep about ¥2,000 on Suica.',
  'Suica works on trains, metros and buses across Tokyo, Kyoto and Osaka, and at convenience stores, lockers and vending machines.',
  'It does not pay for Shinkansen or Narita Express tickets.',
  'Octopus does the same job in Hong Kong: MTR, Star Ferry, trams, buses and convenience stores.',
  'Spend the Suica balance airside at Haneda.']),
 ('Tax-free shopping', [
  'Take the physical passports. The shop scans the entry sticker. A photo is not accepted.',
  'Spend over ¥5,000 before tax in one store on the same day. Look for the Tax-Free sign, or the tax-free counter in a department store.',
  'The 10% comes off at the till, or 8% on food. Department stores refund it at a counter and may keep a small fee.',
  'Consumables such as cosmetics and food are sealed in a bag. Leave it sealed until you have left Japan.',
  'This at-the-till system runs until 31 October, so it covers the whole trip.']),
 ('Moving teamLab for wet weather', [
  'Booked for Mon 26 at 08:30. The date or time can be changed up to three times.',
  'Open the booking from the confirmation email and choose the change option.',
  'Good places for it: any wet morning on the Shibuya leg, or Sunday 25 morning in place of the gardens.',
  'From Shibuya it is about 30 minutes by metro to Azabudai Hills, or 15 to 20 minutes by taxi.',
  'If it moves, Monday 26 morning opens up for an early Tsukiji Outer Market.']),
 ('Ngong Ping 360 voucher', [
  'Buy two Crystal cabin vouchers on Klook before flying. Non-refundable, but good on any day up to 31 October.',
  'Pick the day from the forecast the night before. Clear and calm is what you want.',
  'MTR to Tung Chung, about 50 minutes from Tsim Sha Tsui with one change. The cable car terminal is a few minutes from exit B.',
  'Be there for the first car at 10:00. Follow the signs for Klook or prepaid vouchers, and join the Crystal cabin queue.',
  'If it closes for wind, the voucher simply moves to another day.']),
 ('Peak Tram', [
  'Book a standard one-way ticket up, for about 15:45 on the clearest evening.',
  'The lower terminus is on Garden Road in Central. A 15 minute walk uphill from the ferry, or a short taxi.',
  'Sit on the right going up for the view.',
  'At the top, walk Lugard Road, about 20 minutes each way, for the best free view. Stay through sunset at 17:50.',
  'Taxi down from the rank by the Peak Galleria. Tram seats face backwards on the way down.',
  'If the Peak moves to Friday, the Klook Fast Track ticket runs Friday to Sunday.']),
 ('Dōtonbori canal boat, Thu 22', [
  'The Tombori River Cruise leaves from the canal beside the Don Quijote building.',
  'Buy tickets at the booth when you arrive in Dōtonbori at 18:30, for a boat after dark. They sell by time slot.',
  'About 20 minutes on the water under the neon.',
  'The Glico Running Man photo platform is at the Nanohana cosmetics shop, directly opposite the sign.',
  'Times and price not yet checked. Skip it without regret if the queue is long.']),
]
