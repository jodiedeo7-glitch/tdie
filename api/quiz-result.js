// Find Your Door — quiz results → MailerLite.
//
// GET  /api/quiz-result            → { live: boolean }  (whether the subscribe form can reach MailerLite)
// POST /api/quiz-result { email, name, door, stage, goal, stuck, fear, reframe, first_move, time, hp }
//
// What it does on POST:
//   1. Makes sure the quiz_* custom fields exist (creates any that are missing).
//   2. Finds or creates the five "Quiz — <door>" groups.
//   3. Upserts the subscriber with their answers in those fields and adds them to their door's group.
//   4. Removes them from the other four quiz groups, so a retake leaves them in one door only.
// Nothing is emailed from here. The quiz result stays on the page; this is a list signup
// carrying the door, so a MailerLite automation on a quiz group can pick it up later.
//
// Env: MAILERLITE_API_KEY (already set for the other functions)

const ML = "https://connect.mailerlite.com/api";
const KEY = process.env.MAILERLITE_API_KEY;

const GROUPS = {
  S: "Quiz — Membership Standard",
  P: "Quiz — Membership Premium",
  V: "Quiz — Pretty & Paid PLR Vault",
  W: "Quiz — The Weekend Ecosystem",
  K: "Quiz — Earn With Skool",
};
const DOOR_NAMES = {
  S: "Membership Standard",
  P: "Membership Premium",
  V: "Pretty & Paid PLR Vault™",
  W: "The Weekend Ecosystem™",
  K: "Earn With Skool (SCC)",
};
const FIELDS = ["quiz_door", "quiz_stage", "quiz_goal", "quiz_stuck", "quiz_fear", "quiz_reframe", "quiz_first_move", "quiz_time"];

let fieldsReady = false;
const groupIds = {};

function ml(path, opts = {}) {
  return fetch(`${ML}${path}`, {
    ...opts,
    headers: {
      Authorization: `Bearer ${KEY}`,
      "Content-Type": "application/json",
      Accept: "application/json",
    },
  });
}

async function ensureFields() {
  if (fieldsReady) return;
  const r = await ml("/fields?limit=100");
  if (!r.ok) throw new Error("fields list failed");
  const have = new Set(((await r.json()).data || []).map((f) => f.key));
  for (const key of FIELDS) {
    if (have.has(key)) continue;
    const c = await ml("/fields", { method: "POST", body: JSON.stringify({ name: key, type: "text" }) });
    if (!c.ok) throw new Error(`field create failed: ${key}`);
  }
  fieldsReady = true;
}

async function groupId(door) {
  if (groupIds[door]) return groupIds[door];
  const name = GROUPS[door];
  const r = await ml(`/groups?limit=50&filter[name]=${encodeURIComponent(name)}`);
  if (!r.ok) throw new Error("groups list failed");
  const hit = ((await r.json()).data || []).find((g) => g.name === name);
  if (hit) return (groupIds[door] = hit.id);
  const c = await ml("/groups", { method: "POST", body: JSON.stringify({ name }) });
  if (!c.ok) throw new Error("group create failed");
  return (groupIds[door] = (await c.json()).data.id);
}

const clean = (v, max = 250) => String(v ?? "").replace(/\s+/g, " ").trim().slice(0, max);

export default async function handler(req, res) {
  if (req.method === "GET") return res.status(200).json({ live: Boolean(KEY) });
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });
  if (!KEY) return res.status(503).json({ error: "Email results aren't switched on yet." });

  const b = req.body || {};
  if (b.hp) return res.status(200).json({ ok: true }); // honeypot: quietly accept, do nothing

  const email = clean(b.email, 200).toLowerCase();
  const door = String(b.door || "");
  if (!email || !/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) {
    return res.status(400).json({ error: "Enter a valid email address." });
  }
  if (!GROUPS[door]) return res.status(400).json({ error: "Take the quiz first, then send your results." });

  try {
    await ensureFields();
    const target = await groupId(door);

    const fields = {
      quiz_door: DOOR_NAMES[door],
      quiz_stage: clean(b.stage),
      quiz_goal: clean(b.goal),
      quiz_stuck: clean(b.stuck),
      quiz_fear: clean(b.fear),
      quiz_reframe: clean(b.reframe),
      quiz_first_move: clean(b.first_move),
      quiz_time: clean(b.time),
    };
    const name = clean(b.name, 60);
    if (name) fields.name = name;

    const r = await ml("/subscribers", {
      method: "POST",
      body: JSON.stringify({ email, fields, groups: [target] }),
    });
    if (!r.ok) return res.status(500).json({ error: "Couldn't send that just now. Try again in a moment." });
    const sub = (await r.json()).data;

    // One door at a time: take them out of the other quiz groups.
    for (const d of Object.keys(GROUPS)) {
      if (d === door) continue;
      const id = await groupId(d);
      await ml(`/subscribers/${sub.id}/groups/${id}`, { method: "DELETE" }).catch(() => {});
    }

    return res.status(200).json({ ok: true });
  } catch {
    return res.status(500).json({ error: "Couldn't send that just now. Try again in a moment." });
  }
}
