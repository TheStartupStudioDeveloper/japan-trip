# Directions under the ⓘ button, per day. Key: day number. Each entry: (start of the item title, [steps]).
# Map links: gm(destination, mode) / am(destination, mode). mode: walking/transit/driving.
from urllib.parse import quote_plus as _q
def gm(dest, mode='walking'): return 'https://www.google.com/maps/dir/?api=1&destination=' + _q(dest) + '&travelmode=' + mode
def am(dest, mode='w'): return 'https://maps.apple.com/?daddr=' + _q(dest) + '&dirflg=' + mode
def maps(dest, g='walking', a='w'): return 'Maps: ' + gm(dest, g) + ' ' + am(dest, a)

GO = {
 21: [
  ('Lunch: Kamameshi Shizuka', [
   'Off the train, follow the signs up and out to Noboriōji-dōri (登大路) and Nara Park (奈良公園), the main road just above the station.',
   'On the street, turn left and walk east, gently uphill. Kōfuku-ji\'s pagoda (wrapped for repairs) is on your right, the Nara Prefectural Office on your left.',
   'About 8 minutes on, at the big crossing where the road to Tōdai-ji turns left, Kamameshi Shizuka is on the left beside the Isuien garden. About 10 to 12 minutes in all.',
   'Order as soon as you sit: the rice is cooked to order, about 20 minutes. Long queue: a kakinoha sushi box instead.',
   'Taxi: the rank outside the station. Say "Shizuka, Isuien". About 5 minutes, about ¥800.',
   maps('Kamameshi Shizuka Nara Park'),
  ]),
  ('Into Nara Park for the deer', [
   'Out of Shizuka, cross Noboriōji to the south side. The open lawns on both sides of the road are full of deer.',
   'Deer crackers (鹿せんべい) are about ¥200 a stack from the small stalls on the lawns. Only buy from the stalls, never from shops.',
   'Feed the smaller does. Stags push and nip. Hold the crackers up high, and show your empty hands when you are done and they will stop.',
   'Head south-east across the lawns towards the Nara National Museum and the start of the Kasuga approach.',
  ]),
  ('Kasuga Taisha', [
   'From the lawns, find the wide gravel approach (参道) heading east into the trees, past the Nara National Museum. Follow it straight. It is gently uphill all the way, about 20 minutes.',
   'The stone lanterns start about halfway and line both sides to the shrine.',
   'At the top: the vermilion south gate (南門). The view from the gate is free. No need to pay for the inner area.',
   'Taxi option: a rank by the Kasuga Taisha car park, just before the shrine, or the GO app.',
   maps('Kasuga Taisha'),
  ]),
  ('Tōdai-ji', [
   'From Kasuga, walk back down the approach to the museum, then cross Noboriōji to the north side and take the road north towards Tōdai-ji (by Shizuka). About 20 to 25 minutes.',
   'Through the giant wooden Nandaimon gate, with the two guardian statues either side.',
   'Ticket for the Great Buddha Hall (大仏殿) at the entrance, about ¥800 each. Open to 17:30.',
   'Inside: walk the full loop around the Buddha. The hole in the pillar at the back is the size of the Buddha\'s nostril.',
   'Taxi from Kasuga: ask for "Tōdai-ji Nandaimon", about 5 minutes.',
   maps('Todaiji Nandaimon'),
  ]),
  ('Optional: Nigatsu-dō', [
   'Leave the Great Buddha Hall by the exit and go left, east, behind the hall. Signs to 二月堂.',
   'A short climb on stone paths, then the covered stone stairway up to the hall. About 10 minutes. Free.',
   'The balcony faces west over the city. Skip it in the rain: the steps get slippery.',
  ]),
  ('Back to Kintetsu Nara', [
   'From the Nandaimon gate walk south to Noboriōji-dōri, then right, west, downhill. Straight along to the station, about 15 to 20 minutes.',
   'The station entrance is the stairs down by the fountain with the Gyōki statue, at the Higashimuki corner.',
   'Taxi: hail one on Noboriōji, or use the GO app. About 5 minutes, about ¥800.',
   maps('Kintetsu Nara Station'),
  ]),
  ('Kintetsu back to Kyoto', [
   'At the machines, tap English. Limited express (特急) to Kyoto (京都): about ¥1,280 each, 35 minutes. Or tap Suica for an Express (急行), ¥760.',
   'Check the board says 京都 (Kyoto). If your Express is not direct, change at Yamato-Saidaiji (大和西大寺), two stops, for a Kyoto train.',
   'Kintetsu Kyoto is the end of the line, on the south side of Kyoto Station.',
  ]),
  ('Ramen: Honke Daiichi Asahi', [
   'From the Kintetsu gates, go up to the 2F North-South Free Passage (南北自由通路) and cross north to the Central Exit (中央口), the Kyoto Tower side.',
   'Outside, turn right and walk east along Shiokōji-dōri, about 5 minutes.',
   'Honke Daiichi Asahi (本家 第一旭, red and white striped sign) and Shinpuku Saikan sit side by side on the left. Queue outside. When the person ahead comes back out, go in and buy your ticket at the machine inside (cash), then rejoin the line. ラーメン is ramen, 特製ラーメン has extra pork.',
   maps('Honke Daiichi Asahi Takabashi Kyoto'),
  ]),
  ('Kyoto Tower at night', [
   'Walk back west along Shiokōji-dōri. The tower stands opposite the station\'s Central Exit.',
   'Go into the Kyoto Tower building and follow the signs for the Observation Deck (展望室) lift. Tickets at the counter, ¥900 each. Last entry 20:30.',
   maps('Kyoto Tower'),
  ]),
  ('To sequence KYOTO GOJO', [
   'Subway: Karasuma line from Kyoto Station, one stop north to Gojō (五条). Tap Suica. Follow the exit signs for Karasuma-dōri, then a 2 to 3 minute walk.',
   'Walk: from the Central Exit, cross to Kyoto Tower and go straight north up Karasuma-dōri, about 15 minutes, flat.',
   'Taxi: the rank outside the Central Exit, about 5 minutes. Say "sequence KYOTO GOJO, Gojō Karasuma".',
   maps('sequence KYOTO GOJO Gojo Karasuma'),
  ]),
  ('Option A', [
   'Massage: walk north up Karasuma-dōri to Shijō-Karasuma, about 10 minutes. YUMEMISHI is open to 21:00, Hannari to 22:00. Book ahead for about 20:00.',
   maps('Yumemishi Shijo Karasuma'),
   'Arcades: from Shijō-Karasuma walk east along Shijō-dōri, under the covered footpath, about 10 minutes. The Teramachi and Shinkyōgoku covered arcades open on the left, just before Kawaramachi.',
   maps('Shinkyogoku Shopping Street Kyoto'),
  ]),
  ('Option B', [
   'Taxi to Shijō-Kawaramachi (四条河原町), about 10 minutes. Or the subway one stop to Shijō, then walk east 15 minutes.',
   'Pontochō: walk east along Shijō to the Shijō Bridge. Just before the bridge, the narrow alley on the left with the 先斗町 sign is Pontochō. Walk it north.',
   'Bee\'s Knees: a few minutes from the north end of Pontochō. The door looks like a bookshop: the bar is behind the bookshelf. Walk-in.',
   maps("Bee's Knees Kyoto"),
  ]),
 ],
}

