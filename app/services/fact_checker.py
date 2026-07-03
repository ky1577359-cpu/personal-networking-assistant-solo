import requests
from urllib.parse import quote
from app.config import FACT_CHECK_API


def fact_check(query: str) -> str:
    try:
        url = f"{FACT_CHECK_API}/{quote(query)}"

        response = requests.get(
            url,
            headers={"User-Agent": "PersonalNetworkingAssistant/1.0"},
            timeout=10
        )

        print("URL:", url)
        print("Status:", response.status_code)
        print("Response:", response.text[:300])

        if response.status_code != 200:
            return f"HTTP Error {response.status_code}"

        data = response.json()
        return data.get("extract", "No summary found.")

    except Exception as e:
        return f"Fact-checking failed: {e}"