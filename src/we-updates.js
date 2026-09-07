// ── UPDATE LOG ───────────────────────────────────────────────────
// Newest first. Add an entry every time a module changes.
// `slug` must match the module's slug in we-manifest.js so the
// entry links straight to the changed module.

export const UPDATES = [
  {
    date: "2026-09-07",
    module: "Module 19 — Analytics & Search Console",
    slug: "module-19-analytics-search-console",
    what: "New section on the Meta Pixel, for anyone running ads. Your sales page and your checkout sit on two different domains, and the checkout host quietly installs the pixel for you — so Meta sees the purchase and never sees the page in front of it. Covers the one-ID rule, the Astro is:inline trap, double-counted checkout events, and why verification happens on the root domain.",
  },
  {
    date: "2026-08-30",
    module: "Module 1 — What You Already Own",
    slug: "module-1-what-you-already-own",
    what: "All four inventory prompts now tell the browser agent not to stop or ask for confirmation. It was pausing constantly and turning a twenty-minute job into a two-day one. Thanks to Gina for flagging it.",
  },
  {
    date: "2026-08-25",
    module: "Module 1 — What You Already Own",
    slug: "module-1-what-you-already-own",
    what: "Added full Claude in Chrome setup instructions, plus a section explaining that regular Claude can't browse the web. Three new troubleshooting entries covering the errors people were hitting.",
  },
];
