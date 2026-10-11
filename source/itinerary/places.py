# Interactive cards. One source for the online page. The PDF ignores them.
# P(key, aliases, name, local script, what it is, good to know, maps and photo query, days=None)
# Aliases are written as they appear in the built HTML (apostrophes as &#x27;, ampersands as &amp;).
PLACES = []
def P(key, aliases, name, local, what, tip, q, days=None):
    PLACES.append(dict(key=key, aliases=aliases, n=name, l=local, w=what, t=tip, m=q, days=days))

# Text that must never be linked, usually because it contains a shorter place name.
IGNORE = ['Asakusa line', 'Ginza line', 'JR Nara line', 'Kiyomizu-Gojō', 'Kiyomizu-Gojo', 'Motomachi-Chūkagai', 'Higashi-Umeda', 'Central Pier',
          'Shinjuku-sanchōme', 'Tsim Sha Tsui Pier 1', 'Kowloon Station', 'Hong Kong Station', 'Hong Kong Island', 'Hong Kong dollars',
          'Peak Galleria', 'Saga-Arashiyama', 'JR Sagano line', 'Midōsuji line', 'Tanimachi line', 'Ōedo line', 'Fukutoshin line', 'Tōyoko line', 'Osaka Metro', 'Osaka Station', 'JR Shōnan-Shinjuku line', 'Kowloon and Hong Kong Island', 'Hong Kong Station']

# ---------------- hotels, airports, trains ----------------
P('seq-s', ['Sequence Miyashita Park', 'bags to the hotel'], 'Sequence Miyashita Park', 'シークエンス ミヤシタパーク',
  'Your Shibuya hotel for the first four nights. It is the tower at the northern end of the Miyashita Park building, a seven minute walk from Shibuya Station. The lobby and cafe are on the 4th floor, level with the rooftop park.',
  'Booked direct by Cynthia. Standard check-in is 17:00 and checkout is 14:00, later than most hotels at both ends.', 'sequence MIYASHITA PARK hotel Shibuya')
P('seq-k', ['sequence KYOTO GOJO'], 'sequence KYOTO GOJO', 'シークエンス 京都五条',
  'Your Kyoto hotel for three nights, at the corner of Karasuma and Gojō streets in central Kyoto. Gojō subway station is about three minutes away, one stop north of Kyoto Station.',
  'Booked on Booking.com by G. Same late check-in and checkout as the Shibuya sequence hotel. The address is Gojō Karasuma-chō 409, Shimogyō-ku.', 'sequence KYOTO GOJO hotel')
P('blossom', ['Hotel The Blossom Hibiya', 'the Blossom', 'The Blossom'], 'The Blossom Hibiya', 'THE BLOSSOM HIBIYA',
  'Your second Tokyo hotel, for three nights. It occupies the upper floors of a tower in Shimbashi, so the rooms look out over the city. Ginza, Hibiya and Shimbashi Station are all within a ten minute walk.',
  'Booked on Booking.com by G. Check-in is from 15:00. There is a small guest laundry.', 'THE BLOSSOM HIBIYA hotel Tokyo')
P('sheraton', ['Sheraton Hong Kong Hotel &amp; Towers', 'the Sheraton', 'Sheraton'], 'Sheraton Hong Kong Hotel & Towers', '香港喜來登酒店',
  'Your Hong Kong hotel for three nights, at the foot of Nathan Road in Tsim Sha Tsui. It faces Victoria Harbour, with the Star Ferry, the promenade and the MTR a few minutes away. You have a harbour view room with club lounge access, and there is a rooftop pool.',
  'Booked on Agoda by Cynthia. Late checkout on Friday 30 is confirmed to 18:00.', 'Sheraton Hong Kong Hotel & Towers Tsim Sha Tsui')
P('lounge', ['Club lounge', 'club lounge', 'Lounge breakfast', 'lounge breakfast'], 'Sheraton club lounge', '行政酒廊',
  'A private lounge for guests in club rooms, high up in the hotel with harbour views. It serves breakfast in the morning and drinks with small plates in the early evening, all included in your room rate.',
  'Ask for the exact hours at check-in.', 'Sheraton Hong Kong Hotel Towers club lounge')
P('narita', ['Land at Narita', 'at Narita'], 'Narita International Airport', '成田国際空港',
  'Tokyo\'s main international airport, about 60 kilometres east of the city. After landing you pass immigration, collect bags and clear customs, which usually takes about an hour. The train station is in the basement of the terminal.',
  'Have the Visit Japan Web QR codes open on your phone before you reach immigration.', 'Narita International Airport')
P('nex', ['Narita Express'], 'Narita Express (N\'EX)', '成田エクスプレス',
  'The airport express train from Narita into central Tokyo. Red, white and black, with reserved seats and luggage racks at the end of each car. It is the simplest way in after a long flight: one seat, no changes, about 80 minutes to Shibuya.',
  'Not every service stops at Shibuya, so check the ticket before boarding.', 'Narita Express train')
P('haneda', ['Haneda Terminal 3', 'Haneda'], 'Haneda Airport Terminal 3', '羽田空港 第3ターミナル',
  'Tokyo\'s closer airport, on the bay about 25 minutes from Shimbashi by direct train. Terminal 3 is the international terminal. It is compact and quick to get through, with an Edo-style shopping street upstairs before security.',
  'Spend leftover yen and the Suica balance airside.', 'Haneda Airport Terminal 3')
P('hkia', ['Land in Hong Kong'], 'Hong Kong International Airport', '香港國際機場',
  'Hong Kong\'s airport sits on reclaimed land off Lantau Island, about 35 kilometres from Tsim Sha Tsui. Immigration, bags and customs usually take 45 to 60 minutes. Taxis, the Airport Express train and buses all leave from just outside arrivals.',
  'No arrival card is needed. Keep the small landing slip with your passport.', 'Hong Kong International Airport')
P('redtaxi', ['Red urban taxi', 'Red taxis', 'red taxi'], 'Hong Kong red taxi', '市區的士',
  'Hong Kong taxis are colour coded by area. Red ones serve Kowloon and Hong Kong Island, which is everywhere you are going. They are metered, cheap by Australian standards, and charge small extras for bags and tunnel tolls.',
  'Many still prefer cash. Have the hotel name in Chinese ready to show.', 'Hong Kong red taxi')
P('aex', ['Airport Express'], 'Airport Express', '機場快綫',
  'The fast train from the airport into the city. It reaches Kowloon Station in about 22 minutes, and from there the Sheraton is a short taxi ride.', 'For two people with bags, a taxi all the way costs about the same.', 'Hong Kong Airport Express train')
P('shinkansen', ['Nozomi 13', 'Nozomi 16', 'Shinkansen', 'Green Car'], 'Nozomi Shinkansen', '新幹線 のぞみ',
  'The fastest bullet train on the Tokyo to Kyoto line, running at up to 285 km/h. The trip takes about two hours and ten minutes. You are in the Green Car, which is first class, with a reserved space behind the last row for large suitcases.',
  'Trains leave exactly on time and stop for about a minute. Be on the platform at your car number ten minutes early.', 'Nozomi Shinkansen N700S')
P('fuji', ['Fuji'], 'Mount Fuji from the train', '富士山',
  'Japan\'s highest mountain, a near perfect cone, visible from the Shinkansen for a few minutes about 40 to 45 minutes out of Tokyo. Seat D is the Fuji side in both directions.',
  'It is often hidden by cloud, especially later in the day. Morning gives the best odds.', 'Mount Fuji from Shinkansen')
P('ekiben', ['ekiben', 'Ekiben'], 'Ekiben', '駅弁',
  'Station lunch boxes, sold at stalls inside the Shinkansen gates. Each is a neatly packed meal of rice with fish, meat or vegetables, often a regional speciality, made to be eaten at your seat.',
  'Eating on the Shinkansen is normal and expected. Buy drinks at the same stall.', 'ekiben station bento Japan')
P('shinagawa', ['Shinagawa'], 'Shinagawa Station', '品川駅',
  'A major station in south Tokyo and the Shinkansen stop closest to Shibuya. Boarding here saves going into Tokyo Station. The Kōnan exit, on the east side, is the one nearest the Shinkansen gates.',
  'The ekiben and coffee stalls are inside the Shinkansen gates.', 'Shinagawa Station Shinkansen')
P('yasaka-pagoda', ['Yasaka Pagoda'], 'Yasaka Pagoda', '八坂の塔',
  'A five storey wooden pagoda, 46 metres tall, rising above the roofs of the old lanes below Kiyomizu-dera. Its proper name is Hōkan-ji. The view up the sloping lane towards it is the postcard picture of old Kyoto. It is a different place from Yasaka Shrine, ten minutes north.',
  'The best view is from Yasaka-dōri, the lane running downhill to the west of it.', 'Yasaka Pagoda Hokanji Kyoto sunset')
P('shirakawa', ['Shirakawa canal', 'Shirakawa'], 'Shirakawa', '祇園白川',
  'A willow-lined canal on the north side of Gion, with old teahouses and restaurants backing onto the water and a small stone bridge. The prettiest street in the district, and quiet after dark.', '', 'Gion Shirakawa canal night')
P('kiyamachi', ['Kiyamachi-dōri'], 'Kiyamachi-dōri', '木屋町通',
  'A street running beside the narrow Takase canal, one lane west of Pontochō. Trees over the water, bars and small restaurants along it. Livelier and cheaper than Pontochō.', '', 'Kiyamachi street Takase canal Kyoto')
P('kamo', ['Kamo River'], 'Kamo River', '鴨川',
  'The river through the middle of Kyoto. People sit along its stone banks in the evening, with the lit backs of the Pontochō restaurants on one side.', '', 'Kamo River Kyoto night Shijo')
P('shijo-bridge', ['Shijō Bridge'], 'Shijō Bridge', '四条大橋',
  'The main bridge over the Kamo River, linking Pontochō and the shopping streets on the west bank to Gion on the east.', '', 'Shijo Ohashi Bridge Kyoto night')
P('teramachi', ['Teramachi arcades'], 'Teramachi and Shinkyōgoku arcades', '寺町・新京極',
  'Two long covered shopping streets side by side in the centre of Kyoto, a few minutes from Pontochō. Souvenirs, clothes, tea, sweets and game arcades. Open into the evening.', '', 'Teramachi Shinkyogoku shopping arcade Kyoto')
P('aritsugu', ['Aritsugu'], 'Aritsugu', '有次',
  'A knife and cookware maker founded in 1560 as swordsmiths, now with its shop at the east end of Nishiki Market. Hand-forged kitchen knives, engraved with your name while you wait.',
  'Knives fly in checked bags only.', 'Aritsugu knife shop Nishiki Market')
P('kyoto-tower', ['Kyoto Tower'], 'Kyoto Tower', '京都タワー',
  'A white 131 metre observation tower from 1964, standing opposite the north side of Kyoto Station. The tallest structure in the city.', '', 'Kyoto Tower night')
P('kyoto-st-building', ['Kyoto Station building', 'Sky Garden'], 'Kyoto Station building', '京都駅ビル',
  'The station is a sight in itself. A grand staircase climbs eleven storeys through the open hall and plays an LED light show after dark. At the top is a free open-air garden with views over the city and across to Kyoto Tower.', '', 'Kyoto Station grand staircase illumination')
P('kofukuji', ['Kōfuku-ji'], 'Kōfuku-ji', '興福寺',
  'A temple founded in 710 at the edge of Nara Park, once the family temple of the most powerful clan in Japan. You walk through its open grounds on the way to the deer. Its five storey pagoda, the second tallest in Japan, is fully covered for restoration from 2023 until March 2034, so there is nothing of it to see.',
  'The grounds are free. The octagonal halls and the rebuilt Central Golden Hall are still visible.', 'Kofukuji Temple Nara')
