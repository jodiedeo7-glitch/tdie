# DESKTOP FINISH QUEUE

Account-only steps left by cloud sessions. Each job adds one numbered section with every file path, piece of copy and exact step written in. The DESKTOP FINISH prompt in `ops/cloud-kit/CLOUD_CREDIT_JOBS.md` works through this file on Jodie's computer and marks each section DONE with the date.

## 1 · One-Sentence Offer tool: link from The Offer Edit's opening lesson (26 Sep 2026)

Cloud session could not reach Skool (network policy blocks skool.com; no signed-in browser). Canon Decision 120.

1. Open https://www.skool.com/thedigitalincomeedit/classroom/c47c7df7 signed in as Jodie. Open the first lesson of The Offer Edit.
2. Edit the lesson. At the very end of the body, add this one line as its own paragraph:

   Want to test your sentence before you build the rest? Run it through the free One-Sentence Offer tool. Two minutes, no email.

3. Select the words **the free One-Sentence Offer tool** and hyperlink them to `https://www.thedigitalincomeedit.com/resources/one-sentence-offer`. No raw URL in the text.
4. Save. Reload the lesson and read the line back from the page: the wording matches step 2 exactly and the link opens the tool.
5. Mark this section DONE with the date.

## 2 · The Weekend Ecosystem™ Beacons description (revised 26 Sep 2026)

Jodie is pasting the revised description herself (sent in chat 26 Sep 2026). Remaining step only: on Mon 5 Oct 2026, after the Keep It Running Kit ends (4 Oct, 11:59 pm Eastern), replace the description with the "after 4 Oct" version saved in `ops/cloud-output/WE_BEACONS_DESCRIPTION.md`, then read it back from the public checkout page.

## 3 · The Weekend Ecosystem™ cover, carousel, OG and Meta ads (Job 10, 27 Sep 2026)

All files are in `ops/cloud-output/we-creatives/` (see its `README.md`, `AD_COPY.md`, `PHOTO_PROMPTS.md`, `CONTACT_SHEET.jpg`). The cloud session could not use Gemini, Higgsfield, Beacons or Meta.

1. **Generate the one placeholder photo.** Open Google Gemini, attach `public/images/library/avatar-seed-omni-reference.png`, paste the full prompt under "pay-plan-pasture-blanket.jpg" in `ops/cloud-output/we-creatives/PHOTO_PROMPTS.md`. If Gemini has no credits or the face drifts, use Nano Banana Pro at 2K on Higgsfield with the same reference. Check: her glitter pink tumbler with lavender straw is in frame, no text in the image, she sits in the right third. Save it as `ops/cloud-output/we-creatives/photos/pay-plan-pasture-blanket.jpg`. From the repo root run `node ops/cloud-output/we-creatives/render.mjs ad-payplan`, open the four `png/ad-payplan-*.png` files and confirm the placeholder box is gone, then commit and push.
2. **Beacons carousel.** Open the Beacons product for The Weekend Ecosystem™ (checkout `https://links.thedigitalincomeedit.com/shop/f7b54195-6a0e-4e95-8b92-fc203770176c`) in the Beacons editor. Replace the product images with, in this order:
   1. `ops/cloud-output/we-creatives/png/beacons-hero-keep-it-running-kit.png` (while the Kit runs, until Sun 4 Oct 2026, 11:59 pm Eastern)
   2. `ops/cloud-output/we-creatives/png/beacons-2-what-you-get.png`
   3. `ops/cloud-output/we-creatives/png/beacons-3-review.png`
   Save. Open the public checkout page and read the carousel back: three images, in that order.
