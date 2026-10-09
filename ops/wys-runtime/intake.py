"""Resumable private customer questionnaire. No provider or publication calls."""
import argparse
import copy
import json
from pathlib import Path
import profile as state

# Preferences are deliberately separate from operator-verified capabilities.
QUESTIONS = (
    ('business_direction', 'curation_profile', 'What kind of Amazon finds business are you building, and who do you want to reach?'),
    ('categories', 'product_categories', 'Which product categories do you want to cover?'),
    ('selection_route', 'curation_profile', 'Would you rather supply detailed product examples, share vibe pictures, or start with a short description?'),
    ('aesthetic', 'personal_visual_signature', 'Describe the overall look you want, including how simple or detailed it should feel.'),
    ('palette_materials', 'personal_visual_signature', 'Which colors, materials and textures should appear, and which should be avoided?'),
    ('personal_details', 'personal_visual_signature', 'What interests, places or signature details should make these images feel like your brand?'),
    ('visual_exclusions', 'personal_visual_signature', 'What must never appear in your images?'),
    ('category_preferences', 'curation_profile', 'For your selected categories, what styles, uses, seasons or occasions should guide the products?'),
    ('product_exclusions', 'curation_profile', 'Are there product types, materials, brands or features you want excluded?'),
    ('shopping_price', 'curation_profile', 'What price range or value priorities apply to the selected categories?'),
    ('persona_choice', 'persona', 'Do you want an authorized AI persona appearing in lifestyle images, or the no-persona path?'),
    ('persona_world', 'personal_visual_signature', 'If using a persona, which real-life settings and activities fit your brand?'),
    ('voice', 'curation_profile', 'How should your writing sound, and what wording should it avoid?'),
    ('amazon_path', 'amazon_path', 'Are you an approved Influencer with a storefront, Associates-only, or still setting up?'),
    ('destinations', 'destinations', 'Which owned storefront, list or website should the content send shoppers to?'),
    ('channels', 'channels', 'Which channels do you want included?'),
    ('execution_mode', 'execution_mode', 'Which parts should the agent handle and which parts do you prefer to do manually?'),
    ('provider_choice', 'provider_model', 'Which image provider do you want to use? The operator will verify its exact model and supported execution path.'),
    ('cadence', 'cadence', 'How many looks do you want, and on which days?'),
    ('timezone', 'timezone', 'Which timezone should govern the schedule?'),
    ('generation_budget', 'budget', 'What finite generation budget and retry allowance do you authorize?'),
)
CHOICES = {'business_direction': ['Home and decor shoppers', 'Fashion and accessories shoppers', 'Mixed lifestyle shoppers'], 'categories': ['Clothing and accessories', 'Home, dorm and car', 'Beauty and perfume', 'Books and gifts'], 'selection_route': ['Detailed product examples', 'Vibe/reference images', 'Quick start description'], 'aesthetic': ['Simple and understated', 'Layered and detailed', 'Playful and maximalist'], 'palette_materials': ['Soft colors', 'Bold colors', 'Neutrals', 'Mixed colors'], 'personal_details': ['Home and family', 'Hobbies and interests', 'Places and activities', 'No recurring personal details'], 'visual_exclusions': ['People', 'Decorative props', 'Lettering in photos', 'No additional exclusions'], 'category_preferences': ['Everyday use', 'Special occasions', 'Seasonal or holiday', 'Mixed uses'], 'product_exclusions': ['No additional exclusions', 'Avoid selected materials', 'Avoid selected brands', 'Avoid selected product types'], 'shopping_price': ['Mostly under $25', 'Mostly under $50', 'Mostly under $100', 'Mixed prices based on value'], 'persona_choice': ['Use an authorized persona', 'no_persona'], 'persona_world': ['Home and garden', 'Work or school', 'Outings and activities', 'Mixed settings'], 'voice': ['Friendly and conversational', 'Direct and practical', 'Playful and expressive'], 'amazon_path': ['Approved Influencer storefront', 'Associates-only', 'Still setting up'], 'destinations': ['Amazon storefront or Idea Lists', 'My own website', 'Both'], 'channels': ['Pinterest', 'Instagram', 'Blog/website'], 'execution_mode': ['Agent handles supported steps', 'I perform steps manually', 'Mixed responsibilities'], 'provider_choice': ['Native in-chat generation', 'Higgsfield', 'Another provider I use'], 'cadence': ['3 looks per week', '4 looks per week', '5 looks per week', '6–7 looks per week'], 'timezone': ['America/New_York', 'America/Chicago', 'America/Denver', 'America/Los_Angeles'], 'generation_budget': ['Choose a per-look ceiling', 'Choose a weekly ceiling', 'Choose both ceilings']}
MULTI_SELECT = {'categories', 'category_preferences', 'channels', 'personal_details', 'product_exclusions', 'persona_world', 'visual_exclusions'}
GROUPED = {'curation_profile', 'personal_visual_signature'}
OPERATOR_FIELDS = ('reference_assets', 'disclosure', 'connected_capabilities', 'state_location')


def missing_questions(answers, scope='production'):
    questions = QUESTIONS[:13] if scope == 'visual_pilot' else QUESTIONS
    persona = answers.get('intake.persona_choice', {}).get('value')
    return [question_id for question_id, field, prompt in questions
            if 'intake.' + question_id not in answers
            and not (question_id == 'persona_world' and
                     (persona is False or persona == 'no_persona'))]


def next_question(path):
    """Resume at the first unanswered preference, never at question one by default."""
    profile = state.load(path) if Path(path).exists() else {'answers': {}}
    answers = profile['answers']
    for question_id, field, prompt in QUESTIONS:
        if 'intake.' + question_id in answers:
            continue
        if question_id == 'persona_world':
            persona = answers.get('intake.persona_choice', {}).get('value')
            if persona is False or persona == 'no_persona':
                continue
        return {'question_id': question_id, 'field': field, 'prompt': prompt,
                'options': CHOICES[question_id],
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
    question_id, field, prompt = matching[0]
    current = state.load(path) if Path(path).exists() else {'answers': {}}
    envelope = {'value': copy.deepcopy(value), 'evidence': evidence,
                'answered_at': answered_at, 'question_id': question_id,
                'question': prompt, 'source_kind': 'new_customer_answer'}
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


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command', choices=('next', 'answer'))
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
