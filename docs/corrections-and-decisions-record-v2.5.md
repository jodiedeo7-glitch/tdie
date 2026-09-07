# THE DIGITAL INCOME EDIT™
## CORRECTIONS & DECISIONS RECORD
### v2.5 · Amendment — supersedes Corrections & Decisions Record v2.4 on all tracking, pixel and domain-verification matters
### Issued: 7 September 2026

---

## STATUS OF THIS DOCUMENT

**This is an amendment, not a full replacement.** Every decision in force under v2.4 remains in force except where this document contradicts it. On the Meta Pixel, event tracking and domain verification, **this document wins.**

Records v1.0–v2.4 remain governing on everything else.

### Precedence stack

1. **Live site / live Skool configuration** — overrides every document
2. **Corrections & Decisions Record v2.5** — this document
3. **canon.json / TDIE_CANON.md**
4. **Resource Map v2.2**

---

# DECISION 86 — ONE PIXEL, ONE ID, EVERY SURFACE

**Taken 7 September 2026. Closed. Do not re-raise.**

The live Meta dataset is **1274879031402082**, named *NurseMade Digital*, owned by the **NurseMade Naturals** business portfolio (ID 3694957180833890). It runs Conversions API and Meta Pixel together.

This one ID is installed on every surface in the funnel:

| Surface | Status |
|---|---|
| `www.thedigitalincomeedit.com` (Astro/Vercel) | Installed 7 Sep 2026 |
| `links.thedigitalincomeedit.com` (Beacons) | Pre-existing |
| `beacons.ai`, `shop.beacons.ai`, `account.beacons.ai` | Pre-existing |
| `www.skool.com` | Pre-existing |

**Root cause of the gap that made this necessary.** The checkout host installs its own pixel when an ID is pasted into its settings. That covered Beacons and Skool but never the Astro site, so Meta recorded purchases while never seeing the sales page in front of them. No retargeting audience of page-readers could exist. The repo confirmed it: no `fbq`, no `connect.facebook.net` anywhere in `src/`.

**Site implementation.** Base code plus `PageView` in the `<head>` of every layout that renders its own `<html>` tag. The tag must carry `is:inline` or Astro bundles and defers it out of the head.

**No client-side InitiateCheckout on the handoff link.** Beacons already sends Initiate checkout and Purchase. A second one double-counts.

---

# DECISION 87 — VERIFICATION IS ON THE ROOT DOMAIN

**Taken 7 September 2026. Closed.**

Meta verifies root domains only, never subdomains. **`thedigitalincomeedit.com`** is verified (asset ID 2928954904111736) and that single verification covers `www.` and `links.` and everything else beneath it.

Method used: DNS TXT at Porkbun. Host blank, value `facebook-domain-verification=ez227fq8aajppa81pknp97e3mhkoeh`, TTL 600. Verified 7 September 2026.

The meta-tag method was attempted first and failed: the `facebook-domain-verification` tag already in the site's `<head>` carries a different token. **That stale tag should be removed** — it verifies nothing and will mislead the next person who reads it.

---

# DECISION 88 — DEAD DATASETS, NOT DELETED

**Taken 7 September 2026. Open — accepted, monitored.**

Two further datasets exist in the same portfolio and have never received an event:

- **1210691560027826** — *NurseMade Naturals's pixel*. Zero events in 197 days. Has one connected catalog, so it is not fully orphaned.
- **1306967908291608** — *NurseMade Digital*. Zero events, no integrations.

Neither is deleted. Deletion is irreversible and the first one holds a catalog link. The risk they carry is that either ID gets pasted into a new surface by mistake, splitting the data. **Before pasting any pixel ID anywhere, confirm it reads 1274879031402082.**

---

# DECISION 89 — TWO OPEN DATA-QUALITY WARNINGS ON PURCHASE

**Taken 7 September 2026. Open — not fixable from the repo.**

Meta reports two warnings against the Purchase event, both originating at the checkout host, not the site:

1. Only **36%** of web Purchase events send a valid price in the correct format. Meta's target is 90%.
2. Every web Purchase event carries the **same value**, which normally indicates a hardcoded or missing price parameter.

Consequence: value-based optimisation and return-on-spend reporting are unreliable. Event match quality on the dataset sits at **6.1/10** with an update recommended.

Neither is fixable by changing the Astro site. The fix belongs in the Beacons product configuration, and Advanced Matching is a separate decision that has not been taken because it sends hashed customer data to Meta and carries its own consent considerations.

---

## STANDING RULES ADDED

**Standing Rule 33 — One pixel ID, forever.** Dataset **1274879031402082** is the only Meta dataset in use. Never create a new pixel for a new surface, however tempting the naming. Two IDs split the learning and neither half performs.

**Standing Rule 34 — Verify the root, never the subdomain.** Domain verification and its DNS TXT record live on `thedigitalincomeedit.com`. One record covers every subdomain.

---

## ASSETS REQUIRING REPLACEMENT UNDER THIS RECORD

- ⬜ Stale `facebook-domain-verification` meta tag in the site `<head>` — wrong token, remove it
- ⬜ Beacons Purchase event value parameter — sending a fixed or missing price
- ⬜ Dataset names in Events Manager — the two dead datasets are still named as though they were live
- ✅ Meta Pixel on every site layout — installed 7 September 2026
- ✅ Root domain verified in Meta Business Settings — 7 September 2026
- ✅ Module 19 of The Weekend Ecosystem™ — pixel section added and logged in the update log
