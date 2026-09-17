# The Digital Income Edit™ — Website

Live at www.thedigitalincomeedit.com. Astro, deployed on Vercel from this repo's main branch. Every push to main rebuilds and republishes automatically, usually inside a minute.

learn.thedigitalincomeedit.com 301-redirects to www., path preserved.

## URLs

Flat — /learn/[slug], no trailing slash, no dates.

## Adding an article

Articles are .astro files in src/pages/learn/. This is not an Astro content collection, so a new article needs three edits, not one.

First, the article file itself, in src/pages/learn/. Second, a matching entry in the cluster array in src/pages/learn/index.astro. Third, a matching entry in src/data/article-dates.js.

Skip either of the last two and the article exists but appears nowhere — not in the library, not in the RSS feed, not in the newsletter that runs off the feed.

## Gotchas

ArticleLayout.astro routes the close-out CTAs by pillar category through the "related" prop. Never hardcode a journey slot.

The style tag in PageLayout.astro needs is:global, or it causes scoping bugs across other pages.

The Meta Pixel script needs is:inline so Astro does not bundle it.

## Canon

Governing documents live in ops/canon/. The live site, repo and shop override every document.
