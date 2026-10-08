# Master V2 updates. Version label stays V2.

# Sat 17: sequence check-in is 17:00 as standard
D[17]['rows'][_row(17, '10:00')] = R('10:00', 'Shibuya Station, bags to the hotel', 'Walk from the Hachikō exit, lobby on 4F (How-to 6). Leave the bags. Standard check-in is 17:00, so confirm the early check-in.')
D[17]['rows'][_row(17, '14:45')] = R('14:45', 'Supplies, then check in if the room is ready', 'Don Quijote and 7-Eleven for room supplies. With early check-in: shower, feet up. Without it, bags stay at the desk and check-in follows Shibuya Sky.')

# Sat 24: pre-registration at the Blossom
D[24]['rows'][_row(24, '15:00')] = R('15:00', 'Check in at Hotel The Blossom Hibiya', 'Pre-registered if the hotel allows it, so arrival is keys only. An hour to shower and change. Take a layer, the bay is cool after dark.')

# Checklist
_og = CHECK[-1][1]; _i = [x[1][:10] for x in _og].index('Sat 17: as'); del _og[_i]
_bk = CHECK[1][1]
_i = [x[1][:11] for x in _bk].index('Shibuya Sky')
_bk.insert(_i + 1, ('s', 'Ask Sequence Miyashita Park for early check-in on Sat 17. Standard check-in is 17:00'))
_i = [x[1][:7] for x in _bk].index('Confirm')
_bk.insert(_i, ('g', 'Ask the Blossom about pre-registering for Sat 24, so arrival is keys only'))

# Laundry: the Blossom has a guest laundry
_i = [h[0] for h in HOWTO].index('Laundry, Sun 25'); _h = HOWTO[_i]
_j = [s[:12] for s in _h[1]].index('Ask at the f')
_h[1][_j] = 'The Blossom has a guest laundry with only a few machines, so go early. Not confirmed for sequence KYOTO GOJO, so ask at check-in there.'

# How-to 1: all four hotels in local script, in trip order
_i = [h[0] for h in HOWTO].index('Phones and power'); _h = HOWTO[_i]
_j = [x[:12] for x in _h[1]].index('Two to start')
_h[1][_j:_j+1] = [
 'sequence MIYASHITA PARK, Shibuya: 東京都渋谷区神宮前6-20-10 MIYASHITA PARK North.',
 'sequence KYOTO GOJO: 京都府京都市下京区五条烏丸町409.',
 'THE BLOSSOM HIBIYA, Tokyo: 東京都港区新橋1-1-13.',
 'Sheraton Hong Kong, 香港喜來登酒店: 九龍尖沙咀彌敦道20號.']

