import os
import requests
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("KEY_WEATHER_API")

base_url = "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"

def fetch_weather(location):
    url = f"{base_url}/{location}?unitGroup=metric&key={api_key}&contentType=json"
    response = requests.get(url)
    data = response.json()
    return data
