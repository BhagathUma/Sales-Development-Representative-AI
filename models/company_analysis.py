from pydantic import BaseModel

class CompanyAnalysis(BaseModel):
    industry: str
    company_summary: str
    target_customers: list[str]
    main_services: list[str]
    business_model: str
    pain_points: list[str]
    ai_opportunities: list[str]