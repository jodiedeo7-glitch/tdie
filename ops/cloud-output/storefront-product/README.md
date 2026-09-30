# The While-You-Sleep Storefront™ (working name)

Project sources for turning Jodie's two Amazon Pin workflows into The While-You-Sleep Storefront™ kit and launch funnel. This README began as a 27 Sep 2026 working note and has historical statements that may be stale. Check `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`, section 4 and the live account before making claims about product, lesson, or post status.

## What's here

| Path | What it is |
|---|---|
| `kit/` | The customer kit source: 14 files with numeric prefixes (00 through 13), including three canonical recurring task prompts, the state schema and approved Pin visual standard |
| `While-You-Sleep-Storefront-Kit.zip` | Buyer package: 14 numbered kit files plus the setup guide PDF; rebuild and verify after any source or guide change |
| `pdf/While-You-Sleep-Storefront-Setup-Guide.pdf` | Generated from `render.mjs`; verify all pages after each rebuild |
| `pdf/While-You-Sleep-Storefront-Presale.pdf` | Generated from `render.mjs`; verify after each rebuild |
| `graphics/` | 4 launch graphics (PNG); `photos/` holds their source images and the approved outfit-inspiration sample |
| `IMAGE_PROMPTS.md` | Full prompts for the cover and the 4 graphics |
| `COPY.md` | Skool (5), emails (2), Facebook (2), Threads (5), both vault lessons, Beacons text, Six M check |
| `CANON_ROWS_DRAFT.md` | The canon.json and TDIE_CANON.md rows, drafts only |
| `OWN_SETUP_AUDIT.md` | Jodie's own setup: every problem with its exact fix |
| `tests/` | Historical buyer simulations and live-run notes; they do not prove the current customer Work/Drive/publisher workflow |
| `render.mjs` | Source renderer for both PDFs, graphics and thumbnail contact sheet; run and visually inspect outputs before distribution |
| `run_checks.py` | Runs canon.json `checks` (fail and review) and an em dash check over every file here |

Sales page: branch `storefront-launch`, `src/pages/shop/while-you-sleep-storefront.astro` (never on main until the finish merges it).

## Sources

Read for this job: `ops/cloud-kit/README_START_HERE.md`, `ops/canon/canon.json` (products[] including The Brand Closet™ and Amazon Influencer Storefront, own_affiliate_programs, vault_disambiguation, content_calendar_rules, affiliate_rule, checks, meta.premium_price_increase_2026_09_24, meta.meta_link_rule_2026_09_25), `ops/canon/TDIE_CANON.md`, `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, `TDIE_IMAGE_GENERATION_MASTER.md`, `TDIE_SIX_M_FRAMEWORK.md`, `TDIE_DESIGN_RULES.md`, `TDIE_DFY_SERVICES.md`, `TDIE_THREADS_SYSTEM.md`, `TDIE_JODIE_THREADS_VOICE.md`, `TDIE_ONE_SENTENCE_OFFER.md` (Skool voice sample), `src/lifestyle/README.md`, the look JSON files in `src/lifestyle/`, `src/pages/shop/`, `src/components/LifestyleExtras.astro`, `src/components/Testimonial.astro`, `src/we-reviews.js`.

Historical Claude folder references are not runtime dependencies. The current customer workflow is defined by the numbered kit files; do not rely on unavailable legacy files or claim their contents are read during a task.

## Founder decisions (27 Sep 2026), all applied

1. **Branch scope.** The sales-page source is present in the current storefront architecture branch. Do not rely on the old `storefront-launch` merge instruction; inspect the current branch and deployment state before any release.
2. **Dates.** Tease Sat 3 Oct 3:00 pm; presale Mon 5 Oct 7:00 pm to Thu 8 Oct 11:59 pm; public $27 and member $17 from Fri 9 Oct 9:00 am; launch post Fri 9 Oct 7:00 pm; emails Mon 5 Oct 7:30 pm and Thu 8 Oct 11:00 am. They clear the Premium flash sale and the Keep It Running Kit window, and remove the two-emails-in-one-day problem.
3. **Skool and Facebook posts** rewritten against the posting system rules and four approved posts (see `COPY.md`). The two-link cap wins over "each link twice".
4. **Brand Closet™ line** follows the visible, authorized course interface and current recipe. It uses customer-approved product rows and links, does not reuse member-only materials or third-party destinations, uses bounded recovery, and requires public-board verification plus per-Pin customer selection and schedule authorization.
5. **Join line:** "Affiliate link: I earn a commission if you upgrade, at no extra cost to you." everywhere.
6. **Vault call:** one member-pricing lesson in BOTH vaults; Premium pays half, not nothing; recorded as its own numbered decision in `CANON_ROWS_DRAFT.md`.
7. **Canon rows first:** finish step 4, before any Beacons product.
8. **Amazon search:** the kit reads pages as they load and never fetches in the background (recipe rule R18); the requirements page states the account risk plainly.
9. **Missed runs:** reconciliation is the current third task and handles missed or stale work from structured state. The separate fourth sweep belongs to the retired legacy architecture and is not a canonical task.
10. **Live test** in the buyer's shoes (finish step 9) gates launch readiness; historical buyer simulations do not verify the current customer Work/Drive/publisher path.
11. **Pinterest publishing:** use only the currently documented, supported customer path. The old browser-scheduling decision belongs to the retired local architecture; the current Metricool path and customer authorization gate are documented in `kit/06_SCHEDULED_TASK_PROMPTS.txt`.

Still true and noted: canon's Product Register rule is met by finish step 4 coming before anything goes live. The Value Vault course is Open by design (Decision 95), so the $17 lesson is reachable by non-members; the $17 product itself stays hidden. Buyers' pins use Amazon's own disclosure statement; Jodie's own pins keep canon's wording.

## Recommend it too

Referral check result: 27 Sep 2026, YES. Version A kept. Path: profile picture (top right of Skool) > Settings > Affiliates > "Your affiliate links" > The Brand Closet™ > COPY. The Brand Closet™ About page states members earn 50% recurring commissions when they refer members.
