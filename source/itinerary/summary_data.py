# Itinerary Summary data: one block per leg (stay). Cell = (text, state) where state is 'f' fixed/booked, 'b' to book, '' flexible.
EXTRAS = 'https://thestartupstudiodeveloper.github.io/japan-trip/extras/'
LEGS = [
 dict(pat='s', kanji='渋谷', name='Shibuya, Shinjuku and Yokohama', leg='Leg 1', dates='Sat 17 to Wed 21 Oct', nights='4 nights', hotel='seq-s', sun='Sunset 17:00',
  days=[
   ('d16', 'Fri 16', [('', ''), ('CX104 15:25 from Melbourne', 'f'), ('Hong Kong stopover, CX524 01:20', 'f')]),
   ('d17', 'Sat 17', [('Land at Narita 06:50, N\'EX to Shibuya', 'f'), ('Miyashita Park, Cat Street, Omotesando', ''), ('Shibuya Sky 16:00, dinner nearby', 'f')]),
   ('d18', 'Sun 18', [('Meiji Jingū, Harajuku', ''), ('Festival streets, Street Kart 16:00', 'f'), ('Shibuya dinner', '')]),
   ('d19', 'Mon 19', [('Omotesando vintage stores', ''), ('Lunch, rest at the hotel', ''), ('Shinjuku: Omoide Yokochō, Kabukichō, Golden Gai', '')]),
   ('d20', 'Tue 20', [('Tsukiji breakfast', ''), ('Yokohama waterfront', ''), ('Chinatown dinner, pack', '')]),
  ],
  shift=['Shibuya Sky has backup slots on Mon 19 and Tue 20 if Saturday is clouded out.', 'Kamakura can replace part of Tue 20.', 'Loosest blocks: Sat 17 afternoon and Mon 19 morning.'],
  book=[], extras=[('shibuya', 'Shibuya'), ('shinjuku', 'Shinjuku'), ('yokohama', 'Yokohama'), ('japan', 'Japan other')]),
 dict(pat='k', kanji='京都', name='Kyoto, Nara and Osaka', leg='Leg 2', dates='Wed 21 to Sat 24 Oct', nights='3 nights', hotel='seq-k', sun='Sunset 17:10',
  days=[
   ('d21', 'Wed 21', [('Nozomi 07:55 to Kyoto, bags to Crosta', 'f'), ('Nara: deer, Kasuga, Tōdai-ji', ''), ('Check in, Pontochō dinner', '')]),
   ('d22', 'Thu 22', [('Osaka Castle, Umeda Sky', ''), ('Kuromon lunch, Horie shops', ''), ('Shinsekai, Dōtonbori', '')]),
   ('d23', 'Fri 23', [('Arashiyama bamboo 07:20, Nishiki lunch', ''), ('Rest, Kiyomizu-dera 15:30', ''), ('Yasaka, Gion dinner', 'b')]),
  ],
  shift=['Thu 22 and Fri 23 can swap, but Gion dinner is planned for Friday and Thursday is Jidai Matsuri day in Kyoto.', 'The Pontochō and Gion dinners can swap.', 'Nara can finish early if you are done.'],
  book=['Gion dinner, Fri 23'], extras=[('kyoto', 'Kyoto'), ('nara', 'Nara'), ('osaka', 'Osaka')]),
 dict(pat='g', kanji='銀座', name='Tokyo: Hibiya and Ginza', leg='Leg 3', dates='Sat 24 to Tue 27 Oct', nights='3 nights', hotel='blossom', sun='Sunset 16:55',
  days=[
   ('d24', 'Sat 24', [('Fushimi Inari 07:15, check out', ''), ('Nozomi 12:01 to Tokyo, check in', 'f'), ('Odaiba fireworks, Hilton dinner', 'f')]),
   ('d25', 'Sun 25', [('East Gardens, Tokyo Station', ''), ('Ginza car-free, shopping', ''), ('Ginza dinner, Tokyo Tower lit', '')]),
   ('d26', 'Mon 26', [('teamLab Borderless 08:30', 'f'), ('Kappabashi, Sensō-ji, Skytree at dusk', ''), ('Shimbashi, pack', '')]),
  ],
  shift=['Tokyo Tower works on Sun 25 night or after teamLab on Mon 26.', 'teamLab can change date or time up to three times.', 'Yūrakuchō can take any night.'],
  book=[], extras=[('ginza', 'Ginza and east Tokyo'), ('japan', 'Japan other')]),
 dict(pat='h', kanji='香港', name='Hong Kong', leg='Leg 4', dates='Tue 27 to Sat 31 Oct', nights='3 nights, late checkout', hotel='sheraton', sun='Sunset 17:50',
  days=[
   ('d27', 'Tue 27', [('CX543 10:10 from Haneda', 'f'), ('Land 14:25, Sheraton, club lounge', 'f'), ('Aqua Luna cruise, Symphony of Lights', 'b')]),
   ('d28', 'Wed 28', [('Sheraton pool, optional', ''), ('Central, Peak Tram 15:45', 'b'), ('Big dinner in Central', 'b')]),
   ('d29', 'Thu 29', [('Ngong Ping cable car, Big Buddha', 'b'), ('Sheung Wan, Man Mo Temple', ''), ('Temple Street dinner', '')]),
   ('d30', 'Fri 30', [('Sheraton pool, yum cha', ''), ('Spare window, pack', ''), ('Ozone at sunset, CX105 00:30', 'f')]),
  ],
  shift=['Wed 28, Thu 29 and Fri 30 can swap to suit the weather. The Peak has Fast Track only Friday to Sunday.', 'Ozone can move to Thu 29, freeing Friday evening.'],
  book=['Aqua Luna, Tue 27', 'Peak Tram, Wed 28', 'Big dinner, Wed 28', 'Ngong Ping, Thu 29', 'Ozone, Fri 30'], extras=[('hk', 'Hong Kong')]),
]
