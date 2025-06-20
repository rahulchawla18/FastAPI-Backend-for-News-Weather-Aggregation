import requests
from app.core.config import settings

def get_news(query=None, page=1, page_size=10):
    url = "https://newsapi.org/v2/everything"
    params = {
        "apiKey": settings.NEWS_API_KEY,
        "q": query or "india",
        "language": "en",
        "sortBy": "publishedAt",
        "page": page,
        "pageSize": page_size
    }
    return requests.get(url, params=params).json()