3. **On Mon 5 Oct 2026** (after the Kit ends), swap image 1 for `ops/cloud-output/we-creatives/png/beacons-1-hero.png`. Read it back from the public page. (Same day as section 2's description swap.)
4. **Facebook Sharing Debugger.** Go to https://developers.facebook.com/tools/debug/, enter `https://www.thedigitalincomeedit.com/shop/weekend-ecosystem`, click **Scrape Again**. Confirm the preview image is the new one (`/og/weekend-ecosystem-2026-09.jpg`: porch photo left, loft photo right, "A business that keeps selling on the Tuesday you're too tired to post." in the centre card).
5. **Meta Ads Manager: only with Jodie's go.** Ask Jodie first. When she says go: five ads, one per angle in `AD_COPY.md` (ideal, preview, build, payplan once step 1 is done, review). Each ad: upload its four `png/ad-[angle]-*.png` sizes as placement assets (1080 × 1080 and 1080 × 1350 for feeds, 1080 × 1920 for Stories and Reels, 1200 × 628 for right column), paste Primary text, Headline and Description from `AD_COPY.md` exactly, CTA button **Learn More**, website URL `https://www.thedigitalincomeedit.com/weekend-ecosystem/preview`. No link in any caption. Budget, audience and schedule are Jodie's call. Leave the ads paused until she approves the preview.
6. Mark this section DONE with the date.

## 4 · DROPSHIP (do not run until Jodie approves the bank and picks a platform) (Job D1, 27 Sep 2026)

Files: `ops/cloud-output/dropship/PRODUCT_BANK.xlsx` (sheets Candidates, Suppliers, Margins, Bank40, OrderByDates), `ops/cloud-output/dropship/REPORT.md`, `ops/cloud-output/dropship/looks/` (7 look drafts). The cloud session could not open any supplier site (network policy), so every cost, shipping quote and stock figure in the workbook is an estimate from search snippets and is labelled so. Two steps only, nothing else:

1. **Confirm every winner supplier listing, signed in.** Open cjdropshipping.com signed in as Jodie, turn on the US Warehouse filter, and for each of the 40 rows on the Suppliers sheet (rank "winner") search the exact term in column R ("Search '...'"), open the best matching listing, and read back into the sheet: the listing URL (column E), product cost (F), shipping to ZIP 31808 Fortson GA (G) and to ZIP 90210 Beverly Hills CA (H) using CJ's shipping calculator on the listing, quoted days to each (I, J), the warehouse shown (L), MOQ (M), packaging (N), the return terms (O), and set column Q "Verified?" to "confirmed on cjdropshipping.com [date]". If the US warehouse has no stock of an item, do the same on app.zendrop.com with Ships From: US (the "backup" row), and if neither US option has it, mark the row "no US stock" and leave it; do not substitute a China-shipped listing for a Q4 product. When a confirmed cost or shipping figure differs from the estimate, type it into the blue cells on the Margins sheet (columns E and F) and read the Passes floors? column (T) and Band OK? column (W) back: any row that turns KILL or OUT OF BAND is reported to Jodie in one line, not fixed by raising the price above the band.
2. **Order one sample of the top 5 to Fortson.** After step 1, place a single sample order of each of these five to Jodie's Fortson, GA address through the confirmed winner listing (CJ or Zendrop), paid with her card, and note the order numbers and the promised delivery dates in the sheet's Notes column:
   1. Q11 Pink 40 oz insulated tumbler with handle and straw: CJ search "40oz tumbler with handle" (https://cjdropshipping.com/search/40oz+tumbler+with+handle.html)
   2. E01 Pink PU leather desk mat, large: CJ search "desk mat pu leather pink large waterproof"
   3. E08 Fluffy pink steering wheel cover, universal 15 inch: CJ search "fluffy steering wheel cover pink plush" (AliExpress reference only: https://www.aliexpress.com/item/1005005267863833.html)
   4. Q14 Pink satin sleep bonnet, adjustable: CJ listing https://cjdropshipping.com/product/new-silk-bonnet-for-sleeping-women-satin-bonnet-hair-bonnet-night-sleep-cap-scarf-wrap-for-curly-hair-with-tie-band-for-curly-hair-p-2407140638471615000.html (confirm the US warehouse holds the pink)
   5. Q06 Pink velvet Christmas tree bows, 24 pack: CJ search "velvet christmas bows pink wired 24"
   When the samples arrive, photograph each on the cream surface described in its image alt text in the look's `.copy.md`, and note the real delivery days against the quote. Nothing else in this section: no store, no imports, no pins, no emails until D2.
3. Mark this section DONE with the date.
