'use strict';
const fs = require('node:fs');
function expectedCounts(month) {
  if (!/^\d{4}-(0[1-9]|1[0-2])$/.test(month)) throw new Error('month must be YYYY-MM');
  const [year,mon] = month.split('-').map(Number);
  const days = new Date(Date.UTC(year, mon, 0)).getUTCDate();
  return { instagram_days: days, threads_posts: days * 2 };
}
function validate(packet) {
  const expected = expectedCounts(packet.month);
  const issues = [];
  if (!Array.isArray(packet.instagram) || !Array.isArray(packet.threads)) return ['instagram and threads arrays required'];
  if (packet.instagram.length !== expected.instagram_days) issues.push('Instagram total mismatch');
  if (packet.threads.length !== expected.threads_posts) issues.push('member Threads total mismatch');
  const dates = Array.from({length:expected.instagram_days}, (_,i)=>packet.month+'-'+String(i+1).padStart(2,'0'));
  const ig = new Map(), th = new Map(), seenSlots = new Set();
  for (const row of packet.instagram) {
    if (!dates.includes(row.date)) issues.push('Instagram date outside covered month');
    ig.set(row.date,(ig.get(row.date)||0)+1);
  }
  for (const row of packet.threads) {
    if (!dates.includes(row.date)) issues.push('Threads date outside covered month');
    if (row.slot !== 1 && row.slot !== 2) issues.push('member Threads slot must be 1 or 2');
    const key = row.date + ':' + row.slot;
    if (seenSlots.has(key)) issues.push('duplicate member Threads date/slot');
    seenSlots.add(key);
    th.set(row.date,(th.get(row.date)||0)+1);
  }
  for (const date of dates) {
    if (ig.get(date)!==1) issues.push('Expected one Instagram day: '+date);
    if (th.get(date)!==2) issues.push('Expected two member Threads: '+date);
  }
  return issues;
}
if (require.main === module) {
  try {
    const packet = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
    const issues = validate(packet);
    console.log(JSON.stringify({scope:'month counts and date coverage only; not research, creative, approval or live QA',expected:expectedCounts(packet.month),issues},null,2));
    process.exitCode = issues.length ? 1 : 0;
  } catch (err) { console.error(err.message); process.exitCode=2; }
}
module.exports={expectedCounts,validate};
