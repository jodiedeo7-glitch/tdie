// ── LAUNCH STAGE — change STAGE here and both the sales page and
// the preview page update together. Nothing else needs editing.
// "public67" | "full"   — launch stages retired, the course is open
export const STAGE = "public67";

export const CHECKOUT =
  "https://links.thedigitalincomeedit.com/shop/f7b54195-6a0e-4e95-8b92-fc203770176c";

const STAGES = {
  public67:  { cta: "Get the course \u2014 $67", href: "CHECKOUT", eyebrow: "Launch price \u00b7 $67",
               note: "$67 until 1 September. Then $97, permanently.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
  full:      { cta: "Get the course \u2014 $97", href: "CHECKOUT", eyebrow: "Standalone Course \u00b7 $97 one-time",
               note: "One-time payment, $97. Every future update included.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
};

export const S = STAGES[STAGE];
export const HREF = S.href === "CHECKOUT" ? CHECKOUT : S.href;