# ---------- sequence KYOTO GOJO is at Karasuma-Gojō, by Gojō subway station ----------
def _how(title): return HOWTO[[h[0] for h in HOWTO].index(title)][1]
# Wed 21
D[21]['rows'][_row(21, '17:25')] = R('17:25', 'Walk to sequence KYOTO GOJO', 'About 15 minutes straight up Karasuma-dōri with the bags, or one subway stop to Gojō (How-to 13).')
D[21]['rows'][_row(21, '18:00')] = R('17:50', 'Check in, then dinner around Pontochō or Shijō', 'Pontochō is about 20 minutes on foot from the hotel, or one subway stop to Shijō and a ten minute walk east.')
# Thu 22
D[22]['rows'][_row(22, '07:15')] = R('07:00', 'To Kyoto Station, then JR to Osaka', 'One subway stop or a 15 minute walk. JR special rapid to Osaka Station, about 30 minutes, then the Osaka Loop Line to Osakajōkōen for the castle (How-to 14).')
D[22]['rows'][_row(22, '08:20')] = R('08:30', 'Osaka Castle, up close', 'Through the park to the foot of the tower. Not inside. The park is open around the clock. Takeaway breakfast on a bench.')
D[22]['rows'][_row(22, '09:35')] = R('09:35', 'Tanimachi line to Higashi-Umeda', 'From Tanimachi 4-chōme, on the west side of the castle. Buy the one-day Enjoy Eco Card at the metro station, about ¥820. It covers the Osaka Metro all day, not JR.')
D[22]['rows'][_row(22, '21:30')] = R('21:30', 'Home by Midōsuji line and JR', 'Namba to Umeda, then the JR special rapid from Osaka Station to Kyoto, about 30 minutes. One subway stop to Gojō, or a 15 minute walk (How-to 14).')
# Fri 23
D[23]['rows'][_row(23, '06:45')] = R('06:45', 'Leave the hotel', 'One subway stop or a 15 minute walk to Kyoto Station, then the JR Sagano line to Saga-Arashiyama. About 35 minutes door to door.')
D[23]['rows'][_row(23, '14:15')] = R('14:15', 'Kiyomizu-dera', 'About 10 minutes by taxi from Nishiki or the hotel, or 30 minutes on foot along Gojō. The stage view over the city is the thing.')
D[23]['notes'][0] = ('Getting to Higashiyama', 'The hotel is in the centre of the city, not at the foot of the hill. Take a taxi up to Kiyomizu-dera, and the rest of the afternoon runs downhill on foot to Gion. Taxi home after dinner, about 10 minutes.')
# Sat 24
D[24]['rows'][_row(24, '06:45')] = R('06:30', 'To Kyoto Station, then JR Nara line to Inari', 'One subway stop or a 15 minute walk to the station. Inari is two stops, about 5 minutes, and the shrine gate faces the platform. Sunrise is around 06:10.')
D[24]['rows'][_row(24, '10:30')] = R('10:30', 'Check out and walk to Kyoto Station', 'About 15 minutes with the bags, or one subway stop (How-to 16).')
D[24]['foot'] = D[24]['foot'].replace('06:45 start', '06:30 start')
# How-tos
h = _how('Kyoto Station, bags and the walk, Wed 21')
h[[x[:8] for x in h].index('Walk to ')] = 'To sequence KYOTO GOJO: out the north side, the Kyoto Tower side, then straight north up Karasuma-dōri to Gojō. About 15 minutes, flat. Or take the Karasuma subway line one stop to Gojō, then walk 3 minutes.'
h = _how('Kyoto back to Tokyo, Sat 24')
h[0] = 'Check out and leave the hotel at 10:30. Walk straight down Karasuma-dōri, about 15 minutes, or take the subway one stop.'
HOWTO[[x[0] for x in HOWTO].index('Osaka there and back, Thu 22')] = ('Osaka there and back, Thu 22', [
 'Out: one subway stop from Gojō to Kyoto Station, or a 15 minute walk. Leave the hotel at 07:00.',
 'JR special rapid from Kyoto to Osaka Station, about 30 minutes. They run every 15 minutes and Suica works. No seat booking.',
 'At Osaka, change to the JR Osaka Loop Line, outer loop, to Osakajōkōen. About 10 minutes. The castle park is at the exit.',
 'After the castle, walk to Tanimachi 4-chōme on its west side and buy the Enjoy Eco Card day pass at the metro ticket machine. About ¥820 on a weekday. It covers the Osaka Metro, not JR.',
 'Back: Midōsuji line from Namba to Umeda, four stops. Walk through to JR Osaka Station.',
 'JR special rapid to Kyoto, about 30 minutes. Then the subway one stop to Gojō, or walk.',
 'Leaving Namba at 21:30 puts you home about 22:45. The last trains are after 23:30, but check the night before.'])
_og = CHECK[-1][1]; _i = [x[1][:8] for x in _og].index('Wed 21: ')
_og[_i] = ('k', 'Wed 21: check the JR special rapid times to Osaka for Thursday')

# ---------- who booked each hotel ----------
LEGS['s']['hotel'] += '. Booked direct by Cynthia'
LEGS['k']['hotel'] += '. Booked on Booking.com by G'
LEGS['g']['hotel'] += '. Booked on Booking.com by G'
LEGS['h']['hotel'] += '. Booked on Agoda by Cynthia'