GO[22] = [
 ('To Kyoto Station, then JR to Tennōji', [
  'From the hotel: Karasuma subway one stop south to Kyoto Station, or 15 minutes on foot down Karasuma-dōri.',
  'At Kyoto Station, tap Suica through the JR gates. Take a JR Special Rapid (新快速) towards Osaka (大阪) / Himeji. Check the board: platforms 4 or 5 usually. About 30 minutes, stay on to Osaka.',
  'At Osaka, follow the orange signs for the Osaka Loop line (大阪環状線). Take a train to Tennōji (天王寺): either direction works, but the platform for 天王寺 方面 via Kyōbashi or via Nishikujō is shown on the board. About 20 minutes.',
  maps('Tennoji Station Osaka', 'transit', 'r'),
 ]),
 ('Shitennō-ji flea market', [
  'At Tennōji, exit for Shitennō-ji (四天王寺) on the north side. Walk north up Tanimachi-suji, about 10 minutes. The big stone torii gate (西大門 side) or the south gate leads into the grounds.',
  'The stalls fill the outer grounds around the temple buildings and the pagoda. Walk the loop once, then go back for what you liked.',
  'Cash only. Prices vary between stalls, and a little friendly haggling is fine at some.',
  maps('Shitennoji Osaka'),
 ]),
 ('Shinsekai', [
  'From the west gate of Shitennō-ji, walk west along the main road (Ōsaka Prefectural Route) towards the Tsūtenkaku tower, which you can see ahead. About 15 minutes, through or past Tennōji Park.',
  'Janjan-Yokochō is the narrow covered alley running north from Dōbutsuen-mae station into Shinsekai. Tsūtenkaku stands at the centre.',
  maps('Tsutenkaku Osaka'),
 ]),
 ('Kushikatsu lunch: Daruma', [
  'Daruma Shinsekai main store is a minute south of Tsūtenkaku, with the angry chef statue outside.',
  'Order a set, or point at the picture menu. Dip each skewer once in the shared sauce. Never double-dip. Use the free cabbage to scoop more sauce.',
  maps('Kushikatsu Daruma Shinsekai Sohonten'),
 ]),
 ('Midōsuji line to Namba', [
  'Walk Janjan-Yokochō away from Tsūtenkaku (tower behind you) to the end of the covered lane. The Dōbutsuen-mae (動物園前) subway stairs, red M sign, are at the junction. About 3 minutes.',
  'Take the red Midōsuji line (御堂筋線) towards Umeda / Shin-Osaka, two stops to Namba (なんば).',
  'Buy the Enjoy Eco Card at the ticket machine (English menu), about ¥820. Use it for every metro ride today.',
 ]),
 ('Rikuro cheesecake', [
  'At Namba, take exit 11 towards Namba Walk or the street, then walk to Rikuro\'s Namba main store, about 3 minutes. Three queues: freshly baked, pre-made, and the café.',
  '551 Hōrai\'s main store is a minute away on the Ebisubashi-suji arcade. Takeaway counter at the front.',
  maps('Rikuro Ojisan Namba Honten'),
 ]),
 ('Namba Yasaka Shrine', [
  'About 10 minutes on foot west from Namba, past Namba Parks. The lion head stage is right in front as you enter.',
  maps('Namba Yasaka Shrine'),
 ]),
 ('KOMEHYO Shinsaibashi', [
  'From Namba Yasaka, walk back east and up Midōsuji or the Shinsaibashi-suji covered arcade, about 15 minutes. Or Midōsuji line Namba to Shinsaibashi, one stop.',
  'KOMEHYO is on the Shinsaibashi-suji arcade, 2-1-23. Bags and watches are on the lower floors.',
  maps('KOMEHYO Osaka Shinsaibashi'),
 ]),
 ('Takoyaki in Dōtonbori', [
  'Walk south down Shinsaibashi-suji to Ebisu Bridge over the canal: that is Dōtonbori. Turn left along the canal street.',
  'Kukuru is under the giant octopus. Any busy stand is good. Then find a café to sit for half an hour.',
  maps('Takoyaki Kukuru Dotonbori'),
 ]),
 ('Umeda Sky deck', [
  'Midōsuji line from Shinsaibashi or Namba to Umeda (梅田), about 7 to 10 minutes, on the Enjoy Eco Card.',
  'Follow signs for the Umeda Sky Building, through the underground mall (north-west), then past Grand Front. About 15 minutes on foot.',
  'Lift to the 35th floor, then the long escalator across the gap to the 39th floor ticket desk. The open-air deck is on the roof.',
  maps('Umeda Sky Building'),
 ]),
 ('Midōsuji line back to Namba', [
  'Walk back to Umeda station (梅田), Midōsuji line towards Namba / Tennōji, 4 stops, about 10 minutes.',
 ]),
 ('Dōtonbori as the lights', [
  'From Namba exit 14, walk north up Midōsuji to the canal, about 5 minutes.',
  'Tombori River Cruise tickets: the booth by the Don Quijote ferris wheel on the canal. Cruise about 20 minutes.',
  'Glico Running Man: best view from Ebisu Bridge.',
  maps('Tombori River Cruise'),
 ]),
 ('Okonomiyaki dinner: Mizuno', [
  'Mizuno is on the Dōtonbori main street, 1-4-15, a few minutes east of Ebisu Bridge. Expect a short queue.',
  'Hōzenji Yokochō is two streets south: a stone lane with lanterns and the moss-covered Mizukake Fudō. Splash a ladle of water on the statue.',
  maps('Okonomiyaki Mizuno Dotonbori'),
 ]),
 ('Taxi to Osaka Castle', [
  'Taxis wait along Midōsuji near Namba and Dōtonbori. Show "大阪城 大手門" (Ōsaka-jō, Ōtemon). About 15 minutes.',
  'From Ōtemon gate walk in through the big stone gates to the keep, about 10 to 15 minutes, following the crowds to the south face.',
  'Metro instead: Sennichimae line Namba to Tanimachi 9-chōme, then Tanimachi line two stops to Tanimachi 4-chōme, then 15 minutes on foot.',
  maps('Osaka Castle Otemon Gate'),
 ]),
 ('Home: taxi to JR Osaka (old)', [
  'Walk back out to Ōtemon or the road by the Hōkoku shrine and take a taxi to JR Osaka station (大阪駅), about 15 minutes, about ¥2,000.',
  'Or walk 15 minutes north-east to JR Osakajōkōen station and take the Loop line to Osaka.',
  'At Osaka, JR Special Rapid (新快速) to Kyoto, about 30 minutes. Then the Karasuma subway one stop to Gojō, or a taxi.',
 ]),
]

