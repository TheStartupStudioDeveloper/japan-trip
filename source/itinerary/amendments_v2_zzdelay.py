# Sat 17: CX524 landed 09:35, about 2h45 late. Shift the morning, mark the stretch items optional.
D[17]['sum'] = 'The flight landed at 09:35, almost three hours late. Lunch by the hotel, the festival on the roof, then rest before Shibuya Sky. Anything marked optional can wait for tonight or Sunday.'
D[17]['rows'] = [
 R('09:35', 'Landed at Narita, late', 'CX524 was delayed from 06:50. Get the landing sticker each, then scan it into Visit Japan Web (How-to 4). Allow about an hour to clear.', B),
 R('10:45', 'Narita Express to Shibuya', 'Next train that stops at Shibuya (How-to 5). About 80 minutes.'),
 R('12:15', 'Shibuya Station, bags to the hotel', 'Hachikō exit, lobby on 4F (How-to 6). Ask about early check-in: free if a room is ready, bags held until then.'),
 R('12:30', 'Lunch under the hotel', 'Shibuya Yokochō, on the ground floor of Miyashita Park, or anywhere in the park building. No walking needed.'),
 R('13:30', 'Miyashita Park rooftop and the festival', 'Straight upstairs from lunch.'),
 R('14:00', 'Optional: Cat Street and Omotesando', 'Only with the legs for it. Otherwise it moves to Sunday, where it sits right after Harajuku.'),
 R('14:45', 'Supplies, then check in if the room is ready', 'Don Quijote and 7-Eleven. Shower, feet up. No room yet: bags stay at the desk until after Shibuya Sky.'),
 R('16:00', 'Shibuya Sky', "Seven minutes' walk. Pockets only, no bags (How-to 7). Sunset about 17:00, then the lights.", B),
 R('18:00', 'Optional: the Scramble Crossing from above', 'Free: Shibuya Mark City walkway, or Hikarie Sky Lobby 11F (open to midnight). With a drink: MAGNET by SHIBUYA109 rooftop, ¥1,800 with one drink. Or leave it for Sunday.'),
 R('18:30', 'Dinner close by', 'Nonbei Yokochō or Dōgenzaka, then an early night.'),
]
_rs = D[18]['rows']
_rs[_row(18, '12:15')] = R('12:15', 'Lunch in Harajuku or Omotesando', 'If Omotesando was skipped yesterday: Omotesando Hills, Tod&#x27;s and Dior are ten minutes from Takeshita Street.')
_rs[_row(18, '13:15')] = R('13:15', 'Cat Street back into the festival streets', 'Dōgenzaka, Bunkamura-dori, 109. Dip in and out. Optional, if missed last night: the Scramble Crossing from above, free from the Mark City walkway or Hikarie Sky Lobby 11F.')
