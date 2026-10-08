# TDIE aesthetic and implementation handoff

Updated 8 October 2026. Website-only publication authorized explicitly by Jodie on 8 October; WYS product release, checkout, delivery and generation remain held. Owner: Codex for repository implementation. Audience: Jodie and the next developer working on The Digital Income Edit™.

The supplied website screenshots are the primary visual target, interpreted through TDIE’s current brand rules. The desired result is a detailed, pretty, expressive boutique website with a shoppable blog and a grown-up scrapbook feel. Photography, colorful mats, layered frames, dimensional actions and varied compositions should carry the experience. A page made from plain images and repeated text boxes does not meet the brief.

WYS is the first priority inside this facelift. Complete its landing page, Look Inside and updates signup as one section, verify the whole section, then return to Lifestyle and the other page families. This is an extension of the established TDIE direction, not a separate WYS brand.

## The creative direction

TDIE combines a confident self-made business with Tommy Kate’s lived-in pink farmhouse world. The site should feel like stepping into a pretty boutique that has useful things to show you: a framed photograph, a labeled collection, a guided process, a finished look, an invitation to explore. Pink has a visible role in the composition. Lavender provides another surface and a contrasting mat. Cream gives the photographs and body copy room to read.

The references are useful for their art direction and density: photo-led heroes, generous image-led category tiles, framed product shelves, scrapbook overlaps, contrasting section bands, and small details that look deliberately placed. Borrow those principles and build original TDIE components. Do not copy a reference brand’s assets, logo, typography, exact layout or sales claims.

The final Japanese shop reference is a special case: borrow **only its shopping sequence and lookbook/closet interaction**. Do not borrow its ornate antique frames, wallpaper, cream/brown palette, imagery or typography.

## Reference translation

| Supplied reference | What to carry into TDIE | TDIE interpretation |
| --- | --- | --- |
| Pastel loungewear boutique | Photo and copy share the hero; products become part of the section composition; stripes frame a process | Existing pink farmhouse photography beside upright Newsreader copy; colored mat; a small labeled process strip |
| Retro pink Wix shop | Image-led category navigation, framed shelves, scalloped edges, confident shopping labels | Lifestyle category thumbnails from matching articles; pink/lavender frames; native swipe shelves; glossy pill actions |
| Pink icing and sprinkles | Dimensional decorative trim with a clear silhouette | Occasional curved or scalloped section trim. No screenshot assets or checkerboard transparency baked into the site |
| Pink gelato boutique | Hero focal point, product rows, contrasting collection sections and asymmetric mission block | Framed hero photography, a curated article shelf, photo-and-copy splits and a distinct invitation section |
| Miss Eyelashes studio | Strong hierarchy and small menu details arranged with personality | Inter labels, file tabs, numbered badges, compact useful callouts and clear actions |
| MiniMaisy collection | Layered snapshots, playful collection structure, pink/lavender alternation and decorative edges | Real TDIE images in polaroid, double-rim and scalloped mats; alternate collection bands; restrained pearl badge |
| Purple candy shop | Clear shelf rhythm and section-to-section variety | Lavender frame variants and an occasional ribbon, without switching TDIE’s main pink identity |
| Japanese shop and closet layout | News/features → new arrivals → selected picks → swipe lookbook → individual article | Lifestyle hero → image-led categories → New in the edit → A few favorites → The pink closet → all articles |

## Brand locks

Use these colors consistently: Signature Hot Pink `#D62E73`, Bubblegum `#FF8AC2`, readable small pink text and white-button fill `#B8245F`, Lavender `#F1EAFB`, Cream `#FBF8F5`, near-black text `#1A1417`. Supporting mat colors include `#FFD4E6` and `#DFD0F4`; matching rims include `#E891B6` and `#C4AFE4`. Gold `#C8A96A` can appear as a thin line, never as a large fill or ornate floral treatment.

