from pydantic import BaseModel

class FollowupRequest(BaseModel):
    followup_type: str

    company_analysis: dict

    pain_points: dict

    lead_score: dict