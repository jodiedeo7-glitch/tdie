# THE DIGITAL INCOME EDIT™
## CORRECTIONS & DECISIONS RECORD
### v2.4 · Amendment — supersedes Corrections & Decisions Record v2.3 on all tier, pricing and entry-path matters
### Issued: 30 August 2026

---

## STATUS OF THIS DOCUMENT

**This is an amendment, not a full replacement.** Every decision in force under v2.3 remains in force except where this document contradicts it. On tier names, membership pricing, and the entry path, **this document wins.**

v2.3 and every record beneath it are superseded on those three subjects only and retained as historical artefacts. Records v1.0–v2.3 remain governing on everything else.

### Precedence stack

1. **Live site / live Skool configuration** — overrides every document
2. **Corrections & Decisions Record v2.4** — this document
3. **canon.json / TDIE_CANON.md**
4. **Resource Map v2.2**

---

# DECISION 81 — THE FREE TIER IS RETIRED

**Taken 30 August 2026. Closed.**

The free membership no longer exists. It is closed to new members and will not return.

**Rationale.** The free tier absorbed demand instead of converting it — free membership grew steadily while paid stayed flat. Free members could not see locked paid content, so the free experience exerted no pull toward the paid one. Rather than fix the visibility of locked modules, the tier itself was removed.

**Entry is now a free 7-day trial**, then $9/month. The trial is enabled in Skool at the group level.

**No asset may reference a free tier, a "Free Community," or free membership again.** Free lead magnets are unaffected and remain free; the ban covers membership tiers only.

---

# DECISION 82 — TIER RENAME

**Taken 30 August 2026. Closed. Do not re-raise.**

| Was | Now |
|---|---|
| Free Community ($0) | *retired* |
| Membership Premium ($9) | **Membership** — $9/month · $99/year |
| Membership VIP ($27) | **Membership Premium** — $27/month · $250/year |
| The VIP Vault | **The Premium Vault** |

There are exactly two tiers. The word *VIP* is retired brand-wide.

The Ads Edit™ remains in the top tier, which is now called Premium. This was settled previously and is not reopened by the rename.

---

# DECISION 83 — GRANDFATHERED MEMBERS

**Taken 30 August 2026. Closed.**

The 1,231 members who joined under the free tier are grandfathered permanently. They retain their existing access, are never charged, and require no action. Skool assigns them to the base tier card on the Tiers pricing model.

They do **not** receive Membership or Premium content by virtue of grandfathering. Any upgrade is a normal purchase.

---

# DECISION 84 — SKOOL LABEL DIVERGENCE

**Taken 30 August 2026. Open — accepted, monitored.**

Skool hard-codes its tier card labels as **Standard** and **Premium**. They are plain `<h3>` elements with no edit affordance; tested by click, double-click, keyboard, DOM inspection and pricing-mode switch. They cannot be renamed.

Consequence: site copy reads *Membership / Premium*; the Skool checkout reads *Standard / Premium*. Prices match; the first word does not.

**Accepted for now.** If it produces buyer confusion, the resolution is to change the site to *Standard*, not to fight the platform.

---

# DECISION 85 — SKOOL BENEFIT-EDIT DEFECT

**Taken 30 August 2026. Recorded for operational reference.**

Skool's tier benefit lists cannot be edited or deleted through the UI. The *Edit benefit* dialog exists but its click handler is never wired to the list items, and its Save and Delete requests return HTTP 400. Drag reordering does not persist. Adding is the only working operation, capped at six benefits per tier, with a seventh overwriting the sixth.

**Working method:** `PUT https://api2.skool.com/groups/{groupId}/membership-products/{productId}` with body `{"benefits": [...]}` — a plain array, not nested under `metadata`. Nested payloads return 200 and are silently discarded.

---

## STANDING RULES ADDED

**Standing Rule 31 — No free membership tier.** No asset, page, post, pin, email or graphic may offer, describe or imply a free membership tier. The entry offer is a free 7-day trial.

**Standing Rule 32 — Two tiers only.** Membership ($9) and Premium ($27). Any asset showing three tiers is stale and must be replaced, not annotated.

---

## ASSETS REQUIRING REPLACEMENT UNDER THIS RECORD

- ⬜ Skool group tagline — still reads "Premium and VIP Tiers"
- ⬜ Skool classroom module covers — 24 rendered, not yet uploaded
- ⬜ Pinned announcement post — still describes three tiers and a free path
- ⬜ Pinned START HERE post — still orients new members around a free path
- ⬜ VIP Vault module title and description inside Skool
- ⬜ "Daily Edits of the Past" and July calendar module descriptions — reference old tier names
- ✅ Website, canon.json, TDIE_CANON.md — updated 30 August 2026
