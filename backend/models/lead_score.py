from pydantic import BaseModel

class LeadScore(BaseModel):
    score: int
    qualification: str
    reasons: list[str]