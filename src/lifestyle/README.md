> WYS workflow authority: `claude/WYS_REFERENCE_PACK_2026-10-07.md`. This file documents website authoring only.

# Adding a Lifestyle article

Lifestyle uses the existing JSON files and photographs in this directory. You do not need to edit a route, card, category page or template for each article. `src/data/lifestyle.js` imports the records; the shared frame, cards and article component render them automatically.

## 1. Start with a draft

Copy `ops/lifestyle/article.example.json` into this directory as `<slug>.json`. Use a unique lowercase hyphenated slug. Do not use a category slug. Keep `status: "draft"` until the approved photographs and destinations have been reviewed. Missing status keeps legacy published behavior; use explicit status on new records. `draft: true` is also accepted for compatibility. Status is publication state, not an automatic date scheduler.

Drafts never appear in `astro build`, cards or sitemaps. For a local preview only:

```sh
ASTRO_TELEMETRY_DISABLED=1 LIFESTYLE_PREVIEW_DRAFTS=1 npm run dev -- --background
```

Open `http://localhost:4321/lifestyle/<slug>`. It is marked noindex and shows a local draft notice. Stop/status/logs: `npm run dev -- stop`, `npm run dev -- status`, `npm run dev -- logs`. Restart the dev server when changing the preview flag. A draft may reference expected approved image filenames while those assets are being transferred; missing draft images are omitted from the layout with a transfer notice. An empty image array is also allowed. Never use substitute photos or fabricated placeholders. A public article needs at least one real image and one complete product.

## 2. Fill the record

Required: `slug`, `title`, `category`, `images`, `items`. Add a natural `intro`, a unique concise `description`, and complete `sections` for a new article. Each section has a `heading` and a `paragraphs` array of plain text. Text is escaped automatically; do not insert HTML or private notes.

Categories (existing URLs): `clothing`, `accessories`, `jewelry`, `beauty`, `perfume`, `home-decor`, `dorm`, `car`, `books`, `gifts`. Seasonal decor uses `home-decor` plus `season`, for example `Halloween`. Do not create an empty duplicate category for a season. Articles marked `season: "Halloween"` automatically receive the founder-supplied pink ghost wallpaper and readable article panels. Other seasons, the hub and category pages keep their existing background. The supplied screenshot stays unchanged; CSS presentation clips out its app controls.

Optional `date` is a valid `YYYY-MM-DD` recorded publication/editorial date; ordering is descending date then ascending slug. It does not schedule publication. Existing future-dated records remain available for compatibility, but future dates are not emitted as `datePublished` structured data. Missing dates sort last. Homepage favorites are explicitly selected in `src/pages/lifestyle/index.astro`; new articles otherwise appear automatically in the grid.

## 3. Add approved photos

Put approved published web assets directly in this directory. Put private draft photographs in the Git-ignored `drafts/` subdirectory and reference them as `drafts/<filename>.png`. That folder is imported only during explicitly enabled development previews; production builds omit its assets even when the preview flag is set. Other directories, absolute paths and traversal are rejected. Astro imports dimensions and supplies responsive optimized images. Do not add private packs, sourcing screenshots, prompts, rejected images or social graphics. Preserve approved source files unchanged.

Each image needs `file` and meaningful `alt`. Recommended optional fields:

- `role`: `basic` (curated overhead arrangement with extras), `styled` (finished setting without a person), or `lifestyle` (Tommy Kate interacting with the setting).
- `caption`: what this perspective contributes; say which props are outside the shopping list where relevant.
- `order`: ascending numeric gallery order; omitted fields preserve array order.
- `hero`: `true` on at most one image. Default hero preference is styled, then lifestyle, then the first image.

One or two images work without empty slots. Legacy `-flatlay`/`-lifestyle` filenames get role fallbacks; decor and car images never inherit clothing captions. Unrecognized old filenames get a neutral styled-scene caption. Images keep their proportions in articles; cards use contain within a consistent frame.

