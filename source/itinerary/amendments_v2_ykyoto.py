# ---------- Kyoto evenings split: Pontochō Wed 21, Gion Fri 23. Friday reshaped ----------
_r = D[21]['rows']; _i = _row(21, '16:30')
D[21]['rows'] = _r[:_i] + [
 R('16:30', 'Train back', 'Kyoto by 17:15. Collect the bags.'),
 R('17:15', 'Kyoto Station building', 'Ten minutes while you are here: the grand staircase lights up at dusk, and the free rooftop Sky Garden faces Kyoto Tower.'),
 R('17:35', 'Walk to sequence KYOTO GOJO', 'About 15 minutes straight up Karasuma-dōri with the bags, or one subway stop to Gojō (How-to 13).'),
 R('18:00', 'Check in'),
 R('19:00', 'Pontochō dinner, casual, no booking', 'About 20 minutes on foot, or one subway stop to Shijō. Walk in along Kiyamachi-dōri, the canal street one lane over.'),
 R('20:30', 'Optional: Kamo River and the Shirakawa canal', 'Shijō Bridge is at the end of the alley. Shirakawa is seven minutes beyond, lit and quiet. Or the Teramachi arcades. Taxi home.'),
]
D[21]['foot'] += ' Dinner is Pontochō tonight and Gion on Friday. They can swap.'

_r = D[23]['rows']
D[23]['rows'] = _r[:4] + [
 R('10:15', 'Coffee and a snack in Arashiyama', 'No sit-down breakfast. Lunch is early.'),
 R('10:45', 'Back to the centre', 'About 40 minutes. The Hankyu line to Karasuma, changing at Katsura, comes out beside the market.'),
 R('11:30', 'Nishiki Market lunch', 'Ahead of the lunch crush. Rolled omelette, tofu doughnuts, pickles, skewers. Eat at the stall. Aritsugu, the old knife maker, is at the east end.'),
 R('12:45', 'Walk to the hotel and rest', 'About 15 minutes south. Two hours of rest, or slack if the morning ran long.'),
 R('15:30', 'Kiyomizu-dera', 'Taxi from the hotel at 15:15, about 10 minutes. The top of Higashiyama, the old eastern hills. The stage view over the city is the thing. Closes 18:00.'),
 R('16:30', 'Down through Sannenzaka and Ninenzaka', 'Downhill from Kiyomizu, not uphill from Gion. Steep stone steps, slippery in rain. Shops start closing about 17:30.'),
 R('17:10', 'Yasaka Pagoda at sunset', 'Two minutes off Ninenzaka. The five storey pagoda above the lane roofs.'),
 R('17:30', 'Yasaka shrine, then down into Gion', 'Lanterns lit. Then Hanamikoji, and the Shirakawa canal if you missed it on Wednesday.'),
 R('18:30', 'Dinner in Gion', 'The one special dinner in Kyoto. Book before you leave Melbourne. Friday walk-ins here are hard.', 'tb'),
]
D[23]['sum'] = 'Arashiyama at dawn while it is empty, an early market lunch and a rest, Higashiyama in the late light, Gion for dinner.'
D[23]['notes'] = [
 ('Getting to Higashiyama', 'The hotel is in the centre, not at the foot of the hill. Taxi up to Kiyomizu-dera, then the afternoon runs downhill on foot to Gion. Taxi home after dinner, about 10 minutes.'),
 ('Dinner swap', 'Pontochō on Wednesday, Gion tonight. If the Gion table you want is only free on Wednesday, swap them. Pontochō is five minutes past Gion, over the bridge.'),
 ('Autumn colour', "Late October is green and early gold, not red. Kyoto's maples turn mid to late November.")]
for _g in CHECK:
    _g[1][:] = [(l, 'Gion dinner for Fri 23, 18:30. Pontochō on Wed 21 is walk-in' if t == 'Gion or Pontochō dinner for Fri 23, 18:30' else t) for (l, t) in _g[1]]

