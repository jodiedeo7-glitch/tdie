'use strict';
const {strict:assert}=require('node:assert');
const {expectedCounts,validate}=require('./validate_premium_month_counts.cjs');
function packet(month){
 const n=expectedCounts(month).instagram_days;
 const dates=Array.from({length:n},(_,i)=>month+'-'+String(i+1).padStart(2,'0'));
 return {month,instagram:dates.map(date=>({date})),threads:dates.flatMap(date=>[{date,slot:1},{date,slot:2}])};
}
for(const [month,days] of [['2026-10',31],['2026-11',30],['2027-02',28],['2028-02',29]]){
 assert.deepEqual(expectedCounts(month),{instagram_days:days,threads_posts:days*2});
 assert.deepEqual(validate(packet(month)),[]);
}
const duplicate=packet('2026-11'); duplicate.instagram[29]={date:'2026-11-01'};
assert.ok(validate(duplicate).some(x=>x.startsWith('Expected one')));
const wrongSlots=packet('2026-11');wrongSlots.threads[1].slot=1;
assert.ok(validate(wrongSlots).includes('duplicate member Threads date/slot'));
const outside=packet('2026-11');outside.threads[59].date='2026-12-01';
assert.ok(validate(outside).includes('Threads date outside covered month'));
assert.throws(()=>expectedCounts('2026-13'));
assert.throws(()=>expectedCounts('2026-1'));
assert.ok(validate({month:'2026-11'}).length);
console.log('PASS: October31/62, November30/60, February28/56, leap February29/58; missing/duplicate/out-of-month coverage and invalid input rejected.');
