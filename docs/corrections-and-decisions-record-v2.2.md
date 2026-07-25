# THE DIGITAL INCOME EDIT™
## CORRECTIONS & DECISIONS RECORD
### v2.1 · Full Replacement — supersedes and replaces Corrections & Decisions Record v2.0 in its entirety
### Issued: 24 July 2026

---

## STATUS OF THIS DOCUMENT

**This is a full replacement record. It stands alone.** It carries forward every decision in force — Decisions 1 through 65 as recorded in Records v1.0 through v2.0 — and adds Decisions 66 through 72, taken 24 July 2026 during the pillar completion sessions (Pillars 5, 7, 8, 10, 11, 12) and the email-slot correction.

It also **resolves Decision 63** (email platform), which was previously open.

Where this document and any prior record conflict, **this document wins.** Records v1.0 through v2.0 are superseded as governing documents; they are retained as historical artefacts.

**Scope declaration (Decision 31):** covers decisions, standing rules, brand policy, and process. Does not outrank Product Register v3.1 on product facts.

### Precedence stack

1. **Product Register v3.1** — product facts only
2. **Corrections & Decisions Record v2.1** — this document
3. **Resource Map v2.0**
4. **SOP Library v1.0**
5. **Prompt Library v1.7**
6. **Master Operating Manual v3.0**

The live site, repo, and shop override any document, including this one.

### Full decision list

**Decisions 1–65** — carried forward, in force. Records v1.3 through v2.0 remain the reference texts.

**Decision 63 — RESOLVED** in this record: the site email platform is **MailerLite**, not Kit. See the amended entry below.

**Decisions 66–72** — new in this record:

66. All twelve pillars are built and live
67. The email platform is MailerLite (resolves Decision 63)
68. Email pillar slug collision resolved by Option B (no swap, no 301)
69. A paid product must never occupy a "free" journey slot — corrected and audited
70. Passive Income's entry rung is Membership Premium ($9), not VIP
71. Mindset routes to the free community as a single door — no tier ladder
72. The Automation slug-of-record is the live slug (resolves Decision 59.2)

**Standing Rules 59–60** are added. Standing Rules 1–58 retain their numbers and remain in force.

---
---

# DECISION 66 — ALL TWELVE PILLARS ARE BUILT AND LIVE

## The decision

**As of 24 July 2026, all twelve pillar guides are live in the repo and deployed.** The pillar library is complete. Live slugs of record:

1. AI — `/learn/ultimate-guide-to-ai`
2. Pinterest — `/learn/complete-pinterest-marketing-guide`
3. Content Creation — `/learn/content-creation-guide`
4. Digital Products — `/learn/digital-products-guide`
5. Affiliate Marketing — `/learn/affiliate-marketing-101`
6. Automation & Paid Traffic — `/learn/automating-your-online-business` (see Decision 72)
7. Email Marketing — `/learn/email-marketing-guide` (see Decision 68)
8. Branding — `/learn/branding-guide`
9. Business Systems — `/learn/how-to-build-a-faceless-digital-business`
10. Passive Income — `/learn/passive-income-guide`
11. Mindset — `/learn/mindset-guide`
12. Blogging — `/learn/complete-blogging-guide`

Each carries its journey block (free/paid/affiliate resolved per pillar), Article schema, and real library images. Each is registered in the RSS date manifest (Decision 65).

## Standing rule

> **59. The pillar library is the spine; supporting clusters hang off it.** With all twelve pillars live, new content is cluster/supporting articles under a pillar, not new pillars. The next structural project is per-pillar freebies (see Actions), not more pillar guides.

## Actions

- **66.1** — All twelve pillar guides shipped to `main`. ✅ *Done.*
- **66.2** — Resource Map v2.0 pillar table is now stale on nearly every row (all show "not live"). Regenerate the Map to reflect the live library. *Open — founder or Map revision.*
- **66.3** — Per-pillar freebie project: build a distinct lead magnet for each pillar and replace the shared Blueprint fallback. This is the project that actually **resolves open item 1** (Blueprint segmentation) rather than deferring it. *Open — next major project.*

---

# DECISION 67 — THE EMAIL PLATFORM IS MAILERLITE (RESOLVES DECISION 63)

## The decision

**The site's email platform is MailerLite, not Kit.** Founder decision, 24 July 2026, resolving the open flag in Decision 63.

Rationale: the founder's requirement is auto-email-on-publish (new article → email the list with summary, community link, and the article's promoted offer). MailerLite includes RSS-to-email automation on its free tier (to ~1,000 subscribers); Kit gates the same behind the paid Creator plan (~$33/mo). No Kit account existed, so there was no migration cost. MailerLite does the exact requested automation for $0 at current list size.

