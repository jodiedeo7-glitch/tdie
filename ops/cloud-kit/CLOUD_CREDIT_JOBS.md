# CLOUD CREDIT JOBS: FINAL LIST

26 September 2026. $250 cloud credit, expires 2:59 am ET, 5 November 2026. Cloud sessions only (not Projects, not scheduled routines). The holiday gift guides are already running and are not on this list.

## How every job works
- Start a new cloud session from the Code section (phone, desktop app or claude.ai/code). Pick the repo **jodiedeo7-glitch/tdie**.
- Paste one prompt, everything between START and END. Nothing to fill in, nothing to attach: every file it needs is in the repo at `ops/cloud-kit/` and `ops/canon/`.
- Anything that needs your accounts (Skool, Beacons, Amazon, Gemini, Higgsfield) gets written into `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`. Run the DESKTOP FINISH prompt at the bottom once, on your computer, after your weekly usage resets. That one uses your normal plan, not the credit.

| # | Job | Model | Credit (estimate, unverified) | Why it's worth it |
|---|---|---|---|---|
| 1 | STV demo site + DM | Fable | $40 | One yes is $3,500 plus 20% of his sign-ups for life |
| 2 | Pin Writer Bot + Product Builder Bot | Fable | $50 | Two new products with almost no delivery cost |
| 3 | TikTok packet bank (10 videos) | Fable | $45 | Launch runway for Maniacally Thorough, with Amazon book tie-ins |
| 4 | One-Sentence Offer tool on the site | Opus | $25 | Your best-performing format, turned into a free tool that sells The Offer Edit |
| 5 | 15 buyer-intent articles + packs | Opus | $55 | Google traffic to The Weekend Ecosystem™ while Pinterest is blocked |
| 6 | DFY proof samples | Opus | $35 | Buyers can see the finished work before paying $97 to $1,297 |

If the credit runs low, switch whatever is left to Opus.

---

## JOB 1 · STV DEMO SITE + DM (Fable)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session, then read `ops/cloud-kit/STV_FACTS.md`. Start your first reply with "Sources checked: [file names]."

THE JOB. Build a finished, private demo website for Short The Vix (STV), Jodie's trading mentor, so her outreach DM shows him his site already built.

1. Research first, with web search and fetch: his public YouTube channel (the Market Open Live streams), and any public Whop or Discord listing for LTMP. Keep a sources file with a link for every fact you use. Anything you can't confirm publicly is left out, or shown as grey placeholder text labelled "Jodie to confirm with STV". Follow every hard rule in STV_FACTS.md.
2. Build the site: static HTML, one file per page plus shared CSS, mobile-first, fast. Pages: Home (who he is, the "less trades, more profit" idea in his public words, a Market Open Live video embed, one clear join button to LTMP), About, Start Here (what a new trader should watch first, from his public videos), Market Open Live archive (a written recap page per public stream with the video embedded; build three real recaps from his most recent public streams), LTMP membership (only what public listings say), FAQ, and a blog index. Page titles and descriptions written so Google finds him for his name and "LTMP trading". His brand, not TDIE's: a clean dark or neutral trading look, no TDIE pinks.
3. Privacy: it's his name on a site he hasn't approved. Do NOT publish it anywhere, do not deploy it, and do NOT commit it to the TDIE repo.
4. Take full-page screenshots of every page at desktop and phone width with the headless browser, and build a PDF walkthrough from them.
5. Write the outreach DM in Jodie's warm, direct voice, short enough to read on a phone, covering everything in STV_FACTS.md "The outreach DM must say", then the two options exactly as written there, ending with one easy question he can answer in a word. No em dashes.
6. Send Jodie four files with the send-file tool: the site as a zip, the PDF walkthrough, the sources file, and the DM as a text file. Nothing goes in the desktop finish queue for this job.

Report in one line.

----- END -----

---

## JOB 2 · PIN WRITER BOT + PRODUCT BUILDER BOT (Fable)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json` (especially `pin_render` and `products[]`), `ops/cloud-kit/TDIE_ONE_SENTENCE_OFFER.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md` and `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`. Start your first reply with "Sources checked: [file names]."

THE JOB. Jodie committed to five sellable bots, in this order: Pin Writer Bot, Product Builder Bot, AI CEO Bot, Persona Bot, then a "Build & Sell Your Own Bot" guide. Build the first two as finished products a beginner sets up in under ten minutes.

