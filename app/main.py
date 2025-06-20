from fastapi import FastAPI
from app.api import routes_auth, routes_news, routes_weather
from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="DataHat Backend")

Base.metadata.create_all(bind=engine)

app.include_router(routes_auth.router, tags=["Auth"])
app.include_router(routes_news.router, tags=["News"])
app.include_router(routes_weather.router, tags=["Weather"])