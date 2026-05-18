import requests
from flask import current_app

def get_heritage_by_country(country: str):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/Culture_of)_{country}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"error": "Failed to fetch texts"}
    return response.json()