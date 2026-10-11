// Skool About gallery, final set (11 Oct 2026): five 1600x900 graphics.
// Approved build: ops/cloud-kit/TDIE_DESIGN_RULES.md §2 + THE LOOK (Decision 128).
// Copy: ops/cloud-output/SKOOL_ABOUT_CONVERSION_AUDIT.md (G9 Roadmap copy is Jodie's, word for word).
//
// Run from the repo root:  node ops/cloud-output/about-gallery-2026-10/render.mjs [name ...]
// Needs Playwright (global install is fine). Fonts are Newsreader 600 + Inter, from @fontsource
// on jsdelivr, cached in ./fonts (not committed). Photos live in ./photos (generated on
// Higgsfield Nano Banana Pro 2K from the avatar seed, 11 Oct 2026).

import { existsSync, mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright")); }

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, "out");
const FONTS = join(HERE, "fonts");
mkdirSync(OUT, { recursive: true });
mkdirSync(FONTS, { recursive: true });

const FONT_FILES = {
  "newsreader-600.woff2": "newsreader/files/newsreader-latin-600-normal.woff2",
  "inter-400.woff2": "inter/files/inter-latin-400-normal.woff2",
  "inter-500.woff2": "inter/files/inter-latin-500-normal.woff2",
  "inter-600.woff2": "inter/files/inter-latin-600-normal.woff2",
  "inter-700.woff2": "inter/files/inter-latin-700-normal.woff2",
  "inter-800.woff2": "inter/files/inter-latin-800-normal.woff2",
};
for (const [name, path] of Object.entries(FONT_FILES)) {
  const p = join(FONTS, name);
  if (existsSync(p)) continue;
  const r = await fetch("https://cdn.jsdelivr.net/npm/@fontsource/" + path);
  if (!r.ok) throw new Error("Font download failed: " + path);
  writeFileSync(p, Buffer.from(await r.arrayBuffer()));
}
const f = (n) => "file://" + join(FONTS, n);
const photo = (n) => "file://" + join(HERE, "photos", n);

const CSS = `
@font-face{font-family:Newsreader;font-weight:600;src:url(${f("newsreader-600.woff2")})}
@font-face{font-family:Inter;font-weight:400;src:url(${f("inter-400.woff2")})}
@font-face{font-family:Inter;font-weight:500;src:url(${f("inter-500.woff2")})}
@font-face{font-family:Inter;font-weight:600;src:url(${f("inter-600.woff2")})}
@font-face{font-family:Inter;font-weight:700;src:url(${f("inter-700.woff2")})}
@font-face{font-family:Inter;font-weight:800;src:url(${f("inter-800.woff2")})}
:root{--cream:#FBF8F5;--pink:#D62E73;--bubble:#FF8AC2;--gold:#C8A96A;--ink:#1A1417}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1600px;height:900px;overflow:hidden;background:var(--cream)}
body{text-wrap:pretty;font-family:Inter,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased}
.stage{position:relative;width:1600px;height:900px;overflow:hidden;background:var(--cream)}
.photo{position:absolute;inset:0;background-size:cover;background-repeat:no-repeat}
.scrim{position:absolute;inset:0}
.wrap{position:absolute;inset:0;padding:58px 0 0 76px}
.kicker{display:inline-flex;align-items:center;gap:12px;font-weight:800;font-size:15px;letter-spacing:4.2px;text-transform:uppercase;color:var(--pink)}
.kicker:before{content:"";width:11px;height:11px;border-radius:50%;background:var(--pink);box-shadow:0 0 0 4px rgba(214,46,115,.16)}
h1{font-family:Newsreader,serif;font-weight:600;font-style:normal;color:var(--ink);letter-spacing:-2px;line-height:.98}
h1 .t{color:var(--pink)}
.sub{font-weight:600;color:var(--ink)}
.sub .t{color:var(--pink)}
.glass{background:rgba(255,255,255,.86);backdrop-filter:blur(14px);border:1.5px solid rgba(200,169,106,.75);border-radius:22px;
  box-shadow:0 26px 60px -18px rgba(214,46,115,.32),0 6px 18px -8px rgba(214,46,115,.18)}
.hero{position:relative;overflow:hidden;border-radius:22px;color:#fff;border:1.5px solid rgba(255,255,255,.55);
  background:linear-gradient(135deg,#F0559A 0%,#D62E73 48%,#B81E5E 100%);
  box-shadow:0 30px 70px -18px rgba(184,30,94,.55),0 8px 20px -8px rgba(184,30,94,.35)}
.hero:before{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(115deg,rgba(255,255,255,.34) 0%,rgba(255,255,255,0) 34%),
    radial-gradient(circle at 88% 12%,rgba(255,255,255,.55) 0 1.4px,transparent 2.4px),
    radial-gradient(circle at 76% 22%,rgba(255,255,255,.45) 0 1px,transparent 2px),
    radial-gradient(circle at 93% 30%,rgba(255,236,250,.6) 0 1.2px,transparent 2.2px),
    radial-gradient(circle at 82% 8%,rgba(255,255,255,.5) 0 .9px,transparent 1.8px)}
.hero > *{position:relative}
.foil{background:linear-gradient(100deg,#ffe3f1,#ffffff 22%,#f7d9ff 40%,#fff4c9 58%,#ffd6ea 76%,#ffffff);}
.sticker{position:absolute;border-radius:50%;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;
  background:#fff;color:var(--pink);box-shadow:0 18px 40px -12px rgba(214,46,115,.45)}
.sticker:after{content:"";position:absolute;inset:9px;border-radius:50%;border:2px dashed rgba(214,46,115,.55)}
.sticker.bubble{background:var(--bubble);color:#fff}
.sticker.bubble:after{border-color:rgba(255,255,255,.8)}
.sticker .big{font-family:Inter;font-weight:800;line-height:1}
.sticker .sm{font-weight:800;letter-spacing:2px;text-transform:uppercase}
.cta{display:inline-flex;align-items:center;gap:14px;height:66px;padding:0 36px;border-radius:999px;color:#fff;font-weight:800;font-size:19px;letter-spacing:3px;text-transform:uppercase;
  background:linear-gradient(135deg,#F0559A,#D62E73 55%,#C0246A);box-shadow:0 18px 36px -12px rgba(214,46,115,.6),inset 0 1px 0 rgba(255,255,255,.4)}
.ctaline{font-weight:700;font-size:21px;color:var(--ink)}
.ctaline .t{color:var(--pink)}
.tag{display:inline-block;font-weight:800;font-size:12.5px;letter-spacing:2.6px;text-transform:uppercase;padding:7px 14px;border-radius:999px}
.num{flex:none;width:44px;height:44px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:19px}
`;

