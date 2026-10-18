# Sun 18 rework (sent 07:22): Tomigaya breakfast, park, shrine, Harajuku, vintage. Cynthia's shopping afternoon, G's options.
# Yokohama moves to Mon 19, Shinjuku plus new free time to Tue 20. Shibuya Sky is done, so the tabs go.
D[18].update(cal='Meiji, shopping, Street Kart', title='Premier Mai, Meiji Jingū, shopping, Street Kart')
D[18]['sum'] = "Breakfast in Tomigaya, through Yoyogi Park to Meiji Jingū, Takeshita Street, then Cynthia's shopping afternoon in Omotesando while G does Harajuku and Nintendo. Street Kart at golden hour, then ramen and a foot massage."
D[18]['rows'] = [
 R('08:00', 'Breakfast at Premier Mai', 'The hidden café in Tomigaya, no sign, up the stairs beside the Irish pub. Thick toast and omelette toast. A hit (How-to 26).'),
 R('09:30', 'Yoyogi Park', 'Five minutes away. Walk through to the Harajuku gate. Sunday rockabilly dancers near that entrance.'),
 R('10:15', 'Meiji Jingū', 'Forest paths and the big torii. About 45 minutes.'),
 R('11:00', 'Takeshita Street', 'Out of the Harajuku gate and across the road. Walk it once together.'),
 R('11:30', "Cynthia's shopping afternoon", 'Pre-owned, not vintage, in order back towards the hotel: Brand Collect Omotesando 2, Kindal Harajuku, RAGTAG Harajuku, ALLU, then Brand Collect Shibuya by the hotel. Passport for tax-free. Back by 14:20.'),
 R('11:30', "G's free time", 'Down Cat Street to Jinnan, about 15 minutes. Book tonight\'s foot massages at Mominotakumi (9F), then ZARA Shibuya Kōen-dōri on the same block, Nintendo Tokyo in Shibuya Parco 6F, and H&M Udagawachō (menswear 4F) beside MEGA Don Quijote. All within 5 minutes of each other. Back by 14:20 (How-to 10).'),
 R('14:20', 'Back at the hotel', 'Fully closed shoes. Physical licence cards, physical International Driving Permits, passports. No digital copies.'),
 R('14:45', 'Leave for Street Kart', 'Check which shop the voucher names (How-to 25). Aim to arrive by 15:30.'),
 R('16:00', 'Street Kart, Rainbow Bridge route', 'About two hours. Golden hour over the bay.', B),
 R('18:30', 'Back to the hotel, shower', 'Same way back, or a taxi.'),
 R('19:30', 'Dinner near Jinnan', 'Tonkatsu Kagurazaka Sakura Jinnan, 2 minutes from the massage, to 22:00. Or Gyukatsu Motomura or Tonkatsu Nagi.'),
 R('20:30', 'Foot and leg massage, Mominotakumi', 'SUNX Building 9F, Jinnan. Booked for 2. Then Yakitori Toriton, 3 minutes away and open late, or Ichiran in the same block.', B),
]
D[18].pop('foot', None)

def _strip(d):
    for k in ('alts', 'tabs', 'tablabel', 'group'): D[d].pop(k, None)

