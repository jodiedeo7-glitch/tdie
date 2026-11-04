#!/usr/bin/env python3
"""Validate a TDIE Threads handoff manifest. Does NOT verify live account state."""
import csv, datetime as dt, hashlib, pathlib, re, sys
from collections import Counter, defaultdict

FIELDS = 'post_id,date,time,timezone,slot_type,body,hook_label,offer_name,reply_text,reply_due_time,article_reply_text,article_reply_due_time,source_urls,approval,status,reply_status,article_reply_status,content_hash'.split(',')
SLOTS = {'OPEN','ASK','TEACH','OFFER','PROOF','TAKE','UPDATE'}
SLOT_TIMES = {'OPEN':'07:00','ASK':'09:00','TEACH':'11:00','OFFER':'13:00','PROOF':'15:00','TAKE':'15:00','UPDATE':'17:00'}
STATUSES = {'DRAFT','QA_PASSED','APPROVED','READY','SCHEDULED','VERIFIED','BLOCKED'}
REPLY_STATUSES = {'NOT_REQUIRED','PENDING','READY','SCHEDULED','VERIFIED','BLOCKED'}
BANNED = ('game-changer','utilize','delve','unlock your potential','crush it')
URL = re.compile(r'(?i)https?://|\bwww\.|\b[a-z0-9-]+\.(?:com|net|org|io|co)/')

def validate(path):
    errors=[]; warnings=[]
    with open(path,encoding='utf-8-sig',newline='') as f:
        reader=csv.DictReader(f)
        if not reader.fieldnames or any(x not in reader.fieldnames for x in FIELDS):
            return ['Missing columns: '+', '.join(x for x in FIELDS if x not in (reader.fieldnames or []))], []
        rows=list(reader)
    if not rows: return ['Manifest has no rows'], []
    ids=set(); schedule=set(); bodies=set(); days=defaultdict(list); hooks=defaultdict(set)
    for n,r in enumerate(rows,2):
        if any(r.get(x) is None for x in FIELDS):
            errors.append(f'row {n}: incomplete row'); continue
        label=f'row {n}'; body=r['body']; date=r['date']; time=r['time']; typ=r['slot_type']
        try: dt.date.fromisoformat(date)
        except ValueError: errors.append(f'{label}: invalid ISO date')
        try: dt.datetime.strptime(time,'%H:%M')
        except ValueError: errors.append(f'{label}: invalid HH:MM time')
        if r['timezone']!='America/New_York': errors.append(f'{label}: wrong timezone')
        if typ not in SLOTS: errors.append(f'{label}: unknown slot_type {typ}')
        elif time != SLOT_TIMES[typ]: errors.append(f'{label}: {typ} outside current approved {SLOT_TIMES[typ]} slot')
        if not body.strip(): errors.append(f'{label}: empty body')
        if len(body)>=500: errors.append(f'{label}: {len(body)} characters (must be under 500)')
        if URL.search(body): errors.append(f'{label}: URL in parent post body')
        if 'â€”' in body: errors.append(f'{label}: em dash in body')
        if any(x in body.lower() for x in BANNED): errors.append(f'{label}: banned copy phrase')
        if r['approval'] not in {'PENDING','APPROVED','REJECTED'}: errors.append(f'{label}: invalid approval')
        if r['status'] not in STATUSES: errors.append(f'{label}: invalid status')
        for field in ['reply_status','article_reply_status']:
            if r[field] not in REPLY_STATUSES: errors.append(f'{label}: invalid {field}')
            if r[field] in {'READY','SCHEDULED','VERIFIED'} and r['approval']!='APPROVED': errors.append(f'{label}: reply execution without approval')
        for textfield,timefield,statusfield in [('reply_text','reply_due_time','reply_status'),('article_reply_text','article_reply_due_time','article_reply_status')]:
            if r[textfield].strip():
                if len(r[textfield])>=500: errors.append(f'{label}: reply must be under 500 characters')
                if 'â€”' in r[textfield]: errors.append(f'{label}: em dash in reply')
                try: dt.datetime.strptime(r[timefield],'%H:%M')
                except ValueError: errors.append(f'{label}: invalid reply time')
            elif r[statusfield] not in {'NOT_REQUIRED','BLOCKED'}:
                errors.append(f'{label}: active reply status without copy')
        if r['status'] in {'READY','SCHEDULED','VERIFIED'} and r['approval']!='APPROVED': errors.append(f'{label}: execution status without approval')
        h=hashlib.sha256(body.encode('utf8')).hexdigest()
        if h in bodies: errors.append(f'{label}: duplicate exact post body')
        bodies.add(h)
        if r['content_hash']!=h: errors.append(f'{label}: content_hash mismatch')
        if not r['post_id'].strip(): errors.append(f'{label}: blank post_id')
        if r['post_id'] in ids: errors.append(f'{label}: duplicate post_id')
        ids.add(r['post_id'])
        key=(date,time)
        if key in schedule: errors.append(f'{label}: duplicate local date/time')
        schedule.add(key)
        days[date].append(r)
        hook=r['hook_label'].strip().lower()
        if hook and hook in hooks[date]: errors.append(f'{label}: repeated named hook on {date}')
        hooks[date].add(hook)
        if typ=='OFFER':
            if time!='13:00': errors.append(f'{label}: offer outside approved 13:00 slot')
            if not r['offer_name'].strip(): errors.append(f'{label}: offer name missing')
            if not r['reply_text'].strip() or not URL.search(r['reply_text']): errors.append(f'{label}: offer reply needs approved link')
            if r['reply_due_time']!='13:00': errors.append(f'{label}: offer link reply must be due immediately at 13:00, never two hours later')
            if r['reply_status']=='NOT_REQUIRED': errors.append(f'{label}: offer reply incorrectly not required')
        else:
            if r['offer_name'].strip(): errors.append(f'{label}: offer outside offer slot')
            if r['reply_text'].strip(): errors.append(f'{label}: offer reply outside offer slot')
        if r['article_reply_text'].strip():
            if typ!='TEACH': errors.append(f'{label}: article reply outside teaching slot')
            if not URL.search(r['article_reply_text']): errors.append(f'{label}: article reply missing URL')
            if r['article_reply_status']=='NOT_REQUIRED': errors.append(f'{label}: article reply status mismatch')
        elif r['article_reply_status']!='NOT_REQUIRED': warnings.append(f'{label}: no article reply but reply status active')
        if typ=='SPOILER': warnings.append(f'{label}: human engagement availability must be confirmed')
    for day,entries in days.items():
        offers=[r for r in entries if r['slot_type']=='OFFER']
        if len(offers)>1: errors.append(f'{day}: more than one offer post')
        if len(entries)!=6: warnings.append(f'{day}: {len(entries)} rows; current documented cadence is 6/day; partial-day manifest requires editorial reconciliation')
        if sum(bool(r['article_reply_text'].strip()) for r in entries)>1: errors.append(f'{day}: >1 article replies')
    return errors,warnings

if __name__=='__main__':
    if len(sys.argv)!=2:
        print('Usage: validate_threads_manifest.py <manifest.csv>'); sys.exit(2)
    try: e,w=validate(sys.argv[1])
    except (OSError, UnicodeError) as exc: print('ERROR:',exc);sys.exit(2)
    for x in e: print('ERROR:',x)
    for x in w: print('WARNING:',x)
    print(f'QA: {len(e)} errors, {len(w)} warnings. Live posting and canon facts NOT verified.')
    sys.exit(1 if e else 0)
