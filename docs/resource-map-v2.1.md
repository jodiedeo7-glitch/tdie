# THE DIGITAL INCOME EDIT™
## RESOURCE MAP
### v2.1 · Issued 24 July 2026 · Supersedes Resource Map v2.0 in full

---

## STATUS OF THIS DOCUMENT

This is a surgical update of Resource Map v2.0, reconciled against **Corrections & Decisions Record v2.1** and the repo audit of **24 July 2026**. Only factually stale states (live/not-live) and resolved conflicts have changed; every finding, reasoning note, and standing rule from v2.0 is preserved verbatim.

**Precedence stack, in order:**
1. Product Register v3.1 — product facts only
2. Corrections & Decisions Record v2.1
3. **This document** — Resource Map v2.1
4. SOP Library v1.0
5. Prompt Library v1.7
6. Master Operating Manual v3.0

Where they conflict, the higher one wins. The live site, repo, and shop override any document, including this one.

**⚠️ MAJOR STATE CHANGE SINCE v2.0: all twelve pillar guides are now LIVE (Record v2.1, Decision 66).** v2.0 was written when zero pillar routes were implemented; that is no longer true. Each pillar row below now records its **live slug** and its **resolved journey CTAs** (free/paid/affiliate). The routing fields describe what each pillar's journey block actually renders today, not an aspiration.

---
---

# PART 0 — THE CENTRAL FINDING

## The per-pillar routing does not exist on the site

Resource Map v1.0 describes twelve pillars, each with a distinct free resource, paid resource, and affiliate recommendation. **The site implements one routing block, copy-pasted across all eleven live articles.**

Every live article — regardless of pillar — carries the identical `slot="journey"` block:

| Route | What every article carries | Pillars where the Resource Map agrees |
|---|---|---|
| Free resource | `/resources/faceless-income-blueprint` | 4 (Digital Products), 10 (Passive Income) — and 5 by a different Blueprint |
| Paid resource | `/shop/plr-vault` | 4 (Digital Products) only |
| Affiliate | Canva, `https://www.canva.com` | 3 (Content Creation) only |

**This is not fourteen broken routes.** Broken routes point somewhere wrong. These routes point somewhere *fixed* — the same three destinations, eleven times, irrespective of what the reader was reading.

### Why this is the more serious finding

A broken link announces itself. A 404 gets reported. **A working link to the wrong product converts.** A reader finishing `pinterest-seo` is offered a digital-products blueprint, a PLR subscription, and a Canva referral — all three resolve, all three look intentional, none of them is what the Resource Map says that reader should be offered. The failure is invisible to every check that tests whether links work, because they do.

It is also invisible to per-article review. Each `journey` block, read alone, is a competent close-out: free resource, paid offer, affiliate, community, related reading. It passes the MOM v3.0 Part 5 checklist item-by-item. The defect only appears when you read two articles side by side and notice they are the same article at the bottom.

### What the audit's close-out table actually measured

The Live Site Audit's per-article close-out table records **PASS** on "Contextual free resource," "Contextual paid offer," and "Affiliate recommendation" for all eleven articles. That table is correct as written — the audit checked *presence*, which is what MOM v3.0 Part 5 enumerates. The word doing the work in all three rows is **contextual**, and presence is not context. Eleven articles carrying the same three CTAs satisfy the checklist and defeat its purpose.

**Recorded consequence:** the close-out audit checks in SOP 1, SOP 2, SOP 12, and Prompt 20 test presence, not correspondence. A correspondence check — *does this article's free resource match its pillar's Resource Map row* — does not exist in any SOP or prompt. Every one of them would pass the current site. See Part 3, Finding 1.

### Implementation status of this document

**Zero of the twelve rows below are implemented.** Not partially. Not mostly. The one row that comes closest is Pillar 4 (Digital Products), where the Blueprint and the Vault both happen to be correct — by coincidence of the copy-paste, not by routing.

**⚠️ SUPERSEDED (v2.1):** this paragraph described v2.0's state, when no routing was implemented. As of 24 July 2026 all twelve pillars are live and their journey blocks are `IMPLEMENTED` (Record v2.1, Decision 66). The flags below now describe residual defects or open items in *individual* routing fields, not a universal absence of implementation. Read each row's own status line.

---

## Category labels — resolved

**Decision (16 July 2026):** canon labels win. Confirmed as consistent with the Pillar 6 build decision — **the pillar defines the category label.**

| Canon label | Repo label (live) | Action |
|---|---|---|
| `AI` | `AI & Automation` — `ai-for-online-business.astro:9` | Re-tag to `AI` |
| `Automation & Paid Traffic` | `Automation` — `business-that-runs-without-you.astro:9` | Re-tag to `Automation & Paid Traffic` |

Issues 025 and 027 get re-tagged. Rows 1 and 6 below stand as canon states them.

**Why the site does not win here.** Record v1.2 Decision 7 established that where an architecture document and a running build disagree, the build wins — it resolves, the document was a guess. That precedent does not extend to this case. There, the repo had *one* implementation and the document had *one* different specification. Here the repo has **two labels for two pillars, assigned wrong**: `AI & Automation` on an AI article and `Automation` on an automation article, with the canon label `Automation & Paid Traffic` appearing nowhere and the `Paid Traffic` scope silently dropped. A build that is internally inconsistent is not a fact to defer to. It is a defect with two symptoms.

**Standing Rule 24 (new).** *The pillar defines the category label.* A category label is canon before it is code. Where a live article's category prop does not match MOM v3.0 Part 2's pillar table, the article is re-tagged; the table is not amended.

**Hard-fail strings added:** `AI & Automation` · `Automation` *(as a standalone category label — the substring inside `Automation & Paid Traffic` is not a hit)*. Added to SOP 12 Phase B, Prompt 20, Prompt 10.

---

## How to read the rows

Every article in a pillar routes to that pillar's free resource, paid resource, and affiliate — **not to the site-wide default.** The three related pillars define the internal linking spine.

**Route convention.** All URLs are flat: `/learn/[slug]` (Record v1.2, Decision 7). Product and resource routes carry their own paths. Domain is `learn.thedigitalincomeedit.com` (Record v1.2, Decision 6) and never appears in row text — routes are written path-relative.

**Status convention:**

- `🔴 BLOCKED` — a field names an unreleased or non-existent asset. SOP 1 step 2 applies: the pillar cannot be briefed.
- `⚠️ FLAG` — the field is routable but carries a recorded conflict.
- `GAP — needs creation` — no asset exists for this route.
- `GAP — no current product` — no existing product fits without a forced mismatch.
- `None — not relevant to this pillar` — no honest affiliate fit. **An empty affiliate field is a PASS, not a gap.**

---
---

# PART 1 — PILLAR GUIDES

**No pillar guide carrying a canon title is live. All twelve.**

The audit records Business Systems as "arguably yes" — Issue №017 is first in sequence, longest, most-linked-to, and functions as the pillar in practice. It does not carry the canon title. Resource Map v1.0 asserted the live title was *"How to Build a Faceless Digital Business From Scratch in 2026."* The live SEO title is **"How to Build a Faceless Digital Business (2026 Guide)"** and the live H1 is **"How to Build a Faceless Digital Business."** Neither matches canon.

