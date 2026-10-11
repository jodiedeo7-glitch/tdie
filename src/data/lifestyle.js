// One JSON record per article in src/lifestyle. See src/lifestyle/README.md.
import { normalizeLook, byEditorialDate, isDraft } from './lifestyle-model.js';
export const CATEGORIES = [
  { slug: 'clothing', name: 'Clothing', blurb: 'Halloween costumes you can wear again in November and everyday pink outfits, with every piece listed underneath.' },
  { slug: 'accessories', name: 'Accessories', blurb: 'Bags, bows and little finishing touches, plus playful finds for your four-legged sidekick.' },
  { slug: 'jewelry', name: 'Jewelry', blurb: 'A place for pearls, stacks and small sparkling details.' },
  { slug: 'beauty', name: 'Beauty', blurb: 'Pretty touches for your vanity and getting-ready routine.' },
  { slug: 'perfume', name: 'Perfume', blurb: 'A collection for fragrance finds and pretty bottles.' },
  { slug: 'home-decor', name: 'Home Decor', blurb: 'Pink porches, coffee bars and entryways that still say Halloween. Copy the whole look or just one corner.' },
  { slug: 'dorm', name: 'Dorm', blurb: 'Pink Halloween decor that fits one small room and the housing rules: no flames, no nails, packs flat in November.' },
  { slug: 'car', name: 'Car Accessories', blurb: 'A pink steering wheel, matching seat belt covers and a real spot for your phone, your iced coffee and the trash.' },
  { slug: 'books', name: 'Books', blurb: 'A place for reading lists and books worth making space for.' },
  { slug: 'gifts', name: 'Gift Guides', blurb: 'Thoughtful finds for the people who love a little pink.' },
];
const records = Object.values(import.meta.glob('../lifestyle/*.json', { eager: true, import: 'default' }));
const imageFiles = import.meta.glob('../lifestyle/*.{jpg,jpeg,png,webp}', { eager: true, import: 'default' });
// Private photographs are imported only in explicitly enabled development previews.
if (import.meta.env.DEV && process.env.LIFESTYLE_PREVIEW_DRAFTS === '1') {
  const draftImages = import.meta.glob('../lifestyle/drafts/*.{jpg,jpeg,png,webp}', { import: 'default' });
  for (const [path, resolve] of Object.entries(draftImages)) imageFiles[path] = await resolve();
}
const imageFor = file => imageFiles[`../lifestyle/${file}`];
export const LOOKS = records.map(record => normalizeLook(record, imageFor, CATEGORIES)).filter(Boolean).sort(byEditorialDate);
// Draft routes exist only in the explicitly enabled dev server, never astro build.
export const DRAFT_LOOKS = import.meta.env.DEV && process.env.LIFESTYLE_PREVIEW_DRAFTS === '1'
  ? records.filter(isDraft).map(record => normalizeLook(record, imageFor, CATEGORIES, { preview: true })) : [];
const slugs = [...LOOKS, ...DRAFT_LOOKS].map(l => l.slug);
if (new Set(slugs).size !== slugs.length) throw new Error('Duplicate Lifestyle article slug');
export const categoryOf = slug => CATEGORIES.find(category => category.slug === slug);
export const DISCLOSURE = 'As an Amazon Associate I earn from qualifying purchases. Shopping sections may contain affiliate links. If you buy through an affiliate link, I may earn a commission at no extra cost to you.';
export const IMAGE_NOTICE = 'AI-generated styling inspiration. Retail products may differ; check the actual listing photographs, contents and measurements. Flowers, furniture, artwork, clothing and other props are styling extras.';
