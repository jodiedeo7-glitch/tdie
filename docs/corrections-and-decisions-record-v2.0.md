# THE DIGITAL INCOME EDIT™
## CORRECTIONS & DECISIONS RECORD
### v2.0 · Full Replacement — supersedes and replaces Corrections & Decisions Record v1.9 in its entirety
### Issued: 24 July 2026

---

## STATUS OF THIS DOCUMENT

**This is a full replacement record. It stands alone.** It carries forward every decision in force — Decisions 1 through 58 as recorded in Records v1.0 through v1.9 — and adds Decisions 59 through 65, taken 24 July 2026 during the AI pillar, Digital Products pillar, shop, navigation, verification, and RSS build sessions.

Where this document and any prior record conflict, **this document wins.** Records v1.0 through v1.9 are superseded as governing documents; they are retained as historical artefacts.

**Scope declaration (Decision 31):** covers decisions, standing rules, brand policy, and process. Does not outrank Product Register v3.1 on product facts.

### Precedence stack

1. **Product Register v3.1** — product facts only
2. **Corrections & Decisions Record v2.0** — this document
3. **Resource Map v2.0**
4. **SOP Library v1.0**
5. **Prompt Library v1.7**
6. **Master Operating Manual v3.0**

The live site, repo, and shop override any document, including this one.

### Full decision list

**Decisions 1–58** — carried forward, in force. Records v1.3 through v1.9 remain the reference texts.

**Decisions 59–65** — new in this record:

59. The Resource Map "not live" column is stale across the pillar table
60. The classroom link is a dual-door checkout (VIP subscribe or one-time)
61. The AI pillar's paid rung is the $5 Value Vault prompt pack, not the Planner
62. Three blocked pillars were unblocked by founder decision
63. The site email platform is undecided — Kit vs MailerLite, flagged not decided
64. The Value Vault ledger is three products totalling $21
65. The RSS feed and publish-date manifest are the article-distribution spine

**Standing Rules 57–58** are added. Standing Rules 1–56 retain their numbers and remain in force.

---
---

# DECISION 59 — THE RESOURCE MAP "NOT LIVE" COLUMN IS STALE ACROSS THE PILLAR TABLE

## The decision

**A full repo audit on 24 July 2026 found the Resource Map v2.0 pillar table's live/not-live column is wrong for multiple pillars.** The repo, not the Resource Map, is the source of truth for build state (per the standing "live site and repo override any document" rule). True state as audited:

- **Pillar 1 (AI)** — LIVE at `/learn/ultimate-guide-to-ai`. Built this session cycle.
- **Pillar 2 (Pinterest)** — LIVE at `/learn/complete-pinterest-marketing-guide` (496 lines). Resource Map says "not live." **Stale.**
- **Pillar 3 (Content Creation)** — LIVE at `/learn/content-creation-guide` (410 lines). Resource Map says "not live." **Stale.**
- **Pillar 4 (Digital Products)** — LIVE at `/learn/digital-products-guide`. Built this session.
- **Pillar 6 (Automation)** — LIVE, but at slug `automating-your-online-business`, NOT the Resource Map's canonical `complete-automation-guide`. **Slug-of-record conflict — see Actions.**
- **Pillar 9 (Business Systems)** — LIVE at `/learn/how-to-build-a-faceless-digital-business`.
- **Pillars 5, 8, 10, 11, 12** — genuinely not in the repo.

## Standing rule

> **57. Build state is read from the repo, never from the Resource Map.** The Resource Map records intent and routing, not what is deployed. Before briefing any pillar as "next unbuilt," audit the repo directly. A Resource Map "not live" label is a claim to verify, not a fact to trust.

## Actions

- **59.1** — Resource Map v2.0 pillar table live/not-live column corrected to match repo audit. *Open — founder or next Resource Map revision.*
- **59.2** — Pillar 6 slug-of-record conflict resolved: either the Resource Map adopts `automating-your-online-business` as canonical, or the live article re-slugs to `complete-automation-guide` with a 301. *Open — approval gate.*

---

# DECISION 60 — THE CLASSROOM LINK IS A DUAL-DOOR CHECKOUT

## The decision

**A Skool classroom link paywalls to a checkout that offers both a one-time purchase and a VIP subscription upgrade in the same interface.** Confirmed by founder 24 July 2026 for the AI CEO Planner™ (Scaling & Systems module) and consistent with the Pinterest Foundations™ classroom-as-checkout pattern already in canon.

