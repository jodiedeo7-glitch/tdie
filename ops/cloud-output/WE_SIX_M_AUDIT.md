# The Weekend Ecosystem™: Six M pre-ship audit (27 Sep 2026)

Written before any edit. Pages audited as built from commit `5b373b7`: `/shop/weekend-ecosystem` (sales) and `/weekend-ecosystem/preview` (preview). Checked against `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/canon/canon.json` and `ops/canon/TDIE_CANON.md`.

## Sales page `/shop/weekend-ecosystem`

### 1. Magnet
- Opens on a mechanism line ("Own a website, a blog, and an email list by Sunday afternoon"), not a self-reference ("If you're X"), a true exclusivity or a reciprocity device.
- The free preview (the reciprocity gift canon names first) is buried as a ghost button and a small grey paragraph under a crowded hero.

### 2. Message
- Ideal state is missing from the first screen. The hero stacks 17 items (eyebrow, H1, twist, disarm, brand line, lede, four-box outcome grid, sub, frame, price, Kit banner, two buttons, testimonial strip, timing, peek note, access note, image) and ends with a strip of phase/module chips: a feature dump before she knows what her week looks like after.
- Resume copy sits above the ideal state: the 22 / 36 / 3 / 1 stat strip is the second thing on the page.
- "Friday vs Sunday" (the clearest ideal state on the page) is near the bottom, below the module list.
- Fails the delete test in the hero: delete the product name and what's left is a list of assets, not a change in her life (time back, control, no face, a business that sells when she isn't working).
- Hours contradict each other: hero says fifteen ("two Friday, eight Saturday, five Sunday"), mid-page CTA and structured data say sixteen, the timeline image adds to 16 (2+3+3+3+3+2). Saturday is nine hours, not eight.
- Says the preview has "two full modules ... the update log". It has neither (it shows the module index, one module excerpt, the Quick Sheet excerpt, the real repurposing output, the tracker and the certificate). Inaccurate claim about our own free page.
- "A developer quotes four figures for this build": unverified comparative claim, not in canon.
- Tina Alexander's review appears three times (line in hero, full card in the proof section, pull quote in the terms box). The full card sits in a generic proof block, not at the point of doubt.
- 40+ em dashes in visible copy, including the button label and access note (house rule 9).

### 3. Micro-commitment
- The smallest yes for a cold reader (the preview, free, no email) is visually weaker than every other element in the hero and is not repeated as the calm alternative at the close.

### 4. Make the ask
- CTA language is inconsistent: "Get the course [em dash] $97" (hero, mids, close), "Get it" (sticky bar). Four mid-page CTAs plus sticky: frequency is fine, wording is not one ask.
- No "your/my" in the button. Button carries an em dash.
- Payment plan is not beside the price where she decides: hero shows "$97 once [em dash] or three payments of $33.33" as a sentence; close shows "$97" big and the plan as small caps text. Neither shows both options as two equal, readable choices.

### 5. Money
- Routes to TDIE's owned checkout (Beacons link `f7b54195…` from `we-stage.js`, which matches `own_affiliate_programs.weekend_ecosystem.link`, verified in canon as resolving to the Weekend Ecosystem™ product). Pass.

### 6. Map
- Not a launch-window asset; the Keep It Running Kit window (canon Decision 105, ends 4 Oct 2026 11:59 pm Eastern) is real and self-expires in `KitBanner.astro`. Pass, keep it.

### Objections (six emails, canon `emails.weekend_ecosystem_objection_series`)
| Objection | On the page now? |
|---|---|
| 1. I can't build a website | Partly (FAQ "Do I need to know how to code?", hero disarm line). No dedicated answer at the moment of doubt. |
| 2. I don't have a free weekend | Only in structured data (invisible). Hero line mentions "three weeks of evenings". |
| 3. $97 is a lot right now | Missing. Payment plan is never framed as the answer. |
| 4. No refunds / what if it isn't what I think | Present ("There are no refunds. That's deliberate.") but separated from the preview it points to. |
| 5. Not enough content / I'm not a coach | Only in structured data (invisible), and there it uses an unverified "forty to eighty pieces" figure. |
| 6. I'll do it later | Missing. |

### Pre-ship check (11 points)
1 Magnet: FAIL · 2 Exclusivity true: PASS (none claimed) · 3 Ideal state first: FAIL · 4 One CTA: FAIL (two labels) · 5 Strong verb, your/my, trade: FAIL (no your/my) · 6 Link on CTA words, twice: PASS · 7 Routes to owned: PASS · 8 Canon rows: FAIL (preview description, hours) · 9 Meta: n/a · 10 Launch window: n/a · 11 Real-person voice: PASS mostly, em dashes fail house rule.

### Design (TDIE_DESIGN_RULES.md)
- Near-flat: almost every block is a white card with a hairline on cream. No frosted cards, no tilted sticker badge, no glossy hot-pink hero card, headline has no hot-pink turn phrase (rules 2 "Cards", "Stickers", "Type").
- Headline weight 300 (rules call for Newsreader SemiBold with the turn phrase in hot pink).
- Mobile: hero is ~3 phone screens tall before the first image; 10px and 10.5px mono labels are below comfortable reading size; sticky bar button is 11px.