Articles with enough styling sections pair the remaining photographs with successive groups of advice. Shorter records retain the plain prose and gallery layout. Keep sections concise; the template shows one complete disclosure and one article-level notice when all shopping destinations are pending. Related cards use articles with styled or lifestyle imagery, while the full browse grid retains legacy image records.

## 4. Verify shopping destinations

Products use the existing `items` array. Required public fields: `name`, `link`. Optional: `asin`, `variant`, `note`, `affiliateStatus`, `verifiedAt`.

- `affiliateStatus: "verified"`: only after the exact affiliate destination and product/variant were checked against evidence. Requires `verifiedAt` (date of that check). Store the evidence privately, not in page copy. Verification is an editorial record, not a guarantee of current stock or prices.
- `affiliateStatus: "none"`: an ordinary retail URL, without an affiliate claim.
- `affiliateStatus: "pending"`: keep the entire article draft unless separately authorized as a public inspiration article with `shoppingStatus: "pending"`; the template shows pending text rather than an unfinished shopping button.
- `legacy`: preserved existing destination. Omitted status defaults to legacy except ordinary Amazon `/dp/ASIN` URLs without a tag, which default to none. URL shape never proves affiliate verification. Legacy URLs are not silently upgraded to verified.

ASINs are ten uppercase letters/digits. Where an Amazon product URL exposes its ASIN, it must match the recorded ASIN. Short links need independent redirect/product readback before setting verified. Valid URL hosts are HTTPS `amzn.to`, `link.amazon`, `amazon.com`, `www.amazon.com`; extend that allowlist deliberately only with evidence and tests.

Use `variant` for sourced color/size/set details; do not invent quantities, dimensions, prices, ratings, discounts or availability. Do not name unlinked props as included products. LED tea lights are not real candles.

Optional `ideaList` must be an actual Amazon `/shop/<handle>/list/<id>` destination. `ideaListStatus: "verified"` records a checked list, `legacy` preserves an old list, `pending` requires a draft. For an unsubmitted list, omit the URL and keep the prerequisite in the private verification report. Never invent an ID.

## 5. Check and release separately

```sh
node --test ops/lifestyle/model.test.mjs
ASTRO_TELEMETRY_DISABLED=1 npm run build
```

Preview the article, category and hub at desktop, 390px and 320px. Inspect complete pages, images, captions, focus, links, metadata and one signup form. The unchanged signup posts to the existing MailerLite destination; do not submit or contact MailerLite during a design audit. Correct invalid public records fail the build rather than being silently skipped.

After photo and link review, set `status: "published"` only when the article is ready for a public build. Local implementation does not authorize publishing, pushing, deploying or submitting Idea Lists. Follow current founder release restrictions separately. Navigation, signup, footer, analytics, canonicals and the sitemap remain provided by the existing site. Never restore private publishing tests.

## Historical private Halloween checkpoint

`pretty-wicked-entryway.json` and `ghoul-fuel-coffee-bar.json` contain the complete copy, three role/caption/alt records and five source-matched products each. Their affiliate states remain pending and their Idea Lists are unsubmitted; no list URLs are invented.

All six approved PNGs were transferred from the two article-specific approved-photo ZIPs, visually inspected and copied unchanged to `drafts/<slug>-<role>.png`. The entryway lifestyle image is the approved porch-door replacement. SHA-256 hashes and original dimensions are recorded in `ops/lifestyle/APPROVED_PHOTOS.json`. Both complete three-photo articles passed the original technical desktop/mobile checks. Affiliate links and Idea Lists remain pending; neither article is published. Before any later authorized publication, move approved images out of `drafts/`, update the six paths, complete destination verification and follow release restrictions.

## Authorized public inspiration pages

The founder authorized publication of the completed Lifestyle rebuild and both Halloween articles in this chat on 7 October 2026 Eastern. The two records are published with `shoppingStatus: "pending"`; that explicit mode permits public inspiration pages while suppressing all pending product and list links. Their six approved source photos are now public assets. Other draft photographs remain private. The WYS customer product release hold, social publishing pause and affiliate verification requirements remain in force.
