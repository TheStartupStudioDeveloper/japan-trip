# V2.3 amendments. Applied on top of V2.2. Content only.
def _row(day, t):
    return [x[0] for x in D[day]['rows']].index(t)

# ---------- 1. Street Kart: shoes and physical documents ----------
D[18]['rows'][_row(18, '15:30')] = R('15:30', 'Arrive 30 minutes early', 'Fully closed shoes on. Physical licence card, physical International Driving Permit and passports in hand. No digital copies.')
KART = ' Closed shoes, physical licence and permit.'
e = D[25]['extra']; D[25]['extra'] = (e[0], [(e[1][0][0], e[1][0][1] + KART), e[1][1]])
e = D[26]['extra']; D[26]['extra'] = (e[0], [(e[1][0][0], e[1][0][1] + KART), e[1][1]])

# ---------- 2. Shibuya Sky: nothing that needs a locker ----------
D[17]['rows'][_row(17, '14:45')] = R('14:45', 'Supplies, then check in and rest', 'MEGA Don Quijote Shibuya and the nearest 7-Eleven for room supplies. Shower, feet up. Bags stay in the room.')
D[17]['rows'][_row(17, '16:00')] = R('16:00', 'Shibuya Sky', 'Seven minutes\' walk. Phones and pockets only, nothing for a locker (How-to 18). Sunset about 17:00, then the city lights.', B)
D[19]['alts'][1]['list'][1] = 'Shibuya Sky about 16:15, the booked sunset slot. Bags stay at the hotel (How-to 18).'
D[20]['alts'][2]['list'][1] = 'Back to the hotel about 15:00 to pack and leave the bags, then Shibuya Sky at 16:00, the booked backup slot.'
HOWTO.append(('Shibuya Sky, what to leave behind', [
 'Not allowed on the rooftop: bags, backpacks and pouches, hats and caps, tripods and selfie sticks, earbuds and headphones, food and drink, and anything loose that could blow away.',
 'Fine to take: a phone, and a camera on a strap.',
 'Everything else goes into the free lockers on the 46th floor, which means a queue on the way in and again on the way out.',
 'So drop it all at the hotel first, seven minutes away. Wear pockets that close. Take phones, the booking QR code and one card.']))

# ---------- 3. Backup plan: swap Tsukiji and Asakusa ----------
D[20]['alts'][0]['foot'] = 'Backup, to decide with the forecast: Tsukiji here from 08:30 and a longer Yokohama, with Asakusa moving to Monday 26 after teamLab.'
D[26]['notes'].append(('Backup: Asakusa today', 'Decide with the forecast. Tsukiji moves to Tuesday 20, and Asakusa, Kappabashi and the Skytree at dusk come here. Costs the free afternoon.'))

# ---------- 4. Spare socks ----------
i = [t[0] for t in TIPS].index('Shoes')
TIPS[i] = ('Shoes and socks', 'Shoes come off wherever there is a step up or a rack at the door: temples, some restaurants, fitting rooms. Wear good socks, and carry a clean spare pair on temple and shrine days.')

# ---------- 5. Agoda airport pickup ----------
n = D[27]['notes']
n[1] = ('Instead of the taxi in Hong Kong', 'First check whether the Agoda booking includes an airport pickup. Otherwise the Airport Express to Kowloon Station, then a 5 to 10 minute taxi, costs about the same for two with more bag handling.')

# ---------- 6. Fri 30 rebuilt around the late checkout ----------
D[27]['rows'][_row(27, '16:15')] = R('16:15', 'Check in at the Sheraton', 'Ask two things at the desk: whether pool sessions need booking, and the club lounge hours. Friday\'s late checkout is already confirmed to 18:00.')
D[29]['rows'][_row(29, '14:00')] = R('14:00', 'Lunch in Central or Sheung Wan', 'Yum cha is Friday\'s lunch, so eat whatever appeals here.')
D[29]['rows'][_row(29, '18:15')] = R('18:15', 'Optional: Ozone at the Ritz-Carlton', 'Friday is the plan. If you go tonight instead: quick change first, short taxi to ICC, and Friday evening is free.')
D[30].update(title='Pool, yum cha, Ozone at sunset, then departure', cal='Pool, Ozone, fly',
 sum='Late checkout is confirmed to 18:00, so the room is yours all day. A pool morning, yum cha, a spare window for anything missed, a slow pack and shower, Ozone at sunset, dinner, then a taxi at 20:45.',
 rows=[
  R('09:00', 'Lounge breakfast'),
  R('09:45', 'Sheraton pool', 'Optional. The best sun of the day.'),
  R('12:00', 'Quick change, head out'),
  R('12:30', 'Yum cha lunch', 'Dim sum is a daytime meal and most places stop about 15:00. If lunch slips, an all-day dim sum place can stand in for dinner.'),
  R('14:00', 'Spare window', 'About two hours for anything missed. Central by Star Ferry, M+ and the West Kowloon waterfront, or Nathan Road.'),
  R('16:15', 'Back at the hotel, pack and shower', 'No rush. Ask at the desk whether checkout can go later still.'),
  R('17:20', 'Check out', 'You have until 18:00. Leaving now catches the sunset at Ozone. Suitcases go to the concierge.'),
  R('17:40', 'Ozone at the Ritz-Carlton', 'Short taxi to ICC, 118th floor. Sunset at 17:50, then the lights. Open from 16:00. No flip flops, and no open shoes or sleeveless tops for men.', TB),
  R('19:15', 'Dinner', 'At Elements below Ozone, or back in Tsim Sha Tsui close to the bags.'),
  R('20:30', 'Collect bags at the Sheraton'),
  R('20:45', 'Taxi to the airport', '30 to 40 minutes at that hour.'),
  R('21:30', 'Check in at the Cathay desks', 'Three hours before departure.'),
  R('00:30', 'CX105 departs for Melbourne', 'Saturday 31 October.', B),
 ],
 notes=[
  ('Latest safe timing', 'A taxi at 21:15 puts you at the airport by 22:00, which is 2.5 hours before departure.'),
  ('If you missed the Peak or Ngong Ping', 'It takes the morning in place of the pool. The Peak has Klook Fast Track on a Friday, and the Ngong Ping voucher works any day. Be back by 16:15.'),
  ('If Ozone was Thursday', 'Then tonight is free: a harbourfront drink, a longer dinner, or more time in the room.'),
  ('If Friday is wet or grey', 'Skip the pool. M+ and the West Kowloon waterfront is the indoor option, and the room is yours until 18:00.')])
