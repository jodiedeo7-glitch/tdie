# The Weekend Ecosystem™ · cover, carousel, OG and Meta ad creatives

Cloud Credit Job 10, 27 September 2026. The Weekend Ecosystem™ is $97 one-time, or 3 × $33.33 (canon.json).
Everything is composed in code (`render.mjs`, HTML to PNG, Newsreader SemiBold + Inter pulled from raw.githubusercontent.com/google/fonts) over photos already in the repo. No new photo was generated here. One new photo is prompted in `PHOTO_PROMPTS.md`.

Re-render everything: `node ops/cloud-output/we-creatives/render.mjs` from the repo root (Node 22 + Playwright). Re-render some: add a name fragment, e.g. `ad-payplan`.

## 1 · Audit of the current Beacons cover

From the description in the job (Jodie's screenshot is not in the repo, so this is unverified against the image itself): big condensed pink sans headline "The Weekend Ecosystem™", subline "Your website + blog, built from what you already have", "XOXO, Jodie" in script, Tommy Kate on a sofa with a laptop and her tumbler.

**Keep**
- The product name as the headline. People buying on Beacons need to see the name first.
- The subline, word for word. It is the clearest one-line promise we have.
- The sign-off, as "xoxo, Jodie" (her email sign-off, lower case).
- Tommy Kate with a laptop and her glitter tumbler: her world, her prop.

**Change**
- Headline type: condensed pink sans breaks the type rule. Now Newsreader SemiBold in near-black, with "Ecosystem™" as the turn word in hot pink.
- All-pink headline reads as a pink wash. Now ink with one pink turn.
- Script sign-off: moved to Newsreader SemiBold in hot pink, small, so no thin or script face carries any words.
- No depth: now a cream gradient scrim from the left into a sharp full-height photo, a frosted glass price card with a thin gold edge and pink-tinted shadow, and two tilted sticker badges ("No code no camera", "Every update free") kept off her body.
- No price or callout on the cover: the frosted card now carries "$97 one-time · or 3 × $33.33" and "Every future update, free."
- Photo: the sofa photo (`hook-blog-posts.jpg`) has lettering baked into its top quarter. It is now used only as a clean crop (`photos/sofa-tumbler-no-lettering.jpg`, top 568 px removed), on the review card, so the hero gets a different photo.

## 2 · Files (`png/`)

| File | Size | Photo |
|---|---|---|
| beacons-1-hero.png | 1080 × 1080 | attic loft, cross-legged (`cover-kitchen.jpg`) |
| beacons-2-what-you-get.png | 1080 × 1080 | attic loft, typing at the desk (`hub-header.jpg`) |
| beacons-3-review.png | 1080 × 1080 | living room floor, glitter tumbler (clean sofa crop) |
| beacons-hero-keep-it-running-kit.png | 1080 × 1080 | as the hero, with the Kit card: free until 4 Oct, 11:59 pm Eastern. Swap back to beacons-1-hero on 5 Oct |
| og-weekend-ecosystem-preview.png | 1200 × 630 | preview-hero + hub-header, preview page link image. Live copy: `public/og/weekend-ecosystem-preview.jpg` |
| og-weekend-ecosystem-2026-09.png | 1200 × 630 | porch + loft. Every word sits inside the centre 600 px. Live copy: `public/og/weekend-ecosystem-2026-09.jpg` |
| ad-ideal-* | 4 sizes | porch at sunrise (`cover-sofa.jpg`) |
| ad-preview-* | 4 sizes | loft, facing camera (`preview-hero.jpg`) |
| ad-build-* | 4 sizes | loft, laptop on lap (`preview-working.jpg`); story and 1200 × 628 use `hub-header.jpg` |
| ad-payplan-* | 4 sizes | PLACEHOLDER until `photos/pay-plan-pasture-blanket.jpg` exists |
| ad-review-* | 4 sizes | living room floor, glitter tumbler (clean sofa crop) |

Ad sizes: 1080 × 1080, 1080 × 1350, 1080 × 1920 (copy kept between y 250 and 1580 for the Stories safe area), 1200 × 628. Copy for every ad: `AD_COPY.md`. Contact sheet: `CONTACT_SHEET.jpg`.

## 2b · Final design pass (27 Sep 2026)

Brief from Jodie: branded, premium, trustworthy, never a random scam ad. What changed across all 25:
- **No sticker stamps on any ad or on the OG.** Round "FREE / NO CODE" stamps read as a cold-feed offer. One sticker stays on the Beacons hero and one on the Kit hero.
- **The web address on every image** (`thedigitalincomeedit.com`) above a thin gold rule, with one true line beside it (e.g. "Every future update, free", "Both options at checkout", "Posted on Skool under her name"). A visible domain is the biggest single trust signal on a paid ad.
- **Calm cream background.** The pink glows are gone; pink now lives only in the turn words, the one hero card and the button.
- **Clean photo edges.** The photo is a crisp panel with a gold seam and a soft shadow instead of fading into pink.
- **Bigger, better-spaced type.** Square headlines 58→64 px, 4:5 62→70 px, landscape 46→50 px. Copy is centred in its column with brand at the top and the address at the foot.
- **Stories rebuilt.** Full-bleed photo with her face in the top half and all copy on one frosted card between y 250 and 1580.
- Toy check redone on every crop after the changes (the build ads were tightened to drop a Kuromi ear).

## 3 · Things to know

- **Third-party toys.** Several loft photos have Hello Kitty and Kuromi plush toys in them (Sanrio characters). Every crop in this set was placed to keep them out, and the story crops were zoomed for it. Guardrail: no third-party IP. The same photos are live on the sales and preview pages, which this job did not change.
- **Tumbler rule.** The older loft and porch photos show the Player Two? mug, not the glitter tumbler; they predate the 26 Sep rule. The review images and the new pasture photo carry the tumbler.
- **Preview page (fixed 27 Sep 2026).** New link preview `public/og/weekend-ecosystem-preview.jpg` (rendered here as `og-weekend-ecosystem-preview.png`). `preview-hero.jpg` cropped to take the toys out; the closing image temporarily shows the porch photo. Two replacement photos are prompted in `PHOTO_PROMPTS.md`, with the paste-ready finish instruction.
- **Tina's review** is the approved `pull` cut from `src/we-reviews.js`, verbatim, "word press" spelling kept.
