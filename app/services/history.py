import requests
from requests.exceptions import ReadTimeout, ConnectionError

def get_history(culture_id):
    """
    Fetches an authentic historical summary text for a given country.
    Replaces the flaky Gutendex API with the Wikimedia REST API.
    """
    # Format string (e.g., "kenya" -> "Kenya", "south_africa" -> "South_Africa")
    formatted_country = culture_id.strip().replace(" ", "_").title()
    
    # Target the dedicated history summary page first
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/History_of_{formatted_country}"
    
    headers = {
        "User-Agent": "MILA-Backend/1.0 (MoringaSchool Student Project; contact: student@moringaschool.com)"
    }
    
    try:
        # 5 seconds is plenty for Wikipedia's edge network CDN
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            return {
                "status": "success",
                "title": data.get("title", f"History of {formatted_country}"),
                "summary": data.get("extract", "Historical information unavailable."),
                "source_url": data.get("content_urls", {}).get("desktop", {}).get("page")
            }
            
        # Fallback: If "History_of_Country" doesn't exist, read the main country page summary
        elif response.status_code == 404:
            fallback_url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{formatted_country}"
            fallback_resp = requests.get(fallback_url, headers=headers, timeout=5)
            
            if fallback_resp.status_code == 200:
                data = fallback_resp.json()
                return {
                    "status": "partial_match",
                    "title": data.get("title", formatted_country),
                    "summary": data.get("extract", "Historical information unavailable."),
                    "source_url": data.get("content_urls", {}).get("desktop", {}).get("page")
                }
                
    except (ReadTimeout, ConnectionError) as e:
        print(f"Network log -> History API timeout/error for {formatted_country}: {e}")
    except Exception as e:
        print(f"Unexpected processing error in history service: {e}")

    # Standard fallback dictionary to keep your response body uniform on failure
    return {
        "status": "error",
        "title": f"History of {formatted_country.replace('_', ' ')}",
        "summary": "The history timeline database for this region is currently offline.",
        "source_url": None
    }