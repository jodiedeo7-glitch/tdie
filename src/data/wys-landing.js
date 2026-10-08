// WYS launch landing + Look Inside (private preview, Jodie 7 Oct 2026).
// Photos: the nine-photo private preview bundle (manifest checksums verified 7 Oct 2026).
// Clothing = one Tommy Kate five-product mock look (visual direction approved 6 Oct 2026;
// retail fidelity, avatar identity and full automatic workflow NOT verified).
// Decor = approved Halloween styling photographs; product shapes approximate.
// Scope copy is limited to what claude/WYS_REFERENCE_PACK_2026-10-07.md documents.
// Dates: founder instruction 7 Oct 2026 8:54 pm ET (member presale Sun 11 Oct 2 pm ET;
// full launch "next week", Thursday not promised). No prices, codes or affiliate rate.
import clBasic from "../assets/wys-private/clothing-basic.webp";
import clStyled from "../assets/wys-private/clothing-styled.webp";
import clLife from "../assets/wys-private/clothing-lifestyle.png";
import pwBasic from "../assets/wys-private/pretty-wicked-entryway-basic.png";
import pwStyled from "../assets/wys-private/pretty-wicked-entryway-styled.png";
import pwLife from "../assets/wys-private/pretty-wicked-entryway-lifestyle.png";
import gfBasic from "../assets/wys-private/ghoul-fuel-coffee-bar-basic.png";
import gfStyled from "../assets/wys-private/ghoul-fuel-coffee-bar-styled.png";
import gfLife from "../assets/wys-private/ghoul-fuel-coffee-bar-lifestyle.png";

export const PRODUCT = "The While-You-Sleep Storefront™";
export const LANDING = "/while-you-sleep";
export const INSIDE = "/while-you-sleep/inside";
export const WAITLIST_PAGE = "/while-you-sleep/waitlist";
export const PRESALE_LINE = "Member presale · Sunday, October 11 · 2 PM ET";

export const WAITLIST_ACTION = "https://assets.mailerlite.com/jsonp/2532349/forms/200719393549715350/subscribe";
export const WAITLIST = {
  kicker: "The waitlist",
  heading: "Hear the second the doors open.",
  sub: "One email when the member presale opens Sunday, one on launch day. Confirm the email in your inbox to lock in your spot. Unsubscribe anytime.",
  button: "Join the Waitlist",
  done: "You're on the list! Confirm the email in your inbox and you'll hear from me the minute the presale opens.",
};

export const PHOTOS = { clBasic, clStyled, clLife, pwBasic, pwStyled, pwLife, gfBasic, gfStyled, gfLife };

export const CLOTHING = {
  label: "Clothing",
  name: "Off Duty, the pink edit",
  note: "One five-product mock outfit look. Visual direction approved; exact retail matching not verified.",
  shots: [
    { img: clBasic, role: "Basic", title: "The edit", text: "A labelled editorial flat lay of the five picks.", alt: "Overhead flat lay on cream fabric with the words off duty, the pink edit: a pink cable cardigan, white ribbed tank, light jeans with pink pocket stitching, pink sneakers and a cream chain bag." },
    { img: clStyled, role: "Styled", title: "Getting ready", text: "A fuller, unlabelled outfit flat lay with the accessories that finish it.", alt: "Person-free getting-ready flat lay on a bed: pink cardigan over a white tank, pearl necklaces, jeans, pink sneakers, cream chain bag, phone, watch, sunglasses and a pink claw clip." },
    { img: clLife, role: "Lifestyle", title: "Worn, in her world", text: "Tommy Kate in the outfit, in a separately composed moment.", alt: "Woman in a pink cardigan, white tank, jeans and pink sneakers opening a white garden gate beside a lavender-shuttered farmhouse, a golden retriever sitting at her feet." },
  ],
};

export const DECOR_A = {
  label: "Home decor",
  name: "Pretty Wicked, the Halloween entryway",
  note: "Approved styling photographs. Product shapes are approximate, not retailer photos.",
  shots: [
    { img: pwBasic, role: "Basic", title: "The picks", text: "A curated object flat lay of the products.", alt: "Overhead flat lay of hot pink foam pumpkins, pink gauze, pink jack-o-lantern string lights, black bat cutouts and pink tea lights on a black wooden table." },
    { img: pwStyled, role: "Styled", title: "In place", text: "The products arranged where they're meant to live.", alt: "Cottage entryway with a black console, oval mirror, pink pumpkins, pink gauze, glowing jack-o-lantern lights and black bats on the wall." },
    { img: pwLife, role: "Lifestyle", title: "Lived in", text: "Tommy Kate using the space, from a new angle.", alt: "Woman in a pink cardigan opening the front door to a ghost trick-or-treater, the pink Halloween entryway behind her." },
  ],
};