P('nakatanido', ['Nakatanidō'], 'Nakatanidō', '中谷堂',
  'A small sweet shop on Sanjō-dōri famous for pounding mochi by hand at startling speed, two men with mallets and a third turning the dough between blows. The result is yomogi mochi, a soft green rice cake filled with red bean, sold warm.',
  'The pounding happens in bursts through the day, not on a timetable. A crowd gathers when it starts.', 'Nakatanidou mochi pounding Nara')
P('deer-crackers', ['Deer crackers'], 'Deer crackers', '鹿せんべい',
  'Shika senbei: thin rice bran wafers sold in paper-wrapped stacks at stalls across Nara Park, the only thing you should feed the deer. Many deer bow for one.',
  'Show empty hands when you run out. Deer will nip at pockets, maps and bags.', 'Nara deer shika senbei crackers')
P('nandaimon', ['Nandaimon gate'], 'Nandaimon', '南大門',
  'The Great South Gate of Tōdai-ji, a huge wooden gate from 1203 guarded by two fierce eight metre statues. Deer gather around it.', '', 'Nandaimon Gate Todaiji Nara')
P('kakinoha', ['Kakinoha sushi'], 'Kakinoha sushi', '柿の葉寿司',
  'Nara\'s own sushi: small blocks of rice topped with cured mackerel or salmon, pressed and wrapped in a persimmon leaf. It was made to travel, so it is sold boxed and ready to eat. Unwrap the leaf, do not eat it.',
  'Sold at shops along Sanjō-dōri and at the station. Eat it before you reach the deer.', 'kakinoha sushi Nara persimmon leaf')
P('nara-bus', ['loop bus'], 'Nara city loop bus', 'ぐるっとバス・市内循環',
  'City buses circle between the park and both stations every few minutes. From the Tōdai-ji Daibutsuden stop on the main road it is about ten minutes to JR Nara Station. A flat fare, and Suica works.', '', 'Nara city loop bus Todaiji Daibutsuden stop')
P('go-app', ['GO app'], 'GO taxi app', 'GO タクシーアプリ',
  'Japan\'s main taxi-hailing app, covering Tokyo, Kyoto, Osaka and Nara. It calls a licensed taxi to your pin and shows the fare estimate. It takes foreign cards, or you can pay the driver.',
  'Install it and add a card before you fly. It needs a phone number to register.', 'GO taxi app Japan')
P('crosta', ['Crosta Kyoto'], 'Crosta Kyoto', 'Crosta京都',
  'The staffed baggage counter at Kyoto Station, on level B1 directly below the JR Central Gate on the north side. It stores bags for the day and also delivers them to hotels in the city. This is where the suitcases go while you are in Nara.',
  'Open 08:00 to 20:00. ¥1,000 per bag per day. Keep the receipt. Take passports and valuables out first.', 'Crosta Kyoto baggage counter Kyoto Station B1')
P('mel', ['Melbourne Airport'], 'Melbourne Airport', 'MEL',
  'Tullamarine. International flights leave from Terminal 2, in the middle of the terminal building. Terminal 4 is at the southern end, about ten minutes on foot from Terminal 2 along the front of the building.',
  'You are being dropped at the Terminal 4 drop-off and walking to Terminal 2.', 'Melbourne Airport Terminal 2 international departures')
P('plaza-premium', ['Plaza Premium Lounge'], 'Plaza Premium Lounge, Hong Kong', '環亞機場貴賓室',
  'A pay-to-enter lounge open to any passenger, on Level 6 of the departures level in Terminal 1, near Gate 1. Hot food, drinks, seats with power, and private shower rooms. It is open 24 hours, which matters for a stopover that runs past midnight.',
  'Book online at least an hour ahead, from about HK$650 each. Check whether showers are included in the rate you book.', 'Plaza Premium Lounge Hong Kong Airport Gate 1')
P('hkg-transfer', ['Land in Hong Kong, Terminal 1'], 'Hong Kong transfer', '轉機',
  'Connecting passengers at Hong Kong follow the Transfer signs after leaving the aircraft, not Arrivals. You pass a security check and come out in the departures hall without going through immigration. Bags tagged through at Melbourne go to the next flight on their own.',
  'Have both boarding passes ready. Gates numbered above 200 are reached by a short train.', 'Hong Kong Airport transfer E1 E2')
P('parco', ['Shibuya Parco'], 'Shibuya Parco', '渋谷パルコ',
  'A fashion and culture department store in central Shibuya. The sixth floor is the draw: Nintendo Tokyo, the Pokémon Center, the Capcom Store and the Jump Shop side by side. There is a rooftop terrace and a floor of restaurants.', 'Nintendo Tokyo can have a queue to enter on weekends.', 'Shibuya Parco Nintendo Tokyo')
P('harakado', ['Harakado'], 'Harakado', 'ハラカド',
  'A shopping building opened in 2024 at the corner of Omotesando and Meiji-dōri, opposite Tokyu Plaza. Design shops, cafés and restaurants, a rooftop, and Kosugi-yu Harajuku, a branch of a famous old Tokyo public bath, in the basement.', 'The bath is a proper sento: wash first, no swimwear.', 'Harakado Harajuku Kosugi-yu')
P('tokyu-plaza', ['Tokyu Plaza Omotesando'], 'Tokyu Plaza Omotesando', '東急プラザ表参道「オモカド」',
  'A fashion building at the Harajuku crossing, known for its entrance: an escalator climbing through a tunnel of angled mirrors. On top is a free rooftop terrace planted with trees.', '', 'Tokyu Plaza Omotesando mirror entrance')
P('ura-harajuku', ['Ura-Harajuku', 'the back lanes either side of Cat Street, Ura-Harajuku'], 'Ura-Harajuku', '裏原宿',
  'The back streets either side of Cat Street, between Harajuku and Omotesando. Small streetwear labels, sneaker shops, vintage and cafés grew up here in the 1990s, away from the big avenue.', '', 'Ura-Harajuku streets Tokyo')
P('headspa-harajuku', ['The Head Spa Tokyo Harajuku'], 'The Head Spa Tokyo Harajuku', '原宿',
  'A head spa salon in Jingūmae, about five minutes north of the hotel. A long scalp massage, wash and treatment, with English spoken. Part of a small chain that also has a Kyoto branch.', 'Book ahead. Saturday 10:00 to 20:00, Monday 11:00 to 19:00.', 'The Head Spa Tokyo Harajuku')
P('headspa-josho', ['Head Spa Josho'], 'Head Spa Josho', '上焦',
  'A head spa salon in the Omotesando back streets, open late.', 'Book ahead. Open to 22:00.', 'Head Spa Josho Omotesando')
P('sora', ['Body Spa Sora'], 'Body Spa Sora', 'ボディスパ ソラ 渋谷',
  'A body and foot massage salon on the east side of Shibuya Station.', '10:00 to 23:00.', 'Body Spa Sora Shibuya')
P('joyful', ['Joyful Massage Spa Shibuya'], 'Joyful Massage Spa Shibuya', '高興リラックス空間 渋谷',
  'A large body and foot massage salon in Dōgenzaka, open around the clock.', 'Walk-ins usually fine. Open 24 hours.', 'Joyful Massage Spa Shibuya')
P('quatre', ['Head Spa Salon QUATRE'], 'Head Spa Salon QUATRE Kyoto', 'ヘッドスパ キャトル 京都',
  'A head spa salon near Shijō-Karasuma, one subway stop north of the Kyoto hotel.', 'Book ahead. 12:00 to 20:30.', 'Head Spa Salon QUATRE Kyoto')
P('headspa-kyoto', ['The Head Spa Tokyo Kyoto'], 'The Head Spa Tokyo Kyoto', '四条河原町',
  'The Kyoto branch of The Head Spa Tokyo, at Shijō-Kawaramachi near Pontochō.', 'Book ahead. 11:00 to 19:00.', 'The Head Spa Tokyo Kyoto')
P('yumemishi', ['YUMEMISHI Shijō-Karasuma'], 'YUMEMISHI Shijō-Karasuma', '京の癒処 ゆめみし 四条烏丸店',
  'A relaxation salon for body and foot massage near Shijō-Karasuma, the closest of the list to the Kyoto hotel.', '12:00 to 21:00.', 'Yumemishi Shijo Karasuma massage')
P('hannari', ['Hannari'], 'Kyoto Relaxation Massage Hannari', 'はんなり 京都四条烏丸店',
  'A body massage and chiropractic salon near Shijō-Karasuma and Nishiki Market.', '12:00 to 22:00.', 'Hannari massage Kyoto Shijo Karasuma')
P('headspa-zen', ['Head Spa ZEN'], 'Head Spa ZEN', 'ヘッドスパ 禅 銀座',
  'A head spa salon in Ginza 2-chōme, open late.', 'Book ahead. 11:00 to 23:00.', 'Head Spa ZEN Ginza')
P('zwei-haus', ['Head Spa zwei HAUS'], 'Head Spa zwei HAUS', 'メディカル ヘッドスパ zwei HAUS 銀座',
  'A head spa salon in Ginza 1-chōme.', 'Book ahead. 10:00 to 22:00.', 'Head Spa zwei HAUS Ginza')
P('buasai', ['Buasai Ginza'], 'Buasai Ginza', '銀座 タイ古式マッサージ',
  'A Thai massage salon in Ginza 8-chōme, about five minutes from the Blossom.', '10:00 to midnight.', 'Buasai Ginza Thai massage')
P('yuragi', ['YURAGI'], 'YURAGI', '銀座 マッサージ&ボディワークス ゆらぎ',
  'A body massage and bodywork salon in Ginza 7-chōme, open late.', '13:00 to midnight.', 'Yuragi massage Ginza')
P('kungfu-head', ['Kungfu head therapy'], 'Kungfu head therapy', '宮夫頭療',
  'A small head therapy studio in Alpha House, 27 Nathan Road, two minutes from the Sheraton.', '11:00 to 22:00. Book by message if you can.', '宮夫頭療 Nathan Road Tsim Sha Tsui')
P('foot-lam-moon', ['Foot Lam Moon'], 'Foot Lam Moon Foot Reflexology', '足臨門',
  'A foot reflexology clinic on Hankow Road, Tsim Sha Tsui.', '10:00 to 00:30.', 'Foot Lam Moon foot reflexology Tsim Sha Tsui')
P('fu-ying', ['Fu Ying Massage'], 'Fu Ying Massage', '芙盈足莊',
  'A foot and body massage parlour on Granville Road, Tsim Sha Tsui, open around the clock.', 'Open 24 hours.', 'Fu Ying Massage Granville Road')
P('kyoto-st', ['Kyoto Station'], 'Kyoto Station', '京都駅',
  'A huge modern station of glass and steel, with a soaring central hall, department stores and restaurants inside. The Shinkansen platforms are on the south side and Kyoto Tower faces the north exit.',
  'The staffed luggage counter is where the suitcases go while you are in Nara.', 'Kyoto Station building')
P('tokyo-st', ['Tokyo Station'], 'Tokyo Station', '東京駅',
  'The city\'s grand central terminal. The Marunouchi side is a restored red brick building from 1914 with domed roofs. The Yaesu side, where the Shinkansen arrives, is modern and has the taxi rank.',
  'It is enormous. Follow the signs for the exit name, not the direction.', 'Tokyo Station Marunouchi building')
