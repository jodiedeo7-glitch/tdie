from pathlib import Path
import subprocess

repo = Path(__file__).resolve().parents[2]
paths = [
 'ops/cloud-output/storefront-product/kit/01_REQUIREMENTS.txt',
 'ops/cloud-output/storefront-product/kit/02_SETUP_PROMPT.txt',
 'ops/cloud-output/storefront-product/kit/03_THEMED_LOOK_RECIPE.txt',
 'ops/cloud-output/storefront-product/kit/07_PERSONA_PATHS.txt',
 'ops/cloud-output/storefront-product/kit/13_PIN_VISUAL_STANDARD.md',
 'ops/cloud-output/storefront-product/kit/15_CATEGORY_IMAGE_BASES.md',
]
header = ('WYS SOURCE-BACKED MEMORY / READ BEFORE APPLYING THIS TEMPLATE\n'
 'Read ops/wys-memory/2026-10-07-recovered-spec/GOVERNING-SPEC.md and REQUIREMENTS-LEDGER.json in the TDIE repo (or the supplied recovery ZIP). Latest direct user instructions and scoped approvals govern over conflicting historical defaults below. Clothing BASIC is selected shopping items only; clothing STYLED requires visible as-if-worn garment volume without a person plus relevant personal extras. The objects-only in-situ formula must not replace clothing STYLED. Restore required readable labels for manual test packets. Static rules and document checks are not visual/client-release passes.\n\n')
patches = []
for rel in paths:
    path = repo / rel
    text = path.read_text(encoding='utf-8-sig')
    assert not text.startswith('WYS SOURCE-BACKED MEMORY'), f'Already installed: {rel}'
    path.write_text(header+text,encoding='utf-8')
    # Stage only this new pointer, independently of existing unstaged kit edits.
    head = subprocess.check_output(['git','show','HEAD:'+rel],cwd=repo).decode('utf-8-sig')
    added = ''.join('+'+line+'\n' for line in header.splitlines())
    patches.append(f'diff --git a/{rel} b/{rel}\n--- a/{rel}\n+++ b/{rel}\n@@ -0,0 +1,{len(header.splitlines())} @@\n'+added)
patch_file = repo/'ops/wys-memory/discovery-pointers-index.patch'
patch_file.write_text(''.join(patches),encoding='utf-8',newline='\n')
subprocess.run(['git','apply','--cached','--unidiff-zero',str(patch_file)],cwd=repo,check=True)
print('Installed and staged six discovery pointers only; prior unstaged kit edits preserved.')
