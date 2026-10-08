# ---------- Tsukiji moves to Tue 20 morning, Asakusa and Kappabashi to Mon 26 after teamLab ----------
_yoko = [
 R('07:30', 'Leave the hotel for Tsukiji', 'Ginza line to Ginza, then the Hibiya line two stops to Tsukiji. About 30 minutes, at the commuter peak.'),
 R('08:15', 'Tsukiji Outer Market breakfast', 'The best window, before the 10:00 rush. Tamagoyaki, tuna, grilled scallop and uni, strawberry daifuku. Eat at the stall. Then Namiyoke shrine.'),
 R('10:15', 'Train to Yokohama', 'About an hour. Hibiya line to Naka-meguro, then the Tōyoko line through to Minatomirai. Check the route on the day.'),
 R('11:30', 'Sakuragichō, Air Cabin, Minato Mirai waterfront', 'The cable car across the harbour, Red Brick Warehouses, the skyline. No rush today.'),
 R('13:00', 'Lunch on the waterfront', 'Then walk on along the harbour to Yamashita Park and into Chinatown.'),
 R('17:30', 'Chinatown dinner'),
 R('19:30', 'Train home from Motomachi-Chūkagai', 'Runs straight through to Shibuya, about 40 minutes, no change.'),
]
a = D[20]['alts']
a[0]['rows'] = _yoko + [R('20:30', 'Pack', 'Tomorrow is an early start.')]
a[0]['ttl'] = 'The Tsukiji and Yokohama day'
a[0]['sum'] = 'Breakfast at Tsukiji Outer Market in its best window, then a long Yokohama day: the waterfront, the harbour walk and Chinatown. The outdoor day: give it the better weather of Monday and Tuesday.'
a[0]['foot'] = 'Alternatives: the market also fits Monday 19 before the stores open, or first thing Monday 26 with teamLab moved to 13:30. The market is closed Sundays and Wednesdays.'
a[1]['sum'] = 'Swap the market morning for the coast, temples and the Great Buddha. Join the plan above about 14:30. The market goes to Monday 19 morning, or drops out.'
a[2]['sum'] = a[2]['sum'].replace('Asakusa and Yokohama', 'Tsukiji and Yokohama')
D[20].update(cal='Tsukiji, Yokohama', title='Tsukiji market and Yokohama')
b = D[19]['alts']
b[0]['foot'] = b[0]['foot'].replace('gets Asakusa and Yokohama', 'gets Tsukiji and Yokohama')
b[2]['rows'] = list(_yoko)
b[2]['sum'] = b[2]['sum'].replace('Asakusa and Yokohama', 'Tsukiji and Yokohama')

D[26].update(cal='teamLab, Asakusa', title='teamLab first thing, Asakusa, Shimbashi',
 sum='First session at teamLab, a look at Tokyo Tower, then across town to Kappabashi while the shops are open, Sensō-ji as the crowds ease and the Skytree at dusk, before a casual last night.')
_r = D[26]['rows']
D[26]['rows'] = [_r[0], _r[1],
 R('10:40', 'Sky Room Café, or Tokyo Tower and Zōjō-ji', 'Optional. Coffee on 33F beside the tower, or a 10 minute walk to the temple gate below it.'),
 R('11:30', 'Hibiya line, then Ginza line to Tawaramachi', 'From Kamiyachō, change at Ginza. About 30 minutes. From Zōjō-ji, the Asakusa line runs direct from Daimon.'),
 R('12:00', 'Kappabashi kitchenware street, then lunch', 'While the shops are open, most close about 17:00. Knives and ceramics. Lunch in Asakusa about 13:30.'),
 R('14:45', 'Sensō-ji, Kaminarimon, Nakamise street', 'Ten minutes east. If Nakamise is jammed, take the side lanes to the main hall.'),
 R('16:15', 'Skytree views at dusk, no deck', 'Free terrace at the Asakusa Culture Tourist Information Centre, then Azuma-bashi bridge. Sunset 16:55.'),
 R('17:30', 'Ginza line back to Shimbashi', 'Direct from Asakusa, about 15 minutes. Half pack at the hotel.'),
 _r[_row(26, '19:00')], _r[-1]]
D[26]['notes'] = [
 ('Why Asakusa is today', 'Ceramics and knives bought now go home without a trip through Kyoto. Knives fly in checked bags only. And the market on Tuesday comes before you are sushied out. Shops first as they close about 17:00, temple later as the crowds ease.'),
 ('Other shapes', 'Tsukiji can come back here at 08:00 with teamLab moved to 13:30, and Asakusa returns to Tuesday 20. If teamLab moved for wet weather, start in Asakusa about 10:00.')]
D[26]['extra'] = ('If Street Kart moved to today',
 [('The last backup, after Sunday 18 and Sunday 25', 'Strip the day to make 16:00: teamLab, Kappabashi, a short Sensō-ji, leave Asakusa by 14:30. Arrive 30 minutes ahead. Closed shoes, passports, physical licence and International Driving Permit.'),
  ('Afterwards', 'Straight to Shimbashi for dinner. Pack before you go out.')])
_s = D[25]['rows']; _i = [x[1] for x in _s].index('Optional: Skytree lit up')
_s[_i] = R(_s[_i][0], 'Optional: Tokyo Tower lit up', 'About 10 minutes by taxi. Best from the Zōjō-ji gate. The Skytree is Monday at dusk.')

LEGS['s']['sum'] = LEGS['s']['sum'].replace('old Tokyo at Asakusa and the waterfront at Yokohama', 'breakfast at Tsukiji and the waterfront at Yokohama')
LEGS['g']['sum'] = LEGS['g']['sum'].replace('teamLab first thing Monday then Tsukiji for lunch', 'teamLab first thing Monday then old Tokyo at Asakusa')
GOOD['g'][4] = ('Getting around', 'Everything this leg is walkable or a 10 minute taxi from the hotel, plus the Ginza line direct to Asakusa on Monday.')
for _g in CHECK:
    _g[1][:] = [(l, t.replace('to Asakusa and Yokohama', 'to Tsukiji and Yokohama')) for (l, t) in _g[1] if t != 'Decide on the Tsukiji and Asakusa swap']
h = _how('Moving teamLab for wet weather')
h[-1] = 'If it moves, Monday 26 starts in Asakusa about 10:00.'
h = _how('Laundry, Sun 25')
h[0] = h[0].replace('or Monday 26 afternoon while you pack', 'or Monday 26 before dinner')
