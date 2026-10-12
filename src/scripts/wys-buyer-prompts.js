// The While-You-Sleep Storefront™: the buyer's answers and the prompts built from them.
// Main path = the run that works on Jodie's own account (Claude + Higgsfield + Metricool +
// Google Drive + GitHub + the built-in browser for Amazon), fully automatic.
// Every step also has a by-hand or cheaper option (Jodie, 28 Sep and 4 Oct 2026: "we cannot gatekeep a single thing").
// Edit here to update every buyer's prompts.

export const SECTIONS = [
 {
  id: 'quick', title: 'Quick Start', note: 'Fill in these and you can start tonight. Everything else has a sensible default.', open: true,
  fields: [
   {id: 'tz', label: 'Your time zone', type: 'select', options: [
    ['America/New_York', 'Eastern'], ['America/Chicago', 'Central'], ['America/Denver', 'Mountain'], ['America/Phoenix', 'Arizona'], ['America/Los_Angeles', 'Pacific'], ['America/Anchorage', 'Alaska'], ['Pacific/Honolulu', 'Hawaii']], def: 'America/New_York'},
   {id: 'amazon', label: 'Your Amazon account', type: 'radio', options: [
    ['influencer', 'Amazon Influencer (I have a storefront and can make Idea Lists)'],
    ['associates', 'Amazon Associates only (no storefront yet)']], def: 'influencer',
    help: 'Associates only? Each pin links to a blog post on your own site instead of an Idea List, so blog posts have to be on (automatic or by hand).'},
   {id: 'storefront', label: 'Your Amazon storefront address', type: 'text', ph: 'https://www.amazon.com/shop/yourname', show: 'amazon=influencer'},
   {id: 'tag', label: 'Your Amazon tracking ID', type: 'text', ph: 'yourname-20', help: 'Find it in the SiteStripe bar at the top of any Amazon page while you are signed in.'},
   {id: 'persona', label: 'Does your storefront have a face?', type: 'radio', options: [
    ['yes', 'Yes, my AI persona (or me) is in the lifestyle photos'],
    ['no', 'No face. Lifestyle photos show hands and the products in use']], def: 'yes'},
   {id: 'personaName', label: 'Her name', type: 'text', ph: 'e.g. Tommy Kate', show: 'persona=yes'},
   {id: 'personaRef', label: 'Link to her reference photo', type: 'text', ph: 'A public image link to one clear photo of her face', show: 'persona=yes', help: 'One clear, well-lit photo where her face is easy to see. This is the only place her look comes from.'},
   {id: 'ig', label: 'Instagram carousels', type: 'radio', options: [['on', 'On'], ['off', 'Off']], def: 'on'},
   {id: 'igAccount', label: 'Instagram account', type: 'text', ph: '@youraccount', show: 'ig=on'},
   {id: 'blog', label: 'Do you have a blog or website for your looks?', type: 'radio', options: [
    ['on', 'Yes, and it lives on GitHub: it publishes each post itself'],
    ['hand', 'Yes, on another website: it writes each post, I paste it in'],
    ['off', 'No blog yet']], def: '',
    help: 'With a blog, every look also gets its own post, so people find your looks on Google as well as Pinterest.'},
   {id: 'blogUpsellOff', type: 'note', show: 'blog=off',
    title: 'Want a blog that fills itself?',
    text: 'The Weekend Ecosystem™ builds your own website and blog in one weekend, set up so this system publishes a post for every look, automatically. Your Storefront works fine without it, and you can add it any time.',
    link: '/weekend-ecosystem/preview', linkText: 'See inside The Weekend Ecosystem™'},
   {id: 'blogUpsellHand', type: 'note', show: 'blog=hand',
    title: 'Rather not paste every post?',
    text: 'The Weekend Ecosystem™ builds a website on GitHub, so this system publishes each blog post for you instead of handing it to you to paste.',
    link: '/weekend-ecosystem/preview', linkText: 'See inside The Weekend Ecosystem™'},
   {id: 'repo', label: 'Your GitHub site', type: 'text', ph: 'yourname/yoursite', show: 'blog=on'},
   {id: 'siteUrl', label: 'Your website address', type: 'text', ph: 'https://www.yoursite.com', show: 'blog=on|blog=hand'},
   {id: 'metricool', label: 'Your Metricool brand name', type: 'text', ph: 'The brand name exactly as Metricool shows it', show: 'pinMode=auto|igMode=auto',
    help: 'Metricool loads and schedules your pins and posts automatically. Its free plan is fine to start; you’ll want to upgrade once you scale up. Doing pins and posts by hand? You don’t need it.'}
  ]
 },
 {
  id: 'hand', title: 'Do any step by hand', note: 'The main path is fully automatic. Any step can be done by hand instead, to save money, credits or Claude usage, or just because you want control. Mix and match.',
  fields: [
   {id: 'srcMode', label: 'Finding the products', type: 'radio', options: [
    ['auto', 'Automatic: it plans the looks and finds the products on Amazon'],
    ['hand', 'By hand: I pick the products and list them in my log under My Picks; it builds the looks from those']], def: 'auto'},
   {id: 'listMode', label: 'Idea Lists', type: 'radio', show: 'amazon=influencer', options: [
    ['auto', 'Automatic: it adds each look to a themed Idea List on my storefront'],
    ['hand', 'By hand: it writes the list name and product links in my log, I add them; pins link to my storefront']], def: 'auto'},
   {id: 'photoMode', label: 'Photos', type: 'radio', options: [
    ['auto', 'Automatic: it makes all 3 photos with the Higgsfield connector (uses credits)'],
    ['hand', 'By hand: it writes the 3 photo prompts, I make them on the Higgsfield website (on plans with Unlimited models, those don’t use credits) and drop them in my Drive folder. It finishes the look the next night']], def: 'auto'},
   {id: 'pinMode', label: 'Pinterest pins', type: 'radio', options: [
    ['auto', 'Automatic: it schedules them in Metricool'],
    ['hand', 'By hand: it writes each pin’s title, description, board and link, I schedule them in Pinterest’s own free scheduler']], def: 'auto'},
   {id: 'igMode', label: 'Instagram carousels', type: 'radio', show: 'ig=on', options: [
    ['auto', 'Automatic: it schedules them in Metricool'],
    ['hand', 'By hand: it writes the caption and photo order, I post them myself']], def: 'auto'}
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
   {id: 'looks', label: 'Looks per night', type: 'radio', options: [['2', '2 looks (6 pins, 2 carousels, and 2 blog posts if you have a blog)'], ['1', '1 look (uses half the credits and Claude usage)']], def: '2'},
   {id: 'time', label: 'Run time', type: 'select', options: [['01:05', '1:05 am'], ['02:05', '2:05 am'], ['03:05', '3:05 am'], ['23:05', '11:05 pm']], def: '01:05'},
   {id: 'igTime', label: 'Instagram posting time', type: 'select', show: 'ig=on', options: [['09:00', '9:00 am'], ['10:00', '10:00 am'], ['12:00', '12:00 pm'], ['19:00', '7:00 pm']], def: '10:00'},
   {id: 'order', label: 'Carousel photo order', type: 'radio', show: 'ig=on', options: [['Basic, Styled, Lifestyle', 'Basic, Styled, Lifestyle'], ['Lifestyle, Styled, Basic', 'Lifestyle first']], def: 'Basic, Styled, Lifestyle'},
   {id: 'credits', label: 'Most image credits per month', type: 'text', def: '350', show: 'photoMode=auto', help: 'When it reaches this, it stops making images and tells you. It never switches models to save credits on its own.'},
   {id: 'approve', label: 'Approvals', type: 'radio', show: 'pinMode=auto|igMode=auto', options: [['on', 'On: every pin and carousel waits in Metricool for my OK'], ['off', 'Off: fully automatic']], def: 'on',
    help: 'I recommend approvals on for your first few days. Turn them off when you trust it.'}
  ]
 }
];