**This is a canon change.** Prior records and the Master Operating Manual named Kit. Those references are superseded by this decision.

## Actions

- **67.1** — Amend the Master Operating Manual and any record naming Kit as the newsletter platform. *Open.*
- **67.2** — Build the MailerLite subscribe form and replace the Beacons subscribe destination (`links.thedigitalincomeedit.com/page2`). *Open — requires founder MailerLite account first.*
- **67.3** — Wire MailerLite RSS-to-email automation to the live `/rss.xml` feed (Decision 65). *Open — after account + form.*

---

# DECISION 68 — EMAIL PILLAR SLUG COLLISION RESOLVED BY OPTION B

## The decision

**The Email pillar takes a new clean slug `/learn/email-marketing-guide`; the supporting article stays untouched at `/learn/email-marketing-for-beginners`.** Founder chose Resource Map Option B, 24 July 2026.

This supersedes the earlier "big guide takes the slug, supporting article 301s" framing recorded in Decision 62 (which mapped to Option A). Option B needs **no re-slug and no 301** — the two slugs don't collide because the pillar uses a different one. Decision 62's "blocked until the pillar exists" action item is therefore **closed as moot**: nothing was ever swapped.

## Actions

- **68.1** — Email pillar shipped at `/learn/email-marketing-guide`; supporting article untouched. ✅ *Done.*

---

# DECISION 69 — A PAID PRODUCT MUST NEVER OCCUPY A "FREE" JOURNEY SLOT

## The decision

**The `free` slot in a journey block renders under a free-resource framing and must contain a genuinely free resource — never a paid product.** Correction made 24 July 2026 after the founder caught the Email pillar's `free` slot pointing at "Build Your First Freebie in One Afternoon" ($7 Value Vault product).

The $7 product was replaced with the Faceless Income Blueprint™ (genuinely free). An audit of all twelve pillars' `free` slots confirmed no other instance; the one flagged false positive (Automation's "$10/Day Traffic Machine — Starter Map") is a free `/resources/` page whose price-like name is part of the product title, not a charge.

**Process note:** an earlier same-session review defended keeping the $7 product in the free slot as "on-topic." That was wrong. A price in a free slot is a defect regardless of topical fit, and "keep the live choice" is not a reason to ship a mislabeled price.

## Standing rule

> **60. Free means free. The `free` journey slot carries only $0 resources.** Any slot rendered under a free-resource heading must link a genuinely free page. A priced product belongs in the `paid` slot or nowhere. Topical relevance never overrides this.

## Actions

- **69.1** — Email `free` slot corrected to the Blueprint; all pillars audited. ✅ *Done.*

---

# DECISION 70 — PASSIVE INCOME'S ENTRY RUNG IS MEMBERSHIP PREMIUM ($9), NOT VIP

## The decision

**The Passive Income pillar's paid CTA is Membership Premium ($9/month), not VIP ($27).** Founder decision, 24 July 2026.

This resolves the pillar's long-standing "GAP + ladder mismatch" flag and **open item 2** for this pillar. The layout had suppressed the paid slot pending a gate decision, specifically because routing the most beginner-coded category to a live $27 flagship tier with no cheaper rung was the flagged problem. Setting the entry rung to Premium $9 supplies exactly the rung that was missing. The beginner gets the $9 door, not the $27 flagship.

## Actions

- **70.1** — Passive Income journey paid slot set to Membership Premium ($9), `/membership`. ✅ *Done.*

---

# DECISION 71 — MINDSET ROUTES TO THE FREE COMMUNITY AS A SINGLE DOOR

## The decision

**The Mindset pillar's CTA is the free community join — one door — with the community positioned as the ongoing mindset home. No standalone paid product, and no tier ladder.** Founder decision, 24 July 2026.

This aligns with the Resource Map's existing instruction ("paid GAP by design — do not fill; CTA is Membership Free") — it is a confirmation, not an override. Mindset is taught inside every module and is not sold standalone (MOM v3.0, Part 6).

**Rule protection applied:** the founder initially suggested the article could walk readers "from free to premium to VIP." That is a tier-ladder comparison frame — banned by the vocabulary and comparison-frame rules (upgrade/tier/level/step; membership tiers never appear as an adjacent sequence). It was caught and reframed to a single community invitation before drafting. The Mindset article invites into the community as one door; it does not lay out the tiers as steps to climb.

## Actions

- **71.1** — Mindset journey: Blueprint free slot, community CTA, no paid slot. ✅ *Done.*

---