Headlines are upright Newsreader SemiBold. Body copy, labels, navigation, numbers, prices and buttons use Inter. Preserve the headline lock: desktop H1 at most 52px, H2 at most 40px; mobile H1 30–36px and H2 26–30px. Headline emphasis inherits its parent’s size. No narrow 9ch stacks, italic headings, oversized price type or compressed lines.

Do not introduce Fraunces, Cormorant Garamond or Montserrat. Do not use brown or dark chocolate fills. Do not describe or design TDIE as minimalist, neutral, beige or quiet. Avoid a full pink wash over photographs, fake tiled glitter, flat clip-art star wallpaper, gold roses, and identical hard offset shadows on every card.

## The frame system

Every photo and substantial content block needs an intentional treatment. A treatment means a coordinated perimeter and a clear relationship to its neighbors, not a decorative border pasted indiscriminately on every element.

| Treatment | Construction | Best use |
| --- | --- | --- |
| Pink photographic mat | Pink gradient mat, 10–14px padding, white inner rim, thin rose outer edge, soft pink shadow | Primary article photographs and standard collection images |
| Lavender mat | Lavender perimeter and matching purple rim, with asymmetric corner radii | Secondary photographs and alternating shelf items |
| Double frame | Thin double rose border, square corners, wider blush/lavender mat and white inset | Look Inside hero and selected proof images |
| Scalloped portrait frame | Pink perimeter with scalloped outside edge, a white inner rim and dimensional shadow | WYS landing and waitlist hero photography |
| Arched frame | Lavender arch around a portrait; measured round top, straight lower edge | One supporting image in a split story section |
| Polaroid | White outer paper, pink inset, generous caption margin, a slight tilt and pink shadow | Supporting snapshots and one FAQ or invitation photograph |
| File-tab block | Paper surface, colored border, a small top tab and spacious body | Kit contents and signup forms |
| Note sheet | White reading surface, pink border, stronger top edge, restrained asymmetric corners | Longer explanations and selected product notes |
| Ticket | Dashed lavender rim, square paper surface and small side notches | A short process note or supporting invitation |
| Numbered process block | Circular pink number, white/pale lavender surface, coordinated border and clear heading | Preparation steps and course actions |
| Double-rim invitation | Wide colored border, soft dimensional background, photo-and-copy split | The closing invitation on each major landing page |

Vary treatments by editorial purpose, not randomly. A hero gets the strongest frame. A three-image sequence has a coordinated family with one variation per role. Long reading sections use readable white paper. Small controls, tracking pixels, schema and technical elements do not get decorative mats. The same photograph may appear as a thumbnail linking to its article; do not disguise it as a new output.

## WYS section

The shared section uses `WysFrame`, `WysPhoto`, `src/data/wys.js` and `src/styles/wys.css`.

The landing page pairs a clear introductory message with the approved porch-door Lifestyle photograph in a scalloped pink mat. Its flow is: photo-led hero → compact principles strip → Ghoul Fuel’s three real views → numbered preparation process → Pretty Wicked photo-and-copy split → file-tab kit contents → FAQ with a small polaroid → framed closing invitation.

Look Inside uses the approved photographs as the actual visual content. Each example has a Basic/Styled/Lifestyle switcher, a visible five-product-type list, the viewpoint explanation, and a link to the full styling article. The pictures are generated styling inspiration, not exact retailer photographs or an assertion that every customer workflow passed. Without JavaScript, all photographs remain available; with JavaScript, buttons switch views. Buttons expose their pressed state and preserve keyboard focus.

The waitlist route is an **updates page using the existing Weekly Edit newsletter**, as Jodie selected. Its copy explicitly says the subscription does not reserve a WYS spot, place an order or promise a launch date. It uses the unchanged existing MailerLite form action. The page includes relevant approved photography, a small supporting polaroid, and two illustrated article links. No new MailerLite group, automation, campaign or welcome email is created.

Routes:

