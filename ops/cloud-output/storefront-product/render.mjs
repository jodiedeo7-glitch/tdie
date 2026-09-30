// Rebuild the revised guide and kit. Requires Python with reportlab.
import { spawnSync } from "node:child_process";
import { fileURLToPath } from "node:url";
const p=spawnSync(process.env.PYTHON || "python",[fileURLToPath(new URL("./build_guide.py",import.meta.url))],{stdio:"inherit"});
if(p.error) throw p.error;
process.exit(p.status ?? 1);
