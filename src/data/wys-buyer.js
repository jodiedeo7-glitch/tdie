// The While-You-Sleep Storefront™ buyer website (the product buyers get).
// Private: lives under an unguessable address, noindex, linked from nowhere public.
// The Beacons products deliver this address. To change the address, change WYS_BUYER_KEY
// and update the Beacons delivery link at the same time.
// To update the product for every buyer: edit this file or src/scripts/wys-buyer-prompts.js and deploy.
import {WYS_ROOT} from './wys.js';

export const WYS_BUYER_KEY = 'MrHnXILyVkggFyKf';
export const WYS_BUYER_ROOT = `${WYS_ROOT}/studio-${WYS_BUYER_KEY}`;

export const BUYER_PAGES = [
 {key: 'start', name: 'Start Here', href: WYS_BUYER_ROOT},
 {key: 'approved', name: 'Get Approved', href: WYS_BUYER_ROOT + '/get-approved'},
 {key: 'setup', name: 'Set It Up', href: WYS_BUYER_ROOT + '/set-it-up'},
 {key: 'help', name: 'If Something Breaks', href: WYS_BUYER_ROOT + '/help'},
 {key: 'promote', name: 'Promote It', href: WYS_BUYER_ROOT + '/promote'}
];

// Affiliate links that appear in the product (canon.json, affiliate rows). Disclosure ships with them.
export const AFF = {
 higgsfield: 'https://higgsfield.ai?fpr=jodie-30b092',
 weekendEcosystem: 'https://www.thedigitalincomeedit.com/shop/weekend-ecosystem',
 brandCloset: 'https://www.skool.com/the-brand-closet/about?ref=97643519c9b448d0a683ab33b6cc68ce'
};

// Dated change notes shown on Start Here. Newest first.
export const UPDATES = [
 {date: '23 October 2026', text: 'Amazon disclosure fixed to Amazon\u2019s own wording. Every pin that links to Amazon now ends "#ad As an Amazon Associate I earn from qualifying purchases.", and so does every Instagram carousel caption. Amazon requires a disclosure by every affiliate link plus that exact sentence tied to your account, so also put it in your Instagram bio and your Pinterest profile. Already set up? Copy your new nightly run on Set It Up and tell Claude: "Replace my While-You-Sleep nightly run task\u2019s prompt with this."'},
 {date: '23 October 2026', text: 'Get Approved rewritten as complete beginner steps and fact-checked against Amazon\u2019s own help pages: which to apply for first (neither has to come first), getting your accounts ready, applying to the Influencer Program and to Associates click by click, everything to set up the day you are approved, onsite earnings, and the rules that get accounts closed. It also covers Amazon\u2019s April 2026 change: completing registration now gives a storefront and creator link, not only Influencers.'},
 {date: '23 October 2026', text: 'New page: Get Approved. Not an Amazon Influencer yet? It walks you from no account to your own storefront: Associate vs Influencer, onsite vs offsite, what to fix on your accounts before you apply, how to apply, and everything to set up the day you are approved. Associates only? Your system already runs, with pins linking to your blog posts until your storefront is ready.'},
 {date: '23 October 2026', text: 'You choose your pins now. Set It Up has a new question, \u201cWhich pins to make for every look\u201d: tick Basic, Styled, Lifestyle, Roundup, Found It and the Storefront promo pin, as many or as few as you like. Your nightly run only makes the photos and pins you tick, so fewer pins means fewer credits.'},
 {date: '23 October 2026', text: 'New: a fifth pin for every look, the Found It. It shows the look\u2019s single most interesting piece on its own in a real, lived-in photo with white handwritten words over it, \u201cI found this ___ on\u201d and an arrow to \u201cAmazon \u2661\u201d, like the handwritten \u201cI found this on Amazon\u201d pins that are pulling clicks on Pinterest right now. It links straight to the look\u2019s Idea List. Your system now makes five photos per look and schedules five pins, so 2 looks a night means 10 pins.'},
 {date: '23 October 2026', text: 'New: a fourth pin for every look, the Roundup. It shows every piece of the look together in one styled scene with a three-line headline across the top, like the "You\u2019ll Love This Year" roundup pins all over Pinterest, and it links straight to the look\u2019s Idea List. Your system now makes four photos per look (Basic, Styled, Lifestyle, Roundup) and schedules four pins, so 2 looks a night means 8 pins.'},
 {date: '19 October 2026', text: 'Instagram is now two carousels a day, one per look. Your system spaces them about five hours apart on the next day with room, instead of one carousel a day.'},
 {date: '19 October 2026', text: 'New: one storefront promo pin per look. Each look now also gets a pin of its Lifestyle photo that links to your storefront home page instead of the Idea List, on its own day, so people find your whole storefront, not just one list.'},
 {date: '19 October 2026', text: 'Every piece in a look now has to be on that look’s Idea List. Your system adds any missing piece to the list before the look is written, so every product in your photos is shoppable from the list your pin links to.'},
 {date: '19 October 2026', text: 'Licensed characters are in: a new Licensed characters and fandom favorites category, plus a setup question for your favorite characters (Hello Kitty, Kuromi, Barbie and more). Anything sold on Amazon is allowed, and your system now builds looks and themed lists around the characters you love.'},
 {date: '19 October 2026', text: 'Products now appear exactly as they are: every photo keeps each product\u2019s own logo, tags, patches, stitching and details just like its Amazon listing photo. The no-logos rule now only covers props and anything that is not a product.'},
 {date: '18 October 2026', text: 'Better products and no repeats: every look has 5 or 6 pieces judged on style and quality, every look goes into your log the moment it is chosen so it is never repeated even before its photos are made, and photo prompts open with “Highest quality finished photograph”, give exact piece counts, and make the Styled photo a brand-new picture with no lettering. Every photo is now made from a Product Sheet, one white page holding each piece’s real Amazon photo, so the products look exactly like the listings instead of being described in words.'},
 {date: '16 October 2026', text: 'Size check added: every look now records each product\u2019s real size, every photo prompt ends with a scale line, and a photo fails if a piece looks too big or too small next to the others.'},
 {date: '12 October 2026', text: 'The Storefront opens for members: setup, the nightly run, approvals, a by-hand option for every step, and the affiliate promo kit.'}
];
