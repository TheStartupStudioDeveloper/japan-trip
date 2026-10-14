# ---------- Money tips ----------
_i = [t[0] for t in TIPS].index('Cash and coins')
TIPS[_i] = ('Cash and coins', 'About ¥5,000 to ¥10,000 each a day is plenty. Small restaurants, market stalls, temple entry and shrine charms are often cash only. Keep a coin purse of ¥10, ¥50, ¥100 and ¥500 for machines and temples. Top up as you go: 7-Eleven, Lawson, FamilyMart and Japan Post ATMs take foreign cards, most with English.')
_i = [t[0] for t in TIPS].index('Cards and cash')
TIPS[_i] = ('Cards and cash', 'Carry two cards, kept separately. Leave one card and some emergency cash in the room safe. Never keep both phones, wallets and cards in one bag. If an ATM or card machine offers to charge you in AUD, choose yen.')

# ---------- G's options while the stores are on ----------
_h = _how('While the stores are on, for G')
_j = [x[:15] for x in _h].index('Nintendo Tokyo:')
_h[_j:_j+1] = [
 'Shibuya Parco, a short walk from the hotel: Nintendo Tokyo, the Pokémon Center, the Capcom Store and the Jump Shop, all on one floor, plus the rooftop.',
 'Harakado, at the Harajuku end of Omotesando: design shops, food, a rooftop, and Kosugi-yu, an old-style public bath in the basement.',
 'Tokyu Plaza Omotesando, directly opposite: the mirrored escalator entrance and a free rooftop terrace with trees.',
 'Ura-Harajuku: the back lanes either side of Cat Street, for streetwear and sneaker shops.']

# ---------- Massage, near each hotel ----------
HOWTO.append(('Massage near each hotel', [
 'Head spas are small, appointment-only salons. Book a day or two ahead, weekends first. Body and foot places mostly take walk-ins.',
 'Shibuya. Head spa: The Head Spa Tokyo Harajuku, about 5 minutes north of the hotel, or Head Spa Josho in Omotesando, open to 22:00. Body and foot: Body Spa Sora, east side of the station, to 23:00, or Joyful Massage Spa Shibuya, open 24 hours.',
 'Kyoto. Head spa: Head Spa Salon QUATRE near Shijō-Karasuma, one subway stop north, or The Head Spa Tokyo Kyoto at Shijō-Kawaramachi. Body and foot: YUMEMISHI Shijō-Karasuma, the closest, to 21:00, or Hannari near Nishiki, to 22:00.',
 'Hibiya and Ginza. Head spa: Head Spa ZEN, to 23:00, or Head Spa zwei HAUS, to 22:00. Body and foot: Buasai Ginza, Thai massage 5 minutes from the hotel, to midnight, or YURAGI, to midnight.',
 'Hong Kong. Head: Kungfu head therapy at 27 Nathan Road, two minutes from the Sheraton. Foot: Foot Lam Moon on Hankow Road, to 00:30. Body and foot: Fu Ying Massage on Granville Road, open 24 hours.',
 'Hours are from Google listings in October 2026. Check on the day.']))
_i = [t[0] for t in TIPS].index('Geisha and maiko')
TIPS.insert(_i + 1, ('Massage', 'A head spa, foot or body massage near each hotel is listed in How-to 21. Book head spas a day or two ahead.'))

# ---------- Kabukichō touts and Golden Gai etiquette, Mon 19 ----------
for _a in (D[19]['alts'][0], D[20]['alts'][2]):
    _rs = _a.get('rows') or []
    for _k, _r in enumerate(_rs):
        if _r[0] == '18:45':
            _rs[_k] = R(_r[0], _r[1], 'Through the underpass to the east side. Neon at full strength. Ignore touts: never follow anyone off the street into a bar.', _r[3])
        if _r[0] == '20:00':
            _rs[_k] = R(_r[0], _r[1], 'The shrine is beside Golden Gai, lit at night. In Golden Gai: cash, a cover charge, and look for English menus. Regulars-only means move on (How-to 11).', _r[3])
