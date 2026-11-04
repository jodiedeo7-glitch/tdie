# Lifestyle implementation, 7 October 2026

## Checkpoint and inventory
- Clean local checkout `6c924f6`, branch `work`, matching current remote main. Read-only fetch confirmed Lifestyle code matches Cloudflare production branch. No pushing or deployment authorized.
- 22 existing JSON articles; ten category URLs. Clothing 16, home decor 3, accessories 1, car 1, dorm 1; five empty categories. Seventeen two-image articles and five one-image articles. Also preserve and update `/lifestyle/pink-finds`, the dedicated signup URL. Dates include existing future-dated records; preserve them without claiming daily publication.
- Current routes duplicate cards and signup forms, infer clothing from filenames, overpromise that every photographed piece is linked, and use very large headings. No current rendered audit assumed.
- Framework: Astro 7, local image pipeline, static paths, existing PageLayout/navigation/footer/analytics, Cloudflare worker and no-trailing-slash canonical/sitemap conventions. Official routing/components/content/styling/images documentation consulted.
- The original large handoff pack exceeded the transfer limit. The later approved-photo ZIPs supplied all six originals, now integrated unchanged in the private draft asset folder. Both three-photo articles passed desktop/mobile inspection. Affiliate destinations and Idea Lists remain pending; see VERIFICATION.md.

## Hierarchy and visual direction
- `/lifestyle`: natural introduction, explicitly selected featured articles, populated categories first, then all articles sorted by record date with slug tie-break. No search widget needed for 22 articles.
- Preserve all ten category routes, with breadcrumbs, category-specific introduction, counts and consistent cards; empty categories offer existing populated alternatives.
- Existing `/lifestyle/[slug]` routes delegate to a reusable article component. Hero and shopping are adjacent on desktop; on mobile hero is followed by shopping and then editorial copy/gallery. No sticky shopping panel.
- Scope design to Lifestyle: Newsreader upright headings (52px maximum, 36px mobile), Inter body, cream, lavender, pink accents, crisp outlines, occasional flower/badge details, complete proportional images. Preserve unrelated styles.

## Components and content compatibility
- Shared frame, card grid, category navigation, disclosure, article. Reuse existing PinkFindsSignup once per page and existing footer/navigation.
- Keep JSON in `src/lifestyle`, preserve legacy records. Optional roles/basic-styled-lifestyle, captions, order, hero designation, sections, description, draft status, item ASIN/variant/affiliate status and verified Idea List metadata.
- Legacy filenames only identify generic arrangement/lifestyle roles. Clothing language requires a clothing category; neutral captions for other categories. Product links are not inferred verified from a URL shape.
- Missing status retains published legacy behavior. Explicit drafts are excluded by default; dedicated local draft preview is noindex and sitemap-excluded. Pending destinations cannot enter normal builds. Halloween prose drafts can be reviewed locally but source-specific completion depends on the missing approved pack.
- Authoring guide and example use this same schema; fail actionable invalid public records rather than silently dropping content.

## Verification
- Node tests for migration fallbacks, drafts, destination/ASIN validation, explicit roles/order and collision protection.
- Full Astro build, generated HTML checks for all Lifestyle routes, internal links, image/alt/caption presence, one signup, canonicals and sitemap/private exclusions. Compare legacy product destinations/content unchanged.
- Chromium/Playwright full-page screenshots and actual inspection of all 33 public Lifestyle pages at desktop and mobile; representative 320px overflow, keyboard, menu and signup invalid-state checks without submitting forms. Draft preview inspected separately.
- Keep local implementation, visual QA, link evidence, external prerequisites and publication status separate. No deploy, push, list submission, paid generation, schedule or account writes.