const page = (body, photoFile, pos, scrim) => `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>
<div class="stage">
  <div class="photo" style="background-image:url(${photo(photoFile)});background-position:${pos}"></div>
  <div class="scrim" style="background:${scrim}"></div>
  <div class="wrap">${body}</div>
</div></body></html>`;

const SCRIM = (a, b) => `linear-gradient(90deg,var(--cream) 0%,var(--cream) ${a}%,rgba(251,248,245,.86) ${a + 6}%,rgba(251,248,245,.35) ${b - 6}%,rgba(251,248,245,0) ${b}%)`;

const check = (c = "var(--pink)") => `<svg width="24" height="24" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="12" fill="${c}"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#fff" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const checkW = `<svg width="24" height="24" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="12" fill="#fff"/><path d="M7 12.5l3.2 3.2L17 9" stroke="#D62E73" stroke-width="2.6" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const cross = `<svg width="24" height="24" viewBox="0 0 24 24" style="flex:none"><rect x="1" y="1" width="22" height="22" rx="6" fill="none" stroke="#1A1417" stroke-width="2"/><path d="M8 8l8 8M16 8l-8 8" stroke="#1A1417" stroke-width="2.2" stroke-linecap="round"/></svg>`;

const G = {};

// 1 · HERO
G["01-hero"] = page(`
  <div class="kicker">The Digital Income Edit™</div>
  <h1 style="font-size:106px;margin-top:40px;width:800px"><span class="t">Faceless</span> income,<br>built with <span class="t">AI.</span></h1>
  <p class="sub" style="font-size:36px;line-height:1.25;margin-top:34px;width:720px">Build the <span class="t">whole business</span> before anyone knows your name.</p>
  <div style="display:flex;gap:16px;margin-top:38px">
    ${["No filming", "No audience first", "No performing"].map((t) => `<div class="glass" style="display:flex;align-items:center;gap:12px;padding:15px 24px;border-radius:999px;font-weight:700;font-size:21px">${check()}${t}</div>`).join("")}
  </div>
  <div style="margin-top:46px"><span class="cta">Start your 7 days free <span>→</span></span></div>
  <div class="sticker bubble" style="width:178px;height:178px;left:1360px;top:44px;transform:rotate(9deg)"><span class="big" style="font-size:40px">7 DAYS</span><span class="sm" style="font-size:17px;margin-top:6px">free</span></div>
  <div class="sticker" style="width:154px;height:154px;left:556px;top:690px;transform:rotate(-8deg)"><span class="big" style="font-size:36px">1,200+</span><span class="sm" style="font-size:14px;margin-top:6px;color:var(--ink)">members</span></div>
`, "01-hero.jpg", "right center", SCRIM(36, 66));