P('shibuya-st', ['Shibuya Station'], 'Shibuya Station', '渋谷駅',
  'One of the busiest stations in the world, where nine train and metro lines meet. It is spread over several levels and has been under reconstruction for years, so signs matter more than instinct.',
  'The Hachikō exit is the one for the Scramble Crossing and the walk to the hotel.', 'Shibuya Station Hachiko exit')
P('yurikamome', ['Yurikamome'], 'Yurikamome', 'ゆりかもめ',
  'A driverless elevated train from Shimbashi out to Odaiba. It climbs a spiral ramp and crosses Rainbow Bridge with views over Tokyo Bay.',
  'With no driver, the front seats have a clear view forward. They fill quickly.', 'Yurikamome train Rainbow Bridge')
P('mtr', ['MTR'], 'MTR', '港鐵',
  'Hong Kong\'s metro. Fast, frequent, air conditioned and signed in English. Tsim Sha Tsui to Central is two stops under the harbour.', 'No eating or drinking past the gates. Tap in and out with Octopus.', 'Hong Kong MTR train')

# ---------------- Shibuya leg ----------------
P('hachiko', ['Hachikō exit', 'Hachikō'], 'Hachikō and the Hachikō exit', 'ハチ公',
  'A small bronze statue of an Akita dog who waited at Shibuya Station every day for his owner, for years after the owner died. It is Tokyo\'s best known meeting spot, and the station exit beside it opens straight onto the Scramble Crossing.',
  'There is usually a short queue for a photo with the statue. It moves quickly.', 'Hachiko Memorial Statue Shibuya')
P('miyashita', ['Miyashita Park'], 'Miyashita Park', '宮下公園 MIYASHITA PARK',
  'A long, low shopping building beside the rail line with a public park on its roof: lawn, a skate park, a climbing wall and a cafe. Your hotel is the tower at its northern end. On Saturday the Shibuya Music Festival uses the rooftop as one of its stages.',
  'The ground floor lane, Shibuya Yokochō, is a run of small izakaya and is lively from late afternoon.', 'MIYASHITA PARK Shibuya')
P('cat', ['Cat Street'], 'Cat Street', 'キャットストリート',
  'A narrow, mostly car-free lane that winds from Shibuya up to Omotesando, following a river that was covered over. It is lined with streetwear shops, sneaker stores, small cafes and a few vintage places. It is calm, flat and easy, which is why it is the first walk of the trip.',
  'It runs for about a kilometre. The Shibuya end is quieter, the Omotesando end is busier.', 'Cat Street Shibuya Harajuku', days=[17, 18, 19, 20])
P('omote-arch', ['Omotesando Hills, Tod&#x27;s and Dior'], 'Omotesando architecture', '表参道の建築',
  'The avenue doubles as an open-air gallery of buildings by famous architects. Omotesando Hills is Tadao Ando\'s long concrete mall with a spiral ramp inside. Tod\'s, by Toyo Ito, is wrapped in a concrete frame shaped like bare tree branches. Dior, by SANAA, is a white box that glows from within at dusk.',
  'All three are on the same side of the avenue within a few minutes\' walk. You only need to look up.', 'Omotesando Hills Tokyo')
P('prada', ['Prada Aoyama'], 'Prada Aoyama', 'プラダ青山店',
  'A six storey tower by Herzog and de Meuron, covered entirely in diamond-shaped glass panes, some flat and some bulging outward like bubbles. It is one of the most photographed buildings in Tokyo.',
  'It is about eight minutes further on from the Omotesando crossing, in the quieter Aoyama end.', 'Prada Aoyama Tokyo')
P('vintage', ['vintage luxury'], 'Omotesando and Aoyama vintage luxury stores', '表参道・青山 ヴィンテージ',
  'A cluster of secondhand luxury boutiques in the back streets either side of Omotesando. Amore Vintage, Vintage Qoo, Casanova Vintage, Brand Collect and ALLU sell authenticated pre-owned bags, jewellery and accessories from Chanel, Hermès, Louis Vuitton and others, often in excellent condition and at better prices than new.',
  'All open at 11:00 except Casanova at 12:00. Take the physical passports for tax-free.', 'Amore Vintage Omotesando', days=[19, 20])
P('omote', ['Omotesando'], 'Omotesando', '表参道',
  'A wide avenue lined with zelkova trees, often called Tokyo\'s Champs-Élysées. Flagship stores sit along the main road, and the back lanes on either side hold smaller boutiques and cafes. The same back lanes are where the vintage luxury stores are.',
  'For lunch, the side streets are cheaper and calmer than the avenue itself.', 'Omotesando Avenue Tokyo')
P('scramble', ['Scramble Crossing'], 'Shibuya Scramble Crossing', '渋谷スクランブル交差点',
  'The famous crossing outside Shibuya Station. Every light turns red at once and up to a few thousand people cross in all directions, then it empties and fills again two minutes later. Giant video screens cover the buildings around it.',
  'Cross it once at street level, then look down on it from Shibuya Sky.', 'Shibuya Scramble Crossing')
P('center', ['Center-gai'], 'Center-gai', 'センター街',
  'The pedestrian street that runs off the Scramble Crossing into the heart of Shibuya. Fast food, game arcades, karaoke, cheap fashion and neon signs stacked several storeys high. It is loud, young and busy at any hour.',
  'The lanes branching off it are where the smaller bars and ramen counters are.', 'Shibuya Center Gai')
P('donki', ['MEGA Don Quijote Shibuya', 'Don Quijote'], 'MEGA Don Quijote Shibuya', 'MEGAドン・キホーテ渋谷本店',
  'A seven floor discount store that sells almost everything: snacks, cosmetics, chargers, umbrellas, luggage, costumes and souvenirs, crammed floor to ceiling with handwritten signs and a jingle on repeat. Known as Donki. It is open around the clock.',
  'It has a tax-free counter. Take the passports if you plan to spend over ¥5,000.', 'MEGA Don Quijote Shibuya Honten')
P('seven', ['7-Eleven'], '7-Eleven', 'セブン-イレブン',
  'Japanese convenience stores are far better than the name suggests. Fresh sandwiches, rice balls, hot food, good coffee, toiletries and umbrellas, open all hours. The ATMs inside take foreign cards.',
  'The egg sandwich and the onigiri are worth trying at least once.', '7-Eleven Japan convenience store food')
P('sky', ['Shibuya Sky'], 'Shibuya Sky', '渋谷スカイ SHIBUYA SKY',
  'An open-air observation deck on the roof of the Shibuya Scramble Square tower, 229 metres up. There is no glass ceiling, only glass walls at the edge, so you stand in the open with the whole city around you. You can see the Scramble Crossing directly below and, on a clear day, Mount Fuji.',
  'Bags, hats and loose items are not allowed on the rooftop, so go up with phones and pockets only.', 'SHIBUYA SKY rooftop')
P('nonbei', ['Nonbei Yokochō'], 'Nonbei Yokochō', 'のんべい横丁',
  'Drunkard\'s Alley: two tiny lanes of old wooden bars and yakitori counters beside the rail tracks, a minute from your hotel. Most seat only five or six people. It dates from the 1950s and looks like it, with red lanterns and sliding doors.',
  'Some bars are regulars only or charge a small cover. Look for an open door and an English menu.', 'Nonbei Yokocho Shibuya')
P('dogenzaka', ['Dōgenzaka'], 'Dōgenzaka', '道玄坂',
  'The sloping street that climbs west from the Scramble Crossing, past the Shibuya 109 tower. The main road and the lanes behind it are packed with restaurants, izakaya and bars, from ramen counters to sit-down places.',
  'It is a five to ten minute walk from the hotel.', 'Dogenzaka Shibuya')
P('festival', ['Shibuya Music Festival', 'festival streets', 'Festival streets', 'festival'], 'Shibuya Music Festival', '渋谷音楽祭',
  'A free street music festival held over one weekend each October. Stages are set up around Shibuya, including the Miyashita Park rooftop, and on Sunday the roads around Dōgenzaka and the 109 tower close to traffic for bands, brass ensembles and parades.',
  'There is no ticket and no fixed plan needed. Wander through and stop where something sounds good.', 'Shibuya Music Festival street stage', days=[0, 17, 18])
P('meiji', ['Meiji Jingū'], 'Meiji Jingū', '明治神宮',
  'Tokyo\'s most important Shintō shrine, set inside a forest of about 100,000 trees planted a century ago. You walk in along a wide gravel path under towering wooden torii gates, past a wall of decorated sake barrels, to a courtyard of cypress wood buildings. It is strikingly quiet for the middle of the city.',
  'Allow 15 minutes to walk in from the gate to the main hall. You may see a wedding procession on a weekend.', 'Meiji Jingu Shrine Tokyo')
P('takeshita', ['Takeshita Street'], 'Takeshita Street', '竹下通り',
  'A narrow, 350 metre pedestrian street opposite Harajuku Station and the heart of Tokyo teenage fashion. Crepe stands, candy floss the size of your head, costume shops, sock shops and cute character stores. It is loud, colourful and very crowded.',
  'Walk it once end to end, then escape into the lanes behind.', 'Takeshita Street Harajuku')
P('harajuku', ['Harajuku back lanes', 'Harajuku'], 'Harajuku', '原宿',
  'The neighbourhood between Meiji Jingū and Omotesando, known for youth fashion and street style. Beyond Takeshita Street, the back lanes, called Ura-Harajuku, are calmer and lined with independent boutiques, vintage shops and coffee stands.',
  'The back lanes run all the way down to Cat Street.', 'Harajuku Tokyo backstreets')
P('kart', ['Street Kart'], 'Street Kart', 'ストリートカート',
  'Go-karting on real Tokyo roads, in a small convoy led by a guide. You sit low to the ground in an open kart and drive in normal traffic. Your route crosses Rainbow Bridge over Tokyo Bay, timed for golden hour.',
  'Fully closed shoes are required, plus the physical licence, the physical International Driving Permit and passports.', 'Street Kart Tokyo go kart')
P('rainbow', ['Rainbow Bridge'], 'Rainbow Bridge', 'レインボーブリッジ',
  'A white suspension bridge nearly 800 metres long across Tokyo Bay, linking the city to the island of Odaiba. It is lit up at night and is one of the classic Tokyo skyline views.',
  '', 'Rainbow Bridge Tokyo')
P('cat3d', ['3D cat'], 'Shinjuku 3D cat', '新宿東口の猫',
  'A giant curved video screen on a building opposite Shinjuku Station\'s east exit. It shows a hyper-realistic calico cat that appears to sit inside the building, stretching, meowing and peering down at the street.',
  'It appears for a few minutes at a time between adverts. Stand on the plaza across the road.', 'Shinjuku 3D cat billboard Cross Shinjuku Vision')
P('isetan', ['Isetan food hall'], 'Isetan food hall', '伊勢丹新宿店 デパ地下',
  'The basement of Isetan, Tokyo\'s most fashionable department store. It is a huge, immaculate food hall of sweets, pastries, bento, tea and sake, with every item displayed like jewellery.',
  'A good rainy day stop, and free samples are common.', 'Isetan Shinjuku depachika food hall')
P('omoide', ['Omoide Yokochō'], 'Omoide Yokochō', '思い出横丁',
  'Memory Lane: two narrow alleys beside the west exit of Shinjuku Station, packed with about 60 tiny yakitori counters and bars under red lanterns. It began as a black market after the war and has barely changed in look. This is where you eat.',
  'Arrive about 17:30. Order a drink and a few skewers, then move on to the next counter.', 'Omoide Yokocho Shinjuku')
