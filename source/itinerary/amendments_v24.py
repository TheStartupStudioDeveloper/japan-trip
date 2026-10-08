# V2.4 amendments. Applied on top of V2.3.
import re as _re

# ---------- 1. Appendix in chronological order ----------
_MAP = {1: 5, 2: 6, 3: 12, 4: 13, 5: 16, 6: 18, 7: 14, 8: 2, 9: 3, 10: 4, 11: 8, 12: 20, 13: 19, 14: 15, 15: 11, 16: 9, 17: 10, 18: 7}
def _fix(x):
    if isinstance(x, str): return _re.sub(r'How-to (\d+)', lambda m: 'How-to %d' % _MAP[int(m.group(1))], x)
    if isinstance(x, tuple): return tuple(_fix(v) for v in x)
    if isinstance(x, list):
        x[:] = [_fix(v) for v in x]; return x
    if isinstance(x, dict):
        for k in list(x): x[k] = _fix(x[k])
        return x
    return x
for _o in (DAYS, GOOD, CHECK, TIPS, SWAPS, LEGS, HOWTO): _fix(_o)
_old = list(HOWTO)
_new = [None] * 20
for _i, _h in enumerate(_old, 1): _new[_MAP[_i] - 1] = _h

# ---------- 3. Ubigi eSIM rewritten ----------
_new[1] = ('eSIM and wifi', [
 'Ubigi Best Asia Unlimited, 15 days, AU$78 each. One for each phone.',
 'Install both eSIMs at home on wifi. No manual activation: Smartstart starts the plan at the first connection in a covered place.',
 'That is Hong Kong on Fri 16 October at 21:45. Set Ubigi as the mobile data line when you land. The 15 days then run to the evening of Sat 31, which covers the flight home.',
 'Data Roaming on for Ubigi, and off for the Australian SIM. Keep the Australian number active for SMS and two-factor codes.',
 'It covers Japan on KDDI and Docomo, and Hong Kong on Smartone. No change needed between countries.',
 '30GB at full speed, then 2 Mbps. Track usage in the Ubigi app.',
 'If you need more at the end, top up in the app or buy a Hong Kong only SIM or plan.',
 'Phone settings: Auto-Join on for hotel wifi, Wi-Fi Assist off, photo backup on wifi only.'])

# ---------- 4. Phones and power ----------
_new[0] = ('Phones and power', [
 'Download offline Google Maps areas for Tokyo, Kyoto, Osaka and Hong Kong.',
 'Save flight, hotel and the main booking confirmations offline.',
 'Screenshot each hotel name and address in the local script, from the booking confirmation, to show a driver if a phone dies or data misbehaves.',
 'Two to start with: THE BLOSSOM HIBIYA, 東京都港区新橋1-1-13. Sheraton Hong Kong, 香港喜來登酒店, 九龍尖沙咀彌敦道20號.',
 'A power bank and a USB-C cable each. Every night, charge phones, power banks and AirPods.',
 'Keep one phone able to receive Australian SMS for banking and two-factor codes.'])

# ---------- 8. Laundry ----------
_new[16] = ('Laundry, Sun 25', [
 'By Sunday 25 you are a week in. Three good slots: Friday 23 evening in Kyoto, Sunday 25 morning at the Blossom, which is the easiest, or Monday 26 afternoon while you pack.',
 'Ask at the front desk for the guest laundry, meaning coin washers and dryers. Not yet confirmed for either hotel, so ask at check-in.',
 'A wash and dry takes about 90 minutes and a few hundred yen. Have ¥100 coins ready.',
 'No machines, or all busy: ask the desk for the nearest coin laundry.',
 'Hotel laundry service is charged per item and usually has to be handed in by mid morning for same-day return. Worth it for a few pieces only.',
 'Last chance: the Sheraton in Hong Kong, by laundry service.'])
