// The two looks the system built that are live on the Lifestyle blog.
// Photos are the founder-approved Basic, Styled and Lifestyle images.
// Pins, carousels and phone screens built from them are labelled "Example".
import plaidBasic from '../lifestyle/pink-plaid-pumpkin-patch-outfit-basic.jpg';
import plaidStyled from '../lifestyle/pink-plaid-pumpkin-patch-outfit-styled.jpg';
import plaidLife from '../lifestyle/pink-plaid-pumpkin-patch-outfit-lifestyle.png';
import ghostBasic from '../lifestyle/pink-ghost-coffee-bar-basic.jpg';
import ghostStyled from '../lifestyle/pink-ghost-coffee-bar-styled.jpg';
import ghostLife from '../lifestyle/pink-ghost-coffee-bar-lifestyle.png';
import ghostRoundup from '../lifestyle/pink-ghost-coffee-bar-roundup.jpg';
import plaidRoundup from '../lifestyle/pink-plaid-pumpkin-patch-outfit-roundup.jpg';
import plaidBlogPhone from '../assets/wys/convert/blog-pink-plaid-pumpkin-patch-outfit-phone.jpg';
import plaidBlogDesk from '../assets/wys/convert/blog-pink-plaid-pumpkin-patch-outfit-desktop.jpg';
import ghostBlogPhone from '../assets/wys/convert/blog-pink-ghost-coffee-bar-phone.jpg';
import ghostBlogDesk from '../assets/wys/convert/blog-pink-ghost-coffee-bar-desktop.jpg';
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

export const liveLooks = [
 {
  slug: 'pink-ghost-coffee-bar',
  name: 'The Pink Ghost Coffee Bar',
  short: 'Pink Ghost Coffee Bar',
  category: 'Home decor · Halloween',
  url: `${SITE}/lifestyle/pink-ghost-coffee-bar`,
  overlay: ['Pink Ghost', 'Coffee Bar'],
  blogPhone: ghostBlogPhone,
  blogDesk: ghostBlogDesk,
  blogLine: 'Pink ghosts, a BOO sign, pink jack-o-lanterns and a flock of paper bats. 6 linked finds and how to style them.',
  photos: {
   basic: {src: ghostBasic, alt: 'Pink ghost figurines, printed flameless candles and pink and white jack-o-lanterns lined up on a wood sideboard against a plum wall with paper bats'},
   styled: {src: ghostStyled, alt: 'A pink Halloween coffee bar on a painted sideboard with ghosts, a BOO sign, pink gauze, candy jars and paper bats on the wall'},
   lifestyle: {src: ghostLife, alt: 'Tommy Kate laughing as she sticks pink and black paper bats on her kitchen backsplash, pink ghosts and jack-o-lanterns on the counter'},
   roundup: {src: ghostRoundup, alt: 'Roundup pin: the whole pink ghost coffee bar with the headline Pink Ghost, Coffee Bar Decor, You will love this year'}
  }
 },
 {
  slug: 'pink-plaid-pumpkin-patch-outfit',
  name: 'The Pink Plaid Pumpkin Patch Outfit',
  short: 'Pink Plaid Pumpkin Patch',
  category: 'Clothing · Fall',
  url: `${SITE}/lifestyle/pink-plaid-pumpkin-patch-outfit`,
  overlay: ['Pink Plaid', 'Pumpkin Patch'],
  blogPhone: plaidBlogPhone,
  blogDesk: plaidBlogDesk,
  blogLine: 'A pink plaid shacket, straight leg jeans, white platform sneakers, a purple tote and a green pom beanie. 6 linked finds.',
  photos: {
   basic: {src: plaidBasic, alt: 'Flat lay on a wood floor of a pink plaid shacket, black crop top, light wash jeans, white sneakers, a purple tote and a green pom beanie'},
   styled: {src: plaidStyled, alt: 'The pink plaid shacket, jeans, purple tote and green beanie hanging on a peg rail above white sneakers, pumpkins and apples'},
   lifestyle: {src: plaidLife, alt: 'Tommy Kate crouching at a muddy pumpkin patch holding a pumpkin, wearing the pink plaid shacket, jeans, white sneakers and green beanie'},
   roundup: {src: plaidRoundup, alt: 'Roundup pin: the pink plaid outfit on a peg rail with the headline Pink Plaid, Fall Outfit, Pumpkin Patch Ready'}
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
