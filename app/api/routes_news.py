from fastapi import APIRouter, Depends, Query, Request
from app.api.deps import get_current_user, rate_limiter
from app.services.news_service import get_news

router = APIRouter()

@router.get("/news")
def news(
    request: Request,
    search: str = Query(None),
    page: int = Query(1, ge=1),
    page_size: int = Query(10, ge=1, le=100),
    _: str = Depends(get_current_user),
    __: None = Depends(rate_limiter)
):
    return get_news(query=search, page=page, page_size=page_size)