P('godzilla', ['Godzilla head'], 'Godzilla head', 'ゴジラヘッド',
  'A life-size Godzilla head and claws peering over the top of the Toho cinema building in Kabukichō, as if the monster were standing behind it. It roars and lights up on the hour in the evening.',
  'The best view is from the street leading up to the cinema.', 'Godzilla head Shinjuku Toho')
P('kabuki-tower', ['Kabukichō Tower'], 'Tokyu Kabukichō Tower', '東急歌舞伎町タワー',
  'A 48 storey tower opened in 2023, shaped like a fountain of water. The lower floors hold a neon-lit food hall themed on Japanese festivals, an arcade, cinemas and live venues.',
  'The food hall on the second floor is worth a walk through for the lights alone.', 'Tokyu Kabukicho Tower')
P('kabukicho', ['Kabukichō'], 'Kabukichō', '歌舞伎町',
  'Tokyo\'s biggest entertainment district, a dense grid of neon signs, restaurants, bars, arcades and karaoke north of Shinjuku Station. It is at its most spectacular after dark.',
  'It is safe to walk through. Ignore anyone on the street inviting you into a bar.', 'Kabukicho Shinjuku neon night')
P('hanazono', ['Hanazono Shrine'], 'Hanazono Shrine', '花園神社',
  'A small Shintō shrine with bright vermilion buildings, tucked between Kabukichō and Golden Gai. It is lit by lanterns at night and is a sudden pocket of calm.',
  '', 'Hanazono Shrine Shinjuku')
P('goldengai', ['Golden Gai'], 'Golden Gai', '新宿ゴールデン街',
  'Six tiny alleys holding more than 200 bars, most the size of a cupboard with room for six or eight people. Each has its own theme and regulars. It is a wander more than a destination: look in, and if a place is full or unwelcoming, move on.',
  'Take cash. Most bars charge a cover of roughly ¥500 to ¥1,500. An English menu or sign means visitors are welcome. Ask before taking photos.', 'Golden Gai Shinjuku')
P('tocho', ['Government Building deck'], 'Tokyo Metropolitan Government Building', '東京都庁',
  'Twin towers by architect Kenzo Tange in west Shinjuku, with free observation decks on the 45th floor, 202 metres up. Not in the plan, but of interest if plans change.',
  'Best about 16:15 for dusk. Check which of the two decks is open.', 'Tokyo Metropolitan Government Building observation deck')
P('gyoen', ['Shinjuku Gyoen'], 'Shinjuku Gyoen', '新宿御苑',
  'A large, beautifully kept garden with Japanese, French and English sections, wide lawns and a greenhouse, a short walk from Shinjuku Station.',
  'Closed on Mondays. Gates close at 16:00 in October, the greenhouse at 15:30.', 'Shinjuku Gyoen National Garden')
P('teamlab', ['teamLab Borderless', 'teamLab'], 'teamLab Borderless', 'チームラボボーダレス',
  'A digital art museum in the basement of Azabudai Hills. There is no map and no set route. You walk through dark rooms where projected flowers, waterfalls and animals flow across the walls and floor, react to your touch and drift from one room into the next.',
  'Booked for the first session at 08:30 on Monday 26. Wear trousers, as some floors are mirrored.', 'teamLab Borderless Azabudai Hills')
P('sumo', ['Sumo show'], 'Sumo show', '相撲ショー',
  'An indoor show where former sumo wrestlers demonstrate the rules, rituals and training, then fight exhibition bouts, with dinner included. No real tournament runs on your dates, so a show is the way to see sumo. Kept as a wet weather backup.',
  'Hirakuza Ginza, 1-9-13 Ginza: daily 17:00, about 2 hours 15 minutes with a kaiseki dinner, from ¥17,000. Book on Klook. Within 21 days only 50% is refunded, nothing within 7 days. Alternative: Tokyo Sumo Club at Tokyo Tower, shows 11:00, 14:00, 17:00 and 20:00, from ¥16,000, on TableCheck.', 'Hirakuza Ginza sumo show')
P('culture-centre', ['Asakusa Culture Tourist Information Centre'], 'Asakusa Culture Tourist Information Centre', '浅草文化観光センター',
  'A striking building by Kengo Kuma, stacked like a pile of timber houses, directly opposite the Kaminarimon gate. The free 8th floor terrace looks down the Nakamise street to the temple and across to the Skytree.',
  '', 'Asakusa Culture Tourist Information Center terrace')
P('sensoji', ['Sensō-ji'], 'Sensō-ji', '浅草寺',
  'Tokyo\'s oldest temple, founded in the 7th century. A huge red main hall and a five storey pagoda stand at the end of a long shopping street, with incense smoke drifting across the forecourt. It is the classic image of old Tokyo.',
  'Waft the incense smoke over yourself for good health, as everyone else does.', 'Sensoji Temple Asakusa')
P('kaminarimon', ['Kaminarimon'], 'Kaminarimon', '雷門',
  'The Thunder Gate, the outer gate of Sensō-ji. A giant red paper lantern nearly four metres tall hangs in the middle, flanked by statues of the gods of wind and thunder.',
  '', 'Kaminarimon Gate Asakusa')
P('nakamise', ['Nakamise street', 'Nakamise'], 'Nakamise street', '仲見世通り',
  'A 250 metre lane of about 90 small stalls leading from the Kaminarimon gate to the temple. They sell rice crackers, sweet bean cakes, fans, chopsticks and souvenirs, as they have for centuries.',
  'Eat snacks at the stall, not while walking.', 'Nakamise shopping street Asakusa')
P('skytree', ['Skytree'], 'Tokyo Skytree', '東京スカイツリー',
  'A 634 metre broadcasting tower, the tallest structure in Japan, visible across the river from Asakusa. You are not going up it. The plan is to see it, by day from Asakusa and lit up at night.',
  'The view from Azumabashi bridge has the tower beside the golden Asahi building.', 'Tokyo Skytree from Asakusa')
P('azuma', ['Azuma-bashi bridge', 'Azumabashi bridge', 'Azuma-bashi', 'Azumabashi'], 'Azumabashi bridge', '吾妻橋',
  'A red bridge over the Sumida River, five minutes from Sensō-ji. It gives the postcard view of the Skytree next to the Asahi Beer headquarters and its giant golden flame sculpture.',
  '', 'Azumabashi bridge Skytree view')
P('kappabashi', ['Kappabashi kitchenware street', 'Kappabashi'], 'Kappabashi', 'かっぱ橋道具街',
  'Kitchen Town: an 800 metre street of shops supplying Tokyo\'s restaurants. Japanese knives, ceramics, lacquer bowls, cast iron and the famous plastic food models displayed in restaurant windows.',
  'Knife shops will engrave your name. Many shops close by 17:00.', 'Kappabashi Kitchen Town Tokyo')
P('asakusa', ['Asakusa'], 'Asakusa', '浅草',
  'The old downtown district of Tokyo, on the Sumida River. Low buildings, rickshaws, craft shops and old restaurants around Sensō-ji temple give a feel for the city before the skyscrapers.',
  '', 'Asakusa Tokyo old town')
P('air-cabin', ['Air Cabin'], 'Yokohama Air Cabin', 'ヨコハマ エア キャビン',
  'A short urban cable car that glides over the water from Sakuragichō Station to the Minato Mirai waterfront in about five minutes, with views of the harbour and skyline.',
  '', 'Yokohama Air Cabin')
P('minato', ['Minato Mirai waterfront', 'Minato Mirai'], 'Minato Mirai', 'みなとみらい',
  'Yokohama\'s modern harbourfront: a sweep of towers, a giant Ferris wheel with a clock on it, promenades and parks along the water. It is spacious and breezy after Tokyo.',
  'It is at its best from late afternoon, when the lights come on.', 'Minato Mirai Yokohama skyline')
P('redbrick', ['Red Brick Warehouses'], 'Red Brick Warehouses', '横浜赤レンガ倉庫',
  'Two handsome brick customs warehouses from the 1910s on the Yokohama waterfront, now filled with shops, cafes and event spaces, with a wide plaza facing the harbour.',
  '', 'Yokohama Red Brick Warehouse')
P('chinatown', ['Chinatown'], 'Yokohama Chinatown', '横浜中華街',
  'The largest Chinatown in Japan, with ornate gates, a colourful temple and several hundred restaurants and food stalls packed into a few blocks. Steamed buns, dumplings and roast duck are everywhere.',
  'Share plates at a sit-down restaurant, or graze from the stalls.', 'Yokohama Chinatown')
P('yokohama', ['Yokohama'], 'Yokohama', '横浜',
  'Japan\'s second largest city, a port on Tokyo Bay about 30 minutes south of Tokyo. It opened to foreign trade in 1859 and still feels more open and international, with a long waterfront.',
  '', 'Yokohama waterfront')
P('hachimangu', ['Tsurugaoka Hachimangū'], 'Tsurugaoka Hachimangū', '鶴岡八幡宮',
  'Kamakura\'s main shrine, reached by a long straight avenue from the sea and a steep flight of stone steps. It was the spiritual centre of the samurai government in the 12th century.',
  '', 'Tsurugaoka Hachimangu Kamakura')
P('komachi', ['Komachi-dōri'], 'Komachi-dōri', '小町通り',
  'Kamakura\'s lively shopping lane, running from the station towards the shrine, full of snack stalls, sweet shops and craft stores.', '', 'Komachi-dori Kamakura')
P('enoden', ['Enoden'], 'Enoden', '江ノ電',
  'A small, old-fashioned electric train that trundles along the coast from Kamakura, squeezing between houses and running right beside the sea.', '', 'Enoden train Kamakura coast')
P('hasedera', ['Hase-dera'], 'Hase-dera', '長谷寺',
  'A hillside temple in Kamakura with gardens, a cave, a huge gilded wooden statue of the goddess Kannon and a terrace looking over the sea.', '', 'Hasedera Temple Kamakura')
P('kamakura-buddha', ['Great Buddha'], 'Great Buddha of Kamakura', '鎌倉大仏',
  'An 11 metre bronze seated Buddha cast in 1252. It has sat in the open air since a tsunami washed its hall away in the 15th century.', '', 'Great Buddha Kamakura Kotokuin', days=[19, 20])
P('yamashita', ['Yamashita Park'], 'Yamashita Park', '山下公園',
  'A long strip of lawn and rose gardens on the Yokohama harbour front, with the retired ocean liner Hikawa Maru moored alongside. It links the Red Brick Warehouses to Chinatown on foot.', '', 'Yamashita Park Yokohama')
P('tawaramachi', ['Tawaramachi'], 'Tawaramachi Station', '田原町駅',
  'The Ginza line stop one before Asakusa, and the closest station to Kappabashi. The kitchenware street starts about five minutes west, at the building with the giant chef head on its roof.', '', 'Tawaramachi Station Kappabashi')
P('kamiyacho', ['Kamiyachō'], 'Kamiyachō Station', '神谷町駅',
  'The Hibiya line station under Azabudai Hills, the nearest to teamLab Borderless. Four stops from Ginza.', '', 'Kamiyacho Station Azabudai Hills')
P('kamakura', ['Kamakura'], 'Kamakura', '鎌倉',
  'A small seaside city an hour south of Tokyo that was Japan\'s capital in the 12th and 13th centuries. It is known for temples, shrines, the Great Buddha and its beaches. It is the alternative to the Tsukiji morning on Tuesday 20.',
  '', 'Kamakura Japan')

# ---------------- Kyoto, Nara and Osaka ----------------
P('todaiji', ['Tōdai-ji and the Great Buddha', 'Tōdai-ji'], 'Tōdai-ji and the Great Buddha', '東大寺 大仏',
  'A vast wooden temple hall, one of the largest timber buildings in the world, housing a 15 metre bronze Buddha cast in the 8th century. The scale only registers when you stand beneath it.',
  'One pillar inside has a hole the size of the Buddha\'s nostril. Children squeeze through it for luck.', 'Todaiji Temple Great Buddha Nara')
