// The While-You-Sleep Storefront™: the buyer's answers and the prompts built from them.
// Main path = the run that works on Jodie's own account (Claude + Higgsfield + Metricool +
// Google Drive + GitHub + the built-in browser for Amazon), fully automatic.
// Every step also has a by-hand or cheaper option (Jodie, 28 Sep and 4 Oct 2026: "we cannot gatekeep a single thing").
// Edit here to update every buyer's prompts.

export const SECTIONS = [
 {
  id: 'quick', title: 'Quick Start', note: 'Fill in these and you can start tonight. Everything else has a sensible default.', open: true,
  fields: [
   {id: 'platform', label: 'Which AI runs it?', type: 'radio', private: true, options: [['claude', 'Claude'], ['chatgpt', 'ChatGPT (being tested, not proven yet)']], def: 'claude',
    help: 'Only you can see this choice while the ChatGPT version is tested.'},
   {id: 'imgWhere', label: 'Where do your photos get made?', type: 'radio', show: 'platform=chatgpt', options: [
    ['chatgpt', 'Right in ChatGPT, with its own image maker (no Higgsfield needed)'],
    ['higgsfield', 'Connect Higgsfield and run them there (uses Higgsfield credits)']], def: 'chatgpt',
    help: 'ChatGPT\u2019s image maker comes with your ChatGPT plan, and your plan sets how many images you get. Higgsfield is its own paid plan with credits.'},
   {id: 'tz', label: 'Your time zone', type: 'select', options: [
    ['America/New_York', 'Eastern'], ['America/Chicago', 'Central'], ['America/Denver', 'Mountain'], ['America/Phoenix', 'Arizona'], ['America/Los_Angeles', 'Pacific'], ['America/Anchorage', 'Alaska'], ['Pacific/Honolulu', 'Hawaii']], def: 'America/New_York'},
   {id: 'amazon', label: 'Your Amazon account', type: 'radio', options: [
    ['influencer', 'I have an Amazon storefront and can make Idea Lists in it'],
    ['associates', 'Amazon Associates links only (no Idea Lists yet)']], def: 'influencer',
    help: 'Not sure? Sign in to Amazon, open your storefront and look for Create an Idea List. If it\u2019s there, pick the first answer. Links only? Each pin links to a blog post on your own site instead of an Idea List, so blog posts have to be on (automatic or by hand). Not approved yet? The Get Approved page walks you through it; switch this answer when you can make Idea Lists.'},
   {id: 'storefront', label: 'Your Amazon storefront address', type: 'text', ph: 'https://www.amazon.com/shop/yourname', show: 'amazon=influencer', help: 'Or press Do it for me and it finds it for you.'},
   {id: 'tag', label: 'Your Amazon tracking ID', type: 'text', ph: 'yourname-20', help: 'It ends in -20 and shows in the SiteStripe bar at the top of any Amazon page while you are signed in. Or press Do it for me.'},
   {id: 'persona', label: 'Does your storefront have a face?', type: 'radio', options: [
    ['yes', 'Yes, my AI persona (or me) is in the lifestyle photos'],
    ['no', 'No face. Lifestyle photos show hands and the products in use']], def: 'yes'},
   {id: 'personaName', label: 'Her name', type: 'text', ph: 'e.g. Tommy Kate', show: 'persona=yes'},
   {id: 'personaRef', label: 'Link to her reference photo', type: 'text', ph: 'A public image link to one clear photo of her face', show: 'persona=yes', help: 'One clear, well-lit photo where her face is easy to see. This is the only place her look comes from.'},
   {id: 'ig', label: 'Instagram carousels', type: 'radio', options: [['on', 'On'], ['off', 'Off']], def: 'on'},
   {id: 'igAccount', label: 'Instagram account', type: 'text', ph: '@youraccount', show: 'ig=on'},
   {id: 'blog', label: 'Do you have a blog or website for your looks?', type: 'radio', options: [
    ['on', 'Yes, and my site\u2019s files are kept on GitHub: it publishes each post itself'],
    ['hand', 'Yes, on a website builder (WordPress, Shopify, Squarespace, Wix or similar): it writes each post, I paste it in'],
    ['off', 'No blog yet']], def: '',
    help: 'With a blog, every look also gets its own post, so people find your looks on Google as well as Pinterest. Sites hosted on Cloudflare, Vercel, Netlify or GitHub Pages almost always keep their files on GitHub, so pick the first one. Not sure? Pick the first one, then press Do it for me under the GitHub question.'},
   {id: 'blogUpsellOff', type: 'note', show: 'blog=off',
    title: 'Want a blog that fills itself?',
    text: 'The Weekend Ecosystem™ builds your own website and blog in one weekend, set up so this system publishes a post for every look, automatically. Your Storefront works fine without it, and you can add it any time.',
    link: '/weekend-ecosystem/preview', linkText: 'See inside The Weekend Ecosystem™'},
   {id: 'blogUpsellHand', type: 'note', show: 'blog=hand',
    title: 'Rather not paste every post?',
    text: 'The Weekend Ecosystem™ builds a website on GitHub, so this system publishes each blog post for you instead of handing it to you to paste.',
    link: '/weekend-ecosystem/preview', linkText: 'See inside The Weekend Ecosystem™'},
   {id: 'repo', label: 'Your GitHub site (the place on GitHub where your website\u2019s files are kept)', type: 'text', ph: 'yourname/yoursite', show: 'blog=on'},
   {id: 'branch', label: 'Which version of your site goes live? (the branch name, usually main)', type: 'text', ph: 'main', show: 'blog=on', help: 'GitHub keeps versions of your site called branches. Your host publishes one of them. Posts have to go into that one or they never appear.'},
   {id: 'host', label: 'Where your site is hosted', type: 'select', show: 'blog=on', options: [['', 'Choose one'], ['Cloudflare', 'Cloudflare'], ['Vercel', 'Vercel'], ['Netlify', 'Netlify'], ['GitHub Pages', 'GitHub Pages'], ['other', 'Somewhere else'], ['unsure', 'I am not sure']], def: ''},
   {id: 'siteUrl', label: 'Your website address', type: 'text', ph: 'https://www.yoursite.com', show: 'blog=on|blog=hand'},
   {id: 'metricool', label: 'Your Metricool brand name', type: 'text', ph: 'The brand name exactly as Metricool shows it', show: 'pinMode=auto|igMode=auto',
    help: 'Metricool loads and schedules your pins and posts automatically. Its free plan is fine to start; you’ll want to upgrade once you scale up. Doing pins and posts by hand? You don’t need it. Connect it first (see Check your connections), then press Do it for me to read your brand name.'}
  ]
 },
 {
  id: 'connect', title: 'Check your connections', note: 'Automatic steps only work when the tool behind them is connected and signed in. Each one below says exactly how to connect it, and the button does the checking for you. Your prompts stay locked until every box that applies says Yes. If one says Not yet, connect it first, or switch that step to by hand in the next section.', open: true,
  fields: [
   {id: 'okDrive', label: 'Google Drive is connected', type: 'radio', options: [['yes', 'Yes, it is connected'], ['no', 'Not yet']], def: '',
    how: {claude: ['Open Claude and click <b>Settings</b>, then <b>Connectors</b>.', 'Search for <b>Google Drive</b> and click <b>Connect</b>.', 'Sign in to Google when it asks and click <b>Allow</b>.', 'Press <b>Check it for me</b> below and pick Yes when it works.'],
     chatgpt: ['Open ChatGPT, click your name, then <b>Settings</b>, then <b>Apps</b> (earlier called Connectors).', 'Find <b>Google Drive</b> and click <b>Connect</b>.', 'Sign in to Google when it asks and click <b>Allow</b>.', 'Press <b>Check it for me</b> below and pick Yes when it works.']}},
   {id: 'okMetricool', label: 'Metricool is connected, and your Pinterest business account (and Instagram, if it is on) is connected inside Metricool', type: 'radio', show: 'pinMode=auto|igMode=auto', options: [['yes', 'Yes, they are connected'], ['no', 'Not yet']], def: '',
    how: {claude: ['You need a Metricool account first (its free plan is fine to start). Sign up at metricool.com if you do not have one.', 'In Claude, click <b>Settings</b>, then <b>Connectors</b>, search for <b>Metricool</b> and click <b>Connect</b>. Sign in to Metricool when it asks.', 'Now log in to Metricool itself, open your brand’s <b>Connections</b>, and connect your <b>Pinterest business account</b> (and <b>Instagram</b>, if carousels are on).', 'Press <b>Check it for me</b> below and pick Yes when it shows them.'],
     chatgpt: ['You need a Metricool account first (its free plan is fine to start). Sign up at metricool.com if you do not have one.', 'In ChatGPT, click your name, then <b>Settings</b>, then <b>Apps</b>, find <b>Metricool</b> and click <b>Connect</b>. Sign in to Metricool when it asks.', 'Now log in to Metricool itself, open your brand’s <b>Connections</b>, and connect your <b>Pinterest business account</b> (and <b>Instagram</b>, if carousels are on).', 'Press <b>Check it for me</b> below and pick Yes when it shows them.']}},
   {id: 'okHiggs', label: 'Higgsfield is connected and has credits', type: 'radio', show: 'photoMode=auto&platform=claude|photoMode=auto&imgWhere=higgsfield', options: [['yes', 'Yes, it is connected and has credits'], ['no', 'Not yet']], def: '',
    how: {claude: ['Higgsfield is its own paid plan with credits. Sign up at higgsfield.ai and make sure you have credits.', 'In Claude, click <b>Settings</b>, then <b>Connectors</b>, search for <b>Higgsfield</b> and click <b>Connect</b>. Sign in when it asks.', 'Press <b>Check it for me</b> below. It shows your credit balance. Pick Yes only if the balance is above zero.'],
     chatgpt: ['Higgsfield is its own paid plan with credits. Sign up at higgsfield.ai and make sure you have credits.', 'In ChatGPT, click your name, then <b>Settings</b>, then <b>Apps</b>, find <b>Higgsfield</b> and click <b>Connect</b>. Sign in when it asks.', 'Press <b>Check it for me</b> below. It shows your credit balance. Pick Yes only if the balance is above zero.']}},
   {id: 'okGithub', label: 'GitHub is connected', type: 'radio', show: 'blog=on', options: [['yes', 'Yes, it is connected'], ['no', 'Not yet']], def: '',
    how: {claude: ['In Claude, click <b>Settings</b>, then <b>Connectors</b>, search for <b>GitHub</b> and click <b>Connect</b>.', 'Sign in to GitHub. When it asks which sites (repositories) it may open, choose your website’s.', 'Press <b>Check it for me</b> below and pick Yes when it lists your site.'],
     chatgpt: ['In ChatGPT, click your name, then <b>Settings</b>, then <b>Apps</b>, find <b>GitHub</b> and click <b>Connect</b>.', 'Sign in to GitHub. When it asks which sites (repositories) it may open, choose your website’s.', 'Press <b>Check it for me</b> below and pick Yes when it lists your site.']}},
   {id: 'okAmazon', label: 'You opened amazon.com in the browser the AI will use, the page loaded normally, and you are signed in', type: 'radio', show: 'srcMode=auto|amazon=influencer&listMode=auto', options: [['yes', 'Yes, it loaded and I am signed in'], ['no', 'Not yet, or Amazon refused the browser']], def: '',
    how: {claude: ['In the Claude desktop app, open the browser inside it and go to <b>amazon.com</b>.', 'Sign in with your own Amazon account. Type your own password yourself. The AI never types it.', 'Tick <b>Keep me signed in</b> so it stays signed in overnight.', 'Press <b>Check it for me</b> below. If Amazon says it does not support the browser, pick Not yet: Amazon steps must stay by hand until that works.'],
     chatgpt: ['Connect a browser tool in <b>Settings</b>, then <b>Apps</b>, then open <b>amazon.com</b> in it.', 'Sign in with your own Amazon account. Type your own password yourself. The AI never types it.', 'Tick <b>Keep me signed in</b>.', 'Press <b>Check it for me</b> below. If Amazon says it does not support the browser, pick Not yet: Amazon steps must stay by hand until that works.']}}
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
   {id: 'listGptNote', type: 'note', show: 'platform=chatgpt&amazon=influencer',
    title: 'Idea Lists are by hand on ChatGPT for now',
    text: 'In testing, Amazon refused ChatGPT\u2019s browser ("We do not support your session or client"), so ChatGPT cannot make Idea Lists on its own yet. This stays by hand until it is proven.'},
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
   {id: 'leads', label: 'The words that describe your style most', type: 'pick', options: ["feminine", "cozy", "colorful", "trendy", "farmhouse", "maximalist", "playful", "whimsical", "practical", "girly", "glam", "boho", "vintage", "cottagecore", "classic", "preppy", "western", "edgy", "sporty", "coastal", "modern", "minimalist"], def: ["feminine", "farmhouse", "maximalist", "trendy"]},
   {id: 'alsoStyle', label: 'Also true of your style', type: 'pick', options: ["feminine", "cozy", "colorful", "trendy", "farmhouse", "maximalist", "playful", "whimsical", "practical", "girly", "glam", "boho", "vintage", "cottagecore", "classic", "preppy", "western", "edgy", "sporty", "coastal", "modern", "minimalist"], def: ["colorful", "cozy", "playful", "practical", "whimsical"]},
   {id: 'avoidStyle', label: 'Styles you never want', type: 'pick', options: ["minimalist", "beige everything", "cold modern", "rich or luxury looking", "coastal", "sporty", "preppy", "western", "gothic", "boho", "too girly"], def: ["minimalist", "beige everything", "cold modern", "coastal", "sporty", "rich or luxury looking"], none: 'none'},
   {id: 'colors', label: 'Your signature colors', type: 'pick', options: ["pink", "red", "orange", "rust", "yellow", "gold", "green", "blue", "navy", "lavender", "purple", "camel", "brown", "black", "white", "cream", "gray", "silver", "beige", "pastels", "brights", "prints", "sparkle"], def: ["pink", "green", "blue", "lavender", "prints"]},
   {id: 'colorsSome', label: 'Colors you use sometimes', type: 'pick', options: ["pink", "red", "orange", "rust", "yellow", "gold", "green", "blue", "navy", "lavender", "purple", "camel", "brown", "black", "white", "cream", "gray", "silver", "beige", "pastels", "brights", "prints", "sparkle"], def: ["orange", "rust", "yellow", "gold", "navy", "camel", "brown", "black", "white", "cream", "gray"]},
   {id: 'colorsNever', label: 'Colors you never want', type: 'pick', options: ["pink", "red", "orange", "rust", "yellow", "gold", "green", "blue", "navy", "lavender", "purple", "camel", "brown", "black", "white", "cream", "gray", "silver", "beige", "pastels", "brights", "prints", "sparkle"], def: [], none: 'none', help: 'Leave them all unticked if no color is off limits.'},
   {id: 'cue', label: 'Your signature touch (optional)', type: 'pick', options: ["a little sparkle", "something pink", "a fun print", "something vintage", "a cozy texture", "a pop of bright color", "something handmade"], def: ["a little sparkle"]},
   {id: 'visualYes', label: 'Photos you love', type: 'pick', options: ["styled and layered", "bold and colorful", "real and lived-in", "bright natural light", "full of detail", "playful", "soft and dreamy", "cozy and warm", "clean and simple", "moody and dark"], def: ["styled and layered", "bold and colorful", "real and lived-in", "bright natural light", "full of detail", "playful"]},
   {id: 'visualNo', label: 'Photos you hate', type: 'pick', options: ["beige and neutral everything", "generic AI flat lays", "too empty", "the same surface every time", "plastic or CGI looking", "rich or staged looking", "too cluttered", "too dark", "flowers and bows everywhere"], def: ["beige and neutral everything", "generic AI flat lays", "too empty", "the same surface every time", "plastic or CGI looking", "rich or staged looking", "flowers and bows everywhere"], none: 'none'},
   {id: 'voice', label: 'How you sound', type: 'pick', options: ["warm", "funny", "first person", "like texting a friend about something I just bought", "chatty", "short and sweet", "sassy", "calm", "excited", "helpful expert"], def: ["warm", "funny", "first person", "like texting a friend about something I just bought"]}
  ]
 },
 {
  id: 'world', title: 'Her world', note: 'Where the lifestyle photos happen. Real rooms, real errands.',
  fields: [
   {id: 'rooms', label: 'Her rooms and places', type: 'pick', options: ["kitchen and kitchen island", "hallway or bedroom mirror", "living room", "local outings and errands", "bedroom", "home office", "bathroom vanity", "porch or patio", "backyard or garden", "kids' playroom", "craft room", "gaming room", "in the car", "coffee shop"], def: ["kitchen and kitchen island", "hallway or bedroom mirror", "gaming room", "local outings and errands"], sep: '\n'},
   {id: 'props', label: 'Things that belong in her world (optional)', type: 'pick', options: ["her coffee mug", "a water tumbler", "a dog", "a cat", "kids' crafts", "plants", "books", "candles", "a laptop", "a cozy blanket"], def: []}
  ]
 },
 {
  id: 'shop', title: 'What it shops for', note: 'It plans and sources the looks itself from these.',
  fields: [
   {id: 'cats', label: 'Categories', type: 'checks', options: ['Women\'s fashion and outfits', 'Home decor', 'Organization, desk and office', 'Beauty, hair and self care', 'Gifts', 'Seasonal and holiday', 'Travel, car and everyday essentials', 'Kids, family and homeschool', 'Cozy hobbies and fun finds', 'Kitchen and hosting', 'Pets', 'Licensed characters and fandom favorites'],
    def: ['Women\'s fashion and outfits', 'Home decor', 'Organization, desk and office', 'Beauty, hair and self care', 'Gifts', 'Seasonal and holiday', 'Travel, car and everyday essentials', 'Kids, family and homeschool', 'Cozy hobbies and fun finds']},
   {id: 'chars', label: 'Your favorite licensed characters (optional)', type: 'pick', options: ["Hello Kitty", "Kuromi", "My Melody", "Cinnamoroll", "Pompompurin", "Barbie", "Disney princesses", "Minnie Mouse", "Stitch", "Winnie the Pooh", "Snoopy and Peanuts", "Care Bears", "Strawberry Shortcake", "Squishmallows", "Bluey", "Pok\u00e9mon", "Super Mario", "Animal Crossing", "Harry Potter", "Wicked", "Star Wars", "Marvel"], def: [], none: 'none', help: 'Tick every character you love. It makes whole looks and lists around them. Leave them all unticked if you don\u2019t want character products.'},
   {id: 'uses', label: 'Moments in your life the looks are for', type: 'pick', options: ["work from home", "family", "holidays", "self care", "gifts", "date night", "pets", "kids", "hosting", "travel", "work", "school drop-off", "reading", "gaming", "gardening", "pool and beach", "concerts and events", "errands", "homeschooling", "home projects", "crafts and crochet", "weddings and showers", "church", "sports seasons"], def: ["work from home", "family", "holidays", "self care", "gifts", "date night", "pets", "kids", "hosting", "travel"]},
   {id: 'usesNo', label: 'Never make looks for', type: 'pick', options: ["work from home", "family", "holidays", "self care", "gifts", "date night", "pets", "kids", "hosting", "travel", "work", "school drop-off", "reading", "gaming", "gardening", "pool and beach", "concerts and events", "errands", "homeschooling", "home projects", "crafts and crochet", "weddings and showers", "church", "sports seasons"], def: [], none: 'none', help: 'Leave them all unticked if nothing is off limits.'},
   {id: 'seasonsNo', label: 'Holidays or seasons to skip', type: 'pick', options: ["New Year", "Valentine's Day", "St. Patrick's Day", "spring", "Easter", "Mother's Day", "Father's Day", "summer", "4th of July", "back to school", "fall", "Halloween", "Thanksgiving", "Christmas and winter", "birthdays"], def: [], none: 'none', help: 'Leave them all unticked to keep every holiday and season.'},
   {id: 'triggers', label: 'What makes you buy something', type: 'pick', options: ["solves a problem", "cute version of something boring", "giftable", "cozy", "trendy", "seasonal", "looks more expensive than it is", "everyday upgrade", "nostalgic", "keeps things organized", "practical", "girly novelty", "hard to find", "great price"], def: ["solves a problem", "cute version of something boring", "giftable", "cozy", "trendy", "seasonal", "looks more expensive than it is", "everyday upgrade", "nostalgic", "keeps things organized", "practical", "girly novelty", "hard to find"]},
   {id: 'novelty', label: 'Mix', type: 'radio', options: [['mostly novelty', 'Mostly fun and new'], ['balanced', 'Half fun, half practical'], ['mostly practical', 'Mostly practical']], def: 'mostly novelty'}
  ]
 },
 {
  id: 'pins', title: 'Pinterest', note: 'Make these boards in Pinterest first, or let setup make them for you.',
  fields: [
   {id: 'boards', label: 'Your Pinterest boards', type: 'pick', sep: '\n', options: ["Cute Amazon Finds for Women", "Women's Fashion and Outfit Ideas | Amazon Finds", "Cozy Home Decor Finds | Amazon Finds", "Cute Organization, Desk and Office Finds", "Beauty, Hair and Self Care Finds | Amazon Favorites", "Gift Ideas for Her, Kids and Family", "Seasonal and Holiday Amazon Finds", "Travel, Car and Everyday Essentials", "Kids, Family and Homeschool Finds", "Cozy Hobbies and Fun Finds"], def: ["Cute Amazon Finds for Women", "Women's Fashion and Outfit Ideas | Amazon Finds", "Cozy Home Decor Finds | Amazon Finds", "Cute Organization, Desk and Office Finds", "Beauty, Hair and Self Care Finds | Amazon Favorites", "Gift Ideas for Her, Kids and Family", "Seasonal and Holiday Amazon Finds", "Travel, Car and Everyday Essentials", "Kids, Family and Homeschool Finds", "Cozy Hobbies and Fun Finds"], help: 'Type any other board names in the box, separated with commas.'},
   {id: 'pinTypes', label: 'Which pins to make for every look', type: 'checks', options: ['Basic', 'Styled', 'Lifestyle', 'Roundup', 'Found It', 'Storefront promo'], def: ['Basic', 'Styled', 'Lifestyle', 'Roundup', 'Found It', 'Storefront promo'],
    help: 'Tick as many as you want. Basic is the clean flat lay, Styled the full scene, Lifestyle the products in use. NEW: Roundup puts the whole set in one pin with a big headline; Found It is one piece with handwritten \u201cI found this on Amazon\u201d words. Storefront promo is the Lifestyle photo linking to your storefront home page. Fewer pins means fewer photos and fewer credits.'},
   {id: 'slots', label: 'Most pins in one day', type: 'select', options: [['6', '6'], ['8', '8'], ['10', '10']], def: '8'}
  ]
 },
 {
  id: 'run', title: 'How it runs', note: 'Defaults are the ones I run on my own storefront.',
  fields: [
   {id: 'looks', label: 'Looks per night', type: 'radio', options: [['2', '2 looks (up to 12 pins, 2 carousels, and 2 blog posts if you have a blog)'], ['1', '1 look (uses half the credits and Claude usage)']], def: '2'},
   {id: 'time', label: 'Run time', type: 'select', options: [['01:05', '1:05 am'], ['02:05', '2:05 am'], ['03:05', '3:05 am'], ['23:05', '11:05 pm']], def: '01:05'},
   {id: 'igTime', label: 'Instagram posting time', type: 'select', show: 'ig=on', options: [['09:00', '9:00 am'], ['10:00', '10:00 am'], ['12:00', '12:00 pm'], ['19:00', '7:00 pm']], def: '10:00'},
   {id: 'order', label: 'Carousel photo order', type: 'radio', show: 'ig=on', options: [['Basic, Styled, Lifestyle', 'Basic, Styled, Lifestyle'], ['Lifestyle, Styled, Basic', 'Lifestyle first']], def: 'Basic, Styled, Lifestyle'},
   {id: 'credits', label: 'Most image credits per month', type: 'text', def: '350', show: 'photoMode=auto&platform=claude|photoMode=auto&imgWhere=higgsfield', help: 'When it reaches this, it stops making images and tells you. It never switches models to save credits on its own.'},
   {id: 'approve', label: 'Approvals', type: 'radio', show: 'pinMode=auto|igMode=auto', options: [['on', 'On: every pin and carousel waits in Metricool for my OK'], ['off', 'Off: fully automatic']], def: 'on',
    help: 'I recommend approvals on for your first few days. Turn them off when you trust it.'}
  ]
 }
];

