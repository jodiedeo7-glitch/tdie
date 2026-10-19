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
 {date: '19 October 2026', text: 'Every piece in a look now has to be on that look’s Idea List. Your system adds any missing piece to the list before the look is written, so every product in your photos is shoppable from the list your pin links to.'},
 {date: '19 October 2026', text: 'Licensed characters are in: a new Licensed characters and fandom favorites category, plus a setup question for your favorite characters (Hello Kitty, Kuromi, Barbie and more). Anything sold on Amazon is allowed, and your system now builds looks and themed lists around the characters you love.'},
 {date: '19 October 2026', text: 'Products now appear exactly as they are: every photo keeps each product\u2019s own logo, tags, patches, stitching and details just like its Amazon listing photo. The no-logos rule now only covers props and anything that is not a product.'},
 {date: '18 October 2026', text: 'Better products and no repeats: every look has 5 or 6 pieces judged on style and quality, every look goes into your log the moment it is chosen so it is never repeated even before its photos are made, and photo prompts open with “Highest quality finished photograph”, give exact piece counts, and make the Styled photo a brand-new picture with no lettering. Every photo is now made from a Product Sheet, one white page holding each piece’s real Amazon photo, so the products look exactly like the listings instead of being described in words.'},
 {date: '16 October 2026', text: 'Size check added: every look now records each product\u2019s real size, every photo prompt ends with a scale line, and a photo fails if a piece looks too big or too small next to the others.'},
 {date: '12 October 2026', text: 'The Storefront opens for members: setup, the nightly run, approvals, a by-hand option for every step, and the affiliate promo kit.'}
];
