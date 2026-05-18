import requests

def get_countries(country_code: str):
    url = f"https://restcountries.com/v3.1/name/{country_code}"
    response = requests.get(url)
    if response.status_code != 200:
        return {"error": "Country not found"}
    
    country = response.json()
    if isinstance(country, list):
        country = country[0]
    return{
        "name": country.get("name", {}).get("common"),
        "capital": country.get("capital", [None])[0],
        "region": country.get("region"),
        "subregion": country.get("subregion"),
        "languages": country.get("languages", {}),
        "currencies": country.get("currencies", {}),
        "flag": country.get("flags", {}).get("png")
    }