_h = _how('Omoide Yokochō, Mon 19')
_h += [
 'Golden Gai, about 20:00: around 200 tiny bars across six alleys. Look for an English menu or sign on the door, which means visitors are welcome.',
 'Some bars are for locals or regulars only. If the sign or the barman says so, move on.',
 'Take cash. Most bars charge a cover of roughly ¥500 to ¥1,500 each before the first drink, usually posted at the door.',
 'Many bars do not allow photos inside, and some lanes ask for none at all.',
 'Kabukichō on the way: ignore touts, and never follow anyone off the street into a bar.']

# ---------- counterfeit goods (9 Oct) ----------
_i = [t[0] for t in TIPS].index('Tax-free')
TIPS.insert(_i + 1, ('No fakes into Japan', 'Since October 2022, bringing counterfeit or replica branded goods into Japan is illegal even for personal use, in your luggage or by post. That covers bags, watches, shoes and clothing. Customs can seize and destroy them on arrival, with no compensation. Leave any knockoffs at home. The vintage luxury stores sell authenticated pieces, so keep the receipts.'))

# ---------- Tax-free, the ¥5 coin, eating and walking (9 Oct) ----------
_i = [t[0] for t in TIPS].index('Tax-free')
TIPS[_i] = ('Tax-free', "Japan's tax is already in the price. Spend ¥5,000 or more before tax in one store, show your physical passports, and the tax isn't charged: you save the 10% tax on most goods (8% on take-away food and soft drinks), about 9% and 7% off the shelf price. Food bought tax-free goes in a sealed bag: keep it sealed until you leave Japan. See How-to 4.")
_i = [t[0] for t in TIPS].index('The ¥5 coin')
TIPS[_i] = ('The ¥5 coin', 'Called go-en, which also means "good connection", so it is the lucky offering at a shrine. Keep a few aside.')
_i = [t[0] for t in TIPS].index('Eating and walking')
TIPS[_i] = ('Eating and walking', 'Eat at the stall or standing to one side, not on the move. Same on local trains, other than the Shinkansen. A lidded takeaway coffee on the go is fine in the city, but markets and temple lanes often ask you not to, so stand aside there. Bins are rare, so plan to carry the cup.')
_h = _how('Tax-free shopping')
_h[:] = [
 'Take the physical passports. The shop scans the entry sticker. A photo is not accepted.',
 'Spend ¥5,000 or more before tax in one store on the same day. Food and other goods can be added together to reach it. Look for the Tax-Free sign, or the tax-free counter in a department store.',
 "Prices already include Japan's tax. Tax-free means it isn't charged: 10% on most goods and alcohol, 8% on take-away food and soft drinks. That is about 9% and 7% off the shelf price.",
 'Restaurant meals are never tax-free. Department stores refund at a separate counter, less about 1.5%.',
 'Food, drinks and cosmetics are sealed in a bag. Keep it sealed until you leave Japan.',
 'This at-the-till system runs to 31 October, so it covers the trip. It changes on 1 November.']

# ---------- Omoide Yokochō: otoshi and prices (11 Oct) ----------
_h = _how('Omoide Yokochō, Mon 19')
_j = [x[:22] for x in _h].index('Many counters add a sm')
_h[_j:_j+1] = [
 'Many counters add a small seating charge, a few hundred yen each, and bring a small snack you did not order. It is called otoshi (お通し): that is the charge, so it is normal, not a mistake.',
 'Check the menu and prices before you sit. If none are posted, ask, or pick a counter that shows them. Counters are tiny and best for two.']

