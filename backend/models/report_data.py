from pydantic import BaseModel

class ReportData(BaseModel):
    company_analysis: dict
    pain_points: dict
    lead_score: dict
    outreach: dict

    competitor_analysis: dict | None = None

    followups: dict | None = None