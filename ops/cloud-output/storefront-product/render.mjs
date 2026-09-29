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
      <p class="lede" style="margin-top:18px;font-size:18px">Your Amazon links, turned into reviewable Pinterest Pin drafts. You choose each Pin and approve scheduling when your connected account supports it.</p>
      <div class="card" style="margin-top:6px">
        <ul class="ticks">
          <li>About 5 minutes to start<span>once your accounts are ready</span></li>
          <li>Then no building, no selling, no posting<span>drafts are prepared for your review; you choose and approve each schedule</span></li>
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
  <p class="lede">ChatGPT Work scheduled tasks can prepare reviewable Pin drafts when the feature and connected actions are available in your account. You supply approved product inputs and choose each Pin before scheduling.</p>
  <div class="flow">
    <div class="card"><b>Amazon</b><small>5 to 8 pieces per look, each with your own affiliate link</small></div>
    <div class="arrow">&rarr;</div>
    <div class="card"><b>Pinterest</b><small>two pins per look, 3 days apart, with your #ad line</small></div>
    <div class="arrow">&rarr;</div>
    <div class="card"><b>Your list</b><small>an Idea List, or a shop-the-look page on your own site</small></div>
  </div>
  <div class="grid2">
    <div class="card"><h3>Automation 1 &middot; Themed looks</h3>
      <p>The weekly workflow organizes your approved product inputs into look drafts, prepares images and Pin copy, and records the result. You review each Pin and approve any scheduling action; destination and publishing steps depend on your connected accounts.</p></div>
    <div class="hotcard"><h3>Automation 2 &middot; Outfit of the Day</h3>
      <p>Optional: for members with the required Brand Closet&trade; access, the OOTD workflow can prepare new outfit drafts using your own authorized product inputs and images. Account access and each publishing step must be confirmed.</p></div>
  </div>
  <div class="call"><p><strong>The honest part.</strong> Runs depend on the ChatGPT Work mode and connected actions available in your account. Cloud execution may run while your computer is off when supported; local execution requires your computer during a run. Review and approve each Pin before scheduling. Pull or cancellation depends on the publishing connection.</p></div>
  <div class="call" style="background:rgba(200,169,106,.12);border-left-color:var(--gold)"><p><strong>What it doesn't promise:</strong> sales. Pinterest is search, and pins get found over weeks and months. This builds and runs the machine. What people buy is up to them and Amazon.</p></div>
  ${foot()}
</section>`);

// 3 requirements
guide.push(`<section class="pg">${top(3)}
  <div class="kicker">Step 0 &middot; before anything</div>
  <h2>What you need, <em>up front.</em></h2>
  <p class="lede">If one of these is missing, the machine doesn't run. Get it first. Full detail is in 01_REQUIREMENTS.txt.</p>
  <div class="card"><ul class="ticks">
    <li>A ChatGPT plan with Work and Scheduled Tasks available<span>Feature availability varies by account and workspace. Confirm Scheduled Tasks and the required connected actions in your own account before setup.</span></li>
    <li>A supported execution mode and an available workspace or folder<span>Use only the connected services and actions the setup confirms are available. Complete sign-in through each service's own sign-in flow.</span></li>
    <li>Amazon Associates, plus Influencer approval for Idea Lists<span>No Influencer approval? The Associates-only path uses a page on your own site, and on most site builders you paste it in yourself.</span></li>
    <li>A Pinterest business account and a verified public production board<span>Use a supported authorized path to resolve and confirm the exact board. If it cannot be verified, do not schedule.</span></li>
    <li>Only for the blog half: Chrome signed in to GitHub<span>With write access to your site's repository.</span></li>
    <li>A connected image provider, if you choose that path<span>Use the provider and model confirmed available in your account. Record commercial-use rights; do not silently switch models or plans.</span></li>
    <li>The Brand Closet&trade; at Rose's $9/month tier or above<span>For automation 2 only. It carries the Outfit of the Day.</span></li>
  </ul></div>
  <div class="call"><p><strong>You don't need</strong> a website (unless you choose the Associates-only path or the blog half), Instagram, design skills, code, or your face on camera.</p></div>
    ${foot()}