LEGS['h']['sum'] = 'Optional pool time in the sunny hours and evenings in the city. Thursday is the Big Buddha day. Friday has a late checkout: pool, yum cha, a spare afternoon and Ozone at sunset before the 00:30 flight. Wednesday, Thursday and Friday can swap to suit the weather.'
SWAPS[:] = [
 ('Ngong Ping on Friday, instead of Thursday', 'Replaces the Friday pool and yum cha. First cable car at 10:00, back at the hotel by about 15:30 to pack and shower. The Klook voucher moves with you.', 'Costs the easy last morning. A big day before a red-eye.'),
 SWAPS[1],
 ('M+ and West Kowloon waterfront', 'Replaces any pool block on a wet or grey day.', 'Costs pool time. A short taxi from the hotel.'),
]

# ---------- checklist ----------
def _drop(sec, starts):
    items = CHECK[sec][1]
    hit = [x for x in items if x[1].startswith(starts)]
    assert len(hit) == 1, starts
    items.remove(hit[0])
_drop(0, 'W Hong Kong WET'); _drop(0, 'Kerry Hotel'); _drop(0, 'Sheraton: chase'); _drop(1, 'W or Kerry'); _drop(2, 'Sheraton: late checkout')
b4 = CHECK[0][1]
b4.insert(4, ('s', 'Street Kart: pack fully closed shoes, the physical licence card and the physical International Driving Permit'))
b4 += [('h', 'Cynthia: check whether the Agoda booking includes an airport pickup to the Sheraton on Tue 27'),
       ('h', 'Ozone at the Ritz-Carlton: book for Fri 30, about 17:40'),
       ('h', 'Pick a yum cha place for Fri 30 lunch, 12:30')]
CHECK[2][1].insert(-1, ('h', 'Sheraton: Friday late checkout is confirmed to 18:00. Ask if it can go later'))

D[20]['alts'][0]['sum'] = 'Old Tokyo in the morning with the Skytree in view, kitchenware street, then down the bay to Yokohama for the waterfront and Chinatown. The outdoor day: give it the better weather of Monday and Tuesday.'

# ---------- fit ----------
D[17]['sum'] = 'No trains after the airport, just a slow loop on foot from the hotel while you wait for the room. Only the landing and Shibuya Sky are fixed. The other times are a guide.'
D[17]['rows'][_row(17, '13:45')] = R('13:45', 'Wander back into Shibuya', 'Hachikō, the Scramble Crossing, Center-gai. All within a 15 minute walk of the hotel.')
n = D[26]['notes']
D[26]['notes'] = [n[0], ('Other shapes', 'Market first at 08:00 with teamLab at 13:30 makes room for a market tour. If teamLab was used earlier as a wet weather move, the whole morning is the market.'), n[3]]
D[17]['rows'][_row(17, '14:45')] = R('14:45', 'Supplies, then check in and rest', 'Don Quijote and 7-Eleven for room supplies. Shower, feet up. Bags stay in the room.')
D[17]['rows'][_row(17, '16:00')] = R('16:00', 'Shibuya Sky', 'Seven minutes\' walk. Pockets only, no bags (How-to 18). Sunset about 17:00, then the lights.', B)
D[17]['rows'][_row(17, '10:30')] = R('10:30', 'Miyashita Park and Cat Street', 'Start on the rooftop park above the hotel, where the festival will be on. Then Cat Street: streetwear and small cafés. If shattered, stop here.')
D[26]['rows'][_row(26, '12:00')] = R('12:00', 'Tsukiji Outer Market lunch', 'Arrive by 12:30, stalls wind down early. Tamagoyaki, tuna, grilled scallop and uni, strawberry daifuku, Namiyoke shrine. Eat at the stall.')
D[26]['rows'][_row(26, '10:50')] = R('10:50', 'Tokyo Tower and Zōjō-ji', 'About 10 minutes\' walk. The temple gate with the tower behind it. Sky Room Café on 33F first, if you like.')
