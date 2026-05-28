import requests

from bs4 import BeautifulSoup

def scrape_website(url: str):

    try:

        headers = {
            "User-Agent":
            "Mozilla/5.0"
        }

        response = requests.get(
            url,
            headers=headers,
            timeout=10
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        for script in soup(
            ["script", "style"]
        ):
            script.extract()

        title = (
            soup.title.string.strip()
            if soup.title
            else ""
        )

        paragraphs = soup.find_all("p")

        content = " ".join([
            p.get_text(strip=True)
            for p in paragraphs[:20]
        ])

        return {
            "title": title,
            "content": content
        }

    except Exception as e:

        return {
            "error": str(e)
        }