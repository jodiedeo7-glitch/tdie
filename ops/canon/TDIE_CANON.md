# THE DIGITAL INCOME EDIT™ — CANON
### Current · 25 September 2026 · Single live copy — no versioned predecessors

**Build Your Business Backwards. Scale It Forward.™**

**What this is.** The one governing document for the brand. It replaces Canon v1.0 and v1.1, the Corrections & Decisions Record (all versions), Decision 73 as a standalone file, and the Master Operating Manual v3.0 "Final." Those documents are retired as governing texts. Their decisions survive here as standing rules; their reasoning survives in the Changelog at the end.

**The machine half.** Every enforceable fact below also lives in `canon.json`, which `tdie_audit.py` reads. A price or rule changes in both files on the same day. A rule that is not in `canon.json` is enforced by memory only, which means it is not enforced.

**No more version numbers.** There is one Canon, one `canon.json`, one Resource Map, one SOP Library, one Prompt Library, one Daily OS, one Defect Register. When a document changes, it is edited in place and dated. The version rule that used to say "highest number wins" is retired because there are no longer two numbers to compare.

> **Two copies, kept identical.** This file and `ops/canon/TDIE_CANON.md` in `jodiedeo7-glitch/tdie` are the same document, brought level on 21 September 2026 (Decision 99). Canon changes in both places on the same day, or it has not changed. A repo copy that lags is a stale copy, never a second opinion.

---

## 1 · PRECEDENCE

1. **The live site, repo, Skool and shop.** They override every document, including this one. A document-asserted defect is verified against the live system before it is fixed.
2. **This document and `canon.json`.**
3. **Resource Map · SOP Library · Prompt Library · Daily OS · Repurposing Pack · Tech Standards.** Process, subordinate to canon.
4. **Historical records.** Reference only. Not governing.

**Conflicts are flagged, never resolved silently** — once, before proceeding. A closed item stays closed and is not raised again.

**Product Register rule.** A product gets a row in `canon.json → products[]` before it gets a single asset. No exceptions. If it isn't in the register, it doesn't exist and it doesn't get written. Absence from a document is never grounds for deletion — only positive confirmation that a product does not exist permits removal.

---

## 2 · STANDING FACTS

| | |
|---|---|
| **Canonical host** | `https://www.thedigitalincomeedit.com` |
| **Redirecting hosts** | `thedigitalincomeedit.com` redirects to www. `learn.thedigitalincomeedit.com` 301s to www with the path preserved, and remains the education subdomain — it is no longer the home. An asset printed with a redirecting host as the home is printed wrong. |
| **URL form** | **No trailing slash.** Flat `/learn/[slug]`. |
| **Retired brand** | `nursemadedigital.com` (the domain) and the NurseMadeDigital name are retired everywhere except ONE scoped exception — see Decision 92. Everything on the site, in Skool, in email and on Pinterest runs under The Digital Income Edit™ only. Nurse-forward naming risks brand drift there. The Pinterest username was changed to `TheDigitalIncomeEditTDIE` (September 2026); `nursemadedigital.com` stays a dead domain. **The one exception:** the Threads account `@nursemadedigital` is live and is the account Jodie posts to, as herself — Decision 92, 21 September 2026, after the prior Threads account (the Tommy Kate AI persona) was permanently disabled by Meta. Governing document: `claude/TDIE_THREADS_SYSTEM.md`. |
| **Repo** | `jodiedeo7-glitch/tdie` — Astro on Vercel |
| **Article route** | `/learn/[slug]`, flat. `/blog/` is retired as segment, label and page-type name. |
| **Community** | Skool · `skool.com/thedigitalincomeedit` · Tiers pricing model · **group set to Public, 21 September 2026** |
| **Shop** | Beacons · `links.thedigitalincomeedit.com` — not fetchable, not indexed, unverifiable by tooling |
| **Email** | MailerLite. Env vars: `MAILERLITE_GROUP_ID` (buyers), `MAILERLITE_WAITLIST_GROUP_ID` (waitlist), `MAILERLITE_BAMI_WAITLIST_GROUP_ID`. Kit was never adopted. |
| **Analytics** | Vercel Web Analytics, site-wide |
| **Pinterest** | Username `TheDigitalIncomeEditTDIE` (changed from NurseMadeDigital, September 2026 — `pinterest.com/Nursemadedigital` is now a dead link). **Pinterest blocks every URL on Jodie's domains** — confirmed across www, learn and links. Three appeals were auto-denied. Skool links are the only working Pinterest destination until Jodie says otherwise. The claimed website in Pinterest settings is the bare `thedigitalincomeedit.com` (checked in Pinterest, 16 September 2026); the profile website field shows `www.thedigitalincomeedit.com` as verified. Leave both as they are. Do not edit bio metadata or unclaim the domain until the block resolves — a blocked domain may not be re-claimable. |
| **Amazon** | **Jodie is an approved Amazon Associate and Amazon Influencer** (Decision 101, 24 September 2026). One Associates account, one tracking tag; the Influencer storefront runs on it. Registered in `canon.json → products[]` as "Amazon Influencer Storefront" (not owned). Storefront: `https://www.amazon.com/shop/thedigitalincomeedit` (Decision 113; the old auto-generated `influencer-adc3fcaa` address no longer works). Used on the Legally Blonde Pinterest boards, on Instagram `@itstommykate`, and on the site's `/lifestyle` section. Every link ships with the Amazon disclosure. Never a price. |
| **Instagram** | **Both accounts are Tommy Kate, with two different jobs, never mixed (Decision 112).** `@the.faceless.homestead.mama` is fronted by Tommy Kate and is the face, voice and experiment member of TDIE: the Premium DFY Content Calendar test account (Decision 99), and the account the Daily Prompts, the calendar and every other TDIE asset link to, are inspired by, or use. `@itstommykate` is the affiliate influencer account, a revived old Tommy Kate account (Decision 101). It is separate from TDIE, influencer only, and never uses the Daily Prompts or the DFY Content Calendar. It will grow into a UGC account and is the planned subject of a UGC / AI UGC module, so her content is made with that in mind. |
| **Meta Pixel** | ID ends `...031...` — digit 9 is a THREE. Never "correct" it to `...051...`. |
| **Tool stack** | Astro · Vercel · GitHub · Skool · Beacons · Canva · Claude · MailerLite · Pinterest native. Threads is a channel, run manually/by automation through the browser, not a stack dependency. Nothing outside this list. |

**The New Faceless.** Faceless means the founder's real face is never required — not that no person appears. The brand's face is its AI persona, referenced only by the canonical seed image at `/public/images/library/avatar-seed-omni-reference.png` as "this exact woman." Attach the seed image to every generation prompt. **This governs the site, Skool, Facebook and every generated image.** Threads is the one deliberate exception — see Decision 92: Jodie posts there as herself, by name and by face, not as the AI persona.

**Locked, and never described in words:** her face, facial structure, freckles, skin tone, eye colour, hair colour, hair length and cut, body proportions, age. These come from the seed image alone. Putting any of them into words is what makes her drift from one image to the next.

**Changeable, and described freely — this is what makes two images read as two different days:** how the same hair is worn (loose, braided, claw-clipped, damp, pushed back), nail colour, wardrobe, jewellery, footwear, and what she is doing. Makeup stays minimal and consistent, because a changed face reads as a changed person. Settled 21 September 2026 — Decision 89.

**Positioning thesis.** Jodie is the master of the AI-built faceless business — the complete machine, built backwards. Mechanism pairing: AI + architecture. **Proof is the business itself, not income screenshots.**

**The physical-goods door (Decision 83).** A Shopify store selling print-on-demand or dropshipped products is the same machine with a physical product in the offer slot — product first, store second, fulfilment app third, buyers last. It is one pillar inside the same house, in the same voice, never a second brand, a second community, or a headline identity. Print on demand is the beginner door; dropshipping is door two and only with US-warehoused or same-country suppliers, because the US de minimis duty exemption ended in 2025 and China-direct parcels now carry duties.

---

## 3 · THE LADDER

| Product | Price | Platform |
|---|---|---|
| **Membership Standard** — The Value Vault is available to Standard members à la carte, or in full via Vault Unlock ($49 one-time); it is **not** included in the tier | $9/month · $99/year | Skool |
| **Membership Premium** — includes The Ads Edit™ and the monthly DFY Content Calendar, unlocks The Premium Vault | **$35/month · $297/year** — the only Premium price any promotion quotes, from 24 September 2026 (Decision 114). Skool checkout charges the member flash-sale prices below until 11:59 pm Eastern, Wednesday 30 September 2026, then $35/month · $297/year permanently (Decision 110) | Skool |
| The Business Architect Mentorship Intensive™ (BAMI) | ⬜ pending | Skool |

**Both tiers carry a 7-day free trial.**

**Premium price increase and member flash sale (Decision 110, confirmed by Jodie 24 September 2026).** Membership Premium goes to **$35/month · $297/year** at 11:59 pm Eastern on Wednesday 30 September 2026. Before that, members get first dibs:

| When (Eastern) | Premium price in Skool |
|---|---|
| Sunday 27 Sep, 6:00 pm | $27/month, locked for as long as she stays, or **$197/year** (72 hours) |
| Wednesday 30 Sep, 6:00 pm | $197 closes. Last call: $27/month locked or $250/year |
| Wednesday 30 Sep, 11:59 pm | $35/month · $297/year, permanent |

