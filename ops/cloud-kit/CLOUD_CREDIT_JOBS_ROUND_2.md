> **WYS authority, 7 October 2026:** [Read the complete WYS master](https://github.com/jodiedeo7-glitch/tdie/blob/main/claude/WYS_REFERENCE_PACK_2026-10-07.md). It is the sole active WYS workflow. This shared document cannot supply WYS generation defaults or override its current three-image prompts, pause or release hold. SOP-15/SOP-16 and unrelated systems retain their own authority.

> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.

> Migration routing, 1 October 2026: read `ops/TDIE_AI_ROUTER.md` and `ops/ai-router/EXECUTION_CONTRACT.md` first. This source contains historical job specifications, not active schedules. No blanket commit-to-main, push, listing, campaign, pricing or publication instruction here overrides the current task's authorization. Prepare reviewable work and route account operations separately. Do not restore Find Your Door automation. Read SOURCE_RECONCILIATION_2026-10-01.md and the source register for recovered SOP snapshots and remaining live-verification gates.

# CLOUD CREDIT JOBS: ROUND 2

26 September 2026. For the $250 cloud credit (expires 2:59 am ET, 5 November 2026). Already running, so not on this list: the holiday gift guides, the DFY proof samples, the One-Sentence Offer tool. STV is on hold until he replies.

## How every job works
- Start a new cloud session from the Code section (phone, desktop app or claude.ai/code) and pick the repo **jodiedeo7-glitch/tdie**.
- Paste one prompt, everything between START and END. Nothing to attach: every file it needs is in the repo at `ops/cloud-kit/` and `ops/canon/`.
- The cloud does the tedious part. Anything that needs your sign-ins (Amazon, Pinterest, MailerLite, Skool, Beacons, Gemini, Higgsfield) goes into the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`), fully written out. When your week resets, run the DESKTOP FINISH prompt (bottom of `ops/cloud-kit/CLOUD_CREDIT_JOBS.md`) once on your computer and it clears the whole queue.
- Credit figures are estimates (unverified). Watch your balance after the first two; if it's lower than expected, switch the rest to Opus.

## THE LIST, in the order to start them

| # | Job | Model | Credit | What it does for you |
|---|---|---|---|---|
| 1 | Site conversion sweep | Opus | $20 | Fixes the leaks on pages people already visit, live the same day. Starts with the "Coming soon" cards on /lifestyle |
| 2 | Black Friday and Christmas Pink Finds campaign | Opus | $20 | The list-building push and every email for Amazon's biggest commission weeks, forms switching themselves on the right dates |
| 3 | Evergreen Amazon look bank, 8 weeks | Fable | $35 | Everything for 16 evergreen looks except the clicks only your account can do. Your storefront keeps earning after the holidays |
| 4 | Q4 TDIE Pinterest batch, 60 pins | Opus | $25 | 60 finished, rendered pins routed to Skool: 12 days of your 5-a-day cadence |
| 5 | Weekend Ecosystemâ„¢ conversion rebuild | Opus | $20 | Your $97 flagship's sales page, preview page and checkout copy, rebuilt |
| 6 | 15 buyer-intent articles + packs | Opus | $50 | Google traffic to the Ecosystem, the one search channel Pinterest can't block |
| 7 | Pin Writer Bot + Product Builder Bot | Fable | $45 | Two new products with almost no delivery cost |
| 8 | Maniacally Thorough, 10 packets | Fable | $40 | A launch runway for the TikTok channel, with Amazon book tie-ins |
| 9 | Amazon onsite video starter kit | Opus | $10 | The research and 20 scripts you need to unlock onsite commissions (Creator Hub shows 0 of 3 videos) |

Jobs 6, 7 and 8 are the same prompts as Jobs 5, 2 and 3 in `ops/cloud-kit/CLOUD_CREDIT_JOBS.md`. Use those.

---

## JOB 1 Â· SITE CONVERSION SWEEP (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md` and `ops/cloud-kit/TDIE_PINK_FINDS_GROWTH_PLAN.md`. Start your first reply with "Sources checked: [file names]."

THE JOB. Find and fix every conversion leak on the live site, then push the fixes live.

1. Build the site and crawl every page of the built output. For each page record: its one main call to action (or that it has none, or more than one), every price on it, every link and whether it resolves, and whether it passes the Six M pre-ship check.
2. Fix, directly in the code:
   - Wrong or stale prices against canon.json (Membership Premium is quoted at $35/month Â· $297/year everywhere; The Offer Edit, The Funnel Edit and Scaling & Systems carry their Decision 93 prices; Leni Loves shows its real sale state).
   - Broken internal links, dead-end pages with no next step, retired names (8 Claude Prompts, Free Community, VIP, NurseMadeDigital as a brand).
   - Raw URLs showing where a CTA should be words. Links that appear only once where canon wants twice.
   - The "Coming soon" category cards on /lifestyle (Car, Books, Gift Guides and the rest): a shopper who taps one hits nothing. Change each empty category card so it shows the newest looks that do exist and the Pink Finds signup, with honest copy (no promise of a date). A card fills itself as soon as its category gets a look.
   - Any heading or display text still using a thin display serif.
   - Pages missing a title, description or social preview image.
3. Do not change any price, product, offer structure or settled decision. If a page contradicts canon in a way that isn't a clear typo, list it in your report with the fix you'd make, and leave it.
4. Run npm run build, commit, push to main. After the deploy, load every changed page live with the headless browser at phone width and confirm the fix.
5. Save the full crawl table to `ops/cloud-output/conversion-sweep-2026-09.md`, and send it to Jodie. It is data, so report it in full: what you fixed, and anything you left for her decision, each with its one-line fix.

----- END -----

---

## JOB 2 Â· BLACK FRIDAY + CHRISTMAS PINK FINDS CAMPAIGN (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/cloud-kit/TDIE_PINK_FINDS_GROWTH_PLAN.md`, `claude/WYS_REFERENCE_PACK_2026-10-07.md` (sections 8c, 8d, 10 and 12), `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, and in the repo `src/data/pinkfinds.js`, `src/components/PinkFindsSignup.astro`, `src/pages/lifestyle/pink-finds.astro` and the looks in `src/lifestyle/`. Start your first reply with "Sources checked: [file names]."

THE JOB. Build the whole Q4 Pink Finds push so it runs on real dates with nothing left to write.

1. Confirm the real 2026 dates with web search from Amazon's own announcements where they exist: Black Friday week, Cyber Monday (30 Nov 2026), and any holiday deal events Amazon has announced. Anything not announced is written as unconfirmed and not promised.
2. Extend `src/data/pinkfinds.js` so the site forms switch themselves by date: Halloween last call (week of 19 Oct), Black Friday and Cyber Monday gift guides (from about 20 Nov to the end of Cyber Monday), Christmas gift guide (1 Dec to about 20 Dec), then back to "New pink finds, every Friday." Each window gets its own headline and button in Jodie's site voice, and only promises a send that the calendar below actually makes. Build, push, and load /lifestyle/pink-finds live to confirm the current copy still shows correctly.
3. Write every email in full, ready to paste into MailerLite as regular campaigns to the "Lifestyle Pink Finds" group: a Halloween last-call email, a Black Friday picks email, a Cyber Monday email, two Christmas gift-guide emails, and a "last shipping days" email. Each: 3 subject lines, preview text, body, footer ("The looks are styled on an AI model. Pages contain affiliate links; I may earn a commission at no extra cost to you."). Every look links to its thedigitalincomeedit.com/lifestyle page, NEVER to Amazon. No invented deals: where a deal would be named, write "[check Amazon at send time]". Sign off "Jodie".
4. Write the matching Facebook group posts (link in the first comment only, no earnings figures) and @itstommykate story frames (link sticker to /lifestyle/pink-finds; no other links on Instagram), in the voices the README names.
5. Save everything to `ops/cloud-output/pink-finds-q4.md` with a dated send calendar at the top. Push, and send it to Jodie.
6. Add to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`): schedule each email in MailerLite on its date (every piece of copy pasted in), and queue the Facebook posts and stories, reading each one back.

Report in one line.

----- END -----

---

## JOB 3 Â· EVERGREEN AMAZON LOOK BANK, 8 WEEKS (Fable)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `claude/WYS_REFERENCE_PACK_2026-10-07.md` (all of it), `ops/cloud-kit/TDIE_LIFESTYLE_LIST_MAP.md`, `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`, and in the repo `src/lifestyle/README.md` plus three existing look JSON files in `src/lifestyle/`. Start your first reply with "Sources checked: [file names]."

THE JOB. Every holiday look stops earning after about three weeks. Prepare 16 evergreen looks (two a week for 8 weeks, from 5 Oct 2026) from the Lifestyle List Map so the desktop session only has to do what needs Jodie's sign-ins.

1. Pick the 16 by the map's rules: never the already-built "Pink Workwear for a Freezing Office", pink workwear most weeks, never two clothing looks in the same week, dressed for the season each week falls in (fall into winter).
2. For each look, research the products with web search (Amazon listings, review roundups): 5 to 8 items meeting the recipe's bar (4.0 stars or better, 100+ ratings, in stock, Prime where possible, colour story, one neutral). Record each item's short name, its Amazon product page link and ASIN where you can find them, and two backup items. amazon.com itself may be blocked from this container; if so, use search results and label every item "confirm on Amazon".
3. Write, for each look: the lifestyle page JSON in the exact `src/lifestyle/README.md` format (title, category, `season: "Evergreen"`, intro in Jodie's site voice with no prices, image alt text, items with `link` left as "SITESTRIPE_PENDING"); the flat lay or collage image prompt (factory section 4); the Tommy Kate lifestyle photo prompt (factory section 5 and the image master, including her pink tumbler rule and her wardrobe rules); two pins' title, description and alt text within the copy limits, with the #ad disclosure; the @itstommykate caption; and one cross-link line to another evergreen look.
4. Save the JSON drafts to `ops/cloud-output/evergreen-looks/` (NOT in `src/lifestyle/`, so nothing half-built goes live), plus one `PLAN.md` with the 8-week calendar using the factory's posting times. Push, and send Jodie the plan.
5. Add to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`), one section per look: confirm each product on Amazon and swap any that fail the bar, capture Jodie's SiteStripe short links, build the Idea List, generate both images (prompts pasted in), move the finished JSON and images into `src/lifestyle/`, schedule the pins and queue the Instagram post, all per the factory recipe, logging in `claude/LB_PIN_LOG.md`.