P('narapark', ['Nara Park'], 'Nara Park', '奈良公園',
  'A large open park in the middle of Nara, home to more than a thousand wild deer that roam freely among the temples and lawns. They are considered sacred and are very used to people.',
  'Buy deer crackers from the stalls. Show empty hands when you run out.', 'Nara Park deer')
P('kasuga', ['Kasuga Taisha'], 'Kasuga Taisha', '春日大社',
  'Nara\'s great shrine, painted bright vermilion and set in ancient woodland. The approach is lined with about two thousand moss-covered stone lanterns, and hundreds of bronze lanterns hang from the eaves.',
  '', 'Kasuga Taisha Shrine lanterns Nara')
P('isuien', ['Isuien garden'], 'Isuien garden', '依水園',
  'A quiet Japanese stroll garden of ponds, stepping stones and tea houses, designed so that the roof of Tōdai-ji and the hills behind appear as part of the view.', '', 'Isuien Garden Nara')
P('nigatsu', ['Nigatsu-dō'], 'Nigatsu-dō', '二月堂',
  'A hall of Tōdai-ji built on a hillside, with a wooden balcony that looks out over the temple roofs and the whole city of Nara. It is free, open at all hours and far quieter than the main hall.',
  '', 'Nigatsudo Hall Nara view')
P('nara', ['Nara'], 'Nara', '奈良',
  'Japan\'s first permanent capital, in the 8th century, about 45 minutes south of Kyoto. Its main sights sit together in and around one large park, which makes it an easy half day.',
  '', 'Nara Japan')
P('pontocho', ['Pontochō'], 'Pontochō', '先斗町',
  'A long, narrow lantern-lit alley running parallel to the Kamo River in central Kyoto, lined with restaurants and bars in old wooden townhouses. It is one of the city\'s most atmospheric places to eat.',
  'Menus are often posted outside. Places range from casual to very expensive.', 'Pontocho Alley Kyoto night')
P('castle', ['Osaka Castle'], 'Osaka Castle', '大阪城',
  'A white and green castle tower with gold trim, rising above enormous stone walls and wide moats in a large park. The tower is a 1931 concrete rebuild, so the plan is to walk up to its foot and admire it from outside.',
  'The park is open around the clock. Takeaway breakfast on a bench works well.', 'Osaka Castle')
P('ecocard', ['Enjoy Eco Card'], 'Enjoy Eco Card', 'エンジョイエコカード',
  'A one day pass for the Osaka Metro and city buses, bought from any metro ticket machine. With five or more metro rides on the Osaka day, it pays for itself.',
  'It does not cover JR or Keihan trains.', 'Osaka Metro Enjoy Eco Card')
P('umeda', ['Umeda Sky deck', 'Umeda Sky'], 'Umeda Sky Building', '梅田スカイビル',
  'Two 40 storey towers joined at the top by a ring-shaped rooftop deck, 173 metres up. You reach it by a glass escalator that crosses the open gap between the towers. The deck is open to the sky.',
  '', 'Umeda Sky Building Floating Garden Observatory')
P('kuromon', ['Kuromon Ichiba', 'Kuromon'], 'Kuromon Ichiba', '黒門市場',
  'Osaka\'s Kitchen: a covered market street about 600 metres long with around 150 stalls. Vendors grill scallops, crab and wagyu skewers to order and slice tuna in front of you.',
  'Eat at the stall or in the small seating areas, not while walking.', 'Kuromon Ichiba Market Osaka')
P('horie', ['Horie, Amerikamura and Shinsaibashi'], 'Horie, Amerikamura and Shinsaibashi', '堀江・アメリカ村・心斎橋',
  'Three neighbouring shopping districts in central Osaka. Shinsaibashi is a long covered arcade of mainstream shops. Amerikamura is the youth quarter of streetwear and vintage. Horie is calmer, with design stores and cafes. The secondhand luxury chains Kindal, ALLU and KOMEHYO are all here.',
  'Take the passports for tax-free.', 'Amerikamura Osaka')
P('orange', ['Orange Street'], 'Orange Street', 'オレンジストリート',
  'The main street of Horie, once a row of furniture makers and now lined with design shops, fashion boutiques and good coffee.', '', 'Orange Street Horie Osaka')
P('namba-yasaka', ['Namba Yasaka Shrine'], 'Namba Yasaka Shrine', '難波八阪神社',
  'A small neighbourhood shrine with an astonishing stage in the shape of a giant lion\'s head, 12 metres tall, with its mouth wide open. The mouth is said to swallow evil spirits and bring luck.',
  'Closes about 17:00. Ten minutes is enough.', 'Namba Yasaka Shrine lion head')
P('janjan', ['Janjan-Yokochō'], 'Janjan-Yokochō', 'ジャンジャン横丁',
  'A narrow covered alley leading into Shinsekai, lined with old standing bars, kushikatsu counters and shōgi parlours where locals play Japanese chess.', '', 'Janjan Yokocho Osaka')
P('shinsekai', ['Shinsekai'], 'Shinsekai', '新世界',
  'New World: a district built in 1912 as a vision of the future, modelled on Paris and Coney Island, and now gloriously faded. Enormous signs, giant pufferfish lanterns and retro game parlours fill the streets under the Tsūtenkaku tower.',
  'It looks its best as the signs light up at dusk.', 'Shinsekai Osaka night')
P('tsutenkaku', ['Tsūtenkaku'], 'Tsūtenkaku', '通天閣',
  'A 103 metre steel tower at the centre of Shinsekai and a symbol of Osaka, covered in neon advertising. Its lights change colour to forecast the next day\'s weather.', '', 'Tsutenkaku Tower Osaka')
P('kushikatsu', ['kushikatsu'], 'Kushikatsu', '串カツ',
  'Osaka\'s signature snack: skewers of meat, seafood and vegetables, breaded and deep fried, then dipped in a shared pot of thin savoury sauce.',
  'Never dip twice. Use the cabbage leaves to scoop more sauce.', 'kushikatsu Osaka Shinsekai')
P('dotonbori', ['Dōtonbori'], 'Dōtonbori', '道頓堀',
  'Osaka\'s famous canal-side entertainment strip. Giant mechanical crabs, octopuses and dragons hang over the restaurants, and walls of neon reflect in the water. The local motto is to eat until you drop: takoyaki, okonomiyaki, gyoza and ramen from street counters.',
  'It is at full strength after dark.', 'Dotonbori Osaka night')
P('tombori', ['Tombori River Cruise'], 'Tombori River Cruise', 'とんぼりリバークルーズ',
  'A 20 minute open boat ride along the Dōtonbori canal, passing under the bridges and beneath the neon signs, with a guide on board.',
  'Buy tickets at the booth beside the Don Quijote building when you arrive, for a boat after dark.', 'Tombori River Cruise Dotonbori')
P('glico', ['Glico Running Man', 'Glico', 'Nanohana cosmetics shop'], 'Glico Running Man', 'グリコサイン',
  'A giant illuminated sign of a runner crossing a finish line, advertising a confectionery company. It has stood over the Dōtonbori canal since 1935 and is the photo everyone takes in Osaka.',
  'The Nanohana cosmetics shop directly opposite has a photo platform.', 'Glico Running Man sign Dotonbori')
P('hozenji', ['Hōzenji Yokochō'], 'Hōzenji Yokochō', '法善寺横丁',
  'Two quiet stone-paved lanes just behind Dōtonbori, lit by paper lanterns and lined with small traditional restaurants and bars. A complete change of mood from the neon a minute away.', '', 'Hozenji Yokocho Osaka')
P('fudo', ['Mizukake Fudō'], 'Mizukake Fudō', '水掛不動',
  'A small stone statue of a Buddhist guardian at Hōzenji temple, completely covered in thick green moss. Visitors splash water over it when they make a wish, which is why the moss grows.',
  'Ladle a little water over the statue yourself.', 'Hozenji Mizukake Fudo moss statue')
P('harukas', ['Abeno Harukas 300'], 'Abeno Harukas 300', 'あべのハルカス',
  'The observation deck at the top of a 300 metre skyscraper in south Osaka. Dropped from the plan, and kept only as a weather fallback.', '', 'Abeno Harukas 300 observatory')
P('bamboo', ['Bamboo grove'], 'Arashiyama bamboo grove', '嵐山 竹林の小径',
  'A path through a forest of towering green bamboo, the stalks rising 20 metres or more and creaking as they sway. It is one of Kyoto\'s most famous sights, and only peaceful very early.',
  'By 09:00 it is shoulder to shoulder, which is the reason for the 06:45 start.', 'Arashiyama Bamboo Grove Kyoto')
P('tenryuji', ['Tenryū-ji'], 'Tenryū-ji', '天龍寺',
  'A Zen temple founded in 1339, with one of Japan\'s oldest gardens: a pond ringed by rocks and pines, with the Arashiyama hills borrowed as the backdrop.',
  'The garden\'s north gate opens directly onto the bamboo grove.', 'Tenryuji Temple garden Kyoto')
P('okochi', ['Ōkōchi Sansō villa', 'Ōkōchi Sansō'], 'Ōkōchi Sansō villa', '大河内山荘',
  'The hillside estate of a 1930s film star, at the top of the bamboo grove. Winding garden paths lead to viewpoints over Kyoto and the river gorge.',
  'Entry includes a bowl of matcha and a sweet.', 'Okochi Sanso Villa Arashiyama')
P('togetsukyo', ['Togetsukyō bridge'], 'Togetsukyō bridge', '渡月橋',
  'The Moon Crossing Bridge: a long, low wooden-railed bridge over the Katsura River with forested hills behind it. The landmark of Arashiyama.', '', 'Togetsukyo Bridge Arashiyama')
P('arashiyama', ['Arashiyama'], 'Arashiyama', '嵐山',
  'A scenic district on the western edge of Kyoto, where the river runs out of forested hills. It holds the bamboo grove, Tenryū-ji and the Togetsukyō bridge.', '', 'Arashiyama Kyoto')
P('nishiki', ['Nishiki Market'], 'Nishiki Market', '錦市場',
  'Kyoto\'s Kitchen: a narrow covered market five blocks long with more than a hundred stalls. Pickles, tofu, grilled eel, tiny octopus on sticks, rolled omelette and matcha sweets, many made to recipes centuries old.',
  'Eat at the stall. Walking and eating is frowned on here.', 'Nishiki Market Kyoto')
P('kiyomizu', ['Kiyomizu-dera', 'Kiyomizu'], 'Kiyomizu-dera', '清水寺',
  'Kyoto\'s most famous temple, founded in 778. Its main hall has a huge wooden stage built out over the hillside on tall pillars, without a single nail, with a view across the whole city.',
  'Below the hall, visitors drink from three streams of spring water for health, long life and success.', 'Kiyomizu-dera Temple Kyoto')
P('sannenzaka', ['Sannenzaka and Ninenzaka'], 'Sannenzaka and Ninenzaka', '三年坂・二年坂',
  'Two sloping, stone-paved lanes below Kiyomizu-dera, lined with preserved wooden townhouses that now hold tea shops, pottery stores and sweet makers. This is the Kyoto of postcards.',
  'The steps are steep and slippery when wet.', 'Sannenzaka Ninenzaka Kyoto')
P('sanjusangendo', ['Sanjūsangen-dō'], 'Sanjūsangen-dō', '三十三間堂',
  'A 120 metre long wooden hall containing 1,001 life-size golden statues of the goddess Kannon, standing in ranks around one giant seated figure.',
  'Closes at 17:00. No photos inside.', 'Sanjusangendo Temple Kyoto')
