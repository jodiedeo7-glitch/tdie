// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';
import { readdirSync, readFileSync, existsSync } from 'node:fs';

// Lifestyle departments with no looks yet are noindex (src/pages/lifestyle/[slug].astro),
// so they stay out of the sitemap. A look counts only in the founder schema with
// both pin images present, the same rule src/data/lifestyle.js builds from.
const LS_DIR = new URL('./src/lifestyle/', import.meta.url);
const LS_CATS = ['clothing', 'accessories', 'jewelry', 'beauty', 'perfume', 'home-decor', 'dorm', 'car', 'books', 'gifts'];
const lsLive = new Set();
for (const f of readdirSync(LS_DIR).filter((n) => n.endsWith('.json'))) {
  try {
    const l = JSON.parse(readFileSync(new URL(f, LS_DIR), 'utf8'));
    const imgs = (l.images || []).map((im) => im.file);
    if (l.schema === 'wys-founder-1' && imgs.length === 2 && imgs.every((n) => existsSync(new URL(n, LS_DIR)))) lsLive.add(l.category);
  } catch { /* the build's own loader reports bad files */ }
}
const lsEmpty = new Set(LS_CATS.filter((c) => !lsLive.has(c)).map((c) => `/lifestyle/${c}`));

// https://astro.build/config
export default defineConfig({
  site: 'https://www.thedigitalincomeedit.com',
  // Canonical URL form is no trailing slash (decided Sep 2026). Without this,
  // the sitemap emits /learn/foo/ while the layouts emit /learn/foo as the
  // canonical. Google reads that contradiction as a duplicate and drops the
  // page — it cost us all 26 /learn/ articles.
  trailingSlash: 'never',
  // Course pages are noindex,nofollow (CourseLayout). A noindex URL listed in
  // the sitemap is a contradictory signal to every crawler that reads both —
  // including Pinterest's. Filter them out. The waitlist page canonicals to
  // /shop/weekend-ecosystem, so it doesn't belong in the sitemap either.
  // Match on the path, not on a slash-terminated substring: with
  // trailingSlash 'never' the course index is /weekend-ecosystem with no
  // slash, and a '/weekend-ecosystem/' test lets it through. This one
  // condition covers the index, the modules and the waitlist, and leaves
  // /shop/weekend-ecosystem alone.
  integrations: [sitemap({
    filter: (page) => {
      const path = new URL(page).pathname.replace(/\/+$/, '');
      return !path.startsWith('/weekend-ecosystem') && !lsEmpty.has(path);
    },
  })],
  redirects: {
    '/shop/plr-vault': '/shop/pretty-and-paid-plr-vault',
  },
});
