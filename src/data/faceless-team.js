// The Faceless Team (working name) buyer website: the product buyers get.
// Private: unguessable address, noindex, linked from nowhere public.
// NOT LIVE AND NOT IN CANON YET. Name and prices need Jodie's approval before anything is published.
export const FT_KEY = 'R8oprhIAamx1bNzl';
export const FT_ROOT = `/shop/the-faceless-team/team-${FT_KEY}`;
export const FT_FILES = `/downloads/faceless-team-${FT_KEY}`;

export const FT_PAGES = [
 {key: 'start', name: 'Start Here', href: FT_ROOT},
 {key: 'brand', name: 'Your Brand File', href: FT_ROOT + '/brand-file'},
 {key: 'team', name: 'Your Team', href: FT_ROOT + '/your-team'},
 {key: 'build', name: 'Build Your Own Bot', href: FT_ROOT + '/build-your-own-bot'},
 {key: 'help', name: 'If Something Breaks', href: FT_ROOT + '/help'}
];

export const SETUP_FILE = 'faceless-team-setup.skill';

// Built from the eight quick cards in the kit.
export const BOTS = [
 {
  "slug": "pin-writer-bot",
  "name": "Pin Writer Bot",
  "file": "pin-writer-bot.skill",
  "intro": "Turns one post, product, freebie or link into finished Pinterest pins in your voice.",
  "listLabel": "Every pin comes with",
  "does": [
   "The words that go on the image",
   "Title",
   "Description",
   "Alt text",
   "Board",
   "Link",
   "Image prompt"
  ],
  "after": "Every length is checked before you see it, so nothing gets cut off on Pinterest.",
  "asks": [
   {
    "say": "Write 5 pins for this post.",
    "then": "paste the post or its link"
   },
   {
    "say": "Write 5 pins for my product.",
    "then": "paste the product description"
   },
   {
    "say": "Write 3 pins for my freebie that send people to my sign-up page.",
    "then": ""
   },
   {
    "say": "Give me 10 pins for this post, every one a different angle.",
    "then": ""
   },
   {
    "say": "Rewrite pin 2 to sound more like me.",
    "then": ""
   }
  ],
  "know": [
   "Give it the real post or description, not just a title. Better in, better out.",
   "Add the words to your image in Canva after you make the picture.",
   "Post pins from the same post at least 3 days apart.",
   "It never puts a price on a pin and never promises traffic or income.",
   "If your link earns you a commission, it adds the disclosure for you."
  ]
 },
 {
  "slug": "product-builder-bot",
  "name": "Product Builder Bot",
  "file": "product-builder-bot.skill",
  "intro": "Takes you from \"I don't know what to sell\" to one finished first digital product, in six steps:",
  "does": [
   "Find the idea in what you already know",
   "Write your one-sentence offer and test it",
   "Outline the product",
   "Write it with you, section by section",
   "Write your sales page",
   "Write your shop listing"
  ],
  "after": "It drafts. You correct. You never face a blank page.",
  "asks": [
   {
    "say": "I don't know what to sell. Help me make my first product.",
    "then": ""
   },
   {
    "say": "I want to make a checklist about [your topic]. Start at the outline.",
    "then": ""
   },
   {
    "say": "Here is my offer sentence. Run the four checks on it.",
    "then": "paste it"
   },
   {
    "say": "Write the sales page for this product.",
    "then": "paste the product"
   },
   {
    "say": "Write my shop listing for this product.",
    "then": "paste the product"
   }
  ],
  "know": [
   "It keeps your first product small on purpose: one problem, one person.",
   "It builds from your real steps and examples, so answer its short questions honestly.",
   "It never invents reviews, numbers or results, and never promises income.",
   "Coming back later? Paste the last thing it made and say \"pick up from here.\"",
   "When you finish, take your new product to the Pin Writer Bot."
  ]
 },
 {
  "slug": "ai-ceo-bot",
  "name": "AI CEO Bot",
  "file": "ai-ceo-bot.skill",
  "intro": "Your weekly business check-in, done in a few minutes:",
  "does": [
   "Helps you choose the five numbers worth watching",
   "Shows what moved since last week",
   "Names the number you might be avoiding",
   "Gives you three priorities that fit the hours you really have",
   "Builds a 90-day plan when you are ready"
  ],
  "after": "",
  "asks": [
   {
    "say": "I want to start a weekly CEO review. First time.",
    "then": ""
   },
   {
    "say": "Monday review.",
    "then": "Then type your five numbers."
   },
   {
    "say": "I'm overwhelmed. Here is everything on my mind.",
    "then": "Then dump the list."
   },
   {
    "say": "Should I start a TikTok?",
    "then": "or any \"should I\" question about your business"
   },
   {
    "say": "Plan my next 90 days.",
    "then": ""
   }
  ],
  "know": [
   "Keep it as one chat called Monday CEO Review and return to that same chat every week.",
   "You type your numbers in yourself. It takes about four minutes.",
   "A week of zeros is fine. The line matters more than the number.",
   "It compares you to your own past weeks. It never makes up what \"other businesses\" get.",
   "It is not tax, legal or money advice."
  ]
 },
 {
  "slug": "persona-bot",
  "name": "Persona Bot",
  "file": "persona-bot.skill",
  "intro": "Builds and runs the face of your faceless brand:",
  "does": [
   "Writes her World File: her places, signature prop, named objects and wardrobe",
   "Helps you make her reference image, once",
   "Writes ready-to-paste photo prompts that keep her the same woman every time",
   "Writes captions in her voice",
   "Fixes prompts when she keeps looking different"
  ],
  "after": "",
  "asks": [
   {
    "say": "Create my AI persona from scratch.",
    "then": ""
   },
   {
    "say": "Write a week of 7 photo prompts for my persona.",
    "then": ""
   },
   {
    "say": "She keeps looking different. Here is my prompt.",
    "then": "paste it"
   },
   {
    "say": "Write a photo of her desk with nobody in it.",
    "then": ""
   },
   {
    "say": "Write the caption for photo 3.",
    "then": ""
   }
  ],
  "know": [
   "Attach your reference image to every prompt. Use the same file every time.",
   "After her reference image is made, her face, hair, skin, body and age are never described in words again. That is what keeps her the same.",
   "Add any words to the picture afterwards, in Canva or your editor.",
   "Making three pictures and keeping the best one is normal.",
   "Check the AI label setting on the platforms you post to."
  ]
 },
 {
  "slug": "community-bot",
  "name": "Community Bot",
  "file": "community-bot.skill",
  "intro": "Keeps your group useful and alive without turning it into an advert:",
  "does": [
   "Plans your week in teach, value and sell slots",
   "Writes every post in your voice",
   "Drafts replies to member comments for you to approve",
   "Writes check-ins for members who have gone quiet",
   "Turns anything new in your community into posts"
  ],
  "after": "",
  "asks": [
   {
    "say": "Plan and write my week of community posts.",
    "then": ""
   },
   {
    "say": "Draft replies to these comments.",
    "then": "paste them"
   },
   {
    "say": "Write check-ins for these quiet members.",
    "then": "paste names and anything you know"
   },
   {
    "say": "I added something new to my group. Turn it into posts.",
    "then": ""
   },
   {
    "say": "Suggest a weekly ritual thread for my group.",
    "then": ""
   }
  ],
  "know": [
   "Everything is a draft. It never posts or replies for you.",
   "Teach comes first and sell comes last. Most days have no sell post.",
   "It never invents a member win, a number or a deadline.",
   "Complaints and refund requests are handed back to you with a first line only.",
   "Tell it what members asked this week. Real questions make the best posts."
  ]
 },
 {
  "slug": "email-bot",
  "name": "Email Bot",
  "file": "email-bot.skill",
  "intro": "Writes emails in your voice that sell without shouting:",
  "does": [
   "A six-email sales series, one honest answer per email to a reason people have not bought",
   "Subject lines and preview text for every email",
   "A welcome sequence for your freebie",
   "Single emails: a newsletter, an announcement, something new",
   "A sending checklist so the right people get it"
  ],
  "after": "",
  "asks": [
   {
    "say": "Write my six-email sales series for my offer.",
    "then": "paste the offer"
   },
   {
    "say": "Write a welcome sequence for my freebie.",
    "then": ""
   },
   {
    "say": "Give me five subject lines for this email.",
    "then": "paste it"
   },
   {
    "say": "Write one email announcing my new product.",
    "then": ""
   },
   {
    "say": "Rewrite this email so it sounds like me.",
    "then": "paste it"
   }
  ],
  "know": [
   "Have these ready: your price, what the buyer gets, your refund policy, and any real deadline.",
   "One ask per email, with the link placed twice.",
   "It will not write fake urgency, fake reviews or promised results.",
   "Leave your past buyers out when you send a sales series.",
   "Send only to people who signed up with you."
  ]
 },
 {
  "slug": "viral-research-bot",
  "name": "Viral Research Bot",
  "file": "viral-research-bot.skill",
  "intro": "Shows you what is working right now for small accounts like yours:",
  "does": [
   "Tells you where to look, in ten minutes a week",
   "Tests whether a post is a true standout for the account that posted it",
   "Keeps your swipe file",
   "Finds the patterns, with real counts",
   "Writes your own versions, in your words"
  ],
  "after": "",
  "asks": [
   {
    "say": "Show me where to look for posts that are working in my niche.",
    "then": ""
   },
   {
    "say": "Are these outliers?",
    "then": "paste or screenshot the post and the account's grid"
   },
   {
    "say": "Find the patterns in my swipe file.",
    "then": ""
   },
   {
    "say": "Write me three post ideas from those patterns.",
    "then": ""
   },
   {
    "say": "Here are my own posts from last month. What is working for me?",
    "then": ""
   }
  ],
  "know": [
   "You collect the posts and it does the analysing. It cannot scroll the apps for you.",
   "A screenshot of the post and one of the account's grid is enough.",
   "It needs about ten standout posts before a pattern means much.",
   "It borrows patterns, never another creator's words or video.",
   "It never promises views."
  ]
 },
 {
  "slug": "bot-builder-bot",
  "name": "Bot Builder Bot",
  "file": "bot-builder-bot.skill",
  "intro": "Turns something you already do well into a bot of your own:",
  "does": [
   "Helps you choose the right task",
   "Interviews you so the bot works your way",
   "Writes the bot and a self-check for it",
   "Tests it on real examples",
   "Packages it as one file and writes your buyer's Start Here page",
   "Helps you write the listing if you are selling it"
  ],
  "after": "",
  "asks": [
   {
    "say": "I want to build my own bot.",
    "then": ""
   },
   {
    "say": "Help me find a task that would make a good bot.",
    "then": ""
   },
   {
    "say": "Turn this checklist into a bot.",
    "then": "paste it"
   },
   {
    "say": "Package my bot.",
    "then": ""
   },
   {
    "say": "Write the listing for my bot.",
    "then": ""
   }
  ],
  "know": [
   "One bot does one job.",
   "Build from something you do often and do well.",
   "The real test is a brand-new chat, then one other person trying it without help.",
   "Only your own method and material goes in. Nothing from someone else's paid product.",
   "Read BUILD-AND-SELL-YOUR-OWN-BOT.md for the whole method in one place."
  ]
 }
];

export const UPDATES = [
 {date: '11 November 2026', text: 'Your team is here: the one-time setup, eight bots, the Brand File builder and the Build & Sell Your Own Bot guide.'}
];

// Desk labels for the team roster. Labels only: they name where each bot sits, they add no capability.
export const DEPT = {
 'pin-writer-bot': 'Pinterest desk',
 'product-builder-bot': 'Product desk',
 'ai-ceo-bot': 'Monday meeting',
 'persona-bot': 'Persona studio',
 'community-bot': 'Community desk',
 'email-bot': 'Email desk',
 'viral-research-bot': 'Research desk',
 'bot-builder-bot': 'Bot workshop'
};
export const pad = (n) => String(n).padStart(2, '0');
export const line = (b) => b.intro.replace(/:$/, '.');