# ---------- Nara reordered so nothing doubles back, taxi out, later Kyoto evening ----------
_r = D[21]['rows']; _i = _row(21, '11:30'); _j = _row(21, '19:00')
D[21]['rows'] = _r[:_i] + [
 R('11:30', 'Nara', 'Straight along Sanjō-dōri to the park. All on foot until the taxi back.'),
 R('12:00', 'Lunch on Sanjō-dōri', 'Then Nakatanidō, the shop that pounds mochi at speed in its front window. Two minutes.'),
 R('12:45', 'Kōfuku-ji and the first deer', 'A walk-through. The pagoda is wrapped for repairs until 2034. Deer crackers are about ¥200 at the stalls.'),
 R('13:15', 'Isuien garden, optional', 'Ten minutes north-east. A quiet garden. Skip it for more deer time.'),
 R('14:00', 'Tōdai-ji and the Great Buddha', 'Five minutes, through the Nandaimon gate. The one unmissable thing here.'),
 R('15:00', 'Nigatsu-dō', 'Ten minutes uphill behind the main hall. A balcony with the view over the city. Free.'),
 R('15:30', 'Kasuga Taisha and the lantern path', 'Twenty minutes south along the hill. Quieter, wooded, the better half of Nara.'),
 R('16:15', 'Taxi to JR Nara Station', 'About 10 minutes. Backup: a flat 35 to 40 minute walk back through the park, or the loop bus.'),
 R('16:40', 'Train back', 'Kyoto by 17:25. Collect the bags.'),
 R('17:25', 'Kyoto Station building', 'Ten minutes: the staircase lights up at dusk, and the free rooftop Sky Garden faces Kyoto Tower.'),
 R('17:45', 'Walk to sequence KYOTO GOJO, check in', 'About 15 minutes straight up Karasuma-dōri with the bags, or one subway stop to Gojō (How-to 13).'),
] + _r[_j:]
D[21]['foot'] = 'Skip Hōryū-ji and the western temples. Dinner is Pontochō tonight and Gion on Friday. They can swap.'
_r = D[21]['rows']; _a = _row(21, '05:55'); _b = _row(21, '06:20')
_r[_a] = R('05:55', 'Wake, final pack, check out by 06:20'); del _r[_b]

# ---------- Nara: no Kōfuku-ji stop, no Isuien row, more time for the deer and the three main sights ----------
_r = D[21]['rows']; _i = _row(21, '12:45'); _j = _row(21, '16:15')
D[21]['rows'] = _r[:_i] + [
 R('12:45', 'Into Nara Park for the deer', 'Walk on past Kōfuku-ji: its pagoda is wrapped for restoration until 2034. Deer crackers are about ¥200 at the stalls. An unhurried hour.'),
 R('13:45', 'Tōdai-ji and the Great Buddha', 'Through the Nandaimon gate, where the deer are thickest. The one unmissable thing here.'),
 R('14:45', 'Nigatsu-dō', 'Ten minutes uphill behind the main hall. A balcony with the view over the city. Free.'),
 R('15:20', 'Kasuga Taisha and the lantern path', 'Twenty minutes south along the hill. Quieter, wooded, the better half of Nara.'),
] + _r[_j:]
D[21]['foot'] = 'Skip Hōryū-ji and the western temples. Isuien garden, beside the Tōdai-ji gate, is there if you want a quiet half hour. Dinner is Pontochō tonight and Gion on Friday. They can swap.'

# ---------- Nara order B: Kasuga first, Tōdai-ji after the crowds, Nigatsu-dō in the late light ----------
_r = D[21]['rows']; _i = _row(21, '12:00'); _j = _row(21, '16:40')
D[21]['rows'] = _r[:_i] + [
 R('12:00', 'Quick lunch on Sanjō-dōri', 'Keep it to 40 minutes: no queues, nothing cooked to order. Kakinoha sushi is fast. Then Nakatanidō for the mochi pounding.'),
 R('12:45', 'Into Nara Park for the deer', 'Past Kōfuku-ji, pagoda wrapped until 2034. Head for the lawns towards Kasuga, calmer than the Tōdai-ji gate. Deer crackers about ¥200. No food in your bags.'),
 R('13:35', 'Kasuga Taisha and the lantern path', 'Up through the stone lanterns to the shrine front. No need to pay to go inside.'),
 R('14:25', 'Tōdai-ji and the Great Buddha', 'Twenty minutes north along the hill, in through the Nandaimon gate. The school groups have cleared. Open until 17:30.'),
 R('15:30', 'Nigatsu-dō', 'Ten minutes uphill behind the main hall. A west-facing balcony over the city, best in the late light. Free.'),
 R('16:15', 'Taxi to JR Nara Station', 'Walk down to the Tōdai-ji gate, where taxis wait. Backup: the loop bus, every ten minutes, Suica. Or the GO app.'),
] + _r[_j:]
D[21]['foot'] = 'Stags are pushy in October: feed the does and keep crackers away from the big males. Isuien garden, beside the Tōdai-ji gate, is the quiet option. Dinner is Pontochō tonight and Gion on Friday. They can swap.'

