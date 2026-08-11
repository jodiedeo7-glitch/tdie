const ML_KEY = process.env.MAILERLITE_API_KEY;
const ML_WAITLIST_GROUP = process.env.MAILERLITE_WAITLIST_GROUP_ID;

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const email = String(req.body?.email || "").trim().toLowerCase();
  if (!email || !email.includes("@") || email.length > 200) {
    return res.status(400).json({ error: "Enter a valid email address." });
  }

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
        groups: ML_WAITLIST_GROUP ? [ML_WAITLIST_GROUP] : undefined,
      }),
    });

    if (!r.ok) return res.status(500).json({ error: "Couldn't add you just now. Try again in a moment." });
    return res.status(200).json({ ok: true });
  } catch {
    return res.status(500).json({ error: "Couldn't add you just now. Try again in a moment." });
  }
}
