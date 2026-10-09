// Shared presentation records. Examples are authorized existing Lifestyle
// photographs, not retail photography or evidence of customer automation.
import entryBasic from '../lifestyle/pretty-wicked-entryway-basic.png';
import entryStyled from '../lifestyle/pretty-wicked-entryway-styled.png';
import entryLife from '../lifestyle/pretty-wicked-entryway-lifestyle.png';
import coffeeBasic from '../lifestyle/ghoul-fuel-coffee-bar-basic.png';
import coffeeStyled from '../lifestyle/ghoul-fuel-coffee-bar-styled.png';
import coffeeLife from '../lifestyle/ghoul-fuel-coffee-bar-lifestyle.png';
export const WYS_ROOT = '/shop/while-you-sleep-storefront';
export const WYS_HOLD = true;
export const examples = [
 {slug:'pretty-wicked-entryway',name:'Pretty Wicked',category:'Pink Halloween entryway',photos:[
  {role:'The finds',src:entryBasic,alt:'Hot-pink pumpkins, pink gauze, bat shapes and small pink lights arranged on a dark tabletop',caption:'Start with the selected pieces, photographed as a complete flat lay.'},
  {role:'Pink Halloween entryway',src:entryStyled,alt:'A Halloween console with pink pumpkins and lights, black bats and a large oval mirror',caption:'See how those pieces come together in a styled entryway.'},
  {role:'Tommy Kate at the door',src:entryLife,alt:'Tommy Kate answers the open front door from the porch viewpoint, with the Halloween console receding inside',caption:'A new viewpoint and a natural moment: answering the door on Halloween.'}
 ]},
 {slug:'ghoul-fuel-coffee-bar',name:'Ghoul Fuel',category:'Pink Halloween coffee bar',photos:[
  {role:'The finds',src:coffeeBasic,alt:'A pink ghost mug, heart serving stand, small velvet pumpkins, mirrored balls and LED tea lights in an overhead flat lay',caption:'The five selected product types, with styling extras kept separate.'},
  {role:'Pink Halloween coffee bar',src:coffeeStyled,alt:'Pink Halloween coffee nook with a ghost mug, two-tier heart stand, small pumpkins and silver mirror balls',caption:'The no-person styled scene shows the coffee corner in use.'},
  {role:'Coffee with Tommy Kate',src:coffeeLife,alt:'Tommy Kate in a lavender cardigan holds and stirs one pink ghost mug beside the styled coffee counter',caption:'A separately composed moment: stirring one mug beside the coffee nook.'}
 ]}
];
export const imageNotice='AI-generated styling inspiration. Retail products may differ; check the actual listing photographs, contents and measurements. Flowers, furniture, artwork, clothing and other props are styling extras.';
export const contents=[
 {n:'01',title:'Preparation Guide',text:'Work through the account requirements and choose the path that fits your setup.'},
 {n:'02',title:'Setup Guide',text:'Record your business choices, connect the tools you have and see which setup steps still need attention.'},
 {n:'03',title:'Themed look recipe',text:'Follow the selected products through three styling views, an article and social content for your chosen theme and season.'},
 {n:'04',title:'Recurring task prompts',text:'Weekly planning, optional Outfit of the Day, and reconciliation prompts. Tasks stay paused until the required tests pass.'},
 {n:'05',title:'Your destination path',text:'Influencer Idea Lists or an Associates-only page on your own site, according to your actual account access.'},
 {n:'06',title:'Optional Brand Closet path',text:'For customers with the required membership and authorized lesson access. Member-only material stays private.'}
];