# ---------- Tue 20: free afternoon, Manyo Club footbath as an idea (11 Oct) ----------
_rs = D[20]['alts'][0]['rows']
_k = [r[1] for r in _rs].index('Lunch on the waterfront')
_rs[_k:_k+1] = [
 R('13:00', 'Lunch, then a free afternoon on the waterfront', 'Ideas in Extras, Yokohama.'),
 R('16:30', 'Harbour walk to Chinatown, dinner', 'At dusk. Idea: the footbath at The Wharf House on the way (How-to 22). Dinner from 17:30.'),
]
_k = [r[1] for r in _rs].index('Chinatown dinner')
del _rs[_k]
HOWTO.append(('Footbaths in Yokohama, Tue 20 ideas', [
 'Ideas, not bookings. The easy one is on the dusk walk: The Wharf House in Yamashita Park, a footbath terrace on the water. Feet only, clothes on.',
 'The Wharf House: ¥300 each for 30 minutes, towel ¥200. Take a number inside and wait to be called, often about 20 minutes. Closed in rain. Harbour, Bay Bridge and Hikawa Maru view; the Ferris wheel is only faint from here.',
 'For the Ferris wheel view: Manyo Club, a hot spring spa five minutes from the Air Cabin, has a rooftop footbath facing the wheel. No footbath-only ticket: entry covers the whole spa, ¥3,500 each plus ¥100 tax, and you change into their robe in the locker rooms.',
 'Manyo Club risk: the house rule refuses entry with tattoos, apart from small ones covered by their stickers, up to 11 cm square. A larger tattoo would be hidden by the robe on the roof, but the shared locker room is where it could be seen. If staff notice, expect to be asked to leave, with no refund.',
 'Ask Manyo Club first: call 0570-07-4126, or ask the hotel front desk to ring. Show them: 背中にタトゥーがあります。館内着で完全に隠れます。屋上の足湯だけ利用したいのですが、入館できますか？ (I have a tattoo on my back, fully covered by the loungewear. I only want the rooftop footbath. May I enter?)']))
D[20]['alts'][0]['foot'] = 'Alternatives: the market also fits Mon 19 before the stores open, or Mon 26 with teamLab moved to 13:30. Closed Sundays and Wednesdays.'

# ---------- Sun 18: Sushi Hatsume as an option (11 Oct) ----------
_rs = D[18]['rows']
_k = [r[1] for r in _rs].index('Back to Shibuya, nice dinner')
_rs[_k] = R('Evening', 'Back to Shibuya, nice dinner', 'Option: Sushi Hatsume in Ebisu, one stop away. 22-course omakase, ¥10,890 each, 19:30 seating. Book ahead if you want it.')
_g = [g[0] for g in CHECK].index('Book or confirm before you fly')
CHECK[_g][1].insert(4, ('s', 'Optional: Sushi Hatsume for Sun 18, 19:30, on TableCheck'))

# ---------- Tips: wrinkle spray (Note 2, 11 Oct) ----------
_i = [t[0] for t in TIPS].index('Luggage and lockers')
TIPS.insert(_i + 1, ('Creased clothes', 'Convenience stores and Don Quijote sell wrinkle release spray (シワ取りスプレー). Spray, smooth with your hands and hang for a few minutes. Easier than finding an iron.'))

# ---------- Sun 25: Daikoku car meet as an option (11 Oct) ----------
_rs = D[25]['rows']
_k = [r[1] for r in _rs].index('Optional: Tokyo Tower lit up')
_rs[_k] = R(_rs[_k][0], 'Optional: Tokyo Tower lit up, or a car meet', 'Tower: 10 minutes by taxi, Zōjō-ji gate. Or a JDM car tour to Daikoku from the hotel, 20:00 to 23:00 (How-to 23).')
HOWTO.append(('Daikoku car meet, Sun 25 option', [
 'An option, not a booking. Daikoku PA, on Yokohama\'s Bayshore Route, is where Japanese car fans meet at night. Only reachable by car, so book a tour (Klook or the operator).',
 'You ride in a JDM car such as an R34 Skyline, RX-7 or Supra with an English-speaking guide. Pickup from the Blossom, about 3 hours, tolls included. Start about 20:00; teamLab is 08:30 Monday.',
 'Police can close Daikoku without notice, mostly on Friday and Saturday nights. Pick a tour that moves you to another bay spot if it is shut, and check its refund terms.']))
_g = [g[0] for g in CHECK].index('Book or confirm before you fly')
CHECK[_g][1].insert(10, ('g', 'Optional: Daikoku car meet tour for Sun 25, about 20:00, hotel pickup'))
_f = D[25]['foot']
_i = _f.find(' Sushi Bus idea for lunch')
if _i >= 0:
    D[25]['foot'] = _f[:_i]

