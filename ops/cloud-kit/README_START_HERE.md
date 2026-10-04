> **MIDJOURNEY, STANDING RULE (Jodie, 3 October 2026).** Jodie has an active Midjourney subscription, signed in in her browser, with far more free generations than Higgsfield. Whenever an image would come out better in Midjourney, use Midjourney, with or without a person. This amends every tool-order line in this file that says no other image generator is used. Canva is still never an image generator. Full rule: section M of claude/TDIE_IMAGE_GENERATION_MASTER.md.

> Migration routing, 1 October 2026: read `ops/TDIE_AI_ROUTER.md` and `ops/ai-router/EXECUTION_CONTRACT.md` first. This source contains historical job specifications, not active schedules. No blanket commit-to-main, push, listing, campaign, pricing or publication instruction here overrides the current task's authorization. Prepare reviewable work and route account operations separately. Do not restore Find Your Door automation. Read SOURCE_RECONCILIATION_2026-10-01.md and the source register for recovered SOP snapshots and remaining live-verification gates.


# START HERE: TDIE rules for cloud sessions

Written 26 September 2026 for Jodie's cloud-credit sessions. Cloud sessions cannot open the claude.ai Project, so everything a session needs lives in this repo:

- `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md`: every product, price, link and settled decision. If it is not a row in canon.json `products[]` or `key_pages`, it does not exist.
- `ops/cloud-kit/`: this file plus the project docs each job needs.
- The site itself: `src/` (Astro on Vercel). Live at https://www.thedigitalincomeedit.com.

If a job names a file that is not in this repo, say so in your report. Do not work from memory.

## Who you work for
Jodie DeOliveira, founder of The Digital Income Edit™ (TDIE), a loud, pink, sparkly, luxury education brand (never minimalist, clean-modern, beige or cookie-cutter; see TDIE_DESIGN_RULES.md) teaching women to build faceless digital income with AI. The business is live. Work within what's built; never redesign it.

## House rules (every job)
1. Before starting, read every file your job names. Start your first reply with "Sources checked: [file names]." Finish with "This matches [files]" or name the line that doesn't.
2. Never invent a product, price, link, testimonial or CTA. Full trademark names and exact prices on first reference.
3. If two sources disagree, stop and flag it once, with the fix. Never re-raise a settled decision in TDIE_CANON.md.
4. Ship, don't plan. Do the whole job end to end. No option menus, no stopping mid-job to summarize, no "want me to continue?".
5. Never say done until you have re-read the actual result (live page, pushed file, rendered PDF).
6. Label anything unverified as unverified.
7. Never say something can't be done until every route has been tried.
8. Plain English. No jargon.
9. NO EM DASHES anywhere, in chat or in anything you produce. Also never: "game-changer", "utilize", "delve", "journey", "elevate", "unlock your potential", "let's dive in", "it's important to note", "in conclusion", "It's not just X, it's Y."
10. Never mention GitHub tokens.
11. Reporting: if everything passed and nothing needs Jodie, one line plus the one thing she needs (a link or file). If you truly need her, ask exactly one plain question.
12. Send every finished file to Jodie with the send-file tool. She is often on her phone.

## Anything that needs Jodie's accounts
This session is not linked to her computer, so it cannot use her signed-in Skool, Beacons, Amazon, Pinterest, Instagram, Gemini or Higgsfield. (MailerLite is never a browser job in any session: it is reached only through the MailerLite plugin, Jodie's rule of 2 Oct 2026.) **Do not stop because of that.** Finish everything else, then add the account-only steps to `the relevant workflow queue under ops/queues/ (see ops/TDIE_AI_ROUTER.md)` (create it if missing): one numbered section per job, with every file path, every piece of copy and every exact step already written in, so a later session on her computer can do them without asking anything.

## Standing facts
- Site: www.thedigitalincomeedit.com. Flat URLs `/learn/[slug]`, no trailing slash. Repo: jodiedeo7-glitch/tdie.
- "The New Faceless": Jodie's real face is never required. The brand's face is the AI persona Tommy Kate.
- NurseMadeDigital is retired as a brand. (One exception: her Threads handle is @nursemadedigital.)
- Pinterest blocks her entire domain. Pinterest pins may only link to skool.com addresses (or Amazon Idea Lists for Amazon pins).
- Membership tiers: Standard $9/month · $99/year (7-day free trial) and Premium quoted at $35/month · $297/year. No free tier, no "VIP", no "Free Community".
- Tagline: "Build Your Business Backwards. Scale It Forward.™"
- Build order, always said the same way: offer first, funnel second, automation third, audience last.
- Proof is "show the machine" (TDIE itself, built faceless and solo with AI), never income screenshots.
- No earnings or income figures on Facebook or Instagram. Allowed elsewhere if true.
- Links: every link sits on the CTA words, never a raw URL (www.thedigitalincomeedit.com is the only exception), and appears twice (early and at the close). Instagram: no links anywhere, CTA points to the link in bio. Facebook: no link in the post body, link in the first comment only.
- BAMI and Vault Unlock are never written into a new asset.
- The Value Vault is à la carte for Standard members; Premium has every guide unlocked. Never write that the vault is included in Standard.
- Zero refunds on digital products. Never write a guarantee or a refund window.

## Voice
- **Site and email:** a founder with strong opinions. Curiosity, tension, specificity. Never "this week's article", "here's a guide", "learn how". Never sign off "Warmly"; emails sign off "xoxo, Jodie".
- **Skool:** Jodie's own voice, snarky-ish girls' girl. Warm, casual, emoji-forward, short punchy lines, lots of white space. If the `tdie-skool-post` skill is available, load it first. Samples: `TDIE_ONE_SENTENCE_OFFER.md`.
- **Tommy Kate voice** is only for the Premium DFY Content Calendar and Instagram. Never for Skool.

## Design (any graphic, cover or PDF)
Follow `TDIE_DESIGN_RULES.md`. Short version: Luxury Cream #FBF8F5 base, Signature Hot Pink #D62E73, Bubblegum #FF8AC2, gold #C8A96A as a thin line only, near-black #1A1417 text. Newsreader SemiBold headlines with the key words in hot pink, Inter for everything else. Depth, frosted cards, tilted sticker badges, callout boxes, big crisp headlines. Never Fraunces, Cormorant Garamond or Montserrat. Never brown fills. Never a flat plain background. Never a full pink wash. Jodie is not minimalist. The full look is in TDIE_DESIGN_RULES.md, section "THE LOOK" (Decision 128).

## Images
For Premium member calendar prompts, the current TDIE_DFY_CALENDAR_PRODUCTION_RULES.md governs tool-neutral member usability and optional persona references.
Follow `TDIE_IMAGE_GENERATION_MASTER.md` (or the `tdie-image-prompt` skill if available). Every prompt with Tommy Kate opens: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair colour, eyes, skin or age. Her world only (farmhouse, pink attic gaming loft, porch, kitchen, pasture, red barn, golden retriever). Pink rule: frames with her always include her glitter-flecked pink iced coffee tumbler with a lavender straw and it is never the only pink item; frames without her may use pink freely throughout the scene. Wardrobe: oversized pink knits, soft tees, hoodies, sweatpants, leggings; never blouses or blazers. Hex codes never go inside an image prompt. The seed image is in the repo at `public/images/library/avatar-seed-omni-reference.png`. Cloud sessions cannot run Gemini or Higgsfield: write every image prompt in full, and queue generation in the relevant workflow queue under ops/queues/.
