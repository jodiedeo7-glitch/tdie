// The While-You-Sleep Storefront™ feedback mailer.
// Runs in Jodie's own Google account (script.google.com). The website sends each message from
// the buyer box here, and this emails it to the account that owns the script, with photos attached.
// The passcode is checked so nobody else can use it.
const PASSCODE = 'PASTE_PASSCODE_HERE';

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (err) { return out('bad'); }
  if (!d || d.secret !== PASSCODE) return out('no');
  const to = Session.getEffectiveUser().getEmail();
  const who = d.name || d.email || 'A buyer';
  const love = d.kind === 'love';
  const esc = s => String(s || '').replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const photos = Array.isArray(d.photos) ? d.photos : [];
  const html =
    '<p><b>' + (love ? 'A set they love' : 'Something looks weird') + '</b>' +
    (love ? (d.consent ? ' · <b style="color:#1d6b43">OK to share as real results</b>' : ' · not for sharing') : '') + '</p>' +
    '<p><b>From:</b> ' + esc(d.name || '(no name)') + (d.email ? ' &lt;' + esc(d.email) + '&gt;' : ' (no email given)') +
    (d.credit ? '<br><b>Credit them as:</b> ' + esc(d.credit) : '') + '</p>' +
    '<p><b>Page:</b> ' + esc(d.page) + '<br><b>Sent:</b> ' + esc(d.created) + '</p>' +
    '<p style="white-space:pre-wrap;font-size:15px">' + esc(d.message || '(no message)') + '</p>' +
    (photos.length ? '<p>' + photos.length + ' photo' + (photos.length > 1 ? 's' : '') + ' attached.</p>' : '');
  const opts = { htmlBody: html, name: 'Storefront buyer box' };
  if (d.email) opts.replyTo = d.email;
  if (photos.length) opts.attachments = photos.map((p, i) => Utilities.newBlob(Utilities.base64Decode(p.data), p.type || 'image/jpeg', p.name || ('photo-' + (i + 1) + '.jpg')));
  MailApp.sendEmail(to, (love ? 'Storefront: a set ' + who + ' loves' : 'Storefront feedback from ' + who), (d.message || ''), opts);
  return out('ok');
}

function out(t) { return ContentService.createTextOutput(t); }
