import requests
import json
from app.core.config import settings
from app.cache.redis_cache import get_cached_weather, set_cached_weather
import asyncio

import requests
import json
from app.cache.redis_cache import get_cached_weather, set_cached_weather
from app.core.config import settings

async def get_weather_data(city: str, page: int, page_size: int):
    cached = await get_cached_weather(city)
    
    if cached:
        data = json.loads(cached)
    else:
        url = "https://api.openweathermap.org/data/2.5/forecast"
        params = {
            "q": city,
            "appid": settings.WEATHER_API_KEY,
            "units": "metric"
        }
        response = requests.get(url, params=params)
        if response.status_code != 200:
            return {"error": "Failed to fetch weather"}

        raw_data = response.json()

        full_data = [
            {
                "date": item["dt_txt"],
                "main": item["weather"][0]["main"],
                "temp": item["main"]["temp"]
            }
            for item in raw_data["list"]
        ]

        data = {
            "unit": "metric",
            "location": city,
            "count": len(full_data),
            "full_data": full_data
        }

        await set_cached_weather(city, json.dumps(data))

    # Pagination logic
    start = (page - 1) * page_size
    end = start + page_size
    paginated = data.get("full_data", data.get("data", []))[start:end]

    return {
        "count": data["count"],
        "unit": data["unit"],
        "location": data["location"],
        "page": page,
        "page_size": page_size,
        "data": paginated
    }