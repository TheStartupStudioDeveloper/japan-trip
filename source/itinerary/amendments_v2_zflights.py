# ---------- Friday 16: Melbourne to Hong Kong, overnight to Tokyo ----------
DAY16 = dict(d=16, dow='Friday', legs='', where='Melbourne to Hong Kong', cal='Fly to Hong Kong',
 title='Melbourne to Hong Kong, overnight to Tokyo',
 sum='Car to Moonee Ponds, a lift to the airport, nine hours to Hong Kong, a late-night stopover, then the overnight flight to Tokyo.',
 rows=[
  R('11:15', 'Leave home, park the car in Moonee Ponds', 'Glenn picks up Cynthia on the way.'),
  R('11:45', 'Lift to Melbourne Airport', 'About 15 to 20 minutes. Ask to be dropped at the Terminal 4 drop-off, which avoids the new forecourt arrangement.'),
  R('12:10', 'Walk from Terminal 4 to Terminal 2', 'About 10 minutes with the bags. Terminal 2 is international departures.'),
  R('12:25', 'Check in at the Cathay desks', 'Three hours before departure. Ask for the bags to be tagged through to Tokyo Narita, and collect both boarding passes.'),
  R('13:15', 'Security and passport control', 'Then lunch airside.'),
  R('14:45', 'Boarding'),
  R('15:25', 'CX104 departs Melbourne', 'About 9 hours 20 minutes. Hong Kong is three hours behind Melbourne.', 'b'),
  R('21:45', 'Land in Hong Kong, Terminal 1', 'Follow Transfer, not Arrivals. You stay airside: transfer security only, no immigration, no bags to collect. Switch on the Ubigi eSIM (How-to 2).', 'b'),
  R('22:30', 'Stopover: lounge or dinner', '3 hours 35 minutes. The Plaza Premium Lounge near Gate 1 is open 24 hours, has showers and can be booked online ahead, from about HK$650 each. Or eat in the food hall.'),
  R('00:40', 'At the gate', 'Check the screens for the gate first. Some gates are a train ride away, so leave the lounge 50 minutes before departure.'),
  R('01:20', 'CX524 departs for Tokyo Narita', 'About 4 hours 30 minutes. Tokyo is one hour ahead. Sleep if you can.', 'b'),
 ],
 foot='The night runs straight on into Saturday 17, which starts with the 06:50 landing at Narita.')

# ---------- Nezu Museum removed: closed for exhibition changeover 13 to 23 Oct 2026 ----------
_h = _how('While the stores are on, for G')
_h[:] = [x for x in _h if not x.startswith('Nezu Museum')]
