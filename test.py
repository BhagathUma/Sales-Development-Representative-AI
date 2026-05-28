from utils.web_scraper import scrape_website

data = scrape_website(
    "https://openai.com"
)

print(data)