Each bot is a Claude Project kit the buyer sets up in her own Claude account: (1) complete custom instructions; (2) the knowledge files the bot reads; (3) a designed setup PDF with numbered steps, written for someone who has never set up a bot; (4) a "first five things to ask it" card; (5) a one-page quick reference.

- **Pin Writer Bot:** turns one blog post, product or link into finished Pinterest pins: title (60 to 100 characters), description (450 to 500 characters), alt text (150 to 200 characters), a 3 to 5 word overlay line, a board suggestion and an image prompt. It follows the limits in canon.json `pin_render`, warns about phrasing Pinterest treats as spam (for example "Make Money Online"), and never promises traffic or income.
- **Product Builder Bot:** walks a beginner from "I don't know what to sell" to one finished first digital product. It picks the idea from what she already knows, writes her one-sentence offer with the formula in TDIE_ONE_SENTENCE_OFFER.md and runs the four checks on it, outlines the product, drafts it section by section, and writes the sales page and the listing. No income claims, no results timelines.
- Neither bot contains any prompt from The Weekend Ecosystem™, and neither copies The Operating Prompts™. New, purpose-built instructions only.

Test each bot in this session against three realistic beginner inputs. Fix the instructions until every output is something Jodie would ship. Put the best test run in the setup PDF as a worked example.

PDFs follow TDIE_DESIGN_RULES.md exactly. For each cover, write the full Tommy Kate image prompt per the image master, and put a clean placeholder where the photo goes.

Also write for each bot: a Beacons product description in the site voice, a Value Vault lesson body (à la carte buy link placeholder), a Premium Vault lesson body (file attached, no extra cost), and three Skool launch posts in Jodie's Skool voice.

Commit everything to `ops/cloud-output/bots/` and push. Send Jodie both kits zipped. Add to `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`: generate the two cover photos (exact prompts written in), drop them into the PDFs, then, after Jodie sets prices, add both products to canon.json and TDIE_CANON.md, list them on Beacons, add the two vault lessons in Skool and schedule the launch posts, reading every listing back live.

Then ask Jodie exactly one question: "What price do you want for Pin Writer Bot and for Product Builder Bot?" Nothing gets listed anywhere until she answers.

----- END -----

---

## JOB 3 · MANIACALLY THOROUGH: TEN-PACKET BANK (Fable)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/MANIACALLY_THOROUGH_PACKET_SKILL.md` (or load the maniacally-thorough-packet skill if it's available; they are the same) and follow it in full. From `ops/cloud-kit/README_START_HERE.md`, follow the house rules only; this channel is not TDIE. Start your first reply with "Sources checked: [file names]."

THE JOB. Build ten complete production packets for the TikTok channel @maniacally.thorough, all sixteen required sections from the skill, in order, sections 13 to 16 included.

About the channel: "True crime. Medical mysteries. Rabbit holes." Signature line "I read the whole thing. Unfortunately for you." Payoff "And I brought the receipts." Philosophy: facts first, rabbit holes second, verify before you vilify. It does not retell cases. It finds claims people repeat as fact, checks the record, separates what is known from what is alleged, and calls out reasoning that doesn't hold up. The guiding question is "what can we actually establish?" Analytical, never conspiratorial; "I don't know" and "I was wrong" are features. Voice: intelligent, blunt, conversational, skeptical, occasionally sarcastic, human. Jodie is a BSN-prepared RN and acute-care NP student; her clinical background is the edge.

Pick the ten with real research: what is being searched and argued about now, where the public narrative and the public record visibly disagree, where a primary record exists (court filings, trial video, released autopsy summaries, official reports), and where a nurse's eye adds something. About half recent cases, a few medical mysteries, one or two broader rabbit holes. For each, one line on why it will perform and one line on what the record can establish.

Verification is non-negotiable. Try every route to caption tracks and primary documents. Anything not verified word for word goes in the quarantine section marked "VERIFY ON HER PC BEFORE FILMING", never in the script. Both halves of every damning statistic. Never state guilt, innocence, motive or mental state. No photos of minors or private individuals. Where she lacks standing (forensic pathology, anaesthesia), she says so on camera.