P('kodaiji', ['Kōdai-ji'], 'Kōdai-ji', '高台寺',
  'A graceful Zen temple near Ninenzaka, built in 1606, with raked gravel gardens, a pond, tea houses and a small bamboo grove.', '', 'Kodaiji Temple Kyoto')
P('yasaka', ['Yasaka shrine'], 'Yasaka Shrine', '八坂神社',
  'A large shrine with a bright vermilion gate at the eastern end of Shijō street, where Higashiyama meets Gion. A stage hung with hundreds of paper lanterns stands in the courtyard and is lit at dusk.',
  '', 'Yasaka Shrine Kyoto lanterns')
P('hanamikoji', ['Hanamikoji'], 'Hanamikoji', '花見小路',
  'The main street of Gion, lined with dark wooden teahouses and restaurants. In the early evening you may see geiko and maiko, Kyoto\'s geisha and their apprentices, walking to appointments.',
  'No photos of geiko or maiko, and keep off the private side lanes. There are fines.', 'Hanamikoji Street Gion')
P('gion', ['Gion'], 'Gion', '祇園',
  'Kyoto\'s historic geisha district, a quarter of wooden townhouses, teahouses and lantern-lit lanes on the east bank of the Kamo River.', '', 'Gion Kyoto')
P('higashiyama', ['Higashiyama'], 'Higashiyama', '東山',
  'The old eastern hills district of Kyoto, running along the foot of the mountains. It is the best preserved part of the city, linking Kiyomizu-dera, the sloping lanes, Kōdai-ji and Yasaka Shrine.',
  'The afternoon walk runs downhill from Kiyomizu-dera to Gion.', 'Higashiyama district Kyoto')
P('ginkakuji', ['Ginkaku-ji'], 'Ginkaku-ji', '銀閣寺',
  'The Silver Pavilion: a 15th century Zen temple with a plain wooden pavilion, a moss garden and a raked sand garden with a sand cone meant to reflect moonlight.',
  'Closes at 17:00.', 'Ginkakuji Silver Pavilion Kyoto')
P('philosopher', ['Philosopher&#x27;s Path'], 'Philosopher\'s Path', '哲学の道',
  'A two kilometre stone path beside a narrow canal lined with cherry trees, running south from Ginkaku-ji past small temples and cafes.', '', 'Philosophers Path Kyoto')
P('honenin', ['Hōnen-in'], 'Hōnen-in', '法然院',
  'A small, secluded temple just off the Philosopher\'s Path, entered through a thatched, moss-covered gate between two raked sand mounds.', '', 'Honenin Temple Kyoto')
P('fushimi', ['Fushimi Inari'], 'Fushimi Inari', '伏見稲荷大社',
  'A shrine famous for thousands of bright orange torii gates, set so close together that they form tunnels winding four kilometres up a wooded mountain. Each gate was donated by a business. Stone foxes, the messengers of the god Inari, guard the paths.',
  'The crowds thin sharply after the first ten minutes of climbing.', 'Fushimi Inari Taisha torii gates')

P('sanjo', ['Sanjō-dōri'], 'Sanjō-dōri', '三条通り',
  'Nara\'s main shopping street, running east from JR Nara Station towards the park. It is lined with restaurants, sweet shops and souvenir stores, and is the natural place for lunch on the walk in.',
  'Nakatanidō, near the far end, is famous for pounding mochi rice cakes at high speed.', 'Sanjo-dori Street Nara')

# ---------------- Tokyo: Hibiya and Ginza ----------------
P('hilton', ['Hilton Tokyo Odaiba', 'the Hilton', 'Hilton'], 'Hilton Tokyo Odaiba', 'ヒルトン東京お台場',
  'A waterfront hotel on Odaiba, facing Rainbow Bridge and the Tokyo skyline. Your Seascape package gives you a private viewing area for the fireworks, then the dinner buffet.',
  'Collect the wristbands first, then find your spot before it fills.', 'Hilton Tokyo Odaiba')
P('fireworks', ['Fireworks from the Hilton', 'fireworks'], 'Odaiba fireworks', 'お台場 花火',
  'A large fireworks display over Tokyo Bay, launched from barges off Odaiba, with Rainbow Bridge and the city skyline behind. Japanese fireworks are known for huge, perfectly round bursts.',
  'Take a layer. The bay is cool after dark.', 'Odaiba fireworks Rainbow Bridge', days=[0, 24])
P('liberty', ['Odaiba Statue of Liberty'], 'Odaiba Statue of Liberty', 'お台場 自由の女神像',
  'An 11 metre replica of the Statue of Liberty on the Odaiba waterfront. With Rainbow Bridge lit up behind it, it is an oddly perfect photo.', '', 'Odaiba Statue of Liberty Rainbow Bridge night')
P('odaiba', ['Odaiba'], 'Odaiba', 'お台場',
  'A large man-made island in Tokyo Bay with shopping malls, a beach, museums and wide waterfront promenades facing the city.', '', 'Odaiba Tokyo Bay')
P('eastgardens', ['Imperial Palace East Gardens', 'Ninomaru garden'], 'Imperial Palace East Gardens', '皇居東御苑',
  'The public part of the Imperial Palace grounds, on the site of the old Edo Castle. Massive stone walls and moats, the stone base of the vanished castle keep, wide lawns and a traditional pond garden.',
  'Free. Closed on Mondays and Fridays.', 'Imperial Palace East Gardens Tokyo')
P('kitte', ['KITTE'], 'KITTE rooftop garden', 'KITTE 屋上庭園',
  'A shopping building in the old Tokyo Central Post Office. Its free 6th floor roof garden looks straight down on the red brick front of Tokyo Station and the trains sliding in and out.', '', 'KITTE garden Tokyo Station view')
P('forum', ['Tokyo International Forum'], 'Tokyo International Forum', '東京国際フォーラム',
  'A convention centre by Rafael Viñoly with a spectacular glass hall, 60 metres high and shaped like the hull of a ship, crossed by sloping walkways. It is free to walk in.',
  'Take the lift to the top walkway and walk down.', 'Tokyo International Forum glass hall')
P('chuodori', ['Chūō-dōri'], 'Chūō-dōri', '中央通り',
  'Ginza\'s main street. On weekend afternoons it is closed to cars, and people stroll down the middle of the road between the flagship stores. Chairs and parasols are put out.',
  'Car-free from 12:00 to 17:00 on weekends.', 'Ginza Chuo-dori pedestrian paradise')
P('mitsukoshi', ['Mitsukoshi'], 'Ginza Mitsukoshi', '銀座三越',
  'A grand department store at Ginza\'s main crossing, part of Japan\'s oldest department store chain. Fashion upstairs, a superb food hall in the basement and a rooftop terrace.', '', 'Ginza Mitsukoshi')
P('ginzasix', ['Ginza Six'], 'Ginza Six', 'GINZA SIX',
  'Ginza\'s largest luxury mall, with an art installation hanging in its central atrium, a Tsutaya bookshop devoted to art, and a large rooftop garden with views over the district.', '', 'Ginza Six atrium rooftop garden')
P('matsuya', ['Matsuya'], 'Matsuya Ginza', '松屋銀座',
  'A long-established Ginza department store, known for its design floor and its basement food hall.', '', 'Matsuya Ginza department store')
P('dsm', ['Dover Street Market'], 'Dover Street Market Ginza', 'ドーバー ストリート マーケット ギンザ',
  'A seven floor concept store created by Rei Kawakubo of Comme des Garçons. Each designer has its own installation, so it feels more like a gallery than a shop.', '', 'Dover Street Market Ginza')
P('itoya', ['Itoya'], 'Itoya', '銀座 伊東屋',
  'A twelve floor stationery store, in business since 1904. Pens, paper, notebooks, cards, desk tools and craft supplies, with a floor for each.', '', 'Ginza Itoya stationery')
P('hermes', ['Maison Hermès'], 'Maison Hermès', '銀座メゾンエルメス',
  'A slender tower by Renzo Piano, built entirely of glass blocks. By day it looks like frosted crystal, and at night it glows like a lantern.', '', 'Maison Hermes Ginza Renzo Piano')
P('mikimoto', ['Mikimoto Ginza 2'], 'Mikimoto Ginza 2', 'ミキモト銀座2丁目店',
  'A pale pink tower by Toyo Ito for the pearl jeweller, pierced with irregular windows that look like scattered petals or bubbles.', '', 'Mikimoto Ginza 2 Toyo Ito')
P('wako', ['Wakō clock tower'], 'Wakō clock tower', '和光 時計塔',
  'A curved stone building from 1932 topped with a clock tower, standing on Ginza\'s main crossing. It is the symbol of the district and chimes on the hour.', '', 'Wako clock tower Ginza')
P('sushibus', ['Sushi Bus'], 'Sushi Bus', '寿司バス',
  'A double-decker sightseeing bus with a sushi conveyor belt, touring central Tokyo for about 70 minutes with all-you-can-eat sushi and drinks. New from 10 October 2026. An idea, not decided.',
  '¥16,000 each. Departures 11:00, 13:00, 15:00, 17:00 and 19:00 from the Kajibashi car park near Tokyo Station. Book on sushi-bus.com. Irregular maintenance closures.', 'Tokyo sushi bus Kajibashi')
P('ginza', ['Ginza'], 'Ginza', '銀座',
  'Tokyo\'s most elegant shopping district: wide streets of department stores, flagship boutiques, galleries and striking architecture, a ten minute walk from your hotel.',
  '', 'Ginza Tokyo')
P('azabudai', ['Azabudai Hills'], 'Azabudai Hills', '麻布台ヒルズ',
  'A new district opened in 2023, with Japan\'s tallest building and low, curving, garden-covered buildings by Thomas Heatherwick around a central green. teamLab Borderless is in its basement.', '', 'Azabudai Hills Tokyo')
P('skyroom', ['Sky Room Café'], 'Sky Room Café & Bar', 'Sky Room Cafe & Bar',
  'A cafe on the 33rd floor of the main Azabudai Hills tower, with Tokyo Tower filling the windows at eye level. The floor is open only to customers.', '', 'Azabudai Hills Sky Room cafe Tokyo Tower view')
P('tokyotower', ['Tokyo Tower'], 'Tokyo Tower', '東京タワー',
  'A 333 metre red and white lattice tower built in 1958, modelled on the Eiffel Tower. For decades it was the symbol of modern Tokyo. You are seeing it from below, not going up.', '', 'Tokyo Tower')
P('zojoji', ['Zōjō-ji'], 'Zōjō-ji', '増上寺',
  'A large Buddhist temple at the foot of Tokyo Tower. Its great red gate dates from 1622, and the view of the temple roof with the tower rising directly behind it is one of Tokyo\'s best photographs.', '', 'Zojoji Temple Tokyo Tower')
P('tsukiji', ['Tsukiji Outer Market', 'Tsukiji'], 'Tsukiji Outer Market', '築地場外市場',
  'The warren of lanes that surrounded Tokyo\'s old wholesale fish market. The wholesale market moved away in 2018, but about 400 small shops and stalls remain, selling fresh seafood, knives, tea and street food.',
  'Best from 07:30 to 09:30. From 10:00 to 12:00 the popular stalls can queue 45 minutes. Closed Sundays and Wednesdays.', 'Tsukiji Outer Market Tokyo')
P('namiyoke', ['Namiyoke shrine'], 'Namiyoke Shrine', '波除神社',
  'A small shrine on the edge of Tsukiji market, the guardian of the market and its traders. It houses two giant lion heads carried in the local festival.', '', 'Namiyoke Shrine Tsukiji')
