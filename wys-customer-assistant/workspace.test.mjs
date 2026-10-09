import test from 'node:test';
import assert from 'node:assert/strict';
import {handle} from '../src/worker/api/wys-workspace.js';

test('workspace fails closed without storage and scoped secret',async()=>{
 const response=await handle(new Request('https://example.test/api/wys-workspace'),{});
 assert.equal(response.status,503);
});

test('workspace rejects missing credentials',async()=>{
 const response=await handle(new Request('https://example.test/api/wys-workspace'),{WYS_DB:{},WYS_ACCESS_SECRET:'test-only'});
 assert.equal(response.status,401);
});

test('workspace rejects malformed bearer credentials',async()=>{
 const response=await handle(new Request('https://example.test/api/wys-workspace',{headers:{Authorization:'Bearer not-a-valid-token'}}),{WYS_DB:{},WYS_ACCESS_SECRET:'test-only'});
 assert.equal(response.status,401);
});

import {sign} from '../src/worker/auth.js';
function database(){
 const customers=new Map([['buyer@example.test','buyer-1'],['other@example.test','buyer-2']]);
 const preferences=new Map();
 return {prepare(sql){let args=[];return {bind(...v){args=v;return this},async first(){
 if(sql.includes('FROM wys_customers'))return customers.has(args[0])?{id:customers.get(args[0])}:null;
 if(sql.includes('FROM wys_preferences'))return preferences.has(args[0])?{preferences_json:preferences.get(args[0]),updated_at:'2026-10-09'}:null;
 throw Error('Unexpected SQL');
 },async run(){if(!sql.startsWith('INSERT INTO wys_preferences'))throw Error('Unexpected SQL');preferences.set(args[0],args[1]);return {success:true}}}}};
}
const secret='test-only-not-for-production';
async function request(method,token,body,db){
 return handle(new Request('https://example.test/api/wys-workspace',{method,headers:{Authorization:'Bearer '+token,...(body?{'Content-Type':'application/json'}:{})},...(body?{body:JSON.stringify(body)}:{})}),{WYS_DB:db,WYS_ACCESS_SECRET:secret});
}
test('verified buyer saves and resumes setup',async()=>{
 const db=database(),token=await sign('buyer@example.test',secret);
 assert.equal((await request('PUT',token,{preferences:{niche:'Home decor',amazon:'Associates'}},db)).status,200);
 const result=await request('GET',token,null,db);
 assert.equal(result.status,200);
 assert.deepEqual((await result.json()).preferences,{niche:'Home decor',amazon:'Associates'});
});
test('nonbuyer denied even with signed token',async()=>{
 const db=database(),token=await sign('stranger@example.test',secret);
 assert.equal((await request('GET',token,null,db)).status,403);
});
test('customers cannot read each other preferences',async()=>{
 const db=database(),a=await sign('buyer@example.test',secret),b=await sign('other@example.test',secret);
 await request('PUT',a,{preferences:{niche:'Private buyer A'}},db);
 const result=await request('GET',b,null,db);
 assert.deepEqual((await result.json()).preferences,{});
});
test('rejects unknown fields and non-string values',async()=>{
 const db=database(),token=await sign('buyer@example.test',secret);
 assert.equal((await request('PUT',token,{preferences:{isAdmin:true}},db)).status,400);
 assert.equal((await request('PUT',token,{preferences:{niche:5}},db)).status,400);
});