**Canon pillar titles and routes — the twelve. None live.**

| # | Category | Canon pillar title | Route | Live |
|---|---|---|---|---|
| 1 | AI | The Ultimate Beginner's Guide to AI | `/learn/ultimate-guide-to-ai` | No |
| 2 | Pinterest | The Complete Pinterest Marketing Guide | `/learn/complete-pinterest-marketing-guide` | No |
| 3 | Content Creation | The Content Creation Guide | `/learn/content-creation-guide` | No |
| 4 | Digital Products | Digital Products for Beginners | `/learn/digital-products-guide` | No |
| 5 | Affiliate Marketing | Affiliate Marketing 101 | `/learn/affiliate-marketing-101` | No |
| 6 | Automation & Paid Traffic | The Complete Guide to Automating Your Online Business | `/learn/complete-automation-guide` | No |
| 7 | Email Marketing | Email Marketing for Beginners | ⚠️ **SLUG COLLISION** — see below | No |
| 8 | Branding | The Branding Guide | `/learn/branding-guide` | No |
| 9 | Business Systems | How to Build a Faceless Digital Business From Scratch in 2026 | `/learn/how-to-build-a-faceless-digital-business` | ⚠️ Wrong title, right route |
| 10 | Passive Income | Building Passive Income Streams | `/learn/passive-income-guide` | No |
| 11 | Mindset | The Mindset Guide | `/learn/mindset-guide` | No |
| 12 | Blogging | The Complete Blogging Guide | `/learn/complete-blogging-guide` | No |

**Slugs above are proposed, not canon.** MOM v3.0 Part 2 names the pillar titles; it specifies no slugs, and under flat URLs (Decision 7) the slug is the only identifier. Each requires uniqueness verification against the full live article list at the publishing gate (Standing Rule 15) before it enters canon.

## ⚠️ Slug collision — Pillar 7

**Canon pillar title:** *Email Marketing for Beginners*
**Live article at `/learn/email-marketing-for-beginners`:** *"How to Write Your First 5 Emails (Before You Have a Single Subscriber)"* — a supporting article, ~1,098 words, category `Email Marketing`.

The natural slug for Pillar 7's pillar guide is occupied by a different article. Under flat URLs there is no namespace to escape into (Standing Rule 15). Three options, none taken here:

- **A** — re-slug the supporting article, 301 the old URL, pillar takes `/learn/email-marketing-for-beginners`
- **B** — pillar takes a different slug (`/learn/email-marketing-guide`); the supporting article keeps its URL
- **C** — the live article is promoted to pillar and rewritten to length; canon title is amended to its live title

**✅ RESOLVED (Decision 68): Option B chosen.** The pillar took the new slug `/learn/email-marketing-guide`; the supporting article kept `/learn/email-marketing-for-beginners` untouched. No re-slug, no 301, no collision. Options A and C were not taken.

## ⚠️ Pillar 9 — title defect

Issue №017 resolves at the correct route and functions as the pillar. Its title matches no canon document. Two options:

- **A** — amend the live title to canon: *"How to Build a Faceless Digital Business From Scratch in 2026"*
- **B** — amend canon to the live title, in MOM v3.0 Part 2 and every downstream reference

**Requires approval gate.** The SEO argument favours B (the live title is tighter and already indexed); the canon-integrity argument favours A. Not decided here. Route is unaffected either way.

## Length — all eleven live articles fail the floor

Every live article measures between roughly **1,000 and 1,330 words**. MOM v3.0 Part 5 sets supporting articles at **1,500–2,500** and pillar articles at **3,000–6,000**.

- **Eleven of eleven** fall below the supporting-article floor.
- **Issue №017**, the only article functioning as a pillar, measures ~1,330 against a 3,000 floor — **44% of minimum**.

Word counts are the audit's stripped-tag approximation and are directional, not a publishing-tool count. The gap on Issue №017 is too large to be a measurement artefact.

**Consequence for this document:** no pillar row below can be closed by an article at current length. Every "pillar guide live" answer in this map is **No** on title grounds; on length grounds it would be No regardless. Recorded as Part 3, Finding 2.

---
---

# PART 2 — THE TWELVE ROWS

---

## 1. AI

**Pillar guide:** The Ultimate Beginner's Guide to AI · **Route:** `/learn/ultimate-guide-to-ai` · ✅ **LIVE**
**Category label:** `AI` — re-tag `ai-for-online-business` from `AI & Automation` (Decision, 16 July)
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | AI CEO Planner™ (excerpt). ⚠️ **FLAG — build unconfirmed.** Mapped in MOM v3.0 Part 6; no `/resources/` opt-in page exists in the repo. If the gated PDF does not exist: `GAP — needs creation` — a 5–8 page extract covering the AI operating system framework only. **Route:** `/resources/ai-ceo-planner` — **does not exist.** The repo's only resource page is `/resources/faceless-income-blueprint`. |
| **Paid resource** | AI CEO Planner™ (full workbook) — Shop, core offer rung. ⚠️ **FLAG — no product page.** The repo's only Shop product page is `/shop/plr-vault`. **Route:** `/shop/ai-ceo-planner` — **does not exist.** |
| **Affiliate recommendation** | `None — not relevant to this pillar.` **Resolved from v1.0's flag.** v1.0 named ChatGPT Plus / Claude Pro and flagged that neither runs a public affiliate program. That flag has sat unresolved; it resolves here to the answer v1.0's own reasoning pointed at. Neither runs a public program. The curriculum requires one of them and cannot honestly recommend a third tool with a payout instead. **Empty is correct and is a PASS.** Note: the live article currently carries Canva — Canva is not this pillar's affiliate and its presence here is the Part 0 defect, not a route. |
| **Related pillars** | **Content Creation** — AI is the engine; content is what it produces. Every AI article ends in a content question. · **Automation & Paid Traffic** — AI without automation is still manual labour; the "now make it run without you" step. · **Business Systems** — the AI Operating System Framework lives in Module 6; AI articles that go past tool-level escalate here. |
| **Newsletter CTA** | "Most women use AI like a vending machine. Once a week I'll show you how to use it like a hire." |
| **Community CTA** | "There's a daily prompt waiting inside the community. Free. Copy it, run it, post what you got — that's the whole assignment." |

---

## 2. Pinterest

