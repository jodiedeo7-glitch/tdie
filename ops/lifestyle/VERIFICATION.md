> Historical private-draft checkpoint. The founder subsequently authorized website publication. See PUBLICATION.md for current release status; affiliate links and Amazon lists remain pending.

# Local Lifestyle verification, 7 October 2026

## Implementation

The existing Astro site now uses a Lifestyle-only shared frame, article layout, photo cards, categories and disclosures. `/lifestyle`, all ten category routes, all 22 existing article routes, and `/lifestyle/pink-finds` inherit the pink/cream/lavender design. Headlines are upright Newsreader, body/UI Inter. Category-specific introductions, explicit featured selection, date/slug ordering, readable product lists and one unchanged Pink Finds signup per page replace duplicated templates. The existing site navigation, footer, analytics and Cloudflare configuration are unchanged.

All 22 legacy JSON records, introductions, photographs, shopping URLs and Idea List URLs are unchanged. Single-photo and two-photo articles render without empty slots. Image-role metadata is optional; neutral category-aware captions replace the clothing-only and every-piece-linked assumptions. New articles inherit the layout automatically through the existing JSON import system. `src/lifestyle/README.md` documents the schema and preview/release process; `ops/lifestyle/article.example.json` is a reusable draft example.

## Halloween drafts

- `/lifestyle/pretty-wicked-entryway`: **Pink Halloween Entryway Decor**.
- `/lifestyle/ghoul-fuel-coffee-bar`: **Pink Halloween Coffee Bar**.

Both records contain finished introductions, four practical editorial sections, five product records, and three explicit image-role/alt/caption/order records. Names on the new pages omit source-only merchant brands. LED tea lights are correctly described as LEDs. Optional furniture, flowers, art, clothing and other props are identified separately. Shopping order is deliberate: hero and products together on desktop, hero then products then editorial copy/gallery on mobile. Missing-photo drafts retain a transfer notice. Both Halloween drafts now display their approved styled hero, basic arrangement and lifestyle view.

The original large handoff ZIP exceeded the download limit. The later two approved-photo ZIPs were successfully transferred and each contained exactly `basic.png`, `styled.png` and `lifestyle.png`. All six originals are RGB PNGs at 1024 × 1536. Each was visually inspected and copied byte-for-byte; SHA-256 comparisons and original dimensions are recorded in `APPROVED_PHOTOS.json`. Entryway lifestyle is the approved porch-door replacement, with the console receding behind Tommy Kate and the trick-or-treater in the foreground. Coffee lifestyle is the wider three-quarter coffee-making view. No photo was regenerated, cropped or substituted. The reference text supplied the sourcing descriptions; the original handoff sourcing JSON was not inspected directly.

The first build after photo integration revealed that eager public image imports emitted the six unused original PNGs even though draft routes were excluded. This was introduced by adding the photos and was fixed before completion: private draft photos now live in the Git-ignored `src/lifestyle/drafts/` folder, imported lazily only in explicitly enabled development previews. The model rejects private photo paths in published records. A clean production build with the preview flag deliberately enabled excludes both Halloween routes, their cards and sitemap entries, all six originals and their optimized derivatives. A future authorized release must move approved images to the public asset directory and update their paths.

## Checks actually passed

- Full `ASTRO_TELEMETRY_DISABLED=1 npm run build`: 165 site pages built, image optimization and sitemap generation successful.
- Eleven pure-model tests: legacy compatibility; category-aware role fallbacks; explicit role/order/hero; draft/staged exclusion; pending shopping protection; safe URL and ASIN checks; invalid public content; deterministic ordering; source verification flag; missing-photo draft behavior; private-photo path restrictions and traversal rejection.
- `python ops/lifestyle/check_build.py`: all 34 public Lifestyle HTML pages checked. Unique H1/title, canonical URLs, image alt/dimensions/asset presence, one signup, unique IDs, valid local links and fragment destinations, structured data and no private-path leakage. Legacy records/destinations unchanged. Both drafts absent from generated routes, public cards and sitemap.
- Chromium/Playwright: full-page desktop (1440px) and mobile (390px) screenshots captured for all 34 public Lifestyle pages. Complete-page layouts inspected through overview sheets, with readable-size inspections of the hub, signup, empty category, fashion and single-image articles. No overflow, missing Lifestyle images, unlabeled links, duplicate signups or oversized/italic headings. Unsupported arrow glyph and excessive featured-image side space corrected. Representative mobile product-heading scale corrected.
- Separate 320px checks: hub, populated category, sparse category, empty category, signup, existing fashion article, single-image decor article and both draft articles. Visible keyboard skip-link focus, anchor navigation, invalid-email error/focus without sending, and existing native mobile-menu opening passed.
- Both complete Halloween articles inspected at 1440px desktop and 390px mobile, with additional 320px checks. Styled hero appears beside shopping on desktop and before shopping on mobile; gallery shows basic then lifestyle. All six photos load, retain their 2:3 proportions, have unique accurate alt text and role captions, and use Astro responsive optimized sources. No horizontal overflow. Draft noindex, five pending products per article with no shopping buttons, absent Idea List links and one signup passed. Full-page and readable hero/copy/gallery screenshots are in `/workspace/work/lifestyle-qa/`; browser results are in `approved-photo-browser-results.json`.

