# Japan & Hong Kong Final Itinerary: changelog

## Master Itinerary V2 (7 October 2026). Steady state

Saved as the steady state and renamed "Japan & Hong Kong Master Itinerary V2", online and in the PDF. Content and layout are identical to V2.7. It gathers everything from V2.0 to V2.7 below.

Home-screen names, 9 October
- The three web apps now save to the home screen as "J&HK Itinerary", "J&HK Weather" and "J&HK Expenses" (previously "Japan", "Weather" and "Expenses"). Icons unchanged. Set in the manifests, the apple-mobile-web-app-title tags and the three build scripts.

Expenses update, 9 October
- Street Kart: Cynthia confirmed as the payer, so the "Payer to confirm" note is removed. Amounts and totals are unchanged (G AU$4,290.00, Cynthia AU$4,025.90, Cynthia owes G AU$132.05).
- First update made from the separate expenses chat, to the claude.ai page and the GitHub web app.

Expenses split out, 9 October, still V2
- The Expenses section and its link in the day bar are removed from the Master Itinerary, online.
- Expenses now has its own page, "Japan & Hong Kong Trip Expenses", on claude.ai and as a third home-screen web app at https://thestartupstudiodeveloper.github.io/japan-trip/expenses/ with its own icon. It is kept up to date in a separate chat.
- Source: expenses.json (unchanged, 15 entries) and expenses/expenses_build.py, which builds both copies.

Home-screen web app on GitHub Pages, 9 October, still V2
- The online itinerary is now also published at https://thestartupstudiodeveloper.github.io/japan-trip/ from the repository TheStartupStudioDeveloper/japan-trip. It opens with no sign-in.
- Adds a home-screen icon and the app name "Japan", offline support (network first, cached copy when there is no signal), and a no-index tag.
- site.py builds the GitHub copy from the same page. Every update goes to both the claude.ai link and GitHub.

Live features removed, 9 October, still V2
- The page no longer uses the shared live store, so it opens from the public link with no sign-in.
- Expenses: shown from expenses.json in the source. Claude updates that file and republishes the page for each new expense. The 15 entries are unchanged.
- Checklist: ticks are saved on each device again, not synced between devices. No ticks were stored in the shared store at the time.
- PDF: unchanged.

Kabukichō and Golden Gai notes, 9 October, still V2
- Mon 19, 18:45 Kabukichō row: ignore touts, never follow anyone off the street into a bar.
- Mon 19, 20:00 Golden Gai row: cash, a cover charge, look for English menus, regulars-only means move on, with a pointer to How-to 11.
- How-to 11 now also covers Golden Gai: English menus or signs mean visitors are welcome, regulars-only bars, cash, covers of roughly ¥500 to ¥1,500, photo rules, and touts in Kabukichō.
- Golden Gai card: tip updated to match.
- Not verified: cover charge range and photo rules are from general knowledge.

Money, G's options and massage, 9 October, still V2
- Tips, "Cash and coins": now gives a daily guide of about ¥5,000 to ¥10,000 each, adds temple entry and shrine charms to the cash-only list, says to top up as you go, and names Lawson, FamilyMart and Japan Post ATMs alongside 7-Eleven.
- Tips, "Cards and cash": adds "if an ATM or card machine offers to charge you in AUD, choose yen".
- How-to "While the stores are on, for G": the Nintendo line becomes Shibuya Parco (Nintendo Tokyo, Pokémon Center, Capcom Store, Jump Shop). Added Harakado with the Kosugi-yu bath, Tokyu Plaza Omotesando, and Ura-Harajuku.
- New How-to 21, "Massage near each hotel": two head spas and two body or foot places for each of Shibuya, Kyoto, Hibiya and Ginza, and Hong Kong, with hours and a booking note. New tip "Massage" points to it.
- Cards: 19 added (the four shopping places and 15 massage places), for 248.
- Online: place names in the Tips and the How-to appendix are now tappable too, not only in the days.
- Kept separate and not in the plan: the "Shibuya Sky Cancelled Sat Backup Plan".
- Not verified: Harakado bath and Parco floor details are from general knowledge. Massage hours are from Google listings on 9 October 2026.

