# Lifestyle looks

One look = one JSON file here plus its images in this same folder. The build turns them into /lifestyle pages automatically. Added by the Legally Blonde pin tasks after pins are scheduled (recipe: project doc claude/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md, section 8c).

File name: `<slug>.json`, images `<slug>-flatlay.jpg` and `<slug>-lifestyle.jpg` (web size, 1000 by 1500, JPEG quality 82).

```json
{
  "slug": "pink-suit-law-student-halloween-costume",
  "title": "The Pink Suit Law Student Costume",
  "date": "2026-09-24",
  "category": "clothing",
  "season": "Halloween",
  "intro": "Two or three sentences in Jodie's site voice. No prices.",
  "images": [
    { "file": "pink-suit-law-student-halloween-costume-flatlay.jpg", "alt": "Plain description of the image" },
    { "file": "pink-suit-law-student-halloween-costume-lifestyle.jpg", "alt": "Plain description of the image" }
  ],
  "ideaList": "https://www.amazon.com/shop/<handle>/list/<id>",
  "items": [
    { "name": "Pink tweed blazer", "link": "https://amzn.to/xxxx", "note": "optional one-liner" }
  ]
}
```

category is one of: clothing, accessories, jewelry, beauty, perfume, home-decor, dorm, car, books, gifts. A look with no images or no items is skipped by the build. Slugs must never equal a category name.

Optional fields (Holiday Gift Guides, 26 Sep 2026):

- `"draft": true` keeps a look off the site even when its files are complete. Remove it to publish.
- `"giftGuide": true` puts the look in the Holiday Gift Guides block on /lifestyle, ordered by `"guide"` (a number), with `"label"` as its short name on the chips and cards. Gift guide pages show no prices anywhere, including the Membership card.

The 25 holiday gift guide looks, their image prompts, pins and Instagram posts are in `claude/HOLIDAY_GIFT_GUIDES_BUILD.md`. Their links go in `claude/HOLIDAY_GIFT_GUIDES_LINKS.md` first.
