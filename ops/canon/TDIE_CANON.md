# THE DIGITAL INCOME EDIT™ — CANON
### Current · 1 September 2026 · Single live copy — no versioned predecessors

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
| **Retired brand** | `nursemadedigital.com` and the NurseMadeDigital name. Everything runs under The Digital Income Edit™. Nurse-forward naming risks brand drift. **The one exception is the Pinterest handle**, which is the live account name and cannot be changed — it is not a licence to use the name anywhere else. |
| **Repo** | `jodiedeo7-glitch/tdie` — Astro on Vercel |
| **Article route** | `/learn/[slug]`, flat. `/blog/` is retired as segment, label and page-type name. |
| **Community** | Skool · `skool.com/thedigitalincomeedit` · Tiers pricing model |
| **Shop** | Beacons · `links.thedigitalincomeedit.com` — not fetchable, not indexed, unverifiable by tooling |
| **Email** | MailerLite. Env vars: `MAILERLITE_GROUP_ID` (buyers), `MAILERLITE_WAITLIST_GROUP_ID` (waitlist), `MAILERLITE_BAMI_WAITLIST_GROUP_ID`. Kit was never adopted. |
| **Analytics** | Vercel Web Analytics, site-wide |
| **Pinterest** | Handle `NurseMadeDigital` (the username `thedigitalincomeedit` was unavailable). **Pinterest has blocked all of Jodie's domains, not just this one.** Appeals returned automated denials. Claimed domain form is `https://www.thedigitalincomeedit.com` — not `http://`, not bare. Do not edit bio metadata until the appeal resolves. |
| **Meta Pixel** | ID ends `...031...` — digit 9 is a THREE. Never "correct" it to `...051...`. |
| **Tool stack** | Astro · Vercel · GitHub · Skool · Beacons · Canva · Claude · MailerLite · Pinterest native. Nothing outside this list. |

**The New Faceless.** Faceless means the founder's real face is never required — not that no person appears. The brand's face is its AI persona, referenced only by the canonical seed image at `/public/images/library/avatar-seed-omni-reference.png` as "this exact woman." **Never described in words.** Attach the seed image to every generation prompt.

**Positioning thesis.** Jodie is the master of the AI-built faceless business — the complete machine, built backwards. Mechanism pairing: AI + architecture. **Proof is the business itself, not income screenshots.**

---

## 3 · THE LADDER

| Product | Price | Platform |
|---|---|---|
| **Membership Standard** | $9/month · $99/year | Skool |
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

**BAMI** supersedes the retired name Faceless Income Intensive™. It is **not live**, sold by application, third Skool tier card toggled off and reserved. Structure is undecided — **do not pre-solve.** Stripped from every asset until launch.

**BAMI graduates receive The Weekend Ecosystem™ free on completion** — earned at completion, never "included with BAMI." Stated on `/bami` before application. Applies retroactively to the founding cohort.

**The Premium Monthly DFY Content Calendar** — 31 days of Instagram content delivered as a Skool classroom module, published before the first of the month it covers. Premium only, and the primary reason Premium exists over Standard. Process: SOP 15.

**Pinterest Foundations™** — Standard module, also purchasable standalone at $27. **All Skool modules unlock inside Skool.** No separate checkout page exists for any module, and none is to be built.

**The Weekend Ecosystem™** — $97 one-time, permanent price, 22 modules, delivered as a live website. The launch price ladder is closed; the waitlist page 301-redirects to the sales page. All future updates included free, forever.

---

## 4 · THE THREE VAULTS — NEVER CONFLATED

| Name | What it is |
|---|---|
| **The Value Vault** | Individually priced guide collection inside Skool. Never called "PLR Vault" alone. |
| **The Premium Vault** | The Value Vault unlocked in full for Premium members. |
| **Pretty & Paid PLR Vault™** | Separate $11/month Beacons subscription. Off-ladder. |

Three distinct products. Never conflated, never renamed, never merged.

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

Thirty-one rows with exact prices and live URLs: **`canon.json → products[]`.**

**Price collisions.** `tdie_audit.py` computes the collision table from `canon.json` on every run, so it cannot go stale. Wherever two products share a price on one screen, the copy names what each price buys before the reader has to work it out.

