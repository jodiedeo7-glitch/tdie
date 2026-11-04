import fs from "fs";
import path from "path";
import { check } from "./verify.js";

export default async function handler(req, res) {
  if (req.method !== "POST") return res.status(405).json({ error: "Method not allowed" });

  const token = req.body?.token || "";
  const slug = String(req.body?.slug || "");

  if (!check(token)) return res.status(401).json({ error: "unauthorized" });
  if (!/^[a-z0-9-]+$/.test(slug)) return res.status(400).json({ error: "bad slug" });

  const file = path.join(process.cwd(), "api", "_content", `${slug}.html`);
  if (!fs.existsSync(file)) return res.status(404).json({ error: "not found" });

  res.setHeader("Cache-Control", "no-store");
  return res.status(200).json({ html: fs.readFileSync(file, "utf8") });
}