// 2 · SAME EFFORT
G["02-same-effort"] = page(`
  <div class="kicker">Why this works</div>
  <h1 style="font-size:92px;margin-top:26px">Same effort.<br><span class="t">Opposite order.</span></h1>
  <p class="sub" style="font-size:24px;line-height:1.35;margin-top:18px;width:640px">Most people post for months, then try to make an offer. <span class="t">We build it backwards.</span></p>
  <div style="display:flex;align-items:center;gap:0;margin-top:30px">
    <div class="glass" style="width:300px;padding:22px 24px 20px">
      <span class="tag" style="background:#FFE3EF;color:var(--pink)">The usual way</span>
      <div style="font-family:Newsreader;font-weight:600;font-size:38px;margin:12px 0 8px">Audience first</div>
      ${["Post for months", "Chase followers", "Make an offer last", "Hope it sells"].map((t) => `<div style="display:flex;align-items:center;gap:14px;font-weight:700;font-size:21px;padding:7px 0">${cross}${t}</div>`).join("")}
      <div style="margin-top:14px;padding-top:16px;border-top:2px dashed rgba(214,46,115,.4);font-weight:800;font-size:19px;color:var(--pink);white-space:nowrap">Months in, nothing to sell.</div>
    </div>
    <div class="foil" style="position:relative;z-index:2;width:64px;height:64px;margin:0 -14px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-weight:800;font-size:22px;color:var(--pink);border:2px solid #fff;box-shadow:0 14px 30px -10px rgba(214,46,115,.55)">VS</div>
    <div class="hero" style="width:368px;padding:22px 24px 20px">
      <span class="tag" style="background:#fff;color:var(--pink)">The TDIE way</span>
      <div style="font-family:Newsreader;font-weight:600;font-size:38px;margin:12px 0 4px">Offer first</div>
      ${[["Offer", "The thing people pay for"], ["Funnel", "The path from a click to a sale"], ["Automation", "Set up once, runs on its own"], ["Audience, last", "Lands on a business that's already built"]].map(([h, p], i) => `<div style="display:flex;gap:14px;align-items:flex-start;padding:6px 0"><span class="num" style="background:#fff;color:var(--pink);width:36px;height:36px;font-size:16px">${i + 1}</span><div><div style="font-weight:800;font-size:21px">${h}</div><div style="font-weight:600;font-size:17px;margin-top:1px">${p}</div></div></div>`).join("")}
    </div>
  </div>
  <div class="sticker" style="width:140px;height:140px;left:600px;top:44px;transform:rotate(-10deg)"><span class="big" style="font-size:24px">OFFER<br>FIRST.</span><span class="sm" style="font-size:12px;margin-top:5px;color:var(--ink)">Audience<br>last.</span></div>
`, "02-same-effort.jpg", "0% 0%;background-size:124% auto", SCRIM(44, 62));

