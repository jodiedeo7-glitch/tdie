# The While-You-Sleep Storefront™ (working name)

Cloud session, 27 Sep 2026. Jodie's two Amazon pin automations (the themed-look line and The Brand Closet™ Outfit of the Day line) turned into one standalone, sellable kit, with its funnel, and an audit of Jodie's own running setup. **Nothing is published, listed or registered.** Every account step is in `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`, section 4.

## What's here

| Path | What it is |
|---|---|
| `kit/` | The product the buyer gets: 12 plain-text files and the Setup Guide PDF |
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

**Not in the repo (copy from the TDIE Website project):** `claude/TDIE_BRAND_CLOSET_PIN_FACTORY.md` (worked from the facts in the job brief), `claude/TDIE_SKOOL_POSTING_SYSTEM.md` (Skool copy matched to the approved samples in `TDIE_ONE_SENTENCE_OFFER.md` and `TDIE_OFFER_TOOL_PROMO.md` and the tdie-skool-post skill instead), and `claude/BRAND_CLOSET_PIN_LOG.md` (holds the hoodie lifestyle pin copy the audit schedules).

## Flagged once, with the fix

1. **Tease date vs the flash sale.** The brief says the tease posts on the finish day, and also that no date may fall inside the Premium flash sale (ends 11:59 pm Eastern, 30 Sep 2026). A finish on 28 to 30 Sep would put the tease inside it. Fix: the tease posts Thu 1 Oct, 9:00 am, three hours before the presale opens; presale Thu 1 to Sun 4 Oct and launch Mon 5 Oct stay exactly as briefed. A later finish uses the shifted table in the queue.
2. **Product before its canon row.** Canon's Product Register rule wants the row first; the brief says drafts only. Fix: the finish adds the rows (step 6) before anything goes live (steps 7 to 10).
3. **Premium pays for something in The Premium Vault.** Canon says the Premium Vault is the Value Vault fully unlocked. This product is standalone by instruction, so the draft rows say the two lessons carry a price, not a guide, and add one clarifying line to `vault_disambiguation`.
4. **Same-day emails.** The Weekend Ecosystem™ objection series sends at 11:00 am on 1, 3 and 4 Oct. The presale email goes on Fri 2 Oct (the free day); the last-call email has to go on Sun 4 Oct, the presale's last day, at 6:00 pm, seven hours after that morning's objection email.
5. **The Brand Closet™ join line.** Written exactly as briefed ("I earn a commission if you join"). Joining is free and canon's commission is on paid tiers, so strictly it pays only if she upgrades; the existing site card says "if you upgrade". Left as briefed; change "join" to "upgrade" in `kit/04` and the PDF if Jodie prefers the stricter line.
6. **Buyers' pin disclosure.** The kit uses Amazon's own statement on both paths (`#ad As an Amazon Associate I earn from qualifying purchases.`). Jodie's own pins keep canon's Influencer wording; nothing in her setup changes.

## Recommend it too

Referral check result: recorded here at the desktop finish (step 1).
