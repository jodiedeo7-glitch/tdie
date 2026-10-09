"""Resumable private customer questionnaire. No provider or publication calls."""
import argparse
import copy
import json
from pathlib import Path
import profile as state

# Preferences are deliberately separate from operator-verified capabilities.
BANK = json.loads((Path(__file__).with_name('intake-question-bank.json')).read_text())
QUESTIONS = tuple((q['id'], q['field'], q['prompt']) for q in BANK['questions'])
CHOICES = {q['id']: q['options'] for q in BANK['questions']}
MULTI_SELECT = {q['id'] for q in BANK['questions'] if q['multi']}
CATEGORY_BRANCHES = BANK['category_branches']
GROUPED = {'curation_profile', 'personal_visual_signature'}
OPERATOR_FIELDS = ('reference_assets', 'disclosure', 'connected_capabilities', 'state_location')

def no_persona(value):
    if value is False or value == 'no_persona':
        return True
    return isinstance(value, dict) and any(
        str(choice).startswith('No person:') for choice in value.get('selected', []))


def missing_questions(answers, scope='production'):
    questions = QUESTIONS[:13] if scope == 'visual_pilot' else QUESTIONS
    persona = answers.get('intake.persona_choice', {}).get('value')
    return [question_id for question_id, field, prompt in questions
            if 'intake.' + question_id not in answers
            and not (question_id == 'persona_world' and
                     no_persona(persona))]


def next_question(path):
    """Resume at the first unanswered preference, never at question one by default."""
    profile = state.load(path) if Path(path).exists() else {'answers': {}}
    answers = profile['answers']
    for question_id, field, prompt in QUESTIONS:
        if 'intake.' + question_id in answers:
            continue
        if question_id == 'persona_world':
            persona = answers.get('intake.persona_choice', {}).get('value')
            if no_persona(persona):
                continue
        return {'question_id': question_id, 'field': field, 'prompt': prompt,
                'options': CHOICES[question_id],
                'questionnaire_version': BANK['schema_version'],
                'use': next(q['use'] for q in BANK['questions'] if q['id'] == question_id),
                'category_branches': CATEGORY_BRANCHES if question_id == 'category_preferences' else None,
                'type': 'multi_select' if question_id in MULTI_SELECT else 'single_select',
                'free_text_placeholder': 'Add your specific ' + question_id.replace('_', ' '),
                'operator_rule': 'Resolve existing exact customer evidence first. Ask only if still missing. Present guided choices; custom text is optional, never an open-ended-only question.'}
    return {'result': 'PREFERENCE_INTAKE_RECORDED',
            'operator_fields_to_verify': list(OPERATOR_FIELDS),
            'live_setup': 'NOT_VERIFIED'}


def record_answer(path, customer_id, question_id, value, evidence, answered_at,
                  expected_revision, kind='customer'):
    matching = [q for q in QUESTIONS if q[0] == question_id]
    if not matching:
        raise state.Blocked('QUESTION_ID_UNKNOWN')
    if value is None or (isinstance(value, str) and not value.strip()):
        raise state.Blocked('QUESTION_UNANSWERED')
    if isinstance(value, str) and value.strip().lower() == 'no selection':
        raise state.Blocked('QUESTION_UNANSWERED')
    if isinstance(value, (dict, list)) and not value:
        raise state.Blocked('QUESTION_UNANSWERED')
    if isinstance(value, dict) and ('selected' in value or 'detail' in value):
        selected, detail = value.get('selected', []), value.get('detail', '')
        if not isinstance(selected, list) or not isinstance(detail, str):
            raise state.Blocked('FORM_ANSWER_INVALID:' + question_id)
        if not selected and not detail.strip() and not value.get('categories'):
            raise state.Blocked('QUESTION_UNANSWERED')
    question_id, field, prompt = matching[0]
    current = state.load(path) if Path(path).exists() else {'answers': {}}
    envelope = {'value': copy.deepcopy(value), 'evidence': evidence,
                'answered_at': answered_at, 'question_id': question_id,
                'question': prompt, 'questionnaire_version': BANK['schema_version'],
                'source_kind': 'new_customer_answer'}
    delta = {'intake.' + question_id: envelope}
    if field in GROUPED:
        prior = current['answers'].get(field)
        group = copy.deepcopy(prior['value']) if prior else {}
        if not isinstance(group, dict):
            raise state.Blocked('GROUPED_ANSWER_REQUIRES_EXPLICIT_MIGRATION')
        group[question_id] = copy.deepcopy(value)
        # Keep the source of every component, not just the latest group update.
        components = copy.deepcopy(prior.get('component_evidence', {})) if prior else {}
        if prior and not components:
            components['_recovered_or_prior'] = {k: copy.deepcopy(v) for k, v in prior.items() if k != 'value'}
        components[question_id] = copy.deepcopy(envelope)
        grouped = copy.deepcopy(envelope)
        grouped['value'] = group
        grouped['component_evidence'] = components
        delta[field] = grouped
    else:
        delta[field] = copy.deepcopy(envelope)
    return state.save(path, customer_id, delta, expected_revision, kind)

