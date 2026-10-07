# DESKTOP FINISH QUEUE

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.


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


## 4 · WYS

The old launch and generation finish instructions were removed. Read `claude/WYS_REFERENCE_PACK_2026-10-07.md` for the current complete workflow. Generation is paused and the customer release hold remains active.
