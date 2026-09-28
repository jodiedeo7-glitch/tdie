// The While-You-Sleep Storefront(TM): setup guide PDF, presale PDF, 4 launch graphics,
// and a thumbnail contact sheet for checking. HTML composed in code, printed and
// screenshotted with Playwright + Chromium.
//
// Run from the repo root:   node ops/cloud-output/storefront-product/render.mjs
// Launch date override:     LAUNCH="Thursday 8 October 2026" node ops/cloud-output/storefront-product/render.mjs
//
// Fonts: Newsreader + Inter from raw.githubusercontent.com/google/fonts into ./fonts (not committed).
// Photos: drop generated files into ./graphics/photos/ under the names in IMAGE_PROMPTS.md and run
// again. Until a file exists, that spot renders as a clean placeholder box.

import { existsSync, mkdirSync, writeFileSync, copyFileSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";
import { createRequire } from "node:module";
import { execSync } from "node:child_process";

let chromium;
try { ({ chromium } = await import("playwright")); }
catch { ({ chromium } = createRequire(join(execSync("npm root -g").toString().trim(), "x"))("playwright")); }

const HERE = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(HERE, "../../..");
const FONTS = join(HERE, "fonts");
const PDF = join(HERE, "pdf");
const GFX = join(HERE, "graphics");
const PHOTOS = join(GFX, "photos");
const CHECK = join(HERE, "tests", "thumbnails");
for (const d of [FONTS, PDF, GFX, PHOTOS, CHECK]) mkdirSync(d, { recursive: true });

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

const LAUNCH = process.env.LAUNCH || "Friday 9 October 2026";
const BC = "https://www.skool.com/the-brand-closet/about?ref=97643519c9b448d0a683ab33b6cc68ce";
const DFY = "https://www.skool.com/thedigitalincomeedit/classroom/c83b49d5?md=8ec7129809ce4a85a7e0607b8105deec";
const WE = "https://www.thedigitalincomeedit.com/shop/weekend-ecosystem";

const lf = (f) => "file://" + join(ROOT, "src/lifestyle", f);
const photo = (file, style, pos = "50% 50%", label = "", phPad = "") => {
  const p = join(PHOTOS, file);
  const inner = existsSync(p)
    ? `<img src="file://${p}" style="object-position:${pos}">`
    : `<div class="pht" style="${phPad}"><div>Photo placeholder<small>${label || file}<br>Prompt: IMAGE_PROMPTS.md</small></div></div>`;
  return `<div class="ph" style="${style}">${inner}</div>`;
};

const CSS = `
@font-face{font-family:Newsreader;src:url("file://${FONTS}/Newsreader.ttf") format("truetype");font-weight:200 800}
@font-face{font-family:Inter;src:url("file://${FONTS}/Inter.ttf") format("truetype");font-weight:100 900}
:root{--ink:#1A1417;--ink-soft:#4A3F44;--hot:#D62E73;--hot-deep:#A81F57;--bub:#FF8AC2;--gold:#C8A96A;--cream:#FBF8F5;
  --glass:rgba(255,253,252,.86);--edge:rgba(200,169,106,.6);
  --shadow:0 34px 60px -32px rgba(214,46,115,.42),0 12px 26px -16px rgba(26,20,23,.16)}
*{box-sizing:border-box;margin:0;padding:0}
@page{size:8.5in 11in;margin:0}
html,body{font-family:Inter,sans-serif;color:var(--ink);-webkit-font-smoothing:antialiased;-webkit-print-color-adjust:exact;print-color-adjust:exact}
a{color:var(--hot);font-weight:700;text-decoration:underline;text-decoration-thickness:2px;text-underline-offset:3px}
.pg{position:relative;width:816px;height:1056px;overflow:hidden;page-break-after:always;padding:64px 64px 70px;
  background:radial-gradient(60% 38% at 100% 0%,rgba(255,138,194,.22),transparent 70%),
             radial-gradient(50% 36% at 0% 100%,rgba(255,138,194,.14),transparent 70%),
             linear-gradient(165deg,#FFFEFC 0%,#FBF8F5 55%,#F5EDE8 100%)}
.pg:last-child{page-break-after:auto}
.top{display:flex;justify-content:space-between;align-items:center;margin-bottom:30px}
.brand{display:inline-flex;align-items:center;gap:10px;font:700 10.5px/1 Inter;letter-spacing:.24em;text-transform:uppercase;color:var(--ink)}
.dot{width:9px;height:9px;border-radius:50%;background:var(--hot);box-shadow:0 0 0 4px rgba(214,46,115,.16)}
.pno{font:700 10.5px/1 Inter;letter-spacing:.2em;color:var(--ink-soft)}
.foot{position:absolute;left:64px;right:64px;bottom:34px;display:flex;justify-content:space-between;padding-top:10px;
  border-top:1px solid rgba(200,169,106,.6);font:600 10px/1 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--ink-soft)}
.kicker{font:800 11.5px/1.3 Inter;letter-spacing:.2em;text-transform:uppercase;color:var(--hot);margin-bottom:12px}
h1,h2{font-family:Newsreader,serif;font-weight:600;color:var(--ink);letter-spacing:-.015em;line-height:1.04;text-wrap:balance}
h1 em,h2 em{font-style:normal;color:var(--hot)}
h1{font-size:54px}
h2{font-size:50px;margin-bottom:18px}
h3{font:800 14px/1.25 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);margin-bottom:8px}
p,li{font-size:15.6px;line-height:1.55;color:var(--ink-soft);text-wrap:pretty}
p+p{margin-top:9px}
strong{color:var(--ink)}
.lede{font-size:18px;line-height:1.5;color:var(--ink-soft);margin-bottom:22px}
.card{background:var(--glass);border:1px solid var(--edge);border-radius:18px;box-shadow:var(--shadow);padding:20px 22px}
.hotcard{position:relative;overflow:hidden;border-radius:18px;padding:20px 22px;color:#fff;
  background:linear-gradient(140deg,#F0589A 0%,var(--hot) 50%,var(--hot-deep) 100%);box-shadow:0 30px 50px -26px rgba(168,31,87,.6)}
.hotcard::after{content:"";position:absolute;inset:0;background:linear-gradient(115deg,rgba(255,255,255,.3) 0%,rgba(255,255,255,0) 40%)}
.hotcard p,.hotcard li,.hotcard h3,.hotcard strong{color:#fff}
.call{border-left:4px solid var(--hot);background:rgba(255,138,194,.13);border-radius:0 14px 14px 0;padding:14px 18px;margin-top:14px}
.call p{color:var(--ink)}
.steps{display:grid;gap:14px}
.step{display:grid;grid-template-columns:54px 1fr;gap:16px;align-items:start}
.num{width:54px;height:54px;border-radius:50%;display:grid;place-items:center;font:600 26px/1 Newsreader,serif;color:#fff;
  background:linear-gradient(140deg,#F0589A,var(--hot) 55%,var(--hot-deep));box-shadow:0 14px 24px -12px rgba(168,31,87,.7)}
.step ol,.step ul{margin:6px 0 0 18px}
.step li{margin-top:3px}
.ticks{list-style:none;display:grid;gap:9px}
.ticks li{position:relative;padding-left:30px;color:var(--ink)}
.ticks li::before{content:"\\2713";position:absolute;left:0;top:1px;width:20px;height:20px;border-radius:50%;display:grid;place-items:center;
  background:var(--ink);color:#fff;font:800 11px/1 Inter}
.ticks li span{display:block;color:var(--ink-soft);font-size:14px}
.strip{position:absolute;left:64px;right:64px;bottom:78px;height:230px}
.strip .pin{width:130px;height:195px}
.sticker{position:absolute;z-index:4;display:grid;place-items:center;width:124px;height:124px;border-radius:50%;
  font:800 13px/1.2 Inter;letter-spacing:.1em;text-transform:uppercase;text-align:center;color:var(--ink);background:#fff;
  box-shadow:0 20px 36px -16px rgba(168,31,87,.55),0 6px 12px -6px rgba(26,20,23,.2)}
.sticker.bub{background:var(--bub)}
.sticker>span{display:grid;place-items:center;width:84%;height:84%;border-radius:50%;border:2px dashed currentColor;padding:6px}
.ph{position:absolute;overflow:hidden;border-radius:18px;border:1px solid var(--edge);box-shadow:var(--shadow)}
.ph img{width:100%;height:100%;object-fit:cover;display:block}
.pht{width:100%;height:100%;display:grid;place-items:center;text-align:center;padding:24px;
  background:repeating-linear-gradient(135deg,#F6ECE8 0 16px,#FBF3F0 16px 32px);border:3px dashed rgba(214,46,115,.45);border-radius:18px;
  font:800 14px/1.45 Inter;letter-spacing:.14em;text-transform:uppercase;color:var(--hot)}
.pht small{display:block;margin-top:8px;font-weight:600;letter-spacing:.02em;text-transform:none;color:var(--ink-soft);font-size:12.5px}
.grid2{display:grid;grid-template-columns:1fr 1fr;gap:16px}
.flow{display:grid;grid-template-columns:1fr 26px 1fr 26px 1fr;align-items:center;gap:6px;margin:8px 0 20px}
.flow .card{padding:14px 14px;text-align:center}
.flow b{display:block;font:600 19px/1.1 Newsreader,serif;color:var(--ink);margin-bottom:4px}
.flow small{font-size:12px;color:var(--ink-soft);line-height:1.35;display:block}
.arrow{font:800 22px/1 Inter;color:var(--hot);text-align:center}
.pins{position:relative;height:430px;margin-top:6px}
.pin{position:absolute;border-radius:16px;overflow:hidden;border:1px solid var(--edge);box-shadow:var(--shadow);background:#fff}
.pin img{display:block;width:100%;height:100%;object-fit:cover}
.tag{font:800 10.5px/1 Inter;letter-spacing:.16em;text-transform:uppercase;color:var(--hot);margin:14px 0 6px}
table{width:100%;border-collapse:collapse;font-size:13px}
td{padding:7px 0;border-bottom:1px solid rgba(200,169,106,.45);vertical-align:top;color:var(--ink-soft);line-height:1.45}
td:first-child{font-weight:700;color:var(--ink);width:34%;padding-right:12px}
.small{font-size:12.5px}
`;

const top = (n) => `<div class="top"><div class="brand"><span class="dot"></span>The Digital Income Edit&trade;</div><div class="pno">${n ? String(n).padStart(2, "0") : ""}</div></div>`;
const foot = (t = "The While-You-Sleep Storefront&trade; &middot; Setup Guide") => `<div class="foot"><span>${t}</span><span>xoxo, Jodie</span></div>`;
const strip = (files, stick = "") => `<div class="strip">${files.map((f, i) => `<div class="pin" style="left:${i * 162}px;top:${i % 2 ? 14 : 0}px;transform:rotate(${[-4, 3, -2, 4][i % 4]}deg)"><img src="${lf(f)}"></div>`).join("")}${stick}</div>`;
const sticker = (html, style, bub = false) => `<div class="sticker${bub ? " bub" : ""}" style="${style}"><span>${html}</span></div>`;

// ---------------------------------------------------------------- SETUP GUIDE
const guide = [];

// 1 cover
guide.push(`<section class="pg" style="padding:0">
  ${photo("cover-sofa-dusk.jpg", "left:330px;top:0;width:486px;height:1056px;border-radius:0;border:0;border-left:2px solid var(--gold)", "62% 50%", "cover-sofa-dusk.jpg<br>(Tommy Kate asleep on the sofa at dusk)", "padding-left:170px")}
  <div style="position:absolute;left:0;top:0;width:470px;height:1056px;background:linear-gradient(90deg,#FBF8F5 0%,#FBF8F5 62%,rgba(251,248,245,0) 100%)"></div>
  <div style="position:absolute;left:60px;top:60px;width:420px;display:flex;flex-direction:column;height:936px">
    <div class="brand"><span class="dot"></span>The Digital Income Edit&trade;</div>
    <div style="margin-top:auto">
      <div class="kicker">Setup Guide</div>
      <h1 style="font-size:58px;width:470px">The <em style="white-space:nowrap">While-You-Sleep</em> Storefront&trade;</h1>
      <p class="lede" style="margin-top:18px;font-size:18px">Your prepared Amazon product intake, turned into Pinterest Pins that get built, scheduled and logged on a timetable.</p>
      <div class="card" style="margin-top:6px">
        <ul class="ticks">
          <li>Short setup<span>once your accounts are ready</span></li>
          <li>Then the downstream work repeats<span>your Amazon-side intake stays with you</span></li>
          <li>Found through search<span>not the feed</span></li>
        </ul>
      </div>
    </div>
    <div style="margin-top:auto;font:600 22px/1 Newsreader,serif;color:var(--hot)">xoxo, Jodie</div>
  </div>
  ${sticker("Two real<br>worked<br>examples", "left:392px;top:118px;transform:rotate(-9deg)", true)}
</section>`);

// 2 what it is
guide.push(`<section class="pg">${top(2)}
  <div class="kicker">What you're holding</div>
  <h2>A machine that makes pins <em>while you sleep.</em></h2>
  <p class="lede">You prepare the products and destination. The scheduled workflow handles the repetitive image, copy, Pinterest and logging work after that.</p>
  <div class="flow">
    <div class="card"><b>Your products</b><small>5 to 8 pieces per look, with your own Amazon Special Links</small></div>
    <div class="arrow">&rarr;</div>
    <div class="card"><b>The machine</b><small>images, Pin copy, queue, scheduling and recovery</small></div>
    <div class="arrow">&rarr;</div>
    <div class="card"><b>Pinterest</b><small>two Pins per look, 3 days apart, with your review/PULL control</small></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>What you do</h3>
      <p>Choose the products, create the Amazon destination you want the Pins to point to, and put the required fields into PRODUCT_SOURCES.md. The automated workflow does not browse Amazon or operate your Amazon account.</p></div>
    <div class="hotcard"><h3>What runs</h3>
      <p>The scheduled workflow turns ready product rows into new styling images, Pin copy, scheduled Pins and state/log records. A second task handles your PULL requests and leftovers.</p></div>
  </div>
  <div class="call"><p><strong>The honest part.</strong> The schedule runs in Claude. Local files and browser actions require Claude Desktop to be open and connected. Pinterest publishes the scheduled Pins even when your computer is off.</p></div>
  <div class="call" style="background:rgba(200,169,106,.12);border-left-color:var(--gold)"><p><strong>What it doesn't promise:</strong> sales, Amazon approval, Pinterest approval, or permanent access to any model or platform feature.</p></div>
  ${foot()}
</section>);

// 3 requirements
guide.push(`<section class="pg">${top(3)}
  <div class="kicker">Step 0 &middot; before anything</div>
  <h2>What you need, <em>up front.</em></h2>
  <p class="lede">Get these pieces ready before you run the setup chat.</p>
  <div class="card"><ul class="ticks">
    <li>A paid Claude plan with Scheduled Tasks and the browser/local capabilities your path needs<span>Check your current Claude plan because features can change.</span></li>
    <li>Claude Desktop<span>Keep it open and connected whenever the workflow needs your local Storefront folder or browser.</span></li>
    <li>Amazon access for your path<span>Amazon Associates for the Associates-only path, or Amazon Influencer approval/storefront for the Influencer path.</span></li>
    <li>A Pinterest business account with public production boards<span>The workflow checks boards before scheduling.</span></li>
    <li>An image provider with commercial-use rights<span>OpenArt Plus is the current benchmark; other providers are used only when their current rights and reference workflow fit.</span></li>
    <li>A rights-cleared persona or product reference image, if you use one<span>Use only images you own or are explicitly licensed to transform and publish commercially.</span></li>
    <li>A backup of your Storefront folder<span>The folder contains your persistent state, drafts and logs.</span></li>
  </ul></div>
  <div class="call"><p><strong>You don't need</strong> Amazon browser automation, Canva, a separate missed-run task, or a website on the Influencer path.</p></div>
  ${foot()}
</section>);

// 4 steps 1-3
guide.push(`<section class="pg">${top(4)}
  <div class="kicker">Steps 1 to 3</div>
  <h2>Get your computer <em>ready.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">1</div><div class="card"><h3>Make your folder</h3>
      <p>Make a folder called <strong>While-You-Sleep Storefront</strong> and unzip the kit into it. Keep the folder in one location after setup because the scheduled tasks use that path.</p></div></div>
    <div class="step"><div class="num">2</div><div class="card"><h3>Sign in to the tools you actually use</h3>
      <p>In Chrome, sign in to Pinterest and your chosen image provider. Keep the provider account on a plan that permits commercial use. Amazon product research and Amazon link/list creation happen in your own workflow, not in the scheduled agent.</p></div></div>
    <div class="step"><div class="num">3</div><div class="card"><h3>Connect Claude Desktop</h3>
      <p>Open Claude Desktop and make sure it can reach the Storefront folder. The schedule itself can run remotely, but local files and browser controls require Desktop to be open and connected.</p></div></div>
  </div>
  ${strip(["pink-witch-halloween-costume-flatlay.jpg", "pink-witch-halloween-costume-lifestyle.jpg", "pink-halloween-porch-decor-flatlay.jpg", "pink-graduation-gown-halloween-costume-lifestyle.jpg"], sticker("Downstream<br>work,<br>automated", "right:-10px;top:40px;transform:rotate(8deg)", true))}
  ${foot()}
</section>);

// 5 steps 4-5
guide.push(`<section class="pg">${top(5)}
  <div class="kicker">Steps 4 and 5 &middot; setup chat</div>
  <h2>Paste one prompt. <em>Answer five questions.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">4</div><div class="card"><h3>Open a chat with your folder attached</h3>
      <p>Start a new Claude Desktop chat and attach the Storefront folder so the setup prompt can read and write the files it creates.</p></div></div>
    <div class="step"><div class="num">5</div><div class="card"><h3>Paste the setup prompt</h3>
      <p>Open <strong>02_SETUP_PROMPT.txt</strong>, copy the prompt between its divider lines, and paste it into the chat. It asks, one at a time:</p>
      <ol><li>your theme and content mix</li><li>your Pinterest boards</li><li>your Amazon path and website details, if applicable</li><li>whether you use a persona and which provider/model you will use</li><li>your time zone and computer availability</li></ol>
      <p>It then creates your recipe, product-intake state, logs, queue file and the two core scheduled-task prompts.</p></div></div>
  </div>
  <div class="call"><p>Do not enter Amazon passwords into Claude. Complete Amazon product selection and link/list setup yourself before a look is marked ready in PRODUCT_SOURCES.md.</p></div>
  ${foot()}
</section>);

// 6 steps 6-7
guide.push(`<section class="pg">${top(6)}
  <div class="kicker">Steps 6 and 7 &middot; schedule it</div>
  <h2>Two tasks. <em>That's it.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">6</div><div class="card"><h3>Create the weekly build</h3>
      <p>Open <strong>MY_SCHEDULED_TASKS.txt</strong>. Create the weekly themed-look task using the exact name, schedule and folder line supplied there. At 5 or more looks per week, the setup may create a second weekly build day.</p></div></div>
    <div class="step"><div class="num">7</div><div class="card"><h3>Create the pull sweep</h3>
      <p>Create the daily pull-sweep task at the two times in MY_RECIPE.txt. It removes Pins you mark PULL and finishes eligible leftovers. Run both tasks once by hand so access prompts are approved before relying on the schedule.</p></div></div>
  </div>
  <div class="call"><p><strong>Important:</strong> the schedule is cloud-run. A task that needs local files or browser access still requires Claude Desktop to be open and connected at execution time.</p></div>
  ${foot()}
</section>);

// 7 steps 8-10
guide.push(`<section class="pg">${top(7)}
  <div class="kicker">Steps 8 to 10 &middot; living with it</div>
  <h2>Then you <em>leave it alone.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">8</div><div class="card"><h3>Prepare product rows</h3>
      <p>Add the products for your next looks to <strong>PRODUCT_SOURCES.md</strong>. Each row needs the ASIN, your own Special Link, plain-language attributes, the destination URL and rights status for any reference image.</p></div></div>
    <div class="step"><div class="num">9</div><div class="card"><h3>Use the Pull control</h3>
      <p>Every scheduled Pin is logged. Type <strong>PULL</strong> in its last column before the next sweep if you want it removed. The existing review behavior stays in place.</p></div></div>
    <div class="step"><div class="num">10</div><div class="card"><h3>Let recovery happen</h3>
      <p>The next weekly run checks incomplete prior work before starting new work. Stable IDs prevent the same Pin from being created twice.</p></div></div>
  </div>
  <div class="hotcard" style="margin-top:16px"><h3>What a normal week looks like</h3>
    <p>You prepare product intake in batches. The weekly build creates ready Pins and schedules them. The pull sweep handles removals and leftovers. If a run stops, the next successful weekly run resumes incomplete work instead of starting duplicates.</p></div>
  ${foot()}
</section>);

// 8 worked example 1
guide.push(`<section class="pg">${top(8)}
  <div class="kicker">Worked example 1 &middot; no-persona path</div>
  <h2>A cozy fall <em>outfit look.</em></h2>
  <div style="display:grid;grid-template-columns:330px 1fr;gap:24px">
    <div class="pins">
      <div class="pin" style="left:0;top:0;width:200px;height:300px;transform:rotate(-3deg)"><img src="${lf("pink-witch-halloween-costume-flatlay.jpg")}"></div>
      <div class="pin" style="left:128px;top:112px;width:200px;height:300px;transform:rotate(4deg)"><img src="${lf("pink-halloween-porch-decor-flatlay.jpg")}"></div>
      ${sticker("Pin 1<br>&rarr;<br>3 days<br>&rarr; Pin 2", "left:-6px;top:300px;transform:rotate(-8deg);width:112px;height:112px", true)}
    </div>
    <div>
      <p class="tag">What the workflow used</p>
      <table>
        <tr><td>Product intake</td><td>Six customer-selected products, each with an ASIN, plain-language description, compliant Special Link and destination URL.</td></tr>
        <tr><td>Image inputs</td><td>Written attributes by default. No Amazon-hosted image or marketplace screenshot is used.</td></tr>
        <tr><td>Pin 1</td><td>Person-free styled flat lay with the provider/model recorded in MY_RECIPE.txt.</td></tr>
        <tr><td>Pin 2</td><td>A second person-free format on a different surface, with a different title.</td></tr>
        <tr><td>Queue</td><td>Both Pins are written to the log and review queue before scheduling. PULL remains available.</td></tr>
        <tr><td>Verification</td><td>The workflow verifies the scheduled Pins and records their stable IDs.</td></tr>
      </table>
    </div>
  </div>
  <div class="call"><p>Want to save credits? Generate only the Pin that needs a new image and keep the existing state for everything else.</p></div>
  ${foot()}
</section>);

// 9 worked example 2
guide.push(`<section class="pg">${top(9)}
  <div class="kicker">Worked example 2 &middot; persona path</div>
  <h2>Same products. <em>Different image path.</em></h2>
  <div style="display:grid;grid-template-columns:300px 1fr;gap:24px">
    <div style="position:relative;height:450px">
      ${photo("pink-witch-halloween-costume-lifestyle.jpg", "left:0;top:0;width:290px;height:435px", "50% 50%", "customer persona lifestyle example")}
    </div>
    <div>
      <p class="tag">What changes</p>
      <table>
        <tr><td>Reference</td><td>The customer's own persona reference image, plus only any additional rights-cleared product reference images listed in PRODUCT_SOURCES.md.</td></tr>
        <tr><td>Generation</td><td>The provider/model named in MY_RECIPE.txt generates the lifestyle image. The workflow does not assume the founder's model access.</td></tr>
        <tr><td>Consistency</td><td>Identity comes from the reference image. The prompt describes clothing, pose, setting and activity instead of inventing identity traits.</td></tr>
        <tr><td>Quality gate</td><td>Check identity consistency, required products, framing, realism, no logos/text and spelling before the Pin is scheduled.</td></tr>
        <tr><td>Cost control</td><td>If the provider is unavailable or out of credits, the Pin is held instead of silently switching to a different paid model.</td></tr>
      </table>
    </div>
  </div>
  <div class="call"><p>The customer can change providers later by updating MY_RECIPE.txt and re-testing the workflow. The product never treats your personal founder plan as a customer entitlement.</p></div>
  ${foot()}
</section>);

// 10 troubleshooting
guide.push(`<section class="pg">${top(10)}
  <div class="kicker">When something's off</div>
  <h2>What the tasks do <em>when things go wrong.</em></h2>
  <div class="grid2" style="margin-top:10px">
    <div class="card"><h3>Product intake is incomplete</h3><p>The look is held as needs product intake. No ASIN, Special Link, destination or rights status is invented.</p></div>
    <div class="card"><h3>Pinterest loads blank</h3><p>One fresh retry is allowed. Two consecutive blank pages stop that run. Finished work stays logged for the next sweep.</p></div>
    <div class="card"><h3>Your board is secret</h3><p>The workflow checks production boards before scheduling and stops when a board is secret.</p></div>
    <div class="card"><h3>Image credits run out</h3><p>The Pin is held as waiting: image provider. It is not silently moved to a different model or account.</p></div>
    <div class="card"><h3>A Pin is duplicated</h3><p>Stable IDs are checked before creation. Existing IDs are verified instead of creating another Pin.</p></div>
    <div class="card"><h3>You want one removed</h3><p>Type PULL in pin-tab.md. The pull sweep deletes it and updates the logs. You can also remove it directly in Pinterest.</p></div>
  </div>
  <div class="call"><p>If Claude Desktop is offline when a task needs local files or browser access, the local part waits for a later successful run. Recovery uses the persistent folder state.</p></div>
  ${foot()}
</section>);

// ---------------------------------------------------------------- PRESALE PDF
const presale = [`<section class="pg" style="padding:0">
  ${photo("cover-sofa-dusk.jpg", "left:0;top:0;width:816px;height:470px;border-radius:0;border:0;border-bottom:2px solid var(--gold)", "62% 45%", "cover-sofa-dusk.jpg (Tommy Kate asleep on the sofa at dusk)")}
  <div style="position:absolute;left:64px;right:64px;top:520px">
    <div class="brand"><span class="dot"></span>The Digital Income Edit&trade;</div>
    <div class="kicker" style="margin-top:34px">The While-You-Sleep Storefront&trade; &middot; presale</div>
    <h1 style="font-size:84px">You're <em>in.</em></h1>
    <div class="card" style="margin-top:26px">
      <p style="font-size:21px;line-height:1.45;color:var(--ink)">Your kit unlocks <strong>${LAUNCH}</strong> at <strong>9 am ET</strong>.</p>
      <p style="font-size:21px;line-height:1.45;color:var(--ink);margin-top:10px">Use this same download link then.</p>
    </div>
    <p style="margin-top:22px;font-size:15px">Want a head start? Get your accounts ready now: a Claude plan with Scheduled Tasks, the Claude Desktop app, Amazon access for your path, a Pinterest business account, and a commercial-use image provider.</p>
    <div style="margin-top:28px;font:600 30px/1 Newsreader,serif;color:var(--hot)">xoxo, Jodie</div>
  </div>
  ${sticker("See you<br>at 9 am", "right:70px;top:420px;transform:rotate(8deg)", true)}
</section>`];

// ---------------------------------------------------------------- GRAPHICS
const G = [
  { name: "g1-presale-open", w: 1600, h: 900, photo: "g1-porch-morning.jpg", pos: "70% 50%",
    kicker: "Presale &middot; 4 days only", h1: "Your Amazon pins, made <em>while you sleep.</em>",
    card: `<b>$10</b><span>until Thursday 11:59 pm ET &middot; then $27</span>`, sticker: "No more<br>posting" },
  { name: "g2-tease", w: 1600, h: 900, photo: "g2-loft-night-desk.jpg", pos: "70% 50%",
    kicker: "Coming Monday", h1: "Something's been running <em>while I sleep.</em>",
    card: `<span style="font-size:24px;letter-spacing:.06em">I cannot and will not gatekeep this.</span>`, sticker: "Coming<br>Monday" },
  { name: "g3-last-call", w: 1080, h: 1350, photo: "g3-kitchen-late.jpg", pos: "65% 70%", vertical: true,
    kicker: "Last call", h1: "$10 ends <em>at midnight.</em>",
    card: `<span>The While-You-Sleep Storefront&trade;</span><span>then $27</span>`, sticker: "Thursday<br>11:59 pm<br>ET" },
  { name: "g4-share", w: 1200, h: 630, photo: "g4-nightstand-phone.jpg", pos: "75% 50%",
    kicker: "The Digital Income Edit&trade;", h1: "The <span style=\"white-space:nowrap\">While-You-Sleep</span> <em>Storefront&trade;</em>",
    card: `<span>Amazon links &rarr; Pinterest pins, on a schedule</span>`, sticker: "Found<br>through<br>search" },
];

const gfx = (g) => {
  const u = g.w / 1600;
  const photoBox = g.vertical
    ? `left:0;top:${Math.round(g.h * 0.42)}px;width:${g.w}px;height:${Math.round(g.h * 0.58)}px;border-radius:0;border:0;border-top:2px solid var(--gold)`
    : `left:${Math.round(g.w * 0.42)}px;top:0;width:${Math.round(g.w * 0.58)}px;height:${g.h}px;border-radius:0;border:0;border-left:2px solid var(--gold)`;
  const scrim = g.vertical
    ? `left:0;top:0;width:${g.w}px;height:${Math.round(g.h * 0.56)}px;background:linear-gradient(180deg,#FBF8F5 0%,#FBF8F5 72%,rgba(251,248,245,0) 100%)`
    : `left:0;top:0;width:${Math.round(g.w * 0.62)}px;height:${g.h}px;background:linear-gradient(90deg,#FBF8F5 0%,#FBF8F5 62%,rgba(251,248,245,0) 100%)`;
  const copyBox = g.vertical
    ? `left:70px;top:70px;width:${g.w - 140}px`
    : `left:${Math.round(70 * u) + 10}px;top:0;height:${g.h}px;width:${Math.round(g.w * 0.5)}px;justify-content:center`;
  const h1size = g.vertical ? 104 : Math.round((g.w === 1200 ? 62 : 84));
  const stickerPos = g.vertical ? `right:70px;top:${Math.round(g.h * 0.42) - 80}px` : `left:${Math.round(g.w * 0.42) - 90}px;top:${Math.round(g.h * 0.1)}px`;
  return `<!doctype html><html><head><style>${CSS}
    html,body{width:${g.w}px;height:${g.h}px;overflow:hidden}
    .stage{position:relative;width:${g.w}px;height:${g.h}px;overflow:hidden;
      background:radial-gradient(55% 40% at 0% 100%,rgba(255,138,194,.16),transparent 70%),linear-gradient(165deg,#FFFEFC 0%,#FBF8F5 55%,#F6EFEA 100%)}
    .gcopy{position:absolute;display:flex;flex-direction:column;gap:${g.w === 1200 ? 16 : 24}px;z-index:3}
    .gcopy .kicker{font-size:${g.w === 1200 ? 16 : 20}px;margin:0}
    .gcopy h1{font-size:${h1size}px}
    .gcard{align-self:flex-start;display:flex;flex-direction:column;gap:6px}
    .gcard b{font:600 ${g.vertical ? 88 : 72}px/1 Newsreader,serif;color:#fff}
    .gcard span{font:700 ${g.w === 1200 ? 17 : 21}px/1.3 Inter;letter-spacing:.08em;text-transform:uppercase;color:#fff}
    .ph .pht{border-radius:0}
    .sticker{width:${g.w === 1200 ? 118 : 150}px;height:${g.w === 1200 ? 118 : 150}px;font-size:${g.w === 1200 ? 13 : 16}px}
  </style></head><body><div class="stage">
    ${photo(g.photo, photoBox, g.pos, g.photo + " (see IMAGE_PROMPTS.md)")}
    <div style="position:absolute;${scrim}"></div>
    <div class="gcopy" style="${copyBox}">
      <div class="brand" style="font-size:${g.w === 1200 ? 12 : 15}px"><span class="dot"></span>The Digital Income Edit&trade;</div>
      <div class="kicker">${g.kicker}</div>
      <h1>${g.h1}</h1>
      <div class="hotcard gcard">${g.card}</div>
    </div>
    ${sticker(g.sticker, `${stickerPos};transform:rotate(-8deg)`, true)}
  </div></body></html>`;
};

// ---------------------------------------------------------------- RENDER
const browser = await chromium.launch({ executablePath: existsSync("/opt/pw-browsers/chromium") ? undefined : undefined });
const page = await browser.newPage({ viewport: { width: 816, height: 1056 } });
const wrap = (pages) => `<!doctype html><html><head><meta charset="utf-8"><style>${CSS}</style></head><body>${pages.join("\n")}</body></html>`;

async function doc(name, pages) {
  const html = join(PDF, name + ".html");
  writeFileSync(html, wrap(pages));
  await page.goto("file://" + html);
  await page.evaluate(() => document.fonts.ready);
  await page.pdf({ path: join(PDF, name + ".pdf"), width: "8.5in", height: "11in", printBackground: true, preferCSSPageSize: true });
  // page PNGs for the thumbnail check
  await page.setViewportSize({ width: 816, height: 1056 });
  const shots = [];
  for (let i = 0; i < pages.length; i++) {
    const f = join(CHECK, `${name}-p${String(i + 1).padStart(2, "0")}.png`);
    await page.screenshot({ path: f, clip: { x: 0, y: i * 1056, width: 816, height: 1056 }, fullPage: true });
    shots.push(f);
  }
  return shots;
}

const guideShots = await doc("While-You-Sleep-Storefront-Setup-Guide", guide);
const presaleShots = await doc("While-You-Sleep-Storefront-Presale", presale);

const gfxShots = [];
for (const g of G) {
  const p2 = await browser.newPage({ viewport: { width: g.w, height: g.h } });
  const html = join(GFX, g.name + ".html");
  writeFileSync(html, gfx(g));
  await p2.goto("file://" + html);
  await p2.evaluate(() => document.fonts.ready);
  const f = join(GFX, g.name + ".png");
  await p2.screenshot({ path: f });
  gfxShots.push({ f, w: g.w, h: g.h, name: g.name });
  await p2.close();
}

// thumbnail contact sheet: every PDF page at 150 px wide, every graphic at 300 px wide
const sheet = `<!doctype html><html><head><style>
  body{margin:0;padding:24px;background:#eee;font:12px Inter,sans-serif}
  .row{display:flex;flex-wrap:wrap;gap:14px;margin-bottom:24px;align-items:flex-start}
  figure{margin:0}img{display:block;box-shadow:0 2px 8px rgba(0,0,0,.2)}
</style></head><body>
<div class="row">${[...guideShots, ...presaleShots].map((s) => `<figure><img src="file://${s}" width="150"></figure>`).join("")}</div>
<div class="row">${gfxShots.map((s) => `<figure><img src="file://${s.f}" width="300"></figure>`).join("")}</div>
</body></html>`;
const sp = await browser.newPage({ viewport: { width: 1400, height: 900 } });
writeFileSync(join(CHECK, "contact-sheet.html"), sheet);
await sp.goto("file://" + join(CHECK, "contact-sheet.html"));
await sp.screenshot({ path: join(CHECK, "contact-sheet.png"), fullPage: true });
await browser.close();

copyFileSync(join(PDF, "While-You-Sleep-Storefront-Setup-Guide.pdf"), join(HERE, "kit", "While-You-Sleep-Storefront-Setup-Guide.pdf"));
console.log("Rendered:", guideShots.length, "guide pages,", presaleShots.length, "presale page,", gfxShots.length, "graphics. Launch:", LAUNCH);
