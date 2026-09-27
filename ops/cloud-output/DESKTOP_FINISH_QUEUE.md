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

## 4 · The While-You-Sleep Storefront™: launch and own-setup fixes (27 Sep 2026)

Everything is in `ops/cloud-output/storefront-product/` (start with its `README.md`). The sales page is on the branch `storefront-launch` (`src/pages/shop/while-you-sleep-storefront.astro`). The cloud session could not reach Skool, Beacons, Amazon, Pinterest, MailerLite, Facebook, Threads, Gemini or Higgsfield. Publish nothing and list nothing outside these steps. Work the steps in order; each ends with a read-back. Files named below are repo paths.

Three link tokens are used across the copy and are replaced in step 4 and step 7: `BEACONS_PRODUCT_URL` (the public Beacons product), `MEMBER_PRODUCT_URL` (the private $17 product), `VALUE_VAULT_LESSON_URL` (the new Value Vault lesson). The sales page address, `https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront`, is already written in.

### Step 1 · Brand Closet™ referral check

1. In Jodie's Chrome, open https://www.skool.com/the-brand-closet (signed in as Jodie).
2. Click the group name at the top left to open the group menu. Look for an affiliate option (Skool labels it "Affiliates"). Also check the group's About page and settings menu for "Invite", "Refer" or "Earn" with a personal link.
3. If a member-level personal referral link exists: the answer is YES. Note the exact menu path you used.
   - Open `ops/cloud-output/storefront-product/kit/05_RECOMMEND_IT_TOO.txt`. Delete the `[KIT BUILD NOTE ...]` paragraph and everything from the line `VERSION B (no member referral link)` to the end of the file, and delete the line `VERSION A (members get their own referral link)` with the `====` lines around it.
   - If the menu path you used differs from "Click the group name at the top left to open the group menu, and choose the affiliate option (on Skool it's labelled Affiliates)", replace that sentence in step 2 of FIND YOUR LINK with the exact path you used.
4. If none exists: the answer is NO.
   - In the same file, delete the `[KIT BUILD NOTE ...]` paragraph and everything from the line `VERSION A (members get their own referral link)` down to (not including) the `====` line above `VERSION B (no member referral link)`, and delete the line `VERSION B (no member referral link)` with the `====` lines around it.
5. Record the answer: add one line under the heading "Recommend it too" in `ops/cloud-output/storefront-product/README.md`: `Referral check [date]: YES (kept Version A, path: [menu path])` or `Referral check [date]: NO (kept Version B)`.
6. Read `05_RECOMMEND_IT_TOO.txt` back: one version only, no build note, no em dashes.

### Step 2 · Images

1. Open `ops/cloud-output/storefront-product/IMAGE_PROMPTS.md`. For each of the five photos, in its table order:
   - Tommy Kate photos (`cover-sofa-dusk.jpg`, `g1-porch-morning.jpg`, `g3-kitchen-late.jpg`): Google Gemini, attach `public/images/library/avatar-seed-omni-reference.png`, paste the full prompt. If Gemini has no credits or the face drifts, Nano Banana Pro at 2K on Higgsfield with the same reference.
   - Person-free photos (`g2-loft-night-desk.jpg`, `g4-nightstand-phone.jpg`): Seedream 4.5 on Higgsfield, Unlimited switch on, paste the full prompt.
   - Check each at feed size: face and hands natural, her glitter pink tumbler with lavender straw in every frame with her, exactly one candy-pink object in the person-free frames (headphones in g2, tumbler in g4), no lettering or logos anywhere, subject on the side the prompt names. Two correction rounds at most; garbled results re-run on Nano Banana Pro at 2K.
   - Save as `ops/cloud-output/storefront-product/graphics/photos/<file name>` (no downloads folder: use the capture method in `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` section 3c).