</section>`);

// 4 steps 1-3
guide.push(`<section class="pg">${top(4)}
  <div class="kicker">Steps 1 to 3</div>
  <h2>Choose your setup <em>and accounts.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">1</div><div class="card"><h3>Choose a supported workspace</h3>
      <p>Follow the setup prompt to choose Cloud or Local only if that mode is available in your account. Use the dedicated connected Drive folder or local folder that the setup confirms can store your files. Unzip the kit there if your selected workflow requires it.</p></div></div>
    <div class="step"><div class="num">2</div><div class="card"><h3>Connect only the services you choose</h3>
      <p>Complete sign-in through Amazon, Pinterest, your selected publisher, image provider, and storage service when prompted. Never type passwords into a task. The setup is incomplete if a required action is unavailable; use a supported manual path where the kit describes one.</p></div></div>
    <div class="step"><div class="num">3</div><div class="card"><h3>Optional: join The Brand Closet&trade;</h3>
      <p>Only if you want automation 2. It's Rose's community: free to join, and her paid tiers are $9/month and $19/month (her prices). The Outfit of the Day is on her $9/month tier.</p>
      <p><a href="${BC}">Join The Brand Closet&trade;</a> and stay signed in to Skool in Chrome.</p>
      <p class="small">Affiliate link: I earn a commission if you upgrade, at no extra cost to you.</p></div></div>
  </div>
  ${strip(["pink-angel-halloween-costume-flatlay.jpg", "pink-bunny-halloween-costume-lifestyle.jpg", "pink-halloween-porch-decor-flatlay.jpg", "pink-graduation-gown-halloween-costume-lifestyle.jpg"], sticker("Made by<br>the tasks,<br>not me", "right:-10px;top:40px;transform:rotate(8deg)", true))}
  ${foot()}
</section>`);

// 5 steps 4-5
guide.push(`<section class="pg">${top(5)}
  <div class="kicker">Steps 4 and 5 &middot; the 5 minutes</div>
  <h2>Paste one prompt. <em>Answer six questions.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">4</div><div class="card"><h3>Open a ChatGPT Work chat</h3>
      <p>Start a new Work chat where the kit is available. Follow the setup prompt to connect the supported storage location and authorize the actions you choose. If Work, Scheduled Tasks, or a required write action is unavailable, stop setup and use only the supported manual path.</p></div></div>
    <div class="step"><div class="num">5</div><div class="card"><h3>Paste the setup prompt</h3>
      <p>Open <strong>02_SETUP_PROMPT.txt</strong>. Copy everything between the two long lines. Paste it into the chat and press Enter. The prompt collects the choices needed for your setup, including:</p>
      <ol><li>your theme</li><li>your boards (and it makes you check each one is public)</li><li>your storefront and your website, if you have one</li><li>whether you have an AI persona</li><li>whether you're in The Brand Closet&trade;</li><li>your time zone, cadence, and Cloud or Local mode if available</li></ol>
      <p>Then it writes your files into the folder: <strong>MY_RECIPE.txt</strong>, <strong>storefront-log.md</strong>, <strong>pin-tab.md</strong>, <strong>pin-drafts.md</strong>, <strong>MY_SCHEDULED_TASKS.txt</strong> (plus a pages folder if you paste pages into your site yourself).</p></div></div>
  </div>
  <div class="call"><p>My own words, because people ask: it took me 5 minutes to set up. That's with Amazon, Pinterest and my image tools already signed in.</p></div>
    ${foot()}
</section>`);

// 6 steps 6-7
guide.push(`<section class="pg">${top(6)}
  <div class="kicker">Steps 6 and 7 &middot; never scheduled a task? start here</div>
  <h2>Hand it <em>the timetable.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">6</div><div class="card"><h3>Create your scheduled tasks</h3>
      <p>Open <strong>MY_SCHEDULED_TASKS.txt</strong>. It holds the three canonical task prompts: weekly planning, Outfit of the Day when selected, and daily reconciliation. Configure only tasks supported by your account and setup choices. Each has one line telling you exactly what to type. For each one:</p>
      <ol><li>In ChatGPT Work, create a Scheduled Task only if the feature is available in your account; follow the current in-app instructions.</li>
      <li>Type the <strong>name</strong> from the file.</li>
      <li>Set the <strong>schedule</strong> from the file (for example: weekly, Saturday, 1:05 pm).</li>
      <li>Give it access to the configured state location only if the task's supported setup requires it.</li>
      <li>Paste the <strong>prompt</strong>: everything between that task's two long lines.</li>
      <li><strong>Save.</strong></li></ol>
      <p class="small">Available menus and actions vary by account. If Scheduled Tasks or a required action is missing, do not claim the automation is active.</p></div></div>
    <div class="step"><div class="num">7</div><div class="card"><h3>Watch the first run</h3>
      <p>Run a supported task once only after setup and required permissions are confirmed. Check the result, state record, destination, board, and any approval step. A successful first run does not prove future runs or publishing; monitor the account and report failures.</p></div></div>
  </div>
    ${foot()}
