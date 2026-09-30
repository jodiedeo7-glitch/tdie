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


## 4 · The While-You-Sleep Storefront™: launch and own-setup fixes (27 Sep 2026, founder decisions applied)

### Current audit update · 30 Sep 2026

This section contains older account-work instructions. The customer workflow and sales copy have since moved to the ChatGPT architecture; read this update before acting on any numbered step below.

- The current source kit has three canonical recurring tasks: weekly look preparation, optional Outfit of the Day, and reconciliation. Do not create the retired four-task Claude/browser setup from the old Step 9 or Step 12 instructions.
- The guide, copy, and sales-page source were corrected for per-Pin customer selection and scheduling authorization, account-dependent Cloud/Local execution, and truthful setup-time language. PDFs and the 15-entry buyer ZIP were rebuilt and checked. PR [#4](https://github.com/jodiedeo7-glitch/tdie/pull/4) merged into `cloudflare-migration` on 30 Sep (commit `1aa50bd80bbfb21a66f35cf041c96df4b59a716e`). Cloudflare's production build completed successfully (build `c13e8952-bc18-4e02-9e1d-06b7f1fd3179`); a fresh read of the live sales page confirms the corrected approval-first copy is live. No marketing Pin or schedule was published or changed.
- The current account-specific end-to-end ChatGPT Work → connected state → Metricool publishing/readback path has not passed. The prior legacy desktop test is historical evidence only; it does not prove the current customer workflow. Keep launch status **NOT READY** until the current path and production board verification pass.
- **ChatGPT account-side probe · 30 Sep:** the `While-You-Sleep Storefront` project initially had no chats, so a first project chat was opened. A read-only Metricool request there returned brand `7142540`, Pinterest profile `TheDigitalIncomeEditTDIE`, and timezone `America/New_York`; a scheduled-post query for 30 Sep–3 Oct returned zero posts. Native Pinterest later showed 28 scheduled Pins, so Metricool's zero is a connector/query coverage gap, not evidence that Pinterest has no scheduled content. A read-only Drive search did not find a standalone storefront buyer guide. It found the related `TDIE AI Operating Manual` (25 Sep 2026), which describes existing TDIE operations and is not proof of storefront functionality. A sample existing Pin destination resolved to a public six-item Amazon Influencer list; this does not verify the storefront product path. Both public test Idea Lists (`Test: Pink Girly Desk Setup` and `Test: Pink Halloween Desk Corner`) have since been deleted from the signed-in Amazon owner storefront; exact-title storefront searches return no results. Relevant additional buyer-workflow checks: verify Pin destination links and any Pinterest domain block; determine computer/browser dependencies; test timezone, scheduled execution and daylight-saving behavior; test interrupted-run recovery without duplicate Pins; confirm content checks; and distinguish publication from outbound-click measurement. These are proposed verification items, not passed tests. Publisher create/readback remains unverified; production board and destination verification passed on 30 Sep. The current ChatGPT mode selector exposes ChatGPT and Codex, not a Work mode; the Work-composer path is still unverified. No Drive document was edited/shared, and no Pinterest Pin, Metricool post, draft, or schedule was changed.
- Read-only Metricool inspection on 30 Sep confirmed brand `7142540`, Pinterest profile `TheDigitalIncomeEditTDIE`, and `America/New_York`. Post `384760924` remains a draft (`draft=true`), not a scheduled post. Its Oct 7 time is withdrawn and must not be treated as an approved publishing date or reused as a live Pin. No marketing Pin was scheduled in this audit.
- **Cloudflare follow-up · 30 Sep 2026:** The migration branch `cloudflare-migration` remains the Cloudflare deployment source and retains the Worker entrypoint, APIs, and `wrangler.jsonc`. PR [#4](https://github.com/jodiedeo7-glitch/tdie/pull/4) merged at commit `1aa50bd80bbfb21a66f35cf041c96df4b59a716e`. The production build succeeded, and a fresh browser read confirmed the updated sales page is live. The separate preview build also passed after adding the Wrangler `previews` setting. The storefront branch remains divergent; do not merge it wholesale. The private empty Pinterest test board is in Recently Deleted, and both public Amazon test lists are removed and absence-verified. No production Pins, Pin schedules, or Idea Lists were changed.
- The approved pink and fall visuals are inspiration samples, not verified retail product photos. Apply `kit/13_PIN_VISUAL_STANDARD.md`; a shopping Pin must depict the exact linked items or clearly identified licensed/customer-owned photos.
- The originally named `outputs/AUTOMATION_WORKFLOW_AUDIT.md` is not present in this checkout. The in-repo `OWN_SETUP_AUDIT.md`, `CHATGPT_CANONICAL_ARCHITECTURE.md`, live-test notes, and current source were used instead. Keep the detailed audit local; do not commit its sensitive account/workflow payload.

**Repo and live-page checks · 30 Sep 2026:** The 158-page Astro build and storefront canon check passed (65 files; four documented historical `REVIEW` hits). The page update was merged to `cloudflare-migration`; Cloudflare production build succeeded and the live browser read confirmed the approved copy is present. The sales-page deployment did not publish or schedule account content.

The kit and its package artifacts are in `ops/cloud-output/storefront-product/` (start with its `README.md`). The approved sales-page copy is live. The numbered account steps below are historical and must be reconciled with the current audit update above before use. Do not publish or list Pins except through the verified, explicitly authorized workflow.

**The gate: the presale does not open until step 9 (the live test) passes.** Step 9 must finish before the tease posts on Sat 3 Oct 2026, 3:00 pm Eastern, and it needs one overnight, so start it no later than Thu 1 Oct.

Three link tokens are used across the copy and are replaced in steps 5 and 7: `BEACONS_PRODUCT_URL` (the public Beacons product), `MEMBER_PRODUCT_URL` (the private $17 product), `VALUE_VAULT_LESSON_URL` (the new Value Vault lesson). The sales page address, `https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront`, is already written in.

### Step 1 · Brand Closet™ referral check

**DONE 27 Sep 2026.** YES, Version A kept (path in README).

1. In Jodie's Chrome, open https://www.skool.com/the-brand-closet (signed in as Jodie).
2. Click the group name at the top left to open the group menu. Look for an affiliate option (Skool labels it "Affiliates"). Also check the About page and settings menu for "Invite", "Refer" or "Earn" with a personal link.
3. If a member-level personal referral link exists, the answer is YES. In `ops/cloud-output/storefront-product/kit/05_RECOMMEND_IT_TOO.txt`, delete the `[KIT BUILD NOTE ...]` paragraph, delete everything from the line `VERSION B (no member referral link)` to the end of the file, and delete the line `VERSION A (members get their own referral link)` with the `====` lines around it. If the path you used differs from "Click the group name at the top left to open the group menu, and choose the affiliate option (on Skool it's labelled Affiliates)", replace that sentence with the exact path.
4. If none exists, the answer is NO. In the same file, delete the `[KIT BUILD NOTE ...]` paragraph, delete everything from the line `VERSION A (members get their own referral link)` down to (not including) the `====` line above `VERSION B (no member referral link)`, and delete the line `VERSION B (no member referral link)` with the `====` lines around it.
5. Record the answer on the "Referral check result" line in `ops/cloud-output/storefront-product/README.md`: the date, YES or NO, which version was kept, and the menu path if YES.
6. Read `05_RECOMMEND_IT_TOO.txt` back: one version only, no build note, no em dashes, and the disclosure reads "Affiliate link: I earn a commission if you upgrade, at no extra cost to you."

### Step 2 · Images

**DONE 27 Sep 2026.** Five photos plus the hoodie flat lay in graphics/photos, render and zip rebuilt, pushed.

1. Open `ops/cloud-output/storefront-product/IMAGE_PROMPTS.md`. For each of the five photos, in its table order:
   - Tommy Kate photos (`cover-sofa-dusk.jpg`, `g1-porch-morning.jpg`, `g3-kitchen-late.jpg`): Google Gemini, attach `public/images/library/avatar-seed-omni-reference.png`, paste the full prompt. If Gemini has no credits or the face drifts, Nano Banana Pro at 2K on Higgsfield with the same reference.
   - Person-free photos (`g2-loft-night-desk.jpg`, `g4-nightstand-phone.jpg`): Seedream 4.5 on Higgsfield, Unlimited switch on, paste the full prompt.
   - Check each at feed size: face and hands natural, her glitter pink tumbler with lavender straw in every frame with her, exactly one candy-pink object in the person-free frames (headphones in g2, tumbler in g4), no lettering or logos, subject on the side the prompt names. Two correction rounds at most; garbled results re-run on Nano Banana Pro at 2K.
   - Save as `ops/cloud-output/storefront-product/graphics/photos/<file name>` using the capture method in `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` section 3c (no downloads).
2. The hoodie flat lay for the Setup Guide, worked example 2: Jodie's OWN generated flat lay for the pink color-block hoodie outfit (the Seedream image logged in `claude/BRAND_CLOSET_PIN_LOG.md`, hoodie row), never Rose's image. Capture it at 1000 × 1500 and save it as `ops/cloud-output/storefront-product/graphics/photos/hoodie-flatlay.jpg`.
3. From the repo root run `node ops/cloud-output/storefront-product/render.mjs`. Open `ops/cloud-output/storefront-product/tests/thumbnails/contact-sheet.png` and every `ops/cloud-output/storefront-product/graphics/*.png`: no placeholder box left, every word crisp at thumbnail size, the presale PDF reads "Friday 9 October 2026 at 9 am ET".
4. Rebuild the kit zip: `cd ops/cloud-output/storefront-product && rm -f While-You-Sleep-Storefront-Kit.zip && zip -j While-You-Sleep-Storefront-Kit.zip kit/*.txt kit/While-You-Sleep-Storefront-Setup-Guide.pdf && cd -`
5. Commit and push to main: `git add ops/cloud-output/storefront-product && git commit -m "Storefront kit: photos, final PDFs and zip" && git push`.

### Step 3 · Dates (founder decision, 27 Sep 2026; nothing to calculate)

| What | When (Eastern) |
|---|---|
| Tease (Skool 1, value slot, no price, no link) | Sat 3 Oct 2026, 3:00 pm |
| Presale opens (Skool 2, sell slot, "Send email to all members" ON) | Mon 5 Oct 2026, 7:00 pm |
| Mid-presale value post (Skool 3, Prime Big Deal Days) | Tue 6 Oct 2026, 3:00 pm |
| Last call (Skool 4, sell slot) | Thu 8 Oct 2026, 7:05 pm |
| Presale closes | Thu 8 Oct 2026, 11:59 pm |
| Public $27 and member $17 live | Fri 9 Oct 2026, 9:00 am |
| Launch post (Skool 5, sell slot) | Fri 9 Oct 2026, 7:00 pm |
| Emails (regular MailerLite campaigns) | Mon 5 Oct 7:30 pm (presale) · Thu 8 Oct 11:00 am (last call) |
| Facebook group | Mon 5 Oct 7:15 pm and Thu 8 Oct 12:00 pm, each with its first comment 5 minutes after |
| Threads | Sat 3 Oct 1:00 pm · Mon 5 Oct 11:00 am · Tue 6 Oct 5:00 pm (product) · Thu 8 Oct 7:00 pm · Fri 9 Oct 5:00 pm (product) |

Every piece's exact time is in the date table at the top of `ops/cloud-output/storefront-product/COPY.md`. These dates clear the Premium flash sale (ended 11:59 pm Eastern, Wed 30 Sep) and the Keep It Running Kit window (Skool promo posts through Sun 4 Oct, objection emails on 1, 3 and 4 Oct). The presale PDF, sales page and copy already carry them.

Checks in SkoolKit before scheduling (step 10):
1. All-member emails: list every post with "Send email to all members" on from Wed 30 Sep 2026 onward. Skool 2 (Mon 5 Oct, 7:00 pm) sends one if no all-member email went out in the 72 hours before it; if one did, leave it off and say so in the report. Skool 4 (Thu 8 Oct, 7:05 pm) turns it on only if no other all-member email went out in the 72 hours before it. Skool 1, 3 and 5 never do.
2. Brand Closet™ days: Skool 2 (Mon 5 Oct) and Skool 5 (Fri 9 Oct) name The Brand Closet™ (no link). If any other affiliate post (Brand Closet™, AIM, Shopify, Upside, Skool platform referral, Earn With Skool) is scheduled on those days, move it to the nearest day with no affiliate post the day before or after.
3. Slots: nothing else in the same slot on the same day (Sat 3 Oct 3:00 pm value; Mon 5 Oct 7:00 pm sell; Tue 6 Oct 3:00 pm value; Thu 8 Oct 7:00 pm sell, Skool 4 at 7:05; Fri 9 Oct 7:00 pm sell). If a slot is taken, move the other post, not this one, unless it is an all-member email post already sent.

### Step 4 · Canon rows first (before any Beacons product exists)

**DONE 27 Sep 2026.** Decisions 121 and 122, both canon copies.

On the same day, in both copies (the claude.ai Project's `canon.json` and `TDIE_CANON.md`, and the repo's `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md`):
1. Paste the blocks from `ops/cloud-output/storefront-product/CANON_ROWS_DRAFT.md`: the products[] row (in price order after the $27 rows), `own_affiliate_programs.while_you_sleep_storefront`, `vault_disambiguation.standalone_member_pricing`, and both `meta` decisions (the product decision and `vault_member_pricing`, the founder's vault call). Decision numbers: the highest "Decision N" in `meta` plus one for the product, plus two for the vault call. Replace `DATE` in the keys with today as `YYYY_MM_DD`. The address fields stay `pending: set in finish step 5, same day` (or step 7) until those steps.
2. Paste the `TDIE_CANON.md` paragraph into §5 PRODUCTS after The Keep It Running Kit paragraph, with the same decision numbers.
3. Validate the repo JSON: `python3 -c "import json;json.load(open('ops/canon/canon.json'))"`. Commit and push. Read the project copies back.

### Step 5 · Beacons

**DONE 27 Sep 2026.** Public product https://links.thedigitalincomeedit.com/shop/a2e4f613-9431-4fd0-ad76-84415e14aa39 ($10, presale PDF, published UNLISTED: the Mon 5 Oct 7:10 pm task adds it to the link in bio). Member product https://links.thedigitalincomeedit.com/shop/36b6f2a8-d26b-4e03-9fa5-b4b698fcf84f ($17, kit zip, unlisted). PREMIUM50 read back at checkout: $8.50. Tokens filled everywhere.

1. **The public product** (the presale, repriced at launch). Add a digital product. Title: `The While-You-Sleep Storefront™`. Price: $10. File: `ops/cloud-output/storefront-product/pdf/While-You-Sleep-Storefront-Presale.pdf`. Description: COPY.md, "Public product", "Description (presale ...)", exactly. Product image: `ops/cloud-output/storefront-product/graphics/g4-share.png`. Visible on the storefront. Save. Copy its public address: this is `BEACONS_PRODUCT_URL`.
2. **The private member product.** Add a digital product. Title: `The While-You-Sleep Storefront™ · member price`. Price: $17. File: `ops/cloud-output/storefront-product/While-You-Sleep-Storefront-Kit.zip` (if Beacons refuses a zip, attach `kit/While-You-Sleep-Storefront-Setup-Guide.pdf` and every `kit/*.txt` file instead). Description: COPY.md, "Private member product". Hidden: never on the storefront, never in the link in bio. Save. Copy its address: this is `MEMBER_PRODUCT_URL`.
3. **The code.** Discount code `PREMIUM50`: 50% off, member product only, no expiry, no usage cap. Save. At the member checkout apply `PREMIUM50` and read the total back as $8.50 (stop before paying).
4. Replace `BEACONS_PRODUCT_URL` and `MEMBER_PRODUCT_URL` with the two addresses everywhere in `ops/cloud-output/storefront-product/COPY.md`, `ops/cloud-output/storefront-product/kit/11_WHATS_NEXT.txt`, the `storefront-launch` branch's `src/pages/shop/while-you-sleep-storefront.astro` (the `CHECKOUT` constant), and the canon rows from step 4 (the `pending: set in finish step 5` fields, both copies, today). Search each for the tokens afterwards: zero left.
5. Rebuild the zip (step 2.4) because `11_WHATS_NEXT.txt` changed, and re-attach it to the member product.
6. Read back logged out: public product $10 with the presale description and image; member product not on the storefront, $17.

### Step 6 · Affiliate

**CHANGED 27 Sep 2026.** Beacons refuses affiliate links on any product under $15 (sale price included), so the 40% link cannot exist during the $10 presale. It is turned on by the launch-morning task (Fri 9 Oct 9:00 am) right after the price moves to $27. Canon updated.

1. In Beacons, turn on the public product's affiliate program at 40% (Beacons' own affiliate product feature, the same mechanic as The Weekend Ecosystem™: one shared link, no application).
2. Read back: in a second browser profile or a test Beacons account, add a digital product, choose affiliate product, paste `BEACONS_PRODUCT_URL`, confirm Beacons offers it at 40%, then delete the test product.

### Step 7 · Vault lessons (one member-pricing lesson in BOTH vaults)

**DONE 27 Sep 2026.** Drafts read back from the server: Value Vault c43ba8257c3c474ba386ba070bb97f87, Premium Vault f35c395b0f3d4e0abfd42f064262e012 (title "The While-You-Sleep Storefront™ · half-price code", Skool caps titles near 50 characters). Published by the launch-morning task.

1. **The Value Vault** course: add a lesson `The While-You-Sleep Storefront™ · member price`. Body: COPY.md, "THE VALUE VAULT LESSON", every link on its words (the two `MEMBER_PRODUCT_URL` links and "see Membership Premium" to https://www.skool.com/thedigitalincomeedit/plans). Leave it unpublished. Copy its address: this is `VALUE_VAULT_LESSON_URL`.
2. **The Premium Vault** course: add a lesson `The While-You-Sleep Storefront™ · your half-price code`. Body: COPY.md, "THE PREMIUM VAULT LESSON", links on their words. Unpublished.
3. Replace `VALUE_VAULT_LESSON_URL` in COPY.md with the address, and write both lesson addresses into the canon row's `pending: set in finish step 7` fields (both copies, today). Zero tokens left.
4. Read both drafts back from the server (Skool drops writes silently): body complete, no empty paragraphs, links on their words, `PREMIUM50` only in the Premium lesson. Both publish on launch morning (step 11).

### Step 8 · Sales page

**DONE 27 Sep 2026.** Checkout link set, build passed, live on main; 8 images load, phone width clean, button hidden until Mon 5 Oct 7:00 pm.

1. On `storefront-launch`, confirm `CHECKOUT` in `src/pages/shop/while-you-sleep-storefront.astro` holds the real `BEACONS_PRODUCT_URL` address, `PRESALE_OPENS` is `2026-10-05T23:00:00Z` and `PUBLIC_PRICE_AT` is `2026-10-09T13:00:00Z`.
2. `npm ci && npx astro build` must pass. Commit ("Sales page: checkout link"), push `storefront-launch`, open a pull request into `main`, merge it.
3. After Vercel deploys, open https://www.thedigitalincomeedit.com/shop/while-you-sleep-storefront logged out on desktop and phone: the eight pin images load; before Mon 5 Oct 7:00 pm the price box says the presale opens Monday 5 October with a closed button; the Tina Alexander line sits only in "The blog half"; no earnings figures, no affiliate rate; the one checkout button opens the Beacons product once the presale is open.

### Step 9 · Live test (the gate: before the tease, and the presale doesn't open until it passes)

Run the kit exactly as a new buyer would, in Jodie's own accounts, on a throwaway theme.
1. Pinterest: create a new board `Test: Pink Desk Finds`, set to SECRET.
2. On Jodie's computer, make a folder `While-You-Sleep TEST` and unzip `ops/cloud-output/storefront-product/While-You-Sleep-Storefront-Kit.zip` into it. Open a new chat in the Claude desktop app with that folder attached and paste `kit/02_SETUP_PROMPT.txt` exactly. Answer as a buyer: theme "Test: Pink Desk Finds" (home, desk finds), board `Test: Pink Desk Finds`, storefront https://www.amazon.com/shop/thedigitalincomeedit, website none (Influencer path), persona yes (the Tommy Kate seed image), The Brand Closet™ yes ($9/month tier), time zone America/New_York, computer on 9 am to 11 pm, pace 3. Then open the new MY_RECIPE.txt and add `TEST` after the board name (the kit's one exception to the public-board rule).
3. Create the scheduled tasks from MY_SCHEDULED_TASKS.txt, names prefixed "TEST ". Pause the TEST nightly task for one night so the missed-run sweep has something to catch.
4. Run the TEST weekly build once by hand. It must build ONE themed look end to end: sourcing, Idea List (title starting "Test:"), both images, pin copy, and both pins scheduled at least 2 days out on the secret test board, logged in pin-tab.md, storefront-log.md and pin-drafts.md.
5. The next morning, let the TEST missed-run sweep fire at 9:45 am: it must spot the missed nightly run and run it once, building ONE Brand Closet™ outfit end to end from the latest Outfit of the Day lesson (own Idea List, both images, both pins at least 2 days out on the test board), never saving Rose's image and never touching "Link to Outfit".
6. Type PULL on one test pin in pin-tab.md before the next sweep; let the TEST pull sweep fire once and remove it.
7. Record every place it stalled or needed a hand in `ops/cloud-output/storefront-product/tests/LIVE_TEST.md` (what happened, file and line, the fix). Fix the kit files, rebuild the zip (step 2.4), push to main, and re-send Jodie the zip.
8. Answer every open item in `ops/cloud-output/storefront-product/tests/ROUND_2.md` in LIVE_TEST.md from this run: folder attach and file writing in a desktop chat; whether a missed run is skipped or waits (and that the missed-run sweep caught it); putting a captured screenshot into a page's file input; the SiteStripe clipboard capture; the Brand Closet™ course name and lesson dates via `__NEXT_DATA__`; Pinterest's AI label option and scheduler time zone; the Squarespace code block question (mark "not tested: no Squarespace site"); the GitHub default branch (mark "not tested: blog half off").
9. **Test cleanup status · 30 Sep 2026:** The private empty Pinterest board `Test: Pink Desk Finds` (0 Pins) was moved to Recently deleted; Pinterest says permanent removal occurs after 7 days. Both public Amazon test Idea Lists, `Test: Pink Girly Desk Setup` and `Test: Pink Halloween Desk Corner`, were deleted from the signed-in owner account after explicit founder confirmation. Readback searched each exact title on the owner storefront and returned no results; neither appears among its 17 remaining posts. Historical test Pin IDs and Pinterest state are recorded in `ops/cloud-output/storefront-product/tests/LIVE_TEST.md`. The four TEST scheduled tasks and `While-You-Sleep TEST` folder are still account/local cleanup items unless separately verified; do not mark the full test teardown complete based only on the Amazon and board cleanup. No production Pins or Idea Lists were touched.
10. Only when steps 4 to 6 all worked (after fixes) does the launch go ahead. If it can't pass before Sat 3 Oct 3:00 pm, tell Jodie in one line and don't schedule step 10.

### Step 10 · Scheduling

**SCHEDULED 27 Sep 2026.** Scheduled task "schedule the launch posts" runs Fri 2 Oct 12:20 pm, only if tests/LIVE_TEST.md passes (step 9, Jodie by Thu 1 Oct).

All copy is in `ops/cloud-output/storefront-product/COPY.md`, at the times in its date table. Paste it exactly.
1. **Skool (SkoolKit):** schedule Skool 1 to 5 with their titles, bodies and images (Skool 1: `graphics/g2-tease.png`; Skool 2: `graphics/g1-presale-open.png`; Skool 3: the four `src/lifestyle/` images it names; Skool 4: `graphics/g3-last-call.png`; Skool 5: `graphics/g4-share.png`). Links hyperlinked on their words, at most two per post. "Send email to all members" per step 3 check 1. Read each back in SkoolKit.
2. **Email (MailerLite):** two regular campaigns (not automations), all active subscribers, from COPY.md, links on their words, signed "xoxo, Jodie", no Amazon links. Send a test to Jodie, then schedule for Mon 5 Oct 7:30 pm and Thu 8 Oct 11:00 am. Read back: both Scheduled.
3. **Facebook group:** Facebook 1 (Mon 5 Oct 7:15 pm, image `graphics/g1-presale-open.png`) and Facebook 2 (Thu 8 Oct 12:00 pm, image `graphics/g3-last-call.png`), no link in the body. Each first comment posts 5 minutes after; where the scheduler can't, put it up by hand. Neither is done until its first-comment link is seen live.
4. **Threads:** add the five posts to the Threads week files for the weeks they fall in, at the slots in COPY.md, with the pinned comments at 7:00 pm on the two product posts (Tue 6 Oct replaces The Weekend Build Challenge that day; Fri 9 Oct replaces The Operating Prompts™), so the nightly Threads load posts them.

### Step 11 · Presale open and launch morning

**SCHEDULED 27 Sep 2026.** 11.1 by the Mon 5 Oct 7:10 pm task (also lists the product in the link in bio). 11.2 and 11.3 by the Fri 9 Oct 9:00 am task (also turns on the 40% affiliate link).

1. **Mon 5 Oct, 7:00 pm:** confirm the public Beacons product shows $10 and the sales page shows the open checkout button.
2. **Fri 9 Oct, 9:00 am:** Beacons public product: replace the file with `ops/cloud-output/storefront-product/While-You-Sleep-Storefront-Kit.zip` (or the PDF and .txt files), change the price to $27, and replace the description with COPY.md's "from Fri 9 Oct" version. Publish both vault lessons.
3. Read back: public product $27 with the new description; a test download serves the kit, not the presale note; member product $17 and hidden; `PREMIUM50` still gives $8.50; both lessons live (the Premium one visible only to Premium); the sales page price box shows $27.

### Step 12 · Own-setup fixes

**STATUS 27 Sep 2026.** 12b, 12c, 12f (2K, early exit, Amazon search) done in both recipes and the nightly task. 12a (board rename and public) and 12d moved into one catch-up task, Mon 28 Sep 2:20 pm, because Pinterest loaded blank today. 12e: stories pause and recipe leftovers line done; the LEFTOVERS block for trig_015j was not added because Jodie retired the pull sweep on 26 Sep (leftovers go to the next build run instead). 12f deletion of trig_01F6oCmn4yiWQJhKka6KhhN2 is in the Mon 5 Oct task (it still has a run on 30 Sep).

Apply `ops/cloud-output/storefront-product/OWN_SETUP_AUDIT.md` in its order, to both recipes (`claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` and `claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md` in the project, plus the repo copy `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`) and the scheduled tasks, using the exact text written there:
- 12a. Section 1: the TK Outfits board (rename, description, public, confirm the scheduled hoodie flat lay is on it), then the recipe and task lines.
- 12b. Section 2: the backlog lines in the line 2 recipe (and the hoodie lifestyle pin, the 24 and 25 Sep outfits).
- 12c. Section 3: the rewritten "Pinterest safety" bullet in both recipes. Scheduling stays in the browser (founder decision, 27 Sep 2026); no API switch.
- 12d. Section 4: the one-off catch-up task with its exact prompt.
- 12e. Section 5: the LEFTOVERS block in trig_015jA7LTzhHTH4cHKA6HuX5r, the leftovers line in both recipes, and the stories pause in section 8d.
- 12f. Section 6: delete trig_01F6oCmn4yiWQJhKka6KhhN2 (its last run was 30 Sep 2026); Seedream 4K to 2K in both recipes; the nightly early-exit line in trig_017tQcAgu8D9LxjG3MEmNXx3; the Amazon search change (6f) in section 3c of the line 1 recipe and in the line 2 recipe.
- 12g. List the scheduled tasks after editing and read each changed prompt back.

### Step 13 · Verify

Before marking any step done, read it back live: Skool (both lessons, logged out for The Value Vault and as a Premium member for The Premium Vault; the five scheduled posts in SkoolKit), Beacons (both products and the code, logged out), Pinterest (the renamed public board; every pin the catch-up task scheduled; no test pins or test board left), the site (the sales page on phone and desktop), MailerLite and Facebook (both scheduled; first comments seen live). Mark this section DONE with the date and one line per step.


### Current audit update · 30 Sep 2026, after live account readback

This update supersedes earlier statements in this section that the production board was unverified or that the current Metricool range returned zero upcoming posts.

- Metricool account verified read-only: brand 7142540, Pinterest profile TheDigitalIncomeEditTDIE, timezone America/New_York. The selected creative remains Metricool draft 384760924 (draft=true; Pinterest status PENDING), not an active Pinterest schedule. October 7 at 1:30 pm Eastern remains withdrawn and is not approved.
- Pinterest board verified public: “Legally Blonde Outfits | Pink Amazon Fashion,” board ID 1122311238330934930, matching the Metricool draft. Its Amazon destination opens the public “Pink Workwear for a Freezing Office” list with six items.
- Pinterest’s native Scheduled Pins page showed 27 Pins through October 6 and did not include the Metricool draft. However, it already contains Pin 3895549053585431488 for October 2 at 1:30 pm on this same board and list, featuring substantially the same cold-office pink workwear outfit. The draft would duplicate that look if scheduled unchanged.
- Keep the Metricool draft unscheduled. Do not reuse October 7. Any replacement must be a clearly different look and angle, with its destination and metadata checked and a newly approved date before scheduling.
- Current launch gate: **NOT READY**. Production board and destination are now verified. The untested item is the customer’s complete ChatGPT Work → connected Drive/Metricool → draft/readback/scheduling-authorization path, plus a distinct nonduplicative Pin candidate. The current Codex environment does not expose ChatGPT Work mode. No production Pin, schedule, or Metricool item was changed.
