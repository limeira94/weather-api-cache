# Weather API Wrapper Service with Redis Cache

## Overview

This project is a Weather API Wrapper Service built using FastAPI. It integrates with a third-party weather API to fetch current weather data for a given location. To improve performance and reduce the number of requests to the third-party API, Redis is used for caching the weather data.

## Features

- Fetch current weather data for a specified location.
- Cache weather data using Redis with a configurable expiration time.
- Automatically expire cached data after 12 hours to ensure data freshness.

## Project Structure

```
fast_weather/
├── fast_weather/
|    ├── main.py
|    ├── cache.py
|    ├── weather.py
├── .venv
├── .env
└── pyproject.toml
```


## Environment Variables

Create a `.env` file in the root directory with the following content:

**API_KEY**: Your API key for the weather API.
[weather-api](https://www.visualcrossing.com/)

```dotenv
API_KEY=your_weather_api_key
REDIS_HOST=localhost
REDIS_PORT=6379
REDIS_DB=0
```
## Clone the repository:
```
git clone <repository_url>
cd weather_api_wrapper
```

## Install dependencies:
```
poetry install
```

## Activate the virtual environment:
```
poetry shell
```

## Run the application:
```
fastapi dev fast_weather/main.py
```
