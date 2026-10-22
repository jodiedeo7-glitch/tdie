// Real, attributable member reviews only. Nothing goes in this file that a
// real person did not write under their own name on a platform we can point to.
// Quotes are verbatim, typos and all -- fix nothing, not even a product name.
// See claude/TDIE_TESTIMONIAL_BANK.md, Rule 2.

export const REVIEWS = [
  {
    id: "tina-alexander",
    name: "Tina Alexander",
    url: "https://digitalblogtips.com",
    linkLabel: "digitalblogtips.com",
    stars: 5,
    source: "Skool review \u00b7 public, posted with her name and photo",
    tenure: "Paying member, 4 months",
    date: "2026-09",
    // The full quote, verbatim -- her exact spelling of "word press", unfixed.
    quote:
      "After spending a couple of months on word press, I decided to purchase The Weekend Ecosystem and WOW! In 3 days I had a beautiful website/blog set up and everything connected and looks way better than the word press site would have looked. If you're wanting to start your website/blog this is highly recommended by me!",
    // A shorter cut of the same words, for tight spaces. No new wording.
    pull:
      "In 3 days I had a beautiful website/blog set up and everything connected and looks way better than the word press site would have looked.",
    // The shortest true cut, for a one-line strip.
    line: "In 3 days I had a beautiful website/blog set up and everything connected.",
  },
  {
    id: "tina-alexander-community",
    name: "Tina Alexander",
    url: "https://digitalblogtips.com",
    linkLabel: "digitalblogtips.com",
    source: "said in The Digital Income Edit™ community, unprompted",
    tenure: "Membership Premium member",
    // An unprompted community comment, not a star-rated platform review.
    quote:
      "I ordered your The weekend Ecosystem and I finished it yesterday and love how my website turned out. I struggled with Wordpress for a few months and in 3 days I have something that is way better than that would ever be!",
  },
];

export const FEATURED = REVIEWS[0];

// Member reviews and community wall posts (pulled from the Skool group 12 Oct 2026).
// Verbatim, typos and all. `about` says which product the words are about, so each
// bubble sits beside that product.
export const MEMBER_REVIEWS = [
  {
    id: "brittany-miller-skool",
    name: "Brittany Miller",
    stars: 5,
    about: "membership",
    source: "Skool review",
    quote: "Amazing guidance, content is super easy to follow, super supportive group! This is the best plan to follow BY FAR!",
  },
  {
    id: "cristal-vancarson-brand-bible",
    name: "Cristal Vancarson",
    about: "membership",
    source: "on the Brand Bible lesson",
    quote: "Today I completed my Brand Bible lesson, and wow... this exercise gave me so much clarity.",
  },
  {
    id: "suriya-taylor-prompts",
    name: "Suriya Taylor",
    about: "daily-prompts",
    source: "on the daily prompts",
    quote: "Why do I love these so much?? Thank you for the prompts, Jodie.",
  },
  {
    id: "dee-free-tier",
    name: "Dee MamaswithMissions",
    about: "membership",
    center: true,
    source: "Standard Member",
    quote: "For a free community, there's a surprising amount of value here. ❤️",
  },
];