def import_form(path, customer_id, answer_file, expected_revision, kind='customer'):
    """Import only complete explicit answers; refuse overwriting a saved answer.

    Browser drafts are not accepted as a complete profile. Every imported answer
    uses the same revisioned save/readback path as an interview answer.
    """
    document = state.read(answer_file)
    if document.get('schema_version') != 2 or document.get('questionnaire_version') != 2:
        raise state.Blocked('QUESTIONNAIRE_VERSION_MISMATCH')
    incoming = document.get('answers')
    if not isinstance(incoming, dict):
        raise state.Blocked('ANSWERS_INVALID')
    known = {q[0] for q in QUESTIONS}
    if set(incoming) - known:
        raise state.Blocked('QUESTION_ID_UNKNOWN')
    current = state.load(path) if Path(path).exists() else {'answers': {}, 'revision': 0}
    if current['revision'] != expected_revision:
        raise state.Blocked('REVISION_CONFLICT')
    prepared = []
    categories = incoming.get('categories', {}).get('value', {}).get('selected', [])
    for question_id, field, prompt in QUESTIONS:
        if question_id not in incoming:
            continue
        answer = incoming[question_id]
        value = answer.get('value')
        if not isinstance(value, dict):
            raise state.Blocked('FORM_ANSWER_INVALID:' + question_id)
        selected, detail = value.get('selected', []), value.get('detail', '')
        if not isinstance(selected, list) or not isinstance(detail, str):
            raise state.Blocked('FORM_ANSWER_INVALID:' + question_id)
        if question_id == 'category_preferences':
            responses = value.get('categories', {})
            if not categories or any(category not in CATEGORY_BRANCHES for category in categories):
                raise state.Blocked('CATEGORY_SELECTION_INVALID')
            for category in categories:
                for item in CATEGORY_BRANCHES[category]:
                    if not responses.get(category, {}).get(item['id']):
                        raise state.Blocked('CATEGORY_BRIEF_INCOMPLETE:' + category + ':' + item['id'])
        elif not selected and not detail.strip():
            # A blank browser draft is never a recorded answer.
            continue
        if any(choice not in CHOICES[question_id] for choice in selected):
            raise state.Blocked('FORM_CHOICE_INVALID:' + question_id)
        if question_id not in MULTI_SELECT and len(selected) > 1:
            raise state.Blocked('FORM_SINGLE_CHOICE_REQUIRED:' + question_id)
        if question_id == 'generation_budget':
            attempts = value.get('max_attempts_per_role')
            if type(attempts) is not int or attempts < 1:
                raise state.Blocked('FINITE_ATTEMPT_ALLOWANCE_REQUIRED')
            if not str(value.get('period', '')).strip():
                raise state.Blocked('BUDGET_PERIOD_REQUIRED')
            if selected != ['No paid generation']:
                for limit in ('per_look_limit', 'period_limit'):
                    if type(value.get(limit)) not in (int, float) or value[limit] <= 0:
                        raise state.Blocked('FINITE_PAID_ALLOWANCE_REQUIRED:' + limit)
                if not str(value.get('unit', '')).strip():
                    raise state.Blocked('BUDGET_UNIT_REQUIRED')
        existing = current['answers'].get('intake.' + question_id)
        if existing:
            if existing['value'] != value:
                raise state.Blocked('EXPLICIT_CORRECTION_REQUIRED:' + question_id)
            continue
        if not answer.get('answered_at'):
            raise state.Blocked('ANSWER_TIMESTAMP_MISSING:' + question_id)
        prepared.append((question_id, value, answer['answered_at']))
    for question_id, value, timestamp in prepared:
        saved = record_answer(path, customer_id, question_id, value,
                              'Customer-supplied questionnaire v2 answer file: ' + str(answer_file),
                              timestamp, expected_revision, kind)
        expected_revision = saved['revision']
    return {'result': 'ANSWERS_IMPORTED_AND_READ_BACK', 'imported': len(prepared),
            'revision': expected_revision, 'missing': missing_questions(state.load(path)['answers'])
            if Path(path).exists() else [q[0] for q in QUESTIONS],
            'live_setup': 'NOT_VERIFIED'}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('next', 'answer', 'import-form'))
    parser.add_argument('--profile', required=True)
    parser.add_argument('--customer')
    parser.add_argument('--question')
    parser.add_argument('--answer-file')
    parser.add_argument('--expected-revision', type=int)
    parser.add_argument('--kind', choices=('customer', 'founder', 'fixture'), default='customer')
    args = parser.parse_args()
    try:
        if args.command == 'next':
            print(json.dumps(next_question(args.profile), ensure_ascii=False))
        elif args.command == 'import-form':
            if args.customer is None or args.answer_file is None or args.expected_revision is None:
                raise state.Blocked('ARGUMENT_MISSING')
            print(json.dumps(import_form(args.profile, args.customer, args.answer_file,
                                         args.expected_revision, args.kind)))
        else:
            for name in ('customer', 'question', 'answer_file', 'expected_revision'):
                if getattr(args, name) is None:
                    raise state.Blocked('ARGUMENT_MISSING:' + name)
            answer = state.read(args.answer_file)
            result = record_answer(args.profile, args.customer, args.question,
                                   answer['value'], answer['evidence'], answer['answered_at'],
                                   args.expected_revision, args.kind)
            print(json.dumps({'result': 'SAVED_AND_READ_BACK', 'revision': result['revision'],
                              'sha256': result['sha256'], 'next': next_question(args.profile)}))
    except (state.Blocked, OSError, KeyError, TypeError, ValueError) as error:
        parser.exit(2, 'BLOCKED: ' + str(error) + '\n')


if __name__ == '__main__':
    main()

