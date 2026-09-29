# The While-You-Sleep Storefront™ (working name)

Cloud session, 27 Sep 2026. Jodie's two Amazon pin automations (the themed-look line and The Brand Closet™ Outfit of the Day line) turned into one standalone, sellable kit, with its funnel, and an audit of Jodie's own running setup. **Nothing is published, listed or registered.** Every account step is in `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`, section 4.

## What's here

| Path | What it is |
|---|---|
| `kit/` | The product the buyer gets: 13 numbered kit files, including three scheduled task prompts and the state schema, plus the Setup Guide PDF |
| `While-You-Sleep-Storefront-Kit.zip` | The kit, zipped (rebuilt at the finish after the link tokens are filled) |
| `pdf/While-You-Sleep-Storefront-Setup-Guide.pdf` | 11-page setup guide, numbered steps, two worked examples |
| `pdf/While-You-Sleep-Storefront-Presale.pdf` | The one-page presale file ("You're in ...") |
| `graphics/` | 4 launch graphics (PNG) with photo placeholders; `photos/` takes the generated photos |
| `IMAGE_PROMPTS.md` | Full prompts for the cover and the 4 graphics |
| `COPY.md` | Skool (5), emails (2), Facebook (2), Threads (5), both vault lessons, Beacons text, Six M check |
| `CANON_ROWS_DRAFT.md` | The canon.json and TDIE_CANON.md rows, drafts only |
| `OWN_SETUP_AUDIT.md` | Jodie's own setup: every problem with its exact fix |
| `tests/` | Four buyer tests, the round 1 fix table (`TEST_REPORT.md`), round 2 (`ROUND_2.md`) and the PDF thumbnail check |
| `render.mjs` | Renders both PDFs, the graphics and the thumbnail contact sheet (`node ops/cloud-output/storefront-product/render.mjs`) |
| `run_checks.py` | Runs canon.json `checks` (fail and review) and an em dash check over every file here |

Sales page: branch `storefront-launch`, `src/pages/shop/while-you-sleep-storefront.astro` (never on main until the finish merges it).

## Sources

Read for this job: `ops/cloud-kit/README_START_HERE.md`, `ops/canon/canon.json` (products[] including The Brand Closet™ and Amazon Influencer Storefront, own_affiliate_programs, vault_disambiguation, content_calendar_rules, affiliate_rule, checks, meta.premium_price_increase_2026_09_24, meta.meta_link_rule_2026_09_25), `ops/canon/TDIE_CANON.md`, `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, `TDIE_IMAGE_GENERATION_MASTER.md`, `TDIE_SIX_M_FRAMEWORK.md`, `TDIE_DESIGN_RULES.md`, `TDIE_DFY_SERVICES.md`, `TDIE_THREADS_SYSTEM.md`, `TDIE_JODIE_THREADS_VOICE.md`, `TDIE_ONE_SENTENCE_OFFER.md` (Skool voice sample), `src/lifestyle/README.md`, the look JSON files in `src/lifestyle/`, `src/pages/shop/`, `src/components/LifestyleExtras.astro`, `src/components/Testimonial.astro`, `src/we-reviews.js`.

Historical Claude folder references are not runtime dependencies. The current customer workflow is defined by the numbered kit files; do not rely on unavailable legacy files or claim their contents are read during a task.

## Founder decisions (27 Sep 2026), all applied

1. **Main.** This work is merged into main so the desktop finish can read the queue; `storefront-launch` stays separate and merges at finish step 8.
2. **Dates.** Tease Sat 3 Oct 3:00 pm; presale Mon 5 Oct 7:00 pm to Thu 8 Oct 11:59 pm; public $27 and member $17 from Fri 9 Oct 9:00 am; launch post Fri 9 Oct 7:00 pm; emails Mon 5 Oct 7:30 pm and Thu 8 Oct 11:00 am. They clear the Premium flash sale and the Keep It Running Kit window, and remove the two-emails-in-one-day problem.
3. **Skool and Facebook posts** rewritten against the posting system rules and four approved posts (see `COPY.md`). The two-link cap wins over "each link twice".
4. **Brand Closet™ line** follows the visible, authorized course interface and current recipe. It uses customer-approved product rows and links, does not reuse member-only materials or third-party destinations, uses bounded recovery, and requires public-board verification plus per-Pin customer selection and schedule authorization.
5. **Join line:** "Affiliate link: I earn a commission if you upgrade, at no extra cost to you." everywhere.
6. **Vault call:** one member-pricing lesson in BOTH vaults; Premium pays half, not nothing; recorded as its own numbered decision in `CANON_ROWS_DRAFT.md`.
7. **Canon rows first:** finish step 4, before any Beacons product.
8. **Amazon search:** the kit reads pages as they load and never fetches in the background (recipe rule R18); the requirements page states the account risk plainly.
9. **Missed runs:** a fourth task, the daily 9:45 am missed-run sweep, backed by a Runs table every build and nightly run writes.
10. **Live test** in the buyer's shoes (finish step 9) gates the presale and answers every open item in `tests/ROUND_2.md`.
11. **Pinterest API:** scheduling stays in the browser.

Still true and noted: canon's Product Register rule is met by finish step 4 coming before anything goes live. The Value Vault course is Open by design (Decision 95), so the $17 lesson is reachable by non-members; the $17 product itself stays hidden. Buyers' pins use Amazon's own disclosure statement; Jodie's own pins keep canon's wording.

## Recommend it too

Referral check result: 27 Sep 2026, YES. Version A kept. Path: profile picture (top right of Skool) > Settings > Affiliates > "Your affiliate links" > The Brand Closet™ > COPY. The Brand Closet™ About page states members earn 50% recurring commissions when they refer members.
