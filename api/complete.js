import { check } from "./verify.js";

const ML_KEY = process.env.MAILERLITE_API_KEY;
const ML_DONE_GROUP = process.env.MAILERLITE_COMPLETED_GROUP_ID;

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const email = check(req.body?.token || "");
  if (!email) return res.status(401).json({ error: "unauthorized" });

  const name = String(req.body?.name || "").trim().slice(0, 80);
  const completed = new Date().toISOString().slice(0, 10);

  try {
    const r = await fetch("https://connect.mailerlite.com/api/subscribers", {
      method: "POST",
      headers: {
        Authorization: `Bearer ${ML_KEY}`,
        "Content-Type": "application/json",
        Accept: "application/json",
      },
      body: JSON.stringify({
        email,
        groups: ML_DONE_GROUP ? [ML_DONE_GROUP] : undefined,
        fields: {
          we_completed_on: completed,
          we_certificate_name: name || null,
        },
      }),
    });

    if (!r.ok) return res.status(500).json({ error: "could not record completion" });
    return res.status(200).json({ ok: true });
  } catch {
    return res.status(500).json({ error: "could not record completion" });
  }
}
