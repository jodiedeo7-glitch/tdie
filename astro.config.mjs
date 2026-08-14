// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.thedigitalincomeedit.com',
  // Course pages are noindex,nofollow (CourseLayout). A noindex URL listed in
  // the sitemap is a contradictory signal to every crawler that reads both —
  // including Pinterest's. Filter them out.
  integrations: [sitemap({
    filter: (page) => !page.includes('/weekend-ecosystem/'),
  })],
  redirects: {
    '/shop/plr-vault': '/shop/pretty-and-paid-plr-vault/',
  },
});
