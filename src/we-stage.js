// ── LAUNCH STAGE — change STAGE here and both the sales page and
// the preview page update together. Nothing else needs editing.
// "prelaunch" | "launch37" | "public47" | "public67" | "full"
export const STAGE = "public67";

export const CHECKOUT =
  "https://links.thedigitalincomeedit.com/shop/f7b54195-6a0e-4e95-8b92-fc203770176c";

const WAITLIST = "/weekend-ecosystem-waitlist";

const STAGES = {
  prelaunch: { cta: "Join the waitlist", href: WAITLIST, eyebrow: "Opening soon \u00b7 Waitlist",
               note: "The waitlist opens Friday, three days early and at a lower price. Public access opens Monday 24 August.",
               access: "No payment now. You'll get one email when the doors open." },
  launch37:  { cta: "Get the course \u2014 $37", href: "CHECKOUT", eyebrow: "Launch day \u00b7 $37",
               note: "$37 until midnight tonight. $47 tomorrow.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
  public47:  { cta: "Get the course \u2014 $47", href: "CHECKOUT", eyebrow: "Launch weekend \u00b7 $47",
               note: "$47 this weekend. $67 from Monday.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
  public67:  { cta: "Get the course \u2014 $67", href: "CHECKOUT", eyebrow: "Launch price \u00b7 $67",
               note: "$67 until 1 September. Then $97, permanently.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
  full:      { cta: "Get the course \u2014 $97", href: "CHECKOUT", eyebrow: "Standalone Course \u00b7 $97 one-time",
               note: "One-time payment, $97. Every future update included.",
               access: "Access is tied to the email you buy with \u2014 use one you check. Access opens within a few hours of purchase." },
};

export const S = STAGES[STAGE];
export const HREF = S.href === "CHECKOUT" ? CHECKOUT : S.href;
