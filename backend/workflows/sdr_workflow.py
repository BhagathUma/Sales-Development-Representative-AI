from utils.web_scraper import scrape_website

from agents.research_agent import (
    research_company
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


from langgraph.graph import (
    StateGraph,
    START,
    END
)


from typing import TypedDict

class SDRState(TypedDict):
    url: str

    company_analysis: dict

    pain_points: dict

    lead_score: dict

    outreach: dict



def research_node(
    state: SDRState
):

    scraped_data = scrape_website(
        state["url"]
    )

    analysis = research_company(
        scraped_data
    )

    return {
        "company_analysis": analysis
    }


def pain_point_node(
    state: SDRState
):

    result = analyze_pain_points(
        state["company_analysis"]
    )

    return {
        "pain_points": result
    }

def lead_score_node(
    state: SDRState
):

    result = score_lead(
        state["company_analysis"],
        state["pain_points"]
    )

    return {
        "lead_score": result
    }

def outreach_node(
    state: SDRState
):

    result = generate_outreach(
        state["company_analysis"],
        state["pain_points"],
        state["lead_score"]
    )

    return {
        "outreach": result
    }


graph = StateGraph(
    SDRState
)

graph.add_node(
    "research",
    research_node
)

graph.add_node(
    "pain_points",
    pain_point_node
)

graph.add_node(
    "lead_score",
    lead_score_node
)

graph.add_node(
    "outreach",
    outreach_node
)

graph.add_edge(
    START,
    "research"
)

graph.add_edge(
    "research",
    "pain_points"
)

graph.add_edge(
    "pain_points",
    "lead_score"
)

graph.add_edge(
    "lead_score",
    "outreach"
)

graph.add_edge(
    "outreach",
    END
)

sdr_workflow = graph.compile()


def run_sdr_workflow(
    url: str
):

    result = sdr_workflow.invoke(
        {
            "url": url
        }
    )

    return result   


