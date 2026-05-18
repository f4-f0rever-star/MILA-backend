import requests

def get_art_by_country(country: str):
    url = "https://api.artic.edu/api/v1/artworks/search"
    params = {
        "q": country,
        "limit": 10
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return {"error": "Art API failed"}

    return response.json()