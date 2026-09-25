# src/ig — the Instagram link-in-bio page (/ig)

Instagram posts can't carry links, so every @the.faceless.homestead.mama post points to the link in bio, and the bio link is https://www.thedigitalincomeedit.com/ig.

One JSON file per Instagram post, named `YYYY-MM-DD.json` (the date it goes live), added by the scheduled task "TDIE: DFY calendar post maker". Nothing here is written by hand.

```json
{
  "date": "2026-10-01",
  "title": "The free 5-day challenge",
  "blurb": "The one from today's post. Five emails, one small build a day.",
  "cta": "Start the free challenge",
  "url": "https://www.thedigitalincomeedit.com/resources/weekend-build-challenge",
  "affiliate": false
}
```

Rules: `url` must be a row in canon.json products[] or key_pages, never invented. `affiliate: true` adds the disclosure line and rel="sponsored". No income claims. A post with a date later than today (New York time) stays hidden until its day.