# ---------- Kyoto Station bag drop: Crosta Kyoto, B1 ----------
D[21]['rows'][_row(21, '10:15')] = R('10:15', 'Bags to Crosta Kyoto, level B1', 'Below the JR Central Gate, open until 20:00. Take passports and valuables out first (How-to 13).')
HOWTO[[x[0] for x in HOWTO].index('Kyoto Station, bags and the walk, Wed 21')] = ('Kyoto Station, bags and the walk, Wed 21', [
 'Use Crosta Kyoto, the staffed baggage counter on level B1, directly below the JR Central Gate on the north, Kyoto Tower side. Open 08:00 to 20:00. ¥1,000 per bag per day. Not the Hachijō gate counter by the Shinkansen, which shuts at 18:00.',
 'Before the bags go over the counter, take out: passports, wallets and cards, phones, chargers and power bank, medication, a warm layer, and anything valuable or fragile. Valuables are not accepted in stored bags.',
 'From the Nozomi at 10:00: go out through the Shinkansen gates and follow the signs for the Central Gate and the Karasuma side, along the upper walkway across the tracks. About 7 minutes with the bags.',
 'At the Central Gate, take the escalator down to B1. The counter is behind the escalators, signed for baggage. Hand the bags over, pay, and keep the receipt. You need it to collect.',
 'For Nara: back up the escalator, in through the JR Central Gate with Suica, and follow the signs to platforms 8 to 10 for the JR Nara line.',
 'Coming back about 17:25: out through the Central Gate, down to B1, collect with the receipt. With a 20:00 close, a late train is not a problem.',
 'Option: the same counter delivers to Kyoto hotels for ¥1,500 a bag if dropped by 14:00, arriving after 17:00. Ask sequence KYOTO GOJO first whether it accepts deliveries.',
 'To sequence KYOTO GOJO: out the north side, the Kyoto Tower side, then straight north up Karasuma-dōri to Gojō. About 15 minutes, flat. Or take the Karasuma subway line one stop to Gojō, then walk 3 minutes.',
 'A taxi from the north rank is the easy alternative if you are tired.'])
_i = [t[0] for t in TIPS].index('Luggage and lockers')
TIPS[_i] = (TIPS[_i][0], TIPS[_i][1] + ' Before any bag is handed over, take out passports, wallets, chargers and medication.')

# ---------- Flights: all four Cathay sectors ----------
_r = D[17]['rows'][0]
D[17]['rows'][0] = R(_r[0], _r[1], 'CX524, Terminal 2. Visit Japan Web QR codes ready. About an hour to clear. Suica is in your Apple Wallets.', _r[3])
_i = _row(27, '10:10'); _r = D[27]['rows'][_i]; D[27]['rows'][_i] = R(_r[0], _r[1], 'Terminal 3. Hong Kong is one hour behind Tokyo.', _r[3])
_i = _row(27, '14:25'); _r = D[27]['rows'][_i]; D[27]['rows'][_i] = R(_r[0], _r[1], 'Terminal 1. Allow 45 to 60 minutes for immigration, bags and customs.', _r[3])
_i = _row(30, '21:30'); _r = D[30]['rows'][_i]; D[30]['rows'][_i] = R(_r[0], _r[1], 'Terminal 1. Three hours before departure.', _r[3])
_i = _row(30, '00:30'); _r = D[30]['rows'][_i]; D[30]['rows'][_i] = R(_r[0], _r[1], 'Saturday 31 October, Terminal 1. Lands Melbourne Terminal 2 at 12:30.', _r[3])
for _g in CHECK:
    _g[1][:] = [(l, 'Confirm all four flights in the Cathay app: CX104, CX524, CX543, CX105' if t == 'Confirm CX543 and CX105 times in the Cathay app' else t) for (l, t) in _g[1]]
