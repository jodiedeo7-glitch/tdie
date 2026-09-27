// Link thumbnails (og:image) for every product page. 1200 × 630 JPG.
//
// Run from the repo root:   node ops/og-thumbnails/render.mjs
// Only some pages:          node ops/og-thumbnails/render.mjs find-your-door
//
// Writes public/og/p/<page>.jpg and src/data/og-thumbnails.js (page path → image URL with a
// content hash, so Facebook and iMessage fetch the new image instead of a cached one).
// PageLayout reads that file, so a page never needs its own ogImage line.
//
// Type: Inter only. Headlines are Inter Black (founder decision, 27 Sep 2026: Newsreader and
// every other serif is out for headlines; not readable enough). Every word sits inside the
// centre 600 px, which is the square Facebook shows in comments and small link cards.
//
// Needs Node 22 and Playwright (global install is fine). Inter is pulled once into ./fonts.

import { existsSync, mkdirSync, readFileSync, readdirSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";
import { createHash } from "node:crypto";
import { PRODUCTS } from "./products.mjs";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright")); }

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../..");
const OUT = join(ROOT, "public/og/p");
const MANIFEST = join(ROOT, "src/data/og-thumbnails.js");
const FONTS = join(HERE, "fonts");
mkdirSync(OUT, { recursive: true });
mkdirSync(FONTS, { recursive: true });

const INTER = join(FONTS, "Inter.ttf");
if (!existsSync(INTER)) {
  const url = "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf";
  const r = await fetch(url);
  if (!r.ok) throw new Error(`Font download failed: ${url} (${r.status})`);
  writeFileSync(INTER, Buffer.from(await r.arrayBuffer()));
}

// ---------- photos (Tommy Kate in her own world; no third-party toys in these crops) ----------
const PHOTOS = {
  porch:       ["public/images/we/cover-sofa.jpg", "42% 35%"],
  kitchen:     ["public/images/we/preview-working.jpg", "58% 40%"],
  sofa:        ["ops/cloud-output/we-creatives/photos/sofa-tumbler-no-lettering.jpg", "52% 40%"],
  pasture:     ["ops/cloud-output/we-creatives/photos/pay-plan-pasture-blanket.jpg", "62% 40%"],
  laptopPink:  ["public/images/membership-jodie.webp", "52% 35%"],
  loft:        ["public/images/we/preview-hero.jpg", "48% 35%"],
  hoodie:      ["public/images/library/path-blogging.jpg", "45% 40%"],
  bed:         ["public/images/library/path-digital-products.jpg", "62% 40%"],
  pinkSweater: ["public/images/library/path-pinterest.jpg", "25% 40%"],
  gifts:       ["public/images/library/path-affiliate.jpg", "78% 30%"],
  phoneHands:  ["public/images/library/path-automation.jpg", "50% 45%"],
};
const file = (p) => "file://" + join(ROOT, p);
const vault = (name) => file(`public/images/vault/${name}.jpg`);

// ---------- helpers ----------
const esc = (s) => String(s).replace(/&/g, "&amp;").replace(/</g, "&lt;").replace(/>/g, "&gt;");
const pinkify = (s) => esc(s).replace(/\*([^*]+)\*/g, '<em>$1</em>');
const tick = '<span class="tk">✓</span>';

// ---------- drawn previews (right-hand side) ----------
const MOCKS = {
  quiz: (m) => `<div class="card quiz"><div class="cap">${esc(m.step)}</div><div class="q">${esc(m.q)}</div>
    ${m.opts.map((o, i) => `<div class="opt${i === m.pick ? " on" : ""}"><span class="rd"></span>${esc(o)}</div>`).join("")}
    <div class="bar"><i style="width:27%"></i></div></div>`,

  doc: (m) => `<div class="card doc"><div class="dt">${esc(m.title)}</div>
    ${m.items.map((t, i) => `<div class="li">${m.plain ? "" : m.numbered ? `<span class="nm">${i + 1}</span>` : tick}${esc(t)}</div>`).join("")}</div>`,

  chat: (m) => `<div class="card chat"><div class="cap">AI assistant</div>
    <div class="bub you">${esc(m.you)}</div><div class="bub ai">${esc(m.ai)}</div>
    <div class="inp">Message…<span class="snd">↑</span></div></div>`,

  flow: (m) => `<div class="flow">${m.steps.map((s, i) =>
    `${i ? '<div class="arr">↓</div>' : ""}<div class="node${i === m.steps.length - 1 ? " hot" : ""}">${esc(s)}</div>`).join("")}</div>`,

  browser: (m) => {
    const views = {
      article: `<div class="art"><div class="ah">${esc(m.title)}</div><div class="ln"></div><div class="ln"></div><div class="ln s"></div><div class="img"></div><div class="ln"></div><div class="ln s"></div></div>`,
      shop: `<div class="shop">${["Planner", "Tote", "Mug", "Journal"].map((n, i) =>
        `<div class="it"><div class="ph p${i}"></div><div class="nm">${n}</div><div class="pr">$${[18, 24, 16, 22][i]}</div></div>`).join("")}</div>`,
      site: `<div class="site"><div class="nav"><b>Your Name</b><span>Blog · Shop · Free guide</span></div>
        <div class="hero2"><div class="h">Start here</div><div class="ln"></div><div class="btn">Get the free guide</div></div>
        <div class="posts"><div></div><div></div><div></div></div></div>`,
      sales: `<div class="sales2"><div class="h">The offer, said plainly</div><div class="ln"></div><div class="ln s"></div>
        ${["Who it's for", "What changes", "What's inside"].map((t) => `<div class="li">${tick}${t}</div>`).join("")}<div class="btn">Buy now</div></div>`,
    };
    return `<div class="card browser"><div class="chrome"><i></i><i></i><i></i><span>${esc(m.url)}</span></div>${views[m.view]}</div>`;
  },

  brand: (m) => `<div class="card brand"><div class="cap">Brand promise</div><div class="bp">“${esc(m.promise)}”</div>
    <div class="sw"><i style="background:#D62E73"></i><i style="background:#FF8AC2"></i><i style="background:#FBF8F5"></i><i style="background:#C8A96A"></i></div>
    <div class="ty"><b>Aa</b><span>Headline<br><small>Body text</small></span></div></div>`,

  week: (m) => `<div class="card week"><div class="cap">1 idea → 5 posts</div>
    ${m.days.map((d, i) => `<div class="wd"><span class="dy">${["MON", "TUE", "WED", "THU", "FRI"][i]}</span>${esc(d)}</div>`).join("")}</div>`,

  days: (m) => `<div class="card week"><div class="cap">5 days · 5 emails</div>
    ${m.days.map((d, i) => `<div class="wd"><span class="dy">DAY ${i + 1}</span>${esc(d)}</div>`).join("")}</div>`,

  inbox: (m) => `<div class="card inbox"><div class="cap">Inbox · welcome series</div>
    ${m.rows.map(([a, b], i) => `<div class="mail${i ? "" : " new"}"><span class="av a${i % 3}"></span><div><b>${esc(a)}</b><small>${esc(b)}</small></div></div>`).join("")}</div>`,

  compare: (m) => `<div class="card cmp"><div class="col"><div class="cap">${esc(m.lh)}</div>${m.left.map((t) => `<div class="x">${esc(t)}</div>`).join("")}</div>
    <div class="col hot"><div class="cap">${esc(m.rh)}</div>${m.right.map((t) => `<div class="li">${tick}${esc(t)}</div>`).join("")}</div></div>`,

  sentence: (m) => `<div class="card sent"><div class="cap">Your one sentence</div><div class="field">${esc(m.text)}<span class="caret"></span></div>
    ${m.checks.map((c) => `<div class="li">${tick}${esc(c)}</div>`).join("")}</div>`,

  sales: (m) => `<div class="card notif"><div class="cap">${esc(m.title)}</div>
    ${m.rows.map((r, i) => `<div class="nt"><span class="ic">$</span><div><b>${esc(r)}</b><small>${["2:14 am", "6:40 am", "11:02 am"][i]}</small></div></div>`).join("")}</div>`,

  search: (m) => `<div class="card srch"><div class="sb">⌕ ${esc(m.query)}</div>
    ${m.results.map((r) => `<div class="sr">⌕ ${esc(r)}</div>`).join("")}<div class="cap" style="margin-top:12px">Keyword bank · 30 to 50</div></div>`,

  pins: (m) => `<div class="phone"><div class="scr pins">${m.pins.map((p, i) =>
    `<div class="pin p${i}"><span>${esc(p)}</span></div>`).join("")}</div></div>`,

  stack: (m) => `<div class="stack">${m.covers.map((c, i) =>
    `<div class="cover c${i}"><div class="brandline">The Digital Income Edit™</div><div class="ct">${esc(c)}</div><div class="fr">FREE</div></div>`).join("")}</div>`,

  tiles: (m) => `<div class="card tiles">${m.tiles.map((t) => `<div class="tl" style="background-image:url('${vault(t)}')"></div>`).join("")}</div>`,

  prompts: (m) => `<div class="stack pr">${m.cards.map((c, i) =>
    `<div class="pc c${i}"><div class="cap">Prompt ${String(i * 7 + 3).padStart(2, "0")}</div><div class="pt">${esc(c)}</div><div class="cp">Copy</div></div>`).join("")}</div>`,

  chart: (m) => `<div class="card chart"><div class="cap">${esc(m.title)}</div>
    <svg viewBox="0 0 240 130"><defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FF8AC2" stop-opacity=".55"/><stop offset="1" stop-color="#FF8AC2" stop-opacity="0"/></linearGradient></defs>
    <path d="M0 120 L40 112 L80 100 L120 86 L160 60 L200 40 L240 12 L240 130 L0 130Z" fill="url(#g)"/>
    <path d="M0 120 L40 112 L80 100 L120 86 L160 60 L200 40 L240 12" fill="none" stroke="#D62E73" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/></svg>
    <div class="li">${tick}Faceless</div><div class="li">${tick}AI-made content</div></div>`,

  calendar: (m) => `<div class="card cal"><div class="cap">${m.pins ? "Pins scheduled" : "Your content calendar"}</div><div class="grid">
    ${["M", "T", "W", "T", "F", "S", "S"].map((d) => `<b>${d}</b>`).join("")}
    ${Array.from({ length: 28 }, (_, i) => `<i class="${m.pins || i % 3 !== 2 ? "on" : ""}${i % 5 === 0 ? " hot" : ""}">${i + 1}</i>`).join("")}</div></div>`,

  audit: (m) => `<div class="card audit"><div class="cap">Account audit</div>
    <div class="ig">${Array.from({ length: 6 }, (_, i) => `<i class="g${i}"></i>`).join("")}</div>
    ${m.items.map((t) => `<div class="li">${tick}${esc(t)}</div>`).join("")}</div>`,

  community: () => `<div class="card comm"><div class="cap">Your community</div>
    ${["Welcome! Start here", "Week 1 lesson is live", "Wins thread"].map((t, i) =>
      `<div class="cm"><span class="av a${i}"></span><div><b>${t}</b><div class="ln s"></div></div></div>`).join("")}
    <div class="btn">Join the community</div></div>`,

  post: (m) => `<div class="card fbp"><div class="cm"><span class="av a0"></span><div><b>Featured offer</b><small>Pinned in the group</small></div></div>
    <div class="ptx">${esc(m.text)}</div><div class="pimg"></div><div class="btn">Your link here</div></div>`,

  contacts: (m) => `<div class="card cont"><div class="cap">Brand contacts</div>
    ${m.rows.map((r) => `<div class="ct2"><b>${esc(r)}</b><span class="chip">Email ✓</span></div>`).join("")}<div class="more">+ 145 more</div></div>`,

  reel: (m) => `<div class="phone"><div class="scr reel" style="background-image:url('${vault("faceless-reels")}')"><div class="hk">${esc(m.hook)}</div></div></div>`,
};

// ---------- page ----------
const CSS = `
@font-face{font-family:Inter;src:url('file://${INTER}') format('truetype');font-weight:100 900}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1200px;height:630px;overflow:hidden}
body{font-family:Inter,sans-serif;color:#1A1417;background:#FBF8F5;position:relative}
.glow{position:absolute;right:-120px;top:40px;width:560px;height:560px;border-radius:50%;background:radial-gradient(circle,rgba(255,138,194,.28),rgba(255,138,194,0) 68%)}
.photo{position:absolute;left:0;top:0;width:292px;height:630px;background-size:cover;box-shadow:8px 0 30px rgba(214,46,115,.18)}
.photo::after{content:"";position:absolute;right:0;top:0;width:3px;height:100%;background:#C8A96A}
.copy{position:absolute;left:318px;top:0;width:564px;height:630px;display:flex;flex-direction:column;justify-content:center;gap:0}
.brandline{display:flex;align-items:center;gap:10px;font-weight:700;font-size:16px;letter-spacing:.2em;text-transform:uppercase;color:#1A1417}
.brandline::before{content:"";width:12px;height:12px;border-radius:50%;background:#D62E73;box-shadow:0 0 0 5px rgba(214,46,115,.15)}
.kicker{align-self:flex-start;margin-top:24px;padding:10px 20px 9px;border-radius:999px;background:linear-gradient(135deg,#E8458A,#C4205F);color:#fff;font-weight:800;font-size:21px;letter-spacing:.08em;text-transform:uppercase;box-shadow:0 8px 20px rgba(214,46,115,.35), inset 0 1px 0 rgba(255,255,255,.35)}
h1{margin-top:20px;font-weight:900;font-size:84px;line-height:.98;letter-spacing:-.025em;word-spacing:.05em;text-wrap:balance}
h1 em{font-style:normal;color:#D62E73}
.sub{margin-top:20px;font-weight:600;font-size:24px;line-height:1.3;color:#4A3D42;text-wrap:pretty}
.foot{margin-top:22px;padding-top:14px;border-top:2px solid #C8A96A;font-weight:700;font-size:18px;color:#1A1417;align-self:flex-start;letter-spacing:.01em}
.mockzone{position:absolute;left:888px;top:0;width:300px;height:630px;display:flex;align-items:center;justify-content:center}
.mock{transform:rotate(3deg);position:relative}
.sticker{position:absolute;right:26px;top:26px;width:112px;height:112px;border-radius:50%;background:#fff;color:#D62E73;display:flex;align-items:center;justify-content:center;text-align:center;font-weight:900;font-size:24px;line-height:1;letter-spacing:-.01em;transform:rotate(-10deg);box-shadow:0 10px 24px rgba(214,46,115,.3);z-index:5;padding:10px}
.sticker::before{content:"";position:absolute;inset:7px;border-radius:50%;border:2px dashed #FF8AC2}

.card{width:268px;background:rgba(255,255,255,.94);border:1.5px solid #E6D3A6;border-radius:18px;padding:18px;box-shadow:0 22px 44px rgba(214,46,115,.22),0 4px 10px rgba(26,20,23,.06);font-size:16px}
.cap{font-weight:800;font-size:13px;letter-spacing:.14em;text-transform:uppercase;color:#D62E73;margin-bottom:10px}
.li{display:flex;align-items:center;gap:9px;font-weight:600;font-size:16px;padding:7px 0;border-bottom:1px solid #F1E6EA}
.li:last-child{border-bottom:0}
.tk{flex:none;width:22px;height:22px;border-radius:50%;background:#D62E73;color:#fff;font-size:13px;font-weight:900;display:flex;align-items:center;justify-content:center}
.nm{flex:none;width:24px;height:24px;border-radius:7px;background:#FFE3F0;color:#D62E73;font-weight:900;font-size:14px;display:flex;align-items:center;justify-content:center}
.ln{height:9px;border-radius:5px;background:#EFE4E8;margin:7px 0}.ln.s{width:60%}
.btn{margin-top:12px;text-align:center;padding:10px;border-radius:999px;background:linear-gradient(135deg,#E8458A,#C4205F);color:#fff;font-weight:800;font-size:15px}

.quiz .q{font-weight:800;font-size:19px;line-height:1.2;margin-bottom:12px}
.opt{display:flex;align-items:center;gap:10px;font-weight:600;font-size:16px;padding:10px 12px;border:1.5px solid #EADCE2;border-radius:12px;margin-bottom:8px}
.opt .rd{width:18px;height:18px;border-radius:50%;border:2px solid #CDB9C1;flex:none}
.opt.on{border-color:#D62E73;background:#FFF0F7;color:#1A1417}.opt.on .rd{border:6px solid #D62E73}
.bar{height:8px;border-radius:4px;background:#F1E6EA;margin-top:6px}.bar i{display:block;height:100%;border-radius:4px;background:#D62E73}
.doc .dt{font-weight:900;font-size:21px;letter-spacing:-.02em;margin-bottom:8px;padding-bottom:10px;border-bottom:2px solid #C8A96A}
.doc .li{font-size:17px;padding:10px 0}
.chat .bub{padding:11px 13px;border-radius:14px;font-weight:600;font-size:15px;line-height:1.3;margin-bottom:10px}
.chat .you{background:linear-gradient(135deg,#E8458A,#C4205F);color:#fff;margin-left:26px;border-bottom-right-radius:4px}
.chat .ai{background:#F6EEF1;margin-right:18px;border-bottom-left-radius:4px}
.chat .inp{display:flex;justify-content:space-between;align-items:center;border:1.5px solid #EADCE2;border-radius:999px;padding:8px 8px 8px 14px;color:#9A8A90;font-weight:600}
.chat .snd{width:28px;height:28px;border-radius:50%;background:#D62E73;color:#fff;display:flex;align-items:center;justify-content:center;font-weight:900}
.flow{width:250px;display:flex;flex-direction:column;align-items:stretch}
.node{background:#fff;border:1.5px solid #E6D3A6;border-radius:14px;padding:14px 16px;font-weight:800;font-size:18px;text-align:center;box-shadow:0 12px 26px rgba(214,46,115,.18)}
.node.hot{background:linear-gradient(135deg,#E8458A,#C4205F);color:#fff;border-color:transparent}
.arr{text-align:center;color:#D62E73;font-weight:900;font-size:22px;line-height:1.3}
.browser{padding:0;overflow:hidden;width:272px}
.chrome{display:flex;align-items:center;gap:6px;padding:10px 12px;background:#F6EEF1;border-bottom:1px solid #EADCE2}
.chrome i{width:10px;height:10px;border-radius:50%;background:#E4CBD5}.chrome span{margin-left:6px;font-size:13px;font-weight:600;color:#7A6A70;background:#fff;border-radius:999px;padding:3px 10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.art,.site,.sales2,.shop{padding:14px}
.art .ah{font-weight:900;font-size:20px;line-height:1.12;letter-spacing:-.02em;margin-bottom:6px}
.art .img{height:70px;border-radius:10px;background:linear-gradient(135deg,#FFD6E8,#FFF3F8);margin:10px 0}
.shop{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.shop .ph{height:78px;border-radius:10px}.shop .p0{background:linear-gradient(135deg,#FF8AC2,#FFD6E8)}.shop .p1{background:linear-gradient(135deg,#F3E7D3,#FBF3E8)}.shop .p2{background:linear-gradient(135deg,#FFD6E8,#FFF)}.shop .p3{background:linear-gradient(135deg,#EFD9C6,#FFE9F2)}
.shop .nm{font-weight:700;font-size:14px;margin-top:6px;display:block;width:auto;height:auto;background:none;color:#1A1417}.shop .pr{font-weight:900;font-size:15px;color:#D62E73}
.site .nav{display:flex;justify-content:space-between;align-items:center;font-size:12px;color:#7A6A70;font-weight:600}.site .nav b{font-size:15px;color:#1A1417;font-weight:900}
.site .hero2{margin-top:12px;padding:16px;border-radius:12px;background:linear-gradient(135deg,#FFE3F0,#FFF6FA)}
.site .h,.sales2 .h{font-weight:900;font-size:22px;letter-spacing:-.02em}
.site .posts{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin-top:12px}.site .posts div{height:54px;border-radius:8px;background:#F3E9EC}
.brand .bp{font-weight:800;font-size:19px;line-height:1.25;margin-bottom:14px}
.brand .sw{display:flex;gap:8px;margin-bottom:14px}.brand .sw i{flex:1;height:40px;border-radius:10px;border:1px solid #EADCE2}
.brand .ty{display:flex;align-items:center;gap:12px;font-weight:700}.brand .ty b{font-size:40px;font-weight:900;color:#D62E73}.brand small{font-weight:500;color:#7A6A70}
.week .wd{display:flex;align-items:center;gap:12px;font-weight:700;font-size:17px;padding:9px 0;border-bottom:1px solid #F1E6EA}.week .wd:last-child{border:0}
.week .dy{flex:none;width:62px;text-align:center;padding:5px 0;border-radius:8px;background:#FFE3F0;color:#D62E73;font-weight:900;font-size:13px;letter-spacing:.06em}
.mail{display:flex;align-items:center;gap:10px;padding:9px 0;border-bottom:1px solid #F1E6EA}.mail:last-child{border:0}.mail b{display:block;font-size:15px;font-weight:800}.mail small{font-size:14px;color:#4A3D42;font-weight:600}.mail>div{flex:1}
.mail.new{background:#FFF0F7;border-radius:10px;padding:9px 8px;border:0}
.cmp{display:flex;gap:12px;width:280px}.cmp .col{flex:1}.cmp .col.hot .cap{color:#D62E73}.cmp .col:first-child .cap{color:#9A8A90}
.cmp .x{font-weight:600;font-size:15px;color:#9A8A90;text-decoration:line-through;padding:8px 0;border-bottom:1px solid #F1E6EA}.cmp .li{font-size:15px}
.sent .field{border:2px solid #D62E73;border-radius:12px;padding:12px;font-weight:700;font-size:17px;line-height:1.3;margin-bottom:10px;background:#FFF8FB}
.caret{display:inline-block;width:2px;height:18px;background:#D62E73;vertical-align:-3px;margin-left:2px}
.notif .nt{display:flex;align-items:center;gap:12px;padding:10px;border-radius:12px;background:#FFF6FA;border:1px solid #F4DCE7;margin-bottom:8px}
.notif .ic{flex:none;width:34px;height:34px;border-radius:10px;background:linear-gradient(135deg,#E8458A,#C4205F);color:#fff;font-weight:900;font-size:18px;display:flex;align-items:center;justify-content:center}
.notif b{display:block;font-size:15px;font-weight:800}.notif small{font-size:13px;color:#7A6A70;font-weight:600}
.srch .sb{border:2px solid #D62E73;border-radius:999px;padding:10px 14px;font-weight:800;font-size:17px;margin-bottom:8px}
.srch .sr{padding:8px 6px;font-weight:600;font-size:16px;border-bottom:1px solid #F1E6EA}
.phone{width:230px;height:450px;border-radius:36px;background:#1A1417;padding:10px;box-shadow:0 26px 50px rgba(214,46,115,.3)}
.scr{width:100%;height:100%;border-radius:28px;overflow:hidden;background:#fff}
.pins{display:grid;grid-template-columns:1fr 1fr;gap:7px;padding:8px}
.pin{border-radius:12px;display:flex;align-items:flex-end;padding:9px;font-weight:900;font-size:16px;line-height:1.05;color:#1A1417}
.pin span{background:rgba(255,255,255,.92);padding:5px 7px;border-radius:7px}
.pin.p0{height:230px;background:url('${vault("pinterest-templates")}') 0% 0%/cover}.pin.p1{height:170px;background:url('${vault("printables-planners")}') 20% 0%/cover}
.pin.p2{height:170px;margin-top:0;background:url('${vault("stock-imagery")}') 60% 30%/cover}.pin.p3{height:230px;margin-top:-60px;background:url('${vault("carousel-templates")}') 30% 0%/cover}
.stack{position:relative;width:260px;height:400px}
.cover{position:absolute;width:210px;height:280px;border-radius:14px;padding:18px;background:#fff;border:1.5px solid #E6D3A6;box-shadow:0 20px 40px rgba(214,46,115,.22);display:flex;flex-direction:column}
.cover .brandline{font-size:10px;letter-spacing:.05em;gap:6px;white-space:nowrap}.cover .brandline::before{width:8px;height:8px;box-shadow:none}
.cover .ct{margin-top:auto;font-weight:900;font-size:27px;line-height:1.02;letter-spacing:-.03em}
.cover .fr{margin-top:12px;align-self:flex-start;padding:5px 12px;border-radius:999px;background:#D62E73;color:#fff;font-weight:900;font-size:13px;letter-spacing:.1em}
.cover.c0,.cover.c1{justify-content:flex-start}.cover.c0 .brandline,.cover.c1 .brandline,.cover.c0 .fr,.cover.c1 .fr{display:none}.cover.c0 .ct,.cover.c1 .ct{margin-top:0;font-size:19px}
.cover.c0{left:0;top:0;transform:rotate(-8deg);background:#FFE3F0}.cover.c1{left:30px;top:62px;transform:rotate(-2deg)}.cover.c2{left:50px;top:124px;transform:rotate(5deg);background:linear-gradient(160deg,#fff,#FFF0F7)}
.tiles{display:grid;grid-template-columns:1fr 1fr;gap:8px;padding:10px;width:270px}.tl{height:170px;border-radius:10px;background-size:cover;background-position:center top}
.stack.pr{width:270px;height:440px}
.pc{position:absolute;width:250px;padding:16px;border-radius:16px;background:#fff;border:1.5px solid #E6D3A6;box-shadow:0 18px 36px rgba(214,46,115,.22)}
.pc .pt{font-weight:700;font-size:17px;line-height:1.3}
.pc .cp{margin-top:10px;display:inline-block;padding:6px 14px;border-radius:999px;background:#FFE3F0;color:#D62E73;font-weight:800;font-size:13px}
.pc.c0{left:0;top:0;transform:rotate(-6deg)}.pc.c1{left:14px;top:150px;transform:rotate(-1deg)}.pc.c2{left:6px;top:300px;transform:rotate(4deg);background:linear-gradient(135deg,#E8458A,#C4205F);border-color:transparent;color:#fff}.pc.c2 .cap{color:#FFE3F0}.pc.c2 .cp{background:#fff}
.chart svg{width:100%;height:130px;margin-bottom:6px}
.cal .grid{display:grid;grid-template-columns:repeat(7,1fr);gap:5px;text-align:center}
.cal b{font-size:12px;color:#9A8A90;font-weight:800}
.cal i{font-style:normal;font-size:12px;font-weight:700;color:#9A8A90;height:32px;border-radius:7px;background:#F6EEF1;display:flex;align-items:center;justify-content:center}
.cal i.on{background:#FFD6E8;color:#1A1417}.cal i.hot{background:#D62E73;color:#fff}
.audit .ig{display:grid;grid-template-columns:repeat(3,1fr);gap:4px;margin-bottom:8px}.audit .ig i{height:62px;border-radius:6px;background:url('${vault("stock-imagery")}') center/300%}
.audit .g1{background-position:50% 0!important}.audit .g2{background-position:100% 0!important}.audit .g3{background-position:0 100%!important}.audit .g4{background-position:50% 100%!important}.audit .g5{background-position:100% 100%!important}
.audit .li{padding:5px 0;font-size:15px}
.cm{display:flex;align-items:center;gap:10px;padding:8px 0;border-bottom:1px solid #F1E6EA}.cm b{font-size:15px;font-weight:800;display:block}.cm small{font-size:13px;color:#7A6A70;font-weight:600}.cm>div{flex:1}
.av{flex:none;width:36px;height:36px;border-radius:50%;background:linear-gradient(135deg,#FF8AC2,#D62E73)}.av.a1{background:linear-gradient(135deg,#F3E7D3,#C8A96A)}.av.a2{background:linear-gradient(135deg,#FFD6E8,#FF8AC2)}
.fbp .ptx{font-weight:700;font-size:16px;line-height:1.3;margin:10px 0}.fbp .pimg{height:110px;border-radius:10px;background:url('${vault("announcement-posts")}') center/cover}
.cont .ct2{display:flex;justify-content:space-between;align-items:center;padding:9px 0;border-bottom:1px solid #F1E6EA;font-size:16px}.cont b{font-weight:800}
.chip{font-size:12px;font-weight:800;color:#D62E73;background:#FFE3F0;border-radius:999px;padding:4px 9px}
.more{margin-top:10px;font-weight:900;color:#D62E73;font-size:17px}
.reel{background-size:170%;background-position:65% 40%;display:flex;align-items:center;padding:16px}
.reel .hk{background:#fff;border-radius:12px;padding:12px;font-weight:900;font-size:22px;line-height:1.1;letter-spacing:-.02em;box-shadow:0 8px 20px rgba(0,0,0,.2)}
`;

function page(p) {
  const [src, pos] = PHOTOS[p.photo] ?? PHOTOS.laptopPink;
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>
  <div class="glow"></div>
  <div class="photo" style="background-image:url('${file(src)}');background-position:${pos}"></div>
  <div class="copy">
    <div class="brandline">The Digital Income Edit™</div>
    <div class="kicker">${esc(p.kicker)}</div>
    <h1>${pinkify(p.headline)}</h1>
    <div class="sub">${esc(p.sub)}</div>
    <div class="foot">thedigitalincomeedit.com</div>
  </div>
  <div class="mockzone"><div class="mock">${(MOCKS[p.mock.kind] ?? MOCKS.doc)(p.mock)}</div></div>
  ${p.sticker ? `<div class="sticker">${esc(p.sticker)}</div>` : ""}
  </body></html>`;
}

// ---------- find every product page ----------
function routesIn(dir, prefix) {
  const abs = join(ROOT, "src/pages", dir);
  if (!existsSync(abs)) return [];
  return readdirSync(abs).filter((f) => f.endsWith(".astro") && !f.startsWith("[")).map((f) => {
    const name = f.replace(/\.astro$/, "");
    return { route: name === "index" ? prefix : `${prefix}/${name}`, src: join(abs, f) };
  });
}
const pages = [
  ...routesIn("resources", "/resources"), ...routesIn("shop", "/shop"),
  ...routesIn("vault", "/vault"), ...routesIn("go", "/go"),
  { route: "/weekend-ecosystem/preview", src: join(ROOT, "src/pages/weekend-ecosystem/preview.astro") },
];

// A product with no hand-written entry: build one from the page itself.
function fallback(srcFile) {
  const s = readFileSync(srcFile, "utf8");
  const pick = (re) => (s.match(re) || [])[1];
  const name = pick(/const NAME = "([^"]+)"/) || pick(/title="([^"—|]+)/) || "The Digital Income Edit";
  const price = pick(/const PRICE = "([^"]+)"/);
  const lede = pick(/go-lede">([^<]+)/) || pick(/description="([^"]{0,90})/) || "";
  const free = !price || price === "$0";
  return {
    kicker: free ? "Free" : `${price}`, headline: name.trim(), sub: lede.split(/(?<=\.)\s/)[0],
    photo: "laptopPink", sticker: free ? "Free" : price,
    mock: { kind: "stack", covers: [name.trim().slice(0, 28), "The Digital Income Edit™", name.trim().slice(0, 28)] },
  };
}

const only = process.argv.slice(2);
const manifest = {};
const browser = await chromium.launch();
const tab = await browser.newPage({ viewport: { width: 1200, height: 630 } });
const tmp = join(HERE, ".render.html");
const missing = [];

for (const { route, src } of pages) {
  const slug = route.replace(/^\//, "").replace(/\//g, "-");
  const outFile = join(OUT, `${slug}.jpg`);
  let p = PRODUCTS[route];
  if (!p) { missing.push(route); p = fallback(src); }
  if (!only.length || only.some((o) => slug.includes(o))) {
    writeFileSync(tmp, page(p));
    await tab.goto("file://" + tmp);
    await tab.evaluate(() => document.fonts.ready);
    // Shrink the headline until the copy column fits with room to breathe.
    await tab.evaluate(() => {
      const h = document.querySelector("h1"), c = document.querySelector(".copy");
      let size = 84;
      const fits = () => [...c.children].reduce((a, e) => a + e.getBoundingClientRect().height, 0) + 110 < 600;
      while (!fits() && size > 56) { size -= 2; h.style.fontSize = size + "px"; }
    });
    await tab.waitForTimeout(150);
    writeFileSync(outFile, await tab.screenshot({ type: "jpeg", quality: 90 }));
    console.log("rendered", route);
  }
  if (existsSync(outFile)) {
    const v = createHash("sha1").update(readFileSync(outFile)).digest("hex").slice(0, 8);
    manifest[route] = `/og/p/${slug}.jpg?v=${v}`;
  }
}
await browser.close();

writeFileSync(MANIFEST,
  "// Generated by ops/og-thumbnails/render.mjs. Do not edit by hand; edit ops/og-thumbnails/products.mjs and re-run.\n" +
  "// Page path → link thumbnail (og:image). PageLayout uses this before any ogImage prop.\n" +
  "export default " + JSON.stringify(manifest, null, 2) + ";\n");

if (missing.length) {
  console.log("\nNo hand-written thumbnail yet (auto-built from the page; add a line to products.mjs):");
  for (const m of missing) console.log("  " + m);
}