2. The hoodie flat lay for the Setup Guide, worked example 2: take Jodie's OWN generated flat lay for the pink color-block hoodie outfit (the Seedream image logged in `claude/BRAND_CLOSET_PIN_LOG.md`, hoodie row), never Rose's image. Capture it at 1000 × 1500 and save it as `ops/cloud-output/storefront-product/graphics/photos/hoodie-flatlay.jpg`.
3. From the repo root run `node ops/cloud-output/storefront-product/render.mjs` (add `LAUNCH="<launch weekday day month 2026>"` in front if step 3 moved the launch). Open `ops/cloud-output/storefront-product/tests/thumbnails/contact-sheet.png` and every file in `ops/cloud-output/storefront-product/graphics/*.png`: no placeholder box left, every word crisp at thumbnail size.
4. Rebuild the kit zip from the repo root: `cd ops/cloud-output/storefront-product && rm -f While-You-Sleep-Storefront-Kit.zip && zip -j While-You-Sleep-Storefront-Kit.zip kit/*.txt kit/While-You-Sleep-Storefront-Setup-Guide.pdf && cd -`
5. Commit and push (`git add ops/cloud-output/storefront-product && git commit -m "Storefront kit: photos, final PDFs and zip" && git push`).

### Step 3 · Dates

Use the first table if this finish runs on or before Wed 30 Sep 2026. The Premium flash sale runs until 11:59 pm Eastern, Wed 30 Sep 2026, and no launch date may fall inside it, so the tease moves to the first morning after it.

| What | When (Eastern) |
|---|---|
| Tease (Skool 1) | Thu 1 Oct 2026, 9:00 am |
| Presale opens (Skool 2) | Thu 1 Oct 2026, 12:05 pm |
| Presale closes | Sun 4 Oct 2026, 11:59 pm |
| Public $27 and member prices | Mon 5 Oct 2026, 9:00 am |
| Every other piece | as dated in `ops/cloud-output/storefront-product/COPY.md` (default date table) |

If this finish runs on Thu 1 Oct 2026 or later, call the finish day D:
- Tease on D at 9:00 am (or, if D's 9:00 am has passed, D at the next full hour). Presale opens D+3 at 12:05 pm and closes D+6 at 11:59 pm. Public and member prices at 9:00 am on D+7.
- Shift every date in COPY.md's default date table by the same number of days (N = days from Thu 1 Oct to D+3), keeping each time. In COPY.md, the two Beacons descriptions and `src/pages/shop/while-you-sleep-storefront.astro` on `storefront-launch`, replace each weekday and date with its shifted one ("Sunday" becomes the weekday of D+6, "Thursday 1 October" the weekday and date of D+3, "Monday 5 October" the weekday and date of D+7). In the sales page also change `PRESALE_OPENS` to D+3 at 16:05Z and `PUBLIC_PRICE_AT` to D+7 at 13:00Z (both valid while US Eastern is on daylight time, until 1 Nov 2026; from 1 Nov use 17:05Z and 14:00Z).
- Threads: the Keep It Running Kit override ends Sun 4 Oct; on shifted dates, put the two product posts in the 5 PM slot of the presale's second day and of launch day.

Checks, whichever table:
1. No date falls on or before Wed 30 Sep 2026, 11:59 pm Eastern.
2. All-member Skool emails: open SkoolKit, list every scheduled or sent post with "Send email to all members" on from Wed 30 Sep 2026 onward (Blast 2 is Wed 30 Sep, 6:10 pm). Skool 4 (last call) is the only launch post that emails all members, and only if no other all-member email sits within 72 hours before or after it. If one does, leave the email off on Skool 4 too. No launch post turns the email on otherwise.
3. Brand Closet™ days: Skool 2 names The Brand Closet™ (no link). Open SkoolKit for that day; if any other affiliate post (Brand Closet™, AIM, Shopify, Upside, Skool platform referral, Earn With Skool) is scheduled the same day, move that affiliate post to the next day that has no affiliate post and no affiliate post the day before or after.
4. Spread rules: at most one selling post a day in the Skool feed outside this 4-day promo window, never in the 11:00 am teaching slot, never two selling posts back to back.

### Step 4 · Beacons

Log in to Beacons as Jodie. Create three things:

1. **The public product** (the presale, repriced at launch). Add a digital product. Title: `The While-You-Sleep Storefront™`. Price: $10. File: `ops/cloud-output/storefront-product/pdf/While-You-Sleep-Storefront-Presale.pdf` (the one-page "You're in" note). Description: COPY.md, "Public product", "Description (presale ...)" text, exactly. Product image: `ops/cloud-output/storefront-product/graphics/g4-share.png`. Visible on the storefront. Save. Copy its public address: this is `BEACONS_PRODUCT_URL`.
2. **The private member product.** Add a digital product. Title: `The While-You-Sleep Storefront™ · member price`. Price: $17. File: `ops/cloud-output/storefront-product/While-You-Sleep-Storefront-Kit.zip` (if Beacons refuses a zip, attach `kit/While-You-Sleep-Storefront-Setup-Guide.pdf` and every `kit/*.txt` file instead). Description: COPY.md, "Private member product" text. Set it hidden: never on the storefront and never in the link in bio. Save. Copy its address: this is `MEMBER_PRODUCT_URL`.
3. **The code.** Add a discount code `PREMIUM50`: 50% off, applies to the member product only, no expiry, no usage cap. Save. Open the member product's checkout, apply `PREMIUM50`, and read the total back as $8.50 (stop before paying).
4. Replace `BEACONS_PRODUCT_URL` and `MEMBER_PRODUCT_URL` with the two addresses everywhere in: `ops/cloud-output/storefront-product/COPY.md`, `ops/cloud-output/storefront-product/CANON_ROWS_DRAFT.md`, `ops/cloud-output/storefront-product/kit/11_WHATS_NEXT.txt`, and on the `storefront-launch` branch `src/pages/shop/while-you-sleep-storefront.astro` (the `CHECKOUT` constant). Search each file afterwards for the two tokens: zero left.
5. Rebuild the zip (step 2.4) because `11_WHATS_NEXT.txt` changed, and re-attach it to the member product.
6. Read back: open both product pages logged out. Public: $10, presale description, the product image. Member: not on the storefront, $17.

### Step 5 · Affiliate

1. In Beacons, open the public product's settings and turn on its affiliate program at 40% commission (Beacons' own affiliate product feature, the same mechanic as The Weekend Ecosystem™: one shared link, no application).
2. Read back: in a second browser profile or a test Beacons account, add a digital product, choose affiliate product, paste `BEACONS_PRODUCT_URL`, and confirm Beacons offers it at 40%. Delete the test product.