**Exact prices. Never `from $`.** Applies to owned products only. Changed deliberately, everywhere, on one day.

**Affiliate commission — two separate rates, not a conflict.** 40% on Skool tiers · 30% on The Weekend Ecosystem™.

**Affiliate.** The link, `rel="sponsored"`, and the disclosure ship as a set or not at all. Never quote a sale price on a product you don't own — publish list price. Verify quarterly that each still exists. **Affiliate products never occupy a pillar's paid slot.**

**Flagged, not cut.** Named in canon, no confirmed live listing. Do not write into an asset until confirmed: Luxe Babe Prompt Pack · Vacation Vault™ · Workout Vault™ · AI CEO Planner™ (confirmed as a Module 6 companion asset; no confirmed standalone listing) · Vault Unlock ($49) · DFY Pinterest packages · Pinterest Traffic Engine™.

---

## 6 · SITE ARCHITECTURE

**Navigation:** `HOME · LEARN · SHOP · FREE RESOURCES · ABOUT · CONTACT`
Utility, top-right: `Search · Member Login · Join the Membership`

**Learn is the sole educational hub.** There is no Blog section, no `/blog/` segment, no "blog post" as a page-type name. Blogging survives as a *topic*, not a section.

**Routes:** `/` `/learn/` `/learn/[slug]` `/shop/` `/resources/` `/about/` `/contact/` `/membership/`
No dates in URLs. Short descriptive slugs only.

**Twelve pillars, all live.** Slugs of record are in `canon.json → pillars[]`. The pillar library is the spine; clusters hang off it. New content is supporting articles under a pillar, **not new pillars**.

**Bridge pages.** All 26 owned bridge pages are live. Products route through owned URLs. Beacons direct links are removed site-wide.

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

**Banned brand-wide:** hack · secret · explode · crush it · game-changer · manufactured urgency · fabricated scarcity · fabricated social proof · promises about how fast results arrive.

**Banned near the Vault and near tiers:** upgrade · downgrade · tier · level · step up · next step · plan.

**Banned on Pinterest:** "Make Money Online" and keyword-stuffed variants.

**Two registers, never mixed.** Skool community posts: warm, casual, emoji-forward, peer-to-peer, short lines, heavy white space. Site and editorial: luxury editorial mentor.

**Income and earnings claims** are permitted on every surface **except Meta platforms** (Facebook and Instagram). This includes any page a Meta ad can reach.

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

**Hard third-party IP ban** in every generated image, prompt, listing and asset. No characters, no logos, no branded handbags, no film or franchise likenesses. This has already caused platform deactivations.

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
| BAMI price, structure and live URL | The ladder's top rung |
| Value Vault ledger count | Every "total value" claim in Vault marketing |
| Four Skool module tier assignments — AI Twin/Influencer Creation, Monetization Edit, Content Edit, Pinterest Edit | Module cover production |
| Pinterest domain unblock | The collections-pin lesson; Pinterest Traffic Engine™ |
| Nineteen live shop products routed to no pillar | Nineteen assets earning nothing from site traffic |
| Per-pillar freebies replacing the shared Blueprint fallback | Welcome-sequence segmentation |
| `tdie_audit.py` GitHub Actions deploy — token missing `workflow` scope | The Friday automated audit |
| Sneak-peek PDF in `public/` is publicly reachable and bypasses the email gate | Every opt-in that PDF was built to earn |
| Inactive *WAITLIST* product in Beacons | Nothing — but it carries the retired domain |
| `/affiliates` hub page — status unconfirmed | Nothing confirmed |
| Product and FAQPage JSON-LD on `/shop/weekend-ecosystem`; public `/weekend-ecosystem/curriculum` page | Search indexing of the flagship |
| EverAds Standard-tier campaign — 60 creatives selected, generation not triggered | Standard acquisition |
| Fourthwall merch — awaiting designs, retail pricing, collection name | The merch component of Meta ads |

---

## 10a · SETTLED — NEVER RE-RAISE

These have been decided. They are not open items, not ship gates, and not audit findings. Do not list them, flag them, or ask about them again.

- **The Ads Edit™ pricing on the Beacons Starter Map.** Settled. Any document still describing this as open is stale, and the correct action is to delete that line, not to re-flag it.

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

---

**The Digital Income Edit™ · Canon · 1 September 2026**