// 3 · ROADMAP (Jodie's copy, 27 Sep 2026, word for word)
const steps = [
  ["Your offer", "The Monetization Edit (Standard) · The Offer Edit (Premium, or $37 alone)"],
  ["Your funnel", "The Email Edit (Standard) · The Funnel Edit (Premium, or $37 alone)"],
  ["Your automation", "Scaling & Systems (Premium, or $97 alone)"],
  ["Your audience", "Pinterest Foundations™ (Standard, or $27 alone) · The Content Edit · AI Twin / Influencer Creation (Standard) · The Ads Edit™ + Monthly DFY Content Calendar (Premium)"],
];
G["03-roadmap"] = page(`
  <div class="kicker">Your roadmap</div>
  <h1 style="font-size:92px;margin-top:26px">Four steps. <span class="t">One build.</span></h1>
  <div style="display:grid;grid-template-columns:416px 416px;gap:20px;margin-top:34px">
    ${steps.map(([h, p], i) => `<div class="${i === 3 ? "hero" : "glass"}" style="padding:24px 26px 24px;display:flex;gap:16px;align-items:flex-start;min-height:${i < 2 ? 150 : 176}px">
      <span class="num" style="${i === 3 ? "background:#fff;color:var(--pink)" : "background:var(--pink);color:#fff"}">${i + 1}</span>
      <div style="flex:1"><div style="font-family:Newsreader;font-weight:600;font-size:33px;line-height:1.05;display:flex;align-items:center;gap:12px">${h}${i === 0 ? `<span class="tag" style="font-family:Inter;background:var(--bubble);color:#fff;font-size:11.5px;padding:6px 12px">Start here</span>` : ""}</div>
      <div style="font-weight:600;font-size:${i === 3 ? 16.5 : 18}px;line-height:1.42;margin-top:9px">${p.split(" · ").join("&nbsp;· ").replace(" / ", "&nbsp;/&nbsp;").replace("AI Twin", "AI&nbsp;Twin")}</div></div></div>`).join("")}
  </div>
  <div class="hero" style="display:flex;width:852px;margin-top:20px;padding:18px 10px">
    ${[["20+", "courses"], ["31", "days of content monthly"], ["7", "days free"]].map(([n, l], i) => `<div style="flex:1;text-align:center;${i ? "border-left:2px dashed rgba(255,255,255,.55)" : ""}"><div style="font-family:Newsreader;font-weight:600;font-size:50px;line-height:1">${n}</div><div style="font-weight:800;font-size:13.5px;letter-spacing:1.8px;text-transform:uppercase;margin-top:6px">${l}</div></div>`).join("")}
  </div>
  <div style="display:flex;align-items:center;gap:28px;margin-top:24px"><span class="cta" style="height:60px;font-size:17px">Start your 7 days free <span>→</span></span><span class="ctaline">Start at step 1. <span class="t">We go in order.</span></span></div>
`, "03-roadmap.jpg", "right center", SCRIM(52, 74));

// 4 · MEMBER WINS (quotes word for word)
const quotes = [
  ["BM", "Brittany M.", "“Just got the freebie tackled. Mailerlite automation complete. Tested and it works beautifully.”", false],
  ["BM", "Brittany M.", "“Got my first freebie subscriber today!”", true],
  ["CV", "Cristal V.", "“The remote part IS the surprise, and I've been explaining everything else before I get to the thing that makes my service different!”", false],
];
G["04-member-wins"] = page(`
  <div class="kicker">Inside the community</div>
  <h1 style="font-size:84px;margin-top:22px">Real members.<br><span class="t">Real wins.</span></h1>
  <p class="sub" style="font-size:24px;margin-top:16px">Straight from the community feed, <span class="t">word for word.</span></p>
  <div style="display:flex;flex-direction:column;gap:12px;width:660px;margin-top:22px">
    ${quotes.map(([i, n, q, h]) => `<div class="${h ? "hero" : "glass"}" style="display:flex;gap:16px;padding:16px 22px;align-items:flex-start">
      <span class="num" style="width:46px;height:46px;font-size:16px;${h ? "background:#fff;color:var(--pink)" : "background:#FFE3EF;color:var(--pink);border:2px solid var(--pink)"}">${i}</span>
      <div><div style="font-weight:800;font-size:17px">${n} <span style="font-size:11.5px;letter-spacing:2.4px;margin-left:6px;${h ? "" : "color:var(--pink)"}">MEMBER</span></div>
      <div style="font-weight:600;font-size:${h ? 21 : 18.5}px;line-height:1.36;margin-top:3px">${q}</div></div></div>`).join("")}
  </div>
  <div style="margin-top:18px"><span class="tag" style="background:var(--pink);color:#fff">What members are building</span></div>
  <div style="display:flex;align-items:center;flex-wrap:wrap;gap:9px;width:680px;margin-top:10px">
    ${["Etsy shops", "Freebies + email lists", "One-sentence offers", "AI personas", "Pinterest pins"].map((t) => `<span class="glass" style="display:inline-flex;align-items:center;gap:8px;padding:7px 13px;border-radius:999px;font-weight:700;font-size:16px">${check()}${t}</span>`).join("")}
  </div>
  <div style="margin-top:12px;font-weight:800;font-size:18px;color:var(--pink)">Post your work in the feed. Get a real answer back.</div>
  <div class="sticker" style="width:130px;height:130px;left:614px;top:146px;transform:rotate(-9deg)"><span class="big" style="font-size:29px">1,200+</span><span class="sm" style="font-size:13px;margin-top:5px;color:var(--ink)">members</span></div>
`, "04-member-wins.jpg", "right center", SCRIM(42, 58));