- `/shop/while-you-sleep-storefront`
- `/shop/while-you-sleep-storefront/look-inside`
- `/shop/while-you-sleep-storefront/waitlist`

The customer release hold is separate from website styling. Do not activate checkout, dates/countdowns, customer delivery, discounts, scheduled promotions or affiliate links while it remains in force. The master authority is `claude/WYS_REFERENCE_PACK_2026-10-07.md`; generation remains paused. Existing user permission for website work does not demonstrate that buyer-path release tests passed.

## Lifestyle shopping flow

The hub should help someone find a look before requiring them to read a long article grid. Begin with a framed seasonal story and a clear discovery action. Follow it with the ten image-led category cards. The New in the edit shelf introduces the latest records. A few favorites is an editorial selection, not a claim about sales or popularity. The pink closet is a swipeable outfit lookbook. The complete dated article grid remains available below it.

Use native horizontal scroll with scroll snapping, keyboard access and labeled previous/next buttons. No auto-rotation or forced swipe. Respect reduced motion. The whole card is a link, but it still shows the look’s name and a visible action. Opening a look leads to its actual article; do not create a fake cart or checkout for an affiliate blog.

Category thumbnails should come from a selected article in the same category. Prefer a Lifestyle view, then a Styled view, then the article’s existing hero. Keep the choice explicit and stable. For categories with no article, a relevant stock or authorized library image can preview the subject; label it Collection preview rather than inventing an article count or recommendation. Stock pictures are never Tommy Kate or proof of a product match.

All Halloween articles keep the supplied ghost background. The screenshot bytes remain unchanged; CSS clips the app controls and bottom instruction from the decorative wallpaper tiles. Keep the article header’s ribbon and selected image, the complete photographs, clearly framed shopping details, styling sections, related stories and one signup. Preserve complete 2:3 approved photos and their original files. Use Astro’s responsive image pipeline for display variants.

Pending affiliate links and Amazon Idea Lists stay pending. Do not replace them with a storefront homepage, an unverified canonical product URL or an unrelated short link. Preserve disclosures and AI styling notices.

## Other page families

| Page family | Intended composition | Preserve |
| --- | --- | --- |
| Homepage | Strong split photo hero, framed site artifacts, dimensional method steps, varied pink/lavender sections, illustrated invitation | Built Backwards sequence, current offer facts, testimonials, forms, navigation and SEO |
| Shop and sales pages | Photo or product artifact hero, file-tab contents, readable offer terms, framed proof and useful FAQ | Actual prices and checkout destinations, release holds, source-backed claims and checkout behavior |
| Membership and community | Framed room photography, clear tier comparison, numbered benefits, strong but readable actions | Verified tier facts, trial terms, Skool links and capacity rules |
| Learn hub | Illustrated reading introduction and framed guide shelves with visible titles/actions | Pillar names, guide order, article routes and free-resource destinations |
| Learn articles | Framed hero and body images, reading paper, varied note/quote blocks and related-guide actions | Body content, schema, citations, affiliate rel/disclosures, freebie integration and TOC |
| Resource hub and detail pages | Photo-led introduction where available, clear topic navigation, illustrated or numbered resources, framed signup | Tool behavior, file links, form actions and honest delivery copy |
| About and Work With Me | Portrait or workspace-led introduction, narrative/photo alternation, framed proof and invitation | Founder identity versus AI-persona labeling, truthful claims and contact destinations |
| Course and supporting pages | Branded navigation, framed task notes, useful numbered actions and readable prompt blocks | Access control, progress storage, copy interactions, exercises and noindex |
| Link, FAQ and privacy pages | Smaller branded header, coordinated surfaces, clear labels and visible navigation | Redirect behavior, disclosures, legal text, external URLs and noindex rules |

Do not convert every paragraph into a card. Do not add unrelated photographs to technical/legal content. An appropriate frame around a reading section can carry the design without manufacturing a product example.

## Asset rules and sources

