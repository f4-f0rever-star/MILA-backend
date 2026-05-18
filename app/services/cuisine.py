import requests
from flask import current_app

def get_meals_by_country(country: str):
    base = "https://www.themealdb.com/api/json/v1/1/filter.php"
    url = f"{base}?a={country}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Failed to fetch meals", "code": response.status_code}
    
    data = response.json()
    meals = data.get("meals") or []
    return meals