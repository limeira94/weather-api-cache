import os
import requests
import json
from dotenv import load_dotenv
from fast_weather.cache import get_cache, set_cache

load_dotenv()

api_key = os.getenv("KEY_WEATHER_API")
base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def fetch_weather(location):
    cache_key = f"weather_{location}"
    cache_data = get_cache(cache_key)
    
    if cache_data:
        print("Cache hit")
        return json.loads(cache_data.decode('utf-8'))
    
    url = f"{base_url}/{location}?unitGroup=metric&key={api_key}&contentType=json"
    response = requests.get(url)
    data = response.json()
    
    print("Cache miss")
    set_cache(cache_key, json.dumps(data), 60)
        
    return data