# Tax-free QR and coming home allowances (How-to 4), plus two checklist lines
_h = _how('Tax-free shopping')
_h[-1:-1] = [
 'Tax-free QR: in Visit Japan Web personal details, turn on "Use tax-free QR code" and scan both passports with the camera. After landing, scan the landing sticker QR too. Show the code live in the app; carry passports anyway.',
 'Back in Australia: AUD 900 of goods, 2.25 L of alcohol and 25 cigarettes each. Declare all food and wood. Undeclared items risk a fine of about AUD 626.',
]
for _gi, (_gn, _items) in enumerate(CHECK):
    _k = next((i for i, it in enumerate(_items) if 'Visit Japan Web registered' in it[1]), None)
    if _k is not None:
        _items[_k] = (_items[_k][0], 'Visit Japan Web registered for both, tax-free QR on, passports scanned')
        break
else:
    raise SystemExit('VJW checklist line not found')
_g = [g[0] for g in CHECK].index('On the ground')
_k = next(i for i, it in enumerate(CHECK[_g][1]) if it[1].startswith('Sat 17: Narita Express'))
CHECK[_g][1][_k] = ('s', 'Sat 17 at Narita: scan the landing sticker QR into Visit Japan Web, then Narita Express tickets on a train that stops at Shibuya')
# Fit: merge the two Street Kart checklist lines
_g = [g[0] for g in CHECK].index('Book or confirm before you fly')
_L = CHECK[_g][1]
_a = next(i for i, it in enumerate(_L) if it[1].startswith('Street Kart meeting point'))
_b = next(i for i, it in enumerate(_L) if it[1].startswith('Street Kart: check the rebooking'))
_L[_a] = (_L[_a][0], 'Street Kart: meeting point, arrival time, and rebooking terms in case it moves to Sun 25 or Mon 26')
del _L[_b]

# Nara by Kintetsu, kamameshi lunch at Shizuka, JR as the alternative (How-to 24)
_r = D[21]['rows']; _i = _row(21, '10:45'); _j = _row(21, '12:45')
D[21]['rows'] = _r[:_i] + [
 R('10:40', 'Kintetsu limited express to Nara', 'South side of the station, 5 minutes from Crosta. Seats at the machine, about ¥1,280 each (How-to 24).'),
 R('11:15', 'Kintetsu Nara, up into Higashimuki arcade', 'Covered to Sanjō-dōri. Nakatanidō mochi pounding at the end.'),
 R('11:30', 'Lunch: Kamameshi Shizuka', 'Iron-pot rice cooked to order, about 20 minutes. Ten minutes east, beside Isuien. No bookings. Long queue: a kakinoha box instead.'),
] + _r[_j:]
_i = _row(21, '12:45')
D[21]['rows'][_i] = R('12:45', 'Into Nara Park for the deer', 'Straight onto the lawns towards Kasuga, calmer than the Tōdai-ji gate. Kōfuku-ji\'s pagoda is wrapped until 2034. Deer crackers about ¥200.')
D[21]['rows'][_row(21, '16:15')] = R('16:15', 'Walk down to Kintetsu Nara', 'About 20 minutes downhill past the Tōdai-ji gate. Raining or tired: a taxi from the gate, or the loop bus with Suica.')
D[21]['rows'][_row(21, '16:40')] = R('16:45', 'Kintetsu limited express back', 'Kyoto by about 17:20. Collect the bags.')
D[21]['foot'] = 'Stags are pushy: feed the does. Alternative: JR Nara line on Suica, 20 minutes from the park (How-to 24). Pontochō and Gion dinners can swap.'

HOWTO.append(('Kyoto to Nara and back, Wed 21', [
 'Kintetsu: gates on the south (Hachijō) side of Kyoto Station. At the machine buy to Kintetsu Nara plus a limited express (特急) seat, about ¥1,280. Twice an hour, 35 minutes. Check the board says 奈良: some go to Kashihara-jingū.',
 'No seats: the direct express (急行), 45 minutes, ¥760 on Suica, hourly. In Nara, exit for Higashimuki (東向商店街).',
 'JR alternative: Miyakoji rapid (みやこ路快速) from the JR gates, 45 minutes, ¥720 on Suica. JR Nara is 20 minutes on foot from the park. Back by taxi or loop bus from the Tōdai-ji gate.',
]))

