# Sun 18 rework (sent 07:22): PATH breakfast, park, shrine, Harajuku, vintage. Cynthia's shopping afternoon, G's options.
# Yokohama moves to Mon 19, Shinjuku plus new free time to Tue 20. Shibuya Sky is done, so the tabs go.
D[18].update(cal='PATH, Meiji, vintage, Street Kart', title='PATH breakfast, Meiji Jingū, vintage, Street Kart')
D[18]['sum'] = "Dutch pancakes in Tomigaya, through Yoyogi Park to Meiji Jingū, Takeshita Street, then Cynthia's shopping afternoon in Omotesando while G does Harajuku and Nintendo. Street Kart at golden hour, then ramen and a foot massage."
D[18]['rows'] = [
 R('07:30', 'Walk to PATH, Tomigaya', '20 minutes on foot, or 5 by taxi. Opens 08:00. Sign the electronic waitlist outside straight away: by 10:30 on a Sunday the wait is over two hours.'),
 R('08:00', 'Breakfast at PATH', 'The Dutch pancake with ham, burrata and maple. It takes 30 to 45 minutes, so order it first, with a coffee.'),
 R('09:30', 'Yoyogi Park', 'Five minutes away. Walk through to the Harajuku gate. Sunday rockabilly dancers near that entrance.'),
 R('10:15', 'Meiji Jingū', 'Forest paths and the big torii. About 45 minutes.'),
 R('11:00', 'Takeshita Street', 'Out of the Harajuku gate and across the road. Walk it once together.'),
 R('11:30', "Cynthia's shopping afternoon", 'Omotesando and Aoyama vintage luxury, all open now (How-to 9). Passports for tax-free. Back at the hotel by 14:20: a 10 minute taxi from Omotesando.'),
 R('11:30', "G's free time", 'UNIQLO and H&M Harajuku for cargo pants, ZARA on Meiji-dōri, lunch, then down to Nintendo Tokyo in Shibuya Parco. Back by 14:20 (How-to 10).'),
 R('14:20', 'Back at the hotel', 'Fully closed shoes. Physical licence cards, physical International Driving Permits, passports. No digital copies.'),
 R('14:45', 'Leave for Street Kart', 'Check which shop the voucher names (How-to 25). Aim to arrive by 15:30.'),
 R('16:00', 'Street Kart, Rainbow Bridge route', 'About two hours. Golden hour over the bay.', B),
 R('18:30', 'Back to the hotel, shower', 'Same way back, or a taxi.'),
 R('19:30', 'Ichiran Shibuya, join the queue', 'Jinnan, B1F, open 24 hours. Scan the QR code at the door to join the waitlist, then go next door. Tonkotsu ramen in solo booths.'),
 R('19:45', 'Foot massage at Mominotakumi', 'Next door to Ichiran, 9F. Open to 23:00. Book by phone this afternoon: +81 3-6416-0995. Then ramen when your number comes up.'),
]
D[18].pop('foot', None)

def _strip(d):
    for k in ('alts', 'tabs', 'tablabel', 'group'): D[d].pop(k, None)

# Mon 19: the Tsukiji and Yokohama day (was Tue 20)
_y = [r for r in D[20]['alts'][0]['rows']]
_y = [R(t, p, n.replace('(How-to 22)', '(How-to 22)'), s) for (t, p, n, s) in _y if t != '20:30']
_y.append(R('20:30', 'Early night', 'Tomorrow is a slow start.'))
_strip(19)
D[19].update(cal='Tsukiji, Yokohama', title='Tsukiji market and Yokohama', rows=_y,
  sum='Moved from Tuesday to break up the city days. Breakfast at Tsukiji Outer Market in its best window, then a long Yokohama day: the waterfront, the harbour walk and Chinatown.',
  foot='Tsukiji Outer Market is open Monday. Alternative morning: Kamakura instead of the market, joining Yokohama about 14:30 (JR Shōnan-Shinjuku line, about an hour, then JR to Yokohama, about 25 minutes).')

