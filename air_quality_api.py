import requests

def get_aqi(city):
    try:
        url = f"https://api.openaq.org/v2/latest?city={city}"
        response = requests.get(url, timeout=10).json()

        # Safely check if results exist
        if "results" not in response:
            return None

        for result in response["results"]:
            for measure in result.get("measurements", []):
                if measure.get("parameter") == "pm25":
                    return measure.get("value")

        return None

    except Exception:
        return None
