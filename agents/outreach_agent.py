from services.gemini_service import generate_json

from utils.json_parser import (
    clean_json_response
)
from models.outreach import Outreach

def generate_outreach(
    company_analysis: dict,
    pain_points: dict,
    lead_score: dict
):
    
    prompt = f"""
You are a top-performing enterprise SDR.

Generate personalized outreach.

Company Analysis:
{company_analysis}

Pain Point Analysis:
{pain_points}

Lead Score:
{lead_score}

Create:

1. Cold Email Subject
2. Cold Email Body
3. LinkedIn Message
4. Sales Call Opener

Requirements:

- Professional
- Personalized
- Mention company context
- Mention likely pain points
- Include clear CTA
- Reference the company's products, industry, and likely business challenges.
- Avoid generic sales language
Return ONLY valid JSON.

Schema:

{{
  "email_subject": "",
  "email_body": "",
  "linkedin_message": "",
  "call_opener": "",
  "executive_summary": ""
}}

No markdown.
Return JSON only.
"""
    response = generate_json(prompt)
    parsed = clean_json_response(response)
    validated = Outreach(**parsed)
    return validated.model_dump()