// "Do it for me" requests: each one is a complete message the buyer sends to their AI with one click.
const who = (p) => (p === 'chatgpt' ? 'ChatGPT' : 'Claude');
const browserOf = (p) => (p === 'chatgpt' ? 'the browser tool connected to this chat' : 'the browser inside the Claude desktop app');
const NC = ' Change nothing.';
export const ASKS = {
 connectAll: (a, p) => {
  const m = modes(a);
  const tools = ['Google Drive', ...(m.metricool ? ['Metricool'] : []), ...(m.credits ? ['Higgsfield'] : []), ...(m.blogAuto ? ['GitHub'] : [])];
  const where = p === 'chatgpt' ? 'Tell me exactly where to click in ChatGPT (Settings, then Apps) to connect each one.' : 'Search the connector directory for each one that is not connected and show me its Connect button.';
  return `Help me connect the tools for my While-You-Sleep Storefront. I need: ${tools.join(', ')}. For each one, check whether it is already connected in ${who(p)}. ${where} After I connect each one, test it with one harmless read-only request and tell me in one line whether it worked. Do not create, change or delete anything.`;
 },
 okDrive: (a, p) => `Check that Google Drive is connected in ${who(p)}: list the names of my 3 most recent files (names only) and tell me in one line yes or no.${NC}`,
 okMetricool: () => `Check that Metricool is connected: list my brands exactly as Metricool names them, and for each brand which networks are connected (Pinterest, Instagram and so on). Tell me which brand is mine for pins.${NC}`,
 okHiggs: () => `Check that Higgsfield is connected: show my credit balance and tell me in one line whether I have credits.${NC}`,
 okGithub: () => `Check that GitHub is connected: list the names of the repositories you can see (names only) and tell me in one line yes or no.${NC}`,
 okAmazon: (a, p) => `Use ${browserOf(p)} to open https://www.amazon.com in a new tab. Tell me exactly what you see: did the page load normally, and am I signed in (my name shows near the top)? If Amazon says it does not support the browser, tell me those exact words. Never type a password: if I am signed out, stop and tell me to sign in myself.${NC}`,
 tag: (a, p) => `Use ${browserOf(p)} to open my Amazon Associates account (affiliate-program.amazon.com). Tell me my tracking IDs exactly as written (they end in -20), and which one my Amazon storefront uses. Never type a password: if I am signed out, tell me to sign in myself.${NC}`,
 storefront: (a, p) => `Use ${browserOf(p)} to find my Amazon storefront and tell me its exact web address (it looks like https://www.amazon.com/shop/name). Never type a password: if I am signed out, tell me to sign in myself.${NC}`,
 metricool: () => `Using the Metricool connection, list my brands exactly as Metricool names them. For each, say which networks are connected (Pinterest, Instagram and so on). Tell me which brand name to type into my setup.${NC}`,
 igAccount: () => `Using the Metricool connection, tell me which Instagram account is connected to my brand, written like @name.${NC}`,
 repo: () => `Using the GitHub connection, list the repositories you can see (names only) and tell me which one holds my website. For that one tell me: its exact name written owner/name; the branch my live site is published from (look for Cloudflare, Vercel, Netlify or GitHub Pages settings in its files); where it is hosted if you can tell; and the live website address if you can find it.${NC}`
};

