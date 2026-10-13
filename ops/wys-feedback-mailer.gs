// The While-You-Sleep Storefront™ feedback mailer.
// Runs in Jodie's own Google account (script.google.com). The website sends each
// feedback-box message here, and this emails it to the account that owns the script,
// with any photo attached. The passcode is checked so nobody else can use it.
const PASSCODE = 'PASTE_PASSCODE_HERE';

function doPost(e) {
  let d;
  try { d = JSON.parse(e.postData.contents); } catch (err) { return out('bad'); }
  if (!d || d.secret !== PASSCODE) return out('no');

  const to = Session.getEffectiveUser().getEmail();
  const who = d.name || d.email || 'A buyer';
  const esc = s => String(s || '').replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
  const html =
    '<p><b>From:</b> ' + esc(d.name || '(no name)') + (d.email ? ' &lt;' + esc(d.email) + '&gt;' : ' (no email given)') + '</p>' +
    '<p><b>Page:</b> ' + esc(d.page) + '<br><b>Sent:</b> ' + esc(d.created) + '</p>' +
    '<p style="white-space:pre-wrap;font-size:15px">' + esc(d.message || '(no message, photo only)') + '</p>' +
    (d.photo ? '<p>Their photo is attached.</p>' : '');

  const opts = { htmlBody: html, name: 'Storefront feedback box' };
  if (d.email) opts.replyTo = d.email;
  if (d.photo) opts.attachments = [Utilities.newBlob(Utilities.base64Decode(d.photo), d.photoType || 'image/jpeg', d.photoName || 'screenshot.jpg')];

  MailApp.sendEmail(to, 'Storefront feedback from ' + who, (d.message || ''), opts);
  return out('ok');
}

function out(t) { return ContentService.createTextOutput(t); }
