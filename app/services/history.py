import requests
from requests.exceptions import ReadTimeout, ConnectionError

def get_history(culture_id):
    country = culture_id.strip().replace(" ", "_").title()

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/History_of_{country}"
    
    headers = {
        "User-Agent": "MILA-Backend/1.0"
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=5)
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "title": data.get("title", f"History of {country}"),
                "summary": data.get("extract", "Historical information unavailable."),
                "source_url": data.get("content_urls", {}).get("desktop", {}).get("page")
            }

        elif response.status_code == 404:
            fallback_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{country}"
            fallback_resp = requests.get(fallback_url, headers=headers, timeout=5)
            
            if fallback_resp.status_code == 200:
                data = fallback_resp.json()
                return {
                    "status": "partial_match",
                    "title": data.get("title", country),
                    "summary": data.get("extract", "Historical information unavailable."),
                    "source_url": data.get("content_urls", {}).get("desktop", {}).get("page")
                }
                
    except (ReadTimeout, ConnectionError) as e:
        print(f"Network log -> History API timeout/error for {country}: {e}")
    except Exception as e:
        print(f"Unexpected processing error in history service: {e}")

    return {
        "status": "error",
        "title": f"History of {country.replace('_', ' ')}",
        "summary": "The history timeline database for this region is currently offline.",
        "source_url": None
    }