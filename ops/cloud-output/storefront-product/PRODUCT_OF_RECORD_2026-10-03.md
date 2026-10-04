# The While-You-Sleep Storefront™: product of record

Written 2 Oct 2026 (Eastern), branch `wys-recovery-2026-10-03`. Nothing here is published, deployed or released. The release hold stands.

## The decision

**The customer product is the Claude kit**, the 12 text files plus the Setup Guide PDF in `ops/cloud-output/storefront-product/kit/`, zipped as `While-You-Sleep-Storefront-Kit.zip`.

Why, from the sources:
- `ops/canon/canon.json` products[] (The While-You-Sleep Storefront™) describes "four scheduled task prompts (including a daily missed-run sweep)" and names `ops/cloud-output/storefront-product/kit/` as the kit files.
- The live Beacons product 66271fb0 was rebuilt on 2 Oct "carrying the full kit" (canon.json meta.wys_launch_pricing_2026_10_01).
- The 27 Sep live test (`tests/LIVE_TEST.md`) is the only test of this architecture run in real accounts.
- The V2 / KIT6 build declares itself uncertified: `ops/ai-router/storefront-product/WYS_V2_AUTOMATION_ARCHITECTURE.md` reads "Internal proposed architecture only"; on branch `wys-oct1-manual-path-release-fixes`, `RELEASE_CANDIDATE_MANIFEST.json` reads release_ready false and end_to_end_verified false.

**V2 / KIT6 status: INTERNAL / V2 / NOT CUSTOMER-CERTIFIED.** It covers ChatGPT Work, Metricool, Google Drive, the Creators API, a GO approval per pin and 3 tasks. It is kept intact on its own branches and in `ops/ai-router/storefront-product/` and was not deleted or merged. It cannot ship until it passes its own release gate.

**Conflict flagged once.** On main, the sales page (`src/pages/shop/while-you-sleep-storefront.astro`) described V2 while the zip buyers receive is the Claude kit. Buyers would have paid for one product and received another. This branch fixes the sales page to match the kit. It has not been deployed.

## The 20 answers (Claude kit)

| # | Question | Answer | Source |
|---|---|---|---|
| 1 | Setup app | Claude desktop app. Paste 02_SETUP_PROMPT.txt and answer six questions; it writes MY_RECIPE.txt and the log files. | kit/00 "HOW LONG IT TAKES"; kit/01 item 2; kit/02 |
| 2 | What runs the scheduled tasks | Scheduled tasks in the Claude desktop app | kit/00 para 2; kit/01 item 1 |
| 3 | Where they run | On the buyer's own computer | kit/00 "Two things" 1; kit/01 item 2 |
| 4 | Computer stays on? | Yes, at run times, with Chrome open (minimized is fine) and signed in. Pins post from Pinterest, so the computer can be off at posting time. | kit/00 "Two things" 1 |
| 5 | Browser integration | Claude in Chrome extension, in the buyer's own signed-in Chrome. Browser lock (R16). Never types a password. | kit/01 items 1 and 3; kit/03 R16 |
| 6 | How products are sourced | Normal visible Amazon browsing in Chrome. Reads pages as a person would, with no background scraping (R18). | kit/01 "THE HONEST PART"; kit/03 R18 |
| 7 | Creators API required? | No. It isn't mentioned anywhere in the kit. | kit/00–11 (grep: no matches) |
| 8 | How affiliate links are obtained | The SiteStripe bar on each product page (Associates path, or when the blog half is on). On the Influencer path, products go on the Idea List. Missing SiteStripe means signed out, so the task stops (R14). | kit/01 item 4; kit/03 Part 2 step 3; R14 |
| 9 | How Idea Lists are made | The task builds them in Chrome: Storefront > Create content > Idea List, titled with the look name, every piece added | kit/03 line 55; kit/08 Influencer path |
| 10 | What makes the flat lays | Higgsfield, Seedream 4.5, 2K, portrait 2:3 | kit/01 item 6; kit/03 Pin 1 |
| 11 | What makes the persona images | Google Gemini with the reference image attached. Backup is Nano Banana Pro on Higgsfield. Used for outfit looks only. | kit/07 P7; kit/03 line 79 |
| 12 | How pins are scheduled | Natively in Pinterest's pin builder (Create Pin), in a fresh tab per pin, then read back from pinterest.com/<profile>/scheduled-pins/ | kit/03 Part 5 steps 3–4; kit/06 build and nightly prompts |
| 13 | Metricool required? | No. It isn't mentioned anywhere in the kit. | kit/00–11 (grep: no matches) |
| 14 | Google Drive required? | No. Records are files in the buyer's folder (storefront-log.md, pin-tab.md, pin-drafts.md). | kit/06 READ FIRST lines |
| 15 | GO approval on every pin? | No. Every pin is scheduled automatically. The buyer can type PULL by the cut-off, or delete the pin in the Pinterest app. | kit/00 "Two things" 2; kit/06 pull sweep |
| 16 | How many scheduled tasks | Four: weekly build (Sat, plus Wed at 5–7 looks), nightly Outfit of the Day Sun–Fri (Brand Closet™ members only), pull sweep 12:00 pm and 6:00 pm, missed-run sweep 9:45 am. Non-members run three. | kit/06 lines 2, 13, 46, 78, 110 |
| 17 | Recovery system | Browser lock with a stale rule (R16); leftovers check before scheduling (Part 6 step 4); early-end row fixes and Idea List removal (Part 6 steps 3 and 3b); Runs table; daily missed-run sweep; pull sweep; review of lists still in review | kit/03 R16, Part 6; kit/06 tasks 3–4 |
| 18 | What is automatic | Look choice, product finding, links, Idea List, images, pin copy, scheduling, read-back and logs | kit/00 para 2 |
| 19 | What is manual | Setup (about 5 minutes); keeping the computer on and Chrome signed in; optional PULL; Associates-only on a non-GitHub site: pasting each look's page (10 to 15 minutes a look) | kit/00, kit/01, kit/08 |
| 20 | Influencer vs Associates-only | Influencer: Idea Lists, no website, hands-off. Associates-only: a page on your own site per look. The tasks publish it on GitHub sites; on other sites you paste it in by hand. | kit/08; kit/01 item 4 |