assert all(_new)
HOWTO[:] = _new
D[25]['rows'][0] = R('08:30', 'Slow breakfast near the hotel', 'The easy slot for a load of washing. Details in the appendix (How-to 17).')
_g = CHECK[2][1]; _i = [x[1] for x in _g].index('Ask the Blossom about guest laundry, a week into the trip')
_g[_i] = ('g', 'Ask the Blossom about guest laundry, a week into the trip (How-to 17)')

# ---------- 2, 6, 10. Tips: order, cuts, new tips ----------
_t = dict(TIPS)
del _t['Smoking'], _t['Typhoon season'], _t['Flu season']
_t['Crowded trains'] = 'Carry hand sanitiser. A mask is useful if you prefer one in crowded indoor spaces.'
_t['Cards and cash'] = 'Carry two cards, kept separately. Leave one card and some emergency cash in the room safe. Never keep both phones, wallets and cards in one bag.'
_t['Cash and coins'] = 'Small restaurants, shrines and market stalls are often cash only. Keep a coin purse with ¥10, ¥50, ¥100 and ¥500 coins for machines and temples. 7-Eleven ATMs take foreign cards around the clock.'
_order = ['Data', 'Umbrellas and wet gear', 'Maps on luggage days', 'Luggage and lockers', 'Trains', 'Crowded trains', 'Escalators', 'Crossing', 'Taxi doors',
          'Cash and coins', 'Cards and cash', 'Money tray', 'No tipping in Japan', 'Ticket machine restaurants', 'Eating and walking', 'Chopsticks', 'Litter', 'Cold lockers',
          'Passports', 'Tax-free', 'Shrines and temples', 'The ¥5 coin', 'Bowing', 'Shoes and socks', 'Nara deer', 'Geisha and maiko',
          'Hong Kong: tipping', 'Hong Kong: MTR', 'Hong Kong: trams']
assert set(_order) == set(_t), set(_order) ^ set(_t)
TIPS[:] = [(k, _t[k]) for k in _order]

# ---------- 7. Golden Gai ----------
SHINJUKU[7] = R('20:00', 'Hanazono Shrine, then Golden Gai', 'The shrine is beside Golden Gai, lit at night. Golden Gai is a wander, not a destination. If a bar is full or regulars only, move on. Shinjuku has hundreds more.')
_i = [x[0] for x in GOOD['s']].index('Golden Gai')
GOOD['s'][_i] = ('Golden Gai', 'A wander, not a destination. Many bars charge a small cover and some are regulars only. If one does not feel right, move on.')

# ---------- 9. Aqua Luna ----------
_g = CHECK[0][1]; _i = [x[1][:9] for x in _g].index('Aqua Luna')
_g[_i] = ('h', 'Aqua Luna: confirm the 19:30 Symphony of Lights sailing from Tsim Sha Tsui Pier 1 is running on Tue 27, then book. +852 2116 8821')
D[27]['rows'][_row(27, '19:30')] = R('19:30', 'Aqua Luna harbour cruise', '45 minutes on a red-sail junk, one drink included. Confirm the sailing is running before you fly.', TB)

# ---------- 3, 5. Checklist ----------
_g = CHECK[0][1]; _i = [x[1][:10] for x in _g].index('Ubigi eSIM')
_g[_i] = ('s', 'Ubigi eSIM, one each. Install at home. Smartstart starts it when you land in Hong Kong on Fri 16')
CHECK.insert(0, ('Download and set up before leaving Melbourne', [
 ('', 'Offline Google Maps areas for Tokyo, Kyoto, Osaka and Hong Kong'),
 ('', 'Google Translate with Japanese and Chinese downloaded for offline use'),
 ('', 'Airline, booking, Klook and Ubigi apps installed and logged in'),
 ('', 'Banking apps working with Face ID, and international transactions enabled'),
 ('', 'Travel insurance policy, passports and booking confirmations saved offline'),
 ('', 'Licence and International Driving Permit photographed, as a backup only'),
 ('', 'Hotel names and addresses screenshotted in Japanese and Chinese (How-to 1)'),
 ('', 'Power banks charged, with a USB-C cable each'),
]))
