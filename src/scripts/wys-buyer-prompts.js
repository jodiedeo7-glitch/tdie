// The While-You-Sleep Storefront™: the buyer's answers and the prompts built from them.
// Every step here is the run that works on Jodie's own account (Claude + Higgsfield + Metricool +
// Google Drive + GitHub + the built-in browser for Amazon). Edit here to update every buyer's prompts.

export const SECTIONS = [
 {
  id: 'quick', title: 'Quick Start', note: 'Fill in these and you can start tonight. Everything else has a sensible default.', open: true,
  fields: [
   {id: 'tz', label: 'Your time zone', type: 'select', options: [
    ['America/New_York', 'Eastern'], ['America/Chicago', 'Central'], ['America/Denver', 'Mountain'], ['America/Phoenix', 'Arizona'], ['America/Los_Angeles', 'Pacific'], ['America/Anchorage', 'Alaska'], ['Pacific/Honolulu', 'Hawaii']], def: 'America/New_York'},
   {id: 'amazon', label: 'Your Amazon account', type: 'radio', options: [
    ['influencer', 'Amazon Influencer (I have a storefront and can make Idea Lists)'],
    ['associates', 'Amazon Associates only (no storefront yet)']], def: 'influencer',
    help: 'Associates only? Each pin links to a blog post on your own site instead of an Idea List, so the blog half has to be on.'},
   {id: 'storefront', label: 'Your Amazon storefront address', type: 'text', ph: 'https://www.amazon.com/shop/yourname', show: 'amazon=influencer'},
   {id: 'tag', label: 'Your Amazon tracking ID', type: 'text', ph: 'yourname-20', help: 'Find it in the SiteStripe bar at the top of any Amazon page while you are signed in.'},
   {id: 'metricool', label: 'Your Metricool brand name', type: 'text', ph: 'The brand name exactly as Metricool shows it'},
   {id: 'persona', label: 'Does your storefront have a face?', type: 'radio', options: [
    ['yes', 'Yes, my AI persona (or me) is in the lifestyle photos'],
    ['no', 'No face. Lifestyle photos show hands and the products in use']], def: 'yes'},
   {id: 'personaName', label: 'Her name', type: 'text', ph: 'e.g. Tommy Kate', show: 'persona=yes'},
   {id: 'personaRef', label: 'Link to her reference photo', type: 'text', ph: 'A public image link to one clear photo of her face', show: 'persona=yes', help: 'One clear, well-lit photo where her face is easy to see. This is the only place her look comes from.'},
   {id: 'ig', label: 'Instagram carousels', type: 'radio', options: [['on', 'On'], ['off', 'Off']], def: 'on'},
   {id: 'igAccount', label: 'Instagram account', type: 'text', ph: '@youraccount', show: 'ig=on'},
   {id: 'blog', label: 'Blog posts on your own site', type: 'radio', options: [['on', 'On, my site is on GitHub'], ['off', 'Off']], def: 'off',
    help: 'Needs a website that lives on GitHub. No site like that yet? The Weekend Ecosystem™ builds one.'},
   {id: 'repo', label: 'Your GitHub site', type: 'text', ph: 'yourname/yoursite', show: 'blog=on'},
   {id: 'siteUrl', label: 'Your website address', type: 'text', ph: 'https://www.yoursite.com', show: 'blog=on'}
  ]
 },
 {
  id: 'style', title: 'Your look', note: 'This is what makes the looks yours. The more honest you are, the less you will correct later.',
  fields: [
   {id: 'leads', label: 'The words that describe your style most', type: 'text', def: 'feminine, cozy, colorful, trendy'},
   {id: 'alsoStyle', label: 'Also true of your style', type: 'text', def: 'playful, practical, whimsical'},
   {id: 'avoidStyle', label: 'Styles you never want', type: 'text', def: 'minimalist, beige everything, cold modern'},
   {id: 'colors', label: 'Your signature colors', type: 'text', def: 'pink, green, blue, lavender, prints'},
   {id: 'colorsSome', label: 'Colors you use sometimes', type: 'text', def: 'rust, gold, navy, camel, black, cream'},
   {id: 'colorsNever', label: 'Colors you never want', type: 'text', def: 'none'},
   {id: 'cue', label: 'Your signature touch (optional)', type: 'text', def: '', ph: 'e.g. a little sparkle in every look'},
   {id: 'visualYes', label: 'Photos you love', type: 'text', def: 'styled and layered, bold and colorful, real and lived-in, bright natural light, full of detail'},
   {id: 'visualNo', label: 'Photos you hate', type: 'text', def: 'beige and neutral everything, generic AI flat lays, too empty, the same surface every time, plastic or CGI looking, rich or staged looking'},
   {id: 'voice', label: 'How you sound', type: 'text', def: 'warm, funny, first person, like texting a friend about something I just bought'}
  ]
 },
 {
  id: 'world', title: 'Her world', note: 'Where the lifestyle photos happen. Real rooms, real errands.',
  fields: [
   {id: 'rooms', label: 'Her rooms and places', type: 'textarea', def: 'kitchen and kitchen island\nhallway or bedroom mirror\nliving room\nlocal outings and errands'},
   {id: 'props', label: 'Things that belong in her world (optional)', type: 'text', def: '', ph: 'e.g. her coffee mug, a dog, kids\' crafts'}
  ]
 },
 {
  id: 'shop', title: 'What it shops for', note: 'It plans and sources the looks itself from these.',
  fields: [
   {id: 'cats', label: 'Categories', type: 'checks', options: ['Women\'s fashion and outfits', 'Home decor', 'Organization, desk and office', 'Beauty, hair and self care', 'Gifts', 'Seasonal and holiday', 'Travel, car and everyday essentials', 'Kids, family and homeschool', 'Cozy hobbies and fun finds', 'Kitchen and hosting', 'Pets'],
    def: ['Women\'s fashion and outfits', 'Home decor', 'Organization, desk and office', 'Beauty, hair and self care', 'Gifts', 'Seasonal and holiday', 'Travel, car and everyday essentials', 'Kids, family and homeschool', 'Cozy hobbies and fun finds']},
   {id: 'uses', label: 'Moments in your life the looks are for', type: 'text', def: 'work from home, family, holidays, self care, gifts, date night, pets, kids, hosting, travel'},
   {id: 'usesNo', label: 'Never make looks for', type: 'text', def: 'none'},
   {id: 'seasonsNo', label: 'Holidays or seasons to skip', type: 'text', def: 'none'},
   {id: 'triggers', label: 'What makes you buy something', type: 'text', def: 'solves a problem, cute version of something boring, giftable, cozy, trendy, seasonal, looks more expensive than it is, everyday upgrade'},
   {id: 'novelty', label: 'Mix', type: 'radio', options: [['mostly novelty', 'Mostly fun and new'], ['balanced', 'Half fun, half practical'], ['mostly practical', 'Mostly practical']], def: 'balanced'}
  ]
 },
 {
  id: 'pins', title: 'Pinterest', note: 'Make these boards in Pinterest first, or let setup make them for you.',
  fields: [
   {id: 'boards', label: 'Your boards, one per line', type: 'textarea', def: 'Cute Amazon Finds for Women\nWomen\'s Fashion and Outfit Ideas | Amazon Finds\nCozy Home Decor Finds | Amazon Finds\nCute Organization, Desk and Office Finds\nBeauty, Hair and Self Care Finds | Amazon Favorites\nGift Ideas for Her, Kids and Family\nSeasonal and Holiday Amazon Finds\nTravel, Car and Everyday Essentials\nKids, Family and Homeschool Finds\nCozy Hobbies and Fun Finds'},
   {id: 'slots', label: 'Most pins in one day', type: 'select', options: [['6', '6'], ['8', '8'], ['10', '10']], def: '8'}
  ]
 },
 {
  id: 'run', title: 'How it runs', note: 'Defaults are the ones I run on my own storefront.',
  fields: [
   {id: 'looks', label: 'Looks per night', type: 'radio', options: [['2', '2 looks (6 pins, 2 carousels, 2 blog posts)'], ['1', '1 look (uses half the credits and Claude usage)']], def: '2'},
   {id: 'time', label: 'Run time', type: 'select', options: [['01:05', '1:05 am'], ['02:05', '2:05 am'], ['03:05', '3:05 am'], ['23:05', '11:05 pm']], def: '01:05'},
   {id: 'igTime', label: 'Instagram posting time', type: 'select', options: [['09:00', '9:00 am'], ['10:00', '10:00 am'], ['12:00', '12:00 pm'], ['19:00', '7:00 pm']], def: '10:00'},
   {id: 'order', label: 'Carousel photo order', type: 'radio', options: [['Basic, Styled, Lifestyle', 'Basic, Styled, Lifestyle'], ['Lifestyle, Styled, Basic', 'Lifestyle first']], def: 'Basic, Styled, Lifestyle'},
   {id: 'credits', label: 'Most image credits per month', type: 'text', def: '350', help: 'When it reaches this, it stops making images and tells you. It never switches models to save credits on its own.'},
   {id: 'approve', label: 'Approvals', type: 'radio', options: [['on', 'On: every pin and carousel waits in Metricool for my OK'], ['off', 'Off: fully automatic']], def: 'on',
    help: 'I recommend approvals on for your first few days. Turn them off when you trust it.'}
  ]
 }
];

