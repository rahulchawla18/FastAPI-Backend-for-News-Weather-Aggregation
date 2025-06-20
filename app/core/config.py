import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "DataHat Backend"
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "supersecret")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30
    REDIS_URL = os.getenv("REDIS_URL", "redis://localhost:6379")
    NEWS_API_KEY = os.getenv("NEWS_API_KEY")
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")

settings = Settings()