Report in one line.

----- END -----

---

## JOB 4 Â· Q4 TDIE PINTEREST BATCH, 60 PINS (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/cloud-kit/TDIE_PIN_RULES.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/canon/canon.json` (`pin_render`, `products[]`) and the articles and resource pages in `src/pages/learn/` and `src/pages/resources/`. Start your first reply with "Sources checked: [file names]."

THE JOB. Make 60 finished TDIE pins (six batches of ten), every one linking to https://www.skool.com/thedigitalincomeedit/about, ready to schedule.

1. Material: the free resources, the /learn articles and the classroom topics. Rewrite each idea search-first. Favour the content-dense reference cards the research says rank (numbered steps, checkbox rows, real list items). About a third saturated hot pink or bubblegum, the rest light.
2. Build a renderer in this container per TDIE_PIN_RULES.md "Rendering in a cloud container", using Newsreader and Inter only and the palette in the design rules (no brown fills). Ten layouts per batch, no layout twice, collage at most twice, lockup on every pin. Persona layouts get a clean photo placeholder plus a full Tommy Kate image prompt.
3. For each pin write the title, description and alt text within the limits, the board (rotate the five boards), and a suggested date and time on the 5-a-day cadence starting the first free day after today, with close cousins 3 days apart.
4. Look at every pin at thumbnail size and fix anything that isn't crisp.
5. Commit the PNGs, a contact sheet image and `pins.csv` (file, title, description, alt, link, board, date, time) to `ops/cloud-output/pins-q4/`. Push, and send Jodie the contact sheet.
6. Add to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`): generate the persona photos (prompts pasted in) and drop them into those pins, show Jodie the contact sheet (first run of this batch), then schedule each pin per the scheduling rules, verifying the count.

Report in one line.

----- END -----

---

## JOB 5 Â· WEEKEND ECOSYSTEMâ„¢ CONVERSION REBUILD (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json` (The Weekend Ecosystemâ„¢ row, key_pages, own_affiliate_programs, emails), `ops/canon/TDIE_CANON.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md`, and in the repo every page under `src/pages/weekend-ecosystem/` plus `src/pages/shop/weekend-ecosystem*`, `src/we-reviews.js` and `src/components/Testimonial.astro`. Start your first reply with "Sources checked: [file names]."

