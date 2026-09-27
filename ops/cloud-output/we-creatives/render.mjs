// The Weekend Ecosystem(TM) cover, carousel, OG and Meta ad creatives.
// HTML composed in code, screenshotted to PNG with Playwright + Chromium.
//
// Run from the repo root:   node ops/cloud-output/we-creatives/render.mjs
// Only some files:          node ops/cloud-output/we-creatives/render.mjs ad-payplan
//
// Needs Node 22 and Playwright (npm i -g playwright if missing). Fonts are pulled once from
// raw.githubusercontent.com/google/fonts into ./fonts (not committed).
// Placeholder photos: drop the generated file into ./photos/ under the name in PHOTOS below
// and run again. Until the file exists, that image renders with a clean placeholder box.

import { existsSync, mkdirSync, writeFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

// Playwright from the repo if installed, else the global install.
let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright")); }

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const OUT = join(HERE, "png");
const FONTS = join(HERE, "fonts");
mkdirSync(OUT, { recursive: true });
mkdirSync(FONTS, { recursive: true });

// ---------- fonts ----------
const FONT_SRC = {
  "Newsreader.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/newsreader/Newsreader%5Bopsz,wght%5D.ttf",
  "Inter.ttf": "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf",
};
for (const [name, url] of Object.entries(FONT_SRC)) {
  const p = join(FONTS, name);
  if (existsSync(p)) continue;
  const r = await fetch(url);
  if (!r.ok) throw new Error(`Font download failed: ${url} (${r.status})`);
  writeFileSync(p, Buffer.from(await r.arrayBuffer()));
}

// ---------- photos ----------
// Every photo already in the repo, plus the one new photo this set asks for.
const PHOTOS = {
  porch:    { src: "public/images/we/cover-sofa.jpg" },          // porch at sunrise, red barn, Player Two? mug
  loftCross:{ src: "public/images/we/cover-kitchen.jpg" },       // attic loft, cross-legged, laptop on lap
  loftFace: { src: "public/images/we/preview-hero.jpg" },        // attic loft, facing camera, closed laptop
  loftLap:  { src: "ops/cloud-output/we-creatives/photos/loft-lap-no-logo.jpg" }, // the old preview-working.jpg (logo retouched), kept for ad-build after the page got the new kitchen photo     // attic loft, laptop on lap, barn in window
  loftWide: { src: "public/images/we/hub-header.jpg" },          // attic loft, wide, typing at the pink desk
  sofa:     { src: "ops/cloud-output/we-creatives/photos/sofa-tumbler-no-lettering.jpg" }, // public/images/we/hook-blog-posts.jpg with its baked-in lettering cropped off (top 568 px)
  pasture:  { src: "ops/cloud-output/we-creatives/photos/pay-plan-pasture-blanket.jpg" }, // generated 27 Sep 2026 from the PHOTO_PROMPTS.md prompt; laptop logo and sneaker patch retouched out
};

function photoUrl(key) {
  const p = join(ROOT, PHOTOS[key].src);
  return existsSync(p) ? "file://" + p : null;
}

// ---------- sizes ----------
const SIZES = {
  sq:  { w: 1080, h: 1080 },
  p45: { w: 1080, h: 1350 },
  st:  { w: 1080, h: 1920 },
  ls:  { w: 1200, h: 628 },
  og:  { w: 1200, h: 630 },
};

// ---------- shared CSS ----------
const CSS = `
@font-face{font-family:Newsreader;src:url("file://${FONTS}/Newsreader.ttf") format("truetype");font-weight:200 800;font-style:normal}
@font-face{font-family:Inter;src:url("file://${FONTS}/Inter.ttf") format("truetype");font-weight:100 900;font-style:normal}
:root{--ink:#1A1417;--ink-soft:#4A3F44;--hot:#D62E73;--hot-deep:#A81F57;--bub:#FF8AC2;--gold:#C8A96A;--cream:#FBF8F5;
  --glass:rgba(255,253,252,.84);--edge:rgba(200,169,106,.6);
  --shadow:0 40px 70px -34px rgba(214,46,115,.45),0 14px 30px -16px rgba(26,20,23,.18)}
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:var(--W);height:var(--H);overflow:hidden}
body{font-family:Inter,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;
  background:
    radial-gradient(55% 40% at 0% 100%,rgba(255,138,194,.10),transparent 70%),
    linear-gradient(165deg,#FFFEFC 0%,#FBF8F5 55%,#F6EFEA 100%)}
.stage{position:relative;width:var(--W);height:var(--H);overflow:hidden}
.ph{position:absolute;overflow:hidden}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.ph.fadeL{box-shadow:-34px 0 60px -34px rgba(26,20,23,.28);border-left:2px solid var(--gold)}
.ph.fadeT{box-shadow:0 -34px 60px -34px rgba(26,20,23,.28);border-top:2px solid var(--gold)}
.ph.fadeLR{-webkit-mask-image:linear-gradient(90deg,#000 70%,transparent 100%)}
.ph.fadeRL{-webkit-mask-image:linear-gradient(270deg,#000 70%,transparent 100%)}
.ph.round{border-radius:calc(28px*var(--u));border:1px solid var(--edge);box-shadow:var(--shadow)}
.ph .pht{width:100%;height:100%;display:grid;place-items:center;align-content:var(--phAlign,center);text-align:center;padding:40px;
  background:repeating-linear-gradient(135deg,#F6ECE8 0 18px,#FBF3F0 18px 36px);border:3px dashed rgba(214,46,115,.45);
  font:700 calc(20px*var(--u))/1.45 Inter,sans-serif;letter-spacing:2px;text-transform:uppercase;color:var(--hot)}
.ph .pht small{display:block;margin-top:10px;font-weight:600;letter-spacing:.5px;text-transform:none;color:var(--ink-soft);font-size:max(16px,calc(17px*var(--u)))}
.goldline{position:absolute;height:1px;background:linear-gradient(90deg,var(--gold),rgba(200,169,106,0))}
.copy{position:absolute;display:flex;flex-direction:column;z-index:3}
.brand{display:inline-flex;align-items:center;gap:max(16px,calc(12px*var(--u)));font:700 max(16px,calc(15px*var(--u)))/1 Inter,sans-serif;letter-spacing:.24em;text-transform:uppercase;color:var(--ink)}
.dot{width:max(16px,calc(11px*var(--u)));height:max(16px,calc(11px*var(--u)));border-radius:50%;background:var(--hot);box-shadow:0 0 0 calc(5px*var(--u)) rgba(214,46,115,.16)}
.copy .kicker{margin-top:auto}.copy>.cta,.copy>.sign{margin-bottom:auto}
.kicker{font:800 max(16px,calc(17px*var(--u)))/1.3 Inter,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:var(--ink-soft)}
h1{font-family:Newsreader,serif;font-weight:600;color:var(--ink);letter-spacing:-.015em;line-height:1.02;font-variation-settings:"opsz" 72}
h1 em{font-style:normal;color:var(--hot)}
h1,.stats span,.who{text-wrap:balance}
p,li,.sub,.quote{text-wrap:pretty}
.foot i,.foot span{white-space:nowrap}
.sub{font:500 calc(24px*var(--u))/1.42 Inter,sans-serif;color:var(--ink-soft)}
.sub strong{color:var(--ink);font-weight:700}
.card{background:var(--glass);-webkit-backdrop-filter:blur(16px) saturate(140%);backdrop-filter:blur(16px) saturate(140%);
  border:1px solid var(--edge);border-radius:calc(22px*var(--u));box-shadow:var(--shadow);padding:calc(26px*var(--u)) calc(30px*var(--u))}
.hotcard{position:relative;overflow:hidden;border-radius:calc(22px*var(--u));padding:calc(26px*var(--u)) calc(30px*var(--u));color:#fff;
  background:linear-gradient(140deg,#F0589A 0%,var(--hot) 50%,var(--hot-deep) 100%);box-shadow:0 36px 60px -30px rgba(168,31,87,.65),0 12px 26px -14px rgba(26,20,23,.25)}
.hotcard::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.34) 0%,rgba(255,255,255,0) 38%);pointer-events:none}
.ticks{list-style:none;display:grid;gap:max(16px,calc(14px*var(--u)))}
.ticks li{position:relative;padding-left:calc(44px*var(--u));font:600 calc(23px*var(--u))/1.3 Inter,sans-serif;color:var(--ink)}
.ticks li span{display:block;font-weight:500;font-size:.8em;color:var(--ink-soft);margin-top:3px}
.ticks li::before{content:"\\2713";position:absolute;left:0;top:-1px;width:calc(30px*var(--u));height:calc(30px*var(--u));border-radius:50%;display:grid;place-items:center;
  background:var(--ink);color:#fff;font:800 max(16px,calc(16px*var(--u)))/1 Inter,sans-serif}
.cta{align-self:flex-start;display:inline-flex;align-items:center;gap:.6em;padding:calc(20px*var(--u)) calc(38px*var(--u));border-radius:999px;
  background:linear-gradient(135deg,#E8458A 0%,var(--hot) 55%,var(--hot-deep) 100%);color:#fff;
  font:800 calc(19px*var(--u))/1 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;box-shadow:0 18px 34px -16px rgba(168,31,87,.7)}
.sticker{position:absolute;z-index:4;display:grid;place-items:center;width:calc(150px*var(--u));height:calc(150px*var(--u));border-radius:50%;
  font:800 max(16px,calc(16px*var(--u)))/1.2 Inter,sans-serif;letter-spacing:.1em;text-transform:uppercase;text-align:center;color:var(--ink);background:#fff;
  box-shadow:0 22px 40px -18px rgba(168,31,87,.55),0 6px 14px -6px rgba(26,20,23,.2)}
.sticker>span{display:grid;place-items:center;width:84%;height:84%;border-radius:50%;border:2px dashed currentColor;padding:6px}
.sticker.bub{background:#fff;color:var(--ink)}

.sign{font-family:Newsreader,serif;font-weight:600;color:var(--ink);font-size:calc(30px*var(--u))}
.price{display:flex;align-items:flex-end;gap:calc(18px*var(--u));flex-wrap:wrap}
.price b{font-family:Newsreader,serif;font-weight:600;line-height:1}
.price .or{font:700 max(16px,calc(15px*var(--u)))/1 Inter,sans-serif;letter-spacing:.2em;text-transform:uppercase;opacity:.85;padding-bottom:.5em}
.stars{color:var(--ink);letter-spacing:.14em;font-size:calc(26px*var(--u))}
.quote{font-family:Newsreader,serif;font-weight:600;line-height:1.28;color:var(--ink)}
.quote::before{content:"\\201C"}
.quote::after{content:"\\201D"}
.who{font:700 max(16px,calc(15px*var(--u)))/1.4 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft)}
.who b{color:var(--ink)}
.two{display:grid;grid-template-columns:1.25fr 1fr;gap:max(16px,calc(16px*var(--u)))}
.two h3{font:800 max(16px,calc(15px*var(--u)))/1.2 Inter,sans-serif;letter-spacing:.18em;text-transform:uppercase;margin-bottom:max(16px,calc(12px*var(--u)))}
.two ul{list-style:none;display:grid;gap:calc(9px*var(--u));font:600 calc(19px*var(--u))/1.3 Inter,sans-serif}
.two .card h3{color:var(--ink-soft)}
.two .card li::before{content:"+ ";color:var(--ink);font-weight:800}
.two .hotcard li::before{content:"\\2192  ";font-weight:800}
.stats{display:grid;grid-template-columns:1fr 1fr;gap:max(16px,calc(16px*var(--u)))}
.stats .card{padding:calc(22px*var(--u)) calc(24px*var(--u))}
.stats b{display:block;font-family:Newsreader,serif;font-weight:600;font-size:calc(66px*var(--u));line-height:1;color:var(--ink)}
.stats span{display:block;margin-top:calc(8px*var(--u));font:700 max(16px,calc(15px*var(--u)))/1.3 Inter,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--ink)}
.stats .hotcard b{color:#fff;font-size:calc(40px*var(--u));line-height:1.05}
.stats .hotcard span{color:#fff}
.foot{display:flex;justify-content:space-between;align-items:center;gap:max(16px,calc(16px*var(--u)));padding-top:max(16px,calc(16px*var(--u)));border-top:1px solid rgba(200,169,106,.55);
  font:700 max(16px,calc(15px*var(--u)))/1.2 Inter,sans-serif;letter-spacing:.06em;color:var(--ink)}
.foot i{font-style:normal;font-weight:600;letter-spacing:.04em;color:var(--ink-soft)}
.mid{display:flex;flex-direction:column;gap:inherit;margin:auto 0}
.storycard{background:rgba(255,253,252,.9);position:absolute}
.storycard .mid{margin:0}
.chips{display:flex;flex-wrap:wrap;gap:max(16px,calc(10px*var(--u)))}
.chips span{padding:max(16px,calc(10px*var(--u))) max(16px,calc(16px*var(--u)));border-radius:999px;background:var(--glass);border:1px solid var(--edge);
  font:700 max(16px,calc(15px*var(--u)))/1 Inter,sans-serif;letter-spacing:.08em;color:var(--ink);box-shadow:0 10px 20px -14px rgba(214,46,115,.5)}
`;

// ---------- building blocks ----------
const photo = (key, style, cls = "", pos = "50% 40%", zoom = 1) => {
  const url = photoUrl(key);
  const inner = url
    ? `<img src="${url}" style="object-position:${pos};transform:scale(${zoom});transform-origin:${pos}">`
    : `<div class="pht"><div>Photo placeholder<small>${PHOTOS[key].src.split("/").pop()}<br>Prompt: PHOTO_PROMPTS.md</small></div></div>`;
  return `<div class="ph ${url ? cls : cls.replace(/fade\w+/, "")}" style="${style}">${inner}</div>`;
};
const brand = () => `<div class="brand"><span class="dot"></span>The Digital Income Edit&trade;</div>`;
const sticker = (html, style, bub = false) => `<div class="sticker${bub ? " bub" : ""}" style="${style}"><span>${html}</span></div>`;

// ---------- the five ad angles (copy shared across sizes) ----------
const ANGLES = {
  ideal: {
    photo: "porch", posSt: "50% 0%", pos: { sq: "55% 40%", p45: "55% 40%", st: "55% 45%", ls: "55% 30%" },
    kicker: "The Weekend Ecosystem&trade;",
    h1: `A business that keeps selling <em>on the Tuesday you're too tired to post.</em>`,
    sub: `Your own website, blog and email list, built in one weekend from content you already wrote.`,
    body: (s) => `<div class="card"><ul class="ticks">
      <li>Your time back</li><li>Your domain, your list</li><li>Your face, optional</li></ul></div>`,
    trust: "Every future update, free", cta: "See inside, free",
  },
  preview: {
    photo: "loftFace", posSt: "60% 0%", pos: { sq: "63% 35%", p45: "61% 35%", st: "60% 40%", ls: "60% 30%" },
    kicker: "Free look inside &middot; no email",
    h1: `See the whole machine <em>before you buy a thing.</em>`,
    sub: `The free preview of The Weekend Ecosystem&trade;. <strong>No email, no card, <span style="white-space:nowrap">no sign-up.</span></strong>`,
    body: (s) => `<div class="chips"><span>The module index</span><span>A real module</span><span>The prompt cards</span><span>Real output</span><span>The certificate</span></div>`,
    trust: "Free preview &middot; no email", cta: "Open the preview",
  },
  build: {
    photo: "loftLap", photoLs: "loftWide", posSt: "100% 0%", zoomSt: 1.26, pos: { sq: "94% 40%", p45: "91% 40%", st: "80% 40%", ls: "80% 40%" },
    kicker: "&ldquo;But I can't build a website.&rdquo;",
    h1: `You won't have to. <em>Claude writes every file.</em>`,
    sub: `No code, no developer, no WordPress. Three moves are yours.`,
    body: (s) => `<div class="two">
      <div class="card"><h3>Claude does</h3><ul><li>Every file your site needs</li><li>Your articles and SEO</li><li>Your email capture</li></ul></div>
      <div class="hotcard"><h3>You do</h3><ul><li>Paste the prompt</li><li>Read what came back</li><li>Say yes</li></ul></div></div>`,
    trust: "Every future update, free", cta: "See how it works",
  },
  payplan: {
    photo: "pasture", posSt: "78% 0%", pos: { sq: "86% 40%", p45: "84% 40%", st: "78% 0%", ls: "70% 40%" },
    kicker: "The Weekend Ecosystem&trade;",
    h1: `Build it this weekend. <em>Pay in three.</em>`,
    sub: `Your website, blog and email list, built from content you already wrote. <strong>Every future update, free.</strong>`,
    body: (s) => `<div class="hotcard"><div class="price"><b style="font-size:calc(${s === "ls" ? 58 : 74}px*var(--u))">3 &times; $33.33</b><span class="or">or $97 once</span></div></div>`,
    trust: "Both options at checkout", cta: "See inside, free",
  },
  review: {
    photo: "sofa", posSt: "78% 0%", pos: { sq: "62% 50%", p45: "62% 50%", st: "60% 50%", ls: "60% 40%" },
    kicker: "A member review &middot; Skool",
    h1: `Her website, <em>in her words.</em>`,
    sub: null,
    body: (s) => `<div class="card"><div class="stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
      <p class="quote" style="font-size:calc(${s === "ls" ? 23 : 29}px*var(--u));margin:max(16px,calc(12px*var(--u))) 0 max(16px,calc(14px*var(--u)))">In 3 days I had a beautiful website/blog set up and everything connected and looks way better than the word press site would have looked.</p>
      <p class="who"><b>Tina Alexander</b> &middot; paying member</p></div>`,
    trust: "Posted on Skool under her name", cta: "See what she used",
  },
};

// Layout per ad size. Photo panel on the right (or bottom for stories) with a hard gold seam,
// cream copy column left (or top). Brand line top, copy centred, web address and a trust line at the foot.
// No stickers on ads: they read as "limited offer" stamps on a cold feed.
function adHTML(angleKey, size) {
  const a = ANGLES[angleKey];
  const { w, h } = SIZES[size];
  const key = (size === "ls" && a.photoLs) || (size === "st" && a.photoSt) || a.photo;
  const pos = a.pos[size];
  let ph, copy, u, h1size;
  if (size === "sq") {
    u = 1; h1size = 64;
    ph = photo(key, "right:0;top:0;width:470px;height:1080px", "fadeL", pos);
    copy = `left:64px;top:64px;width:500px;bottom:56px;gap:24px`;
  } else if (size === "p45") {
    u = 1.05; h1size = 70;
    ph = photo(key, "right:0;top:0;width:480px;height:1350px", "fadeL", pos);
    copy = `left:64px;top:80px;width:500px;bottom:72px;gap:30px`;
  } else if (size === "st") {
    // Stories: full-bleed photo, her face in the top half, copy on one frosted card.
    // Every word sits between y=250 and y=1580 (Meta safe area).
    u = 1.12; h1size = 66;
    ph = photo(key, "left:0;top:0;width:1080px;height:1920px;--phAlign:start;padding-top:0", "", a.posSt || "50% 0%", a.zoomSt || 1);
    copy = `left:56px;right:56px;bottom:340px;gap:20px;padding:40px 44px 34px`;
    } else {
    u = 0.82; h1size = 50;
    ph = photo(key, "right:0;top:0;width:470px;height:628px", "fadeL", pos);
    copy = `left:48px;top:36px;width:640px;bottom:30px;gap:14px`;
  }
  const sub = a.sub && size !== "ls" && size !== "st" ? `<p class="sub">${a.sub}</p>` : "";
  const body = `
    ${brand()}
    <div class="mid">
      <p class="kicker">${a.kicker}</p>
      <h1 style="font-size:${h1size}px">${a.h1}</h1>
      ${sub}
      ${a.body(size)}
      <div class="cta">${a.cta} <span>&rarr;</span></div>
    </div>
    <div class="foot"><span>thedigitalincomeedit.com</span><i>${a.trust}</i></div>`;
  return page(w, h, u, `${ph}<div class="copy${size === "st" ? " card storycard" : ""}" style="${copy}">${body}</div>`);
}

function page(w, h, u, inner) {
  return `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head>
  <body style="--W:${w}px;--H:${h}px;--u:${u}"><div class="stage">${inner}</div></body></html>`;
}

// ---------- Beacons carousel, OG, Kit hero ----------
function heroHTML(kit) {
  const u = 1;
  const kitCard = kit
    ? `<div class="hotcard" style="padding:22px 28px">
         <p style="font:800 15px/1.3 Inter,sans-serif;letter-spacing:.18em;text-transform:uppercase;opacity:.95">Free until 4 Oct, 11:59 pm Eastern</p>
         <p style="font-family:Newsreader,serif;font-weight:600;font-size:34px;line-height:1.1;margin-top:8px">+ The Keep It Running Kit</p>
         <p style="font:600 18px/1.35 Inter,sans-serif;margin-top:6px;opacity:.95">Six of my paid guides, in your access email.</p></div>`
    : `<div class="card" style="padding:22px 28px"><div class="price" style="color:var(--ink)"><b style="font-size:58px">$97</b><span class="or" style="color:var(--ink-soft)">one-time &middot; or 3 &times; $33.33</span></div>
         <p style="font:600 17px/1.35 Inter,sans-serif;color:var(--ink-soft);margin-top:10px">Every future update, free.</p></div>`;
  const inner = `
    ${photo("loftCross", "right:0;top:0;width:470px;height:1080px", "fadeL", "78% 40%")}
    <div class="goldline" style="left:64px;top:118px;width:200px"></div>
    <div class="copy" style="left:64px;top:70px;width:514px;bottom:56px;gap:22px">
      ${brand()}
      <div style="height:10px"></div>
      <p class="kicker">Standalone course</p>
      <h1 style="font-size:84px;line-height:.98">The Weekend <em>Ecosystem<sup style="font-size:.38em;vertical-align:1.25em;margin-left:2px">&trade;</sup></em></h1>
      <p class="sub" style="font-size:27px">Your website + blog, <strong>built from what you already have.</strong></p>
      ${kitCard}
      <p class="sign" style="margin-top:auto">xoxo, Jodie</p>
      <div class="foot"><span>thedigitalincomeedit.com</span><i>${kit ? "$97 one-time &middot; or 3 &times; $33.33" : "Both options at checkout"}</i></div>
    </div>
    ${sticker("No code<br>no camera", "left:430px;top:150px;transform:rotate(9deg);width:136px;height:136px")}
`;
  return page(1080, 1080, u, inner);
}

function getHTML() {
  const inner = `
    ${photo("loftWide", "right:0;top:0;width:470px;height:1080px", "fadeL", "84% 40%")}
    <div class="goldline" style="left:64px;top:118px;width:200px"></div>
    <div class="copy" style="left:64px;top:70px;width:514px;bottom:56px;gap:22px">
      ${brand()}
      <div style="height:10px"></div>
      <p class="kicker">What you get</p>
      <h1 style="font-size:66px">Everything in it, <em>one payment, forever.</em></h1>
      <div class="stats">
        <div class="card"><b>22</b><span>Modules, in build order</span></div>
        <div class="card"><b>36</b><span>Prompts, verbatim</span></div>
        <div class="card"><b>3</b><span>Vaults: prompts, fixes, templates</span></div>
        <div class="hotcard"><b>Every update</b><span>Free, forever</span></div>
      </div>
      <p class="sub" style="font-size:21px">Plus the Quick Sheet, the Ask-For-It List, progress tracking and a certificate.</p>
      <div class="foot" style="margin-top:auto"><span>thedigitalincomeedit.com</span><i>$97 one-time &middot; or 3 &times; $33.33</i></div>
    </div>`;
  return page(1080, 1080, 1, inner);
}

function reviewCardHTML() {
  const inner = `
    ${photo("sofa", "right:0;top:0;width:470px;height:1080px", "fadeL", "64% 50%")}
    <div class="goldline" style="left:64px;top:118px;width:200px"></div>
    <div class="copy" style="left:64px;top:70px;width:514px;bottom:56px;gap:22px">
      ${brand()}
      <div style="height:10px"></div>
      <p class="kicker">A member review &middot; Skool</p>
      <h1 style="font-size:64px">Her website, <em>in her words.</em></h1>
      <div class="card" style="padding:32px 34px">
        <div class="stars" style="font-size:30px">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="quote" style="font-size:33px;margin:14px 0 18px">In 3 days I had a beautiful website/blog set up and everything connected and looks way better than the word press site would have looked.</p>
        <p class="who"><b>Tina Alexander</b> &middot; paying member</p>
      </div>
      <div class="foot" style="margin-top:auto"><span>thedigitalincomeedit.com</span><i>Posted on Skool under her name</i></div>
    </div>`;
  return page(1080, 1080, 1, inner);
}

// OG 1200 x 630: every word inside the centre 600 px (x 300 to 900). Photos fill the two sides.
function ogHTML() {
  const inner = `
    ${photo("porch", "left:0;top:0;width:420px;height:630px", "fadeLR", "50% 35%")}
    ${photo("sofa", "right:0;top:0;width:420px;height:630px", "fadeRL", "68% 30%")}
    <div class="card" style="position:absolute;left:310px;top:44px;width:580px;height:542px;padding:34px 38px;display:flex;flex-direction:column;gap:16px;z-index:3;text-align:center;align-items:center">
      ${brand()}
      <div class="goldline" style="position:static;width:120px;background:var(--gold)"></div>
      <h1 style="font-size:50px;line-height:1.02">A business that keeps selling <em>on the Tuesday you're too tired to post.</em></h1>
      <p class="sub" style="font-size:19px">Your website, blog and email list, built in one weekend from content you already wrote.</p>
      <div class="cta" style="align-self:center;font-size:16px;padding:16px 30px">$97 or 3 &times; $33.33 <span>&rarr;</span></div>
      <div class="foot" style="margin-top:auto;align-self:stretch"><span>thedigitalincomeedit.com</span><i>Every future update, free</i></div>
    </div>`;
  return page(1200, 630, 1, inner);
}


// Preview page OG 1200 x 630: same frame as the sales OG, preview message. Every word in the centre 600 px.
// Uses preview-hero.jpg and hub-header.jpg, so dropping new photos in and re-running refreshes it.
function ogPreviewHTML() {
  const inner = `
    ${photo("loftFace", "left:0;top:0;width:420px;height:630px", "fadeLR", "100% 25%")}
    ${photo("loftWide", "right:0;top:0;width:420px;height:630px", "fadeRL", "60% 40%")}
    <div class="card" style="position:absolute;left:310px;top:44px;width:580px;height:542px;padding:34px 38px;display:flex;flex-direction:column;gap:16px;z-index:3;text-align:center;align-items:center">
      ${brand()}
      <div class="goldline" style="position:static;width:120px;background:var(--gold)"></div>
      <h1 style="font-size:54px;line-height:1.02">See the whole machine <em>before you buy a thing.</em></h1>
      <p class="sub" style="font-size:19px">The module index, a real module, the prompt cards, real output and the certificate. <strong>No email, no card.</strong></p>
      <div class="cta" style="align-self:center;font-size:16px;padding:16px 30px">Open the preview <span>&rarr;</span></div>
      <div class="foot" style="margin-top:auto;align-self:stretch"><span>thedigitalincomeedit.com</span><i>Free preview &middot; no email</i></div>
    </div>`;
  return page(1200, 630, 1, inner);
}

// ---------- the job list ----------
const JOBS = [
  ["beacons-1-hero", () => heroHTML(false), 1080, 1080],
  ["beacons-2-what-you-get", getHTML, 1080, 1080],
  ["beacons-3-review", reviewCardHTML, 1080, 1080],
  ["beacons-hero-keep-it-running-kit", () => heroHTML(true), 1080, 1080],
  ["og-weekend-ecosystem-2026-09", ogHTML, 1200, 630],
  ["og-weekend-ecosystem-preview", ogPreviewHTML, 1200, 630],
];
for (const angle of Object.keys(ANGLES)) {
  for (const [size, tag] of [["sq", "1080x1080"], ["p45", "1080x1350"], ["st", "1080x1920"], ["ls", "1200x628"]]) {
    JOBS.push([`ad-${angle}-${tag}`, () => adHTML(angle, size), SIZES[size].w, SIZES[size].h]);
  }
}

const only = process.argv.slice(2);
const browser = await chromium.launch();
const ctx = await browser.newContext({ deviceScaleFactor: 1 });
const pg = await ctx.newPage();
for (const [name, fn, w, h] of JOBS) {
  if (only.length && !only.some((o) => name.includes(o))) continue;
  await pg.setViewportSize({ width: w, height: h });
  const html = fn();
  const tmp = join(HERE, ".render.html");
  writeFileSync(tmp, html);
  await pg.goto("file://" + tmp, { waitUntil: "load" });
  await pg.evaluate(() => document.fonts.ready);
  // Fail loudly on any text that spills out of its box.
  const spill = await pg.evaluate(() => {
    const W = innerWidth, H = innerHeight, bad = [];
    document.querySelectorAll(".copy, .card, .hotcard, .sticker, h1, p").forEach((el) => {
      const r = el.getBoundingClientRect();
      if (r.right > W + 1 || r.bottom > H + 1 || r.left < -1 || r.top < -1) bad.push(el.className || el.tagName);
      if (el.scrollHeight > el.clientHeight + 2 && getComputedStyle(el).overflow !== "visible") bad.push("overflow:" + (el.className || el.tagName));
    });
    const c = document.querySelector(".copy");
    if (c && c.scrollHeight > c.clientHeight + 2) bad.push("copy column too tall");
    return bad;
  });
  await pg.screenshot({ path: join(OUT, name + ".png") });
  console.log(`${spill.length ? "CHECK" : "ok   "} ${name}.png ${spill.join(", ")}`);
}
await browser.close();
