# Japan & Hong Kong trip, 16 to 31 October 2026

Four home-screen web apps, published with GitHub Pages:

- Itinerary: https://thestartupstudiodeveloper.github.io/japan-trip/
- Trip Weather: https://thestartupstudiodeveloper.github.io/japan-trip/weather/
- Trip Expenses: https://thestartupstudiodeveloper.github.io/japan-trip/expenses/
- J&HK Extras: https://thestartupstudiodeveloper.github.io/japan-trip/extras/

The same pages are also published on claude.ai. Every update goes to both.

## Layout
- `index.html`, `manifest.webmanifest`, `sw.js`, `icon-*.png`: the itinerary web app (built, do not edit by hand).
- `weather/`: the Trip Weather web app (built, do not edit by hand).
- `source/itinerary/`: the itinerary source. `python3 build.py && python3 shot.py` builds the online page and the PDF from the same data; `python3 site.py <repo dir>` writes the web app copy.
- `expenses/`: the Trip Expenses web app (built, do not edit by hand).
- `source/expenses/`: `expenses_build.py` builds the expenses page from `source/itinerary/expenses.json`; run it from a folder laid out like `source/itinerary` with the script in an `expenses/` subfolder. `trip-expenses.html` is the claude.ai copy.
- `extras/`: the J&HK Extras web app, the up our sleeve list of things not in the day plans (built, do not edit by hand).
- `source/extras/`: `extras.json` holds the areas, items and Extras-only place cards; `extras_build.py` builds the page and web app, reading the itinerary build for styles and cards and dropping any place already scheduled in a day plan. Run it from an `extras/` subfolder of a folder laid out like `source/itinerary`. `jhk-extras.html` is the claude.ai copy.
- `source/weather/`: `weather.html` is the Trip Weather page as published on claude.ai; `python3 weather_site.py weather.html <repo dir>` writes `weather/`.

## Rules carried over
Australian spelling, no em dashes or double hyphens in copy, black and white with leg patterns, changes recorded in `source/itinerary/CHANGELOG.md`.

## Saved versions (steady states)
- Live apps always show the latest. Frozen copies live at https://thestartupstudiodeveloper.github.io/japan-trip/archive/ with a date-stamped folder per version, e.g. `archive/ss1-2026-10-10/itinerary/`.
- To save one: `python3 source/snapshot.py "note"`, commit and push. Then put that commit's short ID into `archive/versions.json` as `commit`, run `python3 source/snapshot.py --index`, commit and push. Copies have no service worker or Save offline, and carry a banner linking back to the live app.
- The recorded commit is the restore point for the full source at that moment (git tags are blocked through this connection).

