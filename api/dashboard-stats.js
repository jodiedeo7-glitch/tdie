// Read-only stats feed for the TDIE Business Command Centre.
//
// Returns MailerLite list sizes and the published article list so the dashboard
// stops being typed in by hand. No subscriber data, no email addresses, no PII —
// counts and article titles only.
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

async function mailerliteGroups() {
  if (!ML_KEY) return { error: "MAILERLITE_API_KEY is not set" };

  const r = await fetch("https://connect.mailerlite.com/api/groups?limit=100", {
    headers: {
      Authorization: `Bearer ${ML_KEY}`,
      Accept: "application/json",
    },
  });

  if (!r.ok) return { error: `MailerLite returned ${r.status}` };

  const body = await r.json();
  const rows = Array.isArray(body?.data) ? body.data : [];
  const byId = new Map(rows.map((g) => [String(g.id), g]));

  const out = {};
  for (const [label, id] of Object.entries(GROUPS)) {
    const g = byId.get(String(id));
    out[label] = g
      ? {
          id: String(id),
          name: g.name ?? null,
          active: Number(g.active_count ?? 0),
          unsubscribed: Number(g.unsubscribed_count ?? 0),
          unconfirmed: Number(g.unconfirmed_count ?? 0),
        }
      : { id: String(id), error: "group not found on this account" };
  }

  // Total list size across the account, not just these three groups.
  const totalRow = rows.reduce((a, g) => a + Number(g.active_count ?? 0), 0);
  return { groups: out, all_groups_active_sum: totalRow, group_count: rows.length };
}

function textBetween(xml, tag) {
  const m = xml.match(new RegExp(`<${tag}[^>]*>([\\s\\S]*?)</${tag}>`, "i"));
  if (!m) return null;
  return m[1]
    .replace(/^<!\[CDATA\[/, "")
    .replace(/\]\]>$/, "")
    .trim();
}

async function articles() {
  const r = await fetch(`${SITE}/rss.xml`, {
    headers: { Accept: "application/rss+xml, application/xml, text/xml" },
  });
  if (!r.ok) return { error: `rss.xml returned ${r.status}` };

  const xml = await r.text();
  const items = xml.split(/<item[\s>]/i).slice(1);

  const list = items.map((chunk) => {
    const block = chunk.split(/<\/item>/i)[0];
    return {
      title: textBetween(block, "title"),
      url: textBetween(block, "link"),
      published: textBetween(block, "pubDate"),
    };
  });

  return { count: list.length, items: list };
}

export default async function handler(req, res) {
  res.setHeader("Access-Control-Allow-Origin", "*");
  res.setHeader("Access-Control-Allow-Methods", "GET, OPTIONS");
  res.setHeader("Cache-Control", "s-maxage=300, stale-while-revalidate=600");

  if (req.method === "OPTIONS") return res.status(204).end();
  if (req.method !== "GET") return res.status(405).json({ error: "Method not allowed" });

  if (DASHBOARD_TOKEN) {
    const sent = String(req.query?.token || "");
    if (sent !== DASHBOARD_TOKEN) return res.status(401).json({ error: "unauthorized" });
  }

  const [email, learn] = await Promise.all([
    mailerliteGroups().catch((e) => ({ error: String(e?.message || e) })),
    articles().catch((e) => ({ error: String(e?.message || e) })),
  ]);

  return res.status(200).json({
    generated_at: new Date().toISOString(),
    email,
    articles: learn,
  });
}
