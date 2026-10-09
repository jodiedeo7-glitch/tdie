// Site navigation, one source. SiteNav and SiteFooter render from here, so
// every page carries the same labels, in the same order, with the same names.

export const NAV = [
  { label: "Start Here", href: "/resources/find-your-door" },
  { label: "The Method", href: "/#method" },
  { label: "Shop", href: "/shop" },
  { label: "Membership", href: "/membership" },
];

import { SKOOL_PLANS } from "./facts.js";
export const NAV_CTA = { label: "Start free for 7 days", href: SKOOL_PLANS };

export const FOOTER = [
  { h: "Read", links: [
    { label: "The Library", href: "/learn" },
    { label: "Free Resources", href: "/resources" },
    { label: "Find Your Door", href: "/resources/find-your-door" },
    { label: "The Weekly Edit", href: "/newsletter" },
  ] },
  { h: "Build", links: [
    { label: "The Weekend Ecosystem™", href: "/shop/weekend-ecosystem" },
    { label: "Membership", href: "/membership" },
      { label: "Shop", href: "/shop" },
    { label: "Lifestyle", href: "/lifestyle" },
  ] },
  { h: "Studio", links: [
    { label: "About", href: "/about" },
    { label: "Work With Me", href: "/work-with-me" },
    { label: "Questions", href: "/faq" },
    { label: "Privacy", href: "/privacy" },
    { label: "Contact", href: "mailto:hello@thedigitalincomeedit.com" },
  ] },
];

export const SOCIAL = [
  { label: "Pinterest", href: "https://pinterest.com/TheDigitalIncomeEditTDIE" },
  { label: "Instagram", href: "https://instagram.com/the.faceless.homestead.mama" },
];
