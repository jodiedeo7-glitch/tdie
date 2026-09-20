# THE DIGITAL INCOME EDIT™ — CANON
### Current · 19 September 2026 · Single live copy — no versioned predecessors

**Build Your Business Backwards. Scale It Forward.™**

**What this is.** The one governing document for the brand. It replaces Canon v1.0 and v1.1, the Corrections & Decisions Record (all versions), Decision 73 as a standalone file, and the Master Operating Manual v3.0 "Final." Those documents are retired as governing texts. Their decisions survive here as standing rules; their reasoning survives in the Changelog at the end.

**The machine half.** Every enforceable fact below also lives in `canon.json`, which `tdie_audit.py` reads. A price or rule changes in both files on the same day. A rule that is not in `canon.json` is enforced by memory only, which means it is not enforced.

**No more version numbers.** There is one Canon, one `canon.json`, one Resource Map, one SOP Library, one Prompt Library, one Daily OS, one Defect Register. When a document changes, it is edited in place and dated. The version rule that used to say "highest number wins" is retired because there are no longer two numbers to compare.

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
| **Retired brand** | `nursemadedigital.com` and the NurseMadeDigital name. Everything runs under The Digital Income Edit™. Nurse-forward naming risks brand drift. There are no exceptions: the Pinterest username was changed to `TheDigitalIncomeEditTDIE` (September 2026), so NurseMadeDigital is no longer a live handle anywhere. |
| **Repo** | `jodiedeo7-glitch/tdie` — Astro on Vercel |
| **Article route** | `/learn/[slug]`, flat. `/blog/` is retired as segment, label and page-type name. |
| **Community** | Skool · `skool.com/thedigitalincomeedit` · Tiers pricing model |
| **Shop** | Beacons · `links.thedigitalincomeedit.com` — not fetchable, not indexed, unverifiable by tooling |
| **Email** | MailerLite. Env vars: `MAILERLITE_GROUP_ID` (buyers), `MAILERLITE_WAITLIST_GROUP_ID` (waitlist), `MAILERLITE_BAMI_WAITLIST_GROUP_ID`. Kit was never adopted. |
| **Analytics** | Vercel Web Analytics, site-wide |
| **Pinterest** | Username `TheDigitalIncomeEditTDIE` (changed from NurseMadeDigital, September 2026 — `pinterest.com/Nursemadedigital` is now a dead link). **Pinterest blocks every URL on Jodie's domains** — confirmed across www, learn and links. Three appeals were auto-denied. Skool links are the only working Pinterest destination until Jodie says otherwise. The claimed website in Pinterest settings is the bare `thedigitalincomeedit.com` (checked in Pinterest, 16 September 2026); the profile website field shows `www.thedigitalincomeedit.com` as verified. Leave both as they are. Do not edit bio metadata or unclaim the domain until the block resolves — a blocked domain may not be re-claimable. |
| **Meta Pixel** | ID ends `...031...` — digit 9 is a THREE. Never "correct" it to `...051...`. |
| **Tool stack** | Astro · Vercel · GitHub · Skool · Beacons · Canva · Claude · MailerLite · Pinterest native. Nothing outside this list. |

**The New Faceless.** Faceless means the founder's real face is never required — not that no person appears. The brand's face is its AI persona, referenced only by the canonical seed image at `/public/images/library/avatar-seed-omni-reference.png` as "this exact woman." **Never described in words.** Attach the seed image to every generation prompt.

**Positioning thesis.** Jodie is the master of the AI-built faceless business — the complete machine, built backwards. Mechanism pairing: AI + architecture. **Proof is the business itself, not income screenshots.**

**The physical-goods door (Decision 83).** A Shopify store selling print-on-demand or dropshipped products is the same machine with a physical product in the offer slot — product first, store second, fulfilment app third, buyers last. It is one pillar inside the same house, in the same voice, never a second brand, a second community, or a headline identity. Print on demand is the beginner door; dropshipping is door two and only with US-warehoused or same-country suppliers, because the US de minimis duty exemption ended in 2025 and China-direct parcels now carry duties.

---

## 3 · THE LADDER

