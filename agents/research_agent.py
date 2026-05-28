import json
from services.gemini_service import (
    generate_response
)

def research_company(scraped_data):

    prompt = f"""
You are an expert AI sales analyst.

Analyze this company.

COMPANY TITLE:
{scraped_data['title']}

WEBSITE CONTENT:
{scraped_data['content']}

Return ONLY valid JSON.

Format:
{{
  "industry": "",
  "company_summary": "",
  "target_customers": [],
  "main_services": [],
  "business_model": "",
  "pain_points": [],
  "ai_opportunities": []
}}
"""

    response = generate_response(prompt)

    try:
        return json.loads(response)

    except:
        return {
            "raw_response": response
        }