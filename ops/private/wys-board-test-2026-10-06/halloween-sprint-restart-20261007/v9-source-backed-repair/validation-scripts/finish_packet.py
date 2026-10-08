from pathlib import Path
import json,hashlib,shutil,zipfile
from PIL import Image,ImageOps,ImageDraw
root=Path(__file__).resolve().parent.parent
out=root/'outputs/Packet-1-V9'
repo=root/'work/tdie'
rel=Path('ops/private/wys-board-test-2026-10-06/halloween-sprint-restart-20261007/v9-source-backed-repair')
screens=sorted((out/'document-qa').glob('look-*-desktop.png'))
sheet=Image.new('RGB',(960,825),'#eee7f3');d=ImageDraw.Draw(sheet)
for i,f in enumerate(screens):
 im=Image.open(f);im.thumbnail((310,250));x=(i%3)*320;y=(i//3)*275
 sheet.paste(im,(x,y+20));d.text((x+8,y+3),f.stem,fill='#241b27')
sheet.save(root/'work/document-contact-sheet.jpg')
qa=json.loads((out/'document-qa/RENDER-CHECKS.json').read_text())
(out/'.gitattributes').write_text('* -text\n',encoding='utf-8')
assert qa['downloadByteMatch'] and qa['promptTextExactMatches']==27
v=json.loads((out/'VALIDATION.json').read_text());v['rendered_document_QA']=qa
v['rendered_document_QA']['scope']='Document rendering, exact prompt text, functioning controls and byte-identical attachment download only; no generated-image visual QA.'
(out/'VALIDATION.json').write_text(json.dumps(v,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
audit='''SOURCE READ AND DOCUMENT CHECK AUDIT — 8 October 2026

Read the governing specification, 66-rule ledger, recovered user-instruction archive and approval evidence. Inspected all thirteen original clothing screenshots and the preserved approved cardigan BASIC/STYLED/LIFESTYLE trio. Read the supplied historical prompt and acceptance/rejection records used for this repair. The source bundle describes its historical coverage; unavailable earlier conversation history was not read and is not claimed.

All 292 recovered source files were preserved byte-for-byte and are recorded in SOURCE-HASH-MANIFEST.json. Prior failed packets remain source history, not new approvals. Product files are originals, not edited derivatives.

The rendered standalone document passed at 1280, 390 and 320 pixels with no horizontal page overflow, no broken displayed images, no JavaScript errors and all 27 exact prompt texts. All 27 copy controls responded. All 39 unique embedded downloadable assets resolved; one actual clothing-photo download matched its original bytes. Browser downloads required running the local read-only check outside the restricted browser sandbox; the HTML itself did not require changes or a server.

Manual document inspection covers readability and source-photo presentation. It does not approve future generated images, retail fit, current stock, missing affiliate/list records, the look-4 merge, short-shopping-list policy exceptions or the selected-bow preference conflict. No generation, client release, publication, deployment or global memory write occurred.
'''
(out/'SOURCE-READ-AND-DOCUMENT-AUDIT.txt').write_text(audit,encoding='utf-8')
govern=repo/'AGENTS.md';text=govern.read_text(encoding='utf-8')
marker='Packet 1 V9 document repair'
if marker not in text:
 text+='\n'+marker+': follow `ops/wys-memory/README.md` and `ops/wys-memory/2026-10-07-recovered-spec/GOVERNING-SPEC.md` first. Latest repair and evidence: `'+rel.as_posix()+'/`. Static prompt/document coverage is not generated-image or client-release approval.\n'
 govern.write_text(text,encoding='utf-8')
shutil.copytree('\\\\?\\'+str(out),'\\\\?\\'+str(repo/rel),dirs_exist_ok=True)
dest=repo/rel/'validation-scripts';dest.mkdir(exist_ok=True)
for name in ['build_repair.py','verify_packet.cjs','finish_packet.py']:
 (Path('\\\\?\\'+str(dest/name))).write_text((root/'work'/name).read_text(encoding='utf-8-sig').rstrip()+'\n',encoding='utf-8')
zip_path=root/'outputs/WYS-PACKET-1-V9.zip'
files=sorted(f for f in out.rglob('*') if f.is_file())
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
 for f in files:z.write(f,f.relative_to(out).as_posix())
with zipfile.ZipFile(zip_path) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
 for f in files:assert hashlib.sha256(z.read(f.relative_to(out).as_posix())).digest()==hashlib.sha256(f.read_bytes()).digest()
print(json.dumps({'zip':str(zip_path),'bytes':zip_path.stat().st_size,'zip_files':len(files),'html_bytes':(out/'FULL-PACKET-1.html').stat().st_size,'document_checks':'PASS'},indent=2))