**Pillar guide:** The Complete Pinterest Marketing Guide · **Route:** `/learn/complete-pinterest-marketing-guide` · ✅ **LIVE**
**Live cluster:** `pinterest-marketing-guide`, `pinterest-seo` — 2 supporting articles, no pillar
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | Pinterest Keyword Planner (from Pinterest Foundations™). ⚠️ **FLAG — extraction required.** Exists as a member worksheet inside Pinterest Foundations™. Needs extracting into a standalone gated PDF before it functions as a lead magnet. **Route:** `/resources/pinterest-keyword-planner` — **does not exist.** |
| **Paid resource** | Pinterest Foundations™ / DFY Pinterest Packages. ⚠️ **FLAG — pricing scattered.** Record v1.1 open item 6 carries DFY package pricing forward as unresolved ($97–$497+/mo across sources). Foundations™ is the routable entry rung; DFY is a service, not a product, and is not an article CTA. **Route:** `/shop/pinterest-foundations` — **does not exist.** |
| **Affiliate recommendation** | `None — not relevant to this pillar.` Pinterest itself pays nothing. Tailwind is the obvious pick and is not taught — the curriculum uses Pinterest's native scheduler (SOP Library, tool list). Recommending a scheduler the brand doesn't use, for commission, is the forced fit. **Empty is correct and is a PASS.** |
| **Related pillars** | **Blogging** — Pinterest is where the blog gets its traffic; the tightest pair on the site. · **Content Creation** — a Pin is a piece of content before it is a traffic source. · **SEO-adjacent → AI** — keyword research and Pin-copy generation are confirmed AI-cluster supporting articles. |
| **Newsletter CTA** | "Pinterest isn't social media. Treating it like Instagram is why yours is flat. Weekly, what it actually is." |
| **Community CTA** | "Drop your Pinterest URL. Someone will tell you within a day which of your boards is doing nothing." |

---

## 3. Content Creation

**Pillar guide:** The Content Creation Guide · **Route:** `/learn/content-creation-guide` · ✅ **LIVE**
**Live cluster:** none — genuinely empty
**Routing status:** `IMPLEMENTED`
**Gate status:** ✅ **UNBLOCKED** — Record v1.2 Decision 14 closed the Skool Lesson 9 blocker as a false positive. The draft lesson is admin-only. This pillar was gated on it in Daily OS Part 1; that gate is lifted (action 14.4).

| Field | Value |
|---|---|
| **Free resource** | Canva Crash Course PDF. ⚠️ **FLAG — built, no site opt-in page.** The asset exists; `/resources/canva-crash-course` **does not exist** in the repo. This is the cheapest free-resource gap to close on the map — the PDF is done, only the page is missing. |
| **Paid resource** | Tommy Kate Edit™ ($17, 200+ prompts — count corrected per Record v1.0). Alternate: Luxe Babe Prompt Pack. **Route:** `/shop/tommy-kate-edit` — **does not exist.** |
| **Affiliate recommendation** | **Canva** — `https://www.canva.com`. Genuinely relevant: it is the tool taught in the Canva Crash Course, used in every Pin and carousel workflow, and named in the SOP Library tool list. **This is the only pillar where Canva is the correct affiliate.** It currently appears on all eleven articles. Ten of those are the Part 0 defect. |
| **Related pillars** | **Pinterest** — content is what Pinterest distributes; the design-to-traffic pair. · **AI** — AI drafts, Canva dresses; the two halves of one production line. · **Branding** — content without a brand is output; the escalation from making things to making *your* things. |
| **Newsletter CTA** | "Posting more isn't a content strategy. It's a treadmill with a schedule. Weekly, the difference." |
| **Community CTA** | "Post the last thing you made. Not the best thing — the last thing. That's the one worth talking about." |

---

## 4. Digital Products

**Pillar guide:** Digital Products for Beginners · **Route:** `/learn/digital-products-guide` · ✅ **LIVE**
**Live cluster:** `creating-your-first-offer`, `digital-products-for-beginners` — 2 supporting articles, no pillar
**Routing status:** `IMPLEMENTED` — journey block live; free/paid/affiliate resolved per Record v2.1.

| Field | Value |
|---|---|
| **Free resource** | **Faceless Income Blueprint™** — built, live at `/resources/faceless-income-blueprint`. ⚠️ **FLAG — two open items.** (1) **Load-bearing across three pillars** (4, 5 via Lead²Engine, 10) — requires welcome-sequence segmentation on entry pillar. Record v1.2 open item 1: **OPEN, no decision made.** (2) **Live placeholder** — page 4 ships as `[ INSERT ... ]`. Record v1.1 action 4.20 / Record v1.2 open item 4: **OPEN.** A live money link in a lead magnet in readers' hands. |
| **Paid resource** | **Pretty & Paid PLR Vault™** — $11/mo standalone subscription. Off-ladder. 6 rebrandable products + 3 AI transformation workflows, refreshed monthly. **Canon route:** `/shop/pretty-and-paid-plr-vault/` with a 301 from any existing PLR Vault URL (Record v1.1, action 4.8). **Live route:** `/shop/plr-vault` — **the 301 has not shipped and the slug has not changed.** ⚠️ **FLAG — naming defect, live.** The repo never once uses the canonical full name. See Part 3, Finding 3. |
| **Affiliate recommendation** | `None — not relevant to this pillar.` The product *is* the recommendation. A reader who has just been taught to build and sell their own digital product does not need a third-party tool referral in the same breath — and the honest tool answer (Canva, for the artwork) belongs to Pillar 3, where it is the pillar's own affiliate. **Empty is correct and is a PASS.** |
| **Related pillars** | **Affiliate Marketing** — the sibling monetization route; readers should understand the tradeoff before choosing. · **Content Creation** — the product is made of content; the skills are upstream. · **Passive Income** — where "I built one product" becomes "I built a system." |
| **Newsletter CTA** | "The first product doesn't have to be good. It has to exist. Weekly, why that isn't permission to be lazy." |
| **Community CTA** | "Name your product before you build it. Post the name. If nobody understands what it is from the name, that's the real feedback." |

---

## 5. Affiliate Marketing

**Pillar guide:** Affiliate Marketing 101 · **Route:** `/learn/affiliate-marketing-101` · ✅ **LIVE**
**Live cluster:** `affiliate-marketing-for-beginners` — 1 supporting article, no pillar
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | Lead²Engine Faceless Blueprint™. ⚠️ **FLAG — build unconfirmed as a site opt-in.** The PDF exists in project knowledge; `/resources/lead-2-engine-blueprint` **does not exist** in the repo. Also a Blueprint-family asset — see open item 1 on segmentation. |
| **Paid resource** | Leni Loves Collage Edit™ ($27, 70% resell). ⚠️ **FLAG — double-$27.** Record v1.2 Standing Rule 12 (amended): where $27 appears twice — this product and The Ads Edit™ (VIP tier) — the copy names what each $27 buys. This pillar's articles must not let the two sit unlabelled on one screen. **Route:** `/shop/leni-loves-collage-edit` — **does not exist.** |
| **Affiliate recommendation** | ⚠️ **FLAG — requires approval gate.** v1.0 named Amazon Associates as the confirmed cluster topic while noting it is a poor earner for this niche ("teach it, don't lead with it"). That is a teaching subject, not a recommendation. **No affiliate is named for this pillar pending a decision.** Naming one is a Resource Map change and goes to the gate — it is not a drafting choice, and this document does not make it. Until then, treat as `None` and pass. |
| **Related pillars** | **Digital Products** — the sibling monetization route; the tradeoff runs both ways. · **Email Marketing** — affiliate income without a list is a one-shot; "Affiliate + Email Marketing" is a confirmed supporting article. · **Blogging** — evergreen affiliate content is a blogging discipline; the confirmed "Affiliate Marketing" article sits in the Blogging cluster too. |
| **Newsletter CTA** | "Recommending things you don't own is the fastest money in this business — and the easiest to do badly. Weekly, how to do it well." |
| **Community CTA** | "Post the one tool you'd recommend even if nobody paid you. That's your first affiliate link — the community will tell you why." |

