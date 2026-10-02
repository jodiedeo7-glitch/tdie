# TDIE PINTEREST PIN RULES (copy for cloud sessions)

> **📌 PINTEREST GOES THROUGH METRICOOL (Jodie, 2 October 2026, standing rule, overrides every Pinterest-browser step below).** Never schedule, edit or delete a pin in the Pinterest browser. Schedule each pin with the Metricool connector: `createScheduledPost` on blogId 7142540, `providers: [{"network":"pinterest"}]`, `publicationDate` in America/New_York, `autoPublish: true`, `text` = the pin description, `mediaAltText` = the alt text, and `pinterestData: {boardId, pinTitle, pinLink, pinNewFormat:false}`. `boardId`: pass the exact board name (Metricool resolves it) or the numeric ID. Metricool needs a PUBLIC image URL: commit the PNG to the repo folder `pins-public/` and use `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/pins-public/<file>.png`. Before scheduling, run `getScheduledPosts` for the date range and skip any pin already there (no duplicates). Verify by reading the post back with `getScheduledPosts`, not by opening Pinterest. Pulls: `updateScheduledPost` with `draft:true`. Boards that exist: Beginner Online Business Ideas, Faceless Digital Marketing for Beginners, Passive Income Ideas for Beginners, Faceless Content Ideas, Legally Blonde Outfits | Pink Amazon Fashion, Pink Home, Dorm and Car Finds | Amazon, TK Outfits. The Pinterest browser is only for reading a public board check if Metricool cannot.


Rules from the project doc `claude/TDIE_PIN_FACTORY.md` (21 Sep 2026) and canon.json `pin_render`, placed here 26 Sep 2026. The rendering code in the project doc uses Fraunces and Cormorant Garamond, which Jodie has since rejected (see `TDIE_DESIGN_RULES.md`); any renderer built from this must use Newsreader SemiBold/Bold for headlines and Inter for everything else. Brown (#2B161B) is never a fill or background; use near-black #1A1417 for text and hot pink for dark areas.

## Rules that never move
- Destination for EVERY TDIE pin: `https://www.skool.com/thedigitalincomeedit/about` (founder instruction 21 Sep 2026, "that's how it tracks"). The owned domain and links.* (Beacons) are blocked on Pinterest.
- Copy limits: overlay 3 to 5 words · title 60 to 100 characters · description 450 to 500 · alt text 150 to 200 · no prices on pins · max 3 accents · lockup on every TDIE pin: `THE DIGITAL INCOME EDIT™` over `www.thedigitalincomeedit.com`. "Make Money Online" never in copy (spam-flagged).
- Canvas 1000 × 1500 (2:3), rendered at 2× and downsampled. 10 layouts per 10-pin batch, no layout twice, collage max 2: editorial-cover, hot-pink-block, left-rail, number-lead, quote-card, split-horizon, lower-third, stacked-panels, torn-paper, collage. Persona layouts: split-horizon, lower-third.
- AI-generated label ON. No income claims on pins.
- Cadence: 5 a day at 08:00, 11:00, 14:00, 17:00, 20:00 ET, boards rotating so no board takes two in a row. Close cousins (same post, lesson, freebie or topic) at least 3 days apart. The Legally Blonde Amazon line owns other slots.
- Boards in rotation: Pinterest Marketing for Beginners · Build a Business That Runs Without You · Content That Converts | Faceless Content Ideas · Make Money Online for Beginners (board name is Jodie's call) · The CEO Mindset | Money Mindset for Women.
- First run of anything new: Jodie sees a contact sheet before scheduling.

## What won the research (her Pinterest, 21 Sep 2026)
Top-ranked pins in the niche are content-dense reference cards: numbered phase lists with day ranges, checkbox rows with one box ticked, real list items on the pin, product-mockup shots of the actual PDF, and light airy lifestyle photography. Pretty-but-thin headline pins don't rank. About a third of a batch saturated scroll-stoppers (hot pink block, bubblegum panels), the rest light. List numerals set in Inter.

## Material sources
Skool community posts and the Daily Free Prompt · classroom module and lesson names · freebie PDFs and their step content · membership plan copy · pillar topics · the /learn articles.

## Rendering in a cloud container
`pip install weasyprint fonttools pdf2image --break-system-packages`. Fonts download from `https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/` and `.../ofl/inter/` (fonts.googleapis.com is blocked from the container). Render each pin as HTML → PDF → PNG at 1000 × 1500, add light grain. The persona seed is `public/images/library/avatar-seed-omni-reference.png`; persona photos can't be generated in the cloud, so persona layouts get a placeholder and a full image prompt for the finish queue.

## Scheduling (desktop only)
`https://www.pinterest.com/pin-creation-tool/`, a FRESH TAB for every pin, closed after. (SUPERSEDED 2 Oct 2026: use Metricool, see top.) Upload PNG, fill title, description, alt text, link (the /about URL), board, "Publish at a later date", then verify the count on the scheduled-pins page before reporting.