GO[22] += [
 ('Amerikamura and Triangle Park', [
  'From KOMEHYO, walk west across Midōsuji (the big boulevard), about 5 minutes. Triangle Park (三角公園) is the little triangular plaza at the centre of Amerikamura.',
  'Kōgaryū takoyaki is on the corner by the park. Queue, then eat on the park steps.',
  maps('Triangle Park Amerikamura Osaka'),
 ]),
 ('Kuromon Market street eats', [
  'From Amerikamura, walk east along Dōtonbori to Sakaisuji, then south to Kuromon, about 20 minutes. Or a taxi, about 5 minutes: say "Kuromon Ichiba" (黒門市場).',
  'Look for wagyu skewers, tamagoyaki, strawberries and fruit cups, and mochi. Prices on the boards. Many stalls close by about 17:00.',
  maps('Kuromon Ichiba Market'),
 ]),
 ('Hōzenji Yokochō', [
  'From Dōtonbori, walk south one street from the canal near Nakaza Cuidaore Building. Hōzenji Yokochō is the narrow stone-paved lane with lanterns.',
  'Mizukake Fudō is the moss-covered statue at the temple. Take a ladle, splash water on it, make a wish.',
  maps('Hozenji Yokocho Osaka'),
 ]),
 ('Taxi to Umeda Sky', [
  'From the castle, walk back out to Ōtemon or the main road and wave down a taxi. Show "梅田スカイビル" (Umeda Sky Building). About 15 minutes.',
 ]),
 ('Walk to JR Osaka', [
  'From the Umeda Sky Building, walk south-east through the underpass and past Grand Front Osaka to JR Osaka station (大阪駅), about 15 minutes.',
  'JR Special Rapid (新快速) towards Kyoto, about 30 minutes. Check the board for 京都.',
  'At Kyoto, Karasuma subway one stop to Gojō, or a short taxi.',
  maps('JR Osaka Station'),
 ]),
]