_g = [g[0] for g in CHECK].index('On the ground')
_L = CHECK[_g][1]
_k = next(i for i, it in enumerate(_L) if it[1].startswith('Wed 21: check the JR special rapid'))
_L[_k] = ('k', 'Wed 21: Kintetsu seat times to Nara and back, and JR times to Osaka for Thursday')
# How-to 13: Nara now by Kintetsu; tightened to fit
_h = _how('Kyoto Station, bags and the walk, Wed 21')
_h[:] = [x for x in _h if not x.startswith('A taxi from the north rank')]
_h[[i for i, x in enumerate(_h) if x.startswith('For Nara:')][0]] = 'For Nara: back up the escalator and through the station\'s central passage to the Kintetsu gates on the south side, about 10 minutes (How-to 24).'
_h[[i for i, x in enumerate(_h) if x.startswith('Option: the same counter')][0]] = 'Option: Crosta delivers to Kyoto hotels for ¥1,500 a bag if dropped by 14:00. Ask the hotel first.'
_h[-1] = _h[-1] + ' Or a taxi from the north rank.'
_r = D[21]['rows']
_r[_row(21, '10:40')] = R('10:40', 'Kintetsu limited express to Nara', 'South side of the station, about 10 minutes from Crosta. Seats at the machine, about ¥1,280 each (How-to 24).')
_r[_row(21, '20:30')] = R('20:30', 'Optional: Kamo River and the Shirakawa canal', 'Shijō Bridge is at the end of the alley, Shirakawa seven minutes beyond. Taxi home.')
_r[_row(21, '17:25')] = R('17:25', 'Kyoto Station building', 'The staircase lights up at dusk. The free Sky Garden faces Kyoto Tower.')
_r[_row(21, '19:00')] = R('19:00', 'Pontochō dinner, casual, no booking', 'About 20 minutes on foot, or one subway stop to Shijō. Walk in along Kiyamachi-dōri.')
# Fit: tighten How-to 22 and 24
_h = _how('Footbaths in Yokohama, Tue 20 ideas')
_h[1] = 'The Wharf House: ¥300 each for 30 minutes, towel ¥200. Take a number inside, often a 20 minute wait. Closed in rain. Harbour and Bay Bridge view; the Ferris wheel is faint.'
_h[2] = 'For the Ferris wheel view: Manyo Club, five minutes from the Air Cabin, has a rooftop footbath facing the wheel. Entry covers the whole spa, ¥3,600 each, in their robe.'
_h[3] = 'Manyo Club risk: tattoos are refused, apart from small ones under their stickers, up to 11 cm square. The robe covers it on the roof, but not in the shared locker room. If noticed, expect to be asked to leave, no refund.'
_h = _how('Kyoto to Nara and back, Wed 21')
_h[0] = 'Kintetsu: south (Hachijō) side of Kyoto Station. At the machine, buy to Kintetsu Nara plus a limited express (特急) seat, about ¥1,280. Twice an hour, 35 minutes. Some go to Kashihara-jingū: check the board says 奈良.'
_h = _how('Massage near each hotel')
_h[0] = 'Head spas are small, appointment-only salons: book a day or two ahead. Body and foot places mostly take walk-ins. Hours from Google, October 2026; check on the day.'
_h[:] = [x for x in _h if not x.startswith('Hours are from Google')]
_h = _how('While the stores are on, for G')
_k = [i for i, x in enumerate(_h) if x.startswith('Harakado')][0]
_h[_k] = 'Harakado, at the Harajuku end of Omotesando: design shops, a rooftop, and Kosugi-yu, an old-style bath in the basement. Tokyu Plaza opposite has the mirrored escalator and a free rooftop terrace.'
_h[:] = [x for x in _h if not x.startswith('Tokyu Plaza Omotesando')]
_h = _how('Kyoto to Nara and back, Wed 21')
_h[:] = [
 'Kintetsu: south side of Kyoto Station. At the machine, buy Kintetsu Nara plus a limited express (特急) seat, about ¥1,280, 35 minutes. Board one signed 奈良.',
 'No seats: the direct express (急行), 45 minutes, ¥760 on Suica, hourly. In Nara, exit for Higashimuki.',
 'JR alternative: Miyakoji rapid from the JR gates, 45 minutes, ¥720 on Suica, then 20 minutes on foot to the park.',
]
_h = _how('Ngong Ping 360 voucher')
if _h[-1].startswith('If it closes for wind'):
    _h.pop(); _h[0] = _h[0].rstrip('.') + '. If wind closes it, the voucher moves to another day.'