P('shimbashi', ['Shimbashi'], 'Shimbashi', '新橋',
  'An old-school office district beside your hotel. After work its lanes and the arches under the railway tracks fill with salarymen eating and drinking at hundreds of small izakaya, yakitori bars and standing counters.',
  'Weeknights are when it is liveliest. No booking needed.', 'Shimbashi izakaya under tracks night')

# ---------------- Hong Kong ----------------
P('pier', ['Tsim Sha Tsui Public Pier 1'], 'Tsim Sha Tsui Public Pier', '尖沙咀公眾碼頭',
  'A small public pier on the Kowloon waterfront, behind the Cultural Centre and beside the old clock tower. It is where the Aqua Luna junk boat picks up.', '', 'Tsim Sha Tsui Public Pier clock tower')
P('aqualuna', ['Aqua Luna'], 'Aqua Luna', '張保仔號',
  'A traditional wooden Chinese junk with three deep red sails, one of the last built in Hong Kong. It cruises Victoria Harbour in the evening, and you sit on cushioned loungers on deck with a drink while the skyline lights up.',
  'Confirm the sailing is running before you fly. Tickets are non-refundable.', 'Aqua Luna junk boat Hong Kong')
P('symphony', ['A Symphony of Lights', 'Symphony of Lights'], 'A Symphony of Lights', '幻彩詠香江',
  'A nightly ten minute light and sound show at 20:00. Lasers, searchlights and LED screens on more than 40 towers on both sides of Victoria Harbour flash in time to music.',
  'It is being retired during 2026, so check it is still running.', 'A Symphony of Lights Hong Kong')
P('avenue', ['Avenue of Stars', 'Bruce Lee statue'], 'Avenue of Stars', '星光大道',
  'A waterfront promenade in Tsim Sha Tsui honouring Hong Kong cinema, with handprints of film stars set into the railings and a bronze statue of Bruce Lee. It has the best view of the Hong Kong Island skyline.', '', 'Avenue of Stars Hong Kong Bruce Lee')
P('tst', ['Tsim Sha Tsui'], 'Tsim Sha Tsui', '尖沙咀',
  'The southern tip of Kowloon, facing Hong Kong Island across the harbour. Hotels, shops, museums and restaurants crowd the streets around Nathan Road. Your hotel is here.', '', 'Tsim Sha Tsui Hong Kong')
P('temple-st', ['Temple Street dinner and night market', 'Temple Street night market', 'Temple Street'], 'Temple Street Night Market', '廟街夜市',
  'Hong Kong\'s best known night market. From early evening, stalls fill the street selling clothes, gadgets, jade and souvenirs, beside open-air restaurants serving claypot rice and seafood on plastic tables. Fortune tellers and street singers set up nearby.',
  'Bargain politely at the stalls. Start at about half the asking price.', 'Temple Street Night Market Hong Kong')
P('starferry', ['Star Ferry'], 'Star Ferry', '天星小輪',
  'Green and white ferries that have crossed Victoria Harbour since 1888. The ride between Tsim Sha Tsui and Central takes about ten minutes, costs very little, and is the best cheap view in Hong Kong.',
  'Sit on the upper deck. Pay with Octopus.', 'Star Ferry Hong Kong')
P('graham', ['Graham Street Market'], 'Graham Street Market', '嘉咸街市集',
  'One of Hong Kong\'s oldest street markets, running down a steep lane in Central for more than 160 years. Stalls sell fruit, vegetables, fish, tofu and dried goods beneath the surrounding towers.', '', 'Graham Street Market Central Hong Kong')
P('taikwun', ['Tai Kwun'], 'Tai Kwun', '大館',
  'The former Central Police Station, magistracy and Victoria Prison, built from the 1860s and reopened as an arts and heritage centre. Colonial buildings around two courtyards, with galleries, shops and restaurants.', 'Free to enter.', 'Tai Kwun Hong Kong')
P('pmq', ['PMQ'], 'PMQ', '元創方',
  'A 1950s block of police married quarters, converted into studios and shops for about a hundred local designers and makers.', '', 'PMQ Hong Kong')
P('escalator', ['Mid-Levels escalator'], 'Mid-Levels escalator', '中環至半山自動扶梯',
  'The longest outdoor covered escalator system in the world: 800 metres of moving walkways and escalators climbing the hillside from Central through SoHo. You can step off at any street.',
  'It runs downhill until 10:00, then uphill for the rest of the day.', 'Central Mid-Levels Escalator Hong Kong')
P('peaktram', ['Peak Tram'], 'Peak Tram', '山頂纜車',
  'A funicular railway that has hauled passengers up to Victoria Peak since 1888. It climbs so steeply that the skyscrapers outside appear to lean over.',
  'Sit on the right going up. The seats face backwards on the way down, which is why you take a taxi down.', 'Peak Tram Hong Kong')
P('lugard', ['Lugard Road'], 'Lugard Road', '盧吉道',
  'A flat, shaded footpath that circles the Peak. After about 15 minutes the trees open onto the famous free view: the whole of the harbour and both skylines laid out below.', '', 'Lugard Road lookout Victoria Peak')
P('peak', ['Sunset at the Peak', 'the Peak', 'The Peak'], 'Victoria Peak', '太平山頂',
  'The highest hill on Hong Kong Island, 552 metres up, with the classic view over the skyscrapers of Central, the harbour and Kowloon beyond. It is at its best at sunset and as the lights come on.',
  'It is cooler and breezier than the city below.', 'Victoria Peak Hong Kong view night')
P('soho', ['SoHo'], 'SoHo', '蘇豪',
  'South of Hollywood Road: a steep neighbourhood of narrow streets beside the Mid-Levels escalator, packed with restaurants and bars from every cuisine.', '', 'SoHo Hong Kong restaurants')
P('oldtram', ['old tram', 'Old tram'], 'The old tram, or ding ding', '電車 叮叮',
  'Narrow double decker trams that have run along the north shore of Hong Kong Island since 1904. Locals call them ding dings after the bell. They are slow, cheap and open-windowed, and the front seat upstairs gives a moving view of the neon and street life.',
  'Board at the back, and pay with Octopus at the front as you get off.', 'Hong Kong tram ding ding')
P('wanchai', ['Wan Chai'], 'Wan Chai', '灣仔',
  'A lively older district east of Central, mixing markets, office towers and nightlife. Its ferry pier has a Star Ferry service back to Tsim Sha Tsui.', '', 'Wan Chai Hong Kong')
P('central', ['Central'], 'Central', '中環',
  'Hong Kong\'s business heart, on the north shore of Hong Kong Island: a forest of bank towers with steep older streets, markets and temples climbing the hill behind.', '', 'Central Hong Kong skyline')
P('ngongping', ['Ngong Ping 360', 'Ngong Ping', 'Crystal cabin'], 'Ngong Ping 360', '昂坪360',
  'A 5.7 kilometre cable car on Lantau Island, taking 25 minutes to cross a bay and climb over green mountains to the Big Buddha. You have the Crystal cabin, which has a glass floor.',
  'It closes in high wind, and the view vanishes in low cloud. Your voucher works on any day.', 'Ngong Ping 360 cable car crystal cabin')
P('bigbuddha', ['Big Buddha'], 'Tian Tan Buddha', '天壇大佛',
  'A 34 metre bronze seated Buddha on a hilltop on Lantau Island, reached by 268 steps. It was completed in 1993 and can be seen from across the island on a clear day.', '', 'Tian Tan Buddha Lantau')
P('polin', ['Po Lin Monastery'], 'Po Lin Monastery', '寶蓮禪寺',
  'A large, colourful Buddhist monastery facing the Big Buddha, with ornate halls, incense burners and a vegetarian restaurant.', '', 'Po Lin Monastery Lantau')
P('wisdom', ['Wisdom Path'], 'Wisdom Path', '心經簡林',
  'A short forest walk from the Big Buddha to 38 tall wooden columns set on a hillside, each carved with verses of the Heart Sutra.', '', 'Wisdom Path Lantau')
P('hollywood', ['Hollywood Road'], 'Hollywood Road', '荷李活道',
  'One of Hong Kong\'s oldest streets, running through Central and Sheung Wan, known for antique shops, art galleries and Man Mo Temple.', '', 'Hollywood Road Hong Kong antiques')
P('catst-hk', ['Cat Street antiques'], 'Cat Street', '摩羅上街',
  'Upper Lascar Row, a pedestrian lane of stalls and small shops selling antiques, curios, Mao memorabilia, jade, old posters and bric-a-brac.', 'Bargaining is expected.', 'Cat Street Upper Lascar Row Hong Kong')
P('manmo', ['Man Mo Temple'], 'Man Mo Temple', '文武廟',
  'A dim, atmospheric temple from 1847, dedicated to the gods of literature and war. Giant coils of incense hang from the ceiling and burn for weeks, filling the hall with smoke.', '', 'Man Mo Temple Hong Kong incense coils')
P('sheungwan', ['Sheung Wan'], 'Sheung Wan', '上環',
  'The old Chinese quarter west of Central. Dried seafood and herbal medicine shops sit beside galleries, cafes and vintage and resale stores.', '', 'Sheung Wan Hong Kong')
P('eggtart', ['Egg tart', 'egg tart'], 'Egg tart', '蛋撻',
  'A Hong Kong classic: a small pastry shell filled with smooth, barely set egg custard, served warm from the oven in bakeries and old-style cafes.',
  'Have it with a Hong Kong milk tea.', 'Hong Kong egg tart')
P('ozone', ['Ozone at the Ritz-Carlton', 'Ozone'], 'Ozone at the Ritz-Carlton', 'OZONE',
  'A bar on the 118th floor of the ICC tower, about 480 metres up, and one of the highest bars in the world. It has an open-air terrace and views across the harbour to Hong Kong Island.',
  'No flip flops, and no open shoes or sleeveless tops for men. Go for the 17:50 sunset.', 'Ozone bar Ritz-Carlton Hong Kong')
P('lantau', ['Lantau'], 'Lantau Island', '大嶼山',
  'Hong Kong\'s largest island, mostly green mountains and country park. The airport, the cable car and the Big Buddha are all here.', '', 'Lantau Island Hong Kong')
P('dragonsback', ['Dragon&#x27;s Back'], 'Dragon\'s Back', '龍脊',
  'Hong Kong\'s best known hike, along an undulating ridge on the south-east of Hong Kong Island with sea views on both sides. About two to three hours, ending near the beaches.', '', 'Dragons Back hike Hong Kong')
P('sheko', ['Shek O or Big Wave Bay'], 'Shek O and Big Wave Bay', '石澳 大浪灣',
  'Two small beaches at the end of the Dragon\'s Back hike. Shek O is a laid-back village with a wide sandy beach and seafood restaurants. Big Wave Bay is smaller and popular with surfers.', '', 'Shek O beach Hong Kong')
P('mplus', ['M+ and West Kowloon waterfront', 'M+ and the West Kowloon waterfront', 'M+'], 'M+ and the West Kowloon waterfront', 'M+ 西九文化區',
  'M+ is Hong Kong\'s museum of visual culture, a vast building by Herzog and de Meuron with art, design and architecture from across Asia. Outside, a harbourside park and promenade face the Island skyline.',
  'The indoor option on a wet or grey day.', 'M+ museum West Kowloon Hong Kong')