GO[22] += [
 ('Free time: Shinsaibashi', [
  'Don Quijote and the ferris wheel: on the north bank of the Dōtonbori canal, about 2 minutes east of Ebisu Bridge (the Glico sign bridge). Walk along the canal-side boardwalk. The yellow oval ferris wheel is on the front of the building.',
  maps('Don Quijote Dotonbori'),
  'Tombori River Cruise: the pier is right below Don Quijote on the canal. Buy tickets at the booth there, about 20 minutes.',
  'KOMEHYO: up the Shinsaibashi-suji covered arcade, 2-1-23. Amerikamura: across Midōsuji to the west, Triangle Park at the centre.',
  maps('KOMEHYO Osaka Shinsaibashi'),
  'Mizuno okonomiyaki: on the Dōtonbori main street, a few minutes east of Ebisu Bridge. Hōzenji Yokochō is two streets south.',
  maps('Okonomiyaki Mizuno Dotonbori'),
 ]),
]

GO[22] += [
 ('Free time: the Dōtonbori', [
  'Glico Running Man: best photo from Ebisu Bridge (戎橋), the bridge on Midōsuji\'s side of the canal.',
  'Don Quijote ferris wheel (Ebisu Tower): north bank, 2 minutes east of Ebisu Bridge along the canal boardwalk. Go into Don Quijote, take the stairs by the first-floor tax-free counter to the ticket machine. ¥1,000, about 15 minutes, last ride 21:30.',
  'Tombori River Cruise: the pier is on the canal right below Don Quijote. Tickets at the booth, about ¥1,500. Boats about every 30 minutes, about 20 minutes long.',
  maps('Don Quijote Dotonbori'),
  'Mizuno okonomiyaki: Dōtonbori main street, 1-4-15, a few minutes east of Ebisu Bridge on the south side. Expect a short queue.',
  maps('Okonomiyaki Mizuno Dotonbori'),
  'Kukuru takoyaki: under the giant octopus on the main street. The Kani Dōraku crab and Kuidaore Tarō are on the same street.',
  'Hōzenji Yokochō: one street south of the main street, near Nakaza Cuidaore. Splash water on the Mizukake Fudō statue.',
  'KOMEHYO and Amerikamura: north up the Shinsaibashi-suji arcade for KOMEHYO, or west across Midōsuji for Amerikamura and Triangle Park.',
 ]),
]