</section>`);

// 7 steps 8-10
guide.push(`<section class="pg">${top(7)}
  <div class="kicker">Steps 8 to 10 &middot; living with it</div>
  <h2>Then you <em>leave it alone.</em></h2>
  <div class="steps" style="margin-top:14px">
    <div class="step"><div class="num">8</div><div class="card"><h3>Know what your selected mode requires</h3>
      <p>Cloud runs may work while your computer is off when Cloud Work and the required connected actions are enabled for your account. Local runs require your computer and any required local session to be available. Do not assume a missed run will catch up automatically; check the run record and report skipped work.</p></div></div>
    <div class="step"><div class="num">9</div><div class="card"><h3>Optional: glance at your pin tab</h3>
      <p>Review the Pin record and destination before approving a schedule. The publisher may support scheduled-post readback, but a scheduled record alone does not prove publication. Cancellation or removal depends on the selected publisher; remove an already-published Pin through Pinterest and record only confirmed outcomes.</p></div></div>
    <div class="step"><div class="num">10</div><div class="card"><h3>Optional extras</h3>
      <p><strong>09_THE_BLOG_HALF.txt</strong>: a shop-the-look section on your own site, written for Google. <strong>05_RECOMMEND_IT_TOO.txt</strong>: a Brand Closet&trade; card for your pages. <strong>10_INSTAGRAM_ADD_ON.txt</strong>: feed posts (stories are by hand).</p></div></div>
  </div>
  <div class="hotcard" style="margin-top:16px"><h3>What a normal week looks like</h3>
    <p>Cadence is the one recorded in your setup and must fit your publisher plan limits. Each run prepares reviewable work. You choose each Pin and approve scheduling; the report distinguishes draft, approved, scheduled, and verified outcomes. Optional OOTD depends on separate community access.</p></div>
  ${foot()}
</section>`);

// 8 worked example 1
guide.push(`<section class="pg">${top(8)}
  <div class="kicker">Worked example 1 &middot; automation 1</div>
  <h2>My Pink Witch <em>Halloween Costume.</em></h2>
  <div style="display:grid;grid-template-columns:330px 1fr;gap:24px">
    <div class="pins">
      <div class="pin" style="left:0;top:0;width:200px;height:300px;transform:rotate(-3deg)"><img src="${lf("pink-witch-halloween-costume-flatlay.jpg")}"></div>
      <div class="pin" style="left:128px;top:112px;width:200px;height:300px;transform:rotate(4deg)"><img src="${lf("pink-witch-halloween-costume-lifestyle.jpg")}"></div>
      ${sticker("Pin 1<br>&rarr;<br>3 days<br>&rarr; Pin 2", "left:-6px;top:300px;transform:rotate(-8deg);width:112px;height:112px", true)}
    </div>
    <div>
      <p class="tag">What the weekly task did</p>
      <table>
        <tr><td>Picked the look</td><td>From the Halloween window of my calendar.</td></tr>
        <tr><td>Sourced 6 pieces</td><td>Soft pink velvet witch hat, black velvet square neck mini dress, black platform Mary Jane pumps, pale pink lace gloves, black crescent shoulder bag, gold moon and star drop earrings. Every one from customer-supplied product rows and authorized links.</td></tr>
        <tr><td>Destination</td><td>Use the customer's selected, verified destination. Its creation and availability depend on the selected Amazon path and connected account.</td></tr>
        <tr><td>Pin 1</td><td>One generated inspiration flat lay with no baked-in text. A separate headline is added only after framing and image checks.</td></tr>
        <tr><td>Pin 2</td><td>A second image made with the configured provider only if the customer has selected that path and the required rights and reference are available.</td></tr>
        <tr><td>Copy and schedule</td><td>Pin copy and disclosure are drafted. The customer checks image, title, destination, board, disclosure, and alt text, then approves any supported scheduling action.</td></tr>
        <tr><td>Logged and published</td><td>The example illustrates a proposed record only; it is not evidence of a live customer workflow or publication.</td></tr>
      </table>
    </div>
  </div>
  <div class="call"><p>No prices anywhere, no brand names in the list or the pins, and nothing from Amazon's own photos posted: they were only the reference for new images.</p></div>
  ${foot()}