- `git diff --check`: passed.

## Retail destinations versus affiliate links

Individually fetched all nine unique canonical retail URLs (ten product entries because the LED lights are shared). Each returned HTTP 200, the primary ASIN matched the record, and the returned title matched the source product. Evidence is recorded in `ops/lifestyle/HALLOWEEN_SOURCE_CHECKS.json`. Product variants/specifications in copy are attributed to the supplied dated source record; no live prices, discounts, ratings or stock claims are made.

These are ordinary retail URLs. Affiliate verification remains PENDING for every new product. Both five-product Idea Lists remain editor drafts NOT_SUBMITTED, without invented list URLs. The stale bats short link is not assigned to the mug. No existing affiliate URL was changed. Existing links are preserved as legacy rather than falsely upgraded to newly verified.

## Repository-wide canon audit

The audit remains **170 FAIL / 804 REVIEW**. Tracked HEAD has **168 FAIL / 803 REVIEW**. Comparing stable finding identities (severity, check, file and detail) finds no added or removed findings in implementation files. The difference is exclusively the unchanged, environment-provided, untracked `CLAUDE.md`: two hosting-history vocabulary matches and one shared-price review. Counts also match the snapshot taken immediately before photo integration.

Failure breakdown:

| Check | Count |
| --- | ---: |
| affiliate_missing_rel | 44 |
| bami_leak | 36 |
| retired_tier_vocabulary | 32 |
| affiliate_missing_disclosure | 23 |
| retired_module_number | 12 |
| price_floor | 9 |
| retired_vault_description | 7 |
| retired_colour_word | 3 |
| retired_blog_route | 2 |
| placeholder | 1 |
| vault_included_in_standard | 1 |

These combine existing content issues and context-blind text matches. Historical operational documents mention superseded names, curriculum numbers, membership descriptions and palette guidance. Other examples include external citation URL segments being treated as internal retired routes and hosting-history language being treated as membership terminology. The affiliate checks scan raw legacy JSON and require attributes nearby in that same source, although the shared rendered template supplies sponsored rel values and disclosures. Generated HTML checks independently passed those requirements for all 22 existing articles. Other source findings remain unresolved and should receive scoped review; this does not establish that every old failure is harmless.

REVIEW is manual triage, not an automatic failure: 537 shared-price matches, 98 prices absent from the register, 44 persona-description matches, 32 proof/screenshot matches, 27 destination-specific matches, 22 tier-comparison matches, 16 shortened-vault-name matches, 11 vault-bullet matches, 10 third-party-IP matches, 3 vault-lock-list matches, 2 scarcity/proof matches and 2 image-prompt hex matches. Some quoted prices apply to multiple registered products, so context is needed rather than rewriting an accurate price.

Detailed checkpoint comparison and check distributions are in `/workspace/work/lifestyle-qa/canon-audit-comparison.json` and `canon-audit-distribution.json`. No unrelated canon sources were edited or audit rules suppressed. The temporary image-build leak was introduced and corrected here; it was a build-privacy issue, not a new canon finding.

## Preview

In `/workspace/tdie`, the background dev server is running at `http://localhost:4321/lifestyle` with draft preview enabled. The two draft URLs above can be reviewed directly. No deployment is involved.

If restarting:

```sh
cd /workspace/tdie
ASTRO_TELEMETRY_DISABLED=1 LIFESTYLE_PREVIEW_DRAFTS=1 npm run dev -- --background --host 0.0.0.0
```

Manage with `npm run dev -- status`, `npm run dev -- logs`, `npm run dev -- stop`. A normal production build preview uses `npm run preview` and excludes both drafts.

## Exact remaining requirements

1. Before a later authorized release, obtain and verify the exact affiliate destinations. If submitting the optional Amazon lists later, follow action-time terms requirements and verify the resulting list URLs. This session did not authorize those actions. Do not invent tracking tags or relabel ordinary URLs as affiliate-verified.
2. Obtain separate explicit publication clearance, reconcile against the latest Cloudflare production branch, then perform public deployment QA only in that future authorized task.

## Publication state

NOT PUBLISHED. NOT DEPLOYED. NOT PUSHED. Nothing scheduled, submitted to Amazon, generated with paid credits, sent, or changed in an external account. No private publishing test or paused automation was restored. `sources/` was untouched.
