# import json
# # from services.gemini_service import (
# #     generate_response
# # )
# from utils.json_parser import (
#     clean_json_response
# )
# from models.company_analysis import (
#     CompanyAnalysis
# )


# # from utils.web_scraper import scrape_website

# # data = scrape_website(
# #     "https://openai.com"
# # )

# # print(data)

# test_data = {
#     "industry": "SaaS",
#     "company_summary": "Company",
#     "target_customers": [],
#     "main_services": [],
#     "business_model": "Subscription",
#     "pain_points": [],
#     "ai_opportunities": []
# }

# analysis = CompanyAnalysis(
#     **test_data
# )

# print(analysis)

# from agents.pain_point_agent import (
#     analyze_pain_points
# )

# company = {
#     "industry": "SaaS",
#     "company_summary": "CRM platform",
#     "main_services": [
#         "CRM",
#         "Marketing Automation"
#     ]
# }

# result = analyze_pain_points(
#     company
# )

# print(result)

# from agents.lead_scoring_agent import (
#     score_lead
# )

# company_analysis = {
#     "industry": "SaaS",
#     "business_model": "Subscription"
# }

# pain_points = {
#     "pain_points": [
#         "Scaling support",
#         "Manual lead qualification"
#     ]
# }

# result = score_lead(
#     company_analysis,
#     pain_points
# )

# print(result)


from agents.outreach_agent import (
    generate_outreach
)

company_analysis = {
    "industry": "SaaS",
    "company_summary": "CRM platform"
}

pain_points = {
    "pain_points": [
        "Manual lead qualification"
    ]
}

lead_score = {
    "score": 89,
    "qualification": "Hot Lead"
}

result = generate_outreach(
    company_analysis,
    pain_points,
    lead_score
)

print(result)