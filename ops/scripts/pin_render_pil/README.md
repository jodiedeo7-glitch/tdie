# Pin renderer (PIL), built 5 Nov 2026

Renders one 1000x1500 core pin to the 22 Oct 2026 standard: Gloock headline at 100px, one Yellowtail stressed word, Jost 40px teaching rows, one library photo, gold hairlines, no pink fills, CTA "Learn more on Skool", lockup.

Setup (cloud container):
mkdir -p /tmp/pinfonts && cd /tmp/pinfonts
curl -sSLO https://raw.githubusercontent.com/google/fonts/main/ofl/gloock/Gloock-Regular.ttf
curl -sSLO https://raw.githubusercontent.com/google/fonts/main/apache/yellowtail/Yellowtail-Regular.ttf
curl -sSL -o "Jost[wght].ttf" "https://raw.githubusercontent.com/google/fonts/main/ofl/jost/Jost%5Bwght%5D.ttf"

Use: see pins_example_2026-11-06.py for the pin dict (id, kicker, photo from public/images/library, focus, headline with | for line breaks, stress word, rows, take). Call render.render(pin, out_png). Keep photo_h (printed) at 180 or more, no headline overflow warning, no single word alone on a line. Open every PNG at full size before scheduling.