// A 'pick' question: tick boxes plus an optional "anything else" box. The prompts get one plain answer.
export function pickValue(f, picked, more) {
 const sep = f.sep || ', ';
 const extra = String(more ?? '').split(f.sep ? /\n|,/ : /,/).map((x) => x.trim()).filter(Boolean);
 const all = [...picked, ...extra.filter((x) => !picked.includes(x))];
 return all.join(sep) || f.none || '';
}

export function defaults() {
 const a = {};
 for (const s of SECTIONS) for (const f of s.fields) if (f.type === 'pick') a[f.id] = pickValue(f, f.def, '');
 else if (f.type !== 'note') a[f.id] = Array.isArray(f.def) ? [...f.def] : (f.def ?? '');
 return a;
}

// "k=v|k2=v2" shows a field when any one of the conditions is true.
export function shown(cond, a) {
 if (!cond) return true;
 return cond.split('|').some((group) => group.split('&').every((c) => {const [k, val] = c.split('='); return a[k] === val;}));
}

const hostOf = (a) => (a.host && a.host !== 'unsure' && a.host !== 'other' ? a.host : '');
const v = (x, fb = '') => (Array.isArray(x) ? x.join(', ') : String(x ?? '').trim()) || fb;
const tzName = (tz) => (SECTIONS[0].fields.find((f) => f.id === 'tz').options.find((o) => o[0] === tz) || [tz, tz])[1];
const hm = (t) => {const [h, m] = t.split(':').map(Number); const ap = h >= 12 ? 'pm' : 'am'; return `${((h + 11) % 12) + 1}:${String(m).padStart(2, '0')} ${ap}`;};