This resolves an earlier assumption that a single classroom URL could only serve one price. It serves both: a viewer without access sees the checkout, which presents the one-time price and the VIP option. Where a product is module-delivered, the classroom link is a valid CTA and no `/shop/` route is required.

## Standing rule

> **58. Module-delivered products use the classroom link as checkout.** A Skool classroom link is a valid paid CTA when the product lives inside that module. It presents both the one-time and VIP-subscribe doors. No standalone `/resources/` or `/shop/` page is built for a product that is module-delivered only.

## Actions

- **60.1** — Behavior documented for reuse across pillars. ✅ *Done (this entry).*

---

# DECISION 61 — THE AI PILLAR'S PAID RUNG IS THE $5 VALUE VAULT PROMPT PACK

## The decision

**The AI pillar's journey paid CTA is 8 Claude Prompts ($5, one-time, Value Vault), not the AI CEO Planner™.** Founder decision, 24 July 2026, overriding the earlier-in-session direction to surface the VIP Planner.

Rationale as decided: the $5 pack is the entry rung; the AI CEO Planner™ lives inside VIP (Scaling & Systems module) for members already there. The Planner therefore appears nowhere on the AI pillar page — not in the journey block, not in the body. Founder confirmed this is intended: a low-friction paid entry, with the Planner as an in-VIP asset rather than a pillar CTA.

The AI pillar's free rung was reassigned to the **Faceless Income Blueprint™** (the AI CEO Planner™ excerpt page was never built and will not be — the Planner is module-delivered per Decision 60).

## Actions

- **61.1** — `ArticleLayout.astro` AI journey entry: free slot added (Blueprint), paid slot kept as $5 Claude Prompts, comment corrected. ✅ *Done.*

---

# DECISION 62 — THREE BLOCKED PILLARS WERE UNBLOCKED BY FOUNDER DECISION

## The decision

Three pillars carried as blocked in the Resource Map were unblocked 24 July 2026:

- **Pillar 7 (Email) — slug collision resolved.** Decision: the *big* pillar guide takes the natural slug `/learn/email-marketing`; the existing supporting article `email-marketing-for-beginners` re-slugs with a 301. **Not yet executed** — the big guide does not exist yet, so the swap is blocked until the Email pillar is written. The decision is recorded; the code change waits for the pillar build. Shipping the 301 before the pillar guide exists would redirect the live supporting article to a 404 and must not be done.
- **Pillar 8 (Branding) — entry product resolved.** The Brand Building & Brand Identity module on Skool Premium ($9/mo) is the pillar's entry product. Classroom link on file: `skool.com/thedigitalincomeedit/classroom/81c6bb56`. The pillar guide, when built, CTAs into it via the dual-door pattern (Decision 60).
- **Pillar 10 (Passive Income) — two decisions.** (1) The Faceless Income Blueprint™ stays one-size-fits-all for now; segmentation-on-entry (open item 1) is **deferred by decision, not resolved** — nothing is written around it. (2) The first paid step on the Passive Income pillar is Premium ($9), not VIP ($27).

## Actions

- **62.1** — Pillar 7 slug swap + 301. *Blocked until the Email pillar guide is built.*
- **62.2** — Pillar 8 branding module link filed for the pillar build. ✅ *Recorded.*
- **62.3** — Pillar 10 open item 1 (Blueprint segmentation) status changed to *deferred by decision*. Still open as strategy; explicitly parked.

---

# DECISION 63 — THE SITE EMAIL PLATFORM IS UNDECIDED — KIT VS MAILERLITE

## The flag

**This entry records an open decision, not a resolution.** Canon (prior records, Master Operating Manual) names **Kit (ConvertKit)** as the newsletter platform. As of 24 July 2026 no Kit account exists, so there is no migration cost to reconsidering.

The founder's requirement — automatically email the list on each new article publish, with the article's summary, a free-community link, and whatever paid offer that article promotes — needs RSS-to-email automation. Findings:

- **Kit** — RSS-triggered campaigns require the paid Creator plan (~$33/mo as of the Sept 2026 price rise; verify live).
- **MailerLite** — RSS automation is available on the free tier (up to ~1,000 subscribers); likely $0 for the exact request at current list size.

