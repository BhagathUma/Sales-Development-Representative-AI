import json
# from services.gemini_service import (
#     generate_response
# )
from services.gemini_service import generate_json
from utils.json_parser import (
    clean_json_response
)
from models.company_analysis import (
    CompanyAnalysis
)
def research_company(scraped_data):

    prompt = f"""
You are an expert B2B sales analyst.

Analyze the company below.

TITLE:
{scraped_data['title']}

CONTENT:
{scraped_data['content']}

Return ONLY valid JSON.

Schema:

{{
  "industry": "",
  "company_summary": "",
  "target_customers": [],
  "main_services": [],
  "business_model": "",
  "pain_points": [],
  "ai_opportunities": []
}}

Do not include markdown.
Do not explain anything.
Return JSON only.
"""

    response = generate_json(prompt)

    try:
        parsed_response = clean_json_response(response)

        validated = CompanyAnalysis(**parsed_response)

        return validated.model_dump()

    except:
        return {
            "raw_response": response
        }