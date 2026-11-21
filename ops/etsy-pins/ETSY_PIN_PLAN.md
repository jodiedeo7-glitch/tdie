# Etsy to Pinterest plan (The Digital Income Edit Etsy shop)

Set up 21 Nov 2026 on Jodie's request: "make sure there's a regular Etsy Pinterest marketing plan." Etsy search sent her shop 1 visit in 30 days, so Pinterest is the main traffic engine for the Etsy shop.

## The rhythm
- 14 Etsy pins a week, 2 a day at 12:31 pm and 9:13 pm Eastern (these slots stay clear of the core TDIE pin slots at 8, 11, 2, 5 and 8 and the Legally Blonde line).
- 7 listings a week, 2 pins each: pin A = the listing's cover photo (photo 1), pin B = the listing's "What's inside" photo (photo 2). If a listing has been pinned before, use photos 3 to 8 in turn instead, but only photos with a cream or light background (her listing photos with a full flat hot pink background are never used on a pin).
- Never two pins from the same listing on the same day. The A and B pins of one listing are at least 3 days apart.
- Rotation: listings pinned least recently go first. Seasonal listings follow the season: Christmas and holiday items from 1 Nov to 20 Dec, New Year, goal, planner, budget, vision board and Word of the Year items from 15 Nov to 31 Jan, fall and Thanksgiving items from 1 Sep to 25 Nov, Halloween items from 15 Aug to 25 Oct. Off-season and inactive listings are skipped.
- Weekly run: inside the existing Etsy shop task ("Etsy shop: publish the queue, fix held listings, Monday shop check"), on its Friday 12:41 am run (overnight, so it never delays her daytime client tasks). It schedules the coming Saturday to Friday.

## Destinations
- pinLink = `https://www.etsy.com/listing/<listing id>` (no tracking parameters; Etsy stats already show Pinterest traffic).
- These are Etsy pins, not Skool pins: the Skool /about destination rule in TDIE_PIN_RULES.md is for TDIE community pins only.

## Boards (Metricool resolves names; IDs given where known)
- 2027 Planners, Journals and Printables (1122311238331441388): planners, journals, goal, budget, vision board, wellness, gratitude, Word of the Year.
- Beginner Online Business Ideas (1122311238330664773): business workbooks, launch planners, lead magnet, UGC, Etsy seller guides.
- Faceless Content Ideas (1122311238330664783): content calendars and social media planners.
- Pinterest Marketing workbooks: Faceless Digital Marketing for Beginners.
- Coloring books, kids activities, chore charts and party printables: "Printable Coloring Pages and Kids Activities". If that board does not exist yet, create it once (public) from a pinterest.com tab with the BoardResource create call (see the 21 Nov 2026 log entry), record its ID here, then schedule.

## The pin look (approved 21 Nov 2026)
Rendered by `ops/scripts/etsy_pin_render/render.py specs.json <outdir>` (fonts in the same folder). 1000 x 1500, cream paper, pink Montserrat kicker, Gilda Display headline with the turn phrase in glitter hot pink, the listing photo square in its own square frame with a Muted Gold hairline, a white "Shop it on Etsy" button with a pink arrow, and THE DIGITAL INCOME EDIT™ lockup. Example specs: `example_specs_2026-11-21.json`.
- No pink boxes, pills or buttons. No Gloock, Jost, Fraunces, Cormorant Garamond. No brown fills.
- Headline: 6 to 10 words, a specific promise a stranger gets in one second, built from what buyers type (Etsy search suggestions: `/suggestions_ajax.php?search_type=all&search_query=<term>` from an etsy.com tab). Mark 1 to 4 turn words with *asterisks*.
- Kicker: a short true fact (for example "53 printable pages" or "Printable budget planner").
- Copy limits: title 60 to 100 characters, description 450 to 500, alt text 150 to 200. No prices, no em dashes, no "free". Only facts from the listing itself. American English.
- isAiGenerated true, isAiGeneratedPerson false.

## Look before scheduling
Render, then open every pin at full size and a 200 px wide strip of the whole batch. Fix lone words on a line, text touching the photo frame, cut-off text and wrong photos, re-render, look again.

## Hosting and scheduling
Scheduled runs host each PNG on Google Drive (the same method the Facebook promo task uses): create_file in the TDIE Task Files folder (id 1aAqPKUW8-6kEyDLr1PuK2aHGpr225hJE), share_file anyoneWithLink reader, then `createScheduledPost` on Metricool blogId 7142540 with media `https://drive.google.com/file/d/<id>/view?usp=drivesdk` (autoPublish true, draft false). Metricool copies the image to static.metricool.com; once the read-back shows the static copy, trash the Drive file. (The 21 Nov 2026 batch was hosted in pins-public/ on GitHub instead.) Before scheduling, `getScheduledPosts` one day per call for the week and skip any slot already holding an Etsy pin (pinLink starts with https://www.etsy.com/listing/). After scheduling, read each day back.

## Log
History: `ops/etsy-pins/ETSY_PIN_LOG.md` (first batch) plus every Drive file in TDIE Task Files whose title contains "etsy-pin-log". Each run creates its own `etsy-pin-log-YYYY-MM-DD.md` in that Drive folder with: date, listings pinned (id, A/B photo used, slot), and the Etsy shop's Pinterest visits for the last 7 days from Stats.
