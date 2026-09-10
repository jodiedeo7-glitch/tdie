// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

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
  integrations: [sitemap({
    filter: (page) =>
      !page.includes('/weekend-ecosystem/') &&
      !page.includes('/weekend-ecosystem-waitlist'),
  })],
  redirects: {
    '/shop/plr-vault': '/shop/pretty-and-paid-plr-vault',
  },
});