# Mon 19: Kamakura morning, then Yokohama (changed 18 Oct 15:14)
_strip(19)
D[19].update(cal='Kamakura, Yokohama', title='Kamakura, then Yokohama',
  sum='The coast, temples and the Great Buddha in Kamakura in the morning, then the Yokohama waterfront, the harbour walk at dusk and dinner in Chinatown. A long day out: it is fine to drop the Air Cabin if tired.',
  foot='Checked for Monday: Tsurugaoka Hachimangū 06:00 to 20:00, Hase-dera 08:00 to 17:00 (¥400), the Great Buddha at Kōtoku-in 08:00 to 16:45 (¥300), Yokohama Air Cabin 10:00 to 21:00.',
  rows=[
 R('07:45', 'JR Shōnan-Shinjuku line to Kamakura', 'From Shibuya, direct, about an hour. Suica works.'),
 R('09:00', 'Tsurugaoka Hachimangū, Komachi-dōri', 'The shrine up the long approach, then the snack and shop street back to the station.'),
 R('10:45', 'Enoden to Hase', 'The little seaside train, about 5 minutes.'),
 R('11:00', 'Hase-dera, then the Great Buddha', 'Hase-dera on the hillside with sea views, then 5 minutes on foot to the Great Buddha.'),
 R('12:30', 'Lunch in Hase or Kamakura', ''),
 R('14:00', 'JR to Yokohama', 'About 25 minutes. Change to Sakuragichō.'),
 R('14:45', 'Sakuragichō, Air Cabin, Minato Mirai waterfront', 'The cable car across the harbour, Red Brick Warehouses, the skyline.'),
 R('16:30', 'Harbour walk to Chinatown, dinner', 'At dusk. Idea: the footbath at The Wharf House on the way (How-to 22). Dinner from 17:30.'),
 R('19:30', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change.'),
])

# Tue 20: free morning, omakase or sumo, Shinjuku Gyoen, Shinjuku after dark
_strip(20)
D[20].update(cal='Tsukiji, omakase, Shinjuku', title='Tsukiji early, omakase lunch, Shinjuku after dark',
  sum='Tsukiji Outer Market first thing, back to the hotel to rest and pack, then the booked omakase lunch in Shinjuku, the department stores and Shinjuku after dark.',
  foot='Tsukiji Outer Market is closed Sundays, holidays and some Wednesdays, so Tuesday is good. Keep the market to small bites: lunch is the full omakase. Optional after lunch: Shinjuku Gyoen for an hour (last entry 16:00, ¥500), or the Kabukichō sumo show (times on Klook). Wednesday is the 05:55 wake.',
  rows=[
 R('07:30', 'Leave the hotel for Tsukiji', 'Ginza line to Ginza, then the Hibiya line two stops to Tsukiji. About 30 minutes, at the commuter peak.'),
 R('08:00', 'Tsukiji Outer Market breakfast', 'The best window, before the 10:00 rush. Small bites: tamagoyaki, grilled scallop, strawberry daifuku. Then Namiyoke shrine. Bring cash.'),
 R('09:45', 'Back to Shibuya', 'Hibiya line to Ginza, then the Ginza line. About 30 minutes.'),
 R('10:15', 'Hotel: rest, shower, pack', 'Pack the bags for Wednesday now.'),
 R('12:50', 'JR Yamanote to Shinjuku', 'About 7 minutes. Use the New South exit for NEWoMan.'),
 R('13:30', 'Omakase lunch: Sushi Tokyo Ten Shinjuku', 'NEWoMan Shinjuku 2F. Full omakase course, booked. About 90 minutes. Card only.', B),
 R('15:00', 'Department stores', 'NEWoMan and Lumine on the spot, Takashimaya across the south deck, then Isetan and Isetan Men\'s, about 10 minutes east. The Isetan food hall in the basement. Passports for tax-free.'),
 R('17:30', 'Shinjuku: the 3D cat at the east exit', 'Three minutes from Isetan. The giant cat billboard after dark.'),
 R('18:30', 'Omoide Yokochō', 'Light yakitori and a drink after the big lunch, grazing across a couple of counters (How-to 11).'),
 R('19:30', 'Godzilla head, Kabukichō and Kabukichō Tower', 'Through the underpass to the east side. Ignore touts: never follow anyone off the street into a bar.'),
 R('20:30', 'Hanazono Shrine, then Golden Gai', 'The shrine is beside Golden Gai, lit at night. In Golden Gai: cash, a cover charge, look for English menus. Regulars-only means move on.'),
 R('21:45', 'Fukutoshin line home', 'From Shinjuku-sanchōme, direct to Shibuya, about 5 minutes. Early night for the 05:55 wake.'),
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
         'ZARA Harajuku is closed. Use ZARA Shibuya Kōen-dōri instead, 1-22-4 Jinnan, 10:30 to 22:00.',
         'Walk down Cat Street from Omotesando into Jinnan, about 15 minutes.',
         'First stop: Mominotakumi, 9F, same block as ZARA and Ichiran. Book two foot massages for about 19:45 tonight. Open to 23:00, +81 3-6416-0995.',
         'ZARA Kōen-dōri for cargo pants, four floors.',
         'Nintendo Tokyo, Shibuya Parco 6F, 3 minutes away, 10:00 to 21:00. The Pokémon Center and Capcom Store share the floor.',
         'H&M Udagawachō, beside MEGA Don Quijote, 10:00 to 22:00. Menswear is on 4F.',
         'H&M to the hotel is about 8 minutes on foot. Back by 14:20.'])
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

# Shibuya Sky is done: drop the 'Which day is Shibuya Sky?' section
D[17]['sky'] = False

HOWTO.append(('Finding Premier Mai, Sun 18', [
 'Address: 1-6-10 Tomigaya, Yoyogi Park Building, 2F. About a minute from Yoyogi-Kōen Station (Chiyoda line) and Yoyogi-Hachiman Station.',
 'There is no sign on the street. The building looks ordinary, with an Irish pub on the ground floor.',
 'The entrance is a narrow staircase at the side of the pub. Go up to the 2nd floor. If there is a queue, it waits on those stairs: join the end.',
 'The door at the top has no sign either. Open it and you are in.',
 'Open 08:00 to 17:00 on Sunday, closed Wednesday. No booking. Order the thick toast or the omelette toast, and an oat latte.',
 'No closure notice found for today. To be sure, check the Instagram stories at @premiermai_tokyo before walking over.',
 'i2 is the backup, 3 minutes away at 1-14-13 Tomigaya, RayQuon Okushibu 1F.']))
HOWTO.append(('Kamakura on the day, Mon 19', [
 'Shibuya to Kamakura: JR Shōnan-Shinjuku line, platforms 3 and 4 at JR Shibuya. Board a train bound for Zushi (逗子): it runs straight to Kamakura in about an hour, around ¥950 on Suica.',
 'If the next train says Odawara (小田原) or Hiratsuka, take it anyway and change at Ōfuna to the Yokosuka line (blue and cream), two stops to Kamakura.',
 'Kamakura Station east exit: walk Wakamiya-ōji or Komachi-dōri up to Tsurugaoka Hachimangū, about 10 minutes. Back to the station along Komachi-dōri for snacks.',
 'Enoden: from the Enoden platform on the west side of Kamakura Station, 3 stops to Hase, about 5 minutes, Suica works. Sit on the left for glimpses of the sea.',
 'Hase-dera: 5 minutes from Hase Station, open 08:00 to 17:00, ¥400. The Great Buddha (Kōtoku-in): 5 minutes further up the road, open 08:00 to 16:45, ¥300.',
 'The beach: Yuigahama is about 10 minutes downhill from Hase Station. Free, open sand, black and soft. Showers only in summer, so towels are not needed unless you paddle. Watch food: the kites (hawks) swoop.',
 'Mt Fuji: possible on a clear day, never guaranteed, and best before midday. The best spot is Inamuragasaki, two Enoden stops past Hase, then 5 minutes to the cape park. From Yuigahama look west along the coast.',
 'Kamakura to Yokohama: Enoden back to Kamakura, then the JR Yokosuka line to Yokohama, about 25 minutes. Change to the JR Negishi line (light blue), two stops to Sakuragichō.']))
HOWTO.append(('Yokohama on the day, Mon 19', [
 'Sakuragichō Station: the Air Cabin is right outside the east exit. One way ¥1,000, about 5 minutes over the water to Unga Park, beside Cosmo World. Open 10:00 to 21:00.',
 'Cosmo World: free to walk in, pay per ride at the ticket machines. Monday 11:00 to 20:00, closed Thursdays. Cash only.',
 'Diving Coaster Vanish: the one that dives into the pool and disappears into a tunnel. About ¥900 to ¥1,000 each. Short: the fast part is about 30 seconds. Loose items go in the lockers first, staff check pockets.',
 'Cosmo Clock 21: the big ferris wheel, about 15 minutes round. Best at sunset, around 17:05.',
 'Harbour walk: Red Brick Warehouses, then along Yamashita Park to Chinatown, about 30 minutes at an easy pace.',
 'Foot massage after dinner, in Chinatown: Kyūryū SPA (Kirin Kowloon), 2F on a pedestrian lane, 10:00 to 22:00, foot bath, tea and a full 60-minute foot course, card OK. Or Kaisokukan, 10:00 to 23:00, call +81 90-9375-5588.',
 'Japanese dry head spa: Tenkū no Ryōiki, Kannai, 10 minutes walk from Chinatown, 11:00 to 22:00, rated 4.9, couples course. Book ahead by phone +81 70-3179-7818 or online.',
 'Home: Motomachi-Chūkagai Station (Minatomirai line) at the Chinatown end. Trains run through on the Tōkyū Tōyoko line to Shibuya, about 40 minutes on an express, no change.']))
_m = D[19]['rows']
_r = _m[_row(19, '07:45')]; _m[_row(19, '07:45')] = R(_r[0], _r[1], 'From Shibuya, a train bound for Zushi runs direct, about an hour. Suica works (How-to 27).', *_r[3:])
_r = _m[_row(19, '14:00')]; _m[_row(19, '14:00')] = R(_r[0], _r[1], 'About 25 minutes, then change to Sakuragichō (How-to 27). Yokohama on the day: How-to 28.', *_r[3:])
# Mon 19 final shape, 18 Oct 23:00: beach, Vanish coaster, foot massage after dinner
D[19].update(
  sum='Kamakura in the morning: the shrine, Hase-dera and the Great Buddha, then lunch and a walk on Yuigahama beach. Yokohama in the afternoon: the Air Cabin, the Vanish coaster and the ferris wheel at sunset, the harbour walk, dinner in Chinatown and a foot massage before the train home.',
  foot='Checked for Monday: Tsurugaoka Hachimangū 06:00 to 20:00, Hase-dera 08:00 to 17:00 (¥400), the Great Buddha 08:00 to 16:45 (¥300), Air Cabin 10:00 to 21:00, Cosmo World 11:00 to 20:00 (closed Thursdays, cash only), Kyūryū SPA 10:00 to 22:00. Mt Fuji is never guaranteed: clear mornings are best.')
D[19]['rows'] = [
 R('07:45', 'JR Shōnan-Shinjuku line to Kamakura', 'Board a train bound for Zushi: direct, about an hour. If it says Odawara, change at Ōfuna (How-to 27).'),
 R('09:00', 'Tsurugaoka Hachimangū, Komachi-dōri', 'The shrine up the long approach, then the snack and shop street back to the station.'),
 R('10:30', 'Enoden to Hase', 'The little seaside train, 3 stops, about 5 minutes. Sit on the left.'),
 R('10:40', 'Hase-dera, then the Great Buddha', 'Hase-dera on the hillside with sea views, then 5 minutes on foot to the Great Buddha.'),
 R('12:15', 'Lunch, then a look at Yuigahama', 'About 10 minutes downhill from Hase. A walk along the sand, no lying about. If it is clear, look west for Mt Fuji, or ride the Enoden two stops to Inamuragasaki for the classic view (How-to 27).'),
 R('14:00', 'To Yokohama', 'Enoden back to Kamakura, JR Yokosuka line to Yokohama, about 25 minutes, then the Negishi line two stops to Sakuragichō (How-to 27).'),
 R('15:00', 'Air Cabin across the harbour', 'Right outside Sakuragichō east exit. ¥1,000 one way, about 5 minutes. Lands beside Cosmo World.'),
 R('15:15', 'Cosmo World: Vanish coaster, ferris wheel', 'The Diving Coaster Vanish plunges into the pool and into a tunnel, about ¥1,000 each, cash only, pockets into the lockers. Cosmo Clock 21 at sunset, about 17:05 (How-to 28).'),
 R('17:00', 'Harbour walk to Chinatown', 'Red Brick Warehouses and Yamashita Park at dusk, about 30 minutes.'),
 R('17:45', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:00', 'Foot massage, Kyūryū SPA', 'Chinatown, 2F on a pedestrian lane. Foot bath, tea and a 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00 (How-to 28).'),
 R('20:15', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change. Back about 21:00.'),
]
# Mon 19 later start, 18 Oct 23:17: Roastery breakfast, pancakes in Hase
D[19].update(
  sum='A later start: breakfast at the Starbucks Reserve Roastery in Nakameguro, then Kamakura: the shrine, fluffy pancakes with a sea view in Hase, Hase-dera, the Great Buddha and a walk on the beach. Yokohama from late afternoon: the Air Cabin, the Vanish coaster, the ferris wheel at sunset, the harbour walk, dinner in Chinatown and a foot massage.',
  foot='Checked for Monday: Roastery 08:00 to 22:00, Tsurugaoka Hachimangū 06:00 to 20:00, A la Mode Kamakura 10:00 to 18:30 (closed Wednesday and Saturday), Hase-dera 08:00 to 17:00 (¥400), the Great Buddha 08:00 to 16:45 (¥300), Air Cabin 10:00 to 21:00, Cosmo World 11:00 to 20:00 (cash only), Kyūryū SPA 10:00 to 22:00. Mt Fuji is unlikely by afternoon: a bonus if you see it.')
D[19]['rows'] = [
 R('07:45', 'Taxi to the Starbucks Reserve Roastery', 'About 10 minutes from the hotel. Opens 08:00 on Mondays.'),
 R('08:00', 'Breakfast at the Roastery', 'Four floors of coffee and the Princi bakery. Keep it light: pancakes are lunch.'),
 R('09:15', 'Nakameguro to Kamakura', 'Walk 10 minutes to Nakameguro Station. Tōkyū Tōyoko line to Musashi-Kosugi, then the JR Yokosuka line direct to Kamakura. About an hour, Suica works (How-to 27).'),
 R('10:30', 'Tsurugaoka Hachimangū, Komachi-dōri', 'The shrine up the long approach, then the snack and shop street back to the station.'),
 R('11:45', 'Enoden to Hase', 'The little seaside train, 3 stops, about 5 minutes. Sit on the left.'),
 R('12:00', 'Fluffy pancakes, A la Mode Kamakura', 'In Hase, looking out at the sea. Fluffy pancakes with Greek yoghurt ice cream, fruit and real maple syrup. Open from 10:00.'),
 R('13:00', 'Hase-dera, then the Great Buddha', 'Hase-dera on the hillside with sea views, then 5 minutes on foot to the Great Buddha. Last entry 16:45.'),
 R('14:15', 'A walk on Yuigahama', 'About 10 minutes downhill. A look along the sand towards Enoshima.'),
 R('14:45', 'To Yokohama', 'Enoden back to Kamakura, JR Yokosuka line to Yokohama, about 25 minutes, then the Negishi line two stops to Sakuragichō (How-to 27).'),
 R('15:45', 'Air Cabin, then Cosmo World', 'Air Cabin from outside Sakuragichō east exit, ¥1,000, 5 minutes. The Diving Coaster Vanish, about ¥1,000 each, cash only, pockets into the lockers. Cosmo Clock 21 at sunset, about 17:05 (How-to 28).'),
 R('17:30', 'Harbour walk to Chinatown', 'Red Brick Warehouses and Yamashita Park at dusk, about 30 minutes.'),
 R('18:15', 'Dinner in Chinatown', 'Walk the lanes and pick. Steamed buns from the street stalls as a starter.'),
 R('19:30', 'Foot massage, Kyūryū SPA', 'Chinatown, 2F on a pedestrian lane. Foot bath, tea and a 60-minute foot course. Open to 22:00, card OK. Backup: Kaisokukan, open to 23:00 (How-to 28).'),
 R('20:45', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change. Back about 21:30.'),
]
_i = [k for k, h in enumerate(HOWTO) if h[0] == 'Kamakura on the day, Mon 19'][0]
_b = list(HOWTO[_i][1])
_b[0] = 'Roastery to Kamakura: walk 10 minutes to Nakameguro Station. Tōkyū Tōyoko line (any train) to Musashi-Kosugi, then the JR Yokosuka line (blue and cream) bound for Zushi or Kurihama, direct to Kamakura. About an hour in all, Suica works.'
_b[1] = 'If the JR train at Musashi-Kosugi is not a Yokosuka line one, ride to Yokohama and change there to the Yokosuka line, 25 minutes to Kamakura.'
_b.insert(5, 'Pancakes: A la Mode Kamakura, 2-7-15 Hase, about 5 minutes from Hase Station towards the sea. Open 10:00 to 18:30, closed Wednesday and Saturday.')
HOWTO[_i] = (HOWTO[_i][0], _b)
# Mon 19 06:05: Meguro River walk after the Roastery
_m = D[19]['rows']
_m[_row(19, '09:15')] = R('09:00', 'Meguro River walk to Nakameguro', 'The Roastery sits on the river. Follow the river path downstream, the way the water flows, under the cherry trees, past the cafés and small boutiques, about 15 to 20 minutes at an easy pace to Nakameguro Station. Then the Tōkyū Tōyoko line to Musashi-Kosugi and the JR Yokosuka line direct to Kamakura, about an hour (How-to 27).')
_m[_row(19, '08:00')] = R('08:00', 'Breakfast at the Roastery', 'Four floors of coffee and the Princi bakery. Keep it light: pancakes are lunch. Away by 09:00.')
