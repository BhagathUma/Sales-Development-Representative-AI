from pydantic import BaseModel

class PainPointAnalysis(BaseModel):
    pain_points: list[str]
    opportunities: list[str]
    urgency_level: str