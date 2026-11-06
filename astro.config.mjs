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
  // Match on the path, not on a slash-terminated substring: with
  // trailingSlash 'never' the course index is /weekend-ecosystem with no
  // slash, and a '/weekend-ecosystem/' test lets it through. This one
  // condition covers the index, the modules and the waitlist, and leaves
  // /shop/weekend-ecosystem alone.
  integrations: [sitemap({
    // The While-You-Sleep Storefront™ buyer website is private (studio-<key>): never in the sitemap.
    // Internal previews and link-in-bio pages are also noindex, so listing them
    // here would give crawlers a contradictory index/noindex signal.
    filter: (page) => {
      const pathname = new URL(page).pathname;
      const noindexPrefixes = [
        '/brand-reference',
        '/header-options',
        '/ig',
      ];
      return !pathname.startsWith('/weekend-ecosystem')
        && !noindexPrefixes.some((prefix) => pathname === prefix || pathname.startsWith(`${prefix}/`))
        && !pathname.includes('/while-you-sleep-storefront/studio-')
        && !pathname.includes('/while-you-sleep-storefront/jodie-inbox-');
    },
  })],
  redirects: {
    '/shop/plr-vault': '/shop/pretty-and-paid-plr-vault',
  },
});