| Product | Price | Platform |
|---|---|---|
| **Membership Standard** — The Value Vault is available to Standard members à la carte, or in full via Vault Unlock ($49 one-time); it is **not** included in the tier | $9/month · $99/year | Skool |
| **Membership Premium** — includes The Ads Edit™ and the monthly DFY Content Calendar, unlocks The Premium Vault | $27/month · $250/year | Skool |
| The Business Architect Mentorship Intensive™ (BAMI) | ⬜ pending | Skool |

**Both tiers carry a 7-day free trial.**

**No refunds on any digital product.** Stated once on `/faq`, never repeated per-product.

**The free tier is permanently retired.** Never reference "Free Community," "Free tier," or a $0 Skool rung again. Approximately 1,231 members were grandfathered in from the prior free tier.

**Renames in force:**

- `Membership Premium ($9)` → **Membership Standard**
- `Membership VIP ($27)` → **Membership Premium**
- `The VIP Vault` → **The Premium Vault**

**Skool at $17/month never existed.** Any asset printing $17/mo is wrong.

**Module tier split (settled September 2026, per the live "Choose Your Membership" card).** Standard: The Essentials Edit, AI Foundations for Creators, Canva Crash Course, AI Twin / Influencer Creation, The Monetization Edit, Brand Building & Brand Identity, The Content Edit, The Email Edit, The Pinterest Edit, The Tommy Kate Edit, Daily Prompts, Vacation & Luxe Babe Vault bonuses — **and, from 18 September 2026, The Shopify Edit (Decision 83).** Premium: everything in Standard plus The Offer Edit, The Funnel Edit, The Ads Edit™, Scaling & Systems, Monthly DFY Content Calendar, The Premium Vault.

**The Shopify Edit** — Standard module, the full physical-products build lesson by lesson (store, supplier app, product page, first ten sales). Curriculum of record: `claude/TDIE_SHOPIFY_EDIT_MODULE.md`. **LIVE in Skool (18 Sep 2026):** classroom course id `3f764e2e2cbe49e284a2e3f9244f4592` (URL slug `886389d5`), all 10 lessons published, gated to Standard by default (created with the same access profile as The Essentials Edit, so every member with at least Standard sees it). **Cover image set and verified live (18 Sep 2026):** the blush-gradient "THE SHOPIFY EDIT" cover matching the house module-cover style (`cover_image_file` `02336f92102844668de5b82e6ee6bf8d`). It is the paid slot for Pillar 13 on the site.

**BAMI** supersedes the retired name Faceless Income Intensive™. It is **not live**, sold by application, third Skool tier card toggled off and reserved. Structure is undecided — **do not pre-solve.** Stripped from every asset until launch.

**BAMI graduates receive The Weekend Ecosystem™ free on completion** — earned at completion, never "included with BAMI." Stated on `/bami` before application. Applies retroactively to the founding cohort.

**The Premium Monthly DFY Content Calendar** — 31 days of Instagram content delivered as a Skool classroom module. **Two-week rollout:** research starts at the beginning of the last week of the preceding month; the calendar is released one week of posts at a time, every 3–4 days, across the last week of the preceding month and the first week of the month it covers, so each week is tested and scheduled before it runs. Never promise the whole month "before the 1st." Premium only, and the primary reason Premium exists over Standard. **Purpose:** the calendar organically promotes The Digital Income Edit™ and its paid tiers — anything inside TDIE is fair game. Every offer mention is written as a swap-in slot, so a member can run her own offer or keep the TDIE mention and earn through her Skool affiliate link. Process: SOP 15.

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

Thirty-four rows with exact prices and live URLs: **`canon.json → products[]`.**

**Price collisions.** `tdie_audit.py` computes the collision table from `canon.json` on every run, so it cannot go stale. Wherever two products share a price on one screen, the copy names what each price buys before the reader has to work it out.

**Exact prices. Never `from $`.** Applies to owned products only. Changed deliberately, everywhere, on one day.

**Affiliate commission — two separate rates, not a conflict.** 40% on Skool tiers · 30% on The Weekend Ecosystem™.

**Affiliate.** The link, `rel="sponsored"`, and the disclosure ship as a set or not at all. Never quote a sale price on a product you don't own — publish list price. Verify quarterly that each still exists. **Affiliate products never occupy a pillar's paid slot.**

