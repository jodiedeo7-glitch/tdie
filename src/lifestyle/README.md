# Lifestyle looks (founder storefront, schema wys-founder-1)

Rebuilt 7 October 2026. One look = one JSON file here plus its two founder pin images in this same folder. The build turns them into `/lifestyle/<slug>` pages, the department pages and the hub automatically. The only writer is the founder pin factory (recipe: `ops/cloud-kit/TDIE_LEGALLY_BLONDE_PIN_FACTORY.md`, section 8c). Nothing here is written by hand.

Files per look:
- `<slug>.json`
- `<slug>-pin1.jpg`: the look's final approved Pin 1 (the person-free flat lay, exactly as scheduled, generated headline included)
- `<slug>-pin2.jpg`: the look's final approved Pin 2 (Tommy Kate wearing the pieces for outfit looks; the other flat lay format for theme lists)

Images are portrait 2:3, 1000 by 1500, JPEG quality 82 (.png and .webp also accepted, matched by name without the extension).

```json
{
  "schema": "wys-founder-1",
  "slug": "pink-witch-halloween-costume",
  "title": "The Pink Witch Halloween Costume",
  "date": "2026-10-01",
  "category": "clothing",
  "season": "Halloween",
  "intro": "80 to 150 words in Jodie's site voice. No prices. No em dashes.",
  "images": [
    { "file": "pink-witch-halloween-costume-pin1.jpg", "alt": "Pin 1 alt text", "persona": false },
    { "file": "pink-witch-halloween-costume-pin2.jpg", "alt": "Pin 2 alt text", "persona": true }
  ],
  "listLink": "https://www.amazon.com/shop/thedigitalincomeedit/list/1YYCBMZFG52HX",
  "items": [
    { "name": "Soft pink velvet witch hat", "link": "https://link.amazon/B06YRDn0t", "note": "optional one-liner" }
  ]
}
```

Rules:
- `category` is one of: clothing, accessories, jewelry, beauty, perfume, home-decor, dorm, car, books, gifts. Never a new one.
- `slug` is the look name, lowercase words joined by hyphens, no dates, 60 characters at most, never a category name, never a slug already used.
- `season` is the season or holiday ("Halloween", "Fall") or "Evergreen".
- `persona` is true only on an image that shows Tommy Kate.
- Item names describe the piece, never the brand. Every link is Jodie's own SiteStripe short link; every link's destination must be the product named.
- No prices anywhere.
- Run `python3 ops/scripts/validate_lifestyle.py` and get "OK" before uploading. Images go up first, then the JSON.

Retired: the 24 September to 3 October layout (`ideaList`, `-flatlay` / `-lifestyle` images, no `schema`). The build skips any such file and the validator fails it.
