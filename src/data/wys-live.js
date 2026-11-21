// The two looks the system built that are live on the Lifestyle blog.
// Photos are the founder-approved Basic, Styled and Lifestyle images.
// Pins, carousels and phone screens built from them are labeled "Example".
import walkBasic from '../lifestyle/pink-winter-walk-warm-up-basic.jpg';
import walkStyled from '../lifestyle/pink-winter-walk-warm-up-styled.jpg';
import walkLife from '../lifestyle/pink-winter-walk-warm-up-lifestyle.jpg';
import mantelBasic from '../lifestyle/pink-christmas-mantel-basic.jpg';
import mantelStyled from '../lifestyle/pink-christmas-mantel-styled.jpg';
import mantelLife from '../lifestyle/pink-christmas-mantel-lifestyle.jpg';
import walkBlogPhone from '../assets/wys/convert/blog-pink-winter-walk-warm-up-phone.jpg';
import walkBlogDesk from '../assets/wys/convert/blog-pink-winter-walk-warm-up-desktop.jpg';
import mantelBlogPhone from '../assets/wys/convert/blog-pink-christmas-mantel-phone.jpg';
import mantelBlogDesk from '../assets/wys/convert/blog-pink-christmas-mantel-desktop.jpg';
import {WYS_ROOT} from './wys.js';

// One place to change the call to action. The waitlist is closed (Jodie, 13 Oct 2026): every
// button points at the sales page. At launch the site swaps it for the checkout link on its own.
export const WYS_CTA = {href: WYS_ROOT, label: 'See the storefront'};

// The switch times (Jodie, 11 October 2026: member presale Tuesday at noon). The site
// changes itself at these times in the visitor's browser, no rebuild needed:
//  - before WYS_PRESALE_AT: waitlist wording ("member presale opens Tuesday at 12 pm ET")
//  - from WYS_PRESALE_AT: "member presale is open now inside the Skool community"
//  - from WYS_LAUNCH_AT, ONLY once WYS_CHECKOUT holds the real public checkout link: every
//    "Join the waitlist" button becomes "Get the Storefront" to the checkout, the waitlist
//    links and the waitlist page go to the sales page, and the hero waitlist box becomes the
//    $27 launch-weekend box. With WYS_CHECKOUT empty the site stays on the presale wording,
//    so it never shows a dead buy button.
// Preview any stage by adding ?wysphase=wait, ?wysphase=presale or ?wysphase=launch to a page.
export const WYS_PRESALE_AT = '2026-10-13T12:00:00-04:00';
export const WYS_LAUNCH_AT = '2026-10-16T12:00:00-04:00';
// Launch weekend ends Sunday 18 Oct at midnight (Jodie's approved launch posts: "Tonight's the last
// night it's $27. From tomorrow ... $37"). From WYS_REGULAR_AT the site shows $37 and drops the
// launch-weekend wording (stage "regular"; preview with ?wysphase=regular).
export const WYS_REGULAR_AT = '2026-10-19T00:00:00-04:00';
export const WYS_CHECKOUT = 'https://links.thedigitalincomeedit.com/shop/66271fb0-fc54-4aae-ad9f-c826f4635ee7';

// The link row under the intro on every storefront page (Jodie, 11 October 2026):
// waitlist, a free look inside the system (the Real Results page) and see it live (the
// Lifestyle blog the system posts to). The waitlist link flips to the sales page at
// launch on its own (see WYS_LAUNCH_AT). Each page leaves out its own link.
export const WYS_LINKS = [
 {key: 'overview', label: 'See the storefront', href: WYS_ROOT},
 {key: 'inside', label: 'Free look inside the system', href: WYS_ROOT + '/real-results'},
 {key: 'live', label: 'See it live', href: '/lifestyle'}
];

const SITE = 'https://www.thedigitalincomeedit.com';

