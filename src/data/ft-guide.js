// Turns the Build & Sell Your Own Bot guide (plain text file) into sections the page can design.
import raw from './faceless-team-guide.md?raw';
const esc = (s) => s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
const inline = (s) => esc(s).replace(/\*\*(.+?)\*\*/g, '<strong>$1</strong>').replace(/`(.+?)`/g, '<code>$1</code>');
function blocks(text) {
 const out = []; let list = null, para = [];
 const flushP = () => { if (para.length) { out.push(`<p>${inline(para.join(' '))}</p>`); para = []; } };
 const flushL = () => { if (list) { out.push(`<${list.tag}>${list.items.map((i) => `<li>${inline(i)}</li>`).join('')}</${list.tag}>`); list = null; } };
 for (const l of text.split('\n')) {
  const o = l.match(/^\d+\.\s+(.*)$/), u = l.match(/^-\s+(.*)$/);
  if (o || u) { flushP(); const tag = o ? 'ol' : 'ul'; if (!list || list.tag !== tag) { flushL(); list = {tag, items: []}; } list.items.push((o || u)[1]); }
  else if (!l.trim()) { flushP(); flushL(); }
  else { flushL(); para.push(l.trim()); }
 }
 flushP(); flushL(); return out.join('\n');
}
export const GUIDE = raw.split(/\n## /).slice(1).map((sec) => {
 const [head, ...rest] = sec.split('\n');
 const m = head.match(/^Step (\d+) · (.*)$/);
 const body = rest.join('\n').trim();
 const items = [...body.matchAll(/^\d+\.\s+(.*)$/gm)].map((x) => x[1]);
 return {step: m ? +m[1] : null, title: m ? m[2] : head.trim(), html: blocks(body), items, id: m ? `step-${m[1]}` : head.trim().toLowerCase().replace(/[^a-z]+/g, '-').replace(/^-|-$/g, '')};
});