### Step 6 · Canon

On the same day, in both copies (the claude.ai Project's `canon.json` and `TDIE_CANON.md`, and the repo's `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md`):
1. Paste the four `canon.json` blocks from `ops/cloud-output/storefront-product/CANON_ROWS_DRAFT.md` (products[] row in price order after the $27 rows; `own_affiliate_programs.while_you_sleep_storefront`; `vault_disambiguation.standalone_member_pricing`; the `meta` decision). The decision number is the highest "Decision N" in `meta` plus one; the meta key's date is today as `YYYY_MM_DD`. Replace `VALUE_VAULT_LESSON_URL` in the row after step 7 on the same day.
2. Paste the `TDIE_CANON.md` paragraph into §5 PRODUCTS after The Keep It Running Kit paragraph, with the same decision number.
3. Validate the repo JSON: `python3 -c "import json;json.load(open('ops/canon/canon.json'))"`. Commit and push both repo files. Read the project copies back.

### Step 7 · Vault lessons

1. In Skool, classroom, **The Value Vault** course: add a lesson titled `The While-You-Sleep Storefront™ · member price`. Body: COPY.md, "THE VALUE VAULT LESSON" text. Every link sits on its words (the two `MEMBER_PRODUCT_URL` links, and "see Membership Premium" to https://www.skool.com/thedigitalincomeedit/plans). Leave it as a draft (unpublished). Copy its address: this is `VALUE_VAULT_LESSON_URL`.
2. **The Premium Vault** course: add a lesson titled `The While-You-Sleep Storefront™ · your half-price code`. Body: COPY.md, "THE PREMIUM VAULT LESSON" text, links on their words. Draft.
3. Replace `VALUE_VAULT_LESSON_URL` in COPY.md and CANON_ROWS_DRAFT.md (and the pasted canon row from step 6) with the address. Zero tokens left.
4. Read both drafts back from the server (Skool drops writes silently): body complete, no empty paragraphs, links on their words, `PREMIUM50` only in the Premium lesson. Both publish on launch morning (step 10).

### Step 8 · Sales page

1. On the `storefront-launch` branch, confirm the `CHECKOUT` constant in `src/pages/shop/while-you-sleep-storefront.astro` now holds `BEACONS_PRODUCT_URL`'s real address (step 4) and the dates match step 3.
2. `npm ci && npx astro build` must pass. Commit ("Sales page: checkout link and dates"), push `storefront-launch`, open a pull request into `main`, merge it (before the presale opens).
3. After Vercel deploys, open https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront logged out, on desktop and phone: the eight pin images load; before 12:05 pm on presale day the price box shows "The presale opens ..." with a closed button; the Tina Alexander line sits only in "The blog half" section; no earnings figures, no affiliate rate; the one checkout button opens the Beacons product once the presale is open.

### Step 9 · Scheduling

All copy is in `ops/cloud-output/storefront-product/COPY.md`, at the dates from step 3. Paste it exactly.
1. **Skool (SkoolKit):** schedule Skool 1 to 5 with their titles, bodies and images (Skool 1: `graphics/g2-tease.png`; Skool 2: `graphics/g1-presale-open.png`; Skool 3: the four `src/lifestyle/` images it names; Skool 4: `graphics/g3-last-call.png`; Skool 5: `graphics/g4-share.png`). Every link hyperlinked on its words, two per post. "Send email to all members" ON for Skool 4 only, per step 3 check 2. Read each back in SkoolKit.
2. **Email (MailerLite):** two regular campaigns (not automations), to all active subscribers. Subject, preview text and body from COPY.md, links on their words, signed "xoxo, Jodie", no Amazon links. Send a test to Jodie, then schedule. Read back: both show Scheduled at the right time.
3. **Facebook group:** schedule Facebook 1 and 2 with no link in the body and `graphics/g3-last-call.png` on Facebook 2 (Facebook 1: `graphics/g1-presale-open.png`). Set each first comment to post 5 minutes after the post; where the scheduler can't, put the comment up by hand 5 minutes after the post is live. Neither is done until its first-comment link is seen live.
4. **Threads:** add the five Threads posts to the Threads week files for the weeks they fall in, in the slots COPY.md names, with the pinned comments at 7:00 pm on the two product posts, so the nightly Threads load posts them. On the two product days they replace that day's table offer (The Operating Prompts™ on the Friday, AI Influencer Starter Twin on the Monday).

### Step 10 · Launch morning (Mon 5 Oct 2026, or D+7), 9:00 am Eastern

1. Beacons, public product: replace the file with `ops/cloud-output/storefront-product/While-You-Sleep-Storefront-Kit.zip` (or the PDF and .txt files, as in step 4.2), change the price to $27, and replace the description with COPY.md's "from Mon 5 Oct" version. Save.
2. Skool: publish both vault lessons from step 7.
3. Read back: public product shows $27 and the new description; downloading as a test buyer (or Beacons' file preview) serves the kit, not the presale note; the member product still $17 and hidden; `PREMIUM50` still gives $8.50; both lessons live (the Premium one visible only to Premium); the sales page price box shows $27.

### Step 11 · Own-setup fixes

Apply `ops/cloud-output/storefront-product/OWN_SETUP_AUDIT.md` in its order, to both recipes (`claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` and `claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md` in the project, plus the repo copy `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`) and to the scheduled tasks, using the exact text written there:
- 11a. Section 1: the TK Outfits board (rename, description, public, confirm the scheduled hoodie flat lay is on it), then the recipe and task lines.
- 11b. Section 2: the 14-day lesson window and past-due slot lines in the line 2 recipe.
- 11c. Section 3: the rewritten "Pinterest safety" bullet in both recipes. Apply for Standard access for "TDIE- Auto Pin" and record the demo video exactly as section 3 lists; check the two unverified points (API scheduling time, AI label) in Pinterest's own reference before switching anything.
- 11d. Section 4: create the one-off catch-up task with its exact prompt (it also clears the Brand Closet™ backlog from section 2).
- 11e. Section 5: the LEFTOVERS block in trig_015jA7LTzhHTH4cHKA6HuX5r, the leftovers line in both recipes, and the stories pause in section 8d.
- 11f. Section 6: delete trig_01F6oCmn4yiWQJhKka6KhhN2 after its last run on 30 Sep 2026; Seedream 4K to 2K in both recipes; the nightly early-exit line in trig_017tQcAgu8D9LxjG3MEmNXx3; the Amazon search change (6f).
- 11g. List the scheduled tasks after editing and read each changed prompt back.

### Step 12 · Verify

Before marking any step done, read it back live:
- Skool: both lessons (logged out for the Value Vault, as a Premium member for the Premium Vault) and the five scheduled posts in SkoolKit.
- Beacons: both products and the code, logged out.
- Pinterest: the renamed public board, and every pin the catch-up task scheduled, on the scheduled pins page.
- Site: the sales page on phone and desktop.
- MailerLite and Facebook: both scheduled; Facebook first comments seen live after posting.
Mark this section DONE with the date and one line per step.
