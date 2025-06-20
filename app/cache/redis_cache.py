import redis.asyncio as redis
from app.core.config import settings

r = redis.from_url(settings.REDIS_URL, decode_responses=True)

async def get_cached_weather(city: str):
    return await r.get(city.lower())

async def set_cached_weather(city: str, value: str, expire: int = 300):
    await r.set(city.lower(), value, ex=expire)
