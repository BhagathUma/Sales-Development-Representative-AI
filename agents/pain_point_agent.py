from services.gemini_service import generate_json
from utils.json_parser import (
    clean_json_response
)
from models.pain_point_analysis import (
    PainPointAnalysis
)

def analyze_pain_points(
    company_analysis: dict
    ):
    prompt = f"""
    You are a senior B2B sales consultant.

    Analyze the following company.

    Company Analysis:
    {company_analysis}

    Identify:

    1. Likely operational pain points
    2. Sales challenges
    3. Customer support challenges
    4. Automation opportunities
    5. Urgency level

    Return ONLY valid JSON.

    Schema:

    {{
        "pain_points": [],
        "opportunities": [],
        "urgency_level": ""
    }}
    Focus on realistic challenges.
    Avoid generic answers.
    Base all conclusions on the provided company profile.
    Do not include markdown.
    Do not explain anything.
    Return JSON only.
    """

    response = generate_json(prompt)
    parsed = clean_json_response(response)
    validated = PainPointAnalysis(**parsed)
    return validated.model_dump()
    