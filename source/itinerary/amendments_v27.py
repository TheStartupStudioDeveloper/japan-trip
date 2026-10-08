# V2.7. Checklist regrouped by when each thing can actually be done.
CHECK[:] = [
 ('Set up at home', [
  ('', 'Offline Google Maps areas for Tokyo, Kyoto, Osaka and Hong Kong'),
  ('', 'Google Translate with Japanese and Chinese downloaded for offline use'),
  ('', 'Airline, booking, Klook and Ubigi apps installed and logged in'),
  ('', 'Banking apps working with Face ID, and international transactions enabled'),
  ('', 'Travel insurance policy, passports and booking confirmations saved offline'),
  ('', 'Licence and International Driving Permit photographed, as a backup only'),
  ('', 'Hotel names and addresses screenshotted in Japanese and Chinese (How-to 1)'),
  ('', 'Ubigi eSIM installed, one each. Smartstart starts it in Hong Kong on Fri 16 (How-to 2)'),
  ('', 'Suica and Octopus in both Apple Wallets, Suica topped up'),
  ('', 'Visit Japan Web registered for both'),
 ]),
 ('Book or confirm before you fly', [
  ('s', 'International Driving Permit, 1949 Geneva Convention version, for Street Kart'),
  ('s', 'Street Kart meeting point and arrival time, from the booking'),
  ('s', 'Street Kart: check the rebooking terms, in case it moves to Sun 25 or Mon 26'),
  ('s', 'Shibuya Sky Monday and Tuesday slots: check the cancellation or change terms'),
  ('k', 'Gion or Pontochō dinner for Fri 23, 18:30'),
  ('g', 'Confirm where and when the Seascape wristbands are collected on Sat 24'),
  ('h', 'Confirm CX543 and CX105 times in the Cathay app'),
  ('h', 'Cynthia: check whether the Agoda booking includes an airport pickup on Tue 27'),
  ('h', 'Ngong Ping 360 Crystal cabin vouchers on Klook, good on any day to 31 October'),
  ('h', 'Pick a yum cha place for Fri 30 lunch, 12:30'),
  ('h', 'Hong Kong dollars for the airport taxi on arrival'),
 ]),
 ('Pack', [
  ('', 'Street Kart: closed shoes, physical licence and physical permit'),
  ('', 'Passports, carried on shopping days for tax-free'),
  ('', 'A power bank and a USB-C cable each, charged'),
  ('', 'Spare clean socks for temple and shrine days'),
  ('', 'A light rain jacket each, hand sanitiser, and masks if you want them'),
 ]),
 ('Decide with the Tokyo forecast, from Sat 17', [
  ('s', 'Pick the Shibuya Sky day, then cancel or change the other two slots'),
  ('s', 'Give the better weather day of Mon 19 and Tue 20 to Asakusa and Yokohama'),
  ('s', 'A wet morning: move teamLab Borderless forward (How-to 8)'),
  ('g', 'Decide on the Tsukiji and Asakusa swap'),
 ]),
 ('Decide with the Hong Kong forecast, from about Sat 24', [
  ('h', 'Aqua Luna: confirm the 19:30 sailing on Tue 27 is running, then book. +852 2116 8821'),
  ('h', 'Peak Tram one-way up, about 15:45 on the clearest evening (Wed 28 by default)'),
  ('h', 'Dinner in Central or SoHo for the same evening as the Peak, 19:30'),
  ('h', 'Pick the Ngong Ping day for the voucher, first car at 10:00 (Thu 29 by default)'),
  ('h', 'Ozone at the Ritz-Carlton: choose Thursday or Friday by the cloud, then book'),
 ]),
 ('On the ground', [
  ('s', 'Sat 17: Narita Express tickets at Narita, on a train that stops at Shibuya'),
  ('s', 'Sat 17: ask Sequence Miyashita Park about early check-in'),
  ('s', 'Tue 20: book the 06:30 taxi to Shinagawa for Wednesday morning'),
  ('k', 'Wed 21: confirm the 07:15 Keihan train to Osaka for Thursday'),
  ('g', 'Sat 24: ask the Blossom about guest laundry (How-to 17)'),
  ('g', 'Mon 26: settle the bill, and check the 06:38 Asakusa line train to Haneda'),
  ('h', 'Tue 27: ask the Sheraton whether pool sessions need booking, and the club lounge hours'),
  ('h', 'Fri 30: ask whether checkout can go later than 18:00, and confirm bags are held until 20:30'),
 ]),
]

# Pack group removed. Its items live in Tips.
_i = [g[0] for g in CHECK].index('Pack'); del CHECK[_i]
CHECK[:] = [(g[0].split(', from')[0], g[1]) for g in CHECK]
_k = [t[0] for t in TIPS]
TIPS.insert(_k.index('Umbrellas and wet gear') + 1, ('Power', 'A power bank and a USB-C cable each. Charge phones, power banks and AirPods every night.'))
_k = [t[0] for t in TIPS]
TIPS.insert(_k.index('Shrines and temples'), ('Street Kart', 'Wear fully closed shoes. Take the physical licence card, the physical International Driving Permit and passports. Photos are not accepted.'))