export function defaults() {
 const a = {};
 for (const s of SECTIONS) for (const f of s.fields) if (f.type !== 'note') a[f.id] = Array.isArray(f.def) ? [...f.def] : (f.def ?? '');
 return a;
}

// "k=v|k2=v2" shows a field when any one of the conditions is true.
export function shown(cond, a) {
 if (!cond) return true;
 return cond.split('|').some((c) => {const [k, val] = c.split('='); return a[k] === val;});
}

const v = (x, fb = '') => (Array.isArray(x) ? x.join(', ') : String(x ?? '').trim()) || fb;
const tzName = (tz) => (SECTIONS[0].fields[0].options.find((o) => o[0] === tz) || [tz, tz])[1];
const hm = (t) => {const [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; return `${((h + 11) % 12) + 1}:${String(m).padStart(2, '0')} ${ap}`;};

// What each mode works out to for this buyer.
function modes(a) {
 const inf = a.amazon === 'influencer';
 const ig = a.ig === 'on';
 const m = {
  inf, ig,
  srcHand: a.srcMode === 'hand',
  listAuto: inf && a.listMode !== 'hand',
  listHand: inf && a.listMode === 'hand',
  photoAuto: a.photoMode !== 'hand',
  pinAuto: a.pinMode !== 'hand',
  igAuto: ig && a.igMode !== 'hand',
  igHand: ig && a.igMode === 'hand',
  blogAuto: a.blog === 'on',
  blogHand: a.blog === 'hand',
  blog: a.blog === 'on' || a.blog === 'hand'
 };
 m.metricool = m.pinAuto || m.igAuto;
 m.approve = m.metricool && a.approve === 'on';
 m.anyHand = m.srcHand || m.listHand || !m.photoAuto || !m.pinAuto || m.igHand || m.blogHand;
 return m;
}

export function missing(a) {
 const m = modes(a);
 const need = [['tag', 'Amazon tracking ID']];

 if (m.metricool) need.push(['metricool', 'Metricool brand name']);
 if (m.inf) need.push(['storefront', 'Amazon storefront address']);
 if (a.persona === 'yes') need.push(['personaName', 'her name'], ['personaRef', 'her reference photo link']);
 if (m.ig) need.push(['igAccount', 'Instagram account']);
 if (m.blogAuto) need.push(['repo', 'GitHub site']);
 if (m.blog) need.push(['siteUrl', 'website address']);
 const out = need.filter(([k]) => !String(a[k] ?? '').trim()).map(([, n]) => n);
 if (!a.blog) out.unshift('whether you have a blog');
 if (!m.inf && !m.blog) out.push('blog posts switched on, automatic or by hand (Associates only needs them)');
 return out;
}

export function recipe(a) {
 const m = modes(a);
 const persona = a.persona === 'yes'
  ? `PERSONA: ${v(a.personaName, '[HER NAME]')}. Reference photo: ${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}. Her look comes only from that photo.`
  : 'PERSONA: none. Lifestyle photos show hands and the products in use, never a face.';
 const how = (auto) => (auto ? 'automatic' : 'by hand');
 return `MY STOREFRONT RECIPE
TIME ZONE: ${a.tz} (${tzName(a.tz)})
AMAZON: ${m.inf ? `Amazon Influencer. Storefront: ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}` : 'Amazon Associates only (no storefront). Pins link to my blog posts.'}
TRACKING ID: ${v(a.tag, '[YOUR TRACKING ID]')}
${m.metricool ? `METRICOOL BRAND: ${v(a.metricool, '[YOUR METRICOOL BRAND]')}\n` : ''}${persona}
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
FINDING PRODUCTS: ${how(!m.srcHand)}${m.inf ? `\nIDEA LISTS: ${how(m.listAuto)}` : ''}
PHOTOS: ${how(m.photoAuto)}
PINS: ${how(m.pinAuto)}
INSTAGRAM: ${m.ig ? `on (${how(m.igAuto)}), ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')}, posts at ${hm(a.igTime)}, photo order ${a.order}` : 'off'}
BLOG: ${m.blogAuto ? `automatic, GitHub site ${v(a.repo, '[YOUR GITHUB SITE]')}, live at ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')}` : m.blogHand ? `by hand, my site ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')}` : 'off'}
${m.photoAuto ? `MONTHLY IMAGE CREDIT LIMIT: ${v(a.credits, '350')}\n` : ''}${m.metricool ? `APPROVALS: ${m.approve ? 'on (every pin and carousel waits in Metricool for my OK)' : 'off (fully automatic)'}` : 'APPROVALS: not needed (I post by hand)'}`;
}

export function nightly(a) {
 const m = modes(a);
 const n = v(a.looks, '2');
 const face = a.persona === 'yes';
 const lifestyle = face
  ? `Lifestyle: Nano Banana Pro at 2K. Attach her reference photo FIRST (identity only) and the look's accepted Styled photo SECOND (room and products only). The prompt opens with exactly: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair, skin or body anywhere in the prompt. Her face is visible. She is doing something real with the products in one of HER WORLD places (putting it up, wearing it out, using it), mid-moment, not posing. Use a clearly different camera angle, framing or viewpoint from the Styled photo: a new photograph, never her pasted into the Styled frame. No text on the photo.`
  : `Lifestyle: Seedream 5.0 Flash at 2K with the look's accepted Styled photo attached (room and products only). Hands and the products in use in one of HER WORLD places, mid-moment, from a clearly different camera angle or framing than the Styled photo. No face anywhere in the frame. No text on the photo.`;
 const dest = m.listAuto ? 'the themed Idea List the look\'s products are on'
  : m.listHand ? `my storefront (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')})`
  : 'the look\'s blog post';
 const site = v(a.siteUrl, '[YOUR WEBSITE ADDRESS]');
 let s = 0; const step = (t) => `STEP ${++s} · ${t}`;
 const parts = [];

 parts.push(`WHILE-YOU-SLEEP STOREFRONT: NIGHTLY RUN
Make ${n} complete look${n === '1' ? '' : 's'} tonight. Follow every step in order. My recipe is at the bottom and governs every choice.${m.anyHand ? ' Steps marked BY HAND are mine: for those, write exactly what I need under "To Do By Hand" in the log, newest first, and never do them yourself.' : ''}

FIRST
1. Get today's date and time in ${a.tz}. Use that time zone for every date and time below.
2. Open my Google Doc "While-You-Sleep Log" with the Google Drive connector. Read every section: My Corrections, ${m.srcHand ? 'My Picks, ' : ''}Looks, ${m.inf ? 'Idea Lists, ' : ''}Products Used, Pins, Instagram, Blog, Credits, To Do By Hand, Runs. My Corrections override everything in this prompt except the NEVER list.
   Under Runs: if an earlier run is marked "started" but not "finished", it stopped partway. Finish that run's missing steps first, using what the log already records, and never redo a step the log shows as done. Then write "Run [today's date] started" under Runs before you do anything else.${m.photoAuto ? `
3. Higgsfield connector: read my credit balance. Add up this month's credits in the log. Tonight needs about ${n === '1' ? '3' : '6'} credits plus fixes. If tonight would go past ${v(a.credits, '350')} credits for the month, make no images, write it in the log and tell me in one line.` : `
3. Finish waiting looks first: for every look in the log marked "Waiting for photos", look in my Google Drive folder "While-You-Sleep Storefront/Photos/<look name>". If its Basic, Styled and Lifestyle photos are all there, check them: right pieces in the right colors, words spelled right and only on the Basic, ${face ? 'she matches her reference, ' : ''}nothing from PHOTOS I HATE (if one fails, tell me which and why, and leave that look waiting). Then do every step after PHOTOS for that look tonight and mark it done. Looks still missing photos stay waiting; don't remind me more than once a day.`}`);

 parts.push(`${step('PLAN')}
${m.srcHand ? `Build tonight's looks from the products under My Picks in the log that haven't been used yet. Group them into looks that make sense together. If there aren't enough picks for ${n} look${n === '1' ? '' : 's'}, make fewer and tell me in the report how many more picks you need.` : 'For each look choose a theme from my CATEGORIES and LOOKS ARE FOR that fits what people are shopping for in the next six weeks (season, holidays, occasions), skipping anything in my NEVER lists. Spread categories across the week.'} Never repeat a look in the log. Each look is one of: an outfit (5 to 8 pieces), a themed collection (5 to 8 pieces) or a roundup (3 or 5 pieces). Give it a name people would search for, like "The Pink Plaid Pumpkin Patch Outfit".${m.inf ? '\nIdea Lists are themed collections, not one list per look. Many looks come from one list. Use an existing themed list from the log when the theme fits and it holds fewer than 30 items; otherwise start a new themed list named for the theme (for example "Pink Halloween Decor").' : ''}`);

 parts.push(`${step(m.srcHand ? 'CHECK MY PICKS (the built-in browser in the Claude desktop app, on amazon.com)' : 'SOURCE (the built-in browser in the Claude desktop app, on amazon.com)')}
Open one new tab. ${m.srcHand ? 'Open each of my picks and check it is in stock and record its ASIN, a short plain name and the exact color or variant. If one is out of stock, leave it out and say so in the report.' : 'Search Amazon for each piece. Open every candidate and check: in stock, at least 4 stars with real reviews, the exact color or variant fits my recipe, no logos and no licensed characters. Pick the piece and record its ASIN, a short plain name and the exact color or variant. Don\'t reuse a product used in the last 30 days (Products Used in the log).'} Never add anything to a cart, never buy, never type a password. If Amazon is signed out, stop and tell me in one line.`);

 if (m.listAuto) parts.push(`${step('IDEA LIST')}
In the same tab go to my storefront (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}), Create content, Idea List. Add every piece of the look to tonight's themed list (create the list if it is new). Open the list's public page and confirm every piece shows. Record the list address. This is public: it is part of the run I set up and approved. Close the tab.`);
 else if (m.listHand) parts.push(`${step('IDEA LIST · BY HAND')}
Close the Amazon tab. Under To Do By Hand write: the themed list name, and every product's name with its link https://www.amazon.com/dp/ASIN. I add them to my Idea List myself.`);
 else parts.push(`${step('LINKS')}
For each piece, copy the link from the SiteStripe bar (Text) so it carries my tracking ID ${v(a.tag, '[YOUR TRACKING ID]')}. Record each link. Close the tab.`);

 const photoRules = `Basic: only the listed pieces, nothing else in the frame. Clothing is a straight-overhead flat lay on a real surface (wood floor, painted table, rug), never laid on a bed and never on upholstered fabric. Anything that stands up is shown standing, at whatever camera angle that takes. A short headline naming the look (2 to 5 words) laid over the photo, products included, in lettering that fits the look and a color picked for this photo so the words read against whatever is under them. No chunky block capitals.
Styled: completely styled in one of HER WORLD places, layered with props and texture that fit PHOTOS I LOVE. No text on the photo.
Every photo: portrait 2:3. It must look REAL and lived-in, in bright natural light. Never rich-looking, staged, fake, plastic or CGI. Nothing branded and no characters or logos anywhere in the frame. Follow PHOTOS I HATE. Don't use the same surface or room as the last look in the log.`;

 if (m.photoAuto) {
  parts.push(`${step('PRODUCT NOTES')}
Look closely at each piece's Amazon photos in the exact color you chose and write one precise line per piece: what it is, exact color, material, pattern or print, shape and size next to the other pieces. These words are how the photos get the products right. Never attach Amazon product photos to an image prompt: the image tool pastes them in as flat rectangles.`);
  parts.push(`${step('PHOTOS (Higgsfield connector, 2K, three per look, in this order)')}
Basic: Seedream 5.0 Flash at 2K, no attachment. Describe every piece from PRODUCT NOTES.
Styled: Seedream 5.0 Flash at 2K with the look's accepted Basic photo attached so the products keep their shapes and colors. A new scene, not the Basic re-shot.
${lifestyle}
Make each photo only after the one before it passes its check.
${photoRules}
CHECK each photo before using it: right pieces in the right colors, words spelled right and only on the Basic, ${face ? 'she matches her reference, ' : ''}nothing from PHOTOS I HATE. Re-run a failed photo once with the fix written into the prompt. If it still fails, skip that look, log why, and move on.`);
 } else {
  parts.push(`${step('PHOTOS · BY HAND')}
Under To Do By Hand write, for each look: its name, the product photo links (each piece's main Amazon photo in the exact color), and three complete, separate, ready-to-paste prompts, one each for Basic, Styled and Lifestyle. Every prompt stands on its own with nothing to fill in. Basic: for Seedream on the Higgsfield website, no attachment, describing every piece in words (what it is, exact color, material, pattern, shape). Styled: for Seedream, with "attach your finished Basic photo" at the top. Make them in order: Basic, then Styled, then Lifestyle. Lifestyle: ${face ? `for Nano Banana Pro, with "attach her reference photo first, then your finished Styled photo" at the top, from a different camera angle than Styled, and the prompt itself opening with exactly: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair, skin or body. Her face is visible, doing something real with the products in one of HER WORLD places, mid-moment.` : 'for Seedream, with "attach your finished Styled photo" at the top, hands and the products in use in one of HER WORLD places from a different angle than Styled, no face.'}
Write these rules into the prompts themselves: ${photoRules.replace(/\n/g, ' ')}
Tell me to save the three finished photos as Basic, Styled and Lifestyle in "While-You-Sleep Storefront/Photos/<look name>" in my Google Drive. Mark the look "Waiting for photos" in the log and stop work on that look tonight. The steps below run for it on the night the photos are there.`);
 }

 if (m.blogAuto) parts.push(`${step(`BLOG POST (GitHub connector, site ${v(a.repo, '[YOUR GITHUB SITE]')})`)}
Find the newest blog post in the site and copy its format exactly. Add a post for the look: the look's name as the title, a 60 to 100 word intro in MY VOICE (first person, one real specific moment), the three photos in the order Basic, Styled, Lifestyle with plain alt text, every piece with its Amazon link in the form https://www.amazon.com/dp/ASIN?tag=${v(a.tag, '[YOUR TRACKING ID]')}${m.inf ? ' and a button to the Idea List' : ''}, and an affiliate disclosure and an AI-generated images note. Publish it, wait for the site to update, open the live page at ${site} and confirm all three photos and every link load. Record the address.`);
 else if (m.blogHand) parts.push(`${step('BLOG POST · BY HAND')}
Under To Do By Hand write the full post, ready to paste: the look's name as the title, a 60 to 100 word intro in MY VOICE (first person, one real specific moment), where each of the three photos goes (Basic, Styled, Lifestyle) with plain alt text, every piece with its Amazon link in the form https://www.amazon.com/dp/ASIN?tag=${v(a.tag, '[YOUR TRACKING ID]')}${m.inf ? ' and the Idea List link' : ''}, and this note at the end: "As an Amazon Associate I earn from qualifying purchases. Photos are AI-generated styling ideas; check each listing for the exact item." Ask me to paste the post's address under the look in the log once it's live on ${site}.${!m.inf ? ' The pins for this look wait until that address is in the log.' : ''}`);

 const pinText = `Three pins per look, one per photo. Each goes to the most specific board in my PINTEREST BOARDS. Pin title: the search phrase first, under 100 characters. Description: two or three natural sentences with the words people search for, no hashtags. Link: ${dest}. Alt text: a plain description of the photo. A look's three pins go on three separate days that aren't next to each other, different looks are mixed together, and no day gets more than ${v(a.slots, '8')} pins.`;
 if (m.pinAuto) parts.push(`${step(`PINS (Metricool connector, brand ${v(a.metricool, '[YOUR METRICOOL BRAND]')})`)}
${pinText} Read Metricool's schedule first and use open days. If Metricool already holds a pin with the same photo and link (from a run that stopped partway), don't make it again. Set the date, time and time zone (${a.tz}) on every post. ${m.approve ? 'APPROVALS ARE ON: send every pin to Metricool for review instead of scheduling it.' : 'Schedule them.'} Read each one back from Metricool and confirm it is there with the right photo, board and link.`);
 else parts.push(`${step('PINS · BY HAND')}
${pinText} Under To Do By Hand write each pin: which photo, board, title, description, link, alt text and the date to schedule it. I schedule them in Pinterest's own scheduler.`);

 if (m.igAuto) parts.push(`${step(`INSTAGRAM (Metricool connector, ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')})`)}
One carousel per look on the next day that has no carousel, at ${hm(a.igTime)}: the three photos in the order ${a.order}. Caption in MY VOICE, three to five short lines, ending with "Shop it: link in bio" and three to five hashtags. No links in the caption. If Metricool already holds this look's carousel, don't make it again. ${m.approve ? 'APPROVALS ARE ON: send it for review instead of scheduling it.' : 'Schedule it.'} Read it back from Metricool.`);
 else if (m.igHand) parts.push(`${step('INSTAGRAM · BY HAND')}
Under To Do By Hand write one carousel per look for ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')}: the photo order (${a.order}), the day to post it at ${hm(a.igTime)}, and the caption in MY VOICE, three to five short lines, ending with "Shop it: link in bio" and three to five hashtags. No links in the caption.`);

 const pinsWord = `${Number(n) * 3} pins`;
 parts.push(`LAST · LOG
Add to the log: each look's name and theme, ${m.inf ? 'Idea List, ' : ''}every ASIN, ${m.photoAuto ? 'the photo links, credits used tonight, ' : ''}${m.blog ? 'the blog address (or that it is waiting for me), ' : ''}every pin and carousel with its date, what's waiting under To Do By Hand, and anything you skipped and why. Last, write "Run [today's date] finished" under Runs. Read the log back to confirm it saved.

REPORT
One line if everything worked: "Tonight: ${n} look${n === '1' ? '' : 's'}${m.photoAuto ? `, ${pinsWord}${m.pinAuto ? (m.approve ? ' waiting for your OK in Metricool' : ' scheduled') : ' ready for you'}` : ', photo prompts ready for you'}.${m.anyHand ? ' Your by-hand list is in the log.' : ''}" If something failed, say what in plain words and the exact fix.

NEVER: type a password. Buy or add anything to a cart. Post to any account that isn't in my recipe. Do a step marked BY HAND. ${m.photoAuto ? 'Go past my monthly credit limit. Switch image models without telling me. ' : ''}Make any claim about how much money anyone will make.

${recipe(a)}`);

 return parts.join('\n\n');
}

export function setup(a) {
 const m = modes(a);
 const L = 'abcdefgh'.split(''); let i = 0; const c = () => L[i++];
 const conn = [];
 if (m.photoAuto) conn.push(`${c()}. Higgsfield: read my credit balance.`);
 if (m.metricool) conn.push(`${c()}. Metricool: find my brand "${v(a.metricool, '[YOUR METRICOOL BRAND]')}". ${m.pinAuto ? 'Confirm Pinterest is connected and list my Pinterest boards. ' : ''}${m.igAuto ? `Confirm Instagram ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')} is connected.` : ''}`);
 conn.push(`${c()}. Google Drive: make a folder "While-You-Sleep Storefront"${m.photoAuto ? '' : ' with a folder "Photos" inside it'}, and inside it a Google Doc "While-You-Sleep Log" with these headings: My Corrections, ${m.srcHand ? 'My Picks, ' : ''}Looks, ${m.inf ? 'Idea Lists, ' : ''}Products Used, Pins, Instagram, Blog, Credits, To Do By Hand, Runs. Put my recipe (below) at the top. Read it back.`);
 if (m.blogAuto) conn.push(`${c()}. GitHub: open ${v(a.repo, '[YOUR GITHUB SITE]')}. Find where the blog posts live and how a post is built. Tell me in two lines.`);
 conn.push(`${c()}. Built-in browser (the browser inside the Claude desktop app): open amazon.com in a new tab. ${m.listAuto ? `Open my storefront ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')} and confirm I'm signed in (you can see "Create content").` : 'Confirm I\'m signed in (my name shows at the top).'} If I'm signed out, tell me and wait while I sign in. Close the tab.`);

 const boards = m.pinAuto
  ? 'Compare my PINTEREST BOARDS with the boards Metricool lists. If any are missing, list them and ask me whether to create them in Pinterest in the built-in browser. Boards are public, so create them only after I say yes. Then write every board\'s name in the log.'
  : 'List my PINTEREST BOARDS and ask me whether they all exist in Pinterest yet. If any are missing, tell me to create them in Pinterest (or offer to create them in the built-in browser, only after I say yes, because boards are public). Write every board\'s name in the log.';

 const ref = a.persona === 'yes'
  ? (m.photoAuto
   ? `HER REFERENCE\nBring her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) into Higgsfield and record its media ID in the log. Make one test photo of her with Nano Banana Pro at 2K, reference attached, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Show it to me and ask if she looks right.`
   : `HER REFERENCE\nRecord her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) in the log. Write me one test prompt for Nano Banana Pro, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference.", for me to try on the Higgsfield website with her reference attached.`)
  : 'NO FACE\nMy lifestyle photos have no face: hands and products in use only. Write that at the top of My Corrections.';

 const picks = m.srcHand ? `\n\nSTEP 4 · MY PICKS\nAsk me for my first product picks (Amazon links or ASINs, at least ${Number(v(a.looks, '2')) * 5}) and write them under My Picks in the log. Tell me I can add more there any time.` : '';
 const firstN = m.srcHand ? 5 : 4;
 return `WHILE-YOU-SLEEP STOREFRONT: SETUP
You are setting up my While-You-Sleep Storefront. Do these steps in order. After each step tell me in one line whether it passed. If one fails, tell me the exact fix in plain words and wait for me before going on. Never type a password.

STEP 1 · CONNECTIONS
${conn.join('\n')}

STEP 2 · BOARDS
${boards}

STEP 3 · ${ref}${picks}

STEP ${firstN} · FIRST LOOK, WITH ME WATCHING
Make one look using the NIGHTLY RUN below exactly${m.metricool ? ', with one change: approvals are ON for this look whatever my recipe says, so every pin and carousel goes to Metricool for review' : ''}. Then show me ${m.photoAuto ? 'all three photos' : 'the photo prompts'}, ${m.inf ? 'the Idea List, ' : ''}${m.blog ? 'the blog post, ' : ''}the pin text${m.ig ? ' and the caption' : ''}${m.anyHand ? ' and my To Do By Hand list' : ''}, and ask what I'd change. Write every change I give you under My Corrections in the log, in my words. Redo anything I ask, then check it again.

STEP ${firstN + 1} · TURN IT ON
When I say it's right, create a scheduled task named "While-You-Sleep nightly run" that runs every day at ${hm(a.time)} ${tzName(a.tz)} with the full NIGHTLY RUN below as its prompt. Read the task back and tell me when it runs next. If you can't create scheduled tasks here, tell me in one line.

=== NIGHTLY RUN ===
${nightly(a)}`;
}