---

## 6. Automation & Paid Traffic

**Pillar guide:** How to Automate Your Online Business · **Route:** `/learn/automating-your-online-business` · ✅ **LIVE** (Decision 72: live slug is canonical; `/learn/complete-automation-guide` retired)
**Category label:** `Automation & Paid Traffic` — re-tag `business-that-runs-without-you` from `Automation` (Decision, 16 July)
**Live cluster:** `business-that-runs-without-you` — 1 supporting article once re-tagged, no pillar
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | **Starter Map** — 10 pages. Record v1.2 Decision 10, Option A. ⚠️ **FLAG — no trace in the repo.** The audit found no "Starter Map" anywhere: not in the repo, not in the Resource Map, not in any project document. It is a decision without an implementation. Standing Rule 17: it is 10 pages and is not a teaser; length changes only by recorded decision. **Route:** `/resources/starter-map` — **does not exist.** **Live on Beacons** — and carrying a wrong price. See ship-first below. |
| **Paid resource** | `GAP — no current product.` Delivered via Membership only (The Ads Edit™, Module 6). No standalone Shop product exists. **The CTA is Membership VIP — $27/month** (Record v1.2, Decision 15). ⚠️ **FLAG — this is the clearest product hole in the ecosystem:** high commercial intent, nothing to buy at the entry rung, beginner traffic routed to the flagship tier. Same class as open item 2. |
| **Affiliate recommendation** | **Make — recommended, unlinked.** Record v1.2, Decision 11: no affiliate relationship exists. Make is named in Module 6 and is the tool actually taught, so the recommendation is honest and stays. **It ships with no link, no `rel="sponsored"`, and no disclosure.** Standing Rule 18: affiliate mechanics travel as a set — all three or none. An absent link on Make is a **PASS**, not a finding, and not "Named But Uncarryable" (action 11.4). Zapier is the named alternate and is treated identically. |
| **Related pillars** | **AI** — automation is what AI becomes once it stops needing you to press the button. · **Business Systems** — the closest sibling; automation is the tactic, systems are the architecture. Link is near-mandatory. · **Email Marketing** — the welcome sequence is most readers' first real automation; the on-ramp. |
| **Newsletter CTA** | "Doing it by hand isn't discipline. It's a bottleneck. Weekly: one thing you should stop doing yourself." |
| **Community CTA** | "Tell the community the one task you did more than five times this week. That's the one we're automating." |

> ### ⚠️ SHIP FIRST — Record v1.2, action 15.2
> **The Starter Map is live on Beacons and states The Ads Edit™ is Premium, $9/month.** It is **VIP, $27/month**. A live money page is telling readers the wrong price for the wrong tier. Nothing else on this map ships before this is corrected.

---

## 7. Email Marketing

**Pillar guide:** Email Marketing for Beginners · **Route:** `/learn/email-marketing-guide` · ✅ **LIVE** (Decision 68: Option B — pillar took a new slug; supporting article stays at `/learn/email-marketing-for-beginners`, no 301)
**Live cluster:** `email-marketing-for-beginners` — 1 supporting article occupying the pillar's natural slug
**Routing status:** `IMPLEMENTED`
**Gate status:** ✅ **RESOLVED** — Decision 68 (Option B). Pillar took `/learn/email-marketing-guide`; supporting article kept its slug. No collision, no 301.

| Field | Value |
|---|---|
| **Free resource** | Welcome Email Templates (5). ⚠️ **FLAG — tier conflict.** Built, currently a Premium bonus inside The Email Edit™. This is paid-tier content mapped as a free resource. Either extract a free version or this becomes `GAP — needs creation`. **Do not gate-swap without deciding** — Premium members will find their bonus given away. **Route:** `/resources/welcome-email-templates` — **does not exist.** |
| **Paid resource** | `GAP — no current product.` Delivered via Membership only (The Email Edit™). The CTA is Membership Premium — $9/month. |
| **Affiliate recommendation** | ⚠️ **FLAG — requires verification.** v1.0 named Beacons and flagged "confirm current referral terms before linking." **That flag is unresolved and this document does not resolve it.** Beacons is genuinely relevant — it is the brand's own link-in-bio and lead-magnet delivery layer (SOP Library tool list), so the recommendation is honest. But per Standing Rule 18, the link, `rel="sponsored"`, and disclosure ship as a set or not at all. **Until referral terms are confirmed, treat as Make: recommended, unlinked.** Confirming terms and adding the link is maintenance. Naming a different affiliate is a gate change. |
| **Related pillars** | **Affiliate Marketing** — the list is what makes affiliate income repeatable. · **Automation & Paid Traffic** — the welcome sequence is the first automation that matters. · **Digital Products** — the list is who you sell the product to. |
| **Newsletter CTA** | "Your list doesn't want a newsletter. It wants one thing it can't get anywhere else. Weekly, what that is." |
| **Community CTA** | "Post your welcome email's subject line. Just the subject line. That's where it's already going wrong." |

---

## 8. Branding

**Pillar guide:** The Branding Guide · **Route:** `/learn/branding-guide` · ✅ **LIVE** (Decision 62: unblocked via live Skool Premium Brand Building & Brand Identity module; BAMI stays retained-and-unrouted)
**Live cluster:** none — genuinely empty
**Routing status:** `IMPLEMENTED`
**Gate status:** ✅ **UNBLOCKED** — Decision 62. Entry product is the LIVE Skool Premium Brand Building & Brand Identity module ($9/mo), replacing the blocked BAMI row. BAMI stays retained-and-unrouted per Standing Rule 23.

| Field | Value |
|---|---|
| **Free resource** | Brand Bible Memory Chain template. ⚠️ **FLAG — build unconfirmed.** `/resources/brand-bible-memory-chain` — **does not exist.** |
| **Paid resource** | ✅ **RESOLVED (Decision 62).** Brand Building & Brand Identity module, Skool **Membership Premium $9/month**, dual-door checkout (Decision 60). Classroom link on file. BAMI Curriculum remains UNRELEASED and retained-and-unrouted per Standing Rule 23 — it is NOT this CTA; the live module is. |
| **Affiliate recommendation** | `None — not relevant to this pillar.` Branding is taught, not tooled. Canva is the nearest fit and belongs to Pillar 3. **Empty is correct and is a PASS.** |
| **Related pillars** | **Content Creation** — the brand is what makes the content yours rather than output. · **Business Systems** — the Brand Bible is a system artefact before it is an aesthetic one. · **Mindset** — the Creator → CEO shift is a branding decision before it is a psychological one. |
| **Newsletter CTA** | "A brand isn't a colour palette. Yours is probably three fonts and a feeling. Weekly, what it should be instead." |
| **Community CTA** | "Post your brand in one sentence. If it takes two, you don't have one yet — and the community will say so." |

---

## 9. Business Systems