Where a published book genuinely fits a case, name it in the posting package for her Amazon storefront (https://www.amazon.com/shop/thedigitalincomeedit) with "#ad As an Amazon Influencer I earn from qualifying purchases." Never force one.

Save each packet as `ops/cloud-output/maniacally-thorough/V0n-<case-slug>.md` plus an `INDEX.md` ranking the ten by how soon each should film. Push, and send Jodie the index and all ten packets. Each packet's Status section carries the download and clip-cutting steps for her PC exactly as the skill describes. Report in one line with the count.

----- END -----

---

## JOB 4 · THE ONE-SENTENCE OFFER TOOL (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json`, `ops/cloud-kit/TDIE_ONE_SENTENCE_OFFER.md`, `ops/cloud-kit/TDIE_SATURDAY_OFFER_AUDIT.md`, `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md`, and in the repo `src/pages/resources/find-your-door.astro` (the model for an on-screen tool), `src/components/Testimonial.astro` and `src/we-reviews.js`. Start your first reply with "Sources checked: [file names]."

THE JOB. Build a free interactive tool at www.thedigitalincomeedit.com/resources/one-sentence-offer, from the Saturday Offer Audit, the best-performing post in the community two weeks running.

How it works: she types what she sells the way she describes it now. Three short fields walk her through the formula (who she is, what she walks away with, what it costs her). The tool runs the four checks on her new sentence live on screen, and shows which of the five failure modes her original sentence hit, explained in plain words, with the anonymous before-and-after pairs from the bank as examples. Results show on screen only: no email automation, no AI calls, no running cost; simple rules in the page. A "copy my sentence" button, and a line telling her to put the same sentence in her shop bio, link in bio and the first line of her sales page.

The result screen routes to three doors, in this order, hyperlinked on the words: The Offer Edit ($37 one-time, or included in Membership Premium) at its canon.json URL; The Weekend Ecosystem™ ($97 one-time, or 3 × $33.33) at its sales page; Membership Standard ($9/month after a 7-day free trial, or $99/year) at https://www.skool.com/thedigitalincomeedit/plans. Tina Alexander's review through the existing Testimonial component, never hand-pasted.

Design per TDIE_DESIGN_RULES.md, perfect on a phone. Page title and description written for how people search ("how to describe my digital product in one sentence"). Link to it from the Find Your Door result screen and the resources index. Add it to `key_pages` in `ops/canon/canon.json`.

Run npm run build, commit, push to main. Wait for the deploy, then load the live page with the headless browser at phone and desktop width, test three sentences from the bank, and confirm every link resolves. Only then report.

Add to `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`: add a one-line link to the tool at the end of The Offer Edit's opening lesson in Skool (exact line written in), add the same key_pages row to the Project copy of canon.json, and a Skool post announcing it for the next Saturday Offer Audit (written in full, in Jodie's Skool voice).

Report in one line with the live link.

----- END -----

---

## JOB 5 · FIFTEEN BUYER-INTENT ARTICLES (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json`, `ops/canon/TDIE_CANON.md` (pillars, close-out rules), `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`, and in the repo two existing articles under `src/pages/learn/`, `src/pages/learn/index.astro`, `src/data/article-dates.js`, `src/layouts/ArticleLayout.astro`, `src/components/Testimonial.astro` and `src/we-reviews.js`. Start your first reply with "Sources checked: [file names]."

THE JOB. Google is TDIE's one open search channel while Pinterest blocks the domain. Write and publish 15 articles for readers who are ready to buy, each routing to The Weekend Ecosystem™ ($97 one-time, or 3 × $33.33) at https://www.thedigitalincomeedit.com/shop/weekend-ecosystem, with the preview (https://www.thedigitalincomeedit.com/weekend-ecosystem/preview) as the softer link for cold readers.

Research first: check real search demand and what ranks now for each topic, and replace any where a small site can't compete. Start from: Beacons vs Stan Store; build a website without WordPress; Skool vs a Facebook group for a paid community; Astro vs WordPress for a beginner blog; selling digital products without Etsy fees; building a faceless website with AI; how long a blog site really takes to build; what to put on a link-in-bio page that sells; Squarespace vs building your own site; connecting email signup to a new website; getting a new site indexed by Google; the best free email platform for a new creator; turning a blog into a digital product business; a sales page with no designer; launching a site in one weekend.

Every article: site voice; TDIE itself as the proof (built faceless and solo with AI; every article on the site started as a Skool lesson); Tina Alexander's review through the Testimonial component (her spelling "word press" kept); comparisons with current pricing read today from each company's own page, with a "checked [date]" line; passes the Six M pre-ship check. Match the structure and components of the existing articles exactly.