GO[22] += [
 ('Walk to JR Osakajōkōen', [
  'From the keep, walk down the north side to Gokuraku-bashi (極楽橋), the wooden bridge over the inner moat. This is the castle exit to use.',
  'Over the bridge, turn right (east) along the path between the moats. The big Osaka-jō Hall is ahead on your left.',
  'Go out through Aoyamon gate (青屋門), over the outer moat bridge, and keep heading east past Osaka-jō Hall.',
  'The station is on the far side of the park road: JR 大阪城公園駅 (Ōsakajōkōen). About 15 minutes in all from the keep.',
  maps('Osakajokoen Station'),
 ]),
 ('JR Loop line to Osaka', [
  'At Ōsakajōkōen, tap Suica and go to the platform for 京橋・大阪方面 (Kyōbashi and Osaka). It is the outer loop, 外回り. Not the Tennōji direction.',
  'Ride 4 stops to Osaka (大阪), about 10 minutes: Kyōbashi, Sakuranomiya, Temma, Osaka.',
  'At Osaka, stay inside the gates. Follow the JR 京都線 (Kyoto line) signs, usually platform 7 or 8. Check the board for 新快速 (special rapid) to 京都. About every 15 minutes, about 30 minutes to Kyoto.',
  'At Kyoto, follow the subway (地下鉄) signs down to the Karasuma line. Tap out of JR, tap in to the subway. Platform toward 国際会館 (Kokusaikaikan), one stop to Gojō (五条).',
  'At Gojō, follow the exit signs for Karasuma-dōri, then a 2 to 3 minute walk to sequence KYOTO GOJO.',
  maps('Kyoto Station', 'transit', 'r'),
 ]),
]
GO[22] += [
 ('Keihan line to Kyoto', [
  'At Temmabashi, follow the green Keihan (京阪) signs, not the Osaka Metro ones. Tap Suica.',
  'Platform for 京都・出町柳方面 (Kyoto, Demachiyanagi). Take the 特急 (limited express, red sign). About 45 minutes.',
  'Get off at 七条 (Shichijō). The limited express does not stop at Kiyomizu-Gojō.',
  'Up to street level, take a taxi: "sequence KYOTO GOJO, Gojō Karasuma", about 5 minutes. Or walk about 18 minutes.',
  maps('sequence KYOTO GOJO Gojo Karasuma'),
 ]),
]

