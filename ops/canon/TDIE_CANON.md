# THE DIGITAL INCOME EDIT™ — CANON
### v1.0 · 16 August 2026 · Consolidation

**What this is.** One document replacing the reconciliation layer. Built from Product Register v3.1 (amending v3.0), Corrections & Decisions Record v2.1, Resource Map v2.1, SOP Library v1.1, Prompt Library v1.7, Master Operating Manual v3.0.

**What changes on adoption.** The Records stop being *governing* documents and become an append-only changelog. Nothing is deleted — Standing Rule 19 still holds, and the historical texts stay as reference. What ends is six documents each claiming a slice of authority over the same facts.

**Machine half.** Every enforceable fact below also lives in `canon.json`, which `tdie_audit.py` reads. When a price or a rule changes, it changes in `canon.json` and here, on the same day. A rule that isn't in `canon.json` isn't enforced by anything but memory.

---

## 1 · PRECEDENCE

1. **The live site, repo and shop.** They override every document, including this one. A document-asserted defect is verified against the live system before it is fixed (Standing Rule 31).
2. **This document.**
3. Historical records — reference only, not governing.

**The version rule.** Where two versions of anything exist, the higher number is canon. Do not ask which to use.

**Conflicts are flagged, never resolved silently** — once, before proceeding. A closed item stays closed and is not raised again.

---

## 2 · STANDING FACTS

| | |
|---|---|
| **Canonical host** | `https://www.thedigitalincomeedit.com` |
| **Redirecting hosts** | `thedigitalincomeedit.com` and `learn.thedigitalincomeedit.com` — both 308 to www. An asset printed with a redirecting host is printed wrong. |
| **Retired domain** | `nursemadedigital.com` |
| **Repo** | `jodiedeo7-glitch/tdie` — Astro on Vercel |
| **Article route** | `/learn/[slug]`, flat. `/blog/` is retired as segment, label and page-type name. |
| **Community** | Skool · `skool.com/thedigitalincomeedit` |
| **Shop** | Beacons · `links.thedigitalincomeedit.com` — not fetchable, not indexed, unverifiable by tooling |
| **Email** | MailerLite (Decision 67, resolving 63) |
| **Tool stack** | Astro · Vercel · GitHub · Skool · Beacons · Canva · Claude · Pinterest native. Nothing outside this list. |

**The New Faceless.** Faceless means the founder's real face is never required — not that no person appears. The brand's face is its AI persona, referenced only by the canonical seed image at `/public/images/library/avatar-seed-omni-reference.png` as "this exact woman." Never described in words.

---

## 3 · THE LADDER

| Product | Price | Platform |
|---|---|---|
| Membership Standard | $9/month · $99/year | Skool |
| Membership Premium — includes The Ads Edit™ | $27/month · $250/year | Skool |
| The Business Architect Mentorship Intensive™ | ⬜ pending | Skool |

BAMI supersedes the retired name Faceless Income Intensive™. **It is not live and is stripped from every asset until it launches.**

**Pinterest Foundations™ — $27 one-time, Skool.** Also included with Membership Standard. That is inclusion, not a ladder rung. No `/shop/` route is to be built for it.

---

## 4 · THE THREE VAULTS — NEVER CONFLATED

| Name | What it is |
|---|---|
| **The Value Vault** | Guide collection inside Skool. Browsable by all members; guides bought à la carte ($2–$10) or the whole collection for $49. |
| **The Premium Vault** | The entire Value Vault unlocked, included with Membership Premium. |
| **Pretty & Paid PLR Vault™** | Separate $11/month Beacons subscription. Off-ladder. |

**Pretty & Paid PLR Vault™ carries its full prefix and trademark on every first reference.** Short form is banned outright in every title, overlay, heading, button, anchor and alt text — those are first-reference positions with no second reference behind them.

**The Vault and any membership tier never appear in the same asset**, never on adjacent days, and are never framed as related products. Frame by question, never by price.

---

## 5 · PRODUCTS

Full table with exact prices and live URLs: **`canon.json` → `products[]`.** Thirty rows, nine affiliate, twenty-one owned.

**Rule of use.** No asset ships naming a product, price, or link that is not a row in that file. If it isn't there it doesn't get written — and it doesn't get deleted either.

### Price collisions

Seven prices are shared. `tdie_audit.py` computes the table from `canon.json` on every run, so it cannot go stale. The two that matter:

- **$9** — Membership Premium (recurring) vs a Pinterest guide (one-time)
- **$27** — Membership Premium (recurring) vs three one-time products

**Standing Rule 32.** Every price written into an asset is checked against the computed collision table, not against a remembered list of numbers. Wherever two products share a price on one screen, the copy names what each price buys before the reader has to work it out.

**Standing Rule 10.** Exact prices. Never `from $`. Changed deliberately, everywhere, on one day. Applies to owned products only.

### Affiliate — Standing Rule 18

**The link, `rel="sponsored"`, and the disclosure ship as a set or not at all.** Never quote a sale price on a product you don't own — publish list price. Verify quarterly that each still exists. **Affiliate products never occupy a pillar's paid slot.**

### Flagged, not cut

Named in canon, no confirmed live listing. Do not write into an asset until confirmed: Luxe Babe Prompt Pack · Vacation Vault™ · Workout Vault™ · AI CEO Planner™ · Vault Unlock ($49) · DFY Pinterest packages.

