// ─────────────────────────────────────────────────────────────
// LIFESTYLE: Jodie's Amazon Influencer looks (approved 24 Sep 2026).
// Every look is one JSON file in src/lifestyle/ plus its images in
// the same folder. The Legally Blonde pin tasks add them; nothing
// here is written by hand. Format: src/lifestyle/README.md.
// Links are Jodie's own Amazon affiliate links. They ship with
// rel="sponsored" and the Amazon disclosure as a set (Standing
// Rule 18). No prices are ever shown: Amazon prices change hourly.
// ─────────────────────────────────────────────────────────────

export const CATEGORIES = [
  { slug: "clothing",    name: "Clothing",    blurb: "Full outfits, head to toe, every piece linked." },
  { slug: "accessories", name: "Accessories", blurb: "Bags, bows, sunglasses and the little things that finish a look." },
  { slug: "jewelry",     name: "Jewelry",     blurb: "Stacks, pearls and the gold that goes with everything pink." },
  { slug: "beauty",      name: "Beauty",      blurb: "Nails, lips and the vanity that makes getting ready the fun part." },
  { slug: "perfume",     name: "Perfume",     blurb: "Pretty bottles that smell even better than they look." },
  { slug: "home-decor",  name: "Home Decor",  blurb: "Pink rooms that still look grown up." },
  { slug: "dorm",        name: "Dorm",        blurb: "Dorm rooms your roommate will copy by Thursday." },
  { slug: "car",         name: "Car",         blurb: "Every red light, a photo shoot." },
  { slug: "books",       name: "Books",       blurb: "The reading list with a pink spine." },
  { slug: "gifts",       name: "Gift Guides", blurb: "Gifts for the girl who already owns everything pink." },
];

const lookFiles = import.meta.glob("../lifestyle/*.json", { eager: true, import: "default" });
const imageFiles = import.meta.glob("../lifestyle/*.{jpg,jpeg,png,webp}", { eager: true, import: "default" });

function imageFor(file) {
  const hit = Object.entries(imageFiles).find(([p]) => p.endsWith("/" + file));
  return hit ? hit[1] : null;
}

const catSlugs = new Set(CATEGORIES.map((c) => c.slug));

export const LOOKS = Object.values(lookFiles)
  .filter((l) => l && l.slug && l.title && catSlugs.has(l.category))
  .map((l) => ({
    ...l,
    images: (l.images || [])
      .map((im) => ({ ...im, src: imageFor(im.file) }))
      .filter((im) => im.src),
    items: (l.items || []).filter((it) => it && it.name && it.link),
  }))
  .filter((l) => l.images.length && l.items.length)
  .sort((a, b) => String(b.date).localeCompare(String(a.date)));

export const categoryOf = (slug) => CATEGORIES.find((c) => c.slug === slug);

export const DISCLOSURE =
  "As an Amazon Associate I earn from qualifying purchases. Every link on this page is an affiliate link: if you buy through it, I earn a small commission at no extra cost to you.";