_h = _how('Peak Tram')
_h[:] = [
 'Book a standard one-way ticket up, for about 15:45 on the clearest evening. Klook Fast Track runs Friday to Sunday only.',
 'The lower terminus is on Garden Road in Central, 15 minutes uphill from the ferry or a short taxi. Sit on the right going up.',
 'At the top, walk Lugard Road, about 20 minutes each way, for the best free view. Stay through sunset at 17:50.',
 'Taxi down from the rank by the Peak Galleria. Tram seats face backwards on the way down.',
]
_h = _how('Footbaths in Yokohama, Tue 20 ideas')
_h[0] = 'Ideas, not bookings. The easy one, on the dusk walk: The Wharf House footbath terrace in Yamashita Park. Feet only.'
# How-to 10: Mori Art Museum is closed between shows in October
_h = _how('While the stores are on, for G')
_k = [i for i, x in enumerate(_h) if x.startswith('Roppongi design loop')][0]
_h[_k] = 'Roppongi design loop: Chiyoda line from Omotesando, one stop to Nogizaka. 21_21 Design Sight (10:00 to 19:00, closed Tuesdays and between shows) and the National Art Center. The Mori Art Museum is shut in October; Tokyo City View below it is open.'
# Note 5: face cover in fitting rooms
_i = [t[0] for t in TIPS].index('Passports')
TIPS.insert(_i + 1, ('Fitting rooms', 'Put on the thin face cover (フェイスカバー) the shop gives you before pulling on a top, so makeup does not mark the clothes. Shoes off at the fitting room step.'))
# Cash mix tips, Japan and Hong Kong
_i = [t[0] for t in TIPS].index('Cash and coins')
TIPS.insert(_i + 1, ('The right mix of yen', 'Notes are ¥1,000, ¥5,000 and ¥10,000. Keep three or four ¥1,000s each for stalls, temples and taxis; break ¥10,000s at convenience stores, not small shops. ATMs give mostly ¥10,000s, so ask for an amount like ¥19,000 to get smaller notes. Most useful coins: ¥100 and ¥500 for machines, a few ¥10 and ¥5 for shrines.'))
_i = [t[0] for t in TIPS].index('Hong Kong: tipping')
TIPS.insert(_i, ('Hong Kong: cash', 'Octopus covers trains, buses and most shops. For cash, carry HK$20, HK$50 and HK$100 notes. Taxis and small stalls often cannot change HK$500 or HK$1,000. Some red taxis are still cash only.'))

# Ninja Tokyo: optional Sat 17 dinner, to book. Nothing removed.
_r = D[17]['rows']; _i = _row(17, '18:30')
_r.insert(_i + 1, R('19:00', 'Optional: Ninja Tokyo dinner', 'Instead of dinner close by. An underground ninja village in Ōtemachi, tricks at the table. Courses from ¥13,200. Hanzōmon line direct, 20 minutes.', TB))
_g = [g[0] for g in CHECK].index('Book or confirm before you fly')
_L = CHECK[_g][1]
_k = next(i for i, it in enumerate(_L) if 'Sushi Hatsume' in it[1])
_L[_k] = ('s', 'Optional, on TableCheck: Ninja Tokyo Sat 17 19:00, Sushi Hatsume Sun 18 19:30')
# Fit: tighten Sat 17 notes
_r = D[17]['rows']
_r[_row(17, '13:45')] = R('13:45', 'Wander back into Shibuya', 'Hachikō, the Scramble Crossing, Center-gai.')
_r[_row(17, '10:30')] = R('10:30', 'Miyashita Park and Cat Street', 'The rooftop park above the hotel, where the festival is on, then Cat Street. If shattered, stop here.')
_r[_row(17, '18:30')] = R('18:30', 'Dinner close by', 'Nonbei Yokochō or Dōgenzaka, then an early night.')
_r = D[17]['rows']
_r[_row(17, '19:00')] = R('19:00', 'Optional: Ninja Tokyo dinner', 'Instead of dinner close by: a ninja village underground in Ōtemachi. From ¥13,200. Hanzōmon line, 20 minutes.', TB)
_r[_row(17, '10:00')] = R('10:00', 'Shibuya Station, bags to the hotel', 'Hachikō exit, lobby on 4F (How-to 6). Leave the bags; confirm the early check-in.')
_r[_row(17, '12:30')] = R('12:30', 'Omotesando', 'Lunch wherever looks good. Omotesando Hills, Tod\'s and Dior to look up at. Prada Aoyama optional.')
_r[_row(17, '14:45')] = R('14:45', 'Supplies, then check in if the room is ready', 'Don Quijote and 7-Eleven for supplies. No room yet: bags stay at the desk until after Shibuya Sky.')