---

## 6 · CONTENT

**All twelve pillars are live** (Decision 66). Slugs of record are in `canon.json → pillars[]`.

> **Standing Rule 59.** The pillar library is the spine; clusters hang off it. New content is supporting articles under a pillar, not new pillars.

### Journey slots

- **Free slot: $0 only** (Standing Rule 60). Topical relevance never overrides this. A price in a free slot is a defect.
- **Paid slot: never an affiliate product.**
- **Close-out: at most one price.**

### Linking

Every new article sends 3–8 related links plus its lead magnet, product, membership and pillar — **and receives links from its pillar guide and relevant siblings.** Outbound always gets done; inbound never does. That is the orphan failure, and it is now checked by machine.

### Voice

Founder with opinions. Tension, curiosity, specificity. Never *learn how*, *here's a guide*, *this week's article*, *check out my latest post*.

**Banned brand-wide:** hack · secret · explode · crush it · game-changer · manufactured urgency · fabricated scarcity · fabricated social proof · income frequency claims.

**Banned near the Vault:** upgrade · downgrade · tier · level · step up · next step · plan.

**Banned on Pinterest:** "Make Money Online" and keyword-stuffed variants.

**Community-facing posts** use the warm, casual, emoji-forward register — short lines, heavy white space. Editorial and site copy use the luxury-editorial mentor register. These are two voices and they do not mix.

**Income claims** are permitted on every surface except Meta platforms.

---

## 7 · DESIGN

**Palette — exact hex, mandatory in every image prompt. A colour name without a hex is a fail.**

| | |
|---|---|
| Signature Hot Pink | `#D62E73` |
| Luxury Cream | `#FBF8F5` |
| Dark Chocolate | `#2B161B` |
| Muted Gold | `#C8A96A` |
| Bubblegum Pink | `#FF8AC2` |
| Lavender | `#CBB7F7` — never dominant |

Magenta, deep plum and antique gold are retired.

**Type.** Fraunces (display) · Cormorant Garamond (serif; the italic carries the turn line) · Inter (sans; eyebrows and lockups only). One to two families per asset. Fraunces variable axes load in the order `[opsz, wght, SOFT, WONK]` — wrong order silently applies default weights.

**Tier badges.** Standard `#FF8AC2` · Premium `#D62E73`. There is no free tier badge.

**Text is set, never generated — for nano banana (Gemini) only.** Canva AI renders text accurately; do not strip text from Canva prompts or warn about garbled letterforms. *(This resolves the open contradiction between Prompt Library v1.7's blanket rule and the Canva AI correction.)*

**Aesthetic.** "Her real life, shot beautifully" — lived-in modern farmhouse, real slow country life. Not staged, not costume cottagecore. Wardrobe locked: oversized pink knits, soft tees, hoodies, sweatpants, leggings, fuzzy socks, gold claw clip. Blouses, blazers and costume cottagecore are banned. Signature prop: glitter-flecked pink iced coffee tumbler with lavender straw, in every frame with her.

**Hard third-party IP ban** in every generated image prompt and listing. This has caused platform deactivations.

---

## 8 · SECURITY

**GitHub tokens are generated fresh per session, minimally scoped, and revoked when the session ends** — not soon, not at end of day. Revocation confirmed in the GitHub UI.

Weekly: zero live tokens. Any survivor gets revoked **and the reason it survived gets recorded.** The record is the deliverable; the revocation takes ten seconds.

`history -c 2>/dev/null; unset GH` after every session. Working copies removed with `rm -rf`.

**No automation outside the named stack.** Anything else is undocumented, unmaintained, and a single point of failure nobody is watching.

---

## 9 · WHAT THIS DOCUMENT DOES NOT CLOSE

Decisions, not process. No amount of correct execution resolves them.

| Item | Blocks |
|---|---|
| BAMI price and live URL | The ladder's top rung; Blueprint page 9 |
| Value Vault ledger count | Every "total value" claim in Vault marketing |
| Four Skool module tier assignments — AI Twin/Influencer Creation, Monetization Edit, Content Edit, Pinterest Edit | Module cover production |
| Gold and Lavender badge colours for standalones and member rewards | Currently proposed, not canon |
| Nineteen live shop products routed to no pillar | Nineteen assets earning nothing from site traffic |
| Per-pillar freebies replacing the shared Blueprint fallback | Welcome-sequence segmentation |
| Inactive *WAITLIST* product deletion in Beacons | Nothing — but it carries the retired domain |

---

**The Digital Income Edit™ · Canon v1.0 · 16 August 2026**

---

## TIER RENAME — 30 AUGUST 2026

The free tier is retired. Entry is now a **free 7-day trial**, then $9/month.

| Was | Now |
|---|---|
| Free Community ($0) | *retired* — replaced by a free 7-day trial |
| Membership Premium ($9) | **Membership Standard** ($9/mo · $99/yr) |
| Membership VIP ($27) | **Membership Premium** ($27/mo · $250/yr) |
| The VIP Vault | **The Premium Vault** |

1,231 members who joined under the free tier are grandfathered permanently and are never charged.

**Skool platform caveat.** Skool hard-codes its tier card labels as *Standard* and *Premium* and they cannot be edited. Site copy now says Standard / Premium to match the Skool checkout exactly.