## Test classification

| Test | Class |
|---|---|
| `tests/LIVE_TEST.md`, 27 Sep, Jodie's accounts, Claude architecture, items 1–4 and 6 passed | VALID COMPONENT TEST ONLY. Run in the founder's accounts, not as a buyer; item 5 (missed-run sweep) and item 9 (cleanup) are still pending. |
| `tests/` buyer runs 1–4, TEST_REPORT.md, ROUND_2.md | VALID COMPONENT TEST ONLY (desk runs of the materials, not live) |
| ChatGPT / Metricool / Drive / Creators API runs (project docs WYS_AUDIT_2026-10-02.md, HANDOFF_WYS_THREAD_2026-10-02.md) | V2 TEST. Not evidence for the Claude kit. |
| Any ChatGPT Cloud Browser or web-search run of the Claude kit's Amazon steps | INVALID DUE TO WORKFLOW SUBSTITUTION (router operator-fit rule, 2 Oct) |
| KIT6 private candidate (branch `wys-oct1-manual-path-release-fixes`) | V2 TEST, release_ready false |
| Clean customer end-to-end run of the Claude kit | **NOT YET RUN.** UNVERIFIED. |

## Fixed on this branch

1. `kit/11_WHATS_NEXT.txt`: the affiliate link pointed to the dead product a2e4f613 and now points to 66271fb0, the live public product per canon. The zip was rebuilt (13 files) and the change was read back from inside it.
2. Sales page: every V2 claim was replaced with the kit's own facts (Claude desktop app, Chrome, four tasks, native Pinterest scheduling with PULL, Seedream and Gemini, Influencer or website, runs from your own computer). Prices, dates, checkout and the countdown are untouched. The page builds, and the built page contains no ChatGPT, Metricool, Creators API or GO wording.

## Open, not resolved (flagged once)

- **Image cap.** LIVE_TEST S16 records "at most 3 images per pin… Fixed in the kit 27 Sep", but kit/03 R10 still says 4 (first, two fixes, one fresh try). Left as R10 says until Jodie picks one.
- **Setup Guide PDF** step 6 says "three tasks (four if you're in The Brand Closet™)", while 00 and 06 say four with the nightly one for members only. This is consistent in meaning, so the PDF was not re-rendered.

## Release gate (RELEASE_GATE_V2.md) result: NOT RELEASABLE

Product boundary passes by grep: no task IDs, private URLs, logs or Amazon identifiers in kit/. Every buyer-path, automation-safety and clarity item that needs a run is **UNVERIFIED** until the clean customer end-to-end run is done. The run needs the test folder on Jodie's computer attached to a Claude desktop session.