GO[23] = [
 ('Taxi to the bamboo grove', [
  'Taxi from the hotel door or the rank on Karasuma-dōri. Show: 嵐山 竹林の小径、野宮神社までお願いします (Arashiyama bamboo grove, to Nonomiya Shrine, please).',
  'About 25 minutes, about ¥3,500. The bamboo path starts beside Nonomiya Shrine.',
  maps('Nonomiya Shrine Arashiyama', 'driving', 'd'),
 ]),
 ('Bamboo grove', [
  'From Nonomiya Shrine, walk west along the bamboo path, gently uphill, about 10 minutes to the Ōkōchi Sansō gate at the top.',
  'Come back down the same way. Tenryū-ji\'s north gate is on the left (south) side of the path, about halfway.',
  maps('Arashiyama Bamboo Grove'),
 ]),
 ('Tenryū-ji garden', [
  'North gate on the bamboo path, opens 08:30. Buy the garden ticket at the gate.',
  'Loop around the pond garden, then leave by the main gate on the east side onto the main street (Saga-Arashiyama main road).',
  maps('Tenryuji Temple north gate'),
 ]),
 ('Togetsukyō bridge and % Arabica', [
  'From Tenryū-ji\'s main gate turn right (south) down the main street, 5 minutes to the river.',
  '% Arabica is on the riverbank just upstream (right) of the bridge, in a small white glass box.',
  maps('% ARABICA Kyoto Arashiyama'),
 ]),
 ('Taxi to Kinkaku-ji', [
  'Taxis wait along the main street near Togetsukyō. Show: 金閣寺までお願いします (Kinkaku-ji, please).',
  'About 20 minutes, about ¥2,500.',
  maps('Kinkakuji Temple Kyoto', 'driving', 'd'),
 ]),
 ('Taxi to Nijō Castle', [
  'Taxis wait at the Kinkaku-ji bus and taxi area by the entrance. Show: 二条城 東大手門までお願いします (Nijō Castle, east main gate, please).',
  'About 15 minutes, about ¥2,000. Tickets are just inside the east gate.',
  maps('Nijo Castle Higashi Otemon', 'driving', 'd'),
 ]),
 ('Lunch: pick one', [
  'Soba Tatsuichi: out of the east gate, cross Horikawa-dōri, walk east along Nijō-dōri, about 5 minutes. Write your name on the list at the door.',
  maps('Soba Tatsuichi Kyoto'),
  'Sarashina: from the east gate walk south down Horikawa then west on Sanjō, about 10 minutes. Cash only.',
  maps('Sarashina soba Sanbo Omiya Kyoto'),
  'Kyosaimi Nomura (to 14:00) and Ichiran Karasuma: taxi about 10 minutes toward the hotel, both near Shijō-Karasuma.',
  maps('Kyosaimi Nomura Kyoto', 'driving', 'd'),
  'Katsugyu Yodobashi: taxi about 15 minutes to Yodobashi Kyoto, 6F, opposite Kyoto Station.',
 ]),
 ('JR Nara line to Inari', [
  'From the hotel: Karasuma subway one stop south to Kyoto, then follow JR signs. Or walk 15 minutes down Karasuma-dōri.',
  'JR Nara line (奈良線) platforms 8 to 10, any train (local is fine), two stops to Inari (稲荷), about 5 minutes. All on Suica.',
  'Out of Inari station, the big orange torii is straight across the road.',
  maps('Fushimi Inari Taisha'),
 ]),
 ('Fushimi Inari', [
  'Through the main gate and the shrine buildings, then into the Senbon Torii (thousand gates). Keep right where the path splits in two.',
  'Yotsutsuji (四ツ辻) is the crossroads with the view over Kyoto, about 40 minutes up. Turn back there.',
  'Short version: turn back at the Okusha Hōhaisho (奥社奉拝所), the shrine at the end of the first double row, about 15 minutes up.',
 ]),
 ('Keihan to Kiyomizu-Gojō', [
  'From the shrine gate walk west down the main shopping street, 3 minutes, to Keihan Fushimi-Inari (伏見稲荷) station, across the level crossing.',
  'Platform for 京都・出町柳 (toward Kyoto). Take the local (普通), 3 stops to 清水五条 (Kiyomizu-Gojō). The semi-express may skip Fushimi-Inari, so take the first that stops.',
  'Up to Gojō-dōri. Taxi up to Kiyomizu-dera, about 5 minutes: 清水寺までお願いします. Or walk east up Gojōzaka, about 20 minutes uphill.',
  maps('Kiyomizu-dera'),
 ]),
 ('Down through Sannenzaka', [
  'Leave Kiyomizu down Kiyomizu-zaka, then turn right at the shop corner down the stone steps of Sannenzaka (三年坂).',
  'At the bottom keep left onto Ninenzaka (二年坂). The Yasaka Pagoda is just off to the left.',
  maps('Ninenzaka Kyoto'),
 ]),
 ('Yasaka shrine, then down into Gion', [
  'From the pagoda, north along Nene-no-michi, past Kōdai-ji, into Maruyama Park and through to Yasaka Shrine.',
  'Out of the shrine\'s west gate onto Shijō-dōri. Hanamikoji is the second lane on the left. Shirakawa is north across Shijō.',
  maps('Yasaka Shrine Kyoto'),
 ]),
 ('Chao Chao gyoza', [
  'West along Shijō-dōri over the Kamo River (Shijō Bridge), right up Kiyamachi-dōri along the little canal, about 15 minutes to Sanjō.',
  maps('Chao Chao Sanjo Kiyamachi'),
 ]),
 ('Pontochō alley', [
  'One lane west of the river, between Sanjō and Shijō. Enter from the Sanjō end, just south of Chao Chao, and walk south.',
  'Taxi home from Shijō-dōri at the bottom, about 10 minutes: シークエンス京都五条 (sequence KYOTO GOJO), 五条烏丸.',
  maps('Pontocho Kyoto'),
 ]),
]