// 5 · TIERS
const std = ["Pinterest Foundations™", "The Email Edit", "The Content Edit", "The Monetization Edit", "AI Twin / Influencer Creation", "The Shopify Edit", "Daily Prompts"];
const prem = [["The Offer Edit", "$37 alone"], ["The Funnel Edit", "$37 alone"], ["Scaling & Systems", "$97 alone"], ["The Ads Edit™", ""], ["The Premium Vault, all guides open", ""], ["Monthly DFY Content Calendar: 31 days written for you", ""]];
G["05-tiers"] = page(`
  <div class="kicker">Choose your membership</div>
  <h1 style="font-size:76px;margin-top:20px">Two ways in.<br><span class="t">Both free for 7 days.</span></h1>
  <div style="display:flex;gap:18px;margin-top:24px;align-items:stretch">
    <div class="glass" style="width:372px;padding:22px 26px 20px">
      <span class="tag" style="background:#FFE3EF;color:var(--pink)">Start building</span>
      <div style="font-weight:800;font-size:14px;letter-spacing:3px;color:var(--pink);margin-top:14px">MEMBERSHIP STANDARD</div>
      <div style="display:flex;align-items:baseline;gap:8px;margin-top:2px"><span style="font-weight:800;font-size:60px;letter-spacing:-2px;line-height:1">$9</span><span style="font-weight:700;font-size:20px">/month</span><span style="font-weight:700;font-size:17px;margin-left:8px">or $99/year</span></div>
      <div style="margin-top:10px">${std.map((t) => `<div style="display:flex;align-items:center;gap:11px;font-weight:600;font-size:17.5px;padding:6px 0">${check()}${t}</div>`).join("")}</div>
      <div style="display:flex;align-items:center;gap:11px;font-weight:700;font-size:16.5px;padding:7px 0 0;color:var(--pink)"><svg width="24" height="24" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="11" fill="none" stroke="#D62E73" stroke-width="2"/><path d="M12 7v10M7 12h10" stroke="#D62E73" stroke-width="2.4" stroke-linecap="round"/></svg>The Value Vault, guides à la carte</div>
    </div>
    <div class="hero" style="width:420px;padding:22px 26px 20px">
      <span class="tag" style="background:#fff;color:var(--pink)">Everything + done for you</span>
      <div style="font-weight:800;font-size:14px;letter-spacing:3px;margin-top:14px">MEMBERSHIP PREMIUM</div>
      <div style="display:flex;align-items:baseline;gap:8px;margin-top:2px"><span style="font-weight:800;font-size:60px;letter-spacing:-2px;line-height:1">$35</span><span style="font-weight:700;font-size:20px">/month</span><span style="font-weight:700;font-size:17px;margin-left:8px">or $297/year</span></div>
      <div style="display:inline-block;font-weight:800;font-size:15.5px;padding:5px 12px;border:2px dashed rgba(255,255,255,.75);border-radius:10px;margin:10px 0 2px">Everything in Standard, plus:</div>
      ${prem.map(([t, p]) => `<div style="display:flex;align-items:center;gap:11px;font-weight:700;font-size:16.5px;padding:4px 0">${checkW}<span style="flex:1">${t}</span>${p ? `<span style="flex:none;background:#fff;color:var(--pink);font-weight:800;font-size:13px;padding:3px 10px;border-radius:999px">${p}</span>` : ""}</div>`).join("")}
      <div class="foil" style="display:flex;align-items:center;gap:12px;margin-top:10px;padding:9px 14px;border-radius:14px;color:var(--pink)"><span style="font-weight:800;font-size:30px;letter-spacing:-1px">$171</span><span style="font-weight:800;font-size:14.5px;line-height:1.25;color:var(--ink)">in modules sold separately,<br>included in Premium</span></div>
    </div>
  </div>
  <div style="display:flex;align-items:center;gap:26px;margin-top:22px"><span class="cta" style="height:58px;font-size:16.5px">Start your 7 days free <span>→</span></span><span class="ctaline">Pick either one. <span class="t">Both start free.</span></span></div>
`, "05-tiers.jpg", "right center", SCRIM(44, 60));

const only = process.argv.slice(2);
const browser = await chromium.launch(existsSync("/opt/pw-browsers/chromium") ? {} : {});
const ctx = await browser.newContext({ viewport: { width: 1600, height: 900 }, deviceScaleFactor: 2 });
for (const [name, html] of Object.entries(G)) {
  if (only.length && !only.some((o) => name.includes(o))) continue;
  const tmp = join(HERE, ".render-" + name + ".html");
  writeFileSync(tmp, html);
  const p = await ctx.newPage();
  await p.goto("file://" + tmp);
  await p.evaluate(() => document.fonts.ready);
  await p.waitForTimeout(300);
  await p.screenshot({ path: join(OUT, name + ".jpg"), type: "jpeg", quality: 93 });
  await p.close();
  console.log("rendered", name);
}
await browser.close();