**Shopify (affiliate, Decision 83, amended 18 September 2026).** Registered in `products[]` as not owned. **Every Shopify link on every surface — site, Skool, email, Facebook — is Jodie's direct affiliate link `https://shopify.pxf.io/eK3xYz`. There is no bridge page.** Founder call: the link that ships is always the direct one. Wherever it appears it travels with `rel="sponsored"` and the affiliate disclosure as a set (Standing Rule 18) — the journey card and the inline article links both carry the disclosure, and on Facebook the disclosure sits in the comment beside the link. No earnings figures ever appear on a Meta surface. Shopify's offer as of 18 September 2026: 3-day free trial, then $1/month for 3 months (monthly billing), then Basic at $39/month monthly or $29/month annual. Shopify's prices, subject to change — verified quarterly with the other affiliates.

**Flagged, not cut.** Named in canon, no confirmed live listing. Do not write into an asset until confirmed: Luxe Babe Prompt Pack · Vacation Vault™ · Workout Vault™ · AI CEO Planner™ (confirmed as a Module 6 companion asset; no confirmed standalone listing) · DFY Pinterest packages · Pinterest Traffic Engine™.

**Vault Unlock — $49 one-time.** Confirmed by Jodie 19 September 2026 and moved out of the flagged list. It buys a Standard member the entire Value Vault in one payment instead of guide by guide. See §4.

---

## 6 · SITE ARCHITECTURE

**Navigation:** `HOME · LEARN · SHOP · FREE RESOURCES · ABOUT · CONTACT`
Utility, top-right: `Search · Member Login · Join the Membership`

**Learn is the sole educational hub.** There is no Blog section, no `/blog/` segment, no "blog post" as a page-type name. Blogging survives as a *topic*, not a section.

**Routes:** `/` `/learn/` `/learn/[slug]` `/shop/` `/resources/` `/about/` `/contact/` `/membership/`
No dates in URLs. Short descriptive slugs only.

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

**Two registers, never mixed.** Skool community posts: warm, casual, emoji-forward, peer-to-peer, short lines, heavy white space. Site and editorial: luxury editorial mentor.

**Income and earnings claims** are permitted on every surface **except Meta platforms** (Facebook and Instagram). This includes any page a Meta ad can reach. The Shopify affiliate figure Jodie has earned from Facebook replies is never quoted in a Facebook reply, a Facebook group post, or an Instagram post.

### Content calendar rules

- No membership tier content Tuesday–Thursday.
- Pretty & Paid PLR Vault™ promotes Wednesday only.
- Vault and membership posts never share a day and never sit on adjacent days.

---

## 8 · DESIGN

**Palette — exact hex, mandatory in every image prompt. A colour name without a hex is a fail.**

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

**Aesthetic.** "Her real life, shot beautifully" — lived-in modern farmhouse, real slow country life. Not staged, not costume cottagecore, **and not a penthouse skyline.** Wardrobe locked: oversized pink knits, soft tees, hoodies, sweatpants, leggings, fuzzy socks, gold claw clip. Blouses, blazers and costume cottagecore are banned. Signature prop: glitter-flecked pink iced coffee tumbler with lavender straw, in every frame with her.

**Hard third-party IP ban** in every generated image, prompt, listing and asset. No characters, no logos, no branded handbags, no film or franchise likenesses. This has already caused platform deactivations. The same ban governs every product design example in the physical-products track: no cartoon characters, team logos, band names or memes, and recolouring does not make them safe.

**Rendering.** Pins render at 2× (2000×3000) then downsample to 1000×1500 via LANCZOS. Direct Python/Pillow is faster and more reliable than browser-based Canva automation at scale. Canva is retained for carousels, lead magnets, Skool graphics and product mockups.

**Every visual asset is self-audited at feed and thumbnail scale and fully optimised before delivery.** Never ship a first pass and offer to improve it afterward.

---

## 9 · SECURITY

**Classic personal access tokens, never fine-grained.** Test immediately before use. **Generated fresh per session, scoped to the single repo, and revoked when the session ends** — not soon, not at end of day. Revocation confirmed in the GitHub UI.

Weekly: zero live tokens. Any survivor gets revoked **and the reason it survived gets recorded.** The record is the deliverable; the revocation takes ten seconds.

`history -c 2>/dev/null; unset GH` after every session. Working copies removed with `rm -rf`.

**Commit pattern:** fetch HEAD SHA → get base tree SHA → create blobs → POST new tree with `base_tree` → POST new commit → PATCH ref. Delete a file by including its path in the tree with `"sha": null`. Binary files base64-encoded in the blob payload. Raw content via the `Accept: application/vnd.github.raw` header. Repo tarball beats paginating the contents API for full audits.

