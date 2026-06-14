from services.gemini_service import generate_json

from utils.json_parser import clean_json_response

from models.tone_outreach import ToneOutreach


ALLOWED_TONES = [
    "professional",
    "executive",
    "friendly",
    "consultative",
    "challenger",
]


def rewrite_tone(
    tone: str,
    company_analysis: dict,
    pain_points: dict,
    lead_score: dict,
):
    """
    Regenerates outreach content using a different sales tone.

    Returns:
    {
        "tone": "...",
        "email_subject": "...",
        "email_body": "...",
        "linkedin_message": "..."
    }
    """

    tone = tone.lower().strip()

    if tone not in ALLOWED_TONES:
        raise ValueError(
            f"Invalid tone. Must be one of: {ALLOWED_TONES}"
        )

    prompt = f"""
You are an elite B2B Sales Development Representative.

Your task is to rewrite outreach messaging
using the specified tone.

=========================
TARGET TONE
=========================

{tone}

=========================
COMPANY ANALYSIS
=========================

{company_analysis}

=========================
PAIN POINT ANALYSIS
=========================

{pain_points}

=========================
LEAD SCORE
=========================

{lead_score}

=========================
TONE GUIDELINES
=========================

Professional:
- Balanced and business-focused
- Suitable for most prospects

Executive:
- Short
- Strategic
- ROI-focused
- Senior leadership audience

Friendly:
- Conversational
- Warm
- Easy to read

Consultative:
- Advisor mindset
- Focus on solving business problems
- Educational

Challenger:
- Thought-provoking
- Challenge assumptions
- Highlight missed opportunities

=========================
OUTPUT REQUIREMENTS
=========================

Generate:

1. Email Subject
2. Email Body
3. LinkedIn Message

Requirements:

- Personalized
- Mention company context
- Mention likely pain points
- Include a clear call-to-action
- Avoid generic sales language
- Keep LinkedIn message under 300 characters

Return ONLY valid JSON.

Schema:

{{
    "tone": "{tone}",
    "email_subject": "",
    "email_body": "",
    "linkedin_message": ""
}}

Do NOT return markdown.
Do NOT explain anything.
Return JSON only.
"""

    response = generate_json(prompt)

    parsed = clean_json_response(
        response
    )

    validated = ToneOutreach(
        **parsed
    )

    return validated.model_dump()