**Pillar guide:** How to Build a Faceless Digital Business From Scratch in 2026 · **Route:** `/learn/how-to-build-a-faceless-digital-business` · ✅ **LIVE** ⚠️ (canon title vs live title still differs; length note from v2.0 retained)
**Live cluster:** Issue №017 + `choosing-a-niche` — the largest cluster on the site
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | ⚠️ **FLAG — v1.0 field is a cross-reference, not a route.** v1.0's Part 6 map records this pillar's free resource as *"— (see Passive Income),"* which routes to the Faceless Income Blueprint™ and makes it load-bearing across a **fourth** pillar. Open item 1 already flags three. **This is not resolved here.** The Blueprint is the operative route (`/resources/faceless-income-blueprint`, live) and inherits both of its flags: segmentation OPEN, page-4 placeholder OPEN. |
| **Paid resource** | Business Architecture Blueprint™ workbook. **Route:** `/shop/business-architecture-blueprint` — **does not exist.** The repo's only Shop product page is the Vault. |
| **Affiliate recommendation** | **Make — recommended, unlinked.** Identical treatment to Pillar 6. Record v1.2, Decision 11: no relationship, no link, no `rel="sponsored"`, no disclosure. Named in Module 6, genuinely taught, honestly recommended, not monetized. Absence of link mechanics is a **PASS**. |
| **Related pillars** | **Automation & Paid Traffic** — the closest sibling; systems are the architecture, automation is the tactic. · **AI** — the AI Operating System Framework is where systems thinking meets the tooling. · **Passive Income** — the system's whole purpose, stated as an outcome. |
| **Newsletter CTA** | "Most people don't have a business. They have a job they gave themselves. Weekly, the difference — and how to cross it." |
| **Community CTA** | "Post the one thing your business can't do without you. That's not a task. That's the architecture problem." |

---

## 10. Passive Income

**Pillar guide:** Building Passive Income Streams · **Route:** `/learn/passive-income-guide` · ✅ **LIVE** (Decision 70: entry rung is Membership Premium $9, not VIP)
**Live cluster:** none — genuinely empty
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | **Faceless Income Blueprint™** — shared with Pillars 4, 5, and 9. ⚠️ **FLAG — this is the load-bearing centre of open item 1.** Segmentation on entry pillar is required and **OPEN — no decision made, and none is made here.** Prompt 12 step 3, Prompt 13 item 5, Prompt 8 step 5, and SOP 4 Phase A step 5 all correctly instruct that it is open and must be recorded rather than written around. Those instructions stand. Page-4 placeholder also OPEN. |
| **Paid resource** | ✅ **RESOLVED (Decision 70).** Entry rung set to **Membership Premium $9/month** — NOT VIP. This supplies the entry rung the pillar was missing and resolves the ladder mismatch: beginners get the $9 door, not the $27 flagship. VIP remains the deeper tier but is not this pillar's CTA. Open item 2 resolved for this pillar. |
| **Affiliate recommendation** | `None — not relevant to this pillar.` Passive income is an outcome, not a toolset. Any affiliate here would be a tool borrowed from another pillar to fill a field — the definition of the forced fit. **Empty is correct and is a PASS.** |
| **Related pillars** | **Business Systems** — passive is what a system produces; the mechanism lives there. · **Digital Products** — the most common first passive asset. · **Affiliate Marketing** — the other one, and the faster one. |
| **Newsletter CTA** | "Passive income isn't passive. It's front-loaded. Weekly, what you front-load and in what order." |
| **Community CTA** | "Post the last thing you built that earned money while you weren't looking at it. If the answer is nothing, post that." |

---

## 11. Mindset

**Pillar guide:** The Mindset Guide · **Route:** `/learn/mindset-guide` · ✅ **LIVE** (Decision 71: CTA is free community join, single door, no paid slot)
**Live cluster:** none — genuinely empty
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | 🔴 **GAP — needs creation.** Creator → CEO diagnostic. **The highest-value free-resource gap on the map** — it is the only lead magnet that would route into every other pillar rather than one. Nothing exists. |
| **Paid resource** | `GAP by design — do not fill.` Mindset is taught inside every module and is not sold standalone (MOM v3.0, Part 6). **This is a deliberate empty, not a hole.** The CTA is Membership Free/Standard. Do not route this pillar to a product to satisfy the close-out checklist. |
| **Affiliate recommendation** | `None — not relevant to this pillar.` **Empty is correct and is a PASS.** |
| **Related pillars** | **Business Systems** — the Creator → CEO shift is structural before it is emotional. · **Branding** — who you decide to be is a branding decision you make first. · **Passive Income** — the mindset question underneath every passive-income fantasy. |
| **Newsletter CTA** | "You don't have a discipline problem. You have an identity problem wearing a discipline costume. Weekly, the difference." |
| **Community CTA** | "Post the thing you've been 'about to start' for three months. Naming it in public is the whole intervention." |

---

## 12. Blogging

**Pillar guide:** The Complete Blogging Guide · **Route:** `/learn/complete-blogging-guide` · ✅ **LIVE** (no paid slot by design; free CTA = Blueprint fallback)
**Live cluster:** `blogging-guide` — 1 supporting article, no pillar
**Routing status:** `IMPLEMENTED`

| Field | Value |
|---|---|
| **Free resource** | 🔴 **GAP — needs creation.** Evergreen article checklist. **The fastest free-resource gap to build on the map** — the checklist is a byproduct of SOP 1 and SOP 2, which already exist. |
| **Paid resource** | `GAP — no curriculum, no product, no lead magnet.` ⚠️ **FLAG:** defensible short-term — blogging content earns SEO trust and feeds every other pillar — but it means the site's own most-visible discipline monetizes only by referral to other pillars. The CTA is a related pillar's product, chosen by article topic, not a Blogging product. |
| **Affiliate recommendation** | `None — not relevant to this pillar.` **Reasoning, carried from v1.0 and unchanged:** the obvious pick is a hosting or WordPress affiliate — and TDIE runs on Astro/Vercel/GitHub. Recommending WordPress hosting for commission while running a different stack is precisely the forced fit. The honest recommendation is the stack actually in use, and neither Vercel nor GitHub pays for referrals. **Leave it empty. It is a PASS.** |
| **Related pillars** | **Pinterest** — Pinterest is where the blog gets its traffic; the tightest pair on the site and the reason blogging works at all for this audience. · **AI** — AI writing, research, and repurposing are confirmed supporting articles and are how one article becomes twelve assets. · **Affiliate Marketing** — blog monetization is affiliate monetization first; the fastest honest revenue on an article that already ranks. |
| **Newsletter CTA** | "Everyone says blogging is dead. My oldest post is still bringing in leads it wrote three years ago. Weekly, why." |
| **Community CTA** | "Post the URL of the one article you're proudest of. The community will find the three links you forgot to add." |

---
---

# PART 3 — FINDINGS

---

## Finding 1 — No correspondence check exists anywhere in the system

**The defect.** Eleven articles carry three identical CTAs. Every SOP and prompt that audits close-outs would pass this site.