## Preview page `/weekend-ecosystem/preview`

### 1. Magnet
- Kicker "A look inside · No email required" is the reciprocity device: pass. H1 "What you're actually buying" frames it as a sales page, which undercuts the no-pressure promise for a cold reader.

### 2. Message
- No ideal state on the first screen; opens straight on the interface.
- Renders the literal escape text `\u2014` twice (hero lede and close note): visible bug on the live page.
- Close says "four reference vaults"; the sales page and the-numbers image say 3. The included list is three vaults plus the Ask-For-It List. Contradiction.
- Tina's full card sits in the hero before she has seen anything to doubt; the doubt peaks at the module/prompt screen ("can I actually do this?").
- Em dashes throughout visible copy.

### 3. Micro-commitment
- The page itself is the micro-yes, but it pushes the buy link six times ("Get it [em dash] $97" after every section), which turns the bridge back into a sales page for a reader who came here because she wasn't ready.
- No statement of what she is looking at (there is no "here's what's on this page") so she can't skim to the part she doubts.

### 4. Make the ask
- Three different labels: "Get The Weekend Ecosystem™", "Get it [em dash] $97", "Get it". Price shown as "$97" in the inline links without the payment plan beside it.

### 5. Money
- Every buy link goes to the owned sales page. Pass.

### 6. Map
- n/a.

### Objections
- None addressed on the page. No-refunds reason for the preview's existence is not said here at all.

### Pre-ship check
1 PASS · 2 PASS · 3 FAIL · 4 FAIL (three labels, six asks) · 5 FAIL (no your/my) · 6 PASS · 7 PASS · 8 FAIL (four vaults) · 9 n/a · 10 n/a · 11 FAIL (literal escape text, em dashes).

## Source conflicts flagged (once, with the fix)
1. **Refund line.** `TDIE_CANON.md` §3 says "No refunds on any digital product. Stated once on `/faq`, never repeated per-product." The live sales page, the members' door page and the canon objection series (Email 4, Decision 105) all state it per product, and this job requires it stated plainly. Fix: add to §3 "Exception: The Weekend Ecosystem™ sales and preview pages and its objection series state it plainly (Decision 105, 27 Sep 2026 job)." Proceeded with the plain statement.
2. **Doc of record missing.** `claude/TDIE_ECOSYSTEM_OBJECTION_SERIES.md` (the six email bodies) is not in this repo. The objections section is built from the canon rows (subject lines, objections, rules) and facts already on the sales page, not from the email bodies.

## What changed (27 Sep 2026)
Both pages rebuilt on the One-Sentence Offer tool's visual system (frosted cards, glossy hot pink card, tilted stickers, pill CTA, Newsreader SemiBold with the turn phrase in hot pink).

- **Magnet + Message:** both heroes open on the ideal state from the framework ("A business that keeps selling on the Tuesday you're too tired to post."). Sales page second section is Friday vs Sunday plus time, control and no-face cards. Module list, stats and inclusions moved below.
- **Ask:** one CTA label everywhere, "Get my Weekend Ecosystem™", straight to the canon checkout link. Sales page: hero, after inclusions, after objections, close, mobile bar. Preview: after the prompts, close, mobile bar.
- **Price:** new `WePrice` block shows "$97 one-time" and "3 × $33.33, three payments, $99.99 total" side by side, directly above every button.
- **Micro-commitment:** "Not sure yet? Look inside first. Free, no email, no card." under every sales-page button; preview opens with a six-part map of what's on the page and asks for nothing until she's seen the prompts.
- **Social proof:** Tina Alexander's full review (Testimonial component, verbatim, "word press" unfixed) sits directly under Objection 1 "I can't build a website" on the sales page and directly under the real module screen on the preview, the two points where "can I actually do this?" peaks. One-line cut under the final button on each page. Removed from the hero and the generic proof block.
- **Objections:** six, in email-series order, from one source file `src/we-objections.js`: full cards on the sales page, short answers on the preview. No guarantee, no refund window, no income claim. Objection 4 says "there are no refunds. Not a short window, not a partial one. None." The Kit deadline line in Objection 6 renders only until 4 Oct 2026 11:59 pm Eastern (same deadline constant as `KitBanner`, now in `src/we-kit.js`).
- **Fixed:** literal `\u2014` on the preview; "four reference vaults" (now three, plus the Ask-For-It List); fifteen vs sixteen hours (now sixteen: two Friday, nine Saturday, five Sunday); preview described as "two full modules ... the update log" (now described as what it shows); unverified "developer quotes four figures" and "forty to eighty pieces" claims removed; wrong alt text on the porch and attic photos; every em dash on both pages, including the button, access note and Tina's source line.
- **Design:** body text 15.5 to 19px, no label under 12px, every tap target at least 44px tall, no horizontal overflow at 320, 360, 390 and 1440px.
