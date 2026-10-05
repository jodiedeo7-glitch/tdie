import fs from 'node:fs';
import vm from 'node:vm';
import assert from 'node:assert/strict';
const source = fs.readFileSync(new URL('../src/components/PinkFindsSignup.astro', import.meta.url), 'utf8');
const script = source.match(/<script is:inline>([\s\S]*?)<\/script>/)[1];
function fixture(value) {
  const events = {}, frames = {}, attrs = {}, errors = {textContent:''};
  const input = {value, checkValidity:()=>value.includes('@'), setAttribute:(k,v)=>attrs[k]=v, removeAttribute:k=>delete attrs[k], addEventListener:(k,v)=>events['input:'+k]=v, focus:()=>{}};
  const button={disabled:false,textContent:'Send Me the Finds'};
  const pending={hidden:true,focus:()=>{}};
  const form={target:'sink',setAttribute:()=>{},classList:{toggle:()=>{}},querySelector:s=>s.startsWith('input')?input:s==='.pf-error'?errors:s==='.pf-done'?pending:button,addEventListener:(k,v)=>events[k]=v};
  const document={querySelectorAll:s=>s.startsWith('form')?[form]:[],getElementsByName:()=>[{addEventListener:(k,v)=>frames[k]=v}]};
  const calls=[];let timer;
  vm.runInNewContext(script,{document,window:{fbq:()=>calls.push('lead')},fbq:()=>calls.push('lead'),setTimeout:fn=>(timer=fn,1),clearTimeout:()=>{}});
  return {events,frames,button,pending,errors,calls,retry:()=>timer()};
}
for (const email of ['', 'broken', 'a@b']) {
  const f=fixture(email);let prevented=false;
  f.events.submit({preventDefault:()=>prevented=true,stopImmediatePropagation:()=>{}});
  assert.equal(prevented,true);assert.equal(f.pending.hidden,true);assert.equal(f.button.disabled,false);
}
const f=fixture('person@example.com');
f.frames.load();assert.equal(f.pending.hidden,true,'initial frame load must not show submission');
f.events.submit({preventDefault:()=>assert.fail('valid email blocked')});
assert.equal(f.pending.hidden,false);assert.equal(f.button.disabled,true);
f.frames.load();assert.equal(f.button.disabled,false);assert.deepEqual(f.calls,[],'frame load is not a verified lead');
const stalled=fixture('person@example.com');stalled.events.submit({});stalled.retry();assert.equal(stalled.button.disabled,false,'stalled response allows deliberate retry');
const page=fs.readFileSync(new URL('../src/pages/lifestyle/[slug].astro',import.meta.url),'utf8');
const fn=page.match(/export function getStaticPaths\(\) \{([\s\S]*?)\n\}/)[1];
const paths=(looks,categories)=>vm.runInNewContext('(function(){'+fn+'})()',{LOOKS:looks,CATEGORIES:categories});
assert.equal(paths([{slug:'outfit'}],[{slug:'clothing'}]).length,2);
assert.throws(()=>paths([{slug:'outfit'},{slug:'outfit'}],[]),/Duplicate/);
assert.throws(()=>paths([{slug:'clothing'}],[{slug:'clothing'}]),/collides/);
console.log('PASS: invalid email, initial frame, pending submission, no false Lead, stalled retry, valid routes, duplicate look, category collision.');