SOP 1 Phase A step 1 instructs: record the six fields, they are the article's close-out. That is correct at *brief* time. Nothing verifies at *publish* time that the article shipped the fields its brief recorded. Prompt 20 and SOP 12 Phase B search for hard-fail strings — a correct-looking wrong route is not a string, it is a mismatch between two documents.

**Why it went undetected.** Presence checks pass. The audit's own close-out table records PASS on all three routing rows for all eleven articles, and that table is not wrong — it tested what the checklist enumerates. MOM v3.0 Part 5 says *"one contextual free resource."* The check that got built tests the "one." The word carrying the requirement is "contextual," and it is untestable per-article by construction — you cannot see the defect in an article, only between articles.

**Required — new check, all close-out audits.** For every live article: read its category prop. Open this document's row for that pillar. Compare free resource, paid resource, and affiliate against what the article's `journey` block carries. **A mismatch is a defect. Three articles in three pillars carrying the same three CTAs is the defect.**

**Standing Rule 25 (new).** *Close-outs are audited by correspondence, not presence.* An article's free resource, paid resource, and affiliate are checked against its pillar's Resource Map row, not against whether the fields are populated. A populated wrong route is a defect and outranks an empty one.

**Assets requiring amendment:** SOP 1 (add publish-gate correspondence step) · SOP 2 · SOP 12 Phase B · Prompt 16 (affiliate audit — Check 3 tests absence, not wrongness) · Prompt 20 · Daily OS publishing gate.

---

## Finding 2 — Every live article is below the word floor

Eleven of eleven measure ~1,000–1,330 words against a 1,500 supporting-article floor. Issue №017 measures ~1,330 against a 3,000 pillar floor — **44% of minimum.**

Combined with Part 1: no live article is a pillar by title *or* by length. The site has eleven supporting articles, all under-length, and zero pillars.

**Consequence for Part 4's build order.** The audit proposes re-anchoring existing clusters ahead of opening new categories, on the reasoning that a pillar written into an existing cluster gets inbound links on day one. That reasoning holds. But "re-anchor" implies the clusters are sound and only the pillar is missing. They are not sound — every article in every cluster is below floor. Re-anchoring puts a correctly-titled 3,000-word pillar at the centre of a cluster of 1,100-word articles that are themselves rewrites waiting to happen.

**Not resolved here.** Whether the eleven under-length articles are (a) expanded to floor, (b) accepted as a documented exception, or (c) the floor is amended — is a canon question. **Requires approval gate.** It is the largest single body of work implied by this document and it is not scoped in any SOP.

---

## Finding 3 — The Vault's canonical name appears nowhere on the live site

Record v1.1, Decision 4 established the canonical name: **Pretty & Paid PLR Vault™.** The repo:

| Form | Occurrences | Status |
|---|---|---|
| `Pretty & Paid PLR Vault™` — canonical | **0** | The correct name is never used |
| `PLR Vault` — short form, primary use | **12** | Banned as a primary name |
| `Pretty & Paid Digital Vault` | **3** — all on the product's own page: title, meta description, lede | Explicitly banned variant |
| `Pretty & Paid Vault` | 0 | — |

The short form is permitted **on second reference only, within a document that has already used the full name.** No live page has used the full name. Every one of the 12 short-form uses is therefore a first reference and a defect.

**The product's own page carries the banned variant in its `<title>` and meta description** — the two strings that appear in search results and in every share preview.

**Also outstanding:** action 4.8's slug change to `/shop/pretty-and-paid-plr-vault/` and its 301 have not shipped. The live route remains `/shop/plr-vault`.

---

## Finding 4 — The membership page contradicts the Vault page, live

`membership.astro:21` — *"Premium — $9/mo ... including the PLR Vault™"*
`shop/plr-vault.astro:21` — **$11/month**, standalone

Two live pages, two commercial relationships, same product, same moment. Record v1.0 Decision 2 removed the Vault from Premium; Record v1.1 Decision 4 priced it at $11/mo standalone, off-ladder. **The membership page never received either decision.**

This also breaches Record v1.1 Decision 5 — the comparison-frame ban. The Vault is a door, not a rung. The membership page places it inside the ladder as a Premium inclusion, which is the exact frame the ban exists to prevent.

**Action:** action 4.14 (verify Vault absent from Premium inclusion list) was recorded and has not shipped.

---

## Finding 5 — No structured data on any page

`grep -rn "ld+json\|schema.org\|BreadcrumbList\|FAQPage" src/` returns nothing. Twenty-one live pages, zero structured data.

**This is load-bearing for Decision 7.** Record v1.2 justified flat URLs on the reasoning that *"hierarchy is carried by BreadcrumbList schema and internal linking, both already doing the job, neither needing the URL's help."*

**BreadcrumbList schema does not exist.** The decision's own stated compensating mechanism was never built. Flat URLs remain correct — the argument for them does not depend solely on breadcrumbs, and 301-ing eleven live articles to satisfy a paragraph is still the wrong trade. But the reasoning was written against a mechanism that isn't there, and category hierarchy is currently expressed to crawlers by **internal linking alone.**

Action 7.9 ("BreadcrumbList schema — all live articles — verify hierarchy carried here, since the URL no longer carries it") is not a verification task. It is a build task. **Recorded as scope-changed.**

---

## Finding 6 — The newsletter form is dead, twice, sitewide

`ArticleLayout.astro:111` — `<form onsubmit="return false">`. No handler, no endpoint, no fallback. Renders at the bottom of **all eleven articles.**

`newsletter.astro:12` — the same pattern, independently. No shared logic. **Fixing one does not fix the other.**

**Every row in this document carries a newsletter CTA. All twelve route to a form that cannot capture an email.** The newsletter ecosystem has no entry point. Every article, every pillar, every CTA in Part 2 terminates in a dead input.

The audit's close-out table records this as **PRESENT, NON-FUNCTIONAL** — a form that renders passes a presence check. Same failure class as Finding 1.

---

## Finding 7 — The singular next step fails on all eleven articles

Every `journey` block presents 6–7 competing CTAs — Blueprint, Vault, community, Canva, and 3–4 related reading rows — with no hierarchy marking one as *the* next step.

SOP 1 Phase A step 6 requires "the singular next step. One. Not a menu." Eleven of eleven ship a menu.

**Interaction with Part 0.** These two defects compound. The menu is not just long — it is the *same* menu on every article, so a reader moving through the cluster is offered an identical seven-option choice at the end of each piece. The close-out stops being a next step and becomes site furniture.

**Requires a template decision, not eleven article edits.** The block lives in one place.

---

## Finding 8 — Read time is overstated on every article

Issue №017 displays **"20 Min Read"** against ~1,330 words — 5–7 minutes at 200–250 wpm. All eleven show a similar gap; №017's is the largest in absolute terms because it carries the highest displayed number.

The site's own read-time method was not found in source and may use a different standard. **Recorded as a finding; the number displayed is not defensible at the measured length either way.**

Interacts with Finding 2: if the articles are expanded to floor, the read times become closer to accurate. Fixing the length fixes this. Fixing this without fixing the length means publishing a smaller wrong number.

---

## Finding 9 — Ten live articles are undocumented in canon

