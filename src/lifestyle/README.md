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