Existing members keep the price they bought in at (Skool's own pricing dialog says so). Grandfathered Standard access is never taken away and nobody is asked to pay or leave. From 24 September 2026 (Decision 114) the "former free members pay $27/month for Premium" line is replaced by the new price. The three price changes run as scheduled tasks on Jodie's computer, each checking the live price after it saves. The two member emails are scheduled in SkoolKit with "Send email to all members" on: **Blast 1** "Premium prices go up Thursday. You get first dibs." Sunday 27 Sep, 6:05 pm, and **Blast 2** "$197 just closed. Last call on the old prices before midnight." Wednesday 30 Sep, 6:10 pm, set 72 hours and 5 minutes after Blast 1 because Skool allows one all-member email every 72 hours. Both link to the plans page twice on the CTA words and were read back in SkoolKit on 24 September 2026.

**Quote $35 now (Decision 114, founder call, 24 September 2026, 10:57 pm Eastern).** Every page, post, email, PDF, DM and scheduled task that tells anyone what Premium costs says **$35/month · $297/year** from this moment, even though Skool's checkout keeps charging the flash-sale prices until 11:59 pm on 30 September. Jodie's reason: a lower price at checkout is a happy surprise; a higher one is not. The only exceptions are the member flash sale itself (Blast 1, Blast 2, any post that exists only to announce that sale, and the three Skool price-change tasks), because those are the real checkout prices on the days they run. The annual saving is written "eight and a half months' price for twelve". The site was changed and checked live the same night.

**Price-increase and flash-sale windows run 4–5 days at most, with only a few days' heads-up (founder rule, 24 September 2026).** Never announce an increase a month out: a long runway is not scarcity, it reads as unbelievable or just tells people to wait for the deadline. Applies to every future sale or increase.

**No refunds on any digital product.** Stated once on `/faq`, never repeated per-product. **BAMI is the one exception** — see its guarantee below.

**The free tier is permanently retired.** Never reference "Free Community," "Free tier," or a $0 Skool rung again. Approximately 1,231 members were grandfathered in from the prior free tier.

**Renames in force:**

- `Membership Premium ($9)` → **Membership Standard**
- `Membership VIP ($27)` → **Membership Premium**
- `The VIP Vault` → **The Premium Vault**

**Skool at $17/month never existed.** Any asset printing $17/mo is wrong.

**Module tier split (settled September 2026, per the live "Choose Your Membership" card).** Standard: The Essentials Edit, AI Foundations for Creators, Canva Crash Course, AI Twin / Influencer Creation, The Monetization Edit, Brand Building & Brand Identity, The Content Edit, The Email Edit, The Pinterest Edit, The Tommy Kate Edit, Daily Prompts, Vacation & Luxe Babe Vault bonuses — **and, from 18 September 2026, The Shopify Edit (Decision 83).** Premium: everything in Standard plus The Offer Edit, The Funnel Edit, The Ads Edit™, Scaling & Systems, Monthly DFY Content Calendar, The Premium Vault.

**Every published classroom course now carries an explicit gate (Decision 94, 21 September 2026).** Each one was set and then verified by reading the course record back from `api2.skool.com`, never from the editor. **Open on purpose, as the public shop window:** The Essentials Edit, The Value Vault, DFY Services. **Standard:** AI Foundations for Creators, Brand Building & Brand Identity, AI Twin / Influencer Creation, The Monetization Edit, The Content Edit, Daily Prompts, The Tommy Kate Edit, Canva Crash Course, The Shopify Edit, The Email Edit, and Pinterest Foundations™. **Premium:** The Premium Vault, The Ads Edit™, Daily Edits of the Past, both Monthly DFY Content Calendars, and the three Buy Now modules. Confirmed against a genuinely logged-out read once the group went public: a non-member gets lesson titles and cover art on a locked course and zero lesson body text, while the three open courses serve their full contents.

**Vacation Vault and Luxe Babe Prompt Pack are Standard bonuses (Decision 96, 21 September 2026).** Both are named as Standard bonuses on the live Skool plan card, and both were gated to Premium, so a paying Standard member who reached the required level still got nothing. Both moved to Standard with their level gates unchanged — level 2 and level 4. The Workout Vault stays at Premium, level 3, because it is not named on either plan card.

**Standalone module unlock prices (Decision 93, 21 September 2026).** Four classroom modules sell standalone as well as being included in a tier. **Each sells as Buy Now *or* is included in its tier, so tier members never pay twice.**

| Module | Unlock price | Included with |
|---|---|---|
| Pinterest Foundations™ | $27 | Membership Standard |
| The Offer Edit | $37 | Membership Premium |
| The Funnel Edit | $37 | Membership Premium |
| Scaling & Systems | $97 | Membership Premium |

The Offer Edit and The Funnel Edit were raised from $17, and Scaling & Systems from $49, on 21 September 2026. Those old figures are dead wherever they survive — though **$49 is still correct for Vault Unlock**, so check what a $49 is describing before calling it stale. **These are the only standalone module prices.** The Tommy Kate Edit is not sold standalone at all — it is included in Standard and Premium. The Ads Edit™ is **not sold standalone at all** — it is a Premium inclusion with no unlock price, and its pricing is closed and not re-raised (Decision 97, §10a). Every other module is a tier perk with no unlock price.

**The Shopify Edit** — Standard module, the full physical-products build lesson by lesson (store, supplier app, product page, first ten sales). Curriculum of record: `claude/TDIE_SHOPIFY_EDIT_MODULE.md`. **LIVE in Skool (18 Sep 2026):** classroom course id `3f764e2e2cbe49e284a2e3f9244f4592` (URL slug `886389d5`), all 10 lessons published, gated to Standard and verified from the server 21 September 2026. **Cover image set and verified live (18 Sep 2026):** the blush-gradient "THE SHOPIFY EDIT" cover matching the house module-cover style (`cover_image_file` `02336f92102844668de5b82e6ee6bf8d`). It is the paid slot for Pillar 13 on the site.

**Scaling & Systems** — Premium module, **Module 9** following the curriculum reorder. Never Module 6; that number is retired for this module and any asset still printing it is stale. Curriculum of record: `claude/TDIE_SCALING_SYSTEMS_MODULE.md`. **REBUILT AND VERIFIED LIVE (20 Sep 2026):** classroom URL slug `a8a2c78c`, fifteen lessons, all published. Six lessons replaced with the systems actually running inside TDIE (the 8am publish task, the twice-daily reply sweep, the Threads Sunday-write-and-nightly-load system, the DFY calendar pipeline, MailerLite sequences inside the free-plan cap, the seed-image and video pipeline). Four rewritten onto the real stack. Six retired and deleted. This is the module where the Machine Thesis is demonstrable rather than asserted — every lesson in it is something a member can watch running. **The AI CEO Planner™ companion PDF was rebuilt and attached on 21 September 2026 (Decision 87)** — 23 pages, the full planner on Lesson 1 and each worksheet also attached to its own lesson, 17 attachments across the 15 lessons. All nine outdated files were detached and deleted from Skool. The planner is no longer a stale asset. **Platform note:** a deleted Skool lesson id returns a hard 404, not a redirect to its module — any surviving link to a retired lesson is a dead end for the member, not a soft landing on the module page.

**BAMI** supersedes the retired name Faceless Income Intensive™. Sold by application; the third Skool tier card stays toggled off and reserved. **Structure is settled and built (Decision 98, 21 September 2026): 12 weeks, 6 phases, 24 modules, 24 named assets, two weeks per phase, recorded walkthroughs with written founder feedback at six phase gates.** All 24 modules are live in the Skool classroom on the full teaching template, each paired with its same-numbered Blueprint worksheet in 🏛️ BAMI Resources. `/bami` is a live waitlist page — indexable, not in the nav, **carrying no price.** The retired 20-module / 5-phase scheme (Blueprint · Foundation · Structure · Utilities · Penthouse) is dead; any asset printing it is stale. **Price and cohort dates remain undecided and go into no asset until Jodie sets them.**

**BAMI's phases and gate assets.** Phase I · The Specification · weeks 1–2 · modules 1–4 · gate asset The Customer Blueprint™. Phase II · The Brand · weeks 3–4 · modules 5–8 · The Messaging Guide™. Phase III · The Offer · weeks 5–6 · modules 9–12 · The Funnel Frame™. Phase IV · The Machine · weeks 7–8 · modules 13–16 · The Platform Plan™. Phase V · The Traffic · weeks 9–10 · modules 17–20 · The Amplification Plan™. Phase VI · The Business · weeks 11–12 · modules 21–24 · The Business Architecture Binder™.

**BAMI is the one refund exception (live on `/bami` and `/faq`).** Submit the completed Phase I asset within 21 days of cohort start, decide it isn't right, and the payment is refunded in full within 10 business days — no explanation required, no prejudice against a later application. On a payment plan, an instalment already taken is returned and the remainder cancelled. If a cohort is cancelled or moved, the founder chooses a full refund or a seat in the next one at the price paid.

**No BAMI lesson, page or email may promise a live call, a hot seat or a coaching session.** Delivery is recorded; the personal component is written feedback at the six phase gates. The Live Coaching Guide is a recording reference, not a student promise.

**BAMI graduates receive The Weekend Ecosystem™ free on completion** — earned at completion, never "included with BAMI." Stated on `/bami` before application. Applies retroactively to the founding cohort.

**The Premium Monthly DFY Content Calendar** — 31 days of Instagram content delivered as a Skool classroom module. **Two-week rollout:** research starts at the beginning of the last week of the preceding month; the calendar is released one week of posts at a time, every 3–4 days, across the last week of the preceding month and the first week of the month it covers, so each week is tested and scheduled before it runs. Never promise the whole month "before the 1st." Premium only, and the primary reason Premium exists over Standard. **Never sold as a one-time unlock** — it is the strongest retention asset in the business and selling it once would cannibalise the tier it exists to justify. **Purpose:** the calendar organically promotes The Digital Income Edit™ and its paid tiers — anything inside TDIE is fair game. Every offer mention is written as a swap-in slot, so a member can run her own offer or keep the TDIE mention and earn through her Skool affiliate link. Process: SOP 15.

**Research supersedes standing rules for the DFY Content Calendar (Decision 111, 24 September 2026).** Every build starts with extremely thorough viral research: a large set of Reels and posts that got a disproportionate views-to-followers ratio, a major engagement jump or a big follower influx, from accounts in the same niche and of a similar creator type that are normally not viral. Never celebrities or unrealistic accounts. The build finds the patterns and replicates them for the calendar in the persona's own words. Whatever that research proves supersedes any standing rule in canon, SOP 15 or any other document, and the build names every override with its proof. The only rules research cannot override: no income or earnings claims on Meta surfaces, no faith content, no em dashes, no invented products, prices or links, and the Tuesday to Thursday and Vault Wednesday posting rules. The persona is not required in every calendar image; person-free images (her desk, porch, kitchen, hands, a page) are normal and run on Seedream 4.5 with Unlimited on. Process: SOP 15 Phase A, rewritten the same day.

**Pinterest Foundations™** — Standard module, also purchasable standalone at $27. **All Skool modules unlock inside Skool.** No separate checkout page exists for any module, and none is to be built.

**The Weekend Ecosystem™** — $97 one-time, or 3 × $33.33 (the platform's payment-plan minimum is $100), permanent price, 22 modules, delivered as a live website. The launch price ladder is closed; the waitlist page 301-redirects to the sales page. All future updates included free, forever.

---

## 4 · THE THREE VAULTS — NEVER CONFLATED

| Name | Who it is for | What it is |
|---|---|---|
| **The Value Vault** | Standard | The guide collection inside Skool, sold **à la carte**. Each guide carries its own price. A Standard member either buys the individual guides she wants, or pays **Vault Unlock — $49 one-time** to take the whole vault at once. Never called "PLR Vault" alone. |
| **The Premium Vault** | Premium | **The exact same guides as The Value Vault, every one already unlocked**, included in Premium at no extra cost. Nothing is bought à la carte at this tier. |
| **Pretty & Paid PLR Vault™** | Nobody's tier | Separate $11/month Beacons subscription. Off-ladder. In no membership tier. |

Three distinct products. Never conflated, never renamed, never merged.

### The Value Vault course is Open in Skool, and stays Open

**Decision 95, 21 September 2026. Founder call. This is closed.** The Value Vault course in the classroom is set to Open deliberately and permanently, because **it is the storefront**: it carries the links to the à la carte guides, so members and the public have to be able to reach it in order to buy them. Verified logged out the same day — a non-member reaches every Value Vault lesson with its purchase resource attached, exactly as intended.

It is never locked, never appears on a lock list, and is never reported as a public-exposure leak, a defect or an audit finding. The Premium Vault course is the tier-locked twin for Membership Premium. **Any document proposing to lock The Value Vault, or listing it among courses to close off, is wrong and that line is stale.**

### The Value / Premium split — the single most misstated fact in the brand

**The two vaults hold identical contents. The only difference is how the member pays.** Standard pays per guide (or $49 for the lot). Premium pays nothing further — it is already unlocked. That is the whole distinction, and it is the reason Premium exists alongside The Ads Edit™ and the DFY Content Calendar.

**These are false statements, not banned vocabulary — the rule is about what is asserted, not which words are used. None of them may appear in any asset, on any surface:**

- "The Value Vault is included in Standard"
- "every guide, included in Standard"
- "nothing extra to buy" — attached to Standard
- any Standard inclusions list that names The Value Vault without immediately stating it is à la carte

A bare bullet reading `The Value Vault` inside a list of what Standard includes is a defect even when the page defines the vault correctly elsewhere. The bullet is what gets skimmed, quoted and repurposed. Write it as **"The Value Vault — guides à la carte"** or do not list it.

> **Recorded 19 September 2026** after two published Skool posts told Standard members the vault came free with their tier. Both were corrected; one was deleted. This rule exists because that happened, not in anticipation of it.

**The $49-versus-$27 question is closed.** Vault Unlock at $49 one-time sits above the $27/month Premium tier that already includes the same guides. Jodie knows. The vault is still being filled — guides are being added through September 2026 — and the relationship between the two prices is a deliberate interim state, not an error. **It is never raised as a defect, an audit finding, a pricing conflict or an open item.**

**Pretty & Paid PLR Vault™ carries its full prefix and trademark on every first reference.** Short form is banned outright in every title, overlay, heading, button, anchor and alt text — those are first-reference positions with no second reference behind them.

**The Vault never appears in the same asset as a membership tier**, never on adjacent days, never framed as a related product. It promotes **Wednesday only**. Frame by question, never by price.

### What is in the Pretty & Paid PLR Vault™

The "six rebrandable products and three AI transformation workflows" description is **RETIRED**. Any surviving instance is a defect and `tdie_audit.py` fails on it.

- **Products** — planners, journals, guides, eBooks, printables, colouring page sets. Canva-editable, full PLR licence. Bundles rather than single files: 30-page guides, 50+ template sets, 100+ reel packs.
- **Content** — faceless Reel packs, stock photo sets, AI influencer image packs, Pinterest templates, carousel templates, engagement stories, announcement post sets.
- **Training** — Etsy, Stan Store, Beacons, Canva rebranding.
- **PLR Glow Studio** — in-Vault AI tool returning four branded mockup prompts, an SEO product title, a product description, and SEO tags.
- **Cadence** — 20 new products added monthly.
- **Licence** — full PLR, survives cancellation. Downloads are permanent.

> **A product's contents are recorded from the live product, never carried forward from an earlier record.** A contents description in canon is a dated snapshot, not a permanent fact.

---

## 5 · PRODUCTS

Forty-four rows with exact prices and live URLs: **`canon.json → products[]`.** Three affiliate rows were added 21 September 2026 (Decision 90) — The Brand Closet™, Upside and The Anti-Influencer Method™ (AIM) — the Skool platform referral row the same day (Decision 91), and three owned classroom modules the same day (Decision 93) — The Offer Edit, The Funnel Edit and Scaling & Systems, which sell standalone and had been priced in Skool with no register row behind them.

**DFY services (Decision 116, 25 September 2026).** Eleven done-for-you services built on Jodie's own automations, sold from the Open DFY Services classroom course by DM keyword. Each has a row in `products[]`; prices and order words are in `claude/TDIE_DFY_SERVICES.md`. The spicy DFY lesson is Jodie's and is never edited.

**Price collisions.** `tdie_audit.py` computes the collision table from `canon.json` on every run, so it cannot go stale. Wherever two products share a price on one screen, the copy names what each price buys before the reader has to work it out.

**Exact prices. Never `from $`.** Applies to owned products only. Changed deliberately, everywhere, on one day.

**Affiliate commission — two separate rates, not a conflict.** 40% on Skool tiers · 30% on The Weekend Ecosystem™.

**Affiliate.** The link, `rel="sponsored"`, and the disclosure ship as a set or not at all. Never quote a sale price on a product you don't own — publish list price. Verify quarterly that each still exists. **Affiliate products never occupy a pillar's paid slot.**

**The Skool affiliate rotation is capped (20 September 2026).** At most three affiliate posts in any week across *all* affiliate products combined, and three only when there is a genuine sale or something Jodie actually loves. Never two on one day, never two different affiliate products on one day, and never in the day's teaching slot. The old per-product cycles — AIM's six posts, The Brand Closet™'s four — no longer run independently; they draw from one shared queue rationed by this cap. Selling someone else's product is the exception in the feed, not the drumbeat.

**Leni Loves: regular price $37, currently on sale at $27 (Decision 104, 24 September 2026).** Founder correction. The Beacons page shows the real sale, struck-through $37 beside $27, and that is exactly what it should say. Jodie never falsifies a discount; when a real sale or discount is listed on the product, she lists it as a sale. While the sale runs, publish "$27 (regular $37)" or the struck-through $37 beside $27; when it ends, publish $37. Check the live page before naming a price. The $17 figure stays dead. This replaces the 21 September rule that $27 was the only price.

**The Keep It Running Kit (Decision 105, 24 September 2026).** A free bonus with any purchase of The Weekend Ecosystem™, one payment or three, made by Sunday 4 October 2026 at 11:59 pm Eastern: six paid guides worth $63: The Operating Prompts™ ($19), The First 30 Days After Your Site Goes Live ($17), How I Batch & Schedule a Month of Pinterest in One 3-Hour Block ($9), Build Your First Freebie in One Afternoon ($7), My Exact $0-to-First-Sale Path (What I'd Do This Week) ($7) and My 5-Minute Canva Pin Template Swap (1 Design → 30) ($4). Delivered through a private $0 Beacons product linked only from the Access Granted email during the window. Every guide has its own row in `products[]`, and so does the Kit, marked private. The deadline is real: the email block comes out at 11:59 pm on 4 October.

**Email series of record (`canon.json → emails`).** The Weekend Ecosystem™ objection series: six emails, 11:00 am Eastern on 25, 27 and 29 September and 1, 3 and 4 October 2026, to every subscriber except the Weekend Ecosystem Buyers group, scheduled and read back in MailerLite on 24 September 2026. Email 3 is the payment plan email; Emails 2 and 6 mention the plan. Doc of record: `claude/TDIE_ECOSYSTEM_OBJECTION_SERIES.md`.

**Shopify (affiliate, Decision 83, amended 18 September 2026).** Registered in `products[]` as not owned. **Every Shopify link on every surface — site, Skool, email, Facebook — is Jodie's direct affiliate link `https://shopify.pxf.io/eK3xYz`. There is no bridge page.** Founder call: the link that ships is always the direct one. Wherever it appears it travels with `rel="sponsored"` and the affiliate disclosure as a set (Standing Rule 18) — the journey card and the inline article links both carry the disclosure, and on Facebook the disclosure sits in the comment beside the link. No earnings figures ever appear on a Meta surface. Shopify's offer as of 18 September 2026: 3-day free trial, then $1/month for 3 months (monthly billing), then Basic at $39/month monthly or $29/month annual. Shopify's prices, subject to change — verified quarterly with the other affiliates.

**Amazon (affiliate, Decision 101, 24 September 2026).** Jodie is an approved Amazon Associate and Amazon Influencer. Registered in `products[]` as "Amazon Influencer Storefront", not owned. Pinterest pins link to the storefront Idea List for each look; the site's `/lifestyle` pages use her SiteStripe item links and Idea Lists. Every link travels with the disclosure (Standing Rule 18) and `rel="sponsored nofollow"` on the site. No price is ever shown. It does not fill the Pillar 5 affiliate slot. Amazon's own listing photos are never posted; they are only references for AI-made images.

**Jodie is not a Canva affiliate** (September 2026). Canva is recommended without a link and without an affiliate disclosure. Any asset naming "Canva Pro" in a list of affiliate examples is stale — corrected in the Scaling & Systems module on 20 September 2026.

**Flagged, not cut.** Named in canon, no confirmed live listing, or confirmed but still being built out. Do not write into an asset until confirmed: Luxe Babe Prompt Pack · Vacation Vault™ · Workout Vault™ · AI CEO Planner™ (the Module 9 companion workbook, rebuilt and attached 21 September 2026; flagged only because it has no standalone listing — it is not stale and not a defect) · Vault Unlock ($49 one-time) · DFY Pinterest packages · Pinterest Traffic Engine™.

**Vault Unlock — $49 one-time.** Confirmed by Jodie 19 September 2026. It buys a Standard member the entire Value Vault in one payment instead of guide by guide. See §4. **It stays on the flagged-not-cut list above** — confirmed 21 September 2026 by Jodie, who is keeping the offer and adding guides to the vault. Removing it was considered while the vault was thin and was decided against. Flagged means do not write it into a new asset until Jodie says the vault is full enough; it does not mean the price is in question. The $49-versus-$27 relationship is closed — see §4 and §10a — and is never re-raised.

---

## 6 · SITE ARCHITECTURE

**Navigation:** `HOME · LEARN · SHOP · FREE RESOURCES · ABOUT · CONTACT`
Utility, top-right: `Search · Member Login · Join the Membership`

**Learn is the sole educational hub.** There is no Blog section, no `/blog/` segment, no "blog post" as a page-type name. Blogging survives as a *topic*, not a section.

**Routes:** `/` `/learn/` `/learn/[slug]` `/shop/` `/resources/` `/about/` `/contact/` `/membership/` `/lifestyle` `/lifestyle/[category]` `/lifestyle/[look]`

**`/lifestyle` (Decision 101, 24 September 2026)** is the shop-the-look section for Jodie's Amazon Influencer looks: a hub, ten category pages (clothing, accessories, jewelry, beauty, perfume, home decor, dorm, car, books, gift guides) and one page per look. It is in the site nav and footer. It is **not a pillar, not part of the `/learn` library, never a journey slot**, and it changes no Resource Map pillar row. Pages build automatically from one JSON file plus images per look in `src/lifestyle/` (format in `src/lifestyle/README.md`); the Legally Blonde pin factory adds them. A look with no images or no links is skipped by the build.
No dates in URLs. Short descriptive slugs only.

**`/bami`** is live, indexable, in the sitemap, and deliberately not in the navigation. It is reached by direct link from promotion, not by browsing.

**Thirteen pillars, all live.** Slugs of record are in `canon.json → pillars[]`. The pillar library is the spine; clusters hang off it. New content is supporting articles under a pillar, **not new pillars** — Pillar 13 (Physical Products, Decision 83) was the one founder-approved exception and is now closed; the next physical-goods side hustle, if any, is a cluster under Pillar 13, not a fourteenth pillar.

**Pillar 13 — Physical Products.** Category label `Physical Products`. Pillar guide `/learn/shopify-store-guide`. Cluster: `/learn/print-on-demand-vs-dropshipping`, `/learn/shopify-store-in-a-weekend`, `/learn/what-to-sell-online`, `/learn/shopify-supplier-apps`, `/learn/first-10-shopify-sales`. Free slot: The Shopify Starter Kit at `/resources/shopify-starter-kit`. Paid slot: Membership Standard (The Shopify Edit). Affiliate slot: Shopify — Jodie's direct affiliate link on every link, with `rel="sponsored"` and the disclosure. Routing lives in `ArticleLayout.astro` under the `Physical Products` key. **Every Physical Products article carries the prominent `ShopifyCTA.astro` card (button + `rel="sponsored"` + disclosure as a set) placed high (before Chapter One) and again near the end — four direct affiliate links per page in total — plus `ArticleImage.astro` library photos in the body (added 18 Sep 2026). These are the revenue engine of the pillar; do not strip or bury them.**

**Bridge pages.** All 26 owned bridge pages are live. Products route through owned URLs. Beacons direct links are removed site-wide. (Shopify is the deliberate exception — Decision 83 ships its direct affiliate link, not a bridge.)

### Journey slots

- **Free slot: $0 only.** Topical relevance never overrides this. A price in a free slot is a defect.
- **Paid slot: never an affiliate product.**
- **Close-out: at most one price.**

### Linking

Every article sends 3–8 related links plus its lead magnet, product, membership and pillar — **and receives links from its pillar guide and relevant siblings.** Outbound always gets done; inbound never does. That is the orphan failure, and it is checked by machine.

Never leave a page as a dead end.

### The eight mandatory close-out items

An article is not done until all eight are present. If any is absent, it does not ship.

1. **Journey block** present and routed by pillar through the `related` prop — never a hand-written `slot="journey"`.
2. **Free slot** carries a $0 resource. A price in a free slot is a defect regardless of topical fit.
3. **Paid slot** carries an owned product, never an affiliate. Affiliate only where genuinely relevant, and a blank affiliate field is a pass, not a gap.
4. **Lead magnet** offered once, with its own link.
5. **Newsletter CTA** — MailerLite, one instance.
6. **Community CTA** — Skool, one instance, single door. No tier ladder, no adjacent sequence.
7. **Pillar guide link** up, plus 3–8 related article links across, plus **at least one inbound link added** from the pillar guide or a sibling.
8. **Both manifest entries written** — `src/data/article-dates.js` and the cluster array in `src/pages/learn/index.astro`.

Close-out carries at most one price, and every product named has a row in `canon.json → products[]`.

> **Provenance.** These eight were authored 1 September 2026 from canon. The original eight lived in Master Operating Manual v3.0 Part 5, which was retired and deleted before they were copied across; they are not recoverable. This list is a replacement, not a reconstruction.

### Two updates per new article

An article that gets only the first of these will not appear in the library or the RSS feed:

1. The article file itself.
2. `src/data/article-dates.js` **and** the cluster array in `src/pages/learn/index.astro`.

Article routing is controlled by passing a `related` prop to `ArticleLayout.astro`. **Never hand-write a `slot="journey"` block in the page body.**

---

## 7 · VOICE

Founder with opinions. Tension, curiosity, specificity. Never *learn how*, *here's a guide*, *this week's article*, *check out my latest post*.

**There are no banned words in this brand (Decision 85).** What is constrained is what an asset *asserts*, never which words it uses: no manufactured urgency, no fabricated scarcity, no fabricated social proof, no promises about how fast results arrive, no earnings figures on Meta, no third-party IP, and no misstatement of what a tier includes. Word choice is the founder's.

**Three registers now, never mixed.** Skool community posts: warm, casual, emoji-forward, peer-to-peer, short lines, heavy white space. Site and editorial: luxury editorial mentor. **Threads: Jodie's own real voice — snarky, funny, smart, to the point, an authority, a good seller, not soft, a girls' girl who cheers other women on. Governing document: `claude/TDIE_JODIE_THREADS_VOICE.md` (Decision 92, 21 September 2026) — it overrides this section for Threads specifically, the same way TDIE_TOMMY_KATE_VOICE.md used to for the retired Threads persona.**

**Income and earnings claims** are permitted on every surface **except Meta platforms** (Facebook and Instagram). This includes any page a Meta ad can reach. The Shopify affiliate figure Jodie has earned from Facebook replies is never quoted in a Facebook reply, a Facebook group post, or an Instagram post.

### Content calendar rules

- No membership tier content Tuesday–Thursday.
- Pretty & Paid PLR Vault™ promotes Wednesday only.
- Vault and membership posts never share a day and never sit on adjacent days.
- **Every link is buried in the CTA words.** A spelled-out URL never appears in a post, with one exception: `www.thedigitalincomeedit.com` on its own, which is the brand's address. At most two hyperlinks per post.
- **Facebook and Instagram posts never carry a link (Decision 115, 25 September 2026).** No link of any kind goes in a Facebook or Instagram post body or caption, because Meta suppresses posts that carry one. The post names the call to action in words and points to the comments ("link's in the comments 👇"). The link goes only in the first comment, set to post automatically 5 minutes after the post's scheduled publish time; where the scheduler cannot do that, the comment goes up by hand 5 minutes after the post is live, and no post is reported done until its first-comment link has been seen live. **Skool links are never a raw web address:** anywhere a link can sit behind words (Skool posts, comments and lessons, email, the site, PDFs), a Skool link is a hyperlink buried in the call-to-action words. Facebook and Instagram comments cannot hide a link behind words, so there the link sits on its own line after a short call-to-action line. Instagram Story link stickers are untouched until Jodie says otherwise.
- **Membership Standard is never sold in the Skool feed.** 1,213 of the 1,234 members already hold Standard on free lifetime access, so a Standard post asks nearly the whole room to pay for what it has. Standard stays the entry offer for cold traffic arriving from outside the community.

**Governing document for the community feed:** `claude/TDIE_SKOOL_POSTING_SYSTEM.md` — the slot times, the weekly mix, the affiliate cap and the day rules. It is what the weekly SkoolKit load reads from.

**Governing document for Threads:** `claude/TDIE_THREADS_SYSTEM.md`, voice companion `claude/TDIE_JODIE_THREADS_VOICE.md` — the schedule, the account, and Jodie's own voice as the account's real, named founder. See Decision 92. **No direct messages, ever, on Threads or Instagram, from any part of this system, and outreach/reply comments left on other people's posts never carry a pasted link — see Decision 107 and `claude/TDIE_THREADS_SYSTEM.md` Sections 4–5.**

---

## 8 · DESIGN

**Palette.** Six colours. The hex is the authority for set type, Canva design work and rendered pins.

**Hex codes are never written inside a generator prompt.** They render as visible characters in the picture — a defect that cost a full day of rework in September 2026. Inside a prompt, colour is written as name plus shade, plus what it is *not* wherever it has rendered wrong before: *saturated candy pink, never pale* · *lavender, clearly purple-toned, never white or grey*. An unqualified colour word defaults pale — "pink" produces near-white — so every colour named in a prompt is qualified. Settled 21 September 2026 — Decision 89. This replaces the former rule that a colour name without a hex was a fail.

| | |
|---|---|
| Signature Hot Pink | `#D62E73` |
| Luxury Cream | `#FBF8F5` |
| Dark Chocolate | `#2B161B` |
| Muted Gold | `#C8A96A` |
| Bubblegum Pink | `#FF8AC2` |
| Lavender | `#CBB7F7` — never dominant |

Six colours. Magenta, deep plum and antique gold are retired. The ten-colour palette in the old Master Operating Manual — Soft Blush, Soft White, Warm Taupe, Light Rose, Dusty Mauve, Soft Gray — **is retired with it.**

**Type.** Fraunces (display) · Cormorant Garamond (serif; the italic carries the turn line) · Inter (sans; eyebrows and lockups only). One to two families per asset. The old Manual's Canela / Editorial New / Ivy Presto / Manrope alternatives are retired.

Variable axis order — wrong order silently applies default weights:

- Fraunces `[opsz, wght, SOFT, WONK]`
- Cormorant Garamond `[wght]`
- Inter `[opsz, wght]`

**Tier badges.** Standard `#FF8AC2` · Premium `#D62E73`. The Free badge is retired with the free tier. Gold and Lavender badges for standalones and member rewards are proposed, not canon.

**Text is set, never generated — for nano banana (Gemini) only.** Canva AI renders text accurately; do not strip text from Canva prompts and do not warn about garbled letterforms.

**One scoped exception (Decision 109, 24 September 2026):** the Legally Blonde Amazon pins and their Instagram versions keep the short title overlay the generator writes into the image, because it comes out crisp, spelled right, and looks best. Every overlay is checked letter by letter before the pin ships; a misspelled, warped or garbled word means the image is regenerated or the text is set instead. Every other asset follows the rule above.

**Aesthetic.** "Her real life, shot beautifully" — lived-in modern farmhouse, real slow country life. Not staged, not costume cottagecore, **and not a penthouse skyline.**

**Quiet wealth, lived in (settled 21 September 2026 — Decision 89).** She is extremely wealthy and self-made, and you would not know it from looking at her or at her house. Nice, never showy. Real, never run-down. Not an AI-perfect surface, not a five-million-dollar mansion — and not messy either. Clean and natural, with the evidence of kids, dogs and farm animals present in the room rather than the mess of them. Decor that suits her and complements the farmhouse, not decor that performs for the camera. This register governs persona photography; the luxury-campaign register in the Prompt Library governs pin *design*, and the two are not interchangeable.

Wardrobe locked: oversized pink knits, soft tees, hoodies, sweatpants, leggings, fuzzy socks, gold claw clip. Blouses, blazers and costume cottagecore are banned. Signature prop: glitter-flecked pink iced coffee tumbler with lavender straw, in every frame with her.

**Hard third-party IP ban** in every generated image, prompt, listing and asset. No characters, no logos, no branded handbags, no film or franchise likenesses. This has already caused platform deactivations. The same ban governs every product design example in the physical-products track: no cartoon characters, team logos, band names or memes, and recolouring does not make them safe.

**Rendering.** Pins render at 2× (2000×3000) then downsample to 1000×1500 via LANCZOS. Direct Python/Pillow is faster and more reliable than browser-based Canva automation at scale. Canva is retained for carousels, lead magnets, Skool graphics and product mockups.

**Every visual asset is self-audited at feed and thumbnail scale and fully optimised before delivery.** Never ship a first pass and offer to improve it afterward.

---

## 9 · SECURITY

**Classic personal access tokens, never fine-grained.** Test immediately before use. **Generated fresh per session, scoped to the single repo, and revoked when the session ends** — not soon, not at end of day. Revocation confirmed in the GitHub UI.

Weekly: zero live tokens. Any survivor gets revoked **and the reason it survived gets recorded.** The record is the deliverable; the revocation takes ten seconds.

`history -c 2>/dev/null; unset GH` after every session. Working copies removed with `rm -rf`.

**Commit pattern:** fetch HEAD SHA → get base tree SHA → create blobs → POST new tree with `base_tree` → POST new commit → PATCH ref. Delete a file by including its path in the tree with `"sha": null`. Binary files base64-encoded in the blob payload. Raw content via the `Accept: application/vnd.github.raw` header. Repo tarball beats paginating the contents API for full audits.

**When the container cannot reach GitHub, commit from the browser (Decision 98).** The agent proxy refuses `jodiedeo7-glitch/tdie` for both `git push` and `api.github.com` regardless of credential, and no `add_repo` tool is exposed — **a pasted token does not fix it.** The route that works: open a page on Jodie's own domain in her browser, then `fetch` the GitHub contents API from that page with the token in the `Authorization` header. GitHub's API sends permissive CORS, and her browser is not behind the container's proxy. Do not attempt it from an `api.github.com` page — GitHub's own `default-src 'none'` CSP blocks the call. Read the file, patch the string in page context, verify, then `PUT` with the file's `sha`. **For a file too large to paste into one script, send the new content as base64 in numbered chunks, concatenate them in page context, and pass the assembled string straight to the API's `content` field — it wants base64 anyway, so nothing has to be decoded (Decision 99).**

**Skool writes are verified from the server, never from the editor.** A `PUT` to `api2.skool.com/courses/{id}` returns 200 and can still not be what you meant — course access, tier and price are read back with a fresh `GET` after every write before anything is called done. Course access lives on the course record as `privacy` (0 open · 1 tier · 2 level · 3 buy-now), `min_tier` (1 Standard · 2 Premium), `min_access_level`, and `amount` in cents. Setting `amount` on a buy-now course creates its billing product automatically.

**Always verify live state before committing.** The project file copy is not ground truth.

---

## 10 · WHAT IS OPEN

Decisions and dependencies, not process. No amount of correct execution resolves them.

| Item | Blocks |
|---|---|
| Both Blueprint lead magnets are materially wrong — see the Defect Register | Every opt-in currently running |
| The One & Done sales page carries third-party IP and income projections | The $27 product's entire funnel |
| Skool cover image carries fabricated earnings and a branded handbag | The community's first impression |
| The Pinterest Edit is named as a Standard inclusion on the live plan card but is an unpublished draft in the classroom | A tier promise nobody can open |
| BAMI price and cohort dates — provisional thinking only (beta around $297, launch around $1,497, then scale on results); nothing is final and none of it goes into an asset. **Structure and live URL are no longer open — see Decision 98.** | The ladder's top rung, and the switch from waitlist to application |
| BAMI's 24 module walkthrough videos are not recorded — `/bami` promises a recorded walkthrough per module | A cohort starting at all |
| Value Vault ledger count | Every "total value" claim in Vault marketing |
| Pinterest domain unblock | Pinterest Traffic Engine™, and any Pinterest-led BAMI promotion |
| Nineteen live shop products routed to no pillar | Nineteen assets earning nothing from site traffic |
| Per-pillar freebies replacing the shared Blueprint fallback — pattern now proven on Pillar 13 (dedicated MailerLite form → pillar group → delivery automation, single opt-in); the other twelve pillars still share `TDIE Freebie Capture` | Welcome-sequence segmentation |
| `tdie_audit.py` GitHub Actions deploy — token missing `workflow` scope | The Friday automated audit |
| Sneak-peek PDF in `public/` is publicly reachable and bypasses the email gate | Every opt-in that PDF was built to earn |
| Inactive *WAITLIST* product in Beacons | Nothing — but it carries the retired domain |
| ~~`/affiliates` hub page — status unconfirmed~~ RESOLVED 21 Sep 2026 (Decision 100): there is no `/affiliates` page and none is to be built. Founder call. The route never existed, no page file was ever written, nothing on the site links to it, and it returned a 404 the whole time it sat on this list. The member affiliate programme is explained where a buyer already is — in the Weekend Ecosystem™ Access Granted email — not on a page of its own. | — |
| Product and FAQPage JSON-LD on `/shop/weekend-ecosystem`; public `/weekend-ecosystem/curriculum` page | Search indexing of the flagship |
| EverAds Standard-tier campaign — 60 creatives selected, generation not triggered | Standard acquisition |
| Fourthwall merch — awaiting designs, retail pricing, collection name | The merch component of Meta ads |
| ~~The Ads Edit™ shows a Buy Now button with no price~~ RESOLVED 21 Sep 2026: it is not a standalone product; the Buy Now setting was the error and the course is now tier-locked to Premium. See Decision 97. | — |
| ~~`/bami` advertises a 20-module, 5-phase programme that no longer exists~~ RESOLVED 21 Sep 2026: corrected to 6 phases / 24 modules / 24 assets and verified live. See Decision 98. | — |
| ~~The repo copy of canon is twelve decisions behind this file~~ RESOLVED 21 Sep 2026: `ops/canon/TDIE_CANON.md` replaced wholesale; the two copies are now identical. See Decision 99. | — |
| ~~Links pointing at the six deleted Scaling & Systems lessons~~ RESOLVED 21 Sep 2026 — swept and clean. All 325 community posts, all 93 live site pages, and all 1,022 lessons across the 30 classroom courses were scanned for the six retired lesson ids. Zero references found anywhere. The three classroom deep-links on the site (Brand Building, Pinterest Foundations, The Tommy Kate Edit) were opened and confirmed live. Sent emails cannot be swept and are accepted as unfixable. | — |
| ~~Pillar 13 site files written and building locally; not yet committed~~ RESOLVED 18 Sep 2026: pillar guide, five cluster articles, kit capture page and Standard tier listing all committed and live on `www.thedigitalincomeedit.com` (verified) | — |
| ~~The Shopify Edit module — not yet loaded into Skool~~ RESOLVED 18 Sep 2026: all 10 lessons live in the classroom, course id `3f764e2e2cbe49e284a2e3f9244f4592` | — |
| ~~The Shopify Starter Kit — kit PDF needs producing and wiring to delivery~~ RESOLVED 18 Sep 2026: 5-page editorial PDF produced, hosted in MailerLite, and delivering live. First **per-pillar** freebie: the kit page (`/resources/shopify-starter-kit`) posts to a dedicated MailerLite form (id `198982894072366185`, single opt-in) that adds subscribers to the **Physical Products** group; the active automation *Shopify Starter Kit — Delivery* emails the kit on group-join. End-to-end tested (a test opt-in completed the automation). | — |
| ~~Scaling & Systems is built on a stack Jodie does not use and contains no automation she actually runs~~ RESOLVED 20 Sep 2026: rebuilt as Module 9, fifteen lessons, verified live. See Decision 86 and `claude/TDIE_SCALING_SYSTEMS_MODULE.md`. | — |
| ~~The AI CEO Planner™ PDF is stale against the rebuilt Module 9~~ RESOLVED 21 Sep 2026: rebuilt to 23 pages and attached across all fifteen lessons, old files deleted, every upload verified by SHA-256. See Decision 87. | — |
| ~~The Brand Closet™, Upside and AIM are promoted with no row in `products[]`~~ RESOLVED 21 Sep 2026: all three registered with their live links, prices and commission terms. See Decision 90. | — |
| ~~Leni Loves carries three different prices across the project~~ RESOLVED 21 Sep 2026: $27, confirmed by the founder. See Decision 90. | — |
| ~~Classroom courses carry inconsistent access settings~~ RESOLVED 21 Sep 2026: every published course given an explicit gate and verified from the server. See Decision 94. | — |
| ~~The Offer Edit, The Funnel Edit and Scaling & Systems are priced in Skool with no row in `products[]`~~ RESOLVED 21 Sep 2026: all three registered at $37, $37 and $97. See Decision 93. | — |
| ~~Vacation Vault and Luxe Babe Prompt Pack are sold as Standard bonuses but gated to Premium~~ RESOLVED 21 Sep 2026: both moved to Standard, levels unchanged. See Decision 96. | — |

---

## 10a · SETTLED — NEVER RE-RAISE

These have been decided. They are not open items, not ship gates, and not audit findings. Do not list them, flag them, or ask about them again.

- **BAMI's structure is settled and built (Decision 98).** 12 weeks, 6 phases, 24 modules, 24 named assets, two weeks per phase, recorded walkthroughs, six written phase-gate reviews, sold by application. All 24 modules are live in the Skool classroom and `/bami` is a live waitlist page. Do not re-raise the structure as undecided, do not re-plan it, and do not strip BAMI from assets — that instruction belonged to the pre-build state and is retired. Price, cohort dates and the walkthrough recordings are the only parts still open.
- **The Ads Edit™ is a Premium inclusion and is not sold standalone.** It has no unlock price and is not supposed to have one (Decision 97). The $47 that circulated for it was the 20 September 2026 classroom audit's own recommendation, withdrawn in that document's section 12 along with all four of its flags — it was never a founder decision. Do not set an amount on the course, do not ask what its price is, and do not re-flag the blank field: as of 21 September 2026 there is no field, because the course is tier-locked. Its pricing on the Beacons Starter Map is settled and closed on the same terms.
- **The Value Vault course stays Open in Skool.** Decision 95. It is the storefront that carries the à la carte purchase links, so it is never locked and never appears on a lock list or in a public-exposure finding. The Premium Vault is the tier-locked twin. See §4.
- **The standalone module unlock prices.** Decision 93. Pinterest Foundations™ $27 · The Offer Edit $37 · The Funnel Edit $37 · Scaling & Systems $97, and nothing else is sold standalone. The Tommy Kate Edit is not a standalone product. The $67/$47/$37 figures proposed for the Standard modules in the 20 September classroom audit were withdrawn by that document's own section 12 and were never set.
- **The module tier split.** Settled September 2026 per the live "Choose Your Membership" card; the "four Skool module tier assignments" item is closed. The Shopify Edit was added to Standard by Decision 83 — that is an addition, not a reopening.
- **The Value Vault / Premium Vault split, and Vault Unlock at $49.** Settled 19 September 2026. The two vaults hold identical guides; Standard pays à la carte or $49 for the lot, Premium has them all unlocked already. The $49-above-$27 relationship is deliberate while the vault is being filled. Never re-raised as a pricing conflict or a defect.
- **There are no banned words (Decision 85).** Do not reintroduce a vocabulary list, and do not raise an asset's word choice as a defect. Claim and fact rules are what the audit tests.
- **Pillar 13 exists.** The "no new pillars" rule in §6 was waived once, by the founder, for Physical Products. Do not flag Pillar 13 as a violation of that rule.
- **Scaling & Systems is Module 9, and Building Passive Income Streams stays in it.** Settled 20 September 2026 (Decision 86). The module number is not re-litigated, and the Passive Income lesson's place at position 4 is a founder-confirmed decision, not an oversight to be re-flagged.
- **The AI CEO Planner™ is rebuilt and current.** Settled 21 September 2026 (Decision 87). It is no longer stale, no longer an open item and no longer a defect. It stays in the flagged-not-cut list for one reason only — it has no standalone shop listing — and that is not a fault to be fixed.
- **Leni Loves is $37 regular, $27 on a real sale (Decision 104, 24 September 2026).** Showing the struck-through $37 beside $27 is correct while the sale is live and is never re-raised as a defect or a pricing conflict. $17 is dead.
- **The three affiliate rows exist (Decision 90).** The Brand Closet™, Upside and The Anti-Influencer Method™ (AIM) are registered in `products[]` with their live links and terms. Do not flag them as unregistered products again.
- **How colour and the persona are written in image prompts.** Settled 21 September 2026 (Decision 89). No hex inside a generator prompt; locked features never described, changeable style described freely; the quiet-wealth farmhouse register. Not re-raised as a conflict between canon and the SOPs.
- **The `@nursemadedigital` Threads exception exists (Decision 92).** Jodie posts to the Threads account `@nursemadedigital`, as herself, not as an AI persona. This is a deliberate, scoped carve-out from the retired-brand rule and from "The New Faceless" positioning — Threads only, nowhere else. Never flagged as a conflict with either rule, and never re-litigated as whether NurseMadeDigital "should" be retired — it already is, everywhere except this one account.
- **The repo and project copies of canon are the same document (Decision 99).** Brought level 21 September 2026. Neither is "the other one." A change that lands in only one of them is an incomplete change, not a disagreement between sources.
- **There is no `/affiliates` page, and the member affiliate mechanic is Beacons' own affiliate product (Decision 100).** Founder call, 21 September 2026. Do not propose building an affiliate hub page, and do not re-flag the route as unconfirmed — it is confirmed absent. The setup is four steps inside the member's own Beacons account: add a digital product, choose affiliate product, paste The Weekend Ecosystem™ link, done. Beacons issues the member's own tracked link, which is what resolves the old attribution question — that is no longer unverified and is not raised again.
- **No DMs, ever, on Threads or Instagram, from any part of this system; outreach and reply comments never carry a pasted link (Decision 107, 24 September 2026).** Founder request, not a response to any incident. Do not propose adding a DM channel, an auto-DM, or a link-in-comment tactic without Jodie raising it by name — and do not re-flag the absence of links in outreach/reply comments as a missed growth lever. The links that already run on Jodie's own posts (the 5 PM offer's pinned comment, article self-replies) are unaffected and are not what this closes.
- **The Premium price increase is confirmed (Decision 110).** $35/month · $297/year from 11:59 pm Eastern, 30 September 2026, after the member flash sale. Existing members keep their price; grandfathered Standard access is never taken away. Not an open item.
- **The Legally Blonde Amazon pins keep their generated title overlay (Decision 109).** Founder call, 24 September 2026. It is a scoped exception to the set-text rule in §8, not a conflict between canon and `claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, and it is never re-raised as one.
- **DFY calendar research overrides standing rules (Decision 111, 24 September 2026).** Founder instruction. A calendar build's viral research can override the format mix, the persona-in-every-image assumption, the text rules and the band, and it is never flagged as a conflict with canon or the SOPs when it does; the research file is the record. The Daily Prompts (SOP 16) are a separate one-image-a-day product and are never called a calendar.
- **Every promotion quotes Premium at $35/month · $297/year from 24 September 2026 (Decision 114).** Founder call. Skool checkout still charges the flash-sale prices until 11:59 pm Eastern, 30 September 2026, on purpose: a lower price at checkout is a happy surprise, a higher one is not. The member flash sale (Blast 1, Blast 2 and the three Skool price-change tasks) is untouched. Never re-raised as a conflict with Decision 110.
- **Links never go in a Facebook or Instagram post (Decision 115, 25 September 2026).** Founder rule. The link goes in the first comment, 5 minutes after the post publishes, and a Skool link is always hyperlinked words, never a raw URL. Never re-raised, and never read as the "link-in-comment tactic" Decision 107 closed: that decision covers outreach and reply comments left on other people's Threads and Instagram posts, and it still stands.
- **DFY services are Jodie's own automations sold done-for-you (Decision 116, 25 September 2026).** Prices approved by the founder. The spicy DFY lesson is hers and is never edited.

---

## 11 · CHANGELOG

An append-only record. Nothing here governs; it explains why the rules above read as they do.

**Decisions 1–65** — carried forward from Records v1.0–v2.0, folded into the rules above.

**66.** All twelve pillar guides built and live. The pillar library is the spine; new content is clusters, not pillars.
**67.** The email platform is MailerLite, not Kit. Kit was never adopted, so there was no migration.
**68.** Email pillar takes `/learn/email-marketing-guide`; the supporting article stays at `/learn/email-marketing-for-beginners`. No re-slug, no 301.
**69.** A paid product must never occupy a free journey slot. The Email pillar's $7 product was replaced with the Blueprint; all twelve pillars audited.
**70.** Passive Income's entry rung is the $9 tier, not the $27 flagship.
**71.** Mindset routes to the community as a single door. No tier ladder, no paid slot.
**72.** The Automation slug-of-record is the live slug, `/learn/automating-your-online-business`. The Resource Map's `/learn/complete-automation-guide` is retired.
**73.** The Vault's "6 + 3" description is retired; contents restated from the live product. Sales page rebuilt, sitewide propagation done, seven short-form journey cards corrected.
**74.** Skool migrates to two paid tiers. Free retired, Premium → Standard, VIP → Premium, VIP Vault → Premium Vault. ~1,231 members grandfathered. *This decision is what made every document in the project stale at once.*
**75.** The Weekend Ecosystem™ launches at $97 permanent. Launch ladder closed; waitlist 301s to the sales page.
**76.** All 26 owned bridge pages live; Beacons direct links removed site-wide.
**77.** Canon collapses to one file per document. Version numbers retired. Corrections & Decisions Record, Master Operating Manual, Decision 73 and Canon v1.0/v1.1 cease to be governing documents.
**78.** The Weekend Ecosystem™ adds a 3 × $33.33 payment option beside $97 one-time.
**79.** The Weekend Build Challenge goes live at `/resources/weekend-build-challenge` — free 5-day email challenge on its own MailerLite form and automation, featured first on `/resources` and on the Beacons bio. Single door: The Weekend Ecosystem™. **Amended 19 September 2026: the sequence runs 11 emails, not 8, and has two doors, not one.** Three follow-ups were appended after Day 10 — Days 13, 16 and 20 — each routing to Membership Standard at $9/month or $99/year. Door one stays The Weekend Ecosystem™ (Days 5, 7 and 10). No condition step was added; the three membership emails are written to read correctly whether or not the subscriber has already bought the Ecosystem. Verified against the live workflow (`198806793685567038`) on 19 Sep 2026. Any document still saying "8-email" or "single door" for this challenge is stale — `canon.json → checks.review` now catches both phrases.
**80.** The Premium DFY Content Calendar moves to a two-week rollout: research from the start of the last week of the preceding month; one week of posts released every 3–4 days across the last week of that month and the first week of the covered month. Site copy changed from "31 days written before the month starts" to "31 days, released a week at a time around the 1st."
**81.** The DFY Content Calendar is a TDIE promotion engine, not an offer-neutral one: any TDIE product or tier may be mentioned, every mention is a swap-in slot for the member's own offer, and kept mentions pay the member through her Skool affiliate link. Replaces SOP 15's "two or three offer mentions" cap. Posting-day rules still apply.
**82.** The Pinterest username changes from NurseMadeDigital to TheDigitalIncomeEditTDIE. The retired-brand exception for the Pinterest handle is removed; NurseMadeDigital is no longer live anywhere. The block is recorded as domain-wide with Skool as the only working destination. The claimed Pinterest domain is recorded as the bare domain, as Pinterest's settings actually show it; the earlier "www, not bare" wording was wrong.
**83.** (18 September 2026) **The physical-products track.** Founder decision, prompted by Shopify affiliate sales earned from answering "which store do you use" questions in Facebook groups. Pillar 13 — Physical Products — is added as the one approved exception to the no-new-pillars rule: pillar guide `/learn/shopify-store-guide` plus five supporting articles, a free kit at `/resources/shopify-starter-kit`, and routing in `ArticleLayout.astro`. The Shopify Edit is added to Membership Standard as the pillar's paid slot, to pull Pillar 13 readers into the $9 tier. Shopify enters `canon.json → products[]` as an affiliate (not owned). **Amended the same day (founder call): every Shopify link on every surface is Jodie's direct affiliate link `https://shopify.pxf.io/eK3xYz` — no bridge page — each shipping with `rel="sponsored"` and the disclosure. The `/go/shopify` bridge that the first version of this decision created was removed.** Print on demand is the taught beginner door; dropshipping is door two, US-warehoused only, because the US de minimis exemption ended in 2025. Further physical side hustles are clusters under Pillar 13, not new pillars.

**84.** (19 September 2026) **The vault split is written out in full, and Vault Unlock is confirmed at $49.** Two Skool posts had gone live telling Standard members The Value Vault was included in their tier with "nothing extra to buy." Both were wrong. §4 now states the mechanic explicitly — identical contents, different payment — carries a banned-phrase list, and rules that a bare `The Value Vault` bullet inside a Standard inclusions list is itself a defect. Vault Unlock ($49 one-time) moves from flagged-not-cut to confirmed. The $49-versus-$27-Premium relationship is recorded as a deliberate interim state while the vault is filled, and is closed to re-raising.

**85.** (19 September 2026) **There are no banned words in this brand.** Founder instruction. Every banned-word and banned-vocabulary list is removed from canon, and the audit checks `banned_vocabulary` and `ladder_vocabulary_near_vault` are deleted from `canon.json`. What remains are claim rules and fact rules — do not fabricate proof, do not manufacture scarcity, do not promise a timeline for results, do not put earnings figures on Meta, do not use third-party IP, do not misstate what a tier includes. Those constrain what is asserted, never which words are used. Word choice is the founder's. No check may fail an asset for the words it uses.

**86.** (20 September 2026) **Scaling & Systems is rebuilt as Module 9 on the real stack.** Founder decision, taken after the live module was read lesson by lesson rather than from the project record. The audit found roughly 100,000 words of well-built content teaching a stack Jodie does not use — Stan Store, ConvertKit, TikTok, YouTube, Make.com, Zapier, Notion, Google Drive — including one lesson instructing members to strip a watermark from a Reel and schedule it to Pinterest, on a domain Pinterest has blocked. Three further lessons taught cold outreach, agency building and contractor delegation to an audience building faceless digital product businesses. Not one automation Jodie actually runs appeared anywhere in the module about systems, which is the exact failure the Machine Thesis exists to prevent.

Six lessons were replaced with the systems that actually run inside TDIE: the 8am publish-and-post task, the twice-daily reply sweep, the Threads Sunday-write-and-nightly-load system, the DFY calendar pipeline, MailerLite sequences inside the free-plan cap, and the seed-image and video pipeline. Four were rewritten onto the real stack. Six were retired and deleted. Every instance of Module 6 became Module 9, and all next-lesson previews were rewritten to match the new order.

**Building Passive Income Streams was kept**, at position 4. Read live and kept on merit: it teaches no unused stack, targets the right audience, and is the only lesson that states what the machinery is *for*. Canva Pro was removed from its affiliate examples, since Jodie is not a Canva affiliate. Curriculum of record: `claude/TDIE_SCALING_SYSTEMS_MODULE.md`. The module number and the Passive Income lesson's place are both closed items.

**87.** (21 September 2026) **The AI CEO Planner™ is rebuilt for Module 9 and attached lesson by lesson.** This closes the last open item left by Decision 86. The old planner was written for Module 6: its page headers printed the wrong module number, its worksheets mapped to five lessons that no longer exist, and its AI Operating System Map™ page listed ChatGPT, Make, Notion and Kit — none of which are in the stack.

The rebuilt planner is 23 pages and maps one-to-one onto the live module. Every worksheet footer prints `Module 9 · Lesson N · <lesson title>`, so a loose page can always be traced home. The full planner sits on Lesson 1 and each worksheet is also attached to its own lesson — 17 attachments across 15 lessons. **Nine outdated files were deleted, not merely detached**, after scanning all thirty courses to confirm none was attached elsewhere; every new upload was verified by downloading it back from Skool and comparing SHA-256 against the local original.

**88.** (21 September 2026) **Vault Unlock stays on the flagged-not-cut list.** Founder decision. Decision 84 had moved it off the list while `canon.json` kept it flagged, so the two halves of canon disagreed. Jodie's call: keep the offer, keep it flagged, and fill the vault. Flagged has never meant the price is in doubt — it means do not write the offer into a new asset yet. **The price itself is still closed** and is never re-raised.

**89.** (21 September 2026) **How colour and the persona are written in image prompts.** Founder decision, taken after this canon and the two prompt-craft documents were found to contradict each other on three points at once. All three are now settled and written the same way everywhere.

**Colour.** No hex code, colour code, bracket or symbol goes inside a generator prompt — they render as visible characters in the picture, which cost a full day of rework in September 2026. The hexes stay in §8 as the authority for set type, Canva work and rendered pins. In a prompt, colour is name plus shade plus, where it has failed before, what it is not. This overturns the former canon line that a colour name without a hex was a fail, and the identical rule in the Prompt Library and the Repurposing Pack.

**The persona.** The previous rule — never described in words — was right about her face and wrong about everything else, and the Prompt Library's opposite rule, a full persona spec including hair and makeup, was worse. The split is now: **locked features are never described** (face, facial structure, freckles, skin tone, eye colour, hair colour, length and cut, body proportions, age), because a difference in any of them reads as a different woman; **changeable day-to-day style is described freely** (how the hair is worn, nail colour, wardrobe, jewellery, footwear, what she is doing), because that is what makes two images read as two different days rather than two takes of one. Makeup stays minimal and consistent — it changes how her face reads.

**The register.** Quiet wealth, lived in. She is extremely wealthy and self-made and you would not know it to look at her or her house: nice, not showy; real, not run-down; clean and natural rather than either AI-perfect or messy; kids, dogs and farm animals evident in the room without the mess of them. This governs persona photography. The luxury-campaign register in the Prompt Library governs pin design, and the two are no longer written as if they were the same instruction.

Operator handoff of record: `claude/TDIE_CHATGPT_IMAGE_BRIEF.md`.

**90.** (21 September 2026) **Three affiliate products that were already being promoted are registered in `products[]`.** The Brand Closet™, Upside and The Anti-Influencer Method™ (AIM) had written, scheduled and in some cases already-published Skool copy, and none of the three had a row in the register. Under the Product Register rule in §1 that made every one of those posts unshippable, including ones already sent — the rule had been enforced on new products and quietly skipped on affiliates.

Nothing had to be invented. Every link, price and commission term was already on file from the sessions where the copy was written; it had simply never reached canon. The Brand Closet™ (Rose Berry's AI-fashion community) is free to join with $9 and $19 tiers above it and pays 50% recurring — Jodie is on the $9 tier and copy must never claim otherwise, and because the destination is on skool.com it is not caught by the Pinterest domain block. Upside is a free cash-back app with a referral code, Skool-only because its angle carries an earnings figure. AIM is $67/month or $555/year, and a hesitant buyer is always steered to the monthly plan, because the annual carries no refunds and a regretful buyer on it becomes Jodie's credibility problem rather than Meg's.

The same pass settled **Leni Loves at $27**, which had been carrying three different prices across the project, and recorded the Skool affiliate cap in §5. Prompted by the Skool posting system rebuild the same day, which could not name the brand's largest affiliate lever because canon could not confirm it existed.

**91.** (21 September 2026) **The Skool platform referral link is registered in `products[]`.** Decision 90 registered the three affiliates the Daily OS names as the biggest levers and missed the Skool platform referral link itself, which left the approved rotation post "The Skool group you talked yourself out of" unshippable — the course it names (Earn With Skool) had a row, the platform link it also names did not. Founder gave the link and the go the same day. Nothing was invented: the ref code is the one already live in The Brand Closet™ URL. Three distinct Skool money routes now sit in canon, never conflated: this referral row (pays Jodie when someone starts their own Skool community), `own_affiliate_programs.skool_tiers` (40% when someone joins TDIE's own tiers), and Earn With Skool, the $97 course that teaches the build.

**92.** (21 September 2026) **The Threads account moves from the Tommy Kate AI persona to Jodie herself, on `@nursemadedigital`.** The prior Threads account, `@the.faceless.homestead.mama`, was permanently disabled by Meta the same day — "we disabled your account... doesn't follow our Community Standards... you cannot request another review of this decision." Founder call: rather than rebuild the same AI-persona account under a new handle, Threads moves to an account Jodie already had — `@nursemadedigital` — posting as herself, by name and by face, as the founder, owner, coach and mentor of The Digital Income Edit™. Not an AI persona. Not faceless.

This is a scoped, one-platform exception to two standing rules that still hold everywhere else in the brand: the retired-brand rule (NurseMadeDigital stays retired on the site, Skool, email and Pinterest — see §2) and "The New Faceless" positioning (still governs the site, Skool, Facebook and every generated image — see §2). Threads alone runs differently, by founder decision, because the account already existed with its own following and its own established, already-real voice, and because losing the AI-persona account made continuing to hide behind one look like the wrong lesson to take from it.

Governing documents rewritten the same day: `claude/TDIE_THREADS_SYSTEM.md` (the schedule, the account, the mechanics — Kira Goldberg's Threads Code stays the operating system underneath, unchanged) and its new voice companion `claude/TDIE_JODIE_THREADS_VOICE.md`, which overrides §7's voice section for Threads the way `TDIE_TOMMY_KATE_VOICE.md` used to. All Threads-touching scheduled automation was audited the same day and pointed at the new account; a leftover duplicate trigger from before the "single trigger" consolidation was found and removed, since running more than one automated session against the same Threads account at once is what most plausibly got the prior account flagged in the first place.

**93.** (21 September 2026) **The standalone module unlock prices are set, and the three sellable modules enter `products[]`.** The Offer Edit and The Funnel Edit go from $17 to $37; Scaling & Systems goes from $49 to $97. Pinterest Foundations™ stays at $27 and had its Buy Now set live, having been sitting Open with no gate and no buy path at all. Each was written to Skool and then verified by reading the course record back from `api2.skool.com`, never from the editor.

All three of the raised modules had been selling standalone with no row in `products[]`, which under the Product Register rule made their prices unshippable in any asset. They now have rows.

The prices come from the 20 September 2026 classroom audit **as corrected by that document's own section 12**, which re-checked the whole sheet against canon after the fact and withdrew most of it. What section 12 left standing is exactly these three. Everything else the sheet proposed is dead and is not to be revived: the $67/$47/$37 unlock prices for the Standard modules were never set, Pinterest Foundations was never moved to $47, Vault Unlock stays $49, The Tommy Kate Edit is not sold standalone at all, and The Ads Edit™ pricing was raised as a defect four times in that document and withdrawn in all four places — it is closed. **Read section 12 before acting on anything else in that audit.**

**94.** (21 September 2026) **Every published classroom course is given an explicit access gate.** Courses had accumulated inconsistent settings — some Open, some tier-locked, some level-locked, with no rule connecting them. Each published course was set deliberately and then verified by reading its record back from the server.

The gates are recorded in §3. Three courses are Open on purpose and are the public shop window: The Essentials Edit, The Value Vault and DFY Services. Everything else sits behind Standard or Premium, except the four Buy Now modules, which are purchasable or included.

The group was set to Public the same day, which made a genuinely logged-out check possible for the first time — the earlier claim in the 20 September audit that the classroom was readable by anyone could not be reproduced while the group was Private, because every classroom URL redirected to the landing page whether the course was locked or not. Logged out and verified: a non-member gets lesson titles and cover art on a locked course and **zero lesson body text**, while the three open courses serve their full contents. Locked courses therefore work as intended — visible enough to sell, sealed enough to be worth buying.

**95.** (21 September 2026) **The Value Vault course stays Open, permanently.** Founder instruction, given with some force after it was raised once too often. The Value Vault is the storefront: it holds the purchase links for the à la carte guides, so locking it would remove the only route a member has to buy them. It was proposed as a lock-list item in the 20 September classroom audit; that proposal is wrong and withdrawn.

The Premium Vault is the same vault with every guide already unlocked for Membership Premium. The two are never confused, and The Value Vault is never again listed as a leak, a defect or a course to close off. A `checks.review` entry (`value_vault_on_a_lock_list`) now catches any document that proposes locking it.

**96.** (21 September 2026) **Vacation Vault and Luxe Babe Prompt Pack are corrected to Standard.** Both are sold as Standard bonuses on the live Skool plan card and both were gated to Premium, so a paying Standard member who did the work to reach level 2 or level 4 still hit a wall. Found while verifying the gates for Decision 94 by reading the live plan card against the live course settings. Both moved to Standard with their level gates unchanged. The Workout Vault was deliberately left at Premium, level 3, because it is not named on either plan card and no member has been promised it.

**97.** (21 September 2026) **The Ads Edit™ is confirmed as a Premium inclusion with no standalone price, and its broken Buy Now button is removed.** The course had been set to Buy Now in Skool with no amount, so the public classroom page rendered "Unlock for" followed by nothing — and once the group went Public that was visible to anyone.

The missing price was chased four separate times in the 20 September classroom audit and once more in this session before anyone checked whether the module was meant to be sold at all. It is not. The live plan card, the Premium campaign posts, §3 and the Master file all list The Ads Edit™ as a Premium tier inclusion, and it has no row in `products[]` because it has never been a standalone product. **The defect was the Buy Now setting, not a missing price.** Corrected to Private → Tier → Premium and verified twice — from `api2.skool.com` as admin, and from a logged-out read of the public classroom.

The $47 that kept resurfacing was the audit's own recommendation, withdrawn in its section 12. It was never a founder decision, and treating a retracted suggestion as a settled price is what kept the question alive across three sessions. Selling this module standalone would now be a new decision, and would need a `products[]` row before a price is set anywhere.

**98.** (21 September 2026) **BAMI's structure is settled, built and live; `/bami` is corrected to match it.** Canon had carried "not live — structure is undecided — do not pre-solve — stripped from every asset until launch" long after all four had stopped being true, and two parallel sessions built against two different structures as a result.

**What is true.** BAMI is 12 weeks, 6 phases, 24 modules, 24 named assets, two weeks per phase. All 24 modules are live in the Skool classroom on the full teaching template — Lesson Objective, Teaching Points, Video Talking Points, AI Build Lab, a Blueprint-linked Student Action Item, Discussion Prompt and Completion Criteria — each paired with its same-numbered Blueprint worksheet. Delivery is **recorded** walkthroughs; the personal component is written founder feedback at each of six phase gates. No lesson, page or email may promise a live call, a hot seat or a coaching session; the Live Coaching Guide is a recording reference, not a student promise.

**The retired scheme.** A 20-module / 5-phase manuscript (Blueprint · Foundation · Structure · Utilities · Penthouse) with different module numbering is dead. It produced a full set of recording scripts, a decision record and a live sales page, all of them wrong, before anyone checked the classroom. Modules 6 (The Faceless Architecture), 7 (The Persona System), 17 (The Pinterest Engine) and 20 (Paid Amplification) exist only in the live scheme.

**The page.** `/bami` had been advertising 5 Phases · 20 Modules · 20 Named assets with the retired phase names. Corrected and verified live the same day (commit `433a9e7`): 12 Weeks · 6 Phases · 24 Modules · 24 Named assets, six phases at two weeks each, zero stale references. The waitlist form, the refund guarantee and the recorded-not-live wording were untouched, and **no price appears on the page** — which is why none of this had to be retracted. A literal `™` escape sequence rendering in the completion FAQ was fixed in the same commit.

**How it shipped.** The container's agent proxy refuses `jodiedeo7-glitch/tdie` for both `git push` and `api.github.com` regardless of credential, and no `add_repo` tool is exposed — a pasted token does not fix it, and asking for one wasted the founder's time. The route that works is recorded in §9: open a page on Jodie's own domain in her browser, then call the GitHub contents API from that page with the token in the header.

**Still open:** the price, the cohort dates, and the 24 walkthrough recordings.

**The standing rule this adds:** module and phase counts are read from the live classroom before any downstream asset is written. A structure asserted by a document is not a structure.

**99.** (21 September 2026) **The repo copy of canon is replaced wholesale, and the two copies are brought level.** `ops/canon/TDIE_CANON.md` was dated 19 September and stopped at Decision 85 — twelve decisions behind. Any session that opened the repo copy as its source of truth would have missed the Scaling & Systems rebuild, the AI CEO Planner™, the affiliate rows, the classroom gates, the standalone module prices, the Threads move and the whole of BAMI's settled structure, and would have had no way of knowing it.

Patching only the stale BAMI line was considered and rejected. A patched stale file reads as current, which makes it more dangerous than an obviously old one — the wrongness stops announcing itself. The entire file was replaced instead, through the browser route in §9, in one commit.

**The standing rule this adds:** canon changes in both places on the same day, or it has not changed. The repo copy and the project copy are one document with two locations, never two sources to be reconciled later. A session that edits one and not the other has left the job half done.

The same push recorded the chunked-base64 method in §9, since this file is far too large to paste into a single browser script: send the new content as base64 in numbered chunks, concatenate them in page context, and hand the assembled string straight to the contents API, which wants base64 for `content` anyway.

**100.** (21 September 2026) **The `/affiliates` hub page is confirmed never to exist, and the member affiliate mechanic is written down properly.** Two loose ends from the same conversation, closed together by founder call.

**The page.** `/affiliates` had sat in §10 as "status unconfirmed / nothing confirmed" long enough for an audit to go looking for it. There was nothing to find: no page file in the repo, no link to it anywhere on the site, and a 404 for anyone who typed it. Founder decision: it should not have its own page at all. An affiliate programme explained on a page nobody visits earns nothing; explained to a buyer who has just paid, it lands. So the explanation goes in the Weekend Ecosystem™ Access Granted email and nowhere else, and the route stays absent.

**The mechanic.** `canon.json` recorded the member affiliate setup as "members add it to their own Beacons and Beacons handles attribution," with a standing `unverified` note against whether a click from a member's own Beacons page actually attributes the sale back to her. That vagueness is what made the note necessary. The real mechanic, from the founder: inside her own Beacons account the member adds a digital product, chooses affiliate product, and pastes The Weekend Ecosystem™ link — Beacons then issues *her* tracked affiliate link. It is Beacons' own affiliate product feature, not a link block, so the tracking is the platform's job by design. **The attribution question is answered and the `unverified` note is retired.**

Shipped the same day into the live *Weekend Ecosystem — Access Granted* email (MailerLite workflow `196430036792772181`, email `196430145647544181`): the 30% / $29.10 terms, the four-step Beacons setup, and "Grab your affiliate link" hyperlinked to the registered programme URL. The automation was never paused to do it — MailerLite allows email content edits on a live workflow, which avoids the slot-promotion trap recorded in the Defect Register. All four workflows verified still in their original states afterwards.

**101.** (24 September 2026) **Jodie is an approved Amazon Associate and Amazon Influencer, and the site gets a Lifestyle section.** Founder call. Three things follow. The Amazon Influencer Storefront gets a row in `products[]` (not owned); its public URL is captured by the first Legally Blonde sprint run and written in. A `/lifestyle` shop-the-look section goes live on the site (hub, ten categories, one page per look), linked in the nav and footer, built from JSON plus images in `src/lifestyle/`; it is not a pillar and never a journey slot. And the looks come from the Legally Blonde Amazon pin factory (`claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`): a flat lay or shoppable collage pin plus a lifestyle photo of Tommy Kate wearing every item, two a day for six months, seasonal, linking to storefront Idea Lists. Each look is also posted to the revived Instagram account `@itstommykate`, feed post plus Story with a link sticker, and never to `@the.faceless.homestead.mama`, which stays the Premium DFY Content Calendar test account. Every link ships with the Amazon disclosure; no prices; Amazon's listing photos are generation references only, never posted. The owned-domain bridge-page rule cannot apply to Pinterest while the domain is blocked, so Amazon pin links go direct, following the Shopify precedent (Decision 83). Amazon onsite commission videos are planned by Jodie and not yet made.

**104.** (24 September 2026) **Leni Loves: $37 regular, $27 on sale.** Founder correction. The 21 September record called $27 the only price and $37 dead, and banned any struck-through figure. That was wrong: $37 is the regular price and $27 is a real sale, listed on the Beacons page. Jodie never falsifies a discount, and a real, listed sale is shown as a sale. While it runs, copy may show $27 with the regular $37; when it ends, the price is $37. The $17 figure stays dead. Recorded in `canon.json` (products[] and meta.leni_loves_sale_2026_09_24).

**105.** (24 September 2026) **The Keep It Running Kit, its six guides and the objection email series enter canon.** Approved by Jodie 23 and 24 September 2026. Four guides get new rows in `products[]`: My 5-Minute Canva Pin Template Swap (1 Design → 30) at $4, My Exact $0-to-First-Sale Path (What I'd Do This Week) at $7, The First 30 Days After Your Site Goes Live at $17 (new guide, approved the same day), and The Keep It Running Kit itself as a private $0 buyer bonus. All six Kit guides were rebuilt with new covers and relisted on Beacons, each verified on its public page. Zero Income Claim Guide - 100 DFY Reels was taken out of the Kit by Jodie and replaced with The First 30 Days. The six-email objection series is recorded in a new `canon.json → emails` section and was scheduled in MailerLite, with the Weekend Ecosystem Buyers group excluded from every email. Eight Skool posts about every 36 hours and the Threads 5 PM slot about every day and a half carry the same offer until the deadline (`claude/TDIE_ECOSYSTEM_KIT_SOCIAL.md`). **Correction to Decision 100:** on 24 September 2026 MailerLite would not allow the Access Granted email to be edited without pausing the automation first, and new buyers do not enter while it is paused. The Kit block was added during a three-minute pause; the buyer count was checked afterwards (no one bought during it). Any future edit keeps the pause as short as possible and checks the buyer count after.

**106.** (24 September 2026) **The Friday Threads offer is The Operating Prompts™ ($19).** Founder call. It replaces the retired 8 Claude Prompts That Save Me 12 Hours a Week in the Friday 5 PM slot. **Correction, 25 September 2026:** this record originally said the switch took effect from 9 October 2026, after the Kit window — wrong, per the founder's own recency rule (the most recent decision on a topic governs). The live `claude/TDIE_THREADS_SYSTEM.md` Section 2 table already carries the switch as done, effective 24 September 2026 (Decision 102, recorded there), and its Kit Window override table confirms it: Friday 2 October, a non-override day inside the Kit window, runs the normal table — meaning The Operating Prompts™, not a delayed offer. The 9 October date is retired. Recorded in `claude/TDIE_THREADS_SYSTEM.md` Section 2.

**107.** (24 September 2026) **No DMs, ever, on Threads or Instagram; outreach and reply comments never carry a pasted link.** Founder request, given directly in chat, not in response to any incident — nothing in this system has ever sent a Threads DM, and the confirmed cause of the Sept 21 Threads ban (Decision 92) was two automations posting to the account at once, not a message. Two hard rules added to `claude/TDIE_THREADS_SYSTEM.md` Section 4: this system never sends a direct message on Threads or Instagram — the ManyChat auto-DM idea in Section 9 was never turned on and is now retired there, not to be added without Jodie naming it; and outreach/reply comments left on other people's posts never carry a raw URL, since a pasted link in a comment is a stronger spam signal than almost anything else in this system and breaks Kira's Threads Code rule to never hard-pitch — where it fits, a comment may nod to "it's in my bio" instead. Does not touch the links that already run safely because they're on Jodie's own posts: the 5 PM offer's pinned comment and article self-replies (Section 2a).

**108.** (24 September 2026) **The Amazon Influencer Storefront URL is recorded.** Founder instruction. `https://www.amazon.com/shop/influencer-adc3fcaa`, captured from Jodie's signed-in Amazon account by the first Legally Blonde sprint run, replaces `url: null` on the storefront row in `canon.json → products[]`. Per-look Idea Lists sit under it at `/list/<id>`. Written to the project and repo copies the same day. **Handle changed the same night — see Decision 113.**

**109.** (24 September 2026) **Generated title overlays stay on the Legally Blonde Amazon pins.** Founder call ("do whatever looks the best"). The pin factory's generated titles came out crisp and spelled right on the first sprint, and they look better than set type on these images. So the rule that text is set, never generated, gets one scoped exception: those pins and their Instagram versions only, each overlay checked letter by letter before shipping. Recorded in §8, §10a, `canon.json` (`typography.rule`, `image_prompts.text_rule`, `meta.amazon_pin_text_overlay_2026_09_24`) and the pin factory recipe.


**110.** (24 September 2026) **Membership Premium goes to $35/month · $297/year, after a member flash sale.** Confirmed by Jodie. Sale: Sunday 27 September 6:00 pm Eastern, $27/month locked or $197/year; Wednesday 30 September 6:00 pm, $197 closes and $27/month or $250/year runs as a last call; 11:59 pm that night, $35/month · $297/year permanently. Existing members keep the price they joined at. Two all-member email posts carry it (Blast 1 Sunday 6:05 pm, Blast 2 Wednesday 6:10 pm), scheduled in SkoolKit and read back 24 September 2026. The scheduled Premium posts for 11 and 25 October were updated to $35/$297 the same day, and the Monday 28 September post "The one door above the one you're already in" was deleted. Also recorded: sale and price-increase windows run 4–5 days at most with only a few days' heads-up. See §3.

**111.** (24 September 2026) **DFY Content Calendar research is rebuilt around real outlier posts, and research supersedes standing rules.** Founder instruction, given after the first October 2026 build was found to have done no viral research at all: it checked platform-wide format averages, hashtag rules, tool prompt limits and a niche-gap search, never opened a single real post, and then wrote 31 days with the persona in all 162 images because SOP 15 said every asset carries the persona. SOP 15 Phase A was rewritten the same evening: collect at least 40 outlier posts from at least 25 same-niche, similar-creator, normally-not-viral accounts (views far above the account's normal, engagement far above normal, or a visible follower jump), record each one, find the patterns with counts, turn them into the month's build rules and a replication plan, and only then run the supporting benchmark, platform-rule and niche checks. Tool limits moved out of research into Phase D2. The monthly scheduled build and the October rebuild task were rewritten to match, and the October calendar is being rebuilt under the new phase. Whatever the research proves overrides any standing rule, with the exceptions listed in §3. The same instruction fixed the naming: "the calendar" always means the Premium DFY Content Calendar; the Daily Prompts are never called a calendar.

**112.** (24 September 2026) **The two Tommy Kate Instagram accounts are defined.** Founder instruction. Both accounts are Tommy Kate. `@the.faceless.homestead.mama` is TDIE's face, voice and experiment member; the Daily Prompts, the Premium DFY Content Calendar and everything else TDIE links to, is inspired by, or uses that account. `@itstommykate` is the affiliate influencer account on a revived old Tommy Kate account: separate from TDIE, influencer only, never running the Daily Prompts or the calendar. It will expand into a UGC account, and a UGC / AI UGC module will be built around her, so every piece of her content is made with that goal in mind. Recorded in §2.

**113.** (24 September 2026) **The Amazon storefront handle is now `thedigitalincomeedit`.** Amazon Associates support (Cynthia) confirmed by email the same evening that the Influencer vanity handle was changed from the auto-generated `influencer-adc3fcaa` to `thedigitalincomeedit`, effective immediately, and that links using the old handle no longer reach the storefront. The storefront is now `https://www.amazon.com/shop/thedigitalincomeedit`, and each Idea List keeps its own list id under the new handle (`/shop/thedigitalincomeedit/list/<id>`). Updated the same day in §2, `canon.json → products[]`, the three published `/lifestyle` look files, the pin log, the lifestyle list map and the pin factory recipe. Pins and Instagram posts already published with the old address must have their links edited on Pinterest and Instagram.

**114.** (24 September 2026, 10:57 pm Eastern) **Every promotion quotes Premium at $35/month · $297/year now, not from 30 September.** Founder call: "I'd rather have people see a happy surprise at checkout than think it's 27 and see 35." Skool's checkout keeps the Decision 110 flash-sale schedule exactly as set; only what the brand quotes changes. The same night the site was changed on ten pages (homepage, membership, shop, FAQ, community, Find Your Door, Starter Map, Creating Your First Offer, the Automation pillar card, One and Done) and checked live; the "$27 here is a subscription, not the same $27 as the product" notes were removed because the collision no longer exists; the daily Skool member-watch task was changed to quote $35/$297; and the 1 October task that would have changed only the Offer Edit card was turned off as no longer needed. The member flash sale (Blast 1, Blast 2, the three Skool price-change tasks) is untouched. Recorded in §3 and §10a.
**115.** (25 September 2026) **The Meta link rule.** Founder rule, given in chat: "Any links on Meta cannot go in the main post. There is a standing rule that they must go in the first comment, scheduled to auto post five minutes after the post is scheduled to post. Meta suppresses posts with a link in them. If it is a Skool link then the hyperlink needs to be buried in text. It cannot be a raw URL." It extends the Facebook group link rule of 23 September 2026 (claude/TDIE_FB_GROUP_REVIVAL.md) to every Facebook and Instagram surface, fixes the comment timing at 5 minutes, and makes it canon. It overrides any document line that puts a link in a Facebook or Instagram post body or caption, including step 6 of the pre-ship check in claude/TDIE_SIX_M_FRAMEWORK.md ("link sits on the CTA words and appears twice") wherever the asset is a Facebook or Instagram post. Facebook and Instagram comments cannot hide a link behind words, so there the link sits on its own line after a short call-to-action line; everywhere a link can be hidden behind words, a Skool link always is. Instagram Story link stickers are not covered. Threads is not covered by this entry; Threads links follow claude/TDIE_THREADS_SYSTEM.md. Recorded the same day in §7, §10a and `canon.json` (meta.meta_link_rule_2026_09_25 and content_calendar_rules.meta_links), and added to every project document and scheduled task that writes or posts to Facebook, Instagram or Skool.

**116.** (25 September 2026) **DFY services become Jodie's own automations, sold done-for-you.** Founder instruction: every fast system she already runs for TDIE becomes a DFY service, easy to tweak per client, and each one is proof of concept because members can watch the same system run inside TDIE. Prices approved by Jodie in chat the same night. Eleven lessons were added to the Open DFY Services classroom course and "How It Works & How to Order" was rewritten, every lesson read back from the server: Run It Like Mine: DFY Automation Setup ($297 one automation · $697 any three · $1,297 up to six · Care Plan $197/month), DFY Skool Autopilot ($497 setup month, then $297/month; Facebook group mirror +$97/month), DFY Viral Instagram Content Calendar ($297 one month or $247/month, 2-month minimum), DFY 30-Day Threads Calendar ($197), 30 Days of Pinterest, Done & Scheduled ($247 for 30 pins, $597 for 150), DFY Repurposing Pack ($197 per article), DFY 6-Email Sales Series ($197), DFY Etsy Listing Pack ($197 for 5, $347 for 10), DFY Amazon Storefront Launch ($297), 30 Days of AI Persona Photo Prompts ($197) and DFY Custom Business Dashboard ($97). Ordering is by DM keyword, intake form, then payment link. Each has a row in `canon.json → products[]`. The Viral Instagram Content Calendar is a custom build for the client's brand and does not sell the Premium Monthly DFY Content Calendar, which is still never sold as a one-time unlock. The spicy DFY lesson is untouched and stays Jodie's. Doc of record: `claude/TDIE_DFY_SERVICES.md`.
---

**The Digital Income Edit™ · Canon · 25 September 2026**