Use relevant authorized existing photographs first. The six approved Halloween PNGs are the shared worked examples: Pretty Wicked basic, styled and approved porch-door lifestyle; Ghoul Fuel basic, styled and lifestyle. Original dimensions are 1024 × 1536. Their source bytes stay unchanged.

Do not use screenshot imagery from the reference brands, rejected WYS test generations, private avatar reference sheets, retailer catalog photos or paid member material as public decoration. No new paid generation or dependencies are needed for this facelift.

Stock category previews are a last resort for categories with no authored article. Record original source URL, license source, downloaded file digest, selected usage and truthful alternative text. The site’s generated photographs are not a substitute for current product sourcing verification.

## Implementation and maintenance

Keep one owner for repository changes: Codex. Claude can help with product wording and operate the specifically authorized MailerLite connector, but should not run a competing website writer. One source of truth per look, one shared component per repeated treatment, and one checked deployment path make this maintainable.

Prefer named reusable components and explicit page-family selectors. Keep design tokens together. Avoid global selectors that frame every `img`, override every number or change all anchors into buttons. Tracking pixels remain invisible. Use wrappers for mats and preserve source image dimensions, captions and alt text.

When a shared style changes, inventory every template using it. Inspect full rendered pages rather than inferring visual success from CSS or build status. If a shared override conflicts with local styles, resolve the component or stylesheet ownership explicitly. Preserve self-hosted fonts and the headline locks.

## Verification and release

Check production builds, route coverage, image references, schemas, affiliate states and navigation first. Then inspect complete rendered pages on desktop, 390px and 320px phones: actual images, framing, section rhythm, readable body type, heading size, contrast, forms, button labels, wrapping and horizontal overflow.

For WYS, test each photograph switcher, keyboard focus, FAQ expansion, the three cross-page navigation links, invalid email validation and the unchanged form destination. Do not submit a real signup merely to test styling. Verify the product checkout is absent and no countdown activates it.

For Lifestyle, verify the native shelves, both arrow directions, category thumbnails, article routes, one signup, complete approved photographs, the Halloween header and wallpaper, pending shopping state and disclosures.

For course content, use repository fixtures locally and keep production authentication intact. Preserve true redirects rather than redesigning an invisible redirect response.

Publish authorized website changes through Cloudflare worker `tdie-site` from `cloudflare-migration`. Vercel is retired. A successful build or deploy check is not proof of publication. Verify the new CSS and actual page version on the custom domain, then repeat the complete desktop/mobile visual audit for the affected pages. Keep a Git rollback point and source-backed QA report.

Repository-wide canon audit failures must be separated into baseline issues and introduced issues. Preserve the exact audit evidence; do not silence detectors to get a green result. The earlier broader local snapshot recorded 168 failures and 803 review items. A fresh same-scope comparison against the published pre-facelift commit da38d4d records 155 failures and 513 review items before, and 155 failures and 501 review items after the complete website facelift, with no added findings. The older counts covered more local files and are not directly comparable. Existing findings include affiliate rel/disclosure issues outside Lifestyle, retired vocabulary, BAMI-only terminology leakage and dated business facts. Compare the current output with the same clean baseline before attributing any new finding to the facelift. A visual rebuild does not authorize guessed prices or affiliate verification.

## Copy ready Codex prompt

