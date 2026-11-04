#!/usr/bin/env python3
"""Structural package QA against an installed checkout, never live account QA."""
import argparse,ast,csv,json,re
from pathlib import Path
def validate(root):
    errors=[];root=Path(root)
    required=['ops/TDIE_AI_ROUTER.md','ops/ai-router/EXECUTION_CONTRACT.md','ops/ai-router/MIGRATION_SEQUENCE_V2.md','ops/ai-router/CONFLICT_REGISTER.md','ops/ai-router/WORKFLOW_REGISTRY.json','ops/ai-router/SOURCE_REGISTER.json','ops/ai-router/LEGACY_QUEUE_CROSSWALK.csv','ops/canon/canon.json','ops/canon/TDIE_CANON.md']
    for n in required:
        if not (root/n).is_file():errors.append('Missing '+n)
    if errors:return errors
    registry=json.loads((root/'ops/ai-router/WORKFLOW_REGISTRY.json').read_text(encoding='utf-8'))
    ids=[r['id'] for r in registry['workflows']];queues=[r['queue'] for r in registry['workflows']]
    if len(set(ids))!=len(ids) or len(set(queues))!=len(queues):errors.append('Duplicate workflow/queue')
    for p in queues:
        if not (root/p).is_file() or not p.startswith('ops/queues/'):errors.append('Bad queue '+p)
    if registry['find_your_door_automated'] is not False:errors.append('Find Your Door restored')
    for p in ['ops/cloud-output/queues','ops/ai-router/queues','ops/execution-queues','ops/ai-routing']:
        if (root/p).exists() and any(x.is_file() for x in (root/p).rglob('*')):errors.append('Competing draft tree '+p)
    for p in (root/'ops/jobs').glob('*.md'):
        text=p.read_text(encoding='utf-8')
        for token in ['NOT ACTIVATED','CRON_TZ=America/New_York','ops/canon/canon.json','VERIFY','REPORT']:
            if token not in text:errors.append(str(p.relative_to(root))+': missing '+token)
        if p.name.endswith('CLAUDE.md') and text.count('BROWSER FALLBACK RULE (')!=1:errors.append(p.name+': browser fallback count')
        if 'NEEDS_APPROVAL' in text:errors.append(p.name+': undefined state')
    for p in [root/'ops/TDIE_AI_ROUTER.md',*(root/'ops/jobs').glob('*.md'),*(root/'ops/ai-router').rglob('*.md')]:
        text=p.read_text(encoding='utf-8')
        if 'ops/ai-router/queues/' in text:errors.append('Stale queue path in '+p.name)
        for n in re.findall(r'`(ops/[\w./-]+\.(?:md|json|py|csv))`',text):
            if not (root/n).is_file():errors.append(p.name+': unresolved local path '+n)
    for p in (root/'ops/ai-router').rglob('*.json'):json.loads(p.read_text(encoding='utf-8'))
    for p in (root/'ops/scripts').glob('*.py'):
        try:ast.parse(p.read_text(encoding='utf-8'),filename=str(p))
        except SyntaxError as exc:errors.append(str(exc))
    daily=(root/'ops/ai-router/TDIE_DAILY_PROMPTS_ROUTER.md').read_text(encoding='utf-8')
    paid=(root/'ops/ai-router/TDIE_PAID_VIRAL_INSTAGRAM_ROUTER.md').read_text(encoding='utf-8')
    if 'SOP 16' not in daily or '8 AM' not in daily:errors.append('Daily source/time missing')
    if 'client' not in paid or 'SOP 15' not in paid:errors.append('Paid source/client isolation missing')
    for n in ['README_START_HERE.md','CLOUD_CREDIT_JOBS.md','CLOUD_CREDIT_JOBS_ROUND_2.md','JOB_THREADS_VIRAL_RESEARCH.md']:
        if 'ops/cloud-output/DESKTOP_FINISH_QUEUE.md' in (root/'ops/cloud-kit'/n).read_text(encoding='utf-8'):errors.append('Active legacy routing '+n)
    with (root/'ops/ai-router/LEGACY_QUEUE_CROSSWALK.csv').open(encoding='utf-8',newline='') as f:rows=list(csv.DictReader(f))
    if len(rows)!=17 or len({r['task_id'] for r in rows})!=17:errors.append('Legacy inventory incomplete')
    if any(r['source_status']=='RECORDED_DONE' and r['migration_status']!='ARCHIVE_NO_REPLAY' for r in rows):errors.append('Completed legacy item replayed')
    return errors
if __name__=='__main__':
    ap=argparse.ArgumentParser();ap.add_argument('--root',default=str(Path(__file__).resolve().parents[2]));a=ap.parse_args()
    try:errors=validate(Path(a.root))
    except (OSError,ValueError,KeyError) as exc:ap.exit(2,'ERROR: '+str(exc)+'\n')
    for e in errors:print('ERROR:',e)
    print(f'{len(errors)} errors; package structure only. No live automation state verified.')
    raise SystemExit(bool(errors))
