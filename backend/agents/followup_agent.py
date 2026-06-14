from services.gemini_service import generate_json

from utils.json_parser import (
    clean_json_response
)

from models.followup_response import (
    FollowupResponse
)


def generate_followup(
    followup_type: str,
    company_analysis: dict,
    pain_points: dict,
    lead_score: dict
):

    prompt = f"""
You are a senior SDR.

Generate a follow-up email.

FOLLOWUP TYPE:
{followup_type}

COMPANY ANALYSIS:
{company_analysis}

PAIN POINTS:
{pain_points}

LEAD SCORE:
{lead_score}

Rules:

day3:
- Gentle reminder
- Short
- Professional

day7:
- Introduce additional value
- Mention a potential benefit

breakup:
- Polite and respectful final attempt
- Invite future conversation

Return ONLY valid JSON.

Schema:

{{
    "followup_type": "",
    "subject": "",
    "email_body": ""
}}

No markdown.
No explanation.
JSON only.
"""

    response = generate_json(prompt)

    parsed = clean_json_response(response)

    validated = FollowupResponse(**parsed)

    return validated.model_dump()