// What each mode works out to for this buyer.
function modes(a) {
 const inf = a.amazon === 'influencer';
 const ig = a.ig === 'on';
 const m = {
  inf, ig,
  gpt: a.platform === 'chatgpt',
  srcHand: a.srcMode === 'hand',
  listAuto: inf && a.listMode !== 'hand' && a.platform !== 'chatgpt',
  listHand: inf && (a.listMode === 'hand' || a.platform === 'chatgpt'),
  photoAuto: a.photoMode !== 'hand',
  pinAuto: a.pinMode !== 'hand',
  igAuto: ig && a.igMode !== 'hand',
  igHand: ig && a.igMode === 'hand',
  blogAuto: a.blog === 'on',
  blogHand: a.blog === 'hand',
  blog: a.blog === 'on' || a.blog === 'hand'
 };
 m.imgGpt = m.gpt && m.photoAuto && a.imgWhere !== 'higgsfield';
 m.credits = m.photoAuto && !m.imgGpt;
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
 if (m.blogAuto) need.push(['repo', 'GitHub site'], ['branch', 'which version of your site goes live (the branch)'], ['host', 'where your site is hosted']);
 if (m.blog) need.push(['siteUrl', 'website address']);
 const out = need.filter(([k]) => !String(a[k] ?? '').trim()).map(([, n]) => n);
 const conn = [['okDrive', 'connect Google Drive', true],
  ['okMetricool', 'connect Metricool', m.metricool],
  ['okHiggs', 'connect Higgsfield', m.credits],
  ['okGithub', 'connect GitHub', m.blogAuto],
  ['okAmazon', 'sign in to Amazon in the AI\u2019s browser', !m.srcHand || m.listAuto]];
 for (const [k, n, on] of conn) if (on && a[k] !== 'yes') out.push(n);
 if (!a.blog) out.unshift('whether you have a blog');
 if (!m.inf && !m.blog) out.push('blog posts switched on, automatic or by hand (an account with links only needs them)');
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
${m.gpt ? `AI THAT RUNS IT: ChatGPT\n${m.photoAuto ? `PHOTOS MADE WITH: ${m.imgGpt ? 'ChatGPT\u2019s own image maker' : 'Higgsfield (connected)'}\n` : ''}` : ''}AMAZON: ${m.inf ? `Amazon storefront with Idea Lists. Storefront: ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}` : 'Amazon Associates links only (no Idea Lists). Pins link to my blog posts.'}
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
FAVORITE CHARACTERS: ${v(a.chars, 'none')}
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
BLOG: ${m.blogAuto ? `automatic, GitHub site ${v(a.repo, '[YOUR GITHUB SITE]')}${[v(a.branch) ? `publishes from the "${v(a.branch)}" branch` : '', hostOf(a) ? `hosted on ${hostOf(a)}` : ''].filter(Boolean).length ? ` (${[v(a.branch) ? `publishes from the "${v(a.branch)}" branch` : '', hostOf(a) ? `hosted on ${hostOf(a)}` : ''].filter(Boolean).join(', ')})` : ''}, live at ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')}` : m.blogHand ? `by hand, my site ${v(a.siteUrl, '[YOUR WEBSITE ADDRESS]')}` : 'off'}
${m.credits ? `MONTHLY IMAGE CREDIT LIMIT: ${v(a.credits, '350')}\n` : ''}${m.metricool ? `APPROVALS: ${m.approve ? 'on (every pin and carousel waits in Metricool for my OK)' : 'off (fully automatic)'}` : 'APPROVALS: not needed (I post by hand)'}`;
}

export function nightly(a) {
 const m = modes(a);
 const n = v(a.looks, '2');
 const br = m.gpt ? 'the browser tool connected to this chat, signed in to amazon.com' : 'the built-in browser in the Claude desktop app';
 const nb = m.imgGpt ? 'ChatGPT\u2019s image maker' : 'Nano Banana Pro at 2K';
 const sd = m.imgGpt ? 'ChatGPT\u2019s image maker' : 'Seedream 5.0 Flash at 2K';
 const face = a.persona === 'yes';
 const PT = Array.isArray(a.pinTypes) && a.pinTypes.length ? a.pinTypes : ['Basic', 'Styled', 'Lifestyle', 'Roundup', 'Found It', 'Storefront promo'];
 const doR = PT.includes('Roundup'), doF = PT.includes('Found It'), doAd = PT.includes('Storefront promo');
 const lookPins = ['Basic', 'Styled', 'Lifestyle', 'Roundup', 'Found It'].filter((x) => PT.includes(x));
 const photos = ['Basic', 'Styled', 'Lifestyle', ...(doR ? ['Roundup'] : []), ...(doF ? ['Found It'] : [])];
 const W = ['', 'one', 'two', 'three', 'four', 'five'];
 const andList = (xs) => xs.length < 2 ? xs.join('') : xs.slice(0, -1).join(', ') + ' and ' + xs[xs.length - 1];
 const lettered = andList(['the Basic', ...(doR ? ['the Roundup'] : []), ...(doF ? ['the Found It'] : [])]);
 const lifestyle = face
  ? `Lifestyle: ${nb}. Attach her reference photo FIRST (identity only) and the look's Product Sheet SECOND (product details only; render the products as real objects in the scene and never reproduce the sheet's layout or white background). The prompt opens with exactly: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair, skin or body anywhere in the prompt. Her face is fully visible, never hidden by a phone, hand or hair, and she is smiling or laughing toward the camera. Say exactly who is in the frame: only her, plus any pet from THINGS IN HER WORLD (exactly one of each), and no other people. She is wearing or using the real products from the Product Sheet and the room is one of HER WORLD places with real lived-in clutter. She is doing something real with the products in one of HER WORLD places (putting it up, wearing it out, using it), mid-moment, not posing. Use a clearly different camera angle, framing or viewpoint from the Styled photo: a new photograph, never her pasted into the Styled frame. No text on the photo.`
  : `Lifestyle: ${sd} with the look's Product Sheet attached (product details only; never reproduce the sheet's layout or white background). Hands and the products in use in one of HER WORLD places, mid-moment, from a clearly different camera angle or framing than the Styled photo. No face anywhere in the frame. No text on the photo.`;
 const dest = m.listAuto ? 'the themed Idea List the look\'s products are on'
  : m.listHand ? `my storefront (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')})`
  : 'the look\'s blog post';
 const site = v(a.siteUrl, '[YOUR WEBSITE ADDRESS]');
 let s = 0; const step = (t) => `STEP ${++s} · ${t}`;
 const parts = [];

 parts.push(`WHILE-YOU-SLEEP STOREFRONT: NIGHTLY RUN
Make ${n} complete look${n === '1' ? '' : 's'} tonight. Follow every step in order. My recipe is at the bottom and governs every choice.${m.gpt ? ' Use only the tools connected to this chat. Never say a step worked until you have read the result back.' : ''}${m.anyHand ? ' Steps marked BY HAND are mine: for those, write exactly what I need under "To Do By Hand" in the log, newest first, and never do them yourself.' : ''}

FIRST
1. Get today's date and time in ${a.tz}. Use that time zone for every date and time below.
2. Open my Google Doc "While-You-Sleep Log" with the Google Drive connector. Read every section: My Corrections, ${m.srcHand ? 'My Picks, ' : ''}Looks, ${m.inf ? 'Idea Lists, ' : ''}Products Used, Pins, Instagram, Blog, Credits, To Do By Hand, Runs. My Corrections override everything in this prompt except the NEVER list.
   Under Runs: if an earlier run is marked "started" but not "finished", it stopped partway. Finish that run's missing steps first, using what the log already records, and never redo a step the log shows as done. Then write "Run [today's date] started" under Runs before you do anything else.${m.imgGpt ? `
3. My photos are made with ChatGPT's own image maker, so there are no credits to check. Save every finished photo in my Google Drive folder "While-You-Sleep Storefront/Photos/<look name>" as you make it, named ${andList(photos)}. If the image maker stops or says I've hit my limit, make no more photos, write it in the log and tell me in one line.` : m.credits ? `
3. Higgsfield connector: read my credit balance. Add up this month's credits in the log. Tonight needs about ${n === '1' ? '5' : '10'} credits plus fixes. If tonight would go past ${v(a.credits, '350')} credits for the month, make no images, write it in the log and tell me in one line.` : `
3. Finish waiting looks first: for every look in the log marked "Waiting for photos", look in my Google Drive folder "While-You-Sleep Storefront/Photos/<look name>". If its ${andList(photos)} photos are all there, check them: right pieces in the right colors and the right size next to each other (hold each piece against its real size in PRODUCT NOTES; if one looks too big or too small, that photo fails), words spelled right and only on ${lettered}, ${face ? 'she matches her reference, ' : ''}nothing from PHOTOS I HATE (if one fails, tell me which and why, and leave that look waiting). Then do every step after PHOTOS for that look tonight and mark it done. Looks still missing photos stay waiting; don't remind me more than once a day.`}`);

 parts.push(`${step('PLAN')}
${m.srcHand ? `Build tonight's looks from the products under My Picks in the log that haven't been used yet. Group them into looks that make sense together. If there aren't enough picks for ${n} look${n === '1' ? '' : 's'}, make fewer and tell me in the report how many more picks you need.` : 'For each look choose a theme from my CATEGORIES and LOOKS ARE FOR that fits what people are shopping for in the next six weeks (season, holidays, occasions), skipping anything in my NEVER lists. Spread categories across the week, and when I have FAVORITE CHARACTERS, give them their own looks and themed lists regularly. Give every look its own color story drawn from SIGNATURE COLORS and SOMETIMES COLORS, different from the last look in the log (a signature color does not have to appear every time).'} Never repeat a look, whether it has been made yet or not: read the whole Looks section of the log, including looks marked Written or Waiting for photos, and never reuse or re-theme any of them. The moment you decide on a look, add it to the Looks section (name, theme, every piece) marked Written, before you do anything else with it. Every look has 5 or 6 pieces, never fewer than 5. It is an outfit, a themed collection or a set that goes together. Give it a name people would search for, like "The Pink Plaid Pumpkin Patch Outfit".${m.inf ? '\nIdea Lists are themed collections, not one list per look. Many looks come from one list. Use an existing themed list from the log when the theme fits and it holds fewer than 30 items; otherwise start a new themed list named for the theme (for example "Pink Halloween Decor"). Every piece in a look must be on that look’s Idea List: add any missing piece to the list before the look is written, and never build a look around a product that is not on its list.' : ''}`);

 parts.push(`${step(m.srcHand ? `CHECK MY PICKS (${br}, on amazon.com)` : `SOURCE (${br}, on amazon.com)`)}
Open one new tab. ${m.srcHand ? 'Open each of my picks and check it is in stock and record its ASIN, a short plain name, the exact color or variant and its real size in inches from the Product Dimensions or Size line on the listing (if it gives none, write \"size not listed\"). If one is out of stock, leave it out and say so in the report.' : 'Search Amazon for each piece. Open every candidate and check: in stock, at least 4 stars with real reviews, the exact color or variant fits my recipe. Anything sold on Amazon is allowed, including logos and licensed characters: when I have FAVORITE CHARACTERS, make some looks and themed lists around them. Judge each one on how stylish it looks, its appearance and its quality, and choose pieces that are trending and fit my CATEGORIES and LOOKS ARE FOR, not just any item that fits the category. Products that come in several colors or sizes are fine: pick the exact color that fits. Pick the piece and record its ASIN, a short plain name, the exact color or variant and its real size in inches from the Product Dimensions or Size line on the listing (if it gives none, write \"size not listed\"). Don\'t reuse a product used in the last 30 days (Products Used in the log).'} Never add anything to a cart, never buy, never type a password. If Amazon is signed out, stop and tell me in one line.`);

 if (m.listAuto) parts.push(`${step('IDEA LIST')}
In the same tab go to my storefront (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')}), Create content, Idea List. Add every piece of the look to tonight's themed list (create the list if it is new). Open the list's public page and confirm every piece shows. Record the list address. This is public: it is part of the run I set up and approved. Close the tab.${m.gpt ? ' If you can\'t find Create content, Idea List, or can\'t finish adding the products, stop trying: switch Idea Lists to BY HAND for tonight (write the list name and every product link under To Do By Hand) and tell me in one line.' : ''}`);
 else if (m.listHand) parts.push(`${step('IDEA LIST · BY HAND')}
Close the Amazon tab. Under To Do By Hand write: the themed list name, and every product's name with its link https://www.amazon.com/dp/ASIN. I add them to my Idea List myself.`);
 else parts.push(`${step('LINKS')}
For each piece, copy the link from the SiteStripe bar (Text) so it carries my tracking ID ${v(a.tag, '[YOUR TRACKING ID]')}. Record each link. Close the tab.`);

 const photoRules = `Basic: show only the listed pieces and their included accessories, nothing else in the frame and no extra background decor, on a surface that fills the whole background, with every piece fully inside the frame and breathing room around the outer edges. Clothing is a straight-overhead flat lay on a real surface (wood floor, painted table, rug), never laid on a bed and never on upholstered fabric. Anything that stands up is shown standing, at whatever camera angle that takes. Shoot from about 60 degrees above so only the surface shows, no wall or room: a real camera photo with contact shadows, never cutouts or stickers, the pieces close together in an upper half and a lower half, never in rows. A short headline naming the look (2 to 5 words) on two centred lines across the middle, laid over the photo where the pieces meet, each line 85% of the image width, readable on a phone: bold brush script with thick strokes like a fat marker, never thin or block capitals, no outline, with a soft white glow behind the letters. Pick the letter color for THIS photo from what sits behind the words, never one color for every look: light or pale surfaces with pink pieces get deep raspberry-magenta, lavender gets deep plum, mid or darker surfaces get saturated hot pink. Name the color in the prompt and say what it must stand out against. The lettering is a flat layer on top of the photo; every product under or near it stays sharp and recognisable.
Styled: completely styled in one of HER WORLD places, layered with props and texture that fit PHOTOS I LOVE. It is an entirely new photograph: keep the products' shapes, colors, materials and relative sizes, and do not copy the Basic's arrangement, camera framing or headline. No lettering anywhere on the photo.
Layer the Styled scene so nothing is bare: real props, textures and small details that fit PHOTOS I LOVE, colored from SIGNATURE COLORS and SOMETIMES COLORS, with the products still the clear stars.
Write every prompt in this order and keep each one under 2,500 characters: 1) "Highest quality finished photograph, photorealistic vertical 2:3, real-world photography" plus the real materials of these products (for example knit, ceramic, denim, glass) "never glossy or AI-perfect"; 2) the camera (angle, lens, how far back); 3) the attachment lines; 4) exactly which pieces appear, how many of each, and where each one sits; 5) the surface or room, named specifically with its real wear and texture (a different one every look); 6) the light (soft window daylight, lamp glow, golden hour); 7) the colors; 8) the headline (Basic only: two lines, white glow, a color picked for this photo, every product near it sharp); 9) the true sizes; 10) the EXACT PRODUCTS block, word for word, in EVERY photo prompt (Basic, Styled, Lifestyle, Roundup, Found It and the storefront promo; nightly or by hand): "EXACT PRODUCTS: every product looks EXACTLY like its photo on the attached product sheet: the same shape, colour, pattern, material, proportions, hardware, logos, tags and details. Never redesign, simplify, recolour or swap any product for a similar one." Product lines name each product only (for example "the striped-velvet jewelry box, open"), never a description that could compete with the sheet; 11) the NEVER list: no other logos, text, price or characters on anything that is not a product, no extra products, and anything in PHOTOS I HATE. Never tell the image tool to remove, blank out or hide anything that is part of a product. Say it in plain words, one clear scene, no piled-up adjectives.
Every photo: portrait 2:3. It must look REAL and lived-in, in bright natural light. Never rich-looking, staged, fake, plastic or CGI. The products must appear EXACTLY as they are on Amazon, including their own logos, tags, patches, stitching, hardware and printing. Nothing else in the frame is branded: no characters or logos on props, furniture or anything that is not a product. Follow PHOTOS I HATE. Don't use the same surface or room as the last look in the log.
Every Basic and Styled prompt opens with "Highest quality finished photograph" and says "Render the products as real three-dimensional objects photographed together in the new scene. Never reproduce any product photo's layout, white background, cutout edges or rectangular product photographs." The Basic prompt says "Only these [N] product types appear, in the quantities specified below." and states exactly how many individual pieces are visible and where each belongs; a set (for example a table setting) is written as complete place settings with their exact contents. Keep the real-world size relationships and never enlarge a small accessory to make it more prominent.
SCALE CHECK, written at the end of every photo prompt: "Keep every object at its true size next to the others: [each piece and its real size in inches]. Nothing is oversized." Never write "large" or "giant" for a piece unless its real size is large.`;

 if (m.photoAuto) {
  parts.push(`${step('PRODUCT NOTES')}
Look closely at each piece's Amazon photos in the exact color you chose and write one precise line per piece: what it is, exact color, material, pattern or print, shape and real size in inches next to the other pieces (for example: the lamp is 7.5 inches tall, the pillow is 18 inches square, so the pillow is more than twice the lamp's height). The words are for the size check only. The products must look exactly like the real listings, so every photo is made from the PRODUCT SHEET below, never from words alone.`);
  parts.push(`${step('PRODUCT SHEET')}
For each look, open every piece's Amazon page and take its main product photo in the exact color you chose. Put all of them on ONE plain white reference sheet, two photos across, each with breathing room, nothing else on the sheet (no labels and no prices; never cover or crop a product's own logo, tag or details). If any product photo shows a person's face, cover the face with a white box. Make the sheet with whatever image or code tool you have connected, save it as "Product Sheet" in my Google Drive folder "While-You-Sleep Storefront/Photos/<look name>", and open it to confirm every piece is on it and looks like the listing. If you have no tool that can build the sheet, write under To Do By Hand: the look name, each piece's main photo link, and "put these on one plain white page and save it as Product Sheet", and make no photos for that look tonight. This sheet is the product reference for all ${W[photos.length]} photos.`);
  parts.push(`${step(m.imgGpt ? `PHOTOS (ChatGPT\u2019s own image maker, ${W[photos.length]} per look, in this order)` : `PHOTOS (Higgsfield connector, 2K, ${W[photos.length]} per look, in this order)`)}
Basic: ${sd}, with the look's Product Sheet attached. The prompt says "Use the attached product sheet to identify each product's shape, colour, pattern and material" and lists every piece by name; the products must look exactly like the sheet.
Styled: ${sd} with the look's accepted Basic photo attached FIRST and the Product Sheet attached SECOND. The prompt says the Basic is for product continuity only and the sheet is for product details. A new scene, not the Basic re-shot.
${lifestyle}
${doR ? `Roundup: ${sd}, with the look's Product Sheet attached. A Pinterest roundup pin like "Spooky Cute HALLOWEEN DECOR You'll Love This Year": every piece of the look together in one fully styled scene in the lower two-thirds, and a headline across the top third in three centred lines: line 1 a short look name in a big bold rounded brush script, in a colour picked for this look, with a thick white outline; line 2 a short category in bold condensed capitals, near-black with a thin white outline (for example TABLE DECOR or FALL OUTFIT); line 3 a short white script line with a soft shadow followed by two emoji (for example You'll Love This Year). Every word spelled exactly as written.
` : ''}${doF ? `Found It: ${sd}, with the look's Product Sheet attached. A Pinterest pin like "I found this lamp on Amazon": the look's single most interesting piece ALONE (none of the other pieces), in one of HER WORLD places, real, lived-in and a little cluttered, like an everyday phone photo rather than a styled ad. Lettering in thin, casual white handwriting, like words added in a phone app, no outline and no box: across the top "I found this [short name of the piece] on", and lower down a hand-drawn white arrow pointing to the piece beside the word "Amazon" and a small white hand-drawn heart. Every word spelled exactly as written.
` : ''}Make each photo only after the one before it passes its check.
${photoRules}
CHECK each photo before using it: right pieces in the right colors and the right size next to each other (hold each piece against its real size in PRODUCT NOTES; if one looks too big or too small, that photo fails), words spelled right and only on ${lettered}, ${face ? 'she matches her reference, ' : ''}nothing from PHOTOS I HATE. Re-run a failed photo once with the fix written into the prompt. If it still fails, skip that look, log why, and move on.`);
 } else {
  parts.push(`${step('PHOTOS · BY HAND')}
Under To Do By Hand write, for each look: its name, the product photo links (each piece's main Amazon photo in the exact color) with the instruction to put them on one plain white page, two across, face covered if a photo shows a person, and save it as the Product Sheet, and ${W[photos.length]} complete, separate, ready-to-paste prompts, one each for ${andList(photos)}. Every prompt stands on its own with nothing to fill in. Every one of them carries the EXACT PRODUCTS block word for word. Basic: for Seedream on the Higgsfield website, with "attach your Product Sheet" at the top, listing every piece by name so the products look exactly like the sheet. Styled: for Seedream, with "attach your finished Basic photo first, then your Product Sheet" at the top. Make them in order: ${photos.join(', then ')}.${doR ? ' Roundup: for Seedream, with "attach your Product Sheet" at the top: every piece of the look together in one fully styled scene in the lower two-thirds, with a three-line headline across the top third (a big bold brush-script look name with a white outline, a bold condensed capitals category line, a white script line with two emoji), spelled exactly.' : ''}${doF ? ' Found It: for Seedream, with "attach your Product Sheet" at the top: the look\'s single most interesting piece alone in one of HER WORLD places, real and lived-in like an everyday phone photo, with thin white handwritten lettering "I found this [piece] on" across the top and a hand-drawn white arrow pointing to it beside "Amazon" and a small white heart, spelled exactly.' : ''} Lifestyle: ${face ? `for Nano Banana Pro, with "attach her reference photo first, then your Product Sheet" at the top, from a different camera angle than Styled, and the prompt itself opening with exactly: "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Never describe her face, hair, skin or body. Her face is visible, doing something real with the products in one of HER WORLD places, mid-moment.` : 'for Seedream, with "attach your Product Sheet" at the top, hands and the products in use in one of HER WORLD places from a different angle than Styled, no face.'}
Write these rules into the prompts themselves: ${photoRules.replace(/\n/g, ' ')}
Tell me to save the ${W[photos.length]} finished photos as ${andList(photos)} in "While-You-Sleep Storefront/Photos/<look name>" in my Google Drive. Mark the look "Waiting for photos" in the log and stop work on that look tonight. The steps below run for it on the night the photos are there.`);
 }

 if (m.blogAuto) parts.push(`${step(`BLOG POST (GitHub connector, site ${v(a.repo, '[YOUR GITHUB SITE]')})`)}
Find the newest blog post in the site and copy its format exactly. Add a post for the look: the look's name as the title, a 60 to 100 word intro in MY VOICE (first person, one real specific moment), the three photos in the order Basic, Styled, Lifestyle with plain alt text, every piece with its Amazon link in the form https://www.amazon.com/dp/ASIN?tag=${v(a.tag, '[YOUR TRACKING ID]')}${m.inf ? ' and a button to the Idea List' : ''}, and this note at the end: "As an Amazon Associate I earn from qualifying purchases. Photos are AI-generated styling ideas; check each listing for the exact item." ${m.imgGpt ? 'The photos are files in my Drive folder: add them to the site\'s images folder in the same change and use those paths. ' : ''}Publish it${v(a.branch) ? ` on the "${v(a.branch)}" branch` : ''}, wait for the site to update${hostOf(a) ? ` (${hostOf(a)} rebuilds it by itself)` : ''}, open the live page at ${site} and confirm all three photos and every link load. Record the address.`);
 else if (m.blogHand) parts.push(`${step('BLOG POST · BY HAND')}
Under To Do By Hand write the full post, ready to paste: the look's name as the title, a 60 to 100 word intro in MY VOICE (first person, one real specific moment), where each of the three photos goes (Basic, Styled, Lifestyle) with plain alt text, every piece with its Amazon link in the form https://www.amazon.com/dp/ASIN?tag=${v(a.tag, '[YOUR TRACKING ID]')}${m.inf ? ' and the Idea List link' : ''}, and this note at the end: "As an Amazon Associate I earn from qualifying purchases. Photos are AI-generated styling ideas; check each listing for the exact item." Ask me to paste the post's address under the look in the log once it's live on ${site}.${!m.inf ? ' The pins for this look wait until that address is in the log.' : ''}`);

 const pinText = `${W[lookPins.length].replace(/^./, (c) => c.toUpperCase())} pin${lookPins.length === 1 ? '' : 's'} per look, one per photo: ${andList(lookPins)}. Each goes to the most specific board in my PINTEREST BOARDS. Pin title: the search phrase first, under 100 characters. Description: two or three natural sentences with the words people search for, no hashtags${m.inf ? ', ending with exactly: #ad As an Amazon Associate I earn from qualifying purchases. (Amazon requires a disclosure by every affiliate link. Use this exact wording.)' : '.'} Link: ${dest}. Alt text: a plain description of the photo.${doR ? ' The Roundup pin\'s title is its three headline lines as one phrase.' : ''}${doF ? ' The Found It pin\'s title is "I Found This Exact [piece] On Amazon" followed by 😭.' : ''} A look's pins go on separate days that aren't next to each other, different looks are mixed together, and no day gets more than ${v(a.slots, '8')} pins.${doAd ? ` Plus one storefront promo pin per look: the look's Lifestyle photo, titled with the look's name and what my storefront is for, linking to ${m.inf ? `my storefront home page (${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')})` : 'my blog home page'} instead of the list, on a day with none of that look's other pins. Its description follows the same rules${m.inf ? ', disclosure line included' : ''}.` : ''}`;
 if (m.pinAuto) parts.push(`${step(`PINS (Metricool connector, brand ${v(a.metricool, '[YOUR METRICOOL BRAND]')})`)}
${pinText} Read Metricool's schedule first and use open days. If Metricool already holds a pin with the same photo and link (from a run that stopped partway), don't make it again. Set the date, time and time zone (${a.tz}) on every post.${m.gpt ? ' Write every date with its offset (for example 2026-10-20T12:00:00-04:00): Metricool rejects a date without one.' : ''}${m.imgGpt ? ' The photos are files in my Drive folder: give Metricool each photo\'s link. If Metricool won\'t accept a Drive link, don\'t invent another route: put that look\'s pins under To Do By Hand with the photos and say why.' : ''} ${m.approve ? 'APPROVALS ARE ON: send every pin to Metricool for review instead of scheduling it.' : 'Schedule them.'} Read each one back from Metricool and confirm it is there with the right photo, board and link.`);
 else parts.push(`${step('PINS · BY HAND')}
${pinText} Under To Do By Hand write each pin: which photo, board, title, description, link, alt text and the date to schedule it. I schedule them in Pinterest's own scheduler.`);

 if (m.igAuto) parts.push(`${step(`INSTAGRAM (Metricool connector, ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')})`)}
One carousel per look, two carousels a day: on the next day that has fewer than two carousels, the first at ${hm(a.igTime)} and the second about five hours later, never two at the same time: the three photos in the order ${a.order}. Caption in MY VOICE, three to five short lines, ending with "Shop it: link in bio", three to five hashtags, and then exactly: #ad As an Amazon Associate I earn from qualifying purchases. No links in the caption.${m.imgGpt ? ' The photos are files in my Drive folder: give Metricool each photo\'s link, and if it won\'t accept one, put the carousel under To Do By Hand and say why.' : ''} If Metricool already holds this look's carousel, don't make it again. ${m.approve ? 'APPROVALS ARE ON: send it for review instead of scheduling it.' : 'Schedule it.'} Read it back from Metricool.`);
 else if (m.igHand) parts.push(`${step('INSTAGRAM · BY HAND')}
Under To Do By Hand write one carousel per look for ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')}: the photo order (${a.order}), the day to post it (two carousels a day, the first at ${hm(a.igTime)} and the second about five hours later), and the caption in MY VOICE, three to five short lines, ending with "Shop it: link in bio", three to five hashtags, and then exactly: #ad As an Amazon Associate I earn from qualifying purchases. No links in the caption.`);

 const pinsWord = `${Number(n) * (lookPins.length + (doAd ? 1 : 0))} pins`;
 parts.push(`LAST · LOG
Add to the log: each look's name and theme, ${m.inf ? 'Idea List, ' : ''}every ASIN, ${m.credits ? 'the photo links, credits used tonight, ' : m.photoAuto ? 'the photo links, ' : ''}${m.blog ? 'the blog address (or that it is waiting for me), ' : ''}every pin and carousel with its date, what's waiting under To Do By Hand, and anything you skipped and why. Last, write "Run [today's date] finished" under Runs. Read the log back to confirm it saved.

REPORT
One line if everything worked: "Tonight: ${n} look${n === '1' ? '' : 's'}${m.photoAuto ? `, ${pinsWord}${m.pinAuto ? (m.approve ? ' waiting for your OK in Metricool' : ' scheduled') : ' ready for you'}` : ', photo prompts ready for you'}.${m.anyHand ? ' Your by-hand list is in the log.' : ''}" If something failed, say what in plain words and the exact fix.

NEVER: type a password. Buy or add anything to a cart. Post to any account that isn't in my recipe. Do a step marked BY HAND. ${m.credits ? 'Go past my monthly credit limit. Switch image models without telling me. ' : ''}Make any claim about how much money anyone will make.

${recipe(a)}`);

 return parts.join('\n\n');
}

export function setup(a) {
 const m = modes(a);
 const L = 'abcdefgh'.split(''); let i = 0; const c = () => L[i++];
 const conn = [];
 if (m.credits) conn.push(`${c()}. Higgsfield: read my credit balance.`);
 else if (m.imgGpt) conn.push(`${c()}. ChatGPT image maker: make one small test image (a plain mug on a table) to confirm it works in this chat, and tell me if it says I've hit a limit.`);
 if (m.metricool) conn.push(`${c()}. Metricool: find my brand "${v(a.metricool, '[YOUR METRICOOL BRAND]')}". ${m.pinAuto ? 'Confirm Pinterest is connected and list my Pinterest boards. ' : ''}${m.igAuto ? `Confirm Instagram ${v(a.igAccount, '[YOUR INSTAGRAM ACCOUNT]')} is connected.` : ''}`);
 conn.push(`${c()}. Google Drive: make a folder "While-You-Sleep Storefront"${m.photoAuto && !m.imgGpt ? '' : ' with a folder "Photos" inside it'}, and inside it a Google Doc "While-You-Sleep Log" with these headings: My Corrections, ${m.srcHand ? 'My Picks, ' : ''}Looks, ${m.inf ? 'Idea Lists, ' : ''}Products Used, Pins, Instagram, Blog, Credits, To Do By Hand, Runs. Put my recipe (below) at the top. Read it back.`);
 if (m.blogAuto) conn.push(`${c()}. GitHub: open ${v(a.repo, '[YOUR GITHUB SITE]')}. Find where the blog posts live and how a post is built.${v(a.branch) ? ` Confirm the "${v(a.branch)}" branch exists.` : ''} Tell me in two lines.`);
 conn.push(`${c()}. ${m.gpt ? 'Browser: use the browser tool connected to this chat and tell me exactly which one it is. Open amazon.com in a new tab.' : 'Built-in browser (the browser inside the Claude desktop app): open amazon.com in a new tab.'} ${m.listAuto ? `Open my storefront ${v(a.storefront, '[YOUR STOREFRONT ADDRESS]')} and confirm I'm signed in (you can see "Create content").${m.gpt ? ' Then open Create content, Idea List once to check it is there. Create nothing yet.' : ''}` : 'Confirm I\'m signed in (my name shows at the top).'} ${m.gpt ? 'If I\'m signed out, tell me exactly how to sign in to my own Amazon account in that tool and wait. Never use anyone else\'s saved sign-in.' : 'If I\'m signed out, tell me and wait while I sign in.'} Close the tab.`);

 const boards = m.pinAuto
  ? `Compare my PINTEREST BOARDS with the boards Metricool lists. If any are missing, list them and ask me whether to create them in Pinterest in ${m.gpt ? 'the connected browser' : 'the built-in browser'}. Boards are public, so create them only after I say yes. Then write every board's name in the log.`
  : `List my PINTEREST BOARDS and ask me whether they all exist in Pinterest yet. If any are missing, tell me to create them in Pinterest (or offer to create them in ${m.gpt ? 'the connected browser' : 'the built-in browser'}, only after I say yes, because boards are public). Write every board's name in the log.`;

 const ref = a.persona === 'yes'
  ? (m.imgGpt
   ? `HER REFERENCE\nRecord her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) in the log. Make one test photo of her with ChatGPT\u2019s image maker, reference attached, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Show it to me and ask if she looks right.`
   : m.photoAuto
   ? `HER REFERENCE\nBring her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) into Higgsfield and record its media ID in the log. Make one test photo of her with Nano Banana Pro at 2K, reference attached, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference." Show it to me and ask if she looks right.`
   : `HER REFERENCE\nRecord her reference photo (${v(a.personaRef, '[HER REFERENCE PHOTO LINK]')}) in the log. Write me one test prompt for Nano Banana Pro, opening with exactly "Photograph of this exact woman from the attached reference sheet. Identity is taken only from the reference.", for me to try on the Higgsfield website with her reference attached.`)
  : 'NO FACE\nMy lifestyle photos have no face: hands and products in use only. Write that at the top of My Corrections.';

 const picks = m.srcHand ? `\n\nSTEP 4 · MY PICKS\nAsk me for my first product picks (Amazon links or ASINs, at least ${Number(v(a.looks, '2')) * 5}) and write them under My Picks in the log. Tell me I can add more there any time.` : '';
 const firstN = m.srcHand ? 5 : 4;
 return `WHILE-YOU-SLEEP STOREFRONT: SETUP
You are setting up my While-You-Sleep Storefront.${m.gpt ? ' I am using ChatGPT: use only the tools connected to this chat.' : ''} Do these steps in order. After each step tell me in one line whether it passed. If one fails, tell me the exact fix in plain words and wait for me before going on. Never type a password.

STEP 1 · CONNECTIONS
${conn.join('\n')}

STEP 2 · BOARDS
${boards}

STEP 3 · ${ref}${picks}

STEP ${firstN} · FIRST LOOK, WITH ME WATCHING
Make one look using the NIGHTLY RUN below exactly${m.metricool ? ', with one change: approvals are ON for this look whatever my recipe says, so every pin and carousel goes to Metricool for review' : ''}. Then show me ${m.photoAuto ? 'all the photos' : 'the photo prompts'}, ${m.inf ? 'the Idea List, ' : ''}${m.blog ? 'the blog post, ' : ''}the pin text${m.ig ? ' and the caption' : ''}${m.anyHand ? ' and my To Do By Hand list' : ''}, and ask what I'd change. Write every change I give you under My Corrections in the log, in my words. Redo anything I ask, then check it again.

STEP ${firstN + 1} · TURN IT ON
When I say it's right, create a scheduled task named "While-You-Sleep nightly run" that runs every day at ${hm(a.time)} ${tzName(a.tz)} with the full NIGHTLY RUN below as its prompt.${m.gpt ? ' ChatGPT can\'t create a task that starts paused, so create it only now.' : ''} Read the task back and tell me when it runs next. If you can't create scheduled tasks here, tell me in one line.

=== NIGHTLY RUN ===
${nightly(a)}`;
}