# Tue 20: free morning, omakase or sumo, Shinjuku Gyoen, Shinjuku after dark
_strip(20)
D[20].update(cal='Omakase, Shinjuku', title='Omakase lunch, Shinjuku Gyoen, Shinjuku after dark',
  sum='The vintage stores are done, so the day opens up: a slow morning, an omakase sushi lunch, the Shinjuku Gyoen garden, a rest and pack, then Shinjuku after dark.',
  foot='Other ideas for the free time: the Kabukichō live sumo show in Shinjuku (about ¥5,000, times and booking on Klook), or teamLab if a morning turns wet (How-to 8). Pack before going out: Wednesday is the 05:55 wake for the Shinkansen.',
  rows=[
 R('09:30', 'Slow breakfast', 'Nothing booked before lunch. Laundry or a lie-in.'),
 R('11:00', 'Omakase lunch: Sushi Tokyo Ten Shibuya', 'Shibuya Stream 3F, 15 minutes on foot. Weekday lunch omakase ¥5,500, 90 minutes, counter at 11:00 or 13:30. Book on TableCheck. Card only.'),
 R('13:00', 'Shinjuku Gyoen', 'JR Yamanote to Shinjuku, then 10 minutes on foot to the Shinjuku Gate. ¥500. Open Tuesday. The big garden: French, English and Japanese sections, autumn colour starting.'),
 R('15:00', 'Back to the hotel, pack', 'Feet up. Pack the bags tonight for Wednesday.'),
 R('16:45', 'Shinjuku: the 3D cat at the east exit', 'JR Yamanote from Shibuya, about 7 minutes. The giant cat billboard at dusk.'),
 R('17:30', 'Omoide Yokochō', 'Yakitori and a drink, grazing across two or three counters before they fill (How-to 11).'),
 R('18:45', 'Godzilla head, Kabukichō and Kabukichō Tower', 'Through the underpass to the east side. Neon at full strength. Ignore touts: never follow anyone off the street into a bar.'),
 R('20:00', 'Hanazono Shrine, then Golden Gai', 'The shrine is beside Golden Gai, lit at night. In Golden Gai: cash, a cover charge, and look for English menus. Regulars-only means move on.'),
 R('21:30', 'Fukutoshin line home', 'From Shinjuku-sanchōme. Direct to Shibuya, about 5 minutes. Early night.'),
])

# How-tos
for _i, (_t, _b) in enumerate(HOWTO):
    if _t == 'Omotesando and Aoyama store hours':
        HOWTO[_i] = ('Omotesando and Aoyama store hours, Sun 18', [
         'Checked for Sunday 18: AMORE Omotesando 10:00 to 21:00, AMORE Vintage Aoyama 10:00 to 20:00, QOO 11:30 to 20:00, Brand Collect (both shops) 11:00 to 19:00, ALLU 11:00 to 20:00, Casanova Vintage 12:00 to 20:00.',
         'All within a few minutes of Omotesando Hills. Brand Collect is known for the best Chanel prices, ALLU for Hermès.',
         'Weekend afternoons are busy: go straight to the pieces you want. Physical passports for tax-free.',
         'Back to the hotel: a 10 minute taxi from Omotesando, or 20 minutes on foot down Cat Street.'])
    elif _t == 'While the stores are on, for G':
        HOWTO[_i] = ('G on his own, Sun 18', [
         'Cargo pants: UNIQLO Harajuku (B1 and 1F) and H&M share the corner building on Meiji-dōri by Harajuku Station, opposite the Takeshita Street exit. Both open 10:00 to 10:30 on Sunday. UNIQLO is the best bet for a quick, good fit.',
         'ZARA Harajuku is a few minutes south on Meiji-dōri, Jingūmae 6-31-17. Men’s is upstairs.',
         'Then walk 15 minutes down Meiji-dōri into Shibuya for Nintendo Tokyo, Shibuya Parco 6F, 10:00 to 21:00. The Pokémon Center and Capcom Store share the floor. It gets crowded after lunch.',
         'Lunch on the way: anywhere on Meiji-dōri or Cat Street, or the Parco food floor (B1).',
         'Parco to the hotel is 5 minutes on foot. Back by 14:20.'])
    elif _t == 'Omoide Yokochō, Mon 19':
        HOWTO[_i] = ('Omoide Yokochō, Tue 20', _b)
    elif _t == 'Footbaths in Yokohama, Tue 20 ideas':
        HOWTO[_i] = ('Footbaths in Yokohama, Mon 19 ideas', _b)
HOWTO.append(('Getting to Street Kart, Sun 18', [
 'Check the voucher for the shop name. Rainbow Bridge tours run from Street Kart Tokyo Bay (Shinkiba) and the Shinagawa shop.',
 'Tokyo Bay shop, Shinkiba, Kōtō: from Shibuya take the JR Saikyō line toward Shin-Kiba. Many trains run straight through on the Rinkai line; if not, change at Ōsaki to the Rinkai line. About 30 minutes. Suica works. Then about 10 minutes on foot from Shin-Kiba Station.',
 'Shinagawa shop: JR Yamanote from Shibuya to Shinagawa, about 12 minutes, then the walk shown on the voucher.',
 'Or a taxi from the hotel: 25 to 35 minutes and roughly ¥5,000 to ¥6,500 to either. Show the driver the address from the voucher.',
 'Leave the hotel by 14:45 to be there at 15:30, 30 minutes before the start.',
 'Take: physical driving licence cards, physical International Driving Permits, passports, fully closed shoes. No digital copies. Costumes are optional.',
 'If it can’t run today, the backup is Sun 25 or Mon 26 from the Hibiya hotel.']))