# Sequence Miyashita Park replied (14 Oct): high floor requested, not guaranteed; early check-in asked on the day, free; bags held
D[17]['rows'][_row(17, '10:00')] = R('10:00', 'Shibuya Station, bags to the hotel', 'Hachikō exit, lobby on 4F (How-to 6). Ask about early check-in: free if a room is ready, bags held until then.')
_bk = CHECK[[g[0] for g in CHECK].index('Book or confirm before you fly')][1]
_k = next(i for i, it in enumerate(_bk) if it[1].startswith('Ask Sequence Miyashita Park for early check-in'))
del _bk[_k]
_og = CHECK[[g[0] for g in CHECK].index('On the ground')][1]
_k = next(i for i, it in enumerate(_og) if it[1].startswith('Sat 17 at Narita'))
_og.insert(_k + 1, ('s', 'Sat 17: ask Sequence for early check-in at the desk. Free; they hold the bags'))

# Landing permission QR: the process (How-to 4, Sat 17 landing row)
_h = _how('Tax-free shopping')
_k = next(i for i, x in enumerate(_h) if x.startswith('Tax-free QR'))
_h[_k:_k + 1] = [
 'Tax-free QR, at home: in Visit Japan Web, personal details, turn on "Use tax-free QR code" and scan both passports with the phone camera.',
 'Tax-free QR, at Narita: immigration sticks a landing permission sticker with a QR in each passport. Check you both get one. Then in Visit Japan Web open the tax-free section, scan each sticker, and the QR is ready. Show it live at the till; carry passports anyway.',
]
D[17]['rows'][_row(17, '06:50')] = R('06:50', 'Land at Narita', 'CX524, Terminal 2. Visit Japan Web ready. Check you each get the landing sticker, then scan it into Visit Japan Web (How-to 4).', B)

# How-to 2: exact switch-on steps on landing in Hong Kong, Fri 16
_h = _how('eSIM and wifi')
_a = next(i for i, x in enumerate(_h) if x.startswith('Install both eSIMs'))
_b = next(i for i, x in enumerate(_h) if x.startswith('Data Roaming on for Ubigi'))
_h[_a:_b + 1] = [
 'Install both eSIMs at home on wifi, then leave the Ubigi line switched off. Best Asia stays waiting to start, so nothing is used.',
 'On landing in Hong Kong, Fri 16 at 21:45: Settings, Mobile, Ubigi line, turn it on. Ubigi Data Roaming on. Mobile Data set to Ubigi.',
 'Australian SIM: Data Roaming off, but keep the line on for SMS and two-factor codes. The Ubigi app should then show the plan as active.',
 'The 15 days run to the evening of Sat 31, which covers the flight home.',
]
_h = _how('eSIM and wifi')
_a = next(i for i, x in enumerate(_h) if x.startswith('It covers Japan'))
_b = next(i for i, x in enumerate(_h) if x.startswith('30GB'))
_c = next(i for i, x in enumerate(_h) if x.startswith('If you need more'))
_h[_a] = 'Covers Japan (KDDI, Docomo) and Hong Kong (Smartone) with no change. 30GB at full speed, then 2 Mbps; track it in the Ubigi app, top up there if needed.'
del _h[max(_b, _c)]; del _h[min(_b, _c)]
_k = next(i for i, x in enumerate(_h) if x.startswith('The 15 days run'))
_h[0] = _h[0] + ' The 15 days run to the evening of Sat 31, covering the flight home.'
del _h[_k]

# Osaka Castle: the moat-wall view via Gokuraku-bashi on the way in (Thu 22)
D[22]['rows'][_row(22, '08:30')] = R('08:30', 'Osaka Castle, up close', 'In by Aoya-mon to Gokuraku-bashi: the tower over the inner moat walls. Then to its foot, not inside. Takeaway breakfast on a bench.')
