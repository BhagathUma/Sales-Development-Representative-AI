from models.competitor_analysis import (
    CompetitorAnalysis
)
from services.competitor_search import (
    search_competitors
)

from services.gemini_service import (
    generate_json
)

from utils.json_parser import (
    clean_json_response
)
def generate_competitor_analysis(
    company_analysis: dict
    
):
    company_name = company_analysis.get("company_name","")
    competitor_data = search_competitors(company_name)

    prompt = f"""
    You are a senior sales strategist.

    Target Company:

    {company_analysis}

    Competitor Research:

    {competitor_data}

    Determine:

    1. Main Competitor

    2. Competitor Advantages

    3. Competitor Weaknesses

    4. Pricing Gaps

    5. Sales Wedge

    6. Recommended Pitch

    Return valid JSON.

    Schema:

    {{
    "main_competitor": "",
    "competitor_advantages": [],
    "competitor_weaknesses": [],
    "pricing_gaps": [],
    "sales_wedge": "",
    "recommended_pitch": ""
    }}

    Return JSON only.
    """
    response =generate_json(prompt)

    parsed =clean_json_response(
        response
    )

    validated =CompetitorAnalysis(
        **parsed
    )

    return validated.model_dump()
    