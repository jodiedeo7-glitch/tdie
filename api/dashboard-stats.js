// Read-only stats feed for the TDIE Business Command Centre.
//
// Returns MailerLite list sizes and the published article list so the dashboard
// stops being typed in by hand. No subscriber data, no email addresses, no PII —
// counts, titles and slugs only.
//
// Response shape is the contract the Command Centre reads:
//   { generated_at, mailerlite: { subscribers, groups: {...} }, articles: [ {slug,title,pub,url} ] }
//
// Environment (Vercel project settings, never committed):
//   MAILERLITE_API_KEY              required
//   MAILERLITE_GROUP_ID             buyers
//   MAILERLITE_WAITLIST_GROUP_ID    waitlist
//   MAILERLITE_COMPLETED_GROUP_ID   completed the course
//   DASHBOARD_TOKEN                 optional. If set, the request must send
//                                   ?token=... or the endpoint returns 401.

const ML_KEY = process.env.MAILERLITE_API_KEY;
const DASHBOARD_TOKEN = process.env.DASHBOARD_TOKEN;

const GROUPS = {
  buyers: process.env.MAILERLITE_GROUP_ID || "195477643940857421",
  waitlist: process.env.MAILERLITE_WAITLIST_GROUP_ID || "195486362374244004",
  completed: process.env.MAILERLITE_COMPLETED_GROUP_ID || "195481306388236010",
};

const SITE = "https://www.thedigitalincomeedit.com";

const ml = (path) =>
  fetch(`https://connect.mailerlite.com/api/${path}`, {
    headers: { Authorization: `Bearer ${ML_KEY}`, Accept: "application/json" },
  });

async function mailerlite() {
  if (!ML_KEY) return { error: "MAILERLITE_API_KEY is not set" };

  const [gRes, sRes] = await Promise.all([
    ml("groups?limit=100"),
    ml("subscribers?limit=1&filter[status]=active"),
  ]);

  if (!gRes.ok) return { error: `MailerLite groups returned ${gRes.status}` };

  const gBody = await gRes.json();
  const rows = Array.isArray(gBody?.data) ? gBody.data : [];
  const byId = new Map(rows.map((g) => [String(g.id), g]));

  const groups = {};
  for (const [label, id] of Object.entries(GROUPS)) {
    const g = byId.get(String(id));
    groups[label] = g
      ? {
          id: String(id),
          name: g.name ?? null,
          active: Number(g.active_count ?? 0),
          unsubscribed: Number(g.unsubscribed_count ?? 0),
          unconfirmed: Number(g.unconfirmed_count ?? 0),
        }
      : { id: String(id), active: 0, error: "group not found on this account" };
  }

  // Unique active subscribers across the whole account. Falls back to the sum of
  // group counts, which double-counts anyone in more than one group.
  let subscribers = null;
  if (sRes.ok) {
    const sBody = await sRes.json().catch(() => null);
    const total = sBody?.meta?.total ?? sBody?.total ?? null;
    if (typeof total === "number") subscribers = total;
  }
  const groupSum = rows.reduce((a, g) => a + Number(g.active_count ?? 0), 0);
  if (subscribers === null) subscribers = groupSum;

  return {
    subscribers,
    buyers: groups.buyers?.active ?? 0,
    waitlist: groups.waitlist?.active ?? 0,
    completed: groups.completed?.active ?? 0,
    groups,
    group_count: rows.length,
    group_active_sum: groupSum,
    subscribers_is_unique: subscribers !== groupSum,
  };
}

function textBetween(xml, tag) {
  const m = xml.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`, "i"));
  if (!m) return null;
  return m[1].replace(/^<!\[CDATA\[/, "").replace(/\]\]>$/, "").trim();
}

function decode(s) {
  if (!s) return s;
  return s
    .replace(/&apos;/g, "'")
    .replace(/&quot;/g, '"')
    .replace(/&#39;/g, "'")
    .replace(/&amp;/g, "&")
    .replace(/&lt;/g, "<")
    .replace(/&gt;/g, ">");
}

async function articles() {
  const r = await fetch(`${SITE}/rss.xml`, {
    headers: { Accept: "application/rss+xml, application/xml, text/xml" },
  });
  if (!r.ok) throw new Error(`rss.xml returned ${r.status}`);

  const xml = await r.text();
  return xml
    .split(/<item[\s>]/i)
    .slice(1)
    .map((chunk) => {
      const block = chunk.split(/<\/item>/i)[0];
      const url = textBetween(block, "link") || "";
      const slug = (url.split("/learn/")[1] || url.split("/").filter(Boolean).pop() || "")
        .replace(/\/$/, "");
      const pubDate = textBetween(block, "pubDate");
      const d = pubDate ? new Date(pubDate) : null;
      return {
        slug,
        title: decode(textBetween(block, "title")),
        pub: d && !isNaN(d) ? d.toISOString().slice(0, 10) : null,
        url,
      };
    })
    .filter((a) => a.slug);
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.setHeader("Access-Control-Allow-Headers", "Accept, Content-Type");
  res.setHeader("Cache-Control", "s-maxage=300, stale-while-revalidate=600");

  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "GET") return res.status(405).json({ error: "Method not allowed" });

  if (DASHBOARD_TOKEN) {
    const sent = String(req.query?.token || "");
    if (sent !== DASHBOARD_TOKEN) return res.status(401).json({ error: "unauthorized" });
  }

  const [mlOut, artOut] = await Promise.all([
    mailerlite().catch((e) => ({ error: String(e?.message || e) })),
    articles().catch(() => null),
  ]);

  return res.status(200).json({
    generated_at: new Date().toISOString(),
    mailerlite: mlOut,
    articles: Array.isArray(artOut) ? artOut : [],
    article_count: Array.isArray(artOut) ? artOut.length : 0,
    articles_error: artOut ? null : "could not read rss.xml",
  });
}
