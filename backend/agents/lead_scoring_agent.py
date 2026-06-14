from services.gemini_service import generate_json
from utils.json_parser import (
    clean_json_response
)
from models.lead_score import LeadScore
def score_lead(company_analysis: dict,pain_point_analysis: dict):
    prompt = f"""
You are a senior sales manager.

Evaluate the company below.

Company Analysis:
{company_analysis}

Pain Point Analysis:
{pain_point_analysis}

Determine:

1. Lead score from 0-100
2. Lead qualification
3. Top reasons

Qualification Rules:

80-100 = Hot Lead
50-79 = Warm Lead
0-49 = Cold Lead

Return ONLY valid JSON.

Schema:

{{
  "score": 0,
  "qualification": "",
  "reasons": []
}}

No markdown.
Return JSON only.
"""
    response = generate_json(prompt)
    parsed = clean_json_response(response)
    validated = LeadScore(**parsed)

    return validated.model_dump()
