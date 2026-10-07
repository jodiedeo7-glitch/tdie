// ─────────────────────────────────────────────────────────────
// LIFESTYLE · Jodie's founder Amazon storefront section (rebuilt 7 Oct 2026).
//
// One look = one JSON file in src/lifestyle/ plus its two founder pin images
// beside it. The founder pin factory writes them (recipe:
// ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md section 8c). Nothing here
// is written by hand. Format and rules: src/lifestyle/README.md.
//
// The record shape is the While-You-Sleep founder output structure
// (schema "wys-founder-1"): slug, title, date, category, season, intro,
// images [{ file: <slug>-pin1.jpg, alt }, { file: <slug>-pin2.jpg, alt }],
// listLink (the look's Amazon Idea List), items [{ name, link, note? }].
//
// Legacy records (the retired 24 Sep to 3 Oct layout: "ideaList",
// "-flatlay"/"-lifestyle" images, no schema) are refused here and by
// ops/scripts/validate_lifestyle.py, so an old writer can never put the
// retired presentation back on the site.
//
// Links are Jodie's own Amazon affiliate links. They ship with
// rel="sponsored nofollow noopener" and the Amazon disclosure as a set
// (Standing Rule 18). No prices are ever shown: Amazon prices change hourly.
// ─────────────────────────────────────────────────────────────

export const SCHEMA = "wys-founder-1";

// The ten departments of canon §6 (Decision 101). Slugs never change.
export const CATEGORIES = [
  { slug: "clothing",    name: "Clothing",    blurb: "Whole outfits, head to toe, every piece linked." },
  { slug: "accessories", name: "Accessories", blurb: "Bags, bows, dog gear and the little things that finish a look." },
  { slug: "jewelry",     name: "Jewelry",     blurb: "Stacks, pearls and the gold that goes with everything pink." },
  { slug: "beauty",      name: "Beauty",      blurb: "Nails, lips and a vanity that makes getting ready the fun part." },
  { slug: "perfume",     name: "Perfume",     blurb: "Pretty bottles that smell even better than they look." },
  { slug: "home-decor",  name: "Home Decor",  blurb: "Pink rooms and porches that still look grown up." },
  { slug: "dorm",        name: "Dorm",        blurb: "Dorm rooms your roommate will copy by Thursday." },
  { slug: "car",         name: "Car",         blurb: "Every red light, a photo shoot." },
  { slug: "books",       name: "Books",       blurb: "The reading list with a pink spine." },
  { slug: "gifts",       name: "Gift Guides", blurb: "Gifts for the girl who already owns everything pink." },
];

const lookFiles = import.meta.glob("../lifestyle/*.json", { eager: true, import: "default" });
const imageFiles = import.meta.glob("../lifestyle/*.{jpg,jpeg,png,webp}", { eager: true, import: "default" });

const stem = (p) => p.split("/").pop().replace(/\.(jpe?g|png|webp)$/i, "");
function imageFor(file) {
  const want = stem(file);
  const hit = Object.entries(imageFiles).find(([p]) => stem(p) === want);
  return hit ? hit[1] : null;
}

const catSlugs = new Set(CATEGORIES.map((c) => c.slug));
const AMAZON = /^https:\/\/(link\.amazon\/|amzn\.to\/|www\.amazon\.com\/)/;

// Returns a list of problems; an empty list means the record is valid.
export function problemsWith(l) {
  const p = [];
  if (!l || typeof l !== "object") return ["not a JSON object"];
  if (l.schema !== SCHEMA) p.push(`schema must be "${SCHEMA}"`);
  if ("ideaList" in l) p.push('legacy field "ideaList" (use "listLink")');
  if (!/^[a-z0-9]+(-[a-z0-9]+)*$/.test(l.slug || "")) p.push("slug must be lowercase words joined by hyphens");
  if (catSlugs.has(l.slug)) p.push("slug equals a category name");
  if (!l.title) p.push("title missing");
  if (!/^\d{4}-\d{2}-\d{2}$/.test(l.date || "")) p.push("date must be YYYY-MM-DD");
  if (!catSlugs.has(l.category)) p.push(`category "${l.category}" is not one of the ten`);
  if (!l.season) p.push("season missing");
  if (!l.intro) p.push("intro missing");
  if (/\$\s?\d/.test(l.intro || "")) p.push("intro contains a price");
  const imgs = l.images || [];
  if (imgs.length !== 2) p.push("exactly two images (pin1, pin2) required");
  imgs.forEach((im, i) => {
    if (stem(im.file || "") !== `${l.slug}-pin${i + 1}`) p.push(`image ${i + 1} must be ${l.slug}-pin${i + 1}.<jpg|png|webp>`);
    if (!im.alt) p.push(`image ${i + 1} alt text missing`);
  });
  if (l.listLink && !/^https:\/\/www\.amazon\.com\/shop\/thedigitalincomeedit\/list\/[A-Z0-9]+$/.test(l.listLink)) p.push("listLink is not an Idea List on the thedigitalincomeedit storefront");
  const items = l.items || [];
  if (!items.length) p.push("no items");
  items.forEach((it, i) => {
    if (!it.name) p.push(`item ${i + 1} name missing`);
    if (!AMAZON.test(it.link || "")) p.push(`item ${i + 1} link is not an Amazon affiliate link`);
  });
  return p;
}

const seen = new Set();
export const LOOKS = Object.entries(lookFiles)
  .map(([path, l]) => {
    const bad = problemsWith(l);
    if (bad.length) {
      console.warn(`[lifestyle] skipped ${path.split("/").pop()}: ${bad.join("; ")}`);
      return null;
    }
    if (seen.has(l.slug)) throw new Error(`Lifestyle: two looks share the slug "${l.slug}".`);
    seen.add(l.slug);
    const images = l.images.map((im) => ({ ...im, src: imageFor(im.file) }));
    if (images.some((im) => !im.src)) {
      console.warn(`[lifestyle] skipped ${l.slug}: an image file is missing`);
      return null;
    }
    return { ...l, images, items: l.items.filter((it) => it && it.name && it.link) };
  })
  .filter(Boolean)
  .sort((a, b) => String(b.date).localeCompare(String(a.date)) || a.title.localeCompare(b.title));

export const categoryOf = (slug) => CATEGORIES.find((c) => c.slug === slug);
export const looksIn = (slug) => LOOKS.filter((l) => l.category === slug);

export const DISCLOSURE =
  "As an Amazon Associate I earn from qualifying purchases. Every link on this page is an affiliate link: if you buy through it, I earn a small commission at no extra cost to you.";
export const AI_LINE =
  "The images on this page are AI-generated styling photos. The linked pieces may look slightly different in real life.";
export const REL = "sponsored nofollow noopener";
export const STOREFRONT = "https://www.amazon.com/shop/thedigitalincomeedit";