GO[24] = [
 ('Slow breakfast', [
  'Inoda Coffee: taxi about 10 minutes, or 15 minutes on foot up Karasuma then east on Sanjō. Sakaimachi-dōri, just south of Sanjō.',
  maps('Inoda Coffee Honten Kyoto'),
  'Smart Coffee: taxi about 10 minutes to the Teramachi arcade, near Sanjō. Covered arcade, good in the rain.',
  maps('Smart Coffee Teramachi Kyoto'),
  'Kyosaimi Nomura: 10 minutes on foot north up Karasuma-dōri, west side, just past Shijō.',
  maps('Kyosaimi Nomura Kyoto'),
  'Breakfast Udon Express: 12 minutes on foot north, just past Shijō-Karasuma. Before 10:00 only.',
  maps('Breakfast Udon Express Kyoto'),
 ]),
]

# 22 Oct 22:50: lighter Fri 23.
GO[23] = [g for g in GO[23] if not g[0].startswith(('Taxi to Nijō', 'Lunch', 'Keihan', 'Yasaka shrine', 'Chao Chao', 'Bamboo grove', 'Fushimi Inari'))]
GO[23] += [
 ('Bamboo grove, one way', [
  'From Nonomiya Shrine walk west along the bamboo path, flat, about 5 to 10 minutes.',
  'Tenryū-ji\'s north gate is on the left (south) side, where the path bends. Wait here for 08:30 if early, or carry on up to the Ōkōchi Sansō gate and back (about 15 minutes, uphill).',
  maps('Tenryuji north gate Arashiyama'),
 ]),
 ('Taxi to lunch', [
  'Taxis wait by the Kinkaku-ji entrance. For Kyosaimi Nomura or Ichiran: 四条烏丸までお願いします (Shijō-Karasuma, please). For Katsugyu: ヨドバシカメラ京都 (Yodobashi Kyoto). For Soba Tatsuichi: 二条城 (Nijō Castle), then 5 minutes east on foot.',
 ]),
 ('Lunch: pick one', [
  'Kyosaimi Nomura: Karasuma-dōri, west side, just north of Shijō. Order at the ticket machine.',
  maps('Kyosaimi Nomura Kyoto'),
  'Ichiran Kyoto Karasuma: a minute from Shijō-Karasuma. Ticket machine at the door.',
  maps('ICHIRAN Kyoto Karasuma'),
  'Katsugyu Yodobashi: Yodobashi Kyoto 6F, opposite Kyoto Station. Ten minutes on foot from the hotel.',
  maps('Gyukatsu Kyoto Katsugyu Kyoto Yodobashi'),
  'Soba Tatsuichi: Nijō-dōri, 5 minutes east of Nijō Castle\'s east gate. Name on the list at the door.',
  maps('Soba Tatsuichi Kyoto'),
 ]),
 ('Fushimi Inari, short loop', [
  'Through the big torii and up the steps past the main shrine. Follow the crowd to the Senbon Torii, the two rows of gates side by side. Take the right-hand row.',
  'At the end is the Okusha Hōhaisho (奥社奉拝所), about 15 minutes up, with the omokaru stones you lift to make a wish. Turn back here, or go 5 to 10 minutes further for quieter gates.',
  'Back down the same way.',
  maps('Fushimi Inari Taisha'),
 ]),
 ('Taxi to Kiyomizu-dera', [
  'Taxis pass on the road in front of the big torii, by Inari station. Show: 清水寺までお願いします (Kiyomizu-dera, please).',
  'The taxi drops you at the top of Kiyomizu-zaka or Gojōzaka, a few minutes\' walk from the gate.',
  maps('Kiyomizu-dera', 'driving', 'd'),
 ]),
 ('Hanamikoji and Gion', [
  'From the Yasaka Pagoda go west down the lane (Yasaka-dōri) to Higashiōji-dōri, cross, and keep going west to Hanamikoji.',
  'Walk north up Hanamikoji to Shijō-dōri. Taxis on Shijō.',
  maps('Hanamikoji Street Kyoto'),
 ]),
 ('Taxi to Chao Chao', [
  'Taxi on Shijō-dōri heading west. Show: 三条木屋町 餃子ChaoChao (Sanjō Kiyamachi, Chao Chao gyoza). About 5 minutes.',
  maps('Chao Chao Sanjo Kiyamachi'),
 ]),
]
GO[24] += [
 ('Optional: Nijō Castle', [
  'Taxi from the hotel: 二条城 東大手門までお願いします (Nijō Castle, east main gate). About 10 minutes.',
  'Tickets just inside the gate. Follow the arrows to the Ninomaru Palace, shoes off, one-way route through the rooms. Then back out the same gate.',
  'Taxis wait on Horikawa-dōri outside the gate. To Inoda: イノダコーヒ本店 (Inoda Coffee main shop), about 10 minutes.',
  maps('Nijo Castle Higashi Otemon', 'driving', 'd'),
 ]),
]

