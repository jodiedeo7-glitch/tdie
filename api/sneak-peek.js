import fs from "fs";
import path from "path";
import { sign, check } from "./verify.js";

// Pretty & Paid PLR Vault™ sneak peek.
// The PDF lives in api/_content (bundled via vercel.json includeFiles), not public/,
// so it has no public URL. It is only ever streamed from this handler against a
// signed, 30-day token that is issued after the email has landed in MailerLite.

const ML_KEY = process.env.MAILERLITE_API_KEY;
const ML_GROUP = process.env.MAILERLITE_SNEAKPEEK_GROUP_ID;
const FILE = path.join(process.cwd(), "api", "_content", "pretty-and-paid-plr-vault-sneak-peek.pdf");

export default async function handler(req, res) {
  // GET /api/sneak-peek?t=<token>  → the PDF
  if (req.method === "GET") {
    const token = String(req.query?.t || "");
    if (!check(token)) return res.status(401).send("This link has expired. Enter your email again to get a fresh one.");
    if (!fs.existsSync(FILE)) return res.status(404).send("Not found");
    res.setHeader("Content-Type", "application/pdf");
    res.setHeader("Content-Disposition", 'inline; filename="Pretty-and-Paid-PLR-Vault-Sneak-Peek.pdf"');
    res.setHeader("Cache-Control", "private, no-store");
    res.setHeader("X-Robots-Tag", "noindex, nofollow");
    return res.status(200).send(fs.readFileSync(FILE));
  }

  // POST { email }  → subscribe, then return a signed download token
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
        groups: ML_GROUP ? [ML_GROUP] : undefined,
      }),
    });
    if (!r.ok) return res.status(500).json({ error: "Couldn't add you just now. Try again in a moment." });
    return res.status(200).json({ url: `/api/sneak-peek?t=${sign(email)}` });
  } catch {
    return res.status(500).json({ error: "Couldn't add you just now. Try again in a moment." });
  }
}
