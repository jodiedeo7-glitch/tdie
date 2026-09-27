// Live facts, one place. Every price, count and trial length the site prints
// in a structured spot (cards, price blocks, CTAs, stat strips) reads from here.
// Source of record: ops/canon/canon.json. Change a fact here and in canon.json
// on the same day, or it has not changed.
//
// Membership Premium: canon Decision 114 (24 Sep 2026) quotes $35/month ·
// $297/year on every asset ahead of the Skool checkout change at 11:59 pm
// Eastern, 30 Sep 2026. If Skool's /plans page ever disagrees with these
// figures, Skool is what the customer is charged, and this file is wrong.

import { pillars, articles } from "./library.js";

export const SKOOL_PLANS = "https://www.skool.com/thedigitalincomeedit/plans";

export const membership = {
  trialDays: 7,
  trial: "7-day free trial",
  standard: {
    name: "Membership Standard",
    short: "Standard",
    monthly: "$9",
    annual: "$99",
    perMonth: "$9/month",
    perYear: "$99/year",
  },
  premium: {
    name: "Membership Premium",
    short: "Premium",
    monthly: "$35",
    annual: "$297",
    perMonth: "$35/month",
    perYear: "$297/year",
  },
};

export const weekendEcosystem = {
  name: "The Weekend Ecosystem™",
  price: "$97",
  plan: "3 × $33.33",
  modules: 22,
  prompts: 36,
  assetsPerArticle: 24,
  url: "/shop/weekend-ecosystem",
  preview: "/weekend-ecosystem/preview",
};

export const community = {
  members: "1,200+",
};

// Counts resolve from the library data itself, so the homepage, About,
// Free Resources and the Library can never disagree again.
const WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
  "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty"];
export const word = (n) => WORDS[n] ?? String(n);
export const cap = (s) => s.charAt(0).toUpperCase() + s.slice(1);

export const library = {
  guides: pillars.length,
  articles: articles.length,
  total: pillars.length + articles.length,
  guidesWord: word(pillars.length),
};