# DECISION 72 — THE AUTOMATION SLUG-OF-RECORD IS THE LIVE SLUG (RESOLVES 59.2)

## The decision

**The Automation & Paid Traffic pillar's canonical slug is its live slug, `/learn/automating-your-online-business`.** The Resource Map's `/learn/complete-automation-guide` is retired as the canonical route. Resolves Decision 59.2 with Option A (bless the live slug; do not rename a live, indexed page to satisfy a document).

No 301 and no file move. The live URL keeps its search history. The Resource Map text still cites the old slug and is stale until a Map revision.

## Actions

- **72.1** — Resolution recorded. ✅ *Done (this entry).*
- **72.2** — Resource Map v2.0 Automation row updated to the live slug. *Open — Map revision.*

---
---

## SESSION APPENDIX — LIVE SHIP LOG, 24 JULY 2026 (PILLAR COMPLETION)

Completed code changes on `main`, not decisions:

- Pillar 5 (Affiliate Marketing 101) shipped; journey: Blueprint free, Leni Loves Collage Edit™ ($27) paid, None affiliate.
- Pillar 7 (Email Marketing) shipped at `/learn/email-marketing-guide`; journey: Blueprint free (after correction), Beacons affiliate (unlinked), Membership Premium $9 paid.
- Pillar 8 (Branding) shipped; unblocked via the live Skool Premium Brand Building & Brand Identity module; journey: Blueprint free, module $9 paid, None affiliate. BAMI untouched and unrouted.
- Pillar 10 (Passive Income) shipped; journey: Blueprint free, Membership Premium $9 paid.
- Pillar 11 (Mindset) shipped; journey: Blueprint free, free community CTA, no paid slot.
- Pillar 12 (Blogging) shipped; journey: Blueprint free, no paid slot by design, None affiliate.
- Email `free` slot corrected from the $7 product to the Blueprint; all pillars audited for the same defect.
- Digital Products Vault CTA pointed at the canonical slug direct (301 out of the click path).
- All new pillars added to the RSS date manifest.

**All twelve pillars are live as of this session.**

---

---
---

# RECORD v2.2 ADDENDUM — 24 July 2026 (freebie system + MailerLite)

*Appended to Corrections & Decisions Record v2.1. Adds Decisions 73–76.*

# DECISION 73 — TWELVE PILLAR FREEBIES ARE LIVE AND WIRED

Each pillar now has its own lead-magnet page at `/resources/[slug]-kit`, built on `PageLayout` with the shared `FreebieForm.astro` capture component. Each freebie: (a) delivers value on-page (page-is-the-freebie model — no emailed asset yet), (b) captures email to MailerLite, (c) routes to the free community, (d) routes to one upsell.

**Upsell per freebie = the pillar's own journey-block paid rung.** The three no-product pillars (Business Systems, Mindset, Blogging) use Membership Premium ($9) as the upsell, per founder decision.

**Wiring:** every pillar's journey-block `free` slot now points at its own freebie, replacing the shared Faceless Income Blueprint™ fallback. The Blueprint is no longer the catch-all free CTA on any pillar.

Freebie slugs: ai-starter-kit, pinterest-traffic-kit, content-creation-kit, digital-products-kit, affiliate-starter-kit, automation-kit, email-starter-kit, branding-kit, business-systems-kit, passive-income-kit, mindset-kit, blogging-kit.

**Standing Rule 61:** a pillar's `free` journey slot points at that pillar's own freebie. The Blueprint is retained as a general resource but is no longer a pillar free-CTA.

# DECISION 74 — MAILERLITE FORM IS THE SINGLE CAPTURE POINT (OPTION 1)

All freebies and the site newsletter capture into ONE MailerLite list via one embedded form (account 2532349, form 193994333796435364). Per-pillar segmentation (12 groups exist, currently unused) is deferred — Option 1 chosen to ship capture on all pages now. To segment later: swap the form action URL for a pillar-specific form ID, one line per page in `FreebieForm.astro` usage.

# DECISION 75 — NEWSLETTER SUBSCRIBE REPOINTED TO MAILERLITE

`/newsletter` previously linked to Beacons `/page2`. Now uses the MailerLite `FreebieForm` component — same single list as the freebies (founder confirmed). Beacons is no longer the newsletter capture.

# DECISION 76 — EMAIL-DELIVERY AUTOMATION IS DEFERRED

Freebies capture the email and show MailerLite's thank-you, but do NOT auto-email an asset. Content lives on the page. Auto-email-on-publish (RSS→campaign) and per-freebie asset delivery are open MailerLite-dashboard tasks, not repo work.

