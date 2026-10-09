## WYS authority (Jodie, 7 October 2026)

Read `claude/WYS_REFERENCE_PACK_2026-10-07.md` in full before WYS founder or customer-product work. It is the sole complete WYS operating document: current source, exact approved prompts, reference roles, sourcing, state, permissions/spending, manual/mixed paths, website migration, publication and test/release gates. Superseded recipes and instruction packages must not be restored from history or runtime snapshots. General TDIE image defaults do not select a WYS generator. SOP-15 and SOP-16 remain separate.

WYS generation remains PAUSED. Provider/model are unverified; do not infer them. Repository consolidation does not prove that Claude Project documents, skills or scheduled task copies were updated. Codex owns /lifestyle implementation; no competing old page writer may run. The customer release hold remains active. Keep independent code work moving; never describe staging, a documentation edit or a build as live publication.



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

## While-You-Sleep founder autonomy (1 October 2026)
For While-You-Sleep founder work, execute the entire authorized pipeline automatically. Inspect current canon, repository instructions, connected production records and live state before acting. Carry work through Amazon intake and destinations, Pinterest, blog/SEO, the Weekend Ecosystem soft upsell, Instagram, approvals, scheduling, logs and verification.
Do not stop at a plan, audit, draft, PR, connector failure or successful API response. Complete every available authorized step and verify resulting live behavior. Repair routine source, connector, formatting and state failures without returning them to Jodie. Use supported alternative routes, safe retries and readback. Reconcile uncertain writes before retrying to prevent duplicates.
Continue independent work when one dependency is blocked. Preserve checkpoints and a precise resumable next action. A hard stop exists only when available authorized routes are exhausted and the remaining action requires Jodie's input, unavailable access or a permission that has not been granted. Never claim a capability or connection is available without checking.
Use existing approvals and authorizations without asking again. Do not add discretionary approval gates to routine reversible work. Existing explicit publishing, spending and customer-release restrictions remain applicable until Jodie specifically changes them; automation intent alone does not invent a budget or approve an unreviewed asset.
Keep founder automation, the customer kit, Daily Prompts and Premium DFY Calendar separate. Maintain one publishing writer and reconcile legacy ownership before cutover. Never substitute manual customer alternatives for completion of the founder's automatic workflow.
Verify each actual write by supported readback and each live claim against current evidence. Distinguish prepared, scheduled, published and delivered. Keep failures UNVERIFIED until tested; instruction edits are not evidence that the pipeline works.
Handle small failures quietly. Report only verified completion or one genuine blocker requiring Jodie, with the exact action needed. Do not tell her to perform anything that available authorized tools can complete.

**MailerLite access rule (Jodie, 2 October 2026).** MailerLite is connected to Claude as a plugin (`mcp__MailerLite__` tools). Every MailerLite read, count, draft, campaign, test send, schedule, automation edit and report goes through that plugin. **MailerLite is never opened in any browser** (Claude in Chrome, the Claude built-in browser or any other), not to read, not to check, not to upload, not as a fallback, not for a step the plugin cannot do. If the plugin cannot do a MailerLite step, that step stops, the report names the step and why, and it is left for Jodie. Any older line in this repository or the project that opens dashboard.mailerlite.com, says Chrome is signed in to MailerLite, or treats MailerLite as a browser job is superseded by this rule.

## Sales-page typography and deployment QA (Jodie, 3 October 2026)
Do not enlarge page headlines when editing copy. Sales pages use the shared scale in `src/styles/sales-typography.css`: H1 at most 52px on desktop and 36px on mobile; H2 at most 40px desktop and 30px mobile. Emphasis inherits its parent size. Avoid narrow 9ch measures, compressed line heights, clipping, and oversized stacked words. Preserve the Newsreader/Inter brand system.
For every page change, inspect rendered screenshots of all affected pages on desktop and mobile, including the complete page, images, spacing, heading hierarchy, buttons, navigation, and overflow. After deploying, repeat the visual audit against the actual public deployment and verify the new version is live. A successful build or deployment status alone is not visual QA. Fix visible issues before claiming completion. If live rendering is inaccessible, report the audit as blocked rather than claiming it passed.