**Always verify live state before committing.** The project file copy is not ground truth.

---

## 10 · WHAT IS OPEN

Decisions and dependencies, not process. No amount of correct execution resolves them.

| Item | Blocks |
|---|---|
| Both Blueprint lead magnets are materially wrong — see the Defect Register | Every opt-in currently running |
| The One & Done sales page carries third-party IP and income projections | The $27 product's entire funnel |
| Skool cover image carries fabricated earnings and a branded handbag | The community's first impression |
| BAMI price, structure and live URL — provisional thinking only (beta around $297, launch around $1,497, then scale on results); nothing is final and none of it goes into an asset | The ladder's top rung |
| Value Vault ledger count | Every "total value" claim in Vault marketing |
| Pinterest domain unblock | Pinterest Traffic Engine™ |
| Nineteen live shop products routed to no pillar | Nineteen assets earning nothing from site traffic |
| Per-pillar freebies replacing the shared Blueprint fallback — pattern now proven on Pillar 13 (dedicated MailerLite form → pillar group → delivery automation, single opt-in); the other twelve pillars still share `TDIE Freebie Capture` | Welcome-sequence segmentation |
| `tdie_audit.py` GitHub Actions deploy — token missing `workflow` scope | The Friday automated audit |
| Sneak-peek PDF in `public/` is publicly reachable and bypasses the email gate | Every opt-in that PDF was built to earn |
| Inactive *WAITLIST* product in Beacons | Nothing — but it carries the retired domain |
| `/affiliates` hub page — status unconfirmed | Nothing confirmed |
| Product and FAQPage JSON-LD on `/shop/weekend-ecosystem`; public `/weekend-ecosystem/curriculum` page | Search indexing of the flagship |
| EverAds Standard-tier campaign — 60 creatives selected, generation not triggered | Standard acquisition |
| Fourthwall merch — awaiting designs, retail pricing, collection name | The merch component of Meta ads |
| ~~Pillar 13 site files written and building locally; not yet committed~~ RESOLVED 18 Sep 2026: pillar guide, five cluster articles, kit capture page and Standard tier listing all committed and live on `www.thedigitalincomeedit.com` (verified) | — |
| ~~The Shopify Edit module — not yet loaded into Skool~~ RESOLVED 18 Sep 2026: all 10 lessons live in the classroom, course id `3f764e2e2cbe49e284a2e3f9244f4592` | — |
| ~~The Shopify Starter Kit — kit PDF needs producing and wiring to delivery~~ RESOLVED 18 Sep 2026: 5-page editorial PDF produced, hosted in MailerLite, and delivering live. First **per-pillar** freebie: the kit page (`/resources/shopify-starter-kit`) posts to a dedicated MailerLite form (id `198982894072366185`, single opt-in) that adds subscribers to the **Physical Products** group; the active automation *Shopify Starter Kit — Delivery* emails the kit on group-join. End-to-end tested (a test opt-in completed the automation). | — |

---

## 10a · SETTLED — NEVER RE-RAISE

These have been decided. They are not open items, not ship gates, and not audit findings. Do not list them, flag them, or ask about them again.

- **The Ads Edit™ pricing on the Beacons Starter Map.** Settled. Any document still describing this as open is stale, and the correct action is to delete that line, not to re-flag it.
- **The module tier split.** Settled September 2026 per the live "Choose Your Membership" card; the "four Skool module tier assignments" item is closed. The Shopify Edit was added to Standard by Decision 83 — that is an addition, not a reopening.
- **The Value Vault / Premium Vault split, and Vault Unlock at $49.** Settled 19 September 2026. The two vaults hold identical guides; Standard pays à la carte or $49 for the lot, Premium has them all unlocked already. The $49-above-$27 relationship is deliberate while the vault is being filled. Never re-raised as a pricing conflict or a defect.
- **There are no banned words (Decision 85).** Do not reintroduce a vocabulary list, and do not raise an asset's word choice as a defect. Claim and fact rules are what the audit tests.
- **Pillar 13 exists.** The "no new pillars" rule in §6 was waived once, by the founder, for Physical Products. Do not flag Pillar 13 as a violation of that rule.

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

---

**The Digital Income Edit™ · Canon · 19 September 2026**
