// The Keep It Running Kit bonus window (canon Decision 105).
// One deadline for every place the Kit is named: KitBanner and the "I'll do it later" objection.
export const KIT_DEADLINE = "2026-10-05T03:59:00Z"; // Sunday 4 October 2026, 11:59 pm Eastern
export const kitLive = () => Date.now() < Date.parse(KIT_DEADLINE);
