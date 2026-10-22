> **PIN HEADLINE AND DESIGN STANDARD (Jodie, 22 October 2026). This wins over every older line in this file, in the job files, in the weekly pin factory prompt and in canon `pin_render` where they differ.** The batches made 12 to 27 October failed: headlines were verb-fragment lesson names ("Give Your Bio Direction", "Keep Your Groups Useful", "Cut The Extra Promises"), step cards were too small to read, a sticker said "03 USEFUL STEPS", photos did not match the topic (a dog under a table on a bio pin), and nothing said what TDIE or Skool is. Her words: "What are they advertising? Would you click?"
>
> 1. **Headline = a specific promise a stranger understands in one second.** 6 to 10 words. It names who it is for or what it is about AND what they get. Good: "How To Pick A Niche For Your Digital Products". Bad: "Narrow The Reader First". Test every headline: if a woman who has never heard of TDIE, Skool or the lesson cannot say what the pin is about, rewrite it.
> 2. **Big type.** Headline at least 100px on the 1000px canvas, 4 lines at most, readable when the pin is 200px wide. No text on the pin under 28px except the lockup line.
> 3. **No tiny step cards.** Either a real numbered list of specific items at 40px or larger, or no list. Delete the "03 USEFUL STEPS" sticker, "Save the check", "Keep this beside your next draft" and every generic filler line.
> 4. **One photo that matches the topic**, framed in its own shape (portrait photo, portrait frame). No unrelated stock.
> 5. **CTA button text: "Learn more on Skool".** Never "free", "free trial", a price or an income claim.
> 6. **Brand name big.** THE DIGITAL INCOME EDIT\u2122 lockup readable at stamp size.
> 7. **No pink boxes, pills, circles or buttons** (see CLAUDE.md). Pink is type, thin rules and photography.
> 8. **Fonts: Gloock headlines, Yellowtail for the one stressed word, Jost for everything else.** Newsreader and Inter are retired for pins.
> 9. **Research first.** Before any batch, search what is currently performing for the niche (TinyFish search, Pinterest Trends language) and use the phrases people actually search in the headline, title, description and alt text.
> 10. **Look before scheduling.** Render every pin, open each at full size and at 200px wide, fix every defect, then show Jodie a contact sheet before anything is scheduled.

> **Current core Pinterest reconciliation (4 October 2026):** Read `ops/ai-router/CORE_PINTEREST_RECONCILIATION_2026-10-04.md` first. It supersedes conflicting legacy browser, ownership-fallback, missing-source and vocabulary instructions below. This repository edit does not change live tasks or prove a publishing cutover.

# TDIE PINTEREST PIN RULES (copy for cloud sessions)

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.


> **📌 PINTEREST GOES THROUGH METRICOOL (Jodie, 2 October 2026, standing rule, overrides every Pinterest-browser step below).** Never schedule, edit or delete a pin in the Pinterest browser. Schedule each pin with the Metricool connector: `createScheduledPost` on blogId 7142540, `providers: [{"network":"pinterest"}]`, `publicationDate` in America/New_York, `autoPublish: true`, `text` = the pin description, `mediaAltText` = the alt text, and `pinterestData: {boardId, pinTitle, pinLink, pinNewFormat:false}`. `boardId`: pass the exact board name (Metricool resolves it) or the numeric ID. Metricool needs a PUBLIC image URL: commit the PNG to the repo folder `pins-public/` and use `https://raw.githubusercontent.com/jodiedeo7-glitch/tdie/main/pins-public/<file>.png`. Before scheduling, run `getScheduledPosts` for the date range and skip any pin already there (no duplicates). Verify by reading the post back with `getScheduledPosts`, not by opening Pinterest. Pulls: `updateScheduledPost` with `draft:true`. Boards that exist: Beginner Online Business Ideas, Faceless Digital Marketing for Beginners, Passive Income Ideas for Beginners, Faceless Content Ideas, Legally Blonde Outfits | Pink Amazon Fashion, Pink Home, Dorm and Car Finds | Amazon, TK Outfits. The Pinterest browser is only for reading a public board check if Metricool cannot.


Rules from the project doc `claude/TDIE_PIN_FACTORY.md` (21 Sep 2026) and canon.json `pin_render`, placed here 26 Sep 2026. The rendering code in the project doc uses Fraunces and Cormorant Garamond, which Jodie has since rejected (see `TDIE_DESIGN_RULES.md`); any renderer built from this must use Gloock for headlines, Yellowtail for the one stressed word and Jost for everything else (Jodie, Oct 2026; Newsreader and Inter are retired for pins). Brown (#2B161B) is never a fill or background; use near-black #1A1417 for text and hot pink for dark areas.

## Rules that never move
- Destination for EVERY TDIE pin: `https://www.skool.com/thedigitalincomeedit/about` (founder instruction 21 Sep 2026, "that's how it tracks"). The owned domain and links.* (Beacons) are blocked on Pinterest.
- Copy limits: overlay (headline) 6 to 10 words, specific, see the standard above · title 60 to 100 characters · description 450 to 500 · alt text 150 to 200 · no prices on pins · max 3 accents · lockup on every TDIE pin: `THE DIGITAL INCOME EDIT™` over `www.thedigitalincomeedit.com`. "Make Money Online" never in copy (spam-flagged).
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