export const DECOR_B = {
  label: "Kitchen and home",
  name: "Ghoul Fuel, the pink coffee bar",
  note: "Approved styling photographs. Product shapes are approximate, not retailer photos.",
  shots: [
    { img: gfBasic, role: "Basic", title: "The picks", text: "A curated object flat lay of the products.", alt: "Overhead flat lay of a pink heart tiered stand, a pink ghost mug, pink pumpkins, disco balls and pink tea lights on dark wood." },
    { img: gfStyled, role: "Styled", title: "In place", text: "The coffee bar, set up and ready.", alt: "Cream kitchen coffee bar styled with a pink ghost mug, heart tiered stand of pumpkins, an espresso machine and a ghost painting." },
    { img: gfLife, role: "Lifestyle", title: "Lived in", text: "Tommy Kate pouring the first cup.", alt: "Woman in a lavender cardigan and pink slippers holding a pink ghost mug at her Halloween coffee bar." },
  ],
};

// What one look becomes. Each line is documented in the WYS master file.
export const OUTPUTS = [
  { n: "3", t: "Photographs", p: "Basic, styled and lifestyle, built for the category: an outfit is worn, a room is lived in." },
  { n: "3", t: "Pinterest graphics", p: "Finished pins with your headline type, title, description, alt text and disclosure." },
  { n: "3", t: "Instagram slides", p: "A carousel cut from the same look, for after the pins go out." },
  { n: "1", t: "Shopping destination", p: "An Amazon Idea List if you're an Influencer, or a page on your own site if you're an Associate." },
  { n: "1", t: "Blog page", p: "A shop-the-look page on your own site that search can find." },
];

export const PATHS = [
  { t: "Time-saving", p: "Recurring tasks and connected tools do the steps your accounts support. You choose how much you review before anything is scheduled." },
  { t: "Credit-saving", p: "Lower-cost Claude or ChatGPT routes for the steps that would otherwise eat credits." },
  { t: "Manual", p: "Every step as a checklist you run yourself, with the same finish line." },
];

// Look Inside: how each category's recipe differs (master file section 2 roles).
export const HOW = {
  clothing: "Clothing is about the outfit, so the styled shot stays a flat lay: fuller, layered, unlabelled. The lifestyle photo shows it worn in its own scene.",
  entryway: "Decor is about the space, so the styled shot puts the products where they belong, and the lifestyle photo shows someone using that space.",
  coffee: "Same decor recipe, a different corner of the house: the picks, the bar set up, then the first cup.",
};

// Workflow in three chapters (master file sections 15-23).
export const CHAPTERS = [
  { t: "Set it up once", steps: [
    { b: "Your accounts", p: "Influencer Idea Lists, Associates-only, or your own site." },
    { b: "Your look", p: "Persona or no persona, channels, timezone and cadence." },
    { b: "Your control", p: "Image tool and budget, and how much you review." },
  ]},
  { t: "Build each look", steps: [
    { b: "Theme and picks", p: "Choose the theme, season and Amazon products. Vibe photos optional." },
    { b: "Three photographs", p: "Basic, styled and lifestyle, using that category's recipe." },
    { b: "Graphics and copy", p: "Three pins and three Instagram slides, with alt text and your disclosure." },
  ]},
  { t: "Publish and keep it running", steps: [
    { b: "In order", p: "Shopping destination and blog page, then Pinterest, then Instagram." },
    { b: "Read back", p: "Each result is checked, so you know what really went out." },
    { b: "On repeat", p: "A weekly look, an optional Outfit of the Day, and a daily check-up." },
  ]},
];

export const COVERS = [
  "A guided setup that records your choices and what your accounts can and can't do yet",
  "The three-photograph recipe, per category: clothing and decor",
  "Graphic, copy and disclosure rules for pins and Instagram slides",
  "Three recurring tasks: weekly look, optional Outfit of the Day, daily check-up",
  "Persona and no-persona paths; Influencer, Associates-only and own-site paths",
  "The Brand Closet™ Outfit of the Day path, for members of that community",
  "A lower-cost route and a manual checklist for every step that costs credits",
];

export const NEEDS = [
  "Amazon Associates (Influencer approval unlocks Idea Lists)",
  "A Pinterest business account and a public board",
  "An image tool you choose, on your own budget",
  "Persona reference photos, or the no-persona path",
  "A website, for the blog page and the Associates-only path",
  "Metricool, only if you schedule through it",
];

export const LIMITS = [
  "Automatic product finding isn't ready. It needs Amazon's Creators API, which opens at 10 qualifying sales in 30 days.",
  "What runs on its own depends on your accounts and is tested in your setup. A missing step is named, never skipped.",
  "The photographs are styling illustrations. Product shapes are approximate, not retailer photos.",
  "No income, sales or traffic promises.",
];
