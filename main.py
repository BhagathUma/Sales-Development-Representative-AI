from fastapi import FastAPI
from utils.web_scraper import scrape_website

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

app = FastAPI()

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