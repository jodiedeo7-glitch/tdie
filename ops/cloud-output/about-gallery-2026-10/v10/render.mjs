// Skool About gallery (5 x 1600x900) + Skool group cover (1084x576), rebuilt 12 Oct 2026
// on the approved homepage hero system (hero-v10 in src/styles/home.css on cloudflare-migration):
// blush background with white glow, photo panel on the right with a silver glitter edge,
// scattered silver glitter, Gloock headlines with ONE Yellowtail stressed word, Jost for
// everything else, white cards / pills / tags with pink outlines, glitter-dot ticker.
// No pink fills anywhere (standing rule). Run from repo root:
//   node ops/cloud-output/about-gallery-2026-10/v10/render.mjs [name ...]
import { mkdirSync, writeFileSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright")); }

const HERE = dirname(fileURLToPath(import.meta.url));
const OUT = join(HERE, "out"); mkdirSync(OUT, { recursive: true });
const A = (n) => "file://" + join(HERE, "assets", n);
const P = (n) => "file://" + join(HERE, "..", "photos", n);

const CSS = (W, H) => `
@font-face{font-family:Gloock;src:url(${A("gloock-latin-400-normal.woff2")})}
@font-face{font-family:Yellowtail;src:url(${A("yellowtail-latin-400-normal.woff2")})}
${[400,500,600,700,800].map(w=>`@font-face{font-family:Jost;font-weight:${w};src:url(${A(`jost-latin-${w}-normal.woff2`)})}`).join("")}
:root{--pink:#D62E73;--deep:#B8245F;--ink:#1A1417;--ink2:#4A3640;--soft:#EFA8C6}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:${W}px;height:${H}px;overflow:hidden}
body{font-family:Jost,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;text-wrap:pretty}
.stage{position:relative;width:${W}px;height:${H}px;overflow:hidden;
  background:radial-gradient(${W*.45}px ${H*.6}px at 28% 42%,#fff 0%,rgba(255,255,255,0) 70%),#FFF0F6}
.photo{position:absolute;top:0;bottom:0;right:0;background-size:cover;background-repeat:no-repeat}
.photo:before{content:"";position:absolute;left:0;top:0;bottom:0;width:14px;background:#c9ccd2 url(${A("silver-glitter-tile.webp")}) center/420px auto;box-shadow:4px 0 10px rgba(0,0,0,.15)}
.spark{position:absolute;top:0;height:100%;pointer-events:none;z-index:1;
  -webkit-mask-image:linear-gradient(90deg,transparent 0,transparent 40%,#000 85%);mask-image:linear-gradient(90deg,transparent 0,transparent 40%,#000 85%)}
.copy{position:absolute;z-index:3;display:flex;flex-direction:column;align-items:flex-start;justify-content:center}
.pl{font-family:Jost;font-weight:500}
.kick{display:inline-block;padding:8px 18px;border:1.5px solid var(--pink);border-radius:999px;background:#fff;font:600 17px/1.2 Jost;color:var(--pink)}
h1{font:400 74px/1 Gloock,serif;letter-spacing:-.01em;color:var(--ink)}
h1 .p{color:var(--pink)}
h1 .stress{font-family:Yellowtail,cursive;color:var(--pink);font-size:1.16em;line-height:.9;letter-spacing:0}
.lede{font:400 23px/1.45 Jost;color:var(--ink2)}
.lede b{font-weight:600;color:var(--ink)}
.card{background:#fff;border:1.5px solid var(--soft);border-radius:16px;box-shadow:0 2px 4px rgba(90,0,40,.05),0 16px 28px -16px rgba(90,0,40,.32)}
.card.feat{border:2px solid var(--pink);box-shadow:0 2px 4px rgba(90,0,40,.06),0 22px 36px -18px rgba(90,0,40,.42)}
.btn{display:inline-flex;align-items:center;gap:10px;padding:17px 30px;border-radius:14px;background:#fff;border:1.5px solid var(--pink);font:600 20px/1 Jost;color:var(--pink);box-shadow:0 14px 24px -14px rgba(90,0,40,.4)}
.link{font:600 20px/1 Jost;color:var(--ink);border-bottom:2px solid var(--pink);padding-bottom:4px}
.tag{position:absolute;z-index:6;background:#fff;border:1.5px solid var(--pink);border-radius:14px;padding:10px 18px 12px;text-align:center;font:700 12px/1.15 Jost;letter-spacing:.07em;text-transform:uppercase;color:var(--ink);box-shadow:0 14px 24px -14px rgba(90,0,40,.5)}
.tag b{display:block;font:400 38px/1 Gloock;color:var(--pink);letter-spacing:0;text-transform:none;margin-bottom:5px}
.num{flex:none;width:38px;height:38px;border-radius:50%;background:#fff;border:1.5px solid var(--pink);display:flex;align-items:center;justify-content:center;font:400 20px/1 Gloock;color:var(--pink)}
.chip{display:inline-flex;align-items:center;gap:8px;padding:8px 15px;border-radius:999px;background:#fff;border:1.5px solid var(--soft);font:500 17px/1 Jost;color:var(--ink)}
.small{font:700 12.5px/1 Jost;letter-spacing:.14em;text-transform:uppercase;color:var(--deep)}
.tick{position:absolute;z-index:5;left:-40px;right:-40px;background:#fff;border-top:1.5px solid var(--pink);border-bottom:1.5px solid var(--pink);padding:12px 0;white-space:nowrap;overflow:hidden;transform:rotate(-1.5deg);box-shadow:0 14px 24px -14px rgba(90,0,40,.35)}
.tick .row{display:inline-flex;align-items:center;gap:28px;padding-left:70px;font:400 26px/1 Gloock;color:var(--pink)}
.tick i{flex:none;display:inline-block;width:17px;height:17px;border-radius:50%;background:#c9ccd2 url(${A("silver-glitter-tile.webp")}) center/180px auto;box-shadow:0 1px 3px rgba(0,0,0,.3)}
.logo{display:inline-flex;flex-direction:column;align-items:center;line-height:1}
.logo .l1{font:700 11px/1 Jost;letter-spacing:.42em;margin-right:-.42em;text-transform:uppercase}
.logo .l2{font:400 46px/.9 Gloock;color:var(--pink);margin-top:4px}
`;
const chk = `<svg width="22" height="22" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="10.5" fill="#fff" stroke="#D62E73" stroke-width="1.8"/><path d="M7.2 12.4l3.2 3.2L16.8 9" stroke="#D62E73" stroke-width="2.4" fill="none" stroke-linecap="round" stroke-linejoin="round"/></svg>`;
const cross = `<svg width="22" height="22" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="10.5" fill="#fff" stroke="#9C8C93" stroke-width="1.8"/><path d="M8.5 8.5l7 7M15.5 8.5l-7 7" stroke="#9C8C93" stroke-width="2.2" stroke-linecap="round"/></svg>`;
const tick = (items, bottom) => `<div class="tick" style="bottom:${bottom}px"><div class="row">${[...items, ...items].map(t => `<span>${t.replace("+", '<span class="pl">+</span>')}</span><i></i>`).join("")}</div></div>`;

const page = ({ W = 1600, H = 900, photo, pos = "right center", panel = 42, body }) => {
  const px = Math.round(W * (1 - panel / 100));
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS(W, H)}</style></head><body><div class="stage">
  <div class="photo" style="left:${px}px;background-image:url(${photo});background-position:${pos}"></div>
  <img class="spark" src="${A("sparkle-scatter.webp")}" style="left:${px - Math.round(W * .32)}px;width:${Math.round(W * .36)}px">
  ${body(px)}
  </div></body></html>`;
};

const G = {};

// 1 · HERO
G["01-hero"] = page({ photo: P("01-hero.jpg"), pos: "68% center", body: (px) => `
  <div class="copy" style="left:84px;top:0;bottom:110px;width:${px - 150}px">
    <span class="kick">For women building without a personal brand</span>
    <h1 style="margin-top:30px;font-size:96px"><span class="p">Faceless</span> income,<br>built with <span class="p">AI.</span></h1>
    <p class="lede" style="margin-top:28px;width:640px;font-size:25px">Build the <b>whole business</b> before anyone knows your name. Offer first, audience last.</p>
    <div style="display:flex;gap:10px;margin-top:26px">${["No filming", "No audience first", "No performing"].map(t => `<span class="chip">${chk}${t}</span>`).join("")}</div>
    <div style="display:flex;align-items:center;gap:30px;margin-top:34px"><span class="btn">Start your 7 days free <span>→</span></span><span class="link">Free look inside</span></div>
  </div>
  <div class="tag" style="left:${px + 40}px;top:66px;transform:rotate(-8deg)"><b>7 days</b>Free to start</div>
  <div class="tag" style="left:${px + 40}px;bottom:150px;transform:rotate(6deg)"><b>1,200<span class="pl">+</span></b>Members building</div>
  ${tick(["No filming", "Offer first", "Audience last", "Built with AI", "7 days free"], 34)}
` });

// 2 · SAME EFFORT
G["02-same-effort"] = page({ photo: P("02-same-effort.jpg"), pos: "78% center", body: (px) => `
  <div class="copy" style="left:84px;top:0;bottom:0;width:${px - 130}px">
    <span class="kick">Why this works</span>
    <h1 style="margin-top:26px">Same effort.<br><span class="p">Opposite</span> <span class="p">order.</span></h1>
    <p class="lede" style="margin-top:18px;width:640px">Most people post for months, then try to make an offer. <b style="white-space:nowrap">We build it backwards.</b></p>
    <div style="display:flex;align-items:center;margin-top:30px">
      <div class="card" style="width:318px;padding:24px 24px 22px">
        <div class="small" style="color:#8C7A82">The usual way</div>
        <div style="font:400 30px/1.1 Gloock;margin:10px 0 10px;color:#5E4E55">Audience first</div>
        ${["Post for months", "Chase followers", "Make an offer last", "Hope it sells"].map(t => `<div style="display:flex;align-items:center;gap:12px;font:500 19px/1 Jost;padding:8px 0;color:#5E4E55">${cross}${t}</div>`).join("")}
        <div style="margin-top:12px;padding-top:14px;border-top:1.5px dashed var(--soft);font:600 18px/1.2 Jost;color:var(--deep)">Months in, nothing to sell.</div>
      </div>
      <div style="position:relative;z-index:2;width:58px;height:58px;margin:0 -12px;border-radius:50%;background:#fff;border:1.5px solid var(--pink);display:flex;align-items:center;justify-content:center;font:400 22px/1 Gloock;color:var(--pink);box-shadow:0 10px 18px -10px rgba(90,0,40,.45)">vs</div>
      <div class="card feat" style="width:368px;padding:24px 24px 20px">
        <div class="small">The TDIE way</div>
        <div style="font:400 30px/1.1 Gloock;margin:10px 0 6px;color:var(--pink)">Offer first</div>
        ${[["Offer", "The thing people pay for"], ["Funnel", "The path from a click to a sale"], ["Automation", "Set up once, runs on its own"], ["Audience, last", "Lands on a business that's already built"]].map(([h, p], i) => `<div style="display:flex;gap:12px;align-items:center;padding:6px 0"><span class="num" style="width:34px;height:34px;font-size:18px">${i + 1}</span><div><div style="font:600 19px/1.15 Jost">${h}</div><div style="font:400 16px/1.3 Jost;color:var(--ink2)">${p}</div></div></div>`).join("")}
      </div>
    </div>
  </div>
  <div class="tag" style="left:${px + 46}px;top:56px;transform:rotate(-7deg)"><b>Offer first.</b>Audience last.</div>
` });

// 3 · ROADMAP (Jodie's copy, 27 Sep 2026, word for word)
const steps = [
  ["Your offer", "The Monetization Edit (Standard) · The Offer Edit (Premium, or $37 alone)"],
  ["Your funnel", "The Email Edit (Standard) · The Funnel Edit (Premium, or $37 alone)"],
  ["Your automation", "Scaling & Systems (Premium, or $97 alone)"],
  ["Your audience", "Pinterest Foundations™ (Standard, or $27 alone) · The Content Edit · AI Twin / Influencer Creation (Standard) · The Ads Edit™ + Monthly DFY Content Calendar (Premium)"],
];
const nb = (t) => t.split(" · ").map(x => x.length > 40 ? x : `<span style="white-space:nowrap">${x}</span>`).join(" · ").replace("$27 alone", "$27&nbsp;alone").replace("<span style=\"white-space:nowrap\">Pinterest Foundations™ (Standard, or $27 alone)</span>", "Pinterest Foundations™ (Standard, or&nbsp;$27&nbsp;alone)");
G["03-roadmap"] = page({ photo: P("03-roadmap.jpg"), pos: "64% center", panel: 38, body: (px) => `
  <div class="copy" style="left:84px;top:0;bottom:100px;width:${px - 120}px">
    <span class="kick">Your roadmap</span>
    <h1 style="margin-top:22px">Four steps. <span class="p">One</span> <span class="p">build.</span></h1>
    <div style="display:grid;grid-template-columns:418px 418px;gap:16px;margin-top:26px">
      ${steps.map(([h, p], i) => `<div class="card${i === 0 ? " feat" : ""}" style="padding:18px 20px;display:flex;gap:14px;align-items:flex-start;min-height:${i < 2 ? 136 : 168}px">
        <span class="num">${i + 1}</span>
        <div><div style="display:flex;align-items:center;gap:10px;font:400 26px/1.1 Gloock;white-space:nowrap">${h}${i === 0 ? `<span class="small" style="font-size:10.5px;padding:5px 10px;border:1.5px solid var(--pink);border-radius:999px">Start here</span>` : ""}</div>
        <div style="font:500 ${i === 3 ? 15.5 : 17}px/1.42 Jost;color:var(--ink2);margin-top:7px">${nb(p)}</div></div></div>`).join("")}
    </div>
    <div style="display:flex;align-items:center;gap:30px;margin-top:26px"><span class="btn">Start your 7 days free <span>→</span></span><span class="link">Start at step 1. We go in order.</span></div>
  </div>
  ${tick(["20+ courses", "31 days of content monthly", "7 days free", "Offer first", "Audience last"], 28)}
` });

// 4 · MEMBER WINS (quotes word for word)
const quotes = [
  ["BM", "Brittany M.", "“Just got the freebie tackled. Mailerlite automation complete. Tested and it works beautifully.”", false],
  ["BM", "Brittany M.", "“Got my first freebie subscriber today!”", true],
  ["CV", "Cristal V.", "“The remote part IS the surprise, and I've been explaining everything else before I get to the thing that makes my service different!”", false],
];
G["04-member-wins"] = page({ photo: P("04-member-wins.jpg"), pos: "72% center", body: (px) => `
  <div class="copy" style="left:84px;top:0;bottom:0;width:${px - 130}px">
    <span class="kick">Inside the community</span>
    <h1 style="margin-top:22px">Real members.<br><span class="p">Real</span> <span class="p">wins.</span></h1>
    <p class="lede" style="margin-top:12px;font-size:21px">Straight from the community feed, <b>word for word.</b></p>
    <div style="display:flex;flex-direction:column;gap:12px;width:720px;margin-top:22px">
      ${quotes.map(([i, n, q, f]) => `<div class="card${f ? " feat" : ""}" style="position:relative;display:flex;gap:16px;padding:16px 22px;align-items:flex-start">
        ${f ? `<span style="position:absolute;right:22px;top:-6px;font:400 96px/1 Gloock;color:var(--pink)">”</span>` : ""}
        <span class="num" style="width:44px;height:44px;font:600 15px/1 Jost">${i}</span>
        <div><div style="font:600 17px/1 Jost">${n} <span class="small" style="font-size:11px;margin-left:6px">Member</span></div>
        <div style="font:${f ? "400 26px/1.25 Gloock" : "500 18px/1.4 Jost"};margin-top:6px;${f ? "color:var(--pink)" : "color:var(--ink2)"}">${q}</div></div></div>`).join("")}
    </div>
    <div class="small" style="margin-top:22px">What members are building</div>
    <div style="display:flex;flex-wrap:wrap;gap:9px;width:760px;margin-top:10px">${["Etsy shops", "Freebies + email lists", "One-sentence offers", "AI personas", "Pinterest pins"].map(t => `<span class="chip" style="font-size:16px">${chk}${t}</span>`).join("")}</div>
    <div style="margin-top:16px;font:600 19px/1 Jost;color:var(--ink)">Post your work in the feed. <span style="color:var(--pink)">Get a real answer back.</span></div>
  </div>
  <div class="tag" style="left:${px + 40}px;top:60px;transform:rotate(-7deg)"><b>1,200<span class="pl">+</span></b>Members building</div>
` });

// 5 · TIERS
const std = ["Pinterest Foundations™", "The Email Edit", "The Content Edit", "The Monetization Edit", "AI Twin / Influencer Creation", "The Shopify Edit", "Daily Prompts"];
const prem = [["The Offer Edit", "$37 alone"], ["The Funnel Edit", "$37 alone"], ["Scaling & Systems", "$97 alone"], ["The Ads Edit™", ""], ["The Premium Vault, all guides open", ""], ["Monthly DFY Content Calendar (31 days)", ""]];
const price = (n, y) => `<div style="display:flex;align-items:baseline;gap:8px;margin-top:4px"><span style="font:400 58px/1 Gloock;color:var(--pink)">${n}</span><span style="font:600 19px/1 Jost">/month</span><span style="font:500 17px/1 Jost;color:var(--ink2);margin-left:6px">or ${y}/year</span></div>`;
G["05-tiers"] = page({ photo: P("05-tiers.jpg"), pos: "100% 30%", panel: 38, body: (px) => `
  <div class="copy" style="left:84px;top:0;bottom:0;width:${px - 110}px">
    <span class="kick">Choose your membership</span>
    <h1 style="margin-top:20px;font-size:68px">Two ways in. Both <span class="p">free</span><br><span class="p">for 7 days.</span></h1>
    <div style="display:flex;gap:18px;margin-top:24px;align-items:stretch">
      <div class="card" style="width:380px;padding:20px 24px">
        <div class="small">Start building</div>
        <div style="font:400 26px/1 Gloock;margin-top:8px">Membership Standard</div>
        ${price("$9", "$99")}
        <div style="margin-top:10px">${std.map(t => `<div style="display:flex;align-items:center;gap:10px;font:500 17px/1 Jost;padding:6px 0">${chk}${t}</div>`).join("")}</div>
        <div style="display:flex;align-items:center;gap:10px;font:500 16px/1.2 Jost;padding:8px 0 0;color:var(--deep)"><svg width="22" height="22" viewBox="0 0 24 24" style="flex:none"><circle cx="12" cy="12" r="10.5" fill="#fff" stroke="#D62E73" stroke-width="1.8"/><path d="M12 7v10M7 12h10" stroke="#D62E73" stroke-width="2.2" stroke-linecap="round"/></svg>The Value Vault, guides à la carte</div>
      </div>
      <div class="card feat" style="width:440px;padding:20px 24px">
        <div class="small">Everything + done for you</div>
        <div style="font:400 26px/1 Gloock;margin-top:8px">Membership Premium</div>
        ${price("$35", "$297")}
        <div style="font:600 15px/1 Jost;margin:12px 0 4px;color:var(--ink2)">Everything in Standard, plus:</div>
        ${prem.map(([t, p]) => `<div style="display:flex;align-items:center;gap:10px;font:500 16.5px/1.2 Jost;padding:5px 0">${chk}<span style="flex:1">${t}</span>${p ? `<span style="flex:none;font:600 13px/1 Jost;color:var(--pink);padding:4px 9px;border:1.5px solid var(--soft);border-radius:999px">${p}</span>` : ""}</div>`).join("")}
        <div style="display:flex;align-items:center;gap:12px;margin-top:10px;padding:9px 14px;border-radius:12px;border:1.5px dashed var(--pink)"><span style="font:400 30px/1 Gloock;color:var(--pink)">$171</span><span style="font:600 14px/1.25 Jost">in modules sold separately,<br>included in Premium</span></div>
      </div>
    </div>
    <div style="display:flex;align-items:center;gap:30px;margin-top:24px"><span class="btn">Start your 7 days free <span>→</span></span><span class="link">Pick either one. Both start free.</span></div>
  </div>
` });

// 6 · SKOOL GROUP COVER (1084 x 576)
G["06-skool-cover"] = page({ W: 1084, H: 576, photo: A("hero-tk-car.webp"), pos: "30% 35%", panel: 40, body: (px) => `
  <div class="copy" style="left:52px;top:0;bottom:70px;width:${px - 80}px">
    <div class="logo"><span class="l1">The Digital Income</span><span class="l2">Edit</span></div>
    <h1 style="margin-top:22px;font-size:50px;line-height:1">Build a faceless business. <span class="p">Keep your life</span> <span class="stress">off camera.</span></h1>
    <p class="lede" style="margin-top:14px;font-size:17px;width:470px">Pick one thing to sell, build what sells it, and let AI do the repeat work. Your face never has to show up.</p>
    <div style="display:flex;align-items:center;gap:20px;margin-top:20px"><span class="btn" style="font-size:16px;padding:13px 22px">Start your 7 days free <span>→</span></span><span class="link" style="font-size:16px">Free look inside</span></div>
  </div>
  <div class="tag" style="right:22px;top:26px;transform:rotate(-8deg);padding:8px 14px 10px;font-size:10px"><b style="font-size:28px">1,200<span class="pl">+</span></b>Members building</div>
  <div class="tick" style="bottom:22px;padding:9px 0"><div class="row" style="font-size:19px;gap:20px">${[...["No filming", "Offer first", "Audience last", "Built with AI", "7 days free"], ...["No filming", "Offer first", "Audience last", "Built with AI", "7 days free"]].map(t => `<span>${t}</span><i style="width:13px;height:13px"></i>`).join("")}</div></div>
` });

const only = process.argv.slice(2);
const browser = await chromium.launch();
for (const [name, html] of Object.entries(G)) {
  if (only.length && !only.some((o) => name.includes(o))) continue;
  const [W, H] = name.includes("cover") ? [1084, 576] : [1600, 900];
  const ctx = await browser.newContext({ viewport: { width: W, height: H }, deviceScaleFactor: 2 });
  const tmp = join(HERE, ".render-" + name + ".html"); writeFileSync(tmp, html);
  const p = await ctx.newPage(); await p.goto("file://" + tmp);
  await p.evaluate(() => document.fonts.ready); await p.waitForTimeout(300);
  await p.screenshot({ path: join(OUT, name + ".jpg"), type: "jpeg", quality: 93 });
  await ctx.close(); console.log("rendered", name);
}
await browser.close();
