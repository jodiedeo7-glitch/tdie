// src/pages/rss.xml.js
// Generates /rss.xml from the live article files in src/pages/learn/.
// Reads title + description straight from each article's <ArticleLayout> props,
// so the feed never drifts from what's on the page. Publish dates come from
// src/data/article-dates.js. No content collection required.

import rss from "@astrojs/rss";
import { ARTICLE_DATES, FALLBACK_DATE } from "../data/article-dates.js";

const SITE = "https://learn.thedigitalincomeedit.com";

// Pull the value of a prop written as name="..." from the article source.
function prop(source, name) {
  const m = source.match(new RegExp(`${name}\\s*=\\s*"([^"]*)"`));
  return m ? m[1] : null;
}

export async function GET(context) {
  // Grab every article in src/pages/learn/ except the index.
  const files = import.meta.glob("./learn/*.astro", {
    query: "?raw",
    import: "default",
    eager: true,
  });

  const items = [];
  for (const [path, source] of Object.entries(files)) {
    const slug = path.split("/").pop().replace(/\.astro$/, "");
    if (slug === "index") continue;

    const title = prop(source, "title");
    const description = prop(source, "description");
    if (!title) continue; // skip anything without a title prop

    const dateStr = ARTICLE_DATES[slug] || FALLBACK_DATE;

    items.push({
      title,
      description: description || "",
      link: `${SITE}/learn/${slug}`,
      pubDate: new Date(`${dateStr}T09:00:00-05:00`),
      categories: prop(source, "category") ? [prop(source, "category")] : [],
    });
  }

  // Newest first.
  items.sort((a, b) => b.pubDate - a.pubDate);

  return rss({
    title: "The Digital Income Edit™ — The Library",
    description:
      "New guides on building faceless digital income — AI, Pinterest, digital products, and automation for a business of one.",
    site: context.site || SITE,
    items,
    customData: `<language>en-us</language>`,
  });
}
