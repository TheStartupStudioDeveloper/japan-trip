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
