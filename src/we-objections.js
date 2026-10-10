// The six objections, in the order of the objection email series
// (canon.json -> emails.weekend_ecosystem_objection_series). One source for the
// sales page and the preview page. Every answer uses only facts already on the
// sales page or in canon: no guarantee, no refund window, no income claim.
// `short` is the preview page's one-paragraph version of the same answer.

export const OBJECTIONS = [
  {
    n: 1,
    id: "cant-build",
    q: "I can't build a website.",
    a: [
      "You won't build it the way you're picturing. Claude writes every file your site needs. You paste the prompt, read what came back, and say yes or say what to change.",
      "When something breaks, the deploy tells you in plain English and you paste that back. The course assumes you have never opened a code editor. I hadn't, when I built this site.",
    ],
    short: "Claude writes every file. You paste the prompt, read what came back, and say yes or say what to change. The course assumes you have never opened a code editor.",
  },
  {
    n: 2,
    id: "no-weekend",
    q: "I don't have a free weekend.",
    a: [
      "You don't need one. It's sixteen hours in six chunks: two on Friday night, nine on Saturday, five on Sunday.",
      "Or spread the same six chunks across three weeks of evenings. The modules don't expire and neither does your access.",
    ],
    short: "Sixteen hours in six chunks. Do it in one weekend or across three weeks of evenings. The modules don't expire and neither does your access.",
  },
  {
    n: 3,
    id: "too-expensive",
    q: "$97 is a lot right now.",
    a: [
      "Then split it. Three payments of $33.33 gets you all of it: every module, every prompt, every vault, every future update. Both options are at checkout.",
      "After that, the site itself costs about a dollar a month to run, plus your domain at $10 to $15 a year. No monthly site-builder bill.",
    ],
    short: "Split it: three payments of $33.33 gets you all of it. After that the site costs about a dollar a month to run, plus your domain.",
  },
  {
    n: 4,
    id: "no-refunds",
    q: "What if it isn't what I think?",
    a: [
      "Then look first. The look inside shows the real interface, a real module, the prompt cards, the tracker and the certificate. No email, no card. Read it properly, decide properly, then buy.",
      "That's exactly why the look inside exists. The real interface, a real module, the prompt cards, the tracker and the certificate. No email, no card. Read it properly, decide properly, then buy.",
    ],
    short: "There are no refunds. None. That's why this page exists: read it properly, decide properly, then buy.",
    preview: true,
  },
  {
    n: 5,
    id: "not-enough-content",
    q: "I don't have enough content. I'm not a coach.",
    a: [
      "You need content, not authority. Skool lessons, community posts, call recordings, PDFs, the products you already sell, the DM where you explained your whole method to one person at midnight. Module 1 walks you through finding all of it and putting it in one table.",
      "If you truly have nothing written yet, this isn't for you yet. It builds from what you've already made.",
    ],
    short: "You need content, not authority. Lessons, posts, calls, PDFs and products all count, and Module 1 walks you through finding them. Nothing written yet? Then it isn't for you yet.",
  },
  {
    n: 6,
    id: "later",
    q: "I'll do it later.",
    a: [
      "Later is another month of your best writing sitting where nobody can search it. $97 isn't a launch price you're waiting out. It's the permanent price.",
    ],
    short: "Later is another month of your best writing sitting where nobody can search it. $97 is the permanent price, not a launch price to wait out.",
    kit: true,
  },
];
