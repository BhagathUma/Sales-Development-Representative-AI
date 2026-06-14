from pydantic import BaseModel

class CompetitorAnalysis(BaseModel):

    main_competitor: str

    competitor_advantages: list[str]

    competitor_weaknesses: list[str]

    pricing_gaps: list[str]

    sales_wedge: str

    recommended_pitch: str