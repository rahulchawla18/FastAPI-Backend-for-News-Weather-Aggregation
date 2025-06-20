# News & Weather Aggregator API - FastAPI Project

A production-ready backend API built with **FastAPI**, integrating **NewsAPI** and **OpenWeatherMap** to provide real-time headlines and 5-day weather forecasts. Features include JWT-based authentication, Redis caching, pagination, rate limiting, Docker support, and unit tests with Pytest.

---

## Features

- JWT-based Signup, Login, Logout, and Refresh Token
- Fetch top and trending news articles (with search and pagination)
- Weather forecasts using OpenWeatherMap (cached with Redis)
- Pagination for both news and weather
- Redis-based caching for performance
- Rate limiting per IP to prevent abuse
- Unit tests with Pytest
- Docker & Docker Compose setup

---

## Technologies

- FastAPI
- SQLite (via SQLAlchemy)
- Redis
- Uvicorn
- PyJWT (`python-jose`)
- Docker, Docker Compose
- Pytest

---

## Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/your-username/news-weather-api.git
cd news-weather-api
```

### 2. Create your .env file

JWT_SECRET_KEY=your_super_secret
NEWS_API_KEY=your_newsapi_key
WEATHER_API_KEY=your_openweather_key
REDIS_URL=redis://redis:6379

### 3. Get your free API keys from:

1. https://newsapi.org
2. https://openweathermap.org

### 4. Run using Docker

1. docker-compose up --build

### 4. The API will be available at:

1. http://localhost:8000
2. Swagger Docs: http://localhost:8000/docs

### 5. Authentication

1. All protected endpoints require the Authorization header:
2. Authorization: Bearer <access_token>
3. Use /login to get your token.

### 6. API Endpoints

Method      Endpoint      Description                           Auth
POST        /signup       Register a new user	                No
POST	    /login	      Authenticate and get JWT	            No
POST	    /refresh	  Get new access token from refresh	    No
POST	    /logout	      Invalidate access token	            Yes
GET	        /news	      Fetch news articles (searchable)	    Yes
GET	        /weather	  Get weather forecast by city	        No

### 7. To build and run manually:

1. docker build -t fastapi-news-weather .
2. docker run -p 8000:8000 --env-file .env fastapi-news-weather
3. Use docker-compose for Redis integration

### 8. Swagger export

[text](../openapi.json)