export function defaults() {
 const a = {};
 for (const s of SECTIONS) for (const f of s.fields) a[f.id] = Array.isArray(f.def) ? [...f.def] : (f.def ?? '');
 return a;
}

const v = (x, fb = '') => (Array.isArray(x) ? x.join(', ') : String(x ?? '').trim()) || fb;
const tzName = (tz) => (SECTIONS[0].fields[0].options.find((o) => o[0] === tz) || [tz, tz])[1];
const hm = (t) => {const [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; return `${((h + 11) % 12) + 1}:${String(m).padStart(2, '0')} ${ap}`;};

export function missing(a) {
 const need = [['tag', 'Amazon tracking ID'], ['metricool', 'Metricool brand name']];
 if (a.amazon === 'influencer') need.push(['storefront', 'Amazon storefront address']);
 if (a.persona === 'yes') need.push(['personaName', 'her name'], ['personaRef', 'her reference photo link']);
 if (a.ig === 'on') need.push(['igAccount', 'Instagram account']);
 if (a.blog === 'on') need.push(['repo', 'GitHub site'], ['siteUrl', 'website address']);
 const out = need.filter(([k]) => !String(a[k] ?? '').trim()).map(([, n]) => n);
 if (a.amazon === 'associates' && a.blog !== 'on') out.push('blog posts switched on (Associates only needs them)');
 return out;
}

export function recipe(a) {
 const persona = a.persona === 'yes'
  ? `PERSONA: ${v(a.personaName, '[HER NAME]')}. Reference photo: ${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}. Her look comes only from that photo.`
  : 'PERSONA: none. Lifestyle photos show hands and the products in use, never a face.';
 return `MY STOREFRONT RECIPE
TIME ZONE: ${a.tz} (${tzName(a.tz)})
AMAZON: ${a.amazon === 'influencer' ? `Amazon Influencer. Storefront: ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}` : 'Amazon Associates only (no storefront). Pins link to my blog posts.'}
TRACKING ID: ${v(a.tag, '[YOUR TRACKING ID]')}
METRICOOL BRAND: ${v(a.metricool, '[YOUR METRICOOL BRAND]')}
${persona}
HER WORLD: ${v(a.rooms).split('\n').map((x) => x.trim()).filter(Boolean).join('; ')}${v(a.props) ? `\nTHINGS IN HER WORLD: ${v(a.props)}` : ''}
STYLE LEADS: ${v(a.leads)}
ALSO MY STYLE: ${v(a.alsoStyle)}
NEVER MY STYLE: ${v(a.avoidStyle)}
SIGNATURE COLORS: ${v(a.colors)}
SOMETIMES COLORS: ${v(a.colorsSome)}
NEVER COLORS: ${v(a.colorsNever, 'none')}${v(a.cue) ? `\nSIGNATURE TOUCH: ${v(a.cue)}` : ''}
PHOTOS I LOVE: ${v(a.visualYes)}
PHOTOS I HATE: ${v(a.visualNo)}
MY VOICE: ${v(a.voice)}
CATEGORIES: ${v(a.cats)}
LOOKS ARE FOR: ${v(a.uses)}
NEVER MAKE LOOKS FOR: ${v(a.usesNo, 'none')}
SKIP THESE HOLIDAYS OR SEASONS: ${v(a.seasonsNo, 'none')}
WHAT MAKES ME BUY: ${v(a.triggers)}
MIX: ${v(a.novelty)}
PINTEREST BOARDS:
${v(a.boards).split('\n').map((x) => x.trim()).filter(Boolean).map((x) => `- ${x}`).join('\n')}
MOST PINS IN ONE DAY: ${v(a.slots, '8')}
LOOKS PER NIGHT: ${v(a.looks, '2')}
RUN TIME: ${hm(a.time)} ${tzName(a.tz)}
INSTAGRAM: ${a.ig === 'on' ? `on, ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')}, posts at ${hm(a.igTime)}, photo order ${a.order}` : 'off'}
BLOG: ${a.blog === 'on' ? `on, GitHub site ${v(a.repo, '[YOUR GITHUB SITE]')}, live at ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')}` : 'off'}
MONTHLY IMAGE CREDIT LIMIT: ${v(a.credits, '350')}
APPROVALS: ${a.approve === 'on' ? 'on (every pin and carousel waits in Metricool for my OK)' : 'off (fully automatic)'}`;
}

export function nightly(a) {
 const n = v(a.looks, '2');
 const face = a.persona === 'yes';
 const lifestyle = face
  ? `Lifestyle: Nano Banana Pro at 2K. Attach her reference photo FIRST and the product sheet SECOND. The prompt opens with exactly: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair, skin or body anywhere in the prompt. Her face is visible. She is doing something real with the products in one of HER WORLD places (putting it up, wearing it out, using it), mid-moment, not posing. No text on the photo.`
  : `Lifestyle: Seedream 5.0 Flash at 2K with the product sheet attached. Hands and the products in use in one of HER WORLD places, mid-moment. No face anywhere in the frame. No text on the photo.`;
 const dest = a.amazon === 'influencer' ? 'the themed Idea List the look\'s products are on' : 'the look\'s blog post';
 const approve = a.approve === 'on';
 return `WHILE-YOU-SLEEP STOREFRONT: NIGHTLY RUN
Make ${n} complete look${n === '1' ? '' : 's'} tonight: sourced, listed, photographed${a.blog === 'on' ? ', blogged' : ''}, pinned${a.ig === 'on' ? ' and posted to Instagram' : ''}. Follow every step in order. My recipe is at the bottom and governs every choice.

FIRST
1. Get today's date and time in ${a.tz}. Use that time zone for every date and time below.
2. Open my Google Doc "While-You-Sleep Log" with the Google Drive connector. Read every section: Looks, Idea Lists, Products Used, Pins, Instagram, Blog, Credits, My Corrections. My Corrections override everything in this prompt except the NEVER list.
3. Higgsfield connector: read my credit balance. Add up this month's credits in the log. Tonight needs about ${n === '1' ? '3' : '6'} credits plus fixes. If tonight would go past ${v(a.credits, '350')} credits for the month, make no images, write it in the log and tell me in one line.

STEP 1 · PLAN
For each look choose a theme from my CATEGORIES and LOOKS ARE FOR that fits what people are shopping for in the next six weeks (season, holidays, occasions), skipping anything in my NEVER lists. Never repeat a look in the log. Spread categories across the week. Each look is one of: an outfit (5 to 8 pieces), a themed collection (5 to 8 pieces) or a roundup (3 or 5 pieces). Give it a name people would search for, like "The Pink Plaid Pumpkin Patch Outfit".
${a.amazon === 'influencer' ? 'Idea Lists are themed collections, not one list per look. Many looks come from one list. Use an existing themed list from the log when the theme fits and it holds fewer than 30 items; otherwise start a new themed list named for the theme (for example "Pink Halloween Decor").' : ''}

STEP 2 · SOURCE (the built-in browser in the Claude desktop app, on amazon.com)
Open one new tab. Search Amazon for each piece. Open every candidate and check: in stock, at least 4 stars with real reviews, the exact color or variant fits my recipe, no logos and no licensed characters. Pick the piece and record its ASIN, a short plain name and the exact color or variant. Don't reuse a product used in the last 30 days (Products Used in the log). Never add anything to a cart, never buy, never type a password. If Amazon is signed out, stop and tell me in one line.

STEP 3 · ${a.amazon === 'influencer' ? `IDEA LIST
In the same tab go to my storefront (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}), Create content, Idea List. Add every piece of the look to tonight's themed list (create the list if it is new). Open the list's public page and confirm every piece shows. Record the list address. This is public: it is part of the run I set up and approved.` : `LINKS
For each piece, copy the link from the SiteStripe bar (Text) so it carries my tracking ID ${v(a.tag, '[YOUR TRACKING ID]')}. Record each link.`}
Close the tab.

STEP 4 · PRODUCT SHEET
Download each piece's main Amazon photo in the exact color you chose and put all of them on one plain white sheet. If a product photo shows a person's face, cover the face. Upload the sheet to Higgsfield (media upload, then confirm). If you can't make one sheet, upload each photo and attach them all.

STEP 5 · PHOTOS (Higgsfield connector, portrait 2:3, 2K, three per look)
Basic: Seedream 5.0 Flash at 2K, product sheet attached. Only the listed pieces, nothing else in the frame. Clothing is a straight-overhead flat lay on a real surface (wood floor, painted table, rug), never laid on a bed and never on upholstered fabric. Anything that stands up is shown standing, at whatever camera angle that takes. Add a short headline naming the look (2 to 5 words) laid over the photo, products included. Pick the lettering for the look and pick the color for this photo so the words read against whatever is under them. No chunky block capitals.
Styled: Seedream 5.0 Flash at 2K, product sheet attached. Completely styled in one of HER WORLD places, layered with props and texture that fit PHOTOS I LOVE. No text on the photo.
${lifestyle}
Every photo: it must look REAL and lived-in, in bright natural light. Never rich-looking, staged, fake, plastic or CGI. Nothing branded and no characters or logos anywhere in the frame. Follow PHOTOS I HATE. Don't use the same surface or room as the last look in the log.
CHECK each photo before using it: right pieces in the right colors, words spelled right and only on the Basic, ${face ? 'she matches her reference, ' : ''}nothing from PHOTOS I HATE. Re-run a failed photo once with the fix written into the prompt. If it still fails, skip that look, log why, and move on.

${a.blog === 'on' ? `STEP 6 · BLOG POST (GitHub connector, site ${v(a.repo, '[YOUR GITHUB SITE]')})
Find the newest blog post in the site and copy its format exactly. Add a post for the look: the look's name as the title, a 60 to 100 word intro in MY VOICE (first person, one real specific moment), the three photos in the order Basic, Styled, Lifestyle with plain alt text, every piece with its Amazon link in the form https://www.amazon.com/dp/ASIN?tag=${v(a.tag, '[YOUR TRACKING ID]')}${a.amazon === 'influencer' ? ' and a button to the Idea List' : ''}, and an affiliate disclosure and an AI-generated images note. Publish it, wait for the site to update, open the live page at ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')} and confirm all three photos and every link load. Record the address.

` : ''}STEP ${a.blog === 'on' ? '7' : '6'} · PINS (Metricool connector, brand ${v(a.metricool, '[YOUR METRICOOL BRAND]')})
Three pins per look, one per photo. Each goes to the most specific board in my PINTEREST BOARDS. Pin title: the search phrase first, under 100 characters. Description: two or three natural sentences with the words people search for, no hashtags. Link: ${dest}. Alt text: a plain description of the photo. Read Metricool's schedule first and use open days: a look's three pins go on three separate days that aren't next to each other, different looks are mixed together, and no day gets more than ${v(a.slots, '8')} pins. Set the date, time and time zone (${a.tz}) on every post. ${approve ? 'APPROVALS ARE ON: send every pin to Metricool for review instead of scheduling it.' : 'Schedule them.'} Read each one back from Metricool and confirm it is there with the right photo, board and link.

${a.ig === 'on' ? `STEP ${a.blog === 'on' ? '8' : '7'} · INSTAGRAM (Metricool connector, ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')})
One carousel per look on the next day that has no carousel, at ${hm(a.igTime)}: the three photos in the order ${a.order}. Caption in MY VOICE, three to five short lines, ending with "Shop it: link in bio" and three to five hashtags. No links in the caption. ${approve ? 'APPROVALS ARE ON: send it for review instead of scheduling it.' : 'Schedule it.'} Read it back from Metricool.

` : ''}LAST · LOG
Add to the log: each look's name, theme, ${a.amazon === 'influencer' ? 'Idea List address, ' : ''}every ASIN, the photo links, ${a.blog === 'on' ? 'the blog address, ' : ''}every Metricool post with its date, credits used tonight and anything you skipped and why. Read the log back to confirm it saved.

REPORT
If everything worked, one line: "Tonight: ${n} look${n === '1' ? '' : 's'}, ${Number(n) * 3} pins${a.blog === 'on' ? `, ${n} blog post${n === '1' ? '' : 's'}` : ''}${a.ig === 'on' ? `, ${n} carousel${n === '1' ? '' : 's'}` : ''} ${approve ? 'waiting for your OK in Metricool' : 'scheduled'}." If something failed, say what in plain words and the exact fix.

NEVER: type a password. Buy or add anything to a cart. Post to any account that isn't in my recipe. Go past my monthly credit limit. Switch image models without telling me. Make any claim about how much money anyone will make.

${recipe(a)}`;
}

export function setup(a) {
 return `WHILE-YOU-SLEEP STOREFRONT: SETUP
You are setting up my While-You-Sleep Storefront. Do these steps in order. After each step tell me in one line whether it passed. If one fails, tell me the exact fix in plain words and wait for me before going on. Never type a password.

STEP 1 · CONNECTIONS
a. Higgsfield: read my credit balance.
b. Metricool: find my brand "${v(a.metricool, '[YOUR METRICOOL BRAND]')}". Confirm Pinterest is connected${a.ig === 'on' ? ` and Instagram ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')} is connected` : ''}. List my Pinterest boards.
c. Google Drive: make a folder "While-You-Sleep Storefront" and inside it a Google Doc "While-You-Sleep Log" with these headings: My Corrections, Looks, Idea Lists, Products Used, Pins, Instagram, Blog, Credits, Runs. Put my recipe (below) at the top. Read it back.
${a.blog === 'on' ? `d. GitHub: open ${v(a.repo, '[YOUR GITHUB SITE]')}. Find where the blog posts live and how a post is built. Tell me in two lines.
` : ''}${a.blog === 'on' ? 'e' : 'd'}. Built-in browser (the browser inside the Claude desktop app): open amazon.com in a new tab. ${a.amazon === 'influencer' ? `Open my storefront ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')} and confirm I'm signed in (you can see "Create content").` : 'Open any product and confirm the SiteStripe bar shows at the top.'} If I'm signed out, tell me and wait while I sign in. Close the tab.

STEP 2 · BOARDS
Compare my PINTEREST BOARDS with the boards Metricool lists. If any are missing, list them and ask me whether to create them in Pinterest in the built-in browser. Boards are public, so create them only after I say yes. Then write every board's name in the log.

STEP 3 · ${a.persona === 'yes' ? `HER REFERENCE
Bring her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) into Higgsfield and record its media ID in the log. Make one test photo of her with Nano Banana Pro at 2K, reference attached, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Show it to me and ask if she looks right.` : 'NO FACE\nMy lifestyle photos have no face: hands and products in use only. Write that at the top of My Corrections.'}

STEP 4 · FIRST LOOK, WITH ME WATCHING
Make one look using the NIGHTLY RUN below exactly, with one change: approvals are ON for this look whatever my recipe says, so every pin and carousel goes to Metricool for review. Then show me all three photos, ${a.amazon === 'influencer' ? 'the Idea List, ' : ''}${a.blog === 'on' ? 'the blog post, ' : ''}the pin text and the caption, and ask what I'd change. Write every change I give you under My Corrections in the log, in my words. Redo anything I ask, then check it again.

STEP 5 · TURN IT ON
When I say it's right, create a scheduled task named "While-You-Sleep nightly run" that runs every day at ${hm(a.time)} ${tzName(a.tz)} with the full NIGHTLY RUN below as its prompt. Read the task back and tell me when it runs next. If you can't create scheduled tasks here, tell me in one line.

=== NIGHTLY RUN ===
${nightly(a)}`;
}
