#!/usr/bin/env node
/**
 * Independent rendered-image QA. Fail closed if credentials are unavailable.
 * Usage: node ops/visual-qa/visual-review.mjs --image screenshot.png --brief requirements.txt
 * OPENAI_API_KEY required; optional VISUAL_REVIEW_MODEL.
 */
import {readFile,writeFile} from 'node:fs/promises';
import {extname,resolve} from 'node:path';
const args=process.argv.slice(2);
const opt=(n,d)=>{let i=args.indexOf(n);return i<0?d:args[i+1]};
const image=opt('--image'),brief=opt('--brief'),out=opt('--out','visual-review.json');
if(!image||!brief)throw Error('Required: --image and --brief');
if(!process.env.OPENAI_API_KEY)throw Error('OPENAI_API_KEY missing: independent visual review was NOT performed');
const bytes=await readFile(resolve(image));
const mime=extname(image).toLowerCase()==='.jpg'?'image/jpeg':'image/png';
const requirements=await readFile(resolve(brief),'utf8');
const instructions='You are an independent visual art director and QA inspector, NOT the designer. Assess the ACTUAL image, not the prompt. Return JSON object {"pass":boolean,"score":number,"defects":[{"severity":"critical|major|minor","issue":string,"location":string,"exact_fix":string}],"strengths":[string]}. Fail if exact text unreadable, image cropped, amateur composition, obvious AI artifacts, unbalanced whitespace, poor typography, insufficient contrast, or any violated requirement. Do not grant pass for technically correct but ugly work. Requirements:\n'+requirements;
const response=await fetch('https://api.openai.com/v1/responses',{method:'POST',headers:{Authorization:'Bearer '+process.env.OPENAI_API_KEY,'Content-Type':'application/json'},body:JSON.stringify({model:process.env.VISUAL_REVIEW_MODEL||'gpt-4.1',input:[{role:'user',content:[{type:'input_text',text:instructions},{type:'input_image',image_url:'data:'+mime+';base64,'+bytes.toString('base64')}]}],text:{format:{type:'json_object'}},max_output_tokens:2000})});
const data=await response.json();if(!response.ok)throw Error(JSON.stringify(data));
const answer=data.output?.flatMap(o=>o.content||[]).filter(c=>c.type==='output_text').map(c=>c.text).join('');
if(!answer)throw Error('Review response missing text');
const review=JSON.parse(answer);await writeFile(resolve(out),JSON.stringify(review,null,2));
console.log(JSON.stringify(review));if(!review.pass)process.exitCode=1;