```codex-prompt
Continue the TDIE reference-led website facelift in the existing repository. Treat Jodie’s supplied website screenshots and this handoff as the primary visual target, interpreted through the current TDIE brand rules. This is implementation work: finish and verify the actual pages, not just a plan or mood board.

Read AGENTS.md and the THE LOOK section of ops/cloud-kit/TDIE_DESIGN_RULES.md. Read claude/WYS_REFERENCE_PACK_2026-10-07.md in full before WYS work. Inspect the actual worktree, current branch, live Cloudflare production state, existing changes and assets before editing. Preserve other work and resume checkpoints.

Prioritize the complete WYS section: landing page, Look Inside and updates signup. Carry forward the existing facelift’s pink/lavender tokens, upright Newsreader SemiBold headlines, Inter body/labels/prices, dimensional actions and authorized photography. Study the supplied references’ composition, mats, layered frames, decorative detail, hierarchy and section variety. Every photo and major block needs a cute intentional treatment. Vary scalloped portraits, double frames, colored mats, file tabs, note sheets, tickets and polaroids by purpose; do not repeat one rounded card everywhere. Do not strip images for speed.

Use the approved Pretty Wicked and Ghoul Fuel photographs, including the porch-door replacement. Do not repaint, regenerate or overwrite them. Preserve the original PNGs and use Astro responsive optimization. Clearly label AI styling inspiration and separate styling extras from selected product types. Look Inside shows the actual approved three-image examples; do not fabricate a customer dashboard, delivered kit, retailer photo or automation proof. The WYS updates route uses the existing Weekly Edit signup, clearly labeled as a newsletter subscription that reserves no WYS place or launch date. Keep its existing form destination and privacy behavior.

Keep the WYS customer release hold active: no checkout activation, customer delivery, discount/countdown launch, image generation or scheduled promotion. Publication of held WYS pages needs explicit applicable authorization, distinct from releasing the customer product. Finish the concrete private preview and local verification before requesting any genuinely required approval.

After WYS is complete and verified, finish Lifestyle’s photo-led categories, colored mats and shopping sequence. Borrow ONLY the Japanese reference’s flow: new arrivals, editorial picks, swipeable looks, closet/lookbook and individual shoppable articles. Do not borrow its antique aesthetic, colors, imagery or typography. Prefer a selected existing article thumbnail from the same category. Use relevant authorized stock/library previews only where no matching article exists and label empty collections honestly. Keep native scroll, accessible arrows, visible card names/actions, no auto-rotation and reduced-motion support.

Apply the shared TDIE visual system thoughtfully across home, shop, membership, community, about, resources, Learn, articles, newsletter, work pages, legal/link pages and course templates. Preserve verified copy, prices, checkout links, disclosures, affiliate rel, pending affiliate links/Amazon lists, metadata, analytics, signup actions, tool behavior and access controls. No invented products, examples, performance claims or subscriptions. No new paid assets or unnecessary dependencies.

Build and run the checks appropriate to the changes. Inspect complete real screenshots on desktop, 390px and 320px, including interactions. Test course fixtures locally without bypassing production gates. Compare canon audit results against an unchanged baseline and explain pre-existing versus introduced failures. Fix visual and functional regressions before claiming completion. For authorized publishing, use cloudflare-migration and verify actual custom-domain HTML/CSS plus full live desktop/mobile rendering; never use Vercel status as proof. Deliver a clickable preview or live link, an updated handoff, relevant QA evidence and a precise statement of any remaining held action.
```

## Completed implementation and verification checkpoint

The WYS priority section is complete and already public. The remaining website implementation is complete: Lifestyle image-led category cards, two native swipe shelves, approved Halloween photographs with responsive optimization, framed article headers, and shared photo mats, dimensional containers and typography across the public page families. Learn uses existing relevant TDIE bookshelf photography. All 22 prior Lifestyle records remain unchanged. Pending affiliate links and Amazon lists remain pending.

Local verification: production build generates 169 routes; 36 Lifestyle routes pass the build audit and model tests; all 167 rendered routes were captured at desktop and 390px (334 captures), with no missing visible images, heading-limit violations or horizontal document overflow. Two metadata redirect pages retain redirect behavior. Additional 320px checks and shopping/tool interactions pass in 30 captures. All 27 protected course-content fixtures were checked locally at 1440px, 390px and 320px (81 captures); progress, copy and expandable notes pass without touching production authentication. WYS switchers, FAQ, mobile navigation and invalid-email validation pass. A final targeted verification covers the small resource-action grid correction. Public post-deployment verification is the next required checkpoint.