`choosing-a-niche` · `creating-your-first-offer` · `digital-products-for-beginners` · `pinterest-marketing-guide` · `pinterest-seo` · `blogging-guide` · `email-marketing-for-beginners` · `affiliate-marketing-for-beginners` · `ai-for-online-business` · `business-that-runs-without-you`

No canon document — Resource Map v1.0, MOM v3.0, SOP Library, Daily OS — records these as built. Every canon document describing "what's live" says Business Systems / Issue №017 alone.

**This document is the first canonical record of their existence.** Their routes, titles, categories, and cluster memberships are recorded in Parts 1 and 2 above.

**Consequential:** the Daily OS build order is computed from a false inventory. Its stated central signal — *"Pillar #1 is incomplete until Pillars 2, 3, and 4 below are live... the single strongest sequencing signal in the entire canon"* — was reasoned against "only Business Systems is live." Five categories carry live content. **The Daily OS build order requires recomputation against Part 1's inventory.** Its *logic* (unblocked and highest-leverage first) is sound and is preserved. Only its inputs were wrong.

---

## Finding 10 — Site state in project knowledge is stale by ten pages

Project memory records *"Eleven pages are confirmed live with zero dead links."* The repo ships **21 pages** (11 articles + 10 non-article), with two dead newsletter forms.

Both halves of the sentence are wrong. Recorded.

---
---

# PART 4 — GAP SUMMARY

## Free resources

| # | Pillar | Status | Route exists |
|---|---|---|---|
| 1 | AI | Mapped, build unconfirmed — AI CEO Planner™ excerpt | No |
| 2 | Pinterest | Mapped, extraction required — Keyword Planner | No |
| 3 | Content Creation | **Built, no opt-in page** — Canva Crash Course. **Cheapest gap on the map.** | No |
| 4 | Digital Products | **Built and live** — Faceless Income Blueprint™. Two open flags. | **Yes** |
| 5 | Affiliate Marketing | Mapped, build unconfirmed — Lead²Engine | No |
| 6 | Automation & Paid Traffic | **Decision made, no implementation** — Starter Map. No trace in repo. | No |
| 7 | Email Marketing | **Tier conflict** — Welcome Email Templates are Premium content | No |
| 8 | Branding | Mapped, build unconfirmed — Brand Bible Memory Chain | No |
| 9 | Business Systems | Cross-reference, not a route — inherits the Blueprint | Via Pillar 4 |
| 10 | Passive Income | Shared — Blueprint. Load-bearing centre of open item 1. | Via Pillar 4 |
| 11 | **Mindset** | 🔴 **GAP — needs creation.** Creator → CEO diagnostic. **Highest-value gap.** | No |
| 12 | **Blogging** | 🔴 **GAP — needs creation.** Evergreen checklist. **Fastest to build.** | No |

**One of twelve free-resource routes exists on the site.**

## Paid resources

| # | Pillar | Status | Route exists |
|---|---|---|---|
| 1 | AI | Product exists, no page — AI CEO Planner™ | No |
| 2 | Pinterest | Product exists, no page; DFY pricing scattered (open item 6) | No |
| 3 | Content Creation | Product exists, no page — Tommy Kate Edit™ | No |
| 4 | Digital Products | **Live** — Vault. Wrong slug, wrong name, no 301. | **Yes, defective** |
| 5 | Affiliate Marketing | Product exists, no page — Leni Loves Collage Edit™. Double-$27. | No |
| 6 | Automation & Paid Traffic | **GAP — no current product.** Membership VIP only. **Clearest product hole.** | — |
| 7 | Email Marketing | **GAP — no current product.** Membership Premium only. | — |
| 8 | **Branding** | ✅ **LIVE — unblocked via Skool Premium module (Decision 62).** | Yes |
| 9 | Business Systems | Product exists, no page — Business Architecture Blueprint™ | No |
| 10 | **Passive Income** | 🔴 **GAP + ladder mismatch, severity increased.** Open item 2. | — |
| 11 | Mindset | GAP by design — **do not fill** | — |
| 12 | Blogging | GAP — no curriculum, no product, no lead magnet | — |

**One of twelve paid-resource routes exists on the site, and it is defective.**

## Affiliates

| # | Pillar | Named | Live treatment |
|---|---|---|---|
| 1 | AI | `None` — **resolved from v1.0's flag.** No public programs. | PASS if absent |
| 2 | Pinterest | `None` | PASS if absent |
| 3 | **Content Creation** | **Canva** — the only pillar where Canva is correct | Carried on 11 articles; 10 are defects |
| 4 | Digital Products | `None` | PASS if absent |
| 5 | Affiliate Marketing | ⚠️ **Undecided — requires gate.** Amazon Associates is a teaching subject, not a recommendation. | Treat as `None` |
| 6 | Automation & Paid Traffic | **Make — recommended, unlinked** | Absence of link mechanics is a **PASS** |
| 7 | Email Marketing | ⚠️ **Beacons — terms unconfirmed.** Treat as unlinked until confirmed. | PASS if unlinked |
| 8 | Branding | `None` | PASS if absent |
| 9 | Business Systems | **Make — recommended, unlinked** | Absence of link mechanics is a **PASS** |
| 10 | Passive Income | `None` | PASS if absent |
| 11 | Mindset | `None` | PASS if absent |
| 12 | Blogging | `None` — Astro/Vercel/GitHub pay nothing; WordPress is the forced fit | PASS if absent |

**Seven of twelve pillars have no affiliate, correctly.** Two carry Make unlinked, correctly. One (Canva/Content Creation) is correct and misapplied to ten other pillars. Two require gate decisions.

---
---

# PART 5 — REQUIRES APPROVAL GATE

Decisions this document surfaces and does not make.

| # | Question | Source |
|---|---|---|
| 1 | **Pillar 7 slug collision** — A (re-slug supporting, 301), B (pillar takes different slug), C (promote live article to pillar) | Part 1 |
| 2 | **Pillar 9 title** — amend the live title to canon, or amend canon to the live title | Part 1 |
| 3 | **The word floor** — expand eleven under-length articles, accept as documented exception, or amend the floor | Finding 2 |
| 4 | **Pillar 5 affiliate** — name one, or record `None` permanently | Row 5 |
| 5 | **Pillar 7 affiliate** — confirm Beacons referral terms, or record `None` | Row 7 |
| 6 | **Pillar 8 entry product** — BAMI is unreleased; the pillar is blocked without one | Row 8 / open item 8 |
| 7 | **Pillar 10 entry rung** — beginner traffic at a live $27 VIP tier | Row 10 / open item 2 |
| 8 | **Blueprint segmentation** — load-bearing across four pillars, not three | Row 9 / open item 1 |

---

# ITEMS REMAINING OPEN

**Carried from Record v1.2 unchanged. Not re-litigated here.**

