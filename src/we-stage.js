// ── LAUNCH STAGE — change STAGE here and both the sales page and
// the preview page update together. Nothing else needs editing.
// "full"   — launch ladder retired, settled price
export const STAGE = "full";

export const CHECKOUT =
  "https://links.thedigitalincomeedit.com/shop/f7b54195-6a0e-4e95-8b92-fc203770176c";

const STAGES = {
  full:      { cta: "Get the course \u2014 $97", href: "CHECKOUT", eyebrow: "Standalone Course \u00b7 $97 one-time",
               note: "One-time payment, $97. Every future update included.",
               access: "Access is tied to the email you buy with \u2014 use one you check. I unlock each purchase by hand, usually within the hour during waking hours, but please allow a few hours. You'll get an email the moment you're in." },
};

export const S = STAGES[STAGE];
export const HREF = S.href === "CHECKOUT" ? CHECKOUT : S.href;
