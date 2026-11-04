# Blog half review: 09_THE_BLOG_HALF.txt

Tester role 2: a Claude session running the STEP 1 prompt (09 lines 15 to 42) against a typical small Astro site on GitHub and Vercel (Priya's priyaplans.com, a Weekend Ecosystem build), then the weekly task running STEP 3 (lines 51 to 57). No site was built. Each instruction is judged against what a Claude session would actually produce, and compared with the author's working implementation:

- `src/lifestyle/README.md` (format)
- `src/data/lifestyle.js` (loader, categories, disclosure)
- `src/pages/lifestyle/[slug].astro` and `src/pages/lifestyle/index.astro` (pages)
- `astro.config.mjs` (sitemap filter, `trailingSlash: 'never'`) and `vercel.json` (`"trailingSlash": false`)

Verdict: STEP 1 is good enough that a competent Claude Code session will ship a working, mostly SEO-sound section on the first try. The real risk is not STEP 1, it is the hand-off: STEP 3 (the weekly upload) does not match the STEP 1 format closely enough, cannot physically upload a JSON file the way it says, and has no failure handling. Rated per line below: OK / RISK / BREAKS.

---

## Before the prompt

**Line 12. "Open a chat in the Claude desktop app with your website's code folder attached"** : BREAKS as written.
The FINISH block (line 42) asks the session to build the site, run it locally, commit and push. A plain chat with a folder attached can read and write files but cannot run `npm run build`, `astro dev` or `git push`. That needs Claude Code (the Code tab in the desktop app, or the CLI). A Weekend Ecosystem owner has probably used Claude Code before, but the kit says "chat". Fix in FINDINGS F-26.

**Line 10. Pinterest domain test** : OK, and correctly scoped. On the Influencer path (Priya) the pins link to Idea Lists, so the site pages are only for Google. Worth saying that plainly (see line 2 overpromise, F-31).

---

## STEP 1 prompt, instruction by instruction

**Line 15. "Add a shop-the-look section called Lifestyle ... at /lifestyle ... builds itself from data files ... Don't change any existing page."** : RISK.
Two later instructions have to touch existing files: line 32 (nav and footer live in the shared layout or header component) and line 39 (no trailing slash is a site-wide `astro.config` and `vercel.json` setting, not a per-section one). A careful Claude will either stall and ask, or skip them to honor "don't change any existing page". Replace with "Don't change the content or URLs of any existing page. You may edit the shared layout to add the nav and footer links." (F-27)

**Line 18. "src/lifestyle/ holds one JSON file per look plus that look's images, side by side."** : OK, and it is the right call for `astro:assets`. Images under `src/` can be imported (via `import.meta.glob`, as the author does in `lifestyle.js` line 25) and optimized by `<Image>`. The common wrong turn, putting images in `public/`, is closed off by this line. A Claude might instead build an Astro content collection with a `glob()` loader and the `image()` schema helper. That also works, and has one upside: a Zod `z.enum` on category makes a bad category fail loudly instead of silently. Either is acceptable.
RISK: if Claude uses a content collection with pattern `**/*`, the README.md from line 23 is picked up as an entry. Say `*.json`.

**Line 19. File names `<slug>.json`, `<slug>-pin1.jpg`, `<slug>-pin2.jpg`, 1000 by 1500 JPEG** : OK for the site, RISK for the task.
The site does not care about pixel size (`<Image>` resizes). It does care about the extension if the glob is `*.jpg`. The author's glob (`lifestyle.js` line 25) accepts `jpg,jpeg,png,webp`; the kit's prompt does not ask for that tolerance, so a screenshot uploaded as `.png` (the natural screenshot format) is silently ignored and the look is skipped. The author's own files are named `-flatlay.jpg` and `-lifestyle.jpg`, not `-pin1/-pin2`. The kit's names are better for the no-persona path (both pins are flat lays), so keep them, but add "Also accept .jpeg, .png and .webp." (F-11)

**Line 20. JSON fields: slug, title, date, category, season, intro, images[{file, alt}], link, items[{name, link, note}]** : RISK.
- `link` at the top level and `link` inside every item mean two different things. The author calls the top one `ideaList` (README line 19, `[slug].astro` line 81). A Claude writing the weekly JSON from STEP 3 line 52 ("the list link") has a fair chance of writing `listLink` or `ideaList`, and the page silently loses its "Shop every piece on Amazon" button. Rename it `listLink` in both places, or keep `link` and spell it out in STEP 3. (F-17)
- `date` does not say which date (look date, pin 1 date, build date). Sorting on the hub depends on it.
- No slug rule (lowercase, hyphens, a-z0-9 only, max length). The weekly task will improvise.

**Line 21. Categories: 6 to 10 that fit my theme, read MY_RECIPE.txt if attached, otherwise ask** : BREAKS the hand-off.
The categories (slugs) are invented here, once, and written only into the site code (the author keeps them in `src/data/lifestyle.js` lines 11 to 22). The weekly task (STEP 3) must write a `category` value, never sees the repo, and MY_RECIPE.txt has no CATEGORIES line. It will guess ("outfits"? "clothing"? "dark-academia-outfits"?). In the author's loader an unknown category is silently dropped (`lifestyle.js` line 35: `catSlugs.has(l.category)`), so the page 404s and the task logs "not live" with no reason. In a naive implementation `categoryOf(...)` returns undefined and `cat.name` throws, failing the whole Vercel build. Also: "if I attach it" is odd, the STEP 1 chat has the site code attached, not the storefront folder. Fix: the STEP 1 prompt prints the category slugs at the end, and STEP 2 adds a `LIFESTYLE CATEGORIES:` line to MY_RECIPE.txt that maps each board to a category. (F-10)

For Priya a sensible set: `outfits`, `study-desk`, `reading-corner`, `dorm`, `accessories`, `jewelry`, `books-and-stationery`, `gifts`. Note: `books` as a category will attract book looks that R5 and R6 make almost impossible to picture or name (F-20).

**Line 22. "A look with no images or no items is skipped by the build. A look slug that equals a category slug stops the build with a clear error."** : RISK.
- "No images" is ambiguous: an empty `images` array, or image entries whose files are not in the folder? The second is the common failure (JSON uploaded before images, or a `.png` named `.jpg`). The author handles it (`lifestyle.js` lines 38 to 40 drop images with no matching file, then line 43 skips the look). A Claude following the kit literally checks `images.length` and then passes `src: undefined` to `<Image>`, which throws an Astro image error (missing or invalid src) and fails the build for every page on the site. Spell it out. (F-30)
- The slug-clash error is correct in intent (the author does it in `getStaticPaths`, line 11). But a build failure on Vercel means the new look never goes live, and the weekly task only sees a 404 after two minutes. It has no way to read the error. See F-13.
- Missing: unknown category, malformed JSON, duplicate slug across two files. A malformed JSON (a trailing comma typed into GitHub's editor) makes Vite's JSON import throw and fails the whole build.

**Line 23. README.md inside src/lifestyle/ with one example JSON** : OK. Good for the human. The weekly task never reads it (it isn't in the storefront folder), so the README cannot be the source of truth for STEP 3.

**Line 26. Hub: headline, one line, category cards with count or "Coming soon", latest 24 looks** : OK. Matches the author's `index.astro`. Missing: what the hub shows when there are zero looks (the author has an empty-state line, `index.astro` line 44). Line 42's empty build test will expose it, so a Claude will likely add one.

**Line 27. Category page: heading, blurb, every look** : OK functionally. SEO RISK: at 7 looks a week an outfits category passes 100 looks in 6 months with no pagination, all on one page; and empty categories are thin "Coming soon" pages that still go into the sitemap (line 38). The author's site has the same issue (`[slug].astro` line 46 renders "Nothing here yet" and it is indexable). Add: "A category with no looks is noindex and left out of the sitemap until it has one." (F-29)

**Line 28. Look page: eyebrow to category, H1 title, intro, one-line affiliate notice, images, numbered "Shop the look" list, "Shop every piece on Amazon" button if link, up to 4 more looks** : OK. Matches `[slug].astro` lines 59 to 100 closely. Order puts the notice above the images: good for FTC placement.

**Line 29. rel="sponsored nofollow noopener", new tab** : OK. Matches the author (`[slug].astro` line 22).

**Line 30. End-of-page disclosure text** : OK. Identical to `lifestyle.js` line 49. On the Influencer path the site uses "As an Amazon Associate" while the pins use "As an Amazon Influencer". Both are defensible, but a buyer will ask why they differ.

**Line 31. No prices** : OK.

**Line 32. Add Lifestyle to nav and footer** : OK, but conflicts with line 15 (F-27).

**Line 35. HTML title = look title; meta description = intro cut to 155 at a word boundary** : OK and better than the author's own (`[slug].astro` line 55 cuts at 158 mid-word). Missing: many Weekend Ecosystem layouts append " | Site Name" to every title. Say whether to keep the suffix; the look titles are already 55 to 70 characters.

**Line 36. One H1; alt from JSON; site's image optimization; lazy below the first screen** : OK and correct. Note the author's own site does not do this: `<Image>` defaults to `loading="lazy"`, so the first look image (the LCP element) is lazy on every look page. The kit's wording is right; a Claude should add `loading="eager"` and `fetchpriority="high"` to the first image. Worth making explicit: "The first image on a look page loads eagerly with fetchpriority high."

**Line 37. Social share image = first image** : RISK. The share image must be an absolute URL. In Astro that means `new URL(image.src, Astro.site)`, which needs `site` set in `astro.config`. The author's layout builds it from a `SITE` constant (`PageLayout.astro` line 15). A typical small site may not have `site` set (see line 38 too). The 2:3 portrait image is fine for Pinterest; Facebook and X crop it. Acceptable.

**Line 38. Every hub, category and look page in the sitemap** : RISK.
- If the site already uses `@astrojs/sitemap`, this happens automatically (and requires `site` in the config). If the site has no sitemap, Claude must add the integration: that touches `astro.config` and `package.json` ("don't change any existing page" again).
- If the site has a hand-written `sitemap.xml.ts` endpoint (common in Weekend Ecosystem style builds that list content collections), the new pages must be added by hand there. The prompt should say "Use the sitemap the site already has; if there is none, add @astrojs/sitemap and set `site`."
- The sitemap URLs must match the canonical form exactly (see line 39). The author's config comment records losing 26 pages to exactly this mismatch.

**Line 39. Clean, flat URLs with no dates and no trailing slash** : RISK, and missing the canonical.
- "No trailing slash" is global: `trailingSlash: 'never'` in `astro.config` plus `"trailingSlash": false` in `vercel.json` (the author has both). If Priya's site currently uses the default (`ignore`) and serves both forms, flipping it changes every existing URL's canonical form. That is exactly what line 15 forbids, and it can cost rankings for a while. Replace with "Use the same trailing-slash form the rest of the site uses, and make the canonical tag, the sitemap and internal links all use that one form."
- The prompt never asks for a canonical tag. The author's layout sets one (`PageLayout.astro` line 14). Add it. (F-28)
- Structured data (BreadcrumbList on look and category pages, ItemList of the pieces) is not asked for. Optional, but cheap and helps the "found on Google" promise.

**Line 42. FINISH: two example looks, build, fix, show locally, delete, rebuild empty, commit, push** : Mostly OK. A good test. Risks:
- "using any two images already in my site as stand-ins": images in `public/` cannot be imported by the glob; Claude has to copy them into `src/lifestyle/` renamed to `<slug>-pin1.jpg`. It will work that out. When it deletes the examples it must delete the copied images too, or they sit in the repo forever. Say so.
- "Push" assumes the branch is `main` and has no protection. STEP 2's upload URL also hard-codes `main`. Many older repos use `master`.
- "Tell me in one line when it's live": the session has to open the production URL after Vercel builds. Fine in Claude Code.

---

## STEP 2 (lines 45 to 49)

- `REPO UPLOAD PAGE: (your GitHub repo address)/upload/main/src/lifestyle` : the URL format is correct for GitHub (for Priya: `https://github.com/priyaplans/site/upload/main/src/lifestyle`). It commits straight to `main`, which triggers a Vercel production deploy. Fine.
- Missing lines: `LIFESTYLE CATEGORIES:` (F-10), the branch name, and whether SITE is `www` or apex.
- "or paste 02_SETUP_PROMPT.txt again and tell it you now have the blog half": 02 has no question or field for this, so "change one answer" has nothing to change. (F-09)

## STEP 3 (lines 51 to 57) vs the STEP 1 format

| STEP 1 defines | STEP 3 says to write | Match? |
|---|---|---|
| file `<slug>.json` | "Writes the look's JSON" | No file name, no slug rule |
| `slug` | not listed | **Missing** |
| `title` | title | OK |
| `date` (YYYY-MM-DD) | date | OK, but which date is undefined |
| `category` (one of the site's slugs) | category | **Task cannot know the slugs** (F-10) |
| `season` (season name or "Evergreen") | season | OK, but window names ("Early fall and Halloween") are not season names |
| `intro` | "2 to 3 sentence intro in your voice, no prices" | OK |
| `images[{file, alt}]` | "image alt text" | **`file` not mentioned**; the task must know to write `<slug>-pin1.jpg` and `<slug>-pin2.jpg` |
| `link` (Idea List) | "the list link" | Name mismatch risk (`link` vs `listLink` / author's `ideaList`) (F-17) |
| `items[{name, link, note}]` | "every item with its SiteStripe short link" | OK |
| `<slug>-pin1.jpg`, `-pin2.jpg`, 1000 x 1500 JPEG | "Saves both pin images at 1000 by 1500 as JPEG" | Saves where? R9 bans downloads, the capture method is a screenshot, and a screenshot is neither 1000 x 1500 nor necessarily JPEG (F-11) |

Method problems:
1. **The JSON cannot go through the file input.** Line 54 says "uploads the files in one go through the file input". The browser tools can hand a captured screenshot to a file input; they cannot hand over a text file the task composed. The workable route is GitHub's create-file page (`/new/main/src/lifestyle?filename=<slug>.json`) with the JSON pasted in. Two cautions: GitHub's code editor can auto-close brackets and quotes when text is typed key by key, so the JSON must be pasted, not typed; and the images must be committed first, or the first deploy has a look with missing images (fine in the author's loader, a build failure in a naive one). (F-12)
2. **"Waits about two minutes"** : an Astro build that optimizes every image in `src/lifestyle/` (3 widths x 2 images x every look) gets slower every week. At 7 looks a week that is about 700 images after 6 months. Two minutes will not always be enough, and there is no instruction for "it still 404s". Poll up to 10 minutes, then log "page not live" and tell the buyer to open Vercel's Deployments page. (F-13)
3. **Order contradiction.** Line 51 and 03 Part 7 step 4 say "after the pins are verified". Line 57 says on the Associates-only path the page goes up BEFORE the pins are scheduled. 03 is what the weekly task follows step by step, and it never mentions the exception. (F-24)
4. **GitHub sign-in** is not in 01_REQUIREMENTS.txt. The first weekly run with the blog half on will stop at a GitHub login page. (F-25)
5. **Associates site listing.** Priya is on the Influencer path, so 08's "list your site in your Associates account" (08 line 22) never reaches her, but the blog half puts her SiteStripe links on priyaplans.com. (F-23)

## Would a Claude session produce a correct, SEO-sound section?

Yes for STEP 1, with the fixes above: it will match the site's style, use `astro:assets` correctly because images live in `src/`, build with zero looks, and add the pages to an existing `@astrojs/sitemap`. Where it most likely goes wrong without fixes: the trailing-slash change (either skipped or site-wide), no canonical, lazy LCP image, `<Image src={undefined}>` crashing the build when a file is missing, and empty category pages in the sitemap.

No for STEP 3 as written: the weekly task will not reliably produce a page, because it cannot know the category slugs, cannot put a JSON file through a file input, may name the list field differently, and has no recovery when the page does not appear.
