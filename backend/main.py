from fastapi import FastAPI
from utils.web_scraper import scrape_website
from fastapi.middleware.cors import CORSMiddleware
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel      

from agents.competitor_agent import (
    generate_competitor_analysis
)

from agents.research_agent import (
    research_company
)

from services.gemini_service import (
    generate_response
)

from agents.pain_point_agent import (
    analyze_pain_points
)

from agents.lead_scoring_agent import (
    score_lead
)

from agents.outreach_agent import (
    generate_outreach
)
from workflows.sdr_workflow import (
    run_sdr_workflow
)

from agents.tone_rewriter_agent import (
    rewrite_tone
)

from models.followup_request import (
    FollowupRequest
)

from agents.followup_agent import (
    generate_followup
)

from fastapi.responses import Response

from services.pdf_generator import (
    generate_sales_report
)

app = FastAPI()
router = APIRouter()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "AI SDR Backend Running"
    }

@app.get("/test-gemini")
def test_gemini():

    response = generate_response(
        "Explain SaaS startups in one sentence."
    )

    return {
        "response": response
    }

@app.get("/scrape")
def scrape(url: str):

    data = scrape_website(url)

    return data


@app.get("/analyze-company")
def analyze_company(url: str):

    scraped_data = scrape_website(url)

    analysis = research_company(
        scraped_data
    )

    return {
        "website_data": scraped_data,
        "analysis": analysis
    }

@app.get("/pain-points")
def pain_points(url: str):

    scraped_data = scrape_website(url)

    company_analysis = research_company(
        scraped_data
    )

    result = analyze_pain_points(
        company_analysis
    )

    return result

@app.get("/lead-score")
def lead_score(url: str):

    scraped_data = scrape_website(url)

    company_analysis = research_company(
        scraped_data
    )

    pain_points = analyze_pain_points(
        company_analysis
    )

    result = score_lead(
        company_analysis,
        pain_points
    )

    return result


@app.get("/outreach")
def outreach(url: str):

    scraped_data = scrape_website(url)

    company_analysis = research_company(
        scraped_data
    )

    pain_points = analyze_pain_points(
        company_analysis
    )

    lead_score = score_lead(
        company_analysis,
        pain_points
    )

    result = generate_outreach(
        company_analysis,
        pain_points,
        lead_score
    )

    return result


@app.get("/analyze-lead")
def analyze_lead(url: str):

    result = run_sdr_workflow(
        url
    )

    return result


class ToneRequest(BaseModel):
    tone: str
    company_analysis: dict
    pain_points: dict
    lead_score: dict


@app.post("/rewrite-tone")
def rewrite_tone_endpoint(
    request: ToneRequest
):
    return rewrite_tone(
        tone=request.tone,
        company_analysis=request.company_analysis,
        pain_points=request.pain_points,
        lead_score=request.lead_score,
    )


@app.post("/followup")
def create_followup(
    request: FollowupRequest
):

    valid_types = [
        "day3",
        "day7",
        "breakup"
    ]

    if (
        request.followup_type
        not in valid_types
    ):
        raise HTTPException(
            status_code=400,
            detail="Invalid followup type"
        )

    result = generate_followup(
        followup_type=request.followup_type,
        company_analysis=request.company_analysis,
        pain_points=request.pain_points,
        lead_score=request.lead_score
    )

    return result


@app.post(
    "/competitor-analysis"
)
def competitor_analysis(
    payload: dict
):

    return generate_competitor_analysis(
        payload[
            "company_analysis"
        ]
    )


@app.post("/export-report")
def export_report(
    payload: dict
):

    pdf = generate_sales_report(
        payload
    )

    return Response(
        content=pdf,
        media_type="application/pdf",
        headers={
            "Content-Disposition":
            "attachment; filename=Sales_Intelligence_Report.pdf"
        }
    )