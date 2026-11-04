import crypto from "crypto";

const SECRET = process.env.ACCESS_SECRET;
const ML_KEY = process.env.MAILERLITE_API_KEY;
const ML_GROUP = process.env.MAILERLITE_GROUP_ID;
const TTL_DAYS = 30;

export function sign(email) {
  const exp = Date.now() + TTL_DAYS * 86400000;
  const payload = `${email.toLowerCase()}|${exp}`;
  const sig = crypto.createHmac("sha256", SECRET).update(payload).digest("hex");
  return Buffer.from(`${payload}|${sig}`).toString("base64url");
}

export function check(token) {
  try {
    const [email, exp, sig] = Buffer.from(token, "base64url").toString().split("|");
    const expect = crypto.createHmac("sha256", SECRET).update(`${email}|${exp}`).digest("hex");
    if (!crypto.timingSafeEqual(Buffer.from(sig), Buffer.from(expect))) return null;
    if (Date.now() > Number(exp)) return null;
    return email;
  } catch {
    return null;
  }
}

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const email = (req.body?.email || "").trim().toLowerCase();
  if (!email || !email.includes("@")) {
    return res.status(400).json({ error: "Enter a valid email address." });
  }

  try {
    const r = await fetch(
      `https://connect.mailerlite.com/api/subscribers/${encodeURIComponent(email)}`,
      { headers: { Authorization: `Bearer ${ML_KEY}`, Accept: "application/json" } }
    );

    if (r.status === 404) {
      return res.status(403).json({
        error: "We can't find that email. Use the address you purchased with.",
      });
    }
    if (!r.ok) return res.status(500).json({ error: "Verification is temporarily unavailable." });

    const data = await r.json();
    const groups = data?.data?.groups || [];
    const ok = groups.some((g) => String(g.id) === String(ML_GROUP));

    if (!ok) {
      return res.status(403).json({
        error: "That email isn't registered for this course. Use the address you purchased with.",
      });
    }

    return res.status(200).json({ token: sign(email) });
  } catch {
    return res.status(500).json({ error: "Verification is temporarily unavailable." });
  }
}
