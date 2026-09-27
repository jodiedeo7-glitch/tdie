// Site navigation, one source. SiteNav and SiteFooter render from here, so
// every page carries the same labels, in the same order, with the same names.

export const NAV = [
  { label: "Learn", href: "/learn" },
  { label: "Free Resources", href: "/resources" },
  { label: "Shop", href: "/shop" },
  { label: "Lifestyle", href: "/lifestyle" },
  { label: "About", href: "/about" },
];

export const NAV_CTA = { label: "Join the Membership", href: "/membership" };

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
    { label: "Community", href: "/community" },
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
