# Japan & Hong Kong trip, 16 to 31 October 2026

Two home-screen web apps, published with GitHub Pages:

- Itinerary: https://thestartupstudiodeveloper.github.io/japan-trip/
- Trip Weather: https://thestartupstudiodeveloper.github.io/japan-trip/weather/

The same pages are also published on claude.ai. Every update goes to both.

## Layout
- `index.html`, `manifest.webmanifest`, `sw.js`, `icon-*.png`: the itinerary web app (built, do not edit by hand).
- `weather/`: the Trip Weather web app (built, do not edit by hand).
- `source/itinerary/`: the itinerary source. `python3 build.py && python3 shot.py` builds the online page and the PDF from the same data; `python3 site.py <repo dir>` writes the web app copy.
- `source/weather/`: `weather.html` is the Trip Weather page as published on claude.ai; `python3 weather_site.py weather.html <repo dir>` writes `weather/`.

## Rules carried over
Australian spelling, no em dashes or double hyphens in copy, black and white with leg patterns, changes recorded in `source/itinerary/CHANGELOG.md`.
