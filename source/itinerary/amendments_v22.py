# V2.2 amendments. Applied on top of V2.1. Content only.

# ---------- Sat 17: general times ----------
r = D[17]['rows']
for i, t in enumerate(['06:50', '08:15', '10:30', '12:30', '13:45', '14:45', '16:00', '18:30']):
    r[i] = (t,) + tuple(r[i][1:])
r[1] = R('08:15', 'Narita Express to Shibuya', 'Buy the ticket at Narita, on a train that stops at Shibuya (How-to 1). About 80 minutes.')
r.insert(2, R('10:00', 'Shibuya Station, bags to the hotel', 'Walk from the Hachikō exit, lobby on 4F (How-to 2). Leave the bags and ask about early check-in.'))
D[17]['sum'] = 'No trains after the airport, just a slow loop on foot from the hotel while you wait for the room. Two fixed points: the landing and Shibuya Sky. The other times are a guide and slide if the airport is slow.'

# ---------- Mon 19 ----------
SHINJUKU[1] = R('11:00', 'Omotesando and Aoyama vintage luxury', 'Until 14:00. The secondhand luxury boutiques either side of the avenue. All open at 11:00 except Casanova at 12:00 (How-to 16). Passports for tax-free. G has his own options (How-to 17).')
D[19]['alts'][0]['foot'] += ' Running early: go into Shinjuku sooner and wander the station and the east side streets. Shinjuku Gyoen is the park to see, on a Tuesday only.'

# ---------- appendix ----------
HOWTO.append(('Omotesando and Aoyama store hours', [
 'Amore Vintage (Omotesando and Aoyama), Vintage Qoo, Brand Collect and ALLU all open at 11:00.',
 'Casanova Vintage opens at 12:00, so leave it until last.',
 'Amore, Qoo and Casanova trade until 20:00. Take the physical passports for tax-free.']))
HOWTO.append(('While the stores are on, for G', [
 'The window is 11:00 to 14:00 on the Shinjuku day, then lunch together in Omotesando.',
 'Roppongi design loop: Chiyoda line from Omotesando, one stop to Nogizaka. 21_21 Design Sight (10:00 to 19:00) and the National Art Center, then the Mori Art Museum if there is time. 21_21 closes on Tuesdays and between exhibitions, so check first.',
 'Nezu Museum: in Aoyama, with a garden. 10:00 to 17:00, closed on Mondays, so it only works if this day moves to Tuesday. Book a timed ticket online.',
 'Nintendo Tokyo: Shibuya Parco, a short walk from the hotel.',
 'Gym session: Gold\'s Gym Harajuku sells one-day passes, but it shuts on the third Monday of the month, which is the 19th. Fine on a Tuesday.',
 'Sauna: Shibuya Saunas, five minutes from Shibuya Station. 08:00 to midnight, about ¥3,200 on a weekday for 2.5 hours, tattoo friendly.',
 'Sento: Kairyo-yu, nearest Ebisu Station. Opens at 12:00, ¥600 plus ¥550 for the sauna.']))
