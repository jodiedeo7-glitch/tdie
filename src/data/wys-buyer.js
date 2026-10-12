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
 {date: '12 October 2026', text: 'The Storefront opens for members. Claude version: setup, nightly run, approvals mode and every option below.'}
];