# 23 Oct 09:55: Inari before lunch, Ichiran after.
GO[23] = [g for g in GO[23] if not g[0].startswith(('Taxi to lunch', 'Lunch', 'JR Nara line to Inari', 'Taxi to Kiyomizu-dera', 'Taxi to Chao Chao', 'Chao Chao'))]
GO[23] += [
 ('Taxi to Kyoto Station', [
  'Taxis wait by the Kinkaku-ji entrance. Show: 京都駅までお願いします (Kyoto Station, please).',
  'About 25 minutes, about ¥3,000. Either side of the station is fine; the JR gates are in the middle.',
  maps('Kyoto Station', 'driving', 'd'),
 ]),
 ('JR Nara line to Inari', [
  'In through the JR gates (Suica), follow the 奈良線 (Nara line) signs, platforms 8 to 10. Any train, two stops to 稲荷 (Inari), about 5 minutes.',
  'Out of Inari station, the big orange torii is straight across the road.',
  maps('Fushimi Inari Taisha'),
 ]),
 ('JR back to Kyoto, subway to Shijō', [
  'Inari station, platform for 京都 (Kyoto), two stops.',
  'At Kyoto, follow 地下鉄 烏丸線 (Karasuma subway) signs. Tap out of JR, tap in to the subway. Toward 国際会館, two stops to 四条 (Shijō).',
  'Ichiran is a minute from the Shijō exits on Karasuma-dōri.',
  maps('ICHIRAN Kyoto Karasuma'),
 ]),
 ('Lunch: Ichiran', [
  'Buy tickets at the machine by the door, then wait for two booths. Fill in the sheet: richness, garlic, green onion, chashu, red sauce, noodle firmness.',
  'To the hotel after: walk south down Karasuma-dōri, about 10 minutes, or the subway one stop to Gojō.',
  maps('sequence KYOTO GOJO Gojo Karasuma'),
 ]),
 ('Taxi to Kiyomizu-dera', [
  'Taxi from the hotel door. Show: 清水寺までお願いします (Kiyomizu-dera, please). About 10 minutes.',
  'The drop is at the top of Kiyomizu-zaka or Gojōzaka, a few minutes\' walk up to the gate.',
  maps('Kiyomizu-dera', 'driving', 'd'),
 ]),
 ('Walk to Chao Chao', [
  'From Hanamikoji, out onto Shijō-dōri and turn left (west). Over the Kamo River on Shijō Bridge.',
  'Just over the bridge turn right up Kiyamachi-dōri, along the little canal, about 10 minutes to Sanjō. Chao Chao is on the canal side.',
  maps('Chao Chao Sanjo Kiyamachi'),
 ]),
]

GO[23] += [
 ('Bus or taxi to Kyoto Station', [
  'Bus: out of the Kinkaku-ji gate, walk down the approach to the main road (Nishiōji-dōri), about 5 minutes, to the Kinkakuji-michi stop (金閣寺道).',
  'Take bus 205 showing 京都駅 (Kyoto Station). Check the sign at the stop says 京都駅. In by the rear door, tap Suica, out by the front door. About 40 minutes to the bus terminal in front of the station.',
  maps('Kinkakuji-michi bus stop', 'transit', 'r'),
  'Taxi: the rank by the Kinkaku-ji entrance. Show 京都駅までお願いします. About 25 minutes, about ¥3,000.',
 ]),
]
