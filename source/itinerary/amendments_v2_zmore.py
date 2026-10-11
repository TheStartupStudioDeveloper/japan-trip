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
 'Restaurant and café meals are never tax-free. Department stores refund the tax at a separate counter and keep a small fee, around 1.5%.',
 'Food, drinks and cosmetics are sealed in a bag. Leave it sealed until you have left Japan.',
 'This at-the-till system runs until 31 October, so it covers the whole trip. It changes on 1 November.']

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