Nezu Museum removed, 8 October, still V2
- How-to "While the stores are on, for G": the Nezu Museum line is removed. The museum is closed for an exhibition changeover from 13 to 23 October 2026, garden and café included (current exhibition ends 12 Oct, next opens 24 Oct, per the museum's schedule and visiting pages).

Expenses page, online only, 8 October, still V2
- New final section online, "Expenses", with a link in the day bar. It shows what G and Cynthia have each paid, the shared total, who owes whom to even up, and every entry in trip order with fees indented under their booking. Pending and estimated items are tagged.
- Rules as agreed: shared costs only, AUD as charged, flights left out.
- Entries carried over from the ledger kept in chat since 7 October: 15 lines, G AU$4,290.00, Cynthia AU$4,025.90, Cynthia owes G AU$132.05.
- Source data: expenses.json in the source files. The live page reads the page's own shared store, so Claude can update it during the trip without republishing. The two are kept in step.
- PDF: unchanged. The section does not print.
- Checklist: the duplicate "Ticks are saved on this device" line under the heading is fixed.

Fri 16 departure updated, 8 October, still V2
- 11:15 is now "Leave home, park the car in Moonee Ponds", with Glenn picking up Cynthia on the way. The note about photographing the parked car is removed, as the parking is secure.
- 11:45 lift to Melbourne Airport unchanged.

Steady state saved again on 8 October 2026, still V2
- Saved as the steady state at online version 32, with a 24 page PDF. It includes everything in the 8 October blocks below: Tsukiji and Asakusa swapped, Kyoto evenings and Friday reshaped, Nara reversed, the Kyoto Station bag drop, all four flights, Friday 16, the cover flight diagram, the live checklist and 229 place cards.

Updated the same evening, still V2
- Sat 17: sequence hotels check in at 17:00 as standard, an hour after Shibuya Sky. The 10:00 and 14:45 rows now say so. Bags are stored either way. What depends on early check-in is the shower and rest before Sky.
- Checklist: asking Sequence Miyashita Park for early check-in moved from "On the ground" to "Book or confirm before you fly". New line to ask the Blossom about pre-registering for Sat 24, so arrival is keys only before the fireworks.
- Sat 24: the Blossom check-in row mentions pre-registration.
- Laundry how-to: the Blossom is confirmed to have a guest laundry, with few machines.

Tsukiji and Asakusa swapped 8 October, still V2
- Why: Tsukiji Outer Market is best from 07:30 to 09:30 and at its worst from 10:00 to 12:00. The plan had it at 12:00 on Mon 26.
- Tue 20 is now "Tsukiji market and Yokohama": leave 07:30, market breakfast 08:15, train to Yokohama 10:15, waterfront from 11:30, lunch there, Yamashita Park, Chinatown dinner. Yokohama gains about three hours.
- Mon 26 is now "teamLab first thing, Asakusa, Shimbashi": teamLab 08:30 as booked, then optional Sky Room Café or Tokyo Tower and Zōjō-ji, Kappabashi at 12:00 while the shops are open, lunch, Sensō-ji at 14:45 as the crowds ease, Skytree views at dusk, Ginza line back to Shimbashi at 17:30.
- Mon 26 reasons noted on the page: ceramics and knives go home without a trip through Kyoto (knives in checked bags only), and the market comes earlier in the trip.
- Alternatives kept as short notes only: market on Mon 19 before the stores open, or market first on Mon 26 with teamLab at 13:30.
- Removed: the Mon 26 free afternoon, the "Backup: Asakusa today" note, the optional Skytree row on Mon 26, and the checklist line "Decide on the Tsukiji and Asakusa swap".
- Street Kart on Mon 26 is now described as the last backup, after Sun 18 and Sun 25, with the day stripped back to make the 16:00 slot.
- Follow-on wording: the weather rule and Shibuya Sky table now say "Tsukiji and Yokohama", the Kamakura alternative replaces the market morning, the leg summaries, the Hibiya "Getting around" line, the teamLab and laundry how-tos, and the Sun 25 Skytree note.
- Cards: Yamashita Park, Tawaramachi Station and Kamiyachō Station added (209 cards). Tsukiji card now carries the best hours and closed days.
- Sun 25: the optional evening row is now "Tokyo Tower lit up", not the Skytree. It is closer, there is no other night view of it, and the Skytree is covered at dusk on Mon 26.
- Not verified: train routes and times for Tsukiji to Yokohama and Kamiyachō to Tawaramachi, Kappabashi shop hours, Sensō-ji crowd pattern.

Online alternatives match the PDF, 8 October, still V2
- Online, Mon 19 and Tue 20: the "Shibuya Sky is on" tabs are gone. The main schedule shows once, and each alternative sits under it as a short boxed note, the same as the PDF. The full swapped schedules no longer appear online.
- PDF: unchanged.

- Cover key: the "Grey times are targets" label removed. The line under the key, "Times are targets, not commitments, unless marked booked", covers it.

Kyoto evenings and Friday reshaped, 8 October, still V2
- Why: Kiyomizu-dera and the Higashiyama lanes were timed for 14:15 to 16:15, their busiest hours, and both Kyoto dinners said "Gion or Pontochō".
- Dinners split: Pontochō on Wed 21, casual and walk-in. Gion on Fri 23, the one booked dinner. A swap note is on both days.
- Wed 21 evening: new rows for the Kyoto Station building at 17:15 (lit staircase, free rooftop garden, Kyoto Tower), check in at 18:00, Pontochō at 19:00 via Kiyamachi-dōri, and an optional Kamo River, Shirakawa canal or Teramachi arcades at 20:30.
- Fri 23: the sit-down Arashiyama breakfast is now coffee and a snack at 10:15. Nishiki Market lunch moves forward to 11:30. A rest at the hotel from 12:45, which doubles as slack. Kiyomizu-dera moves to 15:30, the lanes to 16:30, Yasaka Pagoda added at sunset 17:10, Yasaka Shrine and Gion at 17:30, dinner 18:30.
- Fri 23 removed: the "Further north instead" Ginkaku-ji note and the Sanjūsangen-dō and Kōdai-ji swaps, which no longer fit the later timing.
- Checklist: the dinner line now reads "Gion dinner for Fri 23, 18:30. Pontochō on Wed 21 is walk-in".
- Cards: nine added, for 218. Yasaka Pagoda, Shirakawa, Kiyamachi-dōri, Kamo River, Shijō Bridge, Teramachi and Shinkyōgoku arcades, Aritsugu, Kyoto Tower, Kyoto Station building.
- Not verified: the Hankyu route from Arashiyama, Kyoto Station staircase lighting times, shop closing times in the lanes, Aritsugu details.

Nara reordered, 8 October, still V2
- Why: the old order went Tōdai-ji, out to Kasuga Taisha, then back for Isuien or Nigatsu-dō, which both sit beside Tōdai-ji.
- Wed 21 Nara is now: Sanjō-dōri and lunch, Nakatanidō mochi, Kōfuku-ji and the first deer with deer crackers, Isuien (optional), Tōdai-ji at 14:00, Nigatsu-dō at 15:00, Kasuga Taisha at 15:30. Both Isuien and Nigatsu-dō now fit.
- Getting around is written into each row. All on foot, then a taxi from Kasuga Taisha to JR Nara at 16:15, with the walk (35 to 40 minutes) or loop bus as backup.
- Train back is 16:40, Kyoto 17:25. The Kyoto Station building, walk and check-in each move about ten minutes later. Pontochō stays at 19:00.
- Checked: the Kōfuku-ji five storey pagoda is covered for restoration from July 2023 to March 2034 (japan-guide.com construction list). The row and card say so.
- Cards: Kōfuku-ji, Nakatanidō, deer crackers and Nandaimon added, for 222.
- Later the same morning: Kōfuku-ji is no longer a stop, only a note that its pagoda is under restoration. The Isuien row is removed and kept as a one-line option in the footnote. The time goes to an unhurried hour with the deer from 12:45, then Tōdai-ji 13:45, Nigatsu-dō 14:45 and Kasuga Taisha 15:20.
- Not verified: walking times, taxi time, Isuien last entry, train times.

Nara reversed, 8 October, still V2
- Wed 21 now runs Kasuga Taisha first and Nigatsu-dō last: deer on the lawns 12:45, Kasuga Taisha and the lantern path 13:35 (outside only), Tōdai-ji 14:25, Nigatsu-dō 15:30 in the late light, taxi 16:15, train 16:40, Kyoto 17:25 as before.
- Why: Tōdai-ji after the midday school groups, calmer deer away from the gate, late light on Nigatsu-dō, and an easier taxi from the Tōdai-ji gate than from Kasuga Taisha.
- Lunch is now "Quick lunch", kept to 40 minutes, with kakinoha sushi suggested. A long lunch squeezes Nigatsu-dō.
- Notes added: no food in bags near the deer, stags are pushy in October, taxi backups are the loop bus or the GO app.
- Cards: kakinoha sushi, the Nara loop bus and the GO taxi app added, for 225.
- Checked on Google listings: Kasuga Taisha 07:00 to 17:00, Tōdai-ji Great Buddha Hall 07:30 to 17:30, Nigatsu-dō open all hours, Nakatanidō 10:00 to 18:00.
- Not verified: crowd patterns, taxi availability, bus frequency, walking times.

Kyoto Station bag drop named, 8 October, still V2
- Wed 21, 10:15: the row now names the counter. Crosta Kyoto, level B1 below the JR Central Gate, open 08:00 to 20:00, ¥1,000 per bag per day.
- How-to 13 rewritten as steps: which counter and which one to avoid (the Hachijō gate counter shuts at 18:00), what to take out of the bags first, the walk from the Shinkansen gates, where the counter is, how to get to the Nara line platforms, and collecting on the way back.
- Valuables reminder added to the row, the how-to, the Crosta card and the "Luggage and lockers" tip: passports, wallets, phones, chargers, medication.
- Hotel delivery noted as an option, not the plan: ¥1,500 a bag, drop by 14:00, arrives after 17:00.
- Card: Crosta Kyoto added, for 226.
- Checked: Crosta location, hours and fees (kyotostation.com, japan-experience.com, and the Kyoto City Hands Free site for hours). Hachijō gate counter hours 10:00 to 18:00 (Hands Free Kyoto).
- Not verified: the walking route from the Shinkansen gates to the Central Gate, Nara line platform numbers, payment methods at the counter, whether the hotel accepts deliveries.

Flights added, 8 October, still V2
- Cover: new Flights table with all four Cathay Pacific sectors, dates, times and terminals. CX104 Melbourne T2 15:25 to Hong Kong T1 21:45, Fri 16. CX524 Hong Kong T1 01:20 to Tokyo Narita T2 06:50, Sat 17. CX543 Tokyo Haneda T3 10:10 to Hong Kong T1 14:25, Tue 27. CX105 Hong Kong T1 00:30 to Melbourne T2 12:30, Sat 31.
- Cover route: the first hop now names CX524. PDF cover title is slightly smaller to fit the flights table on the page.
- Sat 17, Tue 27 and Fri 30: flight numbers and terminals added to the landing, departure and check-in rows. The Melbourne arrival time is on the last row.
- Checklist: the flight line now covers all four flights.
- Source: the booking itinerary supplied by G.

Friday 16 added and cover flight diagram, 8 October, still V2
- Cover: the flights table is replaced by a two-line diagram, Out and Home, with airport codes, times, terminals, a plane on each sector and the flight number. The Hong Kong stop in the middle reads "3 h 35 min stopover" going out and "3 nights" coming home. It stacks on a phone.
- The fortnight at a glance: Friday 16, "Fly to Hong Kong", is the first cell. The grid now runs Friday to Thursday.
- New day page, Friday 16, "Melbourne to Hong Kong, overnight to Tokyo": park in Moonee Ponds 11:15, lift to the Terminal 4 drop-off, walk to Terminal 2, Cathay check-in 12:25 with bags tagged through to Narita, CX104 at 15:25, land Hong Kong 21:45 and stay airside, stopover with the Plaza Premium Lounge near Gate 1 as the paid option, CX524 at 01:20.
- Day bar online gains 16. The cover line now reads "Friday 16 to Saturday 31 October 2026. Four legs, sixteen days."
- PDF is now 24 pages. Friday 16 is page 3.
- Cards: Melbourne Airport, Plaza Premium Lounge and the Hong Kong transfer added, for 229. The Cathay card now lists all four flights.
- Checked: Plaza Premium Lounge near Gate 1 is on Level 6 of Terminal 1 departures, open 24 hours, bookable online at least an hour ahead, from HK$650 (plazapremiumlounge.com).
- Not verified: drive and walk times in Melbourne, whether bags can be tagged through, whether showers are included in the lounge rate, the departure gate, flight durations.

Live checklist online, 8 October, still V2
- The checklist ticks now save to a shared store attached to the page, so they follow you across devices and update live. A line under the Checklist heading says which mode is active.
- If the shared store is not available to a viewer, ticks fall back to being saved on that device, as before.
- PDF: unchanged.

Interactive place cards added 8 October, still V2
- Online: 174 place names are now tappable, across the four legs page, every day and the Hong Kong swaps. Each opens a card with the name in English and local script, what it is, a "Good to know" line, and two buttons: See photos and Open in Maps.
- Covered: sights, streets, markets, shops, stations, airports, trains, the four hotels, food terms such as ekiben, kushikatsu, yum cha and egg tart, and Hong Kong terms such as the old tram and red taxis.
- PDF: unchanged. The links and cards do not print.
- One source: the cards live in places.py and are applied when the page is built, so the online page and the PDF always come from the same data.
- The first mention of each place on each day is the one linked.

Layout fix 8 October, still V2
- PDF, Mon 19 and Tue 20: the footnote in the first box now has proper space above the bottom border. The gap between the boxes on those two pages is a millimetre smaller to keep each day on one page.

- Cover: the line "Times are targets, not commitments, unless marked booked" moved from the end of the document to the cover, under the key.

- Place cards, second pass: every mention of a place is now linked, not only the first on each day. 29 cards added, for 203 in total, covering districts (Shibuya, Shinjuku, Kyoto, Osaka, Kowloon), Sanjō-dōri, the Yamanote line, Suica, Octopus, Visit Japan Web, the Osaka resale chains and more.
- Online, Mon 19 and Tue 20: bottom padding added inside the day box, which was missing whichever Shibuya Sky tab was selected.

- How-to 1: all four hotels are now listed with their addresses in local script, in trip order.
- sequence KYOTO GOJO card corrected: the hotel is at Karasuma-Gojō, by Gojō subway station.

Kyoto hotel location corrected 8 October, still V2
- sequence KYOTO GOJO is at Karasuma-Gojō, three minutes from Gojō subway station and one stop from Kyoto Station. The plan had assumed it was beside Kiyomizu-Gojō station on the Keihan line, about a kilometre east. Address confirmed by G from the booking.
- Wed 21 and Sat 24: the walk between Kyoto Station and the hotel is about 15 minutes, not 20 to 25, or one subway stop.
- Thu 22: Osaka is now by JR special rapid from Kyoto Station, then the Osaka Loop Line to the castle. Leave the hotel at 07:00. The return is the Midōsuji line to Umeda and JR back. The Keihan line is out of the plan.
- Fri 23: Kiyomizu-dera is a 10 minute taxi, not a 20 minute walk. The note that the hotel sits at the foot of the Kiyomizu approach is replaced.
- Sat 24: Fushimi Inari is by JR Nara line from Kyoto Station to Inari, leaving the hotel at 06:30.
- How-tos 13, 14 and 16 rewritten to match. Checklist line changed from the Keihan train to the JR special rapid.
- Four legs page and hotel cards: each hotel now shows who booked it and how. Sequence Miyashita Park direct by Cynthia, sequence KYOTO GOJO and the Blossom on Booking.com by G, the Sheraton on Agoda by Cynthia.

Files
- Japan-Hong-Kong-Master-Itinerary-V2.pdf
- Japan-Hong-Kong-Master-Itinerary-V2-source.zip

## V2.7 (7 October 2026). PDF appendix matches the online layout

Layout only, in the PDF. No content changes.

- Appendix: each how-to is a full-width box, one under the other, as online. Two columns are gone, the type is larger, and most steps sit on one line.
- The appendix runs to four pages, up from three. The PDF is 23 pages.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.7.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.7-source.zip

## V2.6 (7 October 2026). PDF checklist and tips match the online layout

Layout only, in the PDF. No content changes, and the online page is unchanged apart from the version number.

- Checklist: one item per line across the full width, with a rule under each, as online. Larger type and no wrapped lines. Still one page.
- Tips: two columns in place of three, with larger type. Still one page.
- Reason: the online layout reads better, and a tick list is easier to follow straight down.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.6.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.6-source.zip

## V2.5 (7 October 2026). Checklist audited, regrouped and on one page

The section is renamed "Checklist". It is regrouped by when each thing can actually be done, and sits on one page of its own. No day pages change. This entry replaces three interim builds made the same evening.

### Groups, in order

- Set up at home: the phone and download lines, plus the eSIM, Suica and Octopus, and Visit Japan Web. These lines carry no leg label.
- Book or confirm before you fly: only things with fixed dates.
- Decide with the Tokyo forecast: new. The Shibuya Sky day, the Monday and Tuesday order, the teamLab move, and the Tsukiji and Asakusa swap.
- Decide with the Hong Kong forecast: Aqua Luna, the Peak Tram, the Central dinner, the Ngong Ping day, and Ozone.
- On the ground: sorted by date, each line starting with its day.

### Moved, and why

- Aqua Luna, the Central dinner and Ozone moved out of "Before you fly". Reason: each depends on the forecast or on the sailing being confirmed, so they cannot be settled from home.
- Packing items are not in the checklist. They sit in Tips, with two new tips: "Power" and "Street Kart".

### Merged or reworded

- The four Sheraton lines became two, one for arrival and one for Friday.
- Settling the Blossom bill and checking the Haneda train became one Monday 26 line.

### Layout

- The checklist starts on its own page and fits on one page, with open spacing.
- The Hong Kong swaps box is on its own page, as in V2.3.
- Online, ticks are saved against each line's wording, so reworded lines start unticked.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.5.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.5-source.zip

## V2.4 (7 October 2026). Appendix and Tips reordered, phone and money setup

Ten notes applied on top of V2.3. No day changes shape. The PDF goes from 21 to 22 pages, because the appendix now has 20 how-tos at its earlier, larger type size.

### Reordered

Appendix
- The how-tos are now in the order of the trip, and renumbered. Whole-trip ones come first (1 to 4), then Saturday 17 through to Thursday 29.
- Every "How-to" pointer on the day pages, Tips and checklist was renumbered to match.
- Old to new: Narita Express 1 to 5. Station to hotel 2 to 6. Shinkansen 3 to 12. Kyoto bags 4 to 13. Kyoto to Tokyo 5 to 16. Haneda 6 to 18. Osaka 7 to 14. eSIM 8 to 2. Suica and Octopus 9 to 3. Tax-free 10 to 4. teamLab 11 to 8. Ngong Ping 12 to 20. Peak Tram 13 to 19. Dōtonbori 14 to 15. Omoide Yokochō 15 to 11. Store hours 16 to 9. G's options 17 to 10. Shibuya Sky 18 to 7.

Tips
- Now in the order you first need them: before you go, on landing, first meals and shops, the first shrine, the Kyoto leg, then Hong Kong.
- Laid out as flowing columns, so there are no gaps under short tips. They read down each column.

### Added

- How-to 1, Phones and power: offline maps, confirmations saved offline, hotel names and addresses in the local script, power banks, nightly charging, one phone kept able to receive Australian SMS.
- How-to 17, Laundry: when to do it, how, and the fallbacks. Sunday 25 breakfast carries a one line pointer to it.
- Checklist, new first group "Download and set up before leaving Melbourne": eight lines covering maps, translate, apps, banking, documents, licence photos, address screenshots and power banks.
- Tips, "Cards and cash": two cards kept apart, one card and emergency cash in the room safe. "Cash and coins" now names the coins to keep.

### Changed

- How-to 2, eSIM, rewritten: install at home, no manual activation, Smartstart starts the plan at the first connection in Hong Kong on Fri 16 October, Data Roaming on for Ubigi and off for the Australian SIM, keep the Australian number for SMS, and a Hong Kong only SIM if more data is needed at the end. Reason: Ubigi confirms the plan and its validity start automatically on first connection in a covered place.
- Golden Gai, Mon 19 and the four legs page: described as a wander, not a destination. If a bar is full or regulars only, move on.
- Aqua Luna, Tue 27: the checklist line now says to confirm the 19:30 sailing is running before booking, with the phone number. Reason: the booking page showed a cancelled sailing when checked, and tickets are non-refundable.
- Tips, "Flu season" replaced by "Crowded trains": hand sanitiser, and a mask if you prefer one.

### Removed

- Tips: Smoking and Typhoon season.
- The vitamins line.

### Layout

- Appendix type restored to its V2.1 size. It runs to three pages.
- The checklist now starts under the Hong Kong swaps box and runs onto a second page, in place of leaving that page mostly empty.
- The new checklist group is marked "All" with a plain white chip, since it belongs to no single leg.

### Still to confirm

- Guest laundry at THE BLOSSOM HIBIYA and at sequence KYOTO GOJO. Neither could be confirmed, so the how-to says to ask at check-in.
- Hotel names in local script are printed for the Blossom and the Sheraton only, both checked. For the two sequence hotels, take them from the booking confirmations.
- Whether Aqua Luna is sailing on Tue 27.
- Everything listed under earlier versions remains open.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.4.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.4-source.zip
- Japan-Hong-Kong-Itinerary-Changelog-v2.4.pdf

## V2.3 (7 October 2026). Late checkout Friday, and five practical notes

Six notes applied on top of V2.2. Structure, design and layout are unchanged. The PDF stays at 21 pages.

### Moved or reshaped

Fri 30. Pool, yum cha, Ozone at sunset, then departure
- Rebuilt around the late checkout, now confirmed to 18:00. The room is yours all day.
- New flow: lounge breakfast 09:00, Sheraton pool 09:45, yum cha lunch 12:30, a spare window from 14:00, back to pack and shower at 16:15, check out 17:20, Ozone at 17:40 for the 17:50 sunset, dinner 19:15, bags 20:30, taxi 20:45.
- Removed: the 12:00 checkout, the W Hong Kong pool day, the Kerry Hotel alternative, and showering at the W. Reason: with the room until 18:00, a paid day pass is not needed.
- Checkout is set at 17:20, not 18:00, to catch the sunset at Ozone. Ask on the day whether it can go later still.
- Yum cha has a firm slot for the first time. It is a daytime meal, so lunch is the right place. An all-day dim sum place can stand in for dinner if lunch slips.
- If the Peak or Ngong Ping was missed, it takes the morning in place of the pool.

Thu 29
- Ozone becomes optional at 18:15, with Friday as the plan. If you go on Thursday, Friday evening is free.
- Lunch no longer carries the yum cha note.

Hong Kong swaps
- "W pool on Wednesday" removed. "Ngong Ping on Friday" rewritten around the late checkout. Three swaps remain.

### Added

- Street Kart, Sun 18: fully closed shoes, the physical licence card, the physical International Driving Permit and passports. Repeated on the two backup boxes, and added to the checklist.
- Shibuya Sky, Sat 17: bags stay in the room, go up with phones and pockets only. The same line is on the Monday and Tuesday backup slots. New How-to 18 lists what the rooftop does not allow.
- Backup plan, to decide with the forecast: Tsukiji moves to Tuesday 20 morning with a longer Yokohama, and Asakusa and Kappabashi move to Monday 26 after teamLab, ending with the Skytree at dusk. Noted on both days. Neither day changes.
- Tips: "Shoes" becomes "Shoes and socks", with a clean spare pair on temple and shrine days.
- Tue 27: check whether the Agoda booking includes an airport pickup to the Sheraton, before taking the red taxi.

### Checklist

- Removed: W day pass, Kerry Daycation, chasing the Sheraton email, the W or Kerry pool pass, and asking for late checkout.
- Added: Street Kart shoes and documents, the Agoda pickup check for Cynthia, an Ozone booking for Fri 30, a yum cha place for Fri 30, and asking the Sheraton if checkout can go later than 18:00.
- Ticks are now saved against the wording of each line, not its position, so future versions keep your ticks. They reset once with this version.

### Trimmed to fit

- A few row notes on Sat 17 and Mon 26 were shortened, and two Mon 26 notes merged, so each day still fits one page. No information was dropped.

### Still to confirm

- Ozone: hours and dress code are from a rooftop bar guide, not the hotel. Book ahead.
- Shibuya Sky rules are from a travel guide, not the venue's own page.
- Yum cha venue for Friday. Whether Agoda includes the pickup. Uber as the alternative to the red taxi was discussed and is not in the plan.
- Everything listed under earlier versions remains open.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.3.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.3-source.zip
- Japan-Hong-Kong-Itinerary-Changelog-v2.3.pdf

## V2.2 (7 October 2026). Saturday times and Monday extras

Four notes applied on top of V2.1. Structure, design and layout are unchanged. The PDF stays at 21 pages.

### Added

Sat 17. Arrive and wander Shibuya
- Every row now has a general time, where V2.1 had "Morning", "Lunch" and so on: Narita Express 08:15, Shibuya Station 10:00, Miyashita Park and Cat Street 10:30, lunch in Omotesando 12:30, back into Shibuya 13:45, supplies and check in 14:45, dinner 18:30. Reason: it was the only day without times.
- The Narita Express and the walk to the hotel are now two rows.
- Only the landing and Shibuya Sky are fixed. If the airport is slow, the morning slides and Cat Street absorbs it.

Mon 19. Omotesando stores, Shinjuku after dark
- The stores row now says all open at 11:00 except Casanova at 12:00, and points to How-to 16 and How-to 17.
- Footnote added: if you are running early, go into Shinjuku sooner and wander the station and the east side streets. Shinjuku Gyoen is the park to see, on a Tuesday only, because it closes on Mondays.

### Appendix

- New How-to 16, Omotesando and Aoyama store hours.
- New How-to 17, options for G while the stores are on: the Roppongi design loop, the Nezu Museum, Nintendo Tokyo, a gym session, Shibuya Saunas, and the Kairyo-yu sento.
- The appendix type is a fraction smaller, to keep 17 how-tos on two pages.

### Decided and left alone

- Monday and Tuesday mornings stay as they are. Swapping them was looked at and dropped: it cost the relaxed Monday and most of the Yokohama daylight.
- Asakusa on Sunday and the stores on Sunday were both looked at and dropped.

### Still to confirm

- Narita Express: which train stops at Shibuya, and its exact time.
- Brand Collect and ALLU opening times are as supplied by G, not checked.
- Gold's Gym Harajuku is closed on the third Monday of the month, which is Monday 19. A gym for that day is not yet found.
- Kairyo-yu tattoo policy. Nezu Museum and 21_21 exhibition dates for 19 and 20 October.
- Everything listed under V2.0 and V2.1 remains open.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.2.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.2-source.zip
- Japan-Hong-Kong-Itinerary-Changelog-v2.2.pdf

## V2.1 (7 October 2026). Sunday and Monday rebalanced

Seven notes applied on top of V2.0, all on the Shibuya leg. The aim was to spread the days: a fuller but light Sunday, and a Monday that starts slowly and builds. Structure, design and layout are unchanged. The PDF stays at 21 pages.

### Moved or reshaped

Sun 18. Meiji Jingū, Harajuku, the festival, Street Kart
- New morning: slow breakfast, Meiji Jingū at 09:45, Takeshita Street and the Harajuku back lanes at 11:00, lunch in Harajuku, then Cat Street back into the festival streets at 13:15. Street Kart is unchanged.
- Removed: Daikanyama and lunch in Daikanyama or Ebisu. Reason: pleasant but not essential, and the morning felt thin.
- Meiji Jingū and Takeshita Street moved here from Monday. Reason: both cope well with a Sunday, the whole morning is on foot from the hotel, and nothing in it puts Street Kart at risk.

Mon 19. Omotesando stores, Shinjuku after dark
- New flow: late breakfast at 09:30, the Omotesando and Aoyama stores from 11:00 to 14:00 (was 13:30), lunch, back to the hotel at 15:00 to drop bags and rest, then Shinjuku from 16:45.
- Shinjuku now runs one way: the 3D cat at dusk, Omoide Yokochō at 17:30, Godzilla, Kabukichō and Kabukichō Tower at 18:45, Hanazono Shrine and Golden Gai at 20:00, Fukutoshin line home at 21:30 (was 22:30).
- The stores stay on Monday, not Sunday. Reason: a quiet weekday, no deadline behind the shopping, and some shops only open at 12:00.
- Added: the hotel drop-off, Hanazono Shrine, Kabukichō Tower.
- Removed: Bar Benfiddich, and Isetan as a scheduled stop.
- Noted as of interest if plans change: the Government Building deck, best about 16:15 for dusk, and the Isetan food hall.

### Weather rule for Monday and Tuesday

- The better weather day of the two gets Asakusa and Yokohama, which is all outdoors. The other gets the Shinjuku day, which is shops, covered alleys and bars.
- If Shibuya Sky has to move off Saturday, it takes the clear evening and that day becomes the Shinjuku day, as before.
- The rule appears on the Shibuya Sky box on Sat 17, and on Mon 19 and Tue 20. Both "if Shibuya Sky is on" panels were rewritten to match the new Monday.

### Appendix

- New How-to 15, Omoide Yokochō: what it is, when to arrive, how to order, the seating charge, cash.

### Still to confirm

- Whether the Omotesando stores other than Vintage Qoo trade on Tuesdays, in case the weather rule moves the Shinjuku day there.
- Omoide Yokochō seating charges and card acceptance, which are from general knowledge.
- Everything listed under V2.0 remains open.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.1.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.1-source.zip
- Japan-Hong-Kong-Itinerary-Changelog-v2.1.pdf

## V2.0 (7 October 2026). Review pass

All 32 notes from the itinerary review applied in one pass, as amendments to V1.10. V1.10 is kept untouched as the official V1, on its original link. Structure, design and layout are unchanged. Two sections are new, both at the end: Tips, and a how-to Appendix. The PDF goes from 17 to 21 pages.

### Moved or reshaped

Mon 19. The Shinjuku day
- Morning rebuilt: Meiji Jingū 09:00, Takeshita Street 10:00, Omotesando and Aoyama vintage luxury 11:00 to 13:30, lunch in Omotesando, then Shinjuku. Reason: the old morning was thin, and this is the best vintage luxury stretch of the trip for Cynthia.
- Removed: Yoyogi Park and the Government Building deck.
- Added: the 3D cat billboard at the east exit, and a small reminder that Bar Benfiddich is nearby (open from 19:00, no booking, only if passing).
- The night ends with a train about 22:30, not a late taxi.
- Wet weather line added: teamLab can take the morning, or the Sumo show. Tsukiji could also fit. Monday and Tuesday still swap as whole days.
- The two "if Shibuya Sky is on Monday or Tuesday" panels rewritten to match the new day.

Wed 21. Shibuya to Kyoto
- Whole morning earlier: wake 05:55, check out 06:20, taxi 06:30 (was 07:00), at Shinagawa by 07:00. Reason: the Shinkansen cannot be missed, and there is time for food.
- Bags are stored at the Kyoto Station staffed counter, not forwarded by Sagawa. Collected after Nara, then a 20 to 25 minute walk to the hotel. Check in moves to about 18:00.

Thu 22. Osaka
- New order: Keihan line to Temmabashi, Osaka Castle up close with takeaway breakfast, Umeda Sky at 10:15, Kuromon lunch at 12:00, shops at 13:15, Namba Yasaka lion head at 15:30, Shinsekai at dusk, Dōtonbori, Hōzenji Yokochō, home by Midōsuji line and Keihan.
- Removed: Nakazakichō breakfast, Nakanoshima, and Abeno Harukas 300 (its To book row, checklist line and closing time). Reason: one deck in a day is enough. Harukas stays only as a weather fallback.
- Added: the Enjoy Eco Card metro day pass, the Tombori River Cruise, the Glico photo platform at the Nanohana shop, the Mizukake Fudō.

Mon 26. teamLab and Tsukiji
- teamLab is now Booked (08:30 first session) rather than To book.
- New flow: teamLab, Tokyo Tower and Zōjō-ji at 10:50, two stops to Tsukiji Outer Market for lunch at 12:00, walk back through Ginza, free afternoon from 14:00, Shimbashi at 19:00 (was 18:00).
- Removed: the 08:15 coffee stop, the separate Azabudai Hills wander, lunch nearby. Sky Room Café becomes optional.
- Notes added: why the market only fits Monday, the reverse order with a market tour, and what happens if teamLab was used earlier as a wet weather move.
- New box: Street Kart can move to this afternoon at 16:00.

Tue 27. To Haneda
- Train is now the default: wake 05:45, leave 06:22, 06:38 Airport Rapid Limited Express from Shimbashi platform 1. The taxi becomes the fallback note.

Wed 28. The Peak
- Peak Tram up at 15:45 (was 16:45) on a standard one-way ticket, sitting on the right. Taxi down at 18:45, because tram seats face backwards going down.
- To make that work the pool block ends about 13:00 (was 14:00) and the ferry leaves at 13:30 (was 14:30).
- Added: Graham Street Market, and the Klook Fast Track note (Friday to Sunday only).

### Added to existing days

- Sat 17: Suica already in Apple Wallets. Narita Express ticket bought at Narita. Walk from the Hachikō exit, lobby on 4F. Don Quijote and 7-Eleven supplies run. Safety valve if shattered. "Harajuku" and the vintage mention taken out of Saturday, by choice.
- Sun 18: Street Kart backup is now Sunday 25 or Monday 26.
- Fri 23: Higashiyama named as its own line above the three afternoon stops. Lunch is at Nishiki Market.
- Sat 24: check out 10:30 and walk to Kyoto Station.
- Sun 25: passports for tax-free, the Ginza vintage fallback, optional Skytree lit at 19:30, teamLab as a wet morning option, the Sushi Bus idea.
- Thu 29: Crystal cabin on the Klook voucher. Yum cha for lunch. Ozone at the Ritz-Carlton at 18:15, with Friday as the backup. The 17:30 rest becomes a quick change.
- Fri 30: retitled "Pool day or spare day". Kerry Hotel Daycation as the alternative to the W. Late checkout note reflects the email already sent. Ozone as the dinner alternative.
- Hong Kong swaps: the Ngong Ping voucher moves with the day.

### The four legs, calendar, checklist

- Leg summaries updated for Shinjuku, Hibiya and Hong Kong. Kyoto closing times and the Thursday and Friday swap note updated. Pool blocks marked optional.
- Calendar tiles: Mon 19, Mon 26 and Fri 30 relabelled.
- Checklist. Removed: Harukas ticket, teamLab booking, Suica at Narita, taxi to Haneda. Added: Suica and Octopus in Apple Wallets, Ubigi eSIM, Ngong Ping vouchers (moved up to Before you fly), Kerry Daycation, Sheraton email follow up, Narita Express tickets, the 06:30 taxi, and the two train checks. Ticks start fresh in V2.

### New pages

- Tips: 30 short tips. Passports and tax-free, cash, etiquette, escalators, trains, shrines, luggage and lockers, wet gear, flu season, data, and three for Hong Kong.
- Appendix: 14 step by step how-tos. Day pages point to them by number.

### Still to confirm

- Kerry Hotel Daycation price and inclusions. Sumo show venue and times. Ozone hours and dress code.
- Tombori River Cruise times and price. Enjoy Eco Card price. Keihan and Asakusa line train times (check the night before).
- Kyoto Station luggage counter closing time. Sushi Bus day. Yum cha venue.

Files
- Japan-Hong-Kong-Final-Itinerary-v2.0.pdf
- Japan-Hong-Kong-Final-Itinerary-v2.0-source.zip
- Japan-Hong-Kong-Itinerary-Changelog-v2.0.pdf

## V1.10 (5 October 2026). Leg 1 renamed, Street Kart backup, Tuesday 20 reworked

Version numbers were reset at this point. This entry replaces the earlier V1.10, V1.11 and V1.12, and contains all three sets of changes.

Tue 20
- Main plan is now East Tokyo then Yokohama: Ginza line to Asakusa 08:30, Sensō-ji and Nakamise 09:05, Skytree views without the deck 10:15, Kappabashi kitchenware street 10:45, lunch in Asakusa 12:30, Asakusa line towards Yokohama 13:30.
- Yokohama afternoon from 14:45 now starts at Sakuragichō with the Air Cabin, then the Minato Mirai waterfront. Chinatown dinner, train home and packing are unchanged.
- Kamakura is now "Alternative morning: Kamakura", a short list that joins the plan at 14:45.
- Skytree deck is skipped. Views come from the free terrace opposite Kaminarimon and from Azuma-bashi bridge.
- Decided against swapping this morning with teamLab on Mon 26: teamLab is a timed ticket and would break the Shibuya Sky day swap.
- Sat 17 decision table, Mon 19 swap note, the calendar and the leg summary now say Asakusa and Yokohama instead of Kamakura and Yokohama.

Street Kart backup
- Sun 18: new block "If Street Kart can't run today". Spend the extra time in Shibuya, and rebook for Sunday 25 while staying in Hibiya.
- Sun 25: matching block "If Street Kart moved to today". Leave the Ginza shopping about 14:45 for a 16:00 slot, then back to Ginza for the late shops and dinner.
- Checklist: check Street Kart's change and rebooking terms before flying.

Four legs page
- Leg 1 is titled "Shibuya, Shinjuku and Yokohama" instead of "Tokyo: Shibuya".

Files
- Japan-Hong-Kong-Final-Itinerary-v1.10.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.10-source.zip

## V1.9 (5 October 2026). Pink pattern bug fixed in the PDF

Problem
- In the PDF, the Kyoto and Hong Kong patterns showed as flat pink blocks in some PDF viewers. Both were built from CSS gradients, which the PDF stored as gradient shading objects that those viewers draw incorrectly. Hibiya and Shibuya were not gradients, so they were unaffected.

Fix
- Kyoto and Hong Kong patterns are now drawn as plain vector shapes (bars and diagonal bands). The PDF contains no gradient or pattern objects at all, verified after the build.
- Hong Kong is a wide charcoal diagonal on white, per the reference.
- Same change online, so both stay identical.

Content
- No change.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.9.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.9-source.zip

## V1.8 (5 October 2026). Hong Kong pattern: wide charcoal diagonal

Design
- Hong Kong is now a wide diagonal stripe in charcoal on white, matching the supplied reference.
- All pattern colours are now written directly into each pattern (black, charcoal, white) with a solid white backing, instead of being passed through shared colour settings. Nothing outside the page can tint them.
- Patterns: Shibuya solid black, Kyoto vertical stripes, Hibiya centre bar, Hong Kong wide charcoal diagonal.

Content
- No change.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.8.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.8-source.zip

## V1.7 (5 October 2026). Leg pattern keys fixed

Design
- Problem found: in the thin bands on the calendar and day pages, Hibiya's grid collapsed into a row of small boxes that read the same as Kyoto's vertical stripes.
- Hibiya pattern changed from a grid to a single centre bar inside an outline. It holds its shape at every size.
- Patterns are now: Shibuya solid, Kyoto vertical stripes, Hibiya centre bar, Hong Kong diagonal stripes. All black and white.
- Applies to the route key, calendar, leg cards, day bands and checklist.

Content
- No change.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.7.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.7-source.zip

## V1.6 (5 October 2026). Wednesday night restored

Wed 28
- "Late: Bars in Central" is back after dinner, with the way home: taxi through the tunnel, or the MTR from Central to Tsim Sha Tsui.
- The old tram and Wan Chai Star Ferry now sits under it as the optional variation on the way home. Last ferry from Wan Chai is 23:00, so it means leaving the bars by about 22:15.

Design
- No change. Patterns remain black and white: Shibuya solid, Kyoto vertical stripes, Hibiya grid, Hong Kong diagonal.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.6.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.6-source.zip

## V1.5 (5 October 2026). Wednesday night and leg patterns

Wed 28
- Dinner row back to "The big dinner of the trip. Book ahead."
- The last row is now "Optional": old tram to Wan Chai, then the Star Ferry home. It replaces both the bars row and the separate ferry row and note from V1.4.

Design
- Hong Kong pattern changed from dots to bold diagonal stripes, so it no longer reads like Hibiya's grid. Applies to the route key, calendar, leg cards, day bands and checklist.
- Hibiya grid opened up slightly.
- Patterns are now: Shibuya solid, Kyoto vertical stripes, Hibiya grid, Hong Kong diagonal.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.5.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.5-source.zip

## V1.4 (5 October 2026). Hong Kong reshaped, Odaiba statue added

Thu 29
- Versions A, B and C removed. One plan: "Ngong Ping cable car, Big Buddha, then the city".
- First cable car at 10:00, back to Central for lunch, Sheung Wan shops, Star Ferry home at 17:00, rest, Temple Street at 19:30.
- Man Mo Temple reminder added to the Sheung Wan row.
- New block "Notes and optionals for Thursday": skipping the cable car, weather, gentler start, old tram.
- Lamma Island removed entirely, including its checklist items.

Wed 28
- Bars in Central removed. After dinner: Star Ferry from Central, early night before Thursday.
- Optional note: old tram to Wan Chai and the ferry home from there. Wan Chai sailings confirmed to run until 23:00.

Tue 27
- A Symphony of Lights added at 20:00 with a note on what it is.
- Avenue of Stars walk added at 20:20, after the cruise. Dinner moves to 20:45.

Sat 24
- Optional Odaiba Statue of Liberty at 21:15, after dinner. Yurikamome moves to 21:45, back about 22:30.

Elsewhere
- Hong Kong swaps rewritten to fit the single Thursday plan.
- Friday wet weather note updated.
- Checklist: cable car tickets now first car at 10:00. Sheraton pool booking question covers Wednesday only.
- PDF is 17 pages (Thursday is one page).

Files
- Japan-Hong-Kong-Final-Itinerary-v1.4.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.4-source.zip

## V1.3 (5 October 2026). Shibuya pages tidied

Content
- Removed the "Shinjuku Gyoen is closed on Mondays" notes from Mon 19 and from the Shibuya leg summary.
- Shibuya Music Festival note moved into the Shibuya leg summary on the four legs page, in place of the Shinjuku Gyoen note. Removed from Sat 17.
- Sat 17: "Which day is Shibuya Sky?" is now its own block, separate from the Saturday plan.
- Tue 20: "If Shibuya Sky is on Tuesday" is now a short change list like Monday's, instead of a full timetable. It notes the garden is open Tuesdays (not Mondays), so it is the garden or the Government Building deck.
- No times or bookings changed.

Online
- With the switch on Tuesday, the Tuesday card shows the change list followed by the Shinjuku timetable.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.3.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.3-source.zip

## V1.2 (5 October 2026). Shibuya Sky decision simplified

Content
- "Plan B" removed for Mon 19 and Tue 20. Replaced by one decision: which day is Shibuya Sky (Saturday, Monday or Tuesday).
- Sat 17: a decision table under the Shibuya Sky booking shows what Monday and Tuesday become for each choice. It replaces the weather plan paragraph.
- Mon 19: the Shinjuku day, written once. "If Shibuya Sky is on Monday" is a three line change list. "If Shibuya Sky is on Tuesday" says the days swap.
- Tue 20: the Kamakura and Yokohama day, written once. "If Shibuya Sky is on Tuesday" carries the Shinjuku timetable with the sunset slot and Shinjuku Gyoen.
- The Kamakura and Yokohama timetable is no longer printed twice.
- No times or bookings changed.

Online
- One three way switch, "Shibuya Sky is on", sets Monday and Tuesday together.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.2.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.2-source.zip

## V1.1 (5 October 2026). Online matches the PDF

Online
- Black and white throughout, same as the PDF. Leg colours removed; legs are identified by pattern only.
- Dark mode removed so the page is always white paper with black ink.
- Structure now follows the PDF: cover, calendar, the four legs, then the days, swaps and checklist. The separate coloured chapter openers are gone.
- Checklist items carry the leg name, as in the PDF.
- Swaps box is a plain black frame instead of a grey panel.

PDF
- No layout or content change. Version stamp only.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.1.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.1-source.zip

## V1.0 (5 October 2026). Steady state

First locked version. Combines the four source itineraries (Shibuya, Kyoto, Hibiya and Ginza, Hong Kong) into one online page and one 18 page A4 PDF.

Content
- Wed 21, Sat 24 and Tue 27 each written once, joining the source documents.
- Sat 24 Tokyo sunset corrected to 16:55.
- Nozomi 16 seats (Car 9, 1-C and 1-D) carried into Sat 24.
- Hong Kong times converted to 24 hour.
- One merged checklist: before you fly, once you have seen the Hong Kong forecast, on the ground.

Design
- Booked or fixed: bold black with a solid Booked tag. To book: dashed tag. Targets: grey.
- Legs identified by pattern so it works on a black and white printer: Shibuya solid, Kyoto stripes, Hibiya grid, Hong Kong dots. Colour is online only.
- PDF: cover and calendar, a four legs page, one day per page, alternative plans in their own frames, swaps and checklist on the last page.
- Online: sticky day picker, tabs for Plan B and Thursday versions A, B, C, tickable checklist saved per device.

Files
- Japan-Hong-Kong-Final-Itinerary-v1.0.pdf
- Japan-Hong-Kong-Final-Itinerary-v1.0-source.zip (page, build script, template, fonts)

## 9 Oct 2026: J&HK Extras (separate app)
- New companion app, J&HK Extras ("Up our sleeve"): everything not in the day plans, by area, with place cards. Kept separate from the master for now; same source, same cards.
- Places scheduled in any master day plan drop off Extras automatically on build, and return if taken out.
- Shibuya built first: Must try strip, Eat (12), Drink (4), Views, Shopping, Further out, Massage. 30 items, 22 new cards. Backup plan places included as plain options; the backup plan itself stays separate.
- Area chips jump to each area and highlight as you scroll. Each area links back to its days in the itinerary.
- Own icon (black card slipping into a sleeve, "Extras", leg band). Home-screen name "J&HK Extras".