// Swapped 20 Nov 2026 from the October Halloween and pumpkin patch looks to two current
// winter looks the system built and published on the Lifestyle blog.
export const liveLooks = [
 {
  slug: 'pink-christmas-mantel',
  name: 'The Pink Christmas Mantel',
  short: 'Pink Christmas Mantel',
  category: 'Home decor · Christmas',
  url: `${SITE}/lifestyle/pink-christmas-mantel`,
  overlay: ['Pink Christmas', 'Mantel'],
  blogPhone: mantelBlogPhone,
  blogDesk: mantelBlogDesk,
  blogLine: 'A pink cedar garland, knitted stockings, a mini pink tree, pink ornaments and glass candlesticks. 5 linked finds and how to style them.',
  photos: {
   basic: {src: mantelBasic, alt: 'A pink cedar garland, four pink knitted stockings, a pink mini Christmas tree, pink ornaments and pink glass candlestick holders on deep green painted floorboards'},
   styled: {src: mantelStyled, alt: 'A white brick fireplace mantel dressed with a pink garland, pink knitted stockings, a mini pink tree, ornaments and glass candlesticks'},
   lifestyle: {src: mantelLife, alt: 'Tommy Kate hanging a pink knitted stocking on a mantel decorated with a pink garland, with a golden retriever asleep by the fireplace'}
  }
 },
 {
  slug: 'pink-winter-walk-warm-up',
  name: 'The Pink Winter Walk Warm-Up',
  short: 'Pink Winter Walk',
  category: 'Clothing · Winter',
  url: `${SITE}/lifestyle/pink-winter-walk-warm-up`,
  overlay: ['Pink Winter', 'Walk Warm-Up'],
  blogPhone: walkBlogPhone,
  blogDesk: walkBlogDesk,
  blogLine: 'A hot pink puffer vest, a pink beanie and scarf set, furry pink boots, brown leggings, a lavender crossbody and a pink Stanley. 6 linked finds.',
  photos: {
   basic: {src: walkBasic, alt: 'Flat lay of a hot pink puffer vest, pink beanie, scarf, gloves, ear muffs and socks, pink furry boots, brown leggings, a lavender crossbody and a pink Stanley'},
   styled: {src: walkStyled, alt: 'A mudroom entryway with a hot pink puffer vest on a hook, a lavender crossbody, pink beanie and scarf set, furry pink boots and a pink Stanley ready for a winter walk'},
   lifestyle: {src: walkLife, alt: 'Tommy Kate walking a snowy lane with a golden retriever, wearing a hot pink puffer vest, pink beanie and scarf, brown leggings and furry pink boots'}
  }
 }
];

export const roles = [
 {key: 'basic', name: 'Basic', note: 'Clean flat lay of the pieces. The only pin that gets a headline.'},
 {key: 'styled', name: 'Styled', note: 'The pieces in a real setting. No text.'},
 {key: 'lifestyle', name: 'Lifestyle', note: 'Tommy Kate using the pieces in her real rooms. No text.'}
];

export const objections = [
 ['Do I need to be techy?', 'No. The Quick Start takes about 15 minutes. If you want to customize it, give it about an hour.'],
 ['Claude or ChatGPT?', 'Built on Claude. ChatGPT version on the way.'],
 ['Does my computer need to be on?', 'Yes. Leave your computer on and signed into Amazon overnight.'],
 ['Can I approve things first?', 'Yes. It runs automatically by default, and you can switch on approvals to OK each look before it goes out. I recommend approvals on for your first few days.'],
 ['What if I only have a few minutes?', 'Do the 15-minute Quick Start and go to bed. That’s the whole job.'],
 ['Is this a PDF?', 'No. It’s a website that gets updated regularly, so it never goes stale. New affiliate brand automations are on the way.'],
 ['What else will I pay for?', 'Your own AI account: a paid Claude plan, plus an image tool. To load and schedule your pins and posts automatically, you also need Metricool. Its free plan is fine to start, and you’ll want to upgrade once you scale up. The setup tells you which plan to pick. The Storefront itself is one payment.'],
 ['I tried Pinterest before and quit. Why is this different?', 'Because the part you quit was the daily making. This does the making. Turn approvals on for the first few days if you want, and you OK each look before it goes out.']
];
