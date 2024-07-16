from fastapi import FastAPI, HTTPException
from fast_weather.weather import fetch_weather 


app = FastAPI()

@app.get("/weather/{location}")
async def get_weather(location: str):
    try:
        data = fetch_weather(location)
        return data
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
