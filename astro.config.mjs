// @ts-check
import { defineConfig } from 'astro/config';
import sitemap from '@astrojs/sitemap';

// https://astro.build/config
export default defineConfig({
  site: 'https://www.thedigitalincomeedit.com',
  integrations: [sitemap()],
  redirects: {
    '/shop/plr-vault': '/shop/pretty-and-paid-plr-vault/',
  },
});
