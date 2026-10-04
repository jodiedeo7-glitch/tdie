## Development

When starting the dev server, use background mode:

```
astro dev --background
```

Manage the background server with `astro dev stop`, `astro dev status`, and `astro dev logs`.

## Documentation

Full documentation: https://docs.astro.build

Consult these guides before working on related tasks:

- [Adding pages, dynamic routes, or middleware](https://docs.astro.build/en/guides/routing/)
- [Working with Astro components](https://docs.astro.build/en/basics/astro-components/)
- [Using React, Vue, Svelte, or other framework components](https://docs.astro.build/en/guides/framework-components/)
- [Adding or managing content](https://docs.astro.build/en/guides/content-collections/)
- [Adding styles or using Tailwind](https://docs.astro.build/en/guides/styling/)
- [Supporting multiple languages](https://docs.astro.build/en/guides/internationalization/)

## Sales-page typography and deployment QA (Jodie, 3 October 2026)
Do not enlarge page headlines when editing copy. Sales pages use the shared scale in `src/styles/sales-typography.css`: H1 at most 52px on desktop and 36px on mobile; H2 at most 40px desktop and 30px mobile. Emphasis inherits its parent size. Avoid narrow 9ch measures, compressed line heights, clipping, and oversized stacked words. Preserve the Newsreader/Inter brand system.
For every page change, inspect rendered screenshots of all affected pages on desktop and mobile, including the complete page, images, spacing, heading hierarchy, buttons, navigation, and overflow. After deploying, repeat the visual audit against the actual public deployment and verify the new version is live. A successful build or deployment status alone is not visual QA. Fix visible issues before claiming completion. If live rendering is inaccessible, report the audit as blocked rather than claiming it passed.

## Actual production host
The public www.thedigitalincomeedit.com site is hosted on Cloudflare (worker `tdie-site`) and deploys from `cloudflare-migration`. Vercel is retired: ChatGPT migrated the site to Cloudflare after the Vercel free tier ran out of space. Do not reinstate Vercel and do not treat a Vercel status as proof of publication. Target the current production branch for public-site changes; verify the new content and CSS on the custom domain after deployment. Do not assume README snapshots establish public-site publication.

## Site-wide mobile design
`src/styles/mobile.css` applies to every page template, including articles, resources, lifestyle, link pages, and the course. Keep H1 at 30–36px, H2 at 26–30px, readable body text, 48px primary actions, wrapping labels, and zero document overflow at 320px and 390px. Grids must use `minmax(0, 1fr)` when a form or other intrinsic content can widen the track. Inspect the complete rendered mobile pages and interactive states; audit gated course content with repository HTML fixtures locally, without altering production access controls. Repeat public-site visual QA after deployment.
