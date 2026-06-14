from pydantic import BaseModel
from typing import Optional

class FollowupRequest(BaseModel):
    followup_type: str

    company_analysis: Optional[dict] = None

    pain_points: Optional[dict] = None

    lead_score: Optional[dict] = None