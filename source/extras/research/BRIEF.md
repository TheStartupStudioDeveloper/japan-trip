# J&HK Extras research brief (read fully)

G and Cynthia, Australians from Melbourne, first trip to Japan and Hong Kong, 16 to 31 Oct 2026. Today is 9 Oct 2026.
J&HK Extras is their "up our sleeve" reference app: everything worth doing that is NOT in their day plans, grouped by area,
for swapping things around, filling open slots ("eat wherever looks good"), or if something is missed.

Files in /tmp/claude-0/-home-claude/f96e2d08-84c7-5d2f-8bfa-bb192a8f0b3c/scratchpad/master_v2/:
- dayplan.txt: their full day plans (d16 to d30). Anything already in a day plan must NOT be added as an item.
- cards.txt: every existing place card (key | name | description). Don't create a new card for something that already has one.
- research/unscheduled_cards.txt: existing cards that are NOT scheduled. Every one that belongs to your area MUST become an item (reuse its key, no new card).
- research/shibuya_food.json and extras/extras.json: the finished Shibuya area. Match its tone, depth and shape exactly.

## Tastes and rules
- They like meat but NOT wagyu-specific restaurants (one wagyu burger in Tokyo is already covered). Special dinner budget about ¥10,000 to ¥20,000 a head (HK$800 to 1,500 in Hong Kong).
- Bars: cocktails, views, or bars special for some reason (famous, award-winning, unusual).
- Avoid places that need Japanese-only phone bookings, months-ahead bookings or concierge-only bookings. Prefer walk-in or English online booking (TableCheck, OpenTable, Omakase, Tabelog English, own site).
- Must try: the dishes or foods a visitor should try in that place (e.g. okonomiyaki and takoyaki in Osaka, yudofu or matcha sweets in Kyoto), each mapped to an item key (or an existing card key) where they can try it.
- Verify facts against current sources (WebSearch mode standard, extended only if thin; WebFetch). Hours and closed days matter most: check them against the actual dates they would go, and flag clashes. A past mistake was recommending a museum closed for those dates. Never invent. Tabelog scores only if seen in a source, else omit the tag.
- Writing: Australian spelling. NO em dashes and NO double hyphens anywhere (use full stops, commas or colons). Plain, warm, concise. 24-hour times like 11:00 to 22:00. Japanese place names with macrons where standard (Dōgenzaka, Kyōto is written Kyoto).

## What each area needs
1. Must try: 4 to 6 dishes or drinks.
2. Eat: 6 to 10 places across breakfast or coffee, quick lunches, a casual memorable dinner, one special dinner. Tie each to a real open slot in dayplan.txt in its "fits" line.
3. Drink: 2 to 4 bars.
4. Other groups as relevant, from: Views, Sights, Shopping, Night, Further out, Massage. Include the area's unscheduled existing cards here. Add 3 to 8 strong new non-food ideas where they genuinely add something.
Groups appear in this order: Eat, Drink, Views, Sights, Shopping, Night, Further out, Massage.

## Output: write ONE JSON file (path given in your task) with this shape
{
 "cards": { "<new-key>": {"n": "English name", "l": "local script name", "w": "2 to 3 sentence card description", "t": "hours, closed days, price, booking method, cash only if so", "m": "Google Maps search string"} },
 "areas": [ {
   "key": "shinjuku", "name": "Shinjuku", "pat": "s", "kanji": "新宿",
   "meta": "one line: which neighbourhoods it covers",
   "days": [["d19", "Mon 19"]],
   "must": [{"dish": "Tsukemen", "line": "one short sentence", "where": "<item or card key>"}],
   "items": [ {"group": "Eat", "key": "<key>", "time": "45 min", "one": "one line under 60 chars", "fits": "when it fits, tied to a day and slot, one or two short sentences", "tags": ["¥¥", "Walk-in"]} ],
   "notes": "anything G must know: closures clashing with dates, things to book this week"
 } ]
}
- Every item key must exist either in your "cards" or in cards.txt. New keys: kebab-case, unique, not clashing with cards.txt keys.
- Tags vocabulary: price "¥" "¥¥" "¥¥¥" (or "HK$" "HK$$" "HK$$$"), "Free", "Walk-in", "Book" (book ahead, any time), "Book now" (must be booked this week), "Cash", "Card only", "Tabelog 3.6".
- Keep the whole area to roughly 20 to 32 items.
Validate the JSON loads (python3 -c "import json;json.load(open(PATH))") and grep it for em dashes before finishing.
Then reply with a summary under 200 words: counts, anything to book now, and any date clashes.
