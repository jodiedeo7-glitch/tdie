// The two looks the system built that are live on the Lifestyle blog.
// Photos are the founder-approved Basic, Styled and Lifestyle images.
// Pins, carousels and phone screens built from them are labelled "Example".
import plaidBasic from '../lifestyle/pink-plaid-pumpkin-patch-outfit-basic.jpg';
import plaidStyled from '../lifestyle/pink-plaid-pumpkin-patch-outfit-styled.jpg';
import plaidLife from '../lifestyle/pink-plaid-pumpkin-patch-outfit-lifestyle.png';
import ghostBasic from '../lifestyle/pink-ghost-coffee-bar-basic.jpg';
import ghostStyled from '../lifestyle/pink-ghost-coffee-bar-styled.jpg';
import ghostLife from '../lifestyle/pink-ghost-coffee-bar-lifestyle.png';
import plaidBlogPhone from '../assets/wys/convert/blog-pink-plaid-pumpkin-patch-outfit-phone.jpg';
import plaidBlogDesk from '../assets/wys/convert/blog-pink-plaid-pumpkin-patch-outfit-desktop.jpg';
import ghostBlogPhone from '../assets/wys/convert/blog-pink-ghost-coffee-bar-phone.jpg';
import ghostBlogDesk from '../assets/wys/convert/blog-pink-ghost-coffee-bar-desktop.jpg';
import {WYS_ROOT} from './wys.js';

// One place to change the call to action. On presale day, swap href and
// label for the checkout link and "Buy now"; every button on the three pages
// reads from here.
export const WYS_CTA = {href: WYS_ROOT + '/waitlist', label: 'Join the waitlist'};

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
   lifestyle: {src: ghostLife, alt: 'Tommy Kate laughing as she sticks pink and black paper bats on her kitchen backsplash, pink ghosts and jack-o-lanterns on the counter'}
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
   lifestyle: {src: plaidLife, alt: 'Tommy Kate crouching at a muddy pumpkin patch holding a pumpkin, wearing the pink plaid shacket, jeans, white sneakers and green beanie'}
  }
 }
];

export const roles = [
 {key: 'basic', name: 'Basic', note: 'Clean flat lay with a text overlay. The only image with words on it.'},
 {key: 'styled', name: 'Styled', note: 'The pieces in a real setting. No text.'},
 {key: 'lifestyle', name: 'Lifestyle', note: 'Tommy Kate using the pieces in her real rooms. No text.'}
];

export const objections = [
 ['Do I need to be techy?', 'No. The Quick Start takes about 15 minutes. If you want to customize it, give it about an hour.'],
 ['Claude or ChatGPT?', 'Either one, or both. Use whichever you already have.'],
 ['Does my computer need to be on?', 'Yes. Leave your computer on and signed into Amazon overnight.'],
 ['Can I approve things first?', 'Yes. It runs automatically by default, and you can switch on approvals to OK each look before it goes out. I recommend approvals on for your first few days.'],
 ['What if I only have a few minutes?', 'Do the 15-minute Quick Start and go to bed. That’s the whole job.'],
 ['Is this a PDF?', 'No. It’s a website you get access to, so it can be updated as things change.']
];
