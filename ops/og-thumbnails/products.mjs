// One link thumbnail per product page. This is the only file to edit.
//
// Key = the page's URL path. Headline words wrapped in *stars* print in hot pink.
// Keep headlines short: they have to read inside a 200 px square in a Facebook comment.
// `photo` is a key from PHOTOS in render.mjs. `mock` is the drawn preview on the right
// (see MOCKS in render.mjs for the kinds and their fields). `sticker` is the round badge.
//
// A product page with no entry here still gets a thumbnail: render.mjs builds one from the
// page's own name, price and description, and prints a line telling you to hand-write it.

export const PRODUCTS = {
  // ---------- free resources ----------
  "/resources/find-your-door": {
    kicker: "Free quiz", headline: "Which side hustle *fits you?*",
    sub: "11 quick questions. One clear place to start.",
    photo: "kitchen", sticker: "11 Qs",
    mock: { kind: "quiz", step: "Question 3 of 11", q: "What do you want this to do for you?",
      opts: ["Cover a few bills", "Replace my paycheck", "Run while I sleep"], pick: 2 },
  },
  "/resources/affiliate-starter-kit": {
    kicker: "Free kit", headline: "Get paid for links you *already share*",
    sub: "How affiliate links work, and what's worth recommending.",
    photo: "gifts", sticker: "Free",
    mock: { kind: "doc", title: "The honest filter", items: ["I use it myself", "It solves a real problem", "The price is fair", "I'd tell a friend"] },
  },
  "/resources/ai-starter-kit": {
    kicker: "Free kit", headline: "The *4 jobs* to hand AI first",
    sub: "Plus the brief that gets usable answers, and a prompt to run today.",
    photo: "laptopPink", sticker: "Free",
    mock: { kind: "chat", you: "Write 5 Pinterest titles for my freebie.", ai: "Here are five, each under 100 characters and led by your keyword…" },
  },
  "/resources/automation-kit": {
    kicker: "Free kit", headline: "Automate these *3 things first*",
    sub: "In the right order, so the business runs without you.",
    photo: "phoneHands", sticker: "Free",
    mock: { kind: "flow", steps: ["Someone signs up", "Freebie sends itself", "Welcome emails go out", "Offer arrives on day 3"] },
  },
  "/resources/blogging-kit": {
    kicker: "Free kit", headline: "Write the post that gets *found for years*",
    sub: "One article, turned into a month of pins, emails and posts.",
    photo: "hoodie", sticker: "Free",
    mock: { kind: "browser", url: "yourblog.com", view: "article", title: "How to start a blog that still gets read in 2029" },
  },
  "/resources/branding-kit": {
    kicker: "Free kit", headline: "Your brand in *one sentence*",
    sub: "The promise that makes every colour and font choice easy.",
    photo: "bed", sticker: "Free",
    mock: { kind: "brand", promise: "I help tired moms start a business they can run from the couch." },
  },
  "/resources/business-systems-kit": {
    kicker: "Free kit", headline: "Turn your to-do list into *a business*",
    sub: "The few systems that make the work repeatable.",
    photo: "pasture", sticker: "Free",
    mock: { kind: "doc", title: "My weekly systems", items: ["Content: batch on Monday", "Email: one letter a week", "Sales: check on Friday", "Admin: 20 minutes, done"] },
  },
  "/resources/content-creation-kit": {
    kicker: "Free kit", headline: "One idea = *a week of content*",
    sub: "Create once, show up everywhere.",
    photo: "sofa", sticker: "Free",
    mock: { kind: "week", days: ["Blog post", "3 pins", "Reel", "Email", "Carousel"] },
  },
  "/resources/digital-products-kit": {
    kicker: "Free kit", headline: "Your first digital product in *one week*",
    sub: "The four product types worth starting with.",
    photo: "bed", sticker: "Free",
    mock: { kind: "doc", title: "Pick one to start", items: ["Printable planner", "Template pack", "Short guide", "Prompt pack"], numbered: true },
  },
  "/resources/email-starter-kit": {
    kicker: "Free kit", headline: "Start your email list *from zero*",
    sub: "And the welcome emails that turn signups into sales.",
    photo: "kitchen", sticker: "Free",
    mock: { kind: "inbox", rows: [["Welcome!", "Here's your freebie"], ["Day 2", "The mistake I made first"], ["Day 4", "What I'd do in your shoes"], ["Day 6", "Ready for the next step?"]] },
  },
  "/resources/faceless-income-blueprint": {
    kicker: "Free guide", headline: "The whole faceless business on *one page*",
    sub: "See it all, then find exactly where you're stuck.",
    photo: "laptopPink", sticker: "No face",
    mock: { kind: "flow", steps: ["Get found", "Grow your list", "Make the offer", "Deliver on autopilot"] },
  },
  "/resources/mindset-kit": {
    kicker: "Free kit", headline: "Stop waiting to *feel ready*",
    sub: "The shift from creator to CEO, in plain steps.",
    photo: "porch", sticker: "Free",
    mock: { kind: "compare", left: ["Waits to feel ready", "Asks for permission", "Busy all day"], right: ["Acts first", "Decides", "Builds systems"], lh: "Creator", rh: "CEO" },
  },
  "/resources/one-sentence-offer": {
    kicker: "Free tool", headline: "Say what you sell in *one sentence*",
    sub: "Type it in. Watch four checks run live. No email needed.",
    photo: "hoodie", sticker: "No email",
    mock: { kind: "sentence", text: "A 30-day meal planner that gets dinner on the table in 20 minutes.", checks: ["Who it's for", "What it does", "How fast", "Under 25 words"] },
  },
  "/resources/passive-income-kit": {
    kicker: "Free kit", headline: "Build it once. *Get paid on repeat.*",
    sub: "What really counts as passive, and the first stream to build.",
    photo: "pasture", sticker: "Free",
    mock: { kind: "sales", title: "While you were away", rows: ["Sold: Starter Planner", "Sold: Starter Planner", "Sold: Prompt Pack"] },
  },
  "/resources/pinterest-keyword-planner": {
    kicker: "Free planner", headline: "Find the words *Pinterest wants*",
    sub: "From seed words to 30 to 50 checked keywords.",
    photo: "pinkSweater", sticker: "Free",
    mock: { kind: "search", query: "easy dinner", results: ["easy dinner recipes", "easy dinner ideas for family", "easy dinner for two", "easy dinner meal prep"] },
  },
  "/resources/pinterest-traffic-kit": {
    kicker: "Free kit", headline: "Pins that actually *get clicked*",
    sub: "The five parts of a pin people tap on.",
    photo: "pinkSweater", sticker: "Free",
    mock: { kind: "pins", pins: ["5 freezer meals", "Budget planner", "Morning routine", "Easy side hustle"] },
  },
  "/resources/shopify-starter-kit": {
    kicker: "Free kit", headline: "Open your Shopify store *this weekend*",
    sub: "30 niches, the setup checklist, the app guide and 20 AI prompts.",
    photo: "kitchen", sticker: "4 files",
    mock: { kind: "browser", url: "yourshop.com", view: "shop" },
  },
  "/resources/starter-map": {
    kicker: "Free guide", headline: "$10 a day, *mapped out*",
    sub: "Ad, page, list, offer. Fill in four boxes before you spend.",
    photo: "phoneHands", sticker: "$10/day",
    mock: { kind: "flow", steps: ["Ad", "Landing page", "Email list", "Offer"] },
  },
  "/resources/weekend-build-challenge": {
    kicker: "Free 5-day challenge", headline: "Build a small business in *5 days*",
    sub: "One email a day. About 30 minutes each.",
    photo: "sofa", sticker: "30 min",
    mock: { kind: "days", days: ["Pick a model", "Write the offer", "Make the product", "Build the funnel", "Get found"] },
  },
  "/resources": {
    kicker: "Free resources", headline: "A free kit for *every step*",
    sub: "Guides, checklists and starter tools. Take what you need.",
    photo: "porch", sticker: "Free",
    mock: { kind: "stack", covers: ["Pinterest Traffic Kit", "Email Starter Kit", "AI Starter Kit"] },
  },

  // ---------- shop ----------
  "/shop": {
    kicker: "The shop", headline: "Everything to *start selling online*",
    sub: "Guides, prompt packs, memberships and done-for-you services.",
    photo: "laptopPink", sticker: "From $2",
    mock: { kind: "browser", url: "thedigitalincomeedit.com/shop", view: "shop" },
  },
  "/shop/weekend-ecosystem": {
    kicker: "$97 or 3 × $33.33", headline: "Your website, blog and list in *one weekend*",
    sub: "Built with Claude from content you already wrote.",
    photo: "sofa", sticker: "No code",
    mock: { kind: "browser", url: "yourname.com", view: "site" },
  },
  "/weekend-ecosystem/preview": {
    kicker: "Free preview", headline: "Look inside *before you buy*",
    sub: "A real module, the prompts and real output. No email.",
    photo: "loft", sticker: "No email",
    mock: { kind: "doc", title: "The Weekend Ecosystem™", items: ["01 The Website", "02 The Blog", "03 The Capture System", "04 Traffic"], plain: true },
  },
  "/shop/pretty-and-paid-plr-vault": {
    kicker: "$11 a month", headline: "Products you can *sell as your own*",
    sub: "Done-for-you digital products, new every month.",
    photo: "bed", sticker: "20 new / mo",
    mock: { kind: "tiles", tiles: ["printables-planners", "canva-templates", "pinterest-templates", "guides-ebooks"] },
  },
  "/vault/freebie-in-an-afternoon": {
    kicker: "$7 guide", headline: "Your first freebie in *one afternoon*",
    sub: "The lead magnet and the paid offer behind it, on Beacons.",
    photo: "hoodie", sticker: "$7",
    mock: { kind: "flow", steps: ["Free download", "Thank-you page", "$27 offer", "Sells on autopilot"] },
  },

  // ---------- /go product pages ----------
  "/go/550-brilliant-chatgpt-prompts-for-your-business": {
    kicker: "$2 prompt pack", headline: "*550 prompts* for your business",
    sub: "Never stare at a blank ChatGPT box again.",
    photo: "laptopPink", sticker: "$2",
    mock: { kind: "prompts", cards: ["Write a product description for…", "Turn this blog post into 5 pins…", "Draft a welcome email for…"] },
  },
  "/go/ai-influencer-brand-bundle": {
    kicker: "$147 · AI influencer", headline: "Your AI influencer, *fully branded*",
    sub: "The persona plus every brand asset around her.",
    photo: "bed", sticker: "$147",
    mock: { kind: "tiles", tiles: ["ai-influencer-prompts", "stock-imagery", "announcement-posts", "engagement-stories"] },
  },
  "/go/ai-influencer-content-drop": {
    kicker: "$297 · AI influencer", headline: "Ready-to-post content for *your AI persona*",
    sub: "Delivered, for a persona you've already built.",
    photo: "sofa", sticker: "$297",
    mock: { kind: "tiles", tiles: ["stock-imagery", "faceless-reels", "carousel-templates", "announcement-posts"] },
  },
  "/go/ai-influencer-flash-sale": {
    kicker: "$50 flash sale", headline: "Start your AI influencer *for $50*",
    sub: "The entry point into the full build.",
    photo: "pinkSweater", sticker: "$50",
    mock: { kind: "tiles", tiles: ["ai-influencer-prompts", "stock-imagery", "faceless-reels", "ai-prompt-packs"] },
  },
  "/go/ai-influencer-starter-twin": {
    kicker: "$97 · AI influencer", headline: "Your AI persona, *same face* every time",
    sub: "Generated to stay consistent in every image.",
    photo: "laptopPink", sticker: "$97",
    mock: { kind: "tiles", tiles: ["ai-influencer-prompts", "stock-imagery", "ai-prompt-packs", "announcement-posts"] },
  },
  "/go/ai-subs-method": {
    kicker: "Recommended · $147", headline: "Grow a faceless *AI subscription* channel",
    sub: "A step-by-step system to grow it and earn from it.",
    photo: "phoneHands", sticker: "$147",
    mock: { kind: "chart", title: "Subscribers" },
  },
  "/go/bonus-bundle-with-resell-rights": {
    kicker: "$27 bundle", headline: "Ready-made products you can *resell*",
    sub: "Rebrand them and sell them as your own.",
    photo: "gifts", sticker: "$27",
    mock: { kind: "tiles", tiles: ["guides-ebooks", "printables-planners", "coloring-pages", "canva-templates"] },
  },
  "/go/claude-studio-kit": {
    kicker: "Recommended · $57", headline: "Run Claude like *a studio*",
    sub: "A working setup, not just a chat box.",
    photo: "laptopPink", sticker: "$57",
    mock: { kind: "chat", you: "Draft this week's blog post from my notes.", ai: "Done. Here's the draft, three pin titles and the email to send it…" },
  },
  "/go/dfy-instagram-audit-custom-viral-content-calendar": {
    kicker: "Done for you · $350", headline: "Instagram audit + *a calendar made for you*",
    sub: "Built for your account, not a template.",
    photo: "pinkSweater", sticker: "DFY",
    mock: { kind: "calendar" },
  },
  "/go/dfy-instagram-audit-growth-optimization": {
    kicker: "Done for you · $197", headline: "What's *holding back* your Instagram?",
    sub: "A full read of your account and the exact changes to make.",
    photo: "phoneHands", sticker: "DFY",
    mock: { kind: "audit", items: ["Bio", "Highlights", "Reels hooks", "Posting rhythm", "Call to action"] },
  },
  "/go/earn-with-skool-scc": {
    kicker: "Recommended · $97", headline: "Build and earn from *a Skool community*",
    sub: "How to set it up and make it pay.",
    photo: "porch", sticker: "$97",
    mock: { kind: "community" },
  },
  "/go/first-freebie": {
    kicker: "$7 guide", headline: "Your first freebie in *one afternoon*",
    sub: "The lead magnet and the paid offer behind it.",
    photo: "hoodie", sticker: "$7",
    mock: { kind: "flow", steps: ["Free download", "Thank-you page", "$27 offer", "Sells on autopilot"] },
  },
  "/go/free-guide-one-done-money-stream": {
    kicker: "Free guide", headline: "One product. *Paid on repeat.*",
    sub: "The short version of the one-and-done money stream.",
    photo: "pasture", sticker: "Free",
    mock: { kind: "sales", title: "One product, on repeat", rows: ["Sold: your one product", "Sold: your one product", "Sold: your one product"] },
  },
  "/go/how-i-batch-schedule-a-month-of-pinterest-in-one-3-hour-bloc": {
    kicker: "$9 guide", headline: "A month of pins in *3 hours*",
    sub: "The exact order I work in, start to finish.",
    photo: "pinkSweater", sticker: "$9",
    mock: { kind: "calendar", pins: true },
  },
  "/go/leni-loves": {
    kicker: "Recommended · $27", headline: "Pretty templates for *your brand*",
    sub: "Aesthetic templates and resources for your content.",
    photo: "bed", sticker: "$27",
    mock: { kind: "tiles", tiles: ["canva-templates", "carousel-templates", "engagement-stories", "pinterest-templates"] },
  },
  "/go/navia-ai-studio": {
    kicker: "Recommended · $197", headline: "Your own *AI production studio*",
    sub: "Set up once, make content on demand.",
    photo: "loft", sticker: "$197",
    mock: { kind: "tiles", tiles: ["stock-imagery", "faceless-reels", "ai-influencer-prompts", "ai-prompt-packs"] },
  },
  "/go/one-and-done-money-stream": {
    kicker: "$27 guide", headline: "Make it once. *Let it earn.*",
    sub: "Set up one reliable digital income stream.",
    photo: "pasture", sticker: "$27",
    mock: { kind: "sales", title: "While you were away", rows: ["Sold: your one product", "Sold: your one product", "Sold: your one product"] },
  },
  "/go/pretty-and-paid-plr-vault": {
    kicker: "$11 a month", headline: "Products you can *sell as your own*",
    sub: "Twenty new done-for-you products every month.",
    photo: "bed", sticker: "20 new / mo",
    mock: { kind: "tiles", tiles: ["printables-planners", "canva-templates", "pinterest-templates", "guides-ebooks"] },
  },
  "/go/tdie-fb-group-promo": {
    kicker: "$10 a month", headline: "Your offer in front of *the TDIE group*",
    sub: "A recurring promotion spot inside the Facebook group.",
    photo: "gifts", sticker: "$10/mo",
    mock: { kind: "post", text: "This week's featured offer: your product, your link, in front of the group." },
  },
  "/go/the-conversion-architect": {
    kicker: "Recommended · $47", headline: "Sales pages that *actually convert*",
    sub: "The structure behind offers that sell.",
    photo: "kitchen", sticker: "$47",
    mock: { kind: "browser", url: "youroffer.com", view: "sales" },
  },
  "/go/the-faceless-launch-formula-by-thebossdigitalwealth-stan": {
    kicker: "Recommended · $77", headline: "Made a product *nobody's buying?*",
    sub: "The problem was never the product.",
    photo: "sofa", sticker: "$77",
    mock: { kind: "sales", title: "After the relaunch", rows: ["Sold: your product", "Sold: your product", "Sold: your product"] },
  },
  "/go/the-operating-prompts": {
    kicker: "$19 prompt pack", headline: "The *34 prompts* that run my business",
    sub: "The exact ones I use every week.",
    photo: "laptopPink", sticker: "34 prompts",
    mock: { kind: "prompts", cards: ["Plan my week from this list…", "Turn this voice note into an email…", "Check this page for weak spots…"] },
  },
  "/go/the-tommy-kate-edit": {
    kicker: "$17 prompt pack", headline: "Never start a caption from *a blank screen*",
    sub: "Prompts for faceless lifestyle creators. Lifetime access.",
    photo: "porch", sticker: "$17",
    mock: { kind: "prompts", cards: ["Cozy morning caption for…", "Soft-life hook for a reel about…", "Story poll ideas for…"] },
  },
  "/go/ugc-brand-contacts": {
    kicker: "$15 list", headline: "*150 brands* paying creators",
    sub: "Skip the research. Start pitching today.",
    photo: "gifts", sticker: "150",
    mock: { kind: "contacts", rows: ["Skincare", "Home decor", "Pet supplies", "Kids' clothing", "Kitchen tools"] },
  },
  "/go/zero-income-claim-reels": {
    kicker: "$37 · 100 reels", headline: "*100 reels* for before you have proof",
    sub: "Done-for-you hooks and captions that claim no income.",
    photo: "sofa", sticker: "100",
    mock: { kind: "reel", hook: "Things I'd do if I were starting from zero" },
  },
};