MailerLite therefore does the requested automation for free where Kit charges. Choosing MailerLite is a **canon change** (docs say Kit), flagged here rather than silently made.

## Actions

- **63.1** — Founder decides: Kit or MailerLite. *Open.*
- **63.2** — The subscribe button currently points at Beacons (`links.thedigitalincomeedit.com/page2`). Repoint to the chosen platform once decided. *Open.*
- **63.3** — If MailerLite is chosen, amend the Master Operating Manual and any record naming Kit. *Open, conditional.*

---

# DECISION 64 — THE VALUE VAULT LEDGER IS THREE PRODUCTS TOTALLING $21

## The decision

**The Value Vault ledger is three products, total $21**, resolving the open ledger-count defect (formerly recorded as two products / $12):

1. Build Your First Freebie in One Afternoon — $7
2. 8 Claude Prompts That Save Me 12 Hours a Week — $5
3. How I Batch & Schedule a Month of Pinterest in One 3-Hour Block — $9

Founder note: more products will be released, so the Vault's bundled value grows before promotion begins.

**Related decision — the two Vaults coexist.** Record v1.3 stated the Value Vault "absorbs and replaces the former PLR Vault folder concept." Founder overrides this 24 July 2026: the **Value Vault** (single-problem guides, one-time) and the **Pretty & Paid PLR Vault™** ($11/mo rebrandable-product subscription) are two separate products that both stay. The earlier "replaces" language is retired.

## Actions

- **64.1** — Value Vault ledger row updated to three products / $21. Product facts belong to Product Register v3.1; reconcile there. *Open — Register update.*
- **64.2** — Retire the "Value Vault replaces PLR Vault" language wherever it appears. *Open.*

---

# DECISION 65 — THE RSS FEED AND PUBLISH-DATE MANIFEST ARE THE ARTICLE-DISTRIBUTION SPINE

## The decision

**The site publishes an RSS feed at `/rss.xml`, built from the live article files, ordered by a publish-date manifest.** Shipped 24 July 2026.

- `src/pages/rss.xml.js` — reads `title`, `description`, and `category` straight from each article's `<ArticleLayout>` props at build time, so the feed never drifts from the page.
- `src/data/article-dates.js` — the single source of truth for publish dates. **When a new article ships, add one line here** or it appears in the feed at the fallback date, not as newest.
- `@astrojs/rss@^4.0.19` added to `package.json`.

This feed is the platform-neutral spine for the email-on-publish automation (Decision 63) and doubles as a Pinterest crawl-frequency signal (already on the roadmap).

**Known gap resolved:** article `.astro` files carry no date prop; the manifest supplies dates externally rather than retrofitting a prop into every file.

## Actions

- **65.1** — RSS feed, date manifest, and dependency pushed to `main`. ✅ *Done.*
- **65.2** — Verify `/rss.xml` renders after deploy; if the `import.meta.glob` raw import errors on the live Astro version, adjust syntax. *Open — founder eyeball.*
- **65.3** — Add each new article to the date manifest on publish. *Standing task.*

---
---

## SESSION APPENDIX — LIVE SHIP LOG, 24 JULY 2026

For traceability. These are completed code changes on `main`, not decisions.

- Desktop nav: `Join → /membership` corrected to `Community → /community`.
- Footer: Learn column pointed at real pillar articles; two dead `href="#"` socials removed.
- Shop: Value Vault section added (3 products, prices labelled one-time); PLR Vault card renamed to canonical `Pretty & Paid PLR Vault™`.
- Shop: `/shop/plr-vault` renamed to `/shop/pretty-and-paid-plr-vault/`; 301 added in `astro.config.mjs`; old slug deleted.
- Resources: Starter Map, Pinterest Keyword Planner, and Skool `/about` community surfaced.
- Vault sales page: `VAULT_UNLOCK` wired to the live Skool classroom checkout; TODO removed.
- Pinterest domain verification meta tag added to both `PageLayout.astro` and `index.astro` (homepage is a standalone layout that does not inherit `PageLayout` — any site-wide `<head>` tag must go in both).
- AI pillar (`ultimate-guide-to-ai`) and Digital Products pillar (`digital-products-guide`) shipped.
- Digital Products journey CTA pointed at the canonical Vault slug direct (301 no longer in the click path).
- RSS feed, date manifest, `@astrojs/rss` dependency shipped.

---
