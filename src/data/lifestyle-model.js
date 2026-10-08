// Pure compatibility and publication rules for the existing Lifestyle JSON system.
export const IMAGE_ROLES = new Set(['basic', 'styled', 'lifestyle']);
export const AFFILIATE_STATES = new Set(['verified', 'none', 'pending', 'legacy']);
export const isDraft = (record) => ['draft', 'STAGED_NOT_PUBLIC'].includes(record.status) || record.draft === true;

export function shoppingUrl(value) {
  try {
    const url = new URL(value);
    return url.protocol === 'https:' && !url.username && !url.password &&
      (['amzn.to', 'link.amazon', 'amazon.com', 'www.amazon.com'].includes(url.hostname)) ? url : null;
  } catch { return null; }
}

export function validateDestination(item) {
  if (!shoppingUrl(item.link)) throw new Error(`Invalid Amazon destination for "${item.name}"`);
  if (item.affiliateStatus && !AFFILIATE_STATES.has(item.affiliateStatus)) throw new Error(`Invalid affiliateStatus for "${item.name}"`);
  if (item.asin && !/^[A-Z0-9]{10}$/.test(item.asin)) throw new Error(`Invalid ASIN for "${item.name}"`);
  const match = new URL(item.link).pathname.match(/\/(?:dp|gp\/product)\/([A-Z0-9]{10})(?:\/|$)/i);
  if (match && item.asin && match[1].toUpperCase() !== item.asin) throw new Error(`Destination ASIN mismatch for "${item.name}"`);
  if (item.affiliateStatus === 'verified' && !item.verifiedAt) throw new Error(`Verified destination needs verifiedAt for "${item.name}"`);
  if (!item.affiliateStatus && /^(www\.)?amazon\.com$/.test(new URL(item.link).hostname) && match && !new URL(item.link).searchParams.has('tag')) {
    return 'none';
  }
  return item.affiliateStatus || 'legacy';
}

export function normalizeLook(record, imageFor, categories, { preview = false } = {}) {
  if (isDraft(record) && !preview) return null;
  const label = record.slug || '(missing slug)';
  const fail = (message) => { throw new Error(`Lifestyle ${label}: ${message}`); };
  if (!/^[a-z0-9]+(?:-[a-z0-9]+)*$/.test(record.slug || '') || !record.title || !categories.some(c => c.slug === record.category)) fail('requires a valid slug, title and category');
  if (categories.some(c => c.slug === record.slug)) fail('slug collides with a category');
  if (record.status && !['draft', 'published', 'STAGED_NOT_PUBLIC'].includes(record.status)) fail('status must be draft or published');
  if (record.date && (!/^\d{4}-\d{2}-\d{2}$/.test(record.date) || !Number.isFinite(Date.parse(record.date)) || new Date(record.date).toISOString().slice(0, 10) !== record.date)) fail('date must be a valid YYYY-MM-DD');
  const declaredImages = (record.images || []).map((image, index) => {
    if (!image.file || !/^(?:drafts\/)?[^\\/]+$/.test(image.file) || ['.', '..'].includes(image.file)) fail('image file must be a filename in src/lifestyle or its drafts folder');
    if (image.file.startsWith('drafts/') && !isDraft(record)) fail('private draft image must move to public assets before publication');
    const src = imageFor(image.file);
    if (!src && !isDraft(record)) fail(`missing image ${image.file}`);
    if (image.role && !IMAGE_ROLES.has(image.role)) fail(`unknown image role ${image.role}`);
    if (!image.alt?.trim()) fail(`image ${image.file} requires alt text`);
    if (image.order !== undefined && !Number.isFinite(image.order)) fail('image order must be numeric');
    const role = image.role || (/-flatlay\./i.test(image.file) ? 'basic' : /-lifestyle\./i.test(image.file) ? 'lifestyle' : 'styled');
    const fallback = role === 'basic' ? 'The arrangement, with contextual styling extras. Shop the listed products below.' : role === 'styled' ? 'The finished styling, shown as generated inspiration.' : record.category === 'clothing' ? 'The outfit styled on Tommy Kate, our AI model.' : 'A lifestyle view of the setting, shown as generated inspiration.';
    return { ...image, role, caption: image.caption || fallback, order: image.order ?? index, src };
  }).sort((a, b) => a.order - b.order);
  const images = declaredImages.filter(image => image.src);
  const missingImageFiles = declaredImages.filter(image => !image.src).map(image => image.file);
  const items = (record.items || []).map((item) => {
    if (!item.name) fail('each product requires a name');
    if (!item.link && isDraft(record)) return { ...item, affiliateStatus: 'pending' };
    const affiliateStatus = validateDestination({ ...item, affiliateStatus: item.affiliateStatus || (item.affiliate_link_verified === false ? 'pending' : undefined) });
    if (!isDraft(record) && affiliateStatus === 'pending' && record.shoppingStatus !== 'pending') fail(`pending destination for ${item.name}; keep the article draft`);
    return { ...item, affiliateStatus };
  });
  if (!isDraft(record) && (!images.length || !items.length)) fail('published articles require at least one image and product');
  if (images.filter(image => image.hero).length > 1) fail('only one hero image is allowed');
  if (record.ideaList && (!shoppingUrl(record.ideaList) || !/^\/shop\/[^/]+\/list\/[^/]+\/?$/.test(new URL(record.ideaList).pathname) || !['www.amazon.com', 'amazon.com'].includes(new URL(record.ideaList).hostname))) fail('invalid Idea List destination');
  if (record.ideaListStatus && !['verified', 'pending', 'legacy'].includes(record.ideaListStatus)) fail('invalid ideaListStatus');
  if (!isDraft(record) && record.ideaListStatus === 'pending' && (record.shoppingStatus !== 'pending' || record.ideaList)) fail('pending Idea List; keep the article draft');
  if (record.sections && !record.sections.every(s => s.heading && Array.isArray(s.paragraphs) && s.paragraphs.every(p => typeof p === 'string' && p.trim()))) fail('sections require a heading and paragraphs');
  const hero = images.find(image => image.hero) || images.find(image => image.role === 'styled') || images.find(image => image.role === 'lifestyle') || images[0];
  return { ...record, status: isDraft(record) ? 'draft' : 'published', images, missingImageFiles, items, hero, description: record.description || record.intro || record.title };
}

export const byEditorialDate = (a, b) => String(b.date || '').localeCompare(String(a.date || '')) || a.slug.localeCompare(b.slug);