| # | Item | Status |
|---|---|---|
| 1 | Faceless Income Blueprint™ segmentation | **OPEN.** Now load-bearing across **four** pillars (4, 5, 9, 10), not three. Severity increased. |
| 2 | Passive Income ladder mismatch | **OPEN.** Severity increased — VIP confirmed live at $27. |
| 3 | Vacation Vault™ / Workout Vault™ checkout-bundle status | **OPEN** |
| 4 | Blueprint page 4 `[ INSERT ]` placeholder | **OPEN.** Live money link. |
| 5 | Repurposing Pack v2.1's six structural gaps | **OPEN.** Resolved by a v3.0 rewrite against this document, not a palette pass. |
| 6 | DFY Pinterest Package pricing scattered | **OPEN** |
| 7 | Kit migration timing undecided | **OPEN** |
| 8 | Pillar 8 (Branding) blocked — BAMI unreleased | **OPEN** |
| 9 | Pillar numbering ambiguous across documents | **OPEN.** This document uses **Resource Map row numbers**, 1–12, as listed in Part 2. Daily OS sequence slots are a different index. Not resolved. |

**Newly opened by this document:**

| # | Item | Source |
|---|---|---|
| **10** | **Per-pillar routing is unimplemented sitewide.** Twelve rows, one implementation, copy-pasted eleven times. | Part 0 |
| **11** | **No correspondence check exists** in any SOP or prompt. All of them pass the current site. | Finding 1 |
| **12** | **Eleven of eleven articles are below the word floor.** Largest unscoped body of work implied by this document. | Finding 2 |
| **13** | **BreadcrumbList schema does not exist.** Decision 7's stated compensating mechanism was never built. Action 7.9 is a build task, not a verification. | Finding 5 |
| **14** | **The newsletter ecosystem has no working entry point.** Two dead forms, sitewide, no shared logic. | Finding 6 |
| **15** | **Daily OS build order computed from a false inventory.** Logic sound, inputs wrong. Requires recomputation. | Finding 9 |

---

# STANDING RULES ADDED BY THIS DOCUMENT

| # | Rule |
|---|---|
| **24** | **The pillar defines the category label.** A category label is canon before it is code. Where a live article's category prop does not match MOM v3.0 Part 2's pillar table, the article is re-tagged; the table is not amended. |
| **25** | **Close-outs are audited by correspondence, not presence.** An article's free resource, paid resource, and affiliate are checked against its pillar's Resource Map row. A populated wrong route is a defect and outranks an empty one. |

**Hard-fail strings added:**

| String | Source |
|---|---|
| `AI & Automation` | v2.0, category label decision |
| `Automation` *(standalone category label)* | v2.0, category label decision |
| `Pretty & Paid Digital Vault` | Record v1.1 — **confirmed live, 3 occurrences** |
| `PLR Vault` *(as first reference)* | Record v1.1 — **confirmed live, 12 occurrences** |

---
---

# ACTION LIST

## ⚠️ SHIP FIRST

| # | Action |
|---|---|
| **A.1** | **Starter Map, live on Beacons — The Ads Edit™ → VIP, $27/month.** Record v1.2 action 15.2, unshipped. A live money page is telling readers the wrong price. Nothing else ships first. |
| **A.2** | **`shop/plr-vault.astro` lines 5, 6, 10 — remove `Pretty & Paid Digital Vault`.** A banned variant in the `<title>` and meta description is in every search result and every share preview. |
| **A.3** | **`membership.astro:21` — remove the Vault from the Premium inclusion list.** Record v1.1 action 4.14. Two live pages sell the same product two ways. |

## Routing implementation

| # | Action |
|---|---|
| B.1 | **`ArticleLayout.astro` — the `journey` block takes per-pillar routing.** The block is hardcoded. It must read the article's category and route to that pillar's row. This is one template change, not eleven article edits. |
| B.2 | **Re-tag `ai-for-online-business.astro:9`** — `AI & Automation` → `AI` |
| B.3 | **Re-tag `business-that-runs-without-you.astro:9`** — `Automation` → `Automation & Paid Traffic` |
| B.4 | **`learn/index.astro:14–15`** — remove both non-canon labels from the Library index |
| B.5 | **Build `/resources/canva-crash-course`** — the asset exists; only the page is missing. Cheapest free-resource route on the map. |
| B.6 | **Slug the Vault to `/shop/pretty-and-paid-plr-vault/`, 301 from `/shop/plr-vault`.** Record v1.1 action 4.8, unshipped. |
| B.7 | **All 12 `PLR Vault` short-form first references** → `Pretty & Paid PLR Vault™` |

## Infrastructure

| # | Action |
|---|---|
| C.1 | **`ArticleLayout.astro:111`** — the newsletter form has no handler. Build one. |
| C.2 | **`newsletter.astro:12`** — the second, independent dead form. Separate fix. |
| C.3 | **BreadcrumbList schema, all 21 pages** — does not exist. Decision 7 assumed it did. |
| C.4 | **Article + FAQPage schema** — does not exist on any page. |
| C.5 | **`ArticleLayout.astro` `journey` block — singular next step.** One CTA gains hierarchy; the rest recede. Template decision, one place. |
| C.6 | **Read time** — displayed values are not defensible at measured length. Resolve with Finding 2, not before. |

## Canon amendments

| # | Asset | Change |
|---|---|---|
| D.1 | **SOP Library v1.0** · **Prompt Library v1.0** · **Daily OS v1.0** — precedence stacks | Insert `Resource Map v2.0` at position 4, beneath Records v1.2/v1.1/v1.0. Renumber. |
| D.2 | **Every prompt's READ FIRST line** — Prompts 1, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 19, 20 | `Resource Map v1.0` → `Resource Map v2.0` |
| D.3 | **SOP 1** · **SOP 2** · **SOP 12 Phase B** · **Prompt 16** · **Prompt 20** | Add the correspondence check. Standing Rule 25. |
| D.4 | **Prompt 16** — affiliate audit | Check 3 tests absence. Add: a populated **wrong** affiliate is a defect. Canva on ten non-Content-Creation pillars is the worked example. |
| D.5 | **MOM v3.0, Part 2** — pillar table | Add Standing Rule 24. Category label is canon; the article re-tags. |
| D.6 | **MOM v3.0, Part 6** — curriculum-to-product map | Supersede its free/paid columns with Part 2 of this document. Two sources of truth is the failure this rewrite exists to end. |
| D.7 | **Daily OS, Part 1** — build order | Recompute against Part 1's inventory. Logic preserved, inputs replaced. Open item 15. |
| D.8 | **Daily OS, Part 1** — Pillar 8 row | 🟢 Clear → 🔴 **BLOCKED** (Record v1.2 action 15.13, unshipped) |
| D.9 | **Daily OS, Part 1** — Pillar 5 (Content Creation) row | Remove the Lesson 9 blocker. Gate lifted (Record v1.2 action 14.4). |
| D.10 | **Resource Map v1.0** | Superseded in full. Retain; do not delete. Header: `**SUPERSEDED BY RESOURCE MAP v2.0, 16 July 2026.**` |
| D.11 | **Record v1.2, action 7.9** | Scope-changed: verification → build. BreadcrumbList does not exist. |
| D.12 | **Record v1.2, open item 1** | Blueprint is load-bearing across **four** pillars, not three. Pillar 9 added. |

---

**The Digital Income Edit™ · Resource Map v2.0 · 16 July 2026**