</section>`);

// 9 worked example 2
guide.push(`<section class="pg">${top(9)}
  <div class="kicker">Worked example 2 &middot; automation 2</div>
  <h2>My pink color-block hoodie <em>Outfit of the Day.</em></h2>
  <div style="display:grid;grid-template-columns:300px 1fr;gap:24px">
    <div style="position:relative;height:450px">
      ${photo("hoodie-flatlay.jpg", "left:0;top:0;width:290px;height:435px", "50% 50%", "hoodie-flatlay.jpg (my own generated flat lay, never Rose's image)")}
    </div>
    <div>
      <p class="tag">What the nightly task did</p>
      <table>
        <tr><td>Found the lesson</td><td>A new outfit in The Brand Closet&trade; Outfit of the Day Closet course, not yet in my log.</td></tr>
        <tr><td>Looked, didn't take</td><td>One screenshot of Rose's flat lay, for reference only. Her images and prompts are paid member content: never posted, uploaded or attached anywhere.</td></tr>
        <tr><td>Skipped the Benable links</td><td>Do not use third-party links. Use only customer-supplied product rows and authorized destinations.</td></tr>
        <tr><td>Destination</td><td>The customer's selected destination must resolve before scheduling.</td></tr>
        <tr><td>Made new images</td><td>New generated imagery uses the configured provider. Any scene inspiration is rewritten; no image is treated as an exact retail depiction without actual linked-product imagery.</td></tr>
        <tr><td>Scheduled</td><td>Scheduling is customer-approved and account-dependent; this example does not establish a live schedule.</td></tr>
      </table>
    </div>
  </div>
  <div class="call"><p><strong>Example only.</strong> Generated outfit imagery is inspiration unless each pictured item is the actual linked item or a clearly identified customer-owned/licensed product photo. Verify the public board, destination, disclosure, and approval before scheduling.</p></div>
  ${foot()}
</section>`);

// 10 troubleshooting
guide.push(`<section class="pg">${top(10)}
  <div class="kicker">When something's off</div>
  <h2>What the tasks do <em>when things go wrong.</em></h2>
  <div class="grid2" style="margin-top:10px">
    <div class="card"><h3>Pinterest loads blank</h3><p>If a required page or action is unavailable, stop the run, preserve completed drafts, and report what needs attention. Resume only from recorded state; do not promise an automatic retry or catch-up.</p></div>
    <div class="card"><h3>A connection is unavailable</h3><p>If a required connected account or action is unavailable, stop the affected work, preserve completed records, and report what needs attention. Never request or enter passwords in a task.</p></div>
    <div class="card"><h3>A board went secret</h3><p>Verify the exact board through an authorized supported path before scheduling. If public status cannot be verified, schedule nothing.</p></div>
    <div class="card"><h3>A run was missed</h3><p>Check the scheduler and state record. Resume from recorded work, avoid duplicates, and report skipped items. Do not promise automatic recovery until the customer's workflow has demonstrated it.</p></div>
    <div class="card"><h3>You want to remove a Pin</h3><p>Use the removal action supported by the selected publisher. If it is already published and the publisher cannot remove it, remove it in Pinterest and record the confirmed result.</p></div>
    <div class="card"><h3>An image comes out wrong</h3><p>Follow the kit's defined image-attempt limit. If framing, required pieces, or product fidelity still fail, drop the look and record why. Add the headline only after the visual acceptance checks pass.</p></div>
  </div>
  <div class="call"><p>Reports must state what was drafted, approved, scheduled, and verified, and identify any action that still needs you.</p></div>
  ${foot()}
</section>`);

// 11 what's next
guide.push(`<section class="pg">${top(11)}
  <div class="kicker">What's next</div>
  <h2>Add the blog half, <em>or hand it to me.</em></h2>
  <div class="card" style="margin-top:8px"><h3>Have The Weekend Ecosystem&trade;?</h3>
    <p>09_THE_BLOG_HALF.txt adds a shop-the-look section to your site in one paste, with every look page written for Google. My Pinterest block is on my domain only, so your pins can link to your own pages.</p>
    <p>Don't have it? The machine runs without a site, straight to your Idea Lists. If you ever want the blog half too, <a href="${WE}">The Weekend Ecosystem&trade;</a> is $97 one-time, or 3 &times; $33.33.</p></div>
  <div class="card" style="margin-top:16px"><h3>Recommend this kit</h3>
    <p>Members of The Digital Income Edit&trade; earn 40% on every sale they refer, through Beacons' own affiliate feature. The four steps are in 11_WHATS_NEXT.txt.</p></div>
  <div class="hotcard" style="margin-top:16px"><h3>Want it done for you?</h3>
    <p>The DFY Amazon Storefront Launch is $297 for 10 themed looks: each an Idea List in your storefront plus 2 pins with your #ad disclosure, built on the same method you're holding.</p>
    <p><a href="${DFY}" style="color:#fff">See the DFY Amazon Storefront Launch</a></p></div>
  <div style="margin-top:34px;font:600 30px/1 Newsreader,serif;color:var(--hot)">xoxo, Jodie</div>
  ${foot()}
</section>`);

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
    <p style="margin-top:22px;font-size:15px">Want a head start? Check that your account has ChatGPT Work and Scheduled Tasks, Amazon Associates, a Pinterest business account with a verifiable public board, and the connected storage, publisher, and image-provider actions your chosen setup needs. Availability varies by account; see the setup guide before purchasing subscriptions.</p>
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
