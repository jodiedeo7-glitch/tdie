# TDIE visual finish

16 October 2026. Production baseline: `a258a0fae7be930a59526a0c3bdf4c444f44c3e6` on `cloudflare-migration`.

## Design decisions

The supplied collage references inform paper layers, tape, angled product previews and small labels. The long-page references inform varied section compositions, product photography and clear transitions. They are references for composition, not permission to copy their branding, claims or content.

The implementation uses existing TDIE images and browser-rendered HTML/CSS. No images were generated. The approved car hero, notebook, stacked Method cards, Blueprint fan, glossy review bubbles and updated Skool gallery remain recognizable.

- Gloock headlines, Jost body/UI and Yellowtail on the existing single stressed word in selected homepage headlines.
- Light pink foundations, hot-pink typography and small silver glitter details. No black/brown fills, full glitter backgrounds, decorative bows, flowers, butterflies or pink/lavender ombre.
- Different compositions for route choices, foundation help, product previews, membership, free guides and shopping paths.
- Compact headings, visible product names, real product previews, white outlined buttons, readable phone layouts and direct access links.
- The shared public header and footer now use the homepage wordmark. The thin glitter header edge replaces the tall overlay in the shared chrome. Active-page links and keyboard focus remain visible.

## Journey expressed in the design

The homepage immediately presents foundation help, membership support and a qualified owned-website path. Find Your Door remains optional. The hero no longer implies that owning one product establishes course fit.

The Weekend Ecosystem™ is explicitly introduced for existing reusable material plus a website-building need. Friday/Sunday describes that course's website build. It is not a transition from the Blueprint or a promised traffic result. A paid product is not required.

Standard and Premium are support choices at any stage. Premium continues to say posts are supplied every month. Immediate training/guide use is distinguished from adapting promotional calendar details, producing visuals and publishing.

PLR, Shopify, Lifestyle shopping, personal services, BAMI information and existing-customer access have separate visible destinations. The three vaults retain their different roles.

The quiz asks about material and website intent before preferences. The course is excluded unless both answers are explicitly yes. Automatic later-purchase suggestions are removed. Premium and PLR explanations no longer require an offer or an existing shop. Article recommendations for the course carry the same fit explanation, including per-article paid-slot overrides.

Public API payloads and endpoints are unchanged. Email automations, checkout destinations, prices and customer entitlement checks were not changed.

## Current sources and unresolved authority

Read current `main` canon.json before this task, blob `152d63f597867fe1b88d97e5fb6b557efac28074`, and refreshed production source. The governing canon still names Newsreader/Inter; production AGENTS.md and design rules explicitly record Jodie's Gloock/Jost direction with scoped Yellowtail. This design follows the explicit founder direction. This change does not rewrite either governing file.

The WYS master release HOLD conflicts with existing live promotional and timed checkout states, as recorded in the journey mapping. This visual pass does not resolve that conflict, release the product, change its generation workflow or activate new WYS promotions or checkout behavior. Existing WYS-specific page implementation is unchanged; its shared header/footer receives the common chrome corrections.

MailerLite behavior remains unverified because the permitted connector is unavailable. No browser access or other email service was used as a substitute.

## Verification

- Astro static build passed: 183 pages.
- Browser rendering checks covered 98 static public routes at 1440px and 390px after the final spacing changes: no document overflow and no broken images within the visible viewport.
- Fifteen principal routes additionally checked at 320px: homepage, membership, shop, resource hub, quiz, Blueprint, Shopify Starter Kit, library, foundation article, course sales, PLR, About, Work With Me, BAMI and Lifestyle. No document overflow found.
- Screenshot review covered the complete homepage at desktop and mobile widths, shared public page families, the mobile menu and quiz result, and the PLR spacing correction. DOM checks across the remaining routes are not a claim of a full screenshot review of every generated page.
- Exercised the quiz through its visible controls: no material plus strong website/time/payment preferences did not recommend the course; reusable teaching material plus website intent recommended the course without selecting product ownership; a beginner without an offer received Premium with accurate remaining-work expectations.
- New internal route targets and image files checked against the generated site. Direct course access retains the existing authentication flow.

No purchases, subscriber submissions, email delivery, buyer accounts or customer release paths were tested. Public deployment requires a separate live check after the merge; local rendering and a successful build alone are not publication evidence.