THE JOB. The Weekend Ecosystemâ„¢ ($97 one-time, or 3 Ã— $33.33) is the flagship. Make its sales page and preview page convert harder, without changing the offer.

1. Audit both pages against the Six M pre-ship check and write down each gap before changing anything.
2. Rebuild: her ideal state in the first screen, before the module list; one CTA said at least twice; the payment plan named next to the price; Tina Alexander's review placed where the doubt is highest (through the component; her spelling "word press" kept); an objections section built from the six objection emails' objections (can't build a website, no free weekend, the price, no refunds and what if it isn't what I think, not enough content, I'll do it later), answered honestly: no guarantee, no refund window, no income promise; the free preview as the no-risk step for cold readers.
3. Keep every fact, price and inclusion exactly as canon has it. Zero refunds is stated plainly, never softened into a guarantee.
4. Design per the design rules. Perfect on a phone.
5. Build, push, then load both pages live at phone and desktop width and check every link.
6. Write the Beacons checkout page product description (the only surface with no social proof on it) in the site voice, including Tina's review line, and add it to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`) for pasting into Beacons with a read-back.

Report in one line with both live links.

----- END -----

---

## JOB 9 Â· AMAZON ONSITE VIDEO STARTER KIT (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `claude/WYS_REFERENCE_PACK_2026-10-07.md` and the looks in `src/lifestyle/`. Start your first reply with "Sources checked: [file names]."

THE JOB. Jodie's Amazon Creator Hub shows 0 of 3 videos, so onsite commissions are locked. She wants to learn the process before making any. Build her a starter kit.

1. Research, from Amazon's own Associates and Influencer help pages and reputable creator guides: how onsite commission videos work, the eligibility steps, video specs, what gets a video rejected, and specifically what Amazon's current rules say about AI-generated or AI-assisted video and whether a person must appear. Cite every rule with its source link. Anything you can't confirm from Amazon's own pages is labelled unverified. If AI video isn't allowed, say so plainly at the top.
2. Pick 20 products from her existing looks that suit short review videos, and write a 30 to 60 second script and shot list for each, in a real-reviewer voice, following whatever the rules in step 1 allow.
3. Save it all as a designed PDF per `ops/cloud-kit/TDIE_DESIGN_RULES.md` plus a plain text copy, in `ops/cloud-output/amazon-onsite-video/`. Push, and send Jodie the PDF. Nothing goes in the finish queue: she makes these herself when she's ready.

Report in one line.

----- END -----

---

## JOB 10 Â· WEEKEND ECOSYSTEMâ„¢ COVER + AD CREATIVES (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/canon/canon.json` (The Weekend Ecosystemâ„¢ row), `src/pages/shop/weekend-ecosystem.astro`, `src/we-reviews.js`, and look at every image in `public/images/we/` and `public/og/weekend-ecosystem.jpg`. Start your first reply with "Sources checked: [file names]."

THE JOB. Build a finished set of images for The Weekend Ecosystemâ„¢ ($97 one-time, or 3 Ã— $33.33), composed in code from the photos already in the repo. This container cannot generate new photos; it designs with the ones that exist and writes prompts for any new ones.

1. Audit the current Beacons cover (Jodie's screenshot: big condensed pink sans headline "The Weekend Ecosystemâ„¢", subline "Your website + blog, built from what you already have", "XOXO, Jodie" script, Tommy Kate on a sofa with a laptop and her tumbler) against the design rules. It breaks the type rule (headlines must be Newsreader SemiBold, key words hot pink) and has no depth, stickers or callouts. List what to keep and what to change.
2. Build a renderer (HTML to PNG, Newsreader and Inter from raw.githubusercontent.com/google/fonts) and make:
   - Beacons product cover, 3 images for its carousel (square, 1080 Ã— 1080): the hero; a "what you get" card (22 modules, 36 prompts, three vaults, every update free); Tina Alexander's review card (approved `pull` cut from `src/we-reviews.js`, "word press" spelling kept).
   - Site social preview, 1200 Ã— 630, all text inside the centre 600 px (Facebook crops the sides). Save as a NEW filename in `public/og/` and point the sales page's `ogImage` at it (Facebook caches by filename).
   - Meta ad creatives in four sizes (1080 Ã— 1080, 1080 Ã— 1350, 1080 Ã— 1920, 1200 Ã— 628), five angles each, following the Six M framework: her ideal state, "see the machine free" (preview, no email), the objection "I can't build a website", the payment plan, and the review. **Meta rules: no income or earnings figures, no "make money" promises; Tina's review is allowed because it names no money.**
   - A Keep It Running Kit version of the hero ("free until 4 Oct, 11:59 pm Eastern") as a separate file, so the evergreen hero never goes stale.
   Every image: depth, frosted cards, a sticker badge, big crisp headline with the turn words in hot pink, no brown fills, no thin serifs, readable at phone thumbnail size. Use a different photo per image where the repo has one; where a new photo would do better, leave a clean placeholder and write the full Tommy Kate prompt (her tumbler rule, her wardrobe rules, her world).
3. Write primary text, headline and description for each ad angle (Meta rules; link in no caption; CTA "Learn More" to the preview page).
4. Commit everything to `ops/cloud-output/we-creatives/` plus the new OG image and the page change, build, push to main. Send Jodie a contact sheet of every image.
5. Add to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`): generate any placeholder photos (prompts pasted in) and drop them in; upload the 3 carousel images to the Beacons product in order, reading back; re-scrape the sales page in Facebook's Sharing Debugger; load the ads into Meta Ads Manager only with Jodie's go.

Report in one line.

----- END -----

---

## JOB 11 Â· FULL SITE DESIGN AUDIT + FIXES (Fable)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md`. Start your first reply with "Sources checked: [file names]."

THE JOB. Audit every page of the site the way a senior brand designer and conversion designer would, then fix it. The brand stays the brand: this is polish and consistency, never a redesign (Jodie's standing rule).

1. Build the site and screenshot every page with the headless browser at phone (390 px) and desktop (1440 px) width. Group pages by template (home, articles, resources, shop and sales pages, lifestyle, membership, Weekend Ecosystem member pages).
2. Score each template against the design rules and the Six M check: headline type (Newsreader SemiBold, key words hot pink, big and crisp), depth and something that pops (frosted cards, stickers, callouts), colour (no brown fills, no full pink wash, gold only as a thin line), spacing and rhythm, image quality and consistency, tap targets and text size on phone, one clear call to action, the first screen doing its job, and page speed (image sizes, layout shift). Note every inconsistency between templates.
3. Fix directly in code, template first so one fix lands everywhere: shared components and styles, then page-level. Safe fixes (spacing, type, contrast, image sizing, mobile bugs, inconsistent buttons, missing alt text) ship straight away. Anything that changes a page's structure or look substantially gets built on a branch with before-and-after screenshots and waits for Jodie; never merge those without her yes.
4. Never change a price, product, offer, testimonial or settled decision. Never invent copy claims.
5. Build, push the safe fixes to main, then re-screenshot the changed pages live-equivalent (local build) at both widths.
6. Save `ops/cloud-output/design-audit-2026-09/` with the report (every finding, what was fixed, what's waiting on a branch) and a before-and-after contact sheet per template. Send Jodie the contact sheets and the branch list. This job hands her data, so report it in full.

----- END -----

---

## JOB 12 Â· EVERY PRODUCT COVER + LISTING (starts on your computer, finishes in the cloud)

Beacons, Etsy and Skool can't be opened from a cloud session, so this one is two runs.

**Run A, on your computer (normal usage, short):** Claude desktop app, Chrome signed into Beacons, Etsy and Skool. Paste:

----- START (RUN A) -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md`. Using Chrome on this computer (take the browser lock in `claude/TDIE_BROWSER_LOCK.md` first), open every live product on my Beacons store, every active Etsy listing and every Skool classroom course cover. For each, save: the cover image(s) at full size, the title, the price as shown, the full description text, and the page URL. Change nothing. Commit it all to `ops/cloud-output/listings-capture/` (one folder per product, plus `INDEX.csv`) and push to main. Report in one line with the count.

----- END (RUN A) -----

**Run B, cloud credit (Opus):**

----- START (RUN B) -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/canon/canon.json` and everything in `ops/cloud-output/listings-capture/`. Start your first reply with "Sources checked: [file names]."

THE JOB. Audit and redesign every captured product cover and listing so the whole shop looks like one brand and sells harder.
1. Audit each: cover against the design rules at thumbnail size; title and description against the Six M check, canon prices and names, and platform rules (Etsy: original designs only, no PLR claims, 13 tags; Beacons: price and payment plan correct; no em dashes; no earnings claims anywhere Meta might show it).
2. Build one cover system in code (Newsreader and Inter, the approved build in the design rules) and render a new cover set for every product, reusing existing Tommy Kate photos where they fit and leaving a placeholder plus a full image prompt where a new photo is needed. Rewrite every title and description. Never change a price or what a product includes.
3. Save everything to `ops/cloud-output/listings-redesign/` (per product: new covers, new copy, and a before-and-after card), push, and send Jodie one contact sheet of all the before-and-afters.
4. Add to the relevant workflow queue under `ops/queues/` (see `ops/TDIE_AI_ROUTER.md`): generate any placeholder photos, then upload each product's new covers and copy, reading each listing back live. Only after Jodie approves the contact sheet.

Report in one line with the count.

----- END (RUN B) -----
