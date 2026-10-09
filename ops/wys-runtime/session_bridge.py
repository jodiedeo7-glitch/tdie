"""Read-only runtime view of the customer plugin's authoritative session file."""
import copy
from datetime import datetime
import json
import math
from pathlib import Path
from zoneinfo import ZoneInfo

BANK = json.loads(Path(__file__).with_name('intake-question-bank.json').read_text())
QUESTIONS = {q['id']: q for q in BANK['questions']}
GROUPED = {'curation_profile', 'personal_visual_signature'}


def compile_session(session):
    # profile.load verifies the raw file hash before this conversion. This view
    # retains that hash: a later edit must rebuild every prepared input.
    from profile import Blocked
    if session.get('questionnaire_version') != BANK['schema_version']:
        raise Blocked('SESSION_QUESTIONNAIRE_VERSION_MISMATCH')
    if not isinstance(session.get('customer_id'), str) or not session['customer_id'].strip():
        raise Blocked('SESSION_CUSTOMER_REQUIRED')
    if type(session.get('revision')) is not int or session['revision'] < 0:
        raise Blocked('SESSION_REVISION_INVALID')
    answers = session.get('answers')
    if not isinstance(answers, dict) or set(answers) - set(QUESTIONS):
        raise Blocked('SESSION_ANSWERS_INVALID')

    def guided(value, options, multi=True):
        if not isinstance(value, dict):
            raise Blocked('SESSION_GUIDED_ANSWER_REQUIRED')
        selected, detail = value.get('selected', []), value.get('detail', '')
        if (not isinstance(selected, list) or not all(isinstance(x, str) for x in selected)
                or len(set(selected)) != len(selected) or any(x not in options for x in selected)
                or (not multi and len(selected) > 1)):
            raise Blocked('SESSION_CHOICE_INVALID')
        if not isinstance(detail, str) or (not selected and not detail.strip()):
            raise Blocked('SESSION_QUESTION_UNANSWERED')
        return selected, detail

    compiled = {}
    for qid, original in answers.items():
        if not isinstance(original, dict) or 'value' not in original:
            raise Blocked('SESSION_ANSWER_ENVELOPE_REQUIRED')
        if not isinstance(original.get('evidence'), str) or not original['evidence'].strip():
            raise Blocked('SESSION_SOURCE_EVIDENCE_REQUIRED')
        recovered = original.get('source_kind') == 'recovered_direct_instruction'
        if recovered and original.get('answered_at') is not None:
            raise Blocked('SESSION_ORIGINAL_ANSWER_TIME_UNKNOWN')
        try:
            stamp = original.get('recorded_at' if recovered else 'answered_at')
            if datetime.fromisoformat(stamp).tzinfo is None:
                raise ValueError()
        except (TypeError, ValueError) as error:
            raise Blocked('SESSION_TIMESTAMP_INVALID') from error
        question = QUESTIONS[qid]
        value = original['value']
        if qid == 'category_preferences':
            categories = answers.get('categories', {}).get('value', {}).get('selected', [])
            briefs = value.get('categories') if isinstance(value, dict) else None
            if not categories or not isinstance(briefs, dict) or set(briefs) != set(categories):
                raise Blocked('SESSION_CATEGORY_BRANCHES_REQUIRED')
            for category in categories:
                if category not in BANK['category_branches'] or not isinstance(briefs[category], dict):
                    raise Blocked('SESSION_CATEGORY_INVALID')
                for branch in BANK['category_branches'][category]:
                    guided(briefs[category].get(branch['id']), branch['options'])
        else:
            selected, detail = guided(value, question['options'], question['multi'])
            if qid == 'categories' and not selected:
                raise Blocked('SESSION_CATEGORY_SELECTION_REQUIRED')
            if qid == 'timezone':
                ZoneInfo(detail.strip() if not selected or selected == ['Another timezone'] else selected[0])
            if qid == 'generation_budget':
                if (len(selected) != 1 or type(value.get('max_attempts_per_role')) is not int
                        or value['max_attempts_per_role'] < 1
                        or not isinstance(value.get('period'), str) or not value['period'].strip()):
                    raise Blocked('SESSION_FINITE_BUDGET_REQUIRED')
                if selected != ['No paid generation']:
                    for key in ('per_look_limit', 'period_limit'):
                        number = value.get(key)
                        if type(number) not in (int, float) or not math.isfinite(number) or number <= 0:
                            raise Blocked('SESSION_FINITE_PAID_LIMIT_REQUIRED')
                    if not isinstance(value.get('unit'), str) or not value['unit'].strip():
                        raise Blocked('SESSION_BUDGET_UNIT_REQUIRED')
        envelope = copy.deepcopy(original)
        envelope.update(question_id=qid, question=question['prompt'],
                        questionnaire_version=BANK['schema_version'])
        compiled['intake.' + qid] = envelope
        field = question['field']
        if field in GROUPED:
            group = compiled.setdefault(field, {'value': {}, 'component_evidence': {}})
            group['value'][qid] = copy.deepcopy(value)
            group['component_evidence'][qid] = copy.deepcopy(envelope)
        else:
            compiled[field] = copy.deepcopy(envelope)
    return {'schema': 1, 'kind': 'customer', 'customer_id': session['customer_id'],
            'revision': session['revision'], 'sha256': session['sha256'],
            'answers': compiled, 'history': copy.deepcopy(session.get('history', [])),
            'source_format': 'customer_plugin_session_read_only',
            'source_events': copy.deepcopy(session.get('events', []))}
