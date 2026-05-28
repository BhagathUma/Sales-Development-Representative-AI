from fastapi import FastAPI
from utils.web_scraper import scrape_website

from agents.research_agent import (
    research_company
)

from services.gemini_service import (
    generate_response
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