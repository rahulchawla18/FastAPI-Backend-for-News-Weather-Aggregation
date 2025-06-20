from fastapi import APIRouter, Query, Request, Depends
from app.api.deps import rate_limiter
from app.services.weather_service import get_weather_data

router = APIRouter()
from fastapi import APIRouter, Query, Request, Depends
from app.api.deps import rate_limiter
from app.services.weather_service import get_weather_data

router = APIRouter()

@router.get("/weather")
async def weather(
    request: Request,
    city: str = Query("Bangalore"),
    page: int = Query(1, ge=1),
    page_size: int = Query(5, ge=1, le=40),
    _: None = Depends(rate_limiter)
):
    return await get_weather_data(city=city, page=page, page_size=page_size)