P('yumcha', ['Yum cha', 'yum cha'], 'Yum cha', '飲茶',
  'Literally "drink tea": the Cantonese tradition of a long morning or lunchtime meal of dim sum, small steamed and fried dishes shared at the table with a pot of tea. Prawn dumplings, pork buns, rice rolls and custard tarts.',
  'Most restaurants stop serving dim sum about 15:00.', 'Hong Kong yum cha dim sum')
P('elements', ['Elements'], 'Elements', '圓方',
  'A large shopping mall at the base of the ICC tower, above Kowloon Station, with a wide choice of restaurants. Ozone is at the top of the same tower.', '', 'Elements mall Kowloon Hong Kong')
P('nathan', ['Nathan Road'], 'Nathan Road', '彌敦道',
  'Kowloon\'s main street, running north from the harbour past your hotel. It is a canyon of shops, hotels and signs, once known as the Golden Mile.', '', 'Nathan Road Hong Kong')

# ---------------- districts, cards and terms added on review ----------------
P('shibuya', ['Shibuya'], 'Shibuya', '渋谷',
  'One of Tokyo\'s busiest districts and the centre of its youth culture: the Scramble Crossing, towers of shops, music venues and thousands of restaurants. Your first hotel is here, and everything on day one is within a 15 minute walk.', '', 'Shibuya Tokyo')
P('shinjuku', ['Shinjuku'], 'Shinjuku', '新宿',
  'Tokyo\'s biggest hub, built around the world\'s busiest station. Skyscrapers and offices on the west side, department stores, neon, bars and nightlife on the east. About seven minutes by train from Shibuya.', '', 'Shinjuku Tokyo night')
P('kyoto', ['Kyoto'], 'Kyoto', '京都',
  'Japan\'s capital for more than a thousand years, until 1868. It was spared wartime bombing, so it still has around 1,600 temples, hundreds of shrines, old wooden streets and gardens, ringed by wooded hills.', '', 'Kyoto Japan')
P('osaka', ['Osaka'], 'Osaka', '大阪',
  'Japan\'s third largest city, about 30 to 50 minutes from Kyoto. It is a merchant town known for street food, humour and neon, louder and more down to earth than Tokyo or Kyoto.', '', 'Osaka Japan')
P('hibiya', ['Hibiya'], 'Hibiya', '日比谷',
  'A small central district between the Imperial Palace and Ginza, with a park, theatres and office towers. It gives its name to your second Tokyo hotel and that leg of the trip.', '', 'Hibiya Tokyo')
P('aoyama', ['Aoyama'], 'Aoyama', '青山',
  'The quieter, more grown-up neighbourhood at the far end of Omotesando: designer flagships, galleries, cafes and small boutiques on leafy streets.', '', 'Aoyama Tokyo')
P('s109', ['Bunkamura-dori and 109', 'Bunkamura-dori, 109', 'Bunkamura-dori'], 'Bunkamura-dori and Shibuya 109', '文化村通り・SHIBUYA109',
  'Shibuya 109 is the silver cylindrical tower of small fashion shops that splits the road just west of the Scramble Crossing. Bunkamura-dori is the street running past it. Both are closed to cars for festival stages on the Sunday.', '', 'Shibuya 109 building')
P('manyo', ['Manyo Club'], 'Manyo Club, Minato Mirai', '横浜みなとみらい 万葉倶楽部',
  'A hot spring spa complex on the Minato Mirai waterfront, with natural spring baths fed by water trucked in from Atami and Yugawara, saunas, lounges and restaurants. On the roof is a long footbath that looks straight at the Cosmo Clock Ferris wheel and Landmark Tower, lit up after dark.',
  'Entry covers the whole spa: about ¥3,500 each plus ¥100 bath tax. There is no footbath-only ticket. Robe and towels included. Open 24 hours, entry from 10:00. Tattoos may be refused at entry: see How-to 22 before you go.', 'Yokohama Minato Mirai Manyo Club')
P('sakuragicho', ['Sakuragichō'], 'Sakuragichō', '桜木町',
  'The railway station for Yokohama\'s Minato Mirai waterfront. The Air Cabin cable car leaves from just outside.', '', 'Sakuragicho Station Yokohama')
P('yamanote', ['JR Yamanote', 'Yamanote line', 'Yamanote'], 'JR Yamanote line', '山手線',
  'The green loop line that circles central Tokyo, linking Shibuya, Harajuku, Shinjuku, Tokyo Station, Shimbashi and Shinagawa. Trains run every few minutes.', 'Suica works on it.', 'JR Yamanote line train')
P('yurakucho', ['Yūrakuchō'], 'Yūrakuchō', '有楽町',
  'The district next to Ginza, known for the brick arches under the railway tracks, which are filled with smoky, cheerful izakaya and yakitori bars.', '', 'Yurakucho under the tracks izakaya')
P('shijo', ['Shijō'], 'Shijō', '四条',
  'Kyoto\'s main east to west shopping street, running from the department stores in the centre across the river to Gion and Yasaka Shrine.', '', 'Shijo street Kyoto')
P('namba', ['Namba'], 'Namba', '難波',
  'The southern centre of Osaka and its main entertainment district. Dōtonbori, Kuromon market and Hōzenji Yokochō are all within a short walk of the station.', '', 'Namba Osaka')
P('resale-osaka', ['Kindal Horie, ALLU, KOMEHYO'], 'Kindal, ALLU and KOMEHYO', 'カインドオル・ALLU・コメ兵',
  'Three of Japan\'s best known secondhand luxury chains, each with a store in this part of Osaka. Kindal leans to designer clothing and streetwear, ALLU to vintage handbags, and KOMEHYO is a large multi-floor store for bags, watches and jewellery. Items are authenticated and graded by condition.',
  'Take the physical passports for tax-free.', 'KOMEHYO Shinsaibashi Osaka')
P('leftout-osaka', ['Nakazakichō, Nakanoshima'], 'Nakazakichō and Nakanoshima', '中崎町・中之島',
  'Two Osaka areas dropped from the plan. Nakazakichō is a pocket of old wooden houses turned into cafes near Umeda. Nakanoshima is a river island with a red brick public hall and art museums.', '', 'Nakazakicho Osaka cafes')
P('universal', ['Universal'], 'Universal Studios Japan', 'ユニバーサル・スタジオ・ジャパン',
  'Osaka\'s big theme park, home to Super Nintendo World. You decided against it, to spend the day in the city.', '', 'Universal Studios Japan')
P('horyuji', ['Hōryū-ji'], 'Hōryū-ji', '法隆寺',
  'A temple outside Nara with the oldest wooden buildings in the world, from the 7th century. It is a separate trip from Nara Park and is not in the plan.', '', 'Horyuji Temple Nara')
P('daiba', ['Daiba'], 'Daiba Station', '台場駅',
  'The Yurikamome stop on Odaiba, right beside the Hilton and the waterfront.', '', 'Daiba Station Odaiba')
P('seascape', ['Seascape'], 'Seascape package', 'シースケープ',
  'Your booking at the Hilton Tokyo Odaiba: a place in the hotel\'s private fireworks viewing area, followed by the dinner buffet at its Seascape restaurant, which faces Rainbow Bridge.',
  'A wristband is needed for both. Confirm where to collect it.', 'Hilton Tokyo Odaiba Seascape restaurant')
P('tamagoyaki', ['Tamagoyaki'], 'Tamagoyaki', '玉子焼き',
  'A sweet, layered Japanese omelette, rolled in a rectangular pan. At Tsukiji it is sold hot on a stick for a couple of hundred yen.', '', 'tamagoyaki Tsukiji market')
P('suica', ['Suica'], 'Suica', 'Suica スイカ',
  'A rechargeable tap card for trains, metros and buses across Japan, which also pays at convenience stores, lockers and vending machines. Yours are already in your Apple Wallets.', 'It does not cover Shinkansen or Narita Express tickets.', 'Suica card Apple Wallet')
P('octopus', ['Octopus'], 'Octopus', '八達通',
  'Hong Kong\'s tap card for the MTR, Star Ferry, trams and buses, also accepted in most shops. Yours are in your Apple Wallets.', '', 'Hong Kong Octopus card')
P('vjw', ['Visit Japan Web'], 'Visit Japan Web', 'Visit Japan Web',
  'Japan\'s online arrival service. You enter your passport, flight and customs details before you fly and receive QR codes to scan at immigration and customs, in place of paper forms.', 'Screenshot the QR codes in case the airport wifi is slow.', 'Visit Japan Web QR code')
P('idp', ['International Driving Permit'], 'International Driving Permit', '国際運転免許証',
  'A paper booklet issued in Australia by the state motoring clubs that translates your licence. Japan accepts only the 1949 Geneva Convention version. Street Kart will not let you drive without the physical permit and your physical licence.', '', 'International Driving Permit Australia')
P('cathay', ['Cathay desks', 'Cathay'], 'Cathay Pacific', '國泰航空',
  'Your airline for all four flights: CX104 Melbourne to Hong Kong, CX524 on to Tokyo Narita, CX543 from Haneda to Hong Kong, and CX105 home to Melbourne.', 'Check in online in the app the day before.', 'Cathay Pacific check-in desks')
P('klook', ['Klook Fast Track', 'Fast Track', 'Klook'], 'Klook', 'Klook',
  'A travel booking app widely used across Asia for attraction tickets. Your Ngong Ping cable car vouchers come from it, and it sells the Peak Tram Fast Track ticket, which skips the queue and runs Friday to Sunday only.', '', 'Klook app tickets')
P('kowloon', ['Kowloon'], 'Kowloon', '九龍',
  'The peninsula on the mainland side of Victoria Harbour, facing Hong Kong Island. It is denser and more local in feel. Your hotel, Temple Street and the ICC tower are all in Kowloon.', '', 'Kowloon Hong Kong')
P('tungchung', ['Tung Chung'], 'Tung Chung', '東涌',
  'A new town on Lantau Island at the end of an MTR line. The Ngong Ping cable car terminal is a few minutes\' walk from the station.', '', 'Tung Chung Ngong Ping cable car terminal')
P('races', ['Happy Valley', 'Sha Tin'], 'Hong Kong horse racing', '香港賽馬',
  'Night racing at Happy Valley, a floodlit track ringed by apartment towers on Hong Kong Island, is a classic Wednesday night out. On Wednesday 28 the meeting is at Sha Tin instead, which is further away, so it is not in the plan.', '', 'Happy Valley Racecourse night')

P('jr-rapid', ['JR special rapid', 'JR to Osaka'], 'JR special rapid', 'JR 新快速',
  'The fast JR commuter train between Kyoto and Osaka. It takes about 30 minutes with two stops, runs every 15 minutes and needs no seat booking.', 'Suica works. It is not covered by the Osaka metro day pass.', 'JR special rapid Kyoto Osaka train')
P('subway-k', ['subway'], 'Kyoto subway, Karasuma line', '京都市営地下鉄 烏丸線',
  'Kyoto\'s north to south subway line. Gojō station is three minutes from your hotel, and Kyoto Station is one stop south.', 'Suica works.', 'Kyoto subway Karasuma line Gojo Station', days=[21, 22, 23, 24])
P('karasuma', ['Karasuma-dōri'], 'Karasuma-dōri', '烏丸通',
  'The wide main avenue running north from Kyoto Station through the centre of the city. Your hotel is on it, at the Gojō crossing.', '', 'Karasuma-dori Kyoto')
P('inari-st', ['to Inari', 'Inari'], 'JR Nara line to Inari', 'JR 奈良線 稲荷駅',
  'Inari is the second stop from Kyoto Station on the JR Nara line, about five minutes. The great red gate of Fushimi Inari stands directly opposite the station exit.', 'Local trains only stop here. Rapid trains pass through.', 'JR Inari Station Fushimi Inari')