Build rules: each article is an .astro file in `src/pages/learn/`, with entries in the `src/pages/learn/index.astro` cluster array and `src/data/article-dates.js`; flat URL, no trailing slash; CTAs through ArticleLayout's `related` prop, never a hardcoded block; free slot only a $0 resource, paid slot never an affiliate, at most one price in the close-out. Link each article into its pillar article and the pillar back.

For each article also write the 24-asset Repurposing Pack (10 Pinterest pins routed to https://www.skool.com/thedigitalincomeedit/about, 1 carousel, 8 Threads posts, 2 reels, 1 Facebook post, 1 email, 1 Skool post), every carousel slide with its own complete image prompt, saved as `ops/cloud-output/packs/<slug>.md`. Don't post any of it.

Run npm run build, commit, push to main. After the deploy, load all 15 live URLs with the headless browser and confirm each loads with its CTA and testimonial and every link resolves. Report in one line with the count of live articles.

----- END -----

---

## JOB 6 · DFY PROOF SAMPLES (Opus)

----- START -----

Attach the repo jodiedeo7-glitch/tdie and clone it. Read `ops/cloud-kit/README_START_HERE.md` and follow it for this whole session. Then read `ops/canon/canon.json`, `ops/cloud-kit/TDIE_DFY_SERVICES.md`, `ops/cloud-kit/TDIE_DESIGN_RULES.md`, `ops/cloud-kit/TDIE_IMAGE_GENERATION_MASTER.md`, `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md` and `ops/cloud-kit/TDIE_SIX_M_FRAMEWORK.md`. Also fetch the public DFY Services course at https://www.skool.com/thedigitalincomeedit/classroom/c83b49d5 and read each service lesson's own description; if it won't load, work from TDIE_DFY_SERVICES.md. Start your first reply with "Sources checked: [file names]."

THE JOB. Every DFY service lesson has only a short worked example. Build a full proof sample for each of the eleven services in TDIE_DFY_SERVICES.md: the actual finished thing a buyer receives, built for one realistic made-up client with an obviously fictional business name (never a real brand). Every sample says "Sample built for a fictional client."

What each holds, big enough to judge: the full first week of the Threads calendar; 5 finished pin designs with copy; 2 of the 6 emails in full; 1 complete Etsy listing; 3 looks from the storefront launch; 5 of the 30 persona prompts; the dashboard as a working one-page HTML file; a one-week run log from The Engine; a full week of Skool Autopilot posts; one week of the Instagram calendar; 6 of the 24 repurposing assets. Prices, discounts and order words exactly as in TDIE_DFY_SERVICES.md. Never touch the spicy lesson or anything listed as untouched.

Build each as a designed PDF following TDIE_DESIGN_RULES.md exactly, checked at thumbnail size. Where a photo belongs, write the complete image prompt per the image master and leave a clean placeholder.

Commit all eleven PDFs and their image prompts to `ops/cloud-output/dfy-samples/`, push, and send Jodie the PDFs. Add to `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`: generate the photos (every prompt written in), drop them into the PDFs, then attach each PDF to its own DFY lesson in Skool with this line added above the "Ready to order?" block: "See the whole thing first: [sample name] (sample built for a fictional client)." Include the Skool writing mechanics from TDIE_DFY_SERVICES.md.

Report in one line.

----- END -----

---

## DESKTOP FINISH (run once, later, on your computer, on your normal weekly usage)

Open the Claude desktop app on your computer, with Claude in Chrome connected and signed into Skool, Beacons, Amazon, Gemini and Higgsfield. Start a session in the TDIE Website project and paste:

----- START -----

Attach the repo jodiedeo7-glitch/tdie with push access and clone it. Read `ops/cloud-kit/README_START_HERE.md`, `claude/CLAUDE_SOURCE_CHECK_RULE.md` from the project, and `ops/cloud-output/DESKTOP_FINISH_QUEUE.md`. Start your first reply with "Sources checked: [file names]." Work through every section of the finish queue in order, using Chrome on this computer. Take the browser lock in `claude/TDIE_BROWSER_LOCK.md` first. Generate images per `claude/TDIE_IMAGE_GENERATION_MASTER.md` (Gemini first for anything with Tommy Kate, Seedream 4.5 with Unlimited on for anything without her). Read back every Skool, Beacons and site change live before marking it done; Skool drops writes silently. Skip anything waiting on Jodie (for example bot prices she hasn't set) and say so. Update canon.json and TDIE_CANON.md in both the project and the repo the same day if anything in them changed. Mark each queue section DONE with the date. Report "Task completed successfully" in one line if everything passed; otherwise ask me exactly one plain question.

----- END -----
