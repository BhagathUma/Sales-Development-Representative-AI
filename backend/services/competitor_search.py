import os
from dotenv import load_dotenv
from tavily import TavilyClient

load_dotenv()

tavily_client = TavilyClient(
    api_key=os.getenv("TAVILY_API_KEY")
)


def search_competitors(
    company_name: str,
) -> dict:
    """
    Search for competitors, pricing information,
    and feature comparisons.
    """

    search_query = f"""
    {company_name} competitors,
    alternatives,
    pricing comparison,
    feature comparison,
    market rivals
    """

    try:

        response = tavily_client.search(
            query=search_query,
            search_depth="advanced",
            max_results=8,
        )

        results = response.get(
            "results",
            []
        )

        competitor_data = []

        for result in results:

            competitor_data.append(
                {
                    "title": result.get(
                        "title",
                        ""
                    ),
                    "url": result.get(
                        "url",
                        ""
                    ),
                    "content": result.get(
                        "content",
                        ""
                    ),
                }
            )

        return {
            "company_name": company_name,
            "research": competitor_data,
        }

    except Exception as e:

        print(
            f"Competitor search failed: {e}"
        )

        return {
            "company_name": company_name,
            "research": [],
        }   