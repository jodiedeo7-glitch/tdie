// src/data/article-dates.js
// Single source of truth for article publish dates, used by the RSS feed to
// order posts and tell subscribers what's new. When you publish a new article,
// add one line here with today's date. Slug must match the filename in
// src/pages/learn/ (without .astro). Articles missing from this map still
// appear in the feed, dated to the fallback below.

export const ARTICLE_DATES = {
  // Known live pillars (dated from the Corrections & Decisions Record / issue order).
  "how-to-build-a-faceless-digital-business": "2026-07-01",
  "automating-your-online-business": "2026-07-08",
  "ultimate-guide-to-ai": "2026-07-24",
  "digital-products-guide": "2026-07-24",
  "affiliate-marketing-101": "2026-07-24",
  "email-marketing-guide": "2026-07-24",
  "branding-guide": "2026-07-24",
  "passive-income-guide": "2026-07-24",
  "mindset-guide": "2026-07-24",
  "complete-blogging-guide": "2026-07-24",

  // Supporting + cluster articles already live. Dates are ordered by issue
  // number where known; adjust any you want to reflect true publish dates.
  "ai-for-online-business": "2026-06-20",
  "business-that-runs-without-you": "2026-06-24",
  "choosing-a-niche": "2026-06-10",
  "creating-your-first-offer": "2026-06-12",
  "pinterest-marketing-guide": "2026-06-14",
  "pinterest-seo": "2026-06-16",
  "complete-pinterest-marketing-guide": "2026-06-18",
  "content-creation-guide": "2026-06-22",
  "digital-products-for-beginners": "2026-06-26",
  "affiliate-marketing-for-beginners": "2026-06-28",
  "email-marketing-for-beginners": "2026-06-30",
  "blogging-guide": "2026-07-04",
};

// Any article not listed above falls back to this date so it still appears.
export const FALLBACK_DATE = "2026-01-01";
