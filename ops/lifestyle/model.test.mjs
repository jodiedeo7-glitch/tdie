import test from 'node:test';
import assert from 'node:assert/strict';
import { normalizeLook, validateDestination, byEditorialDate } from '../../src/data/lifestyle-model.js';
const categories = [{ slug: 'clothing' }, { slug: 'home-decor' }, { slug: 'car' }];
const record = { slug: 'pink-scene', title: 'Pink Scene', category: 'home-decor', images: [{ file: 'pink-scene-lifestyle.jpg', alt: 'A woman beside a decorated console.' }], items: [{ name: 'Existing find', link: 'https://link.amazon/Existing' }] };
const normalize = (r, options) => normalizeLook(r, () => ({ src: '/test.jpg' }), categories, options);
test('legacy records preserve destinations and neutral decor captions', () => {
 const look = normalize(record); assert.equal(look.items[0].link, record.items[0].link); assert.equal(look.items[0].affiliateStatus, 'legacy'); assert.equal(look.status, 'published'); assert.equal(look.images[0].role, 'lifestyle'); assert.doesNotMatch(look.images[0].caption, /worn|outfit|every one linked/i);
});
test('fashion fallback is scoped to clothing; unlabelled images stay neutral', () => {
 assert.match(normalize({ ...record, category: 'clothing' }).images[0].caption, /outfit/);
 assert.equal(normalize({ ...record, category: 'car', images: [{ file: 'scene.jpg', alt: 'Pink car interior.' }] }).images[0].role, 'styled');
});
test('explicit roles, captions, order and hero take priority over filenames', () => {
 const look = normalize({ ...record, images: [{ file: 'a-lifestyle.jpg', alt: 'Arrangement', role: 'basic', order: 2, caption: 'Approved caption.' }, { file: 'b.jpg', alt: 'Finished room', role: 'styled', order: 1, hero: true }] });
 assert.equal(look.hero.file, 'b.jpg'); assert.equal(look.images[1].role, 'basic'); assert.equal(look.images[1].caption, 'Approved caption.');
});
test('drafts are excluded before resolving private assets, and preview is explicit', () => {
 assert.equal(normalizeLook({ ...record, status: 'draft' }, () => { throw Error('should not resolve'); }, categories), null);
 assert.equal(normalize({ ...record, status: 'draft', images: [], items: [] }, { preview: true }).status, 'draft');
 assert.equal(normalize({ ...record, draft: true }), null);
});
test('pending destinations cannot enter public articles', () => {
 assert.throws(() => normalize({ ...record, items: [{ ...record.items[0], affiliateStatus: 'pending' }] }), /pending destination/);
 assert.equal(normalize({ ...record, status: 'draft', items: [{ name: 'Pending find' }] }, { preview: true }).items[0].affiliateStatus, 'pending');
 assert.throws(() => normalize({ ...record, ideaListStatus: 'pending' }), /pending Idea List/);
});
test('ASIN mismatch and unsafe destinations fail instead of becoming shopping buttons', () => {
 assert.throws(() => validateDestination({ name: 'Find', asin: 'B012345678', link: 'https://www.amazon.com/dp/B098765432' }), /mismatch/);
 for (const link of ['javascript:alert(1)', 'https://amazon.com.evil.test/dp/B012345678', 'http://amazon.com/dp/B012345678', 'https://user@amazon.com/dp/B012345678']) assert.throws(() => validateDestination({ name: 'Find', link }), /Invalid/);
 assert.equal(validateDestination({ name: 'Find', asin: 'B012345678', link: 'https://www.amazon.com/dp/B012345678' }), 'none');
 assert.throws(() => validateDestination({ name: 'Find', link: 'https://amzn.to/abc', affiliateStatus: 'verified' }), /verifiedAt/);
});
test('published records fail on missing images, invalid metadata and category collisions', () => {
 assert.throws(() => normalizeLook(record, () => null, categories), /missing image/);
 assert.throws(() => normalize({ ...record, slug: 'home-decor' }), /collides/);
 assert.throws(() => normalize({ ...record, images: [] }), /at least one/);
 assert.throws(() => normalize({ ...record, images: [{ file: '../private.png', alt: 'A scene' }] }), /filename/);
 assert.throws(() => normalize({ ...record, date: '2026-02-30' }), /valid YYYY-MM-DD/);
 assert.throws(() => normalize({ ...record, images: [{ file: 'a.jpg', alt: '' }] }), /alt text/);
});
test('ordering is deterministic with dates and tie-breaking slugs', () => {
 assert.deepEqual([{ slug: 'z', date: '2026-10-01' }, { slug: 'b' }, { slug: 'a', date: '2026-10-01' }].sort(byEditorialDate).map(r => r.slug), ['a', 'z', 'b']);
});

test('staged source records and explicit unverified affiliate flags stay private', () => {
 assert.equal(normalize({ ...record, status: 'STAGED_NOT_PUBLIC' }), null);
 assert.equal(normalize({ ...record, status: 'STAGED_NOT_PUBLIC' }, { preview: true }).status, 'draft');
 assert.throws(() => normalize({ ...record, items: [{ ...record.items[0], affiliate_link_verified: false }] }), /pending destination/);
});

test('draft image metadata can await transfer while public missing images fail', () => {
 const look = normalizeLook({ ...record, status: 'draft' }, () => null, categories, { preview: true });
 assert.deepEqual(look.images, []); assert.deepEqual(look.missingImageFiles, ['pink-scene-lifestyle.jpg']);
 assert.throws(() => normalizeLook(record, () => null, categories), /missing image/);
});

test('private photo paths work only in drafts and cannot traverse directories', () => {
 const images = [{ file: 'drafts/approved.png', alt: 'Approved scene' }];
 assert.equal(normalize({ ...record, status: 'draft', images }, { preview: true }).images.length, 1);
 assert.throws(() => normalize({ ...record, images }), /private draft image/);
 for (const file of ['drafts/../approved.png', '/approved.png', '../approved.png']) assert.throws(() => normalize({ ...record, status: 'draft', images: [{ file, alt: 'Scene' }] }, { preview: true }), /filename/);
});

test('authorized public articles may keep pending destinations hidden', () => {
 const pending = { ...record, shoppingStatus: 'pending', items: [{ ...record.items[0], affiliateStatus: 'pending' }] };
 assert.equal(normalize(pending).items[0].affiliateStatus, 'pending');
 assert.throws(() => normalize({ ...pending, ideaListStatus: 'pending', ideaList: 'https://www.amazon.com/shop/example/list/EXAMPLE' }), /pending Idea List/);
});