## Brand look (Jodie, 4 October 2026, Decision 128; clarified 11:30 am Eastern)
Before any visual or page work, read `ops/cloud-kit/TDIE_DESIGN_RULES.md` (section "THE LOOK"). The Digital Income Edit™ brand is loud, pink, sparkly, confident and girly: a big pink glittery mashup of a self-made millionaire and a sparkly grown-up pop-star princess in a homestead mom package. It must read luxury, never cheap. Never describe or design the brand as minimalist, clean and modern, beige, neutral, quiet, editorial calm or "luxury editorial". Headlines are Newsreader SemiBold, upright, never italic; everything else is Inter, including prices, labels, body text and buttons. Never use Fraunces, Cormorant Garamond or Montserrat anywhere. Never use brown or dark chocolate as a fill or background, including cards, panels, footers and buttons. Break up text with stickers, callout boxes, badges and pull quotes. Every clickable card shows its name and a button.
Headline sizes still follow the sales-page typography rule above and the headline lock. These explicit founder rules supersede conflicting older brand instructions.

## Actual production host
The public www.thedigitalincomeedit.com site is hosted on Cloudflare (worker `tdie-site`) and deploys from `cloudflare-migration`. Vercel is retired: ChatGPT migrated the site to Cloudflare after the Vercel free tier ran out of space. Do not reinstate Vercel and do not treat a Vercel status as proof of publication. Target the current production branch for public-site changes; verify the new content and CSS on the custom domain after deployment. Do not assume README snapshots establish public-site publication.

## Site-wide mobile design
`src/styles/mobile.css` applies to every page template, including articles, resources, lifestyle, link pages, and the course. Keep H1 at 30–36px, H2 at 26–30px, readable body text, 48px primary actions, wrapping labels, and zero document overflow at 320px and 390px. Grids must use `minmax(0, 1fr)` when a form or other intrinsic content can widen the track. Inspect the complete rendered mobile pages and interactive states; audit gated course content with repository HTML fixtures locally, without altering production access controls. Repeat public-site visual QA after deployment.

## Founder decoration preference (8 October 2026)
No bows on any design, page, graphic or other work for Jodie unless she explicitly requests a bow. Do not infer bow permission from reference images. Remove existing decorative bows when editing the affected work.

## WYS website corrections (8 October 2026)
Typography corrections mean restyling the visible words, not deleting the heading, description, example names or photo captions. Public Instagram examples are mockups with captions and blog destinations, not a slide-download giveaway. Preserve named Pretty Wicked and Ghoul Fuel examples with three equal-sized photographs apiece and colored backing mats behind the entire white Polaroid, offset beyond its outside edges. Never place the colored mat inside the photograph opening or add nested outlines.

## WYS visual corrections (8 October 2026, latest founder instructions)
No stripes, decorative double lines, mismatched category tile designs, or dark-pink pill buttons on WYS pages. Product selections must include an actual visible photograph of the selection, not a text-only records list. Avoid generic filler headings and internal workflow language in customer-facing content. Preview photos and fonts must load in the actual embedded preview, not merely on the production host.

## Required Lifestyle product shelves and decorative header (Jodie, 8 October 2026)
Every Lifestyle article must show its complete product list in a horizontal, side-to-side scrolling shelf near the top, after visitors have seen the article photographs. The required order is introduction → photographs → shopping shelf → article text. Shopping buttons must also follow the photographs; never put a shopping list or shopping action ahead of the pieces. Never restore the tall vertical product list or a vertically scrolling product pane. Apply this through the shared article component to ALL existing and future Lifestyle articles. Support touch swiping, a visible horizontal scrollbar, keyboard access and previous/next buttons; keep the document itself free of horizontal overflow. Preserve every product, variant, note, disclosure and verified shopping destination.
The header must be a complete decorative branded masthead with the TDIE name and composition above navigation. A drip strip alone does not meet the header request. Keep complete photograph frames compact enough to fit the viewport. Polaroid captions use light handwritten Caveat, actually verified in rendered computed styles; the later founder rejection of the thick Fredoka font supersedes the older rounded-font instruction. Never put decorative stickers over photographs, never add nested frames, and avoid white frames on white panels or excessive empty white space. Instagram previews display the actual photograph slides, without added graphic lettering or background mats. These latest explicit instructions supersede conflicting older decoration and typography guidance.


## Evergreen brand banner scope and production rules (Jodie, 9 October 2026)
WYS is one product, not the entire TDIE brand. Never use WYS examples, Halloween photographs or other seasonal/product-specific scenes in the brand-wide masthead. It must represent The Digital Income Edit as a whole. Do not use image generators for Jodie's website designs, headers, banners, mockups or design options. Build real browser-rendered HTML/CSS with manually authored SVG if useful. No decorative flowers or butterflies, ivory, or assumed pink-and-purple background palette. Do not interpret a request for header designs as a font selection exercise. A complete banner and its navigation must be designed as a composition; a drip strip alone is insufficient.
