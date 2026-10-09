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
