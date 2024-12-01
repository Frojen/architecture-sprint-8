from fastapi import APIRouter

from app.api.routes import reports

api_router = APIRouter()
api_router.include_router(reports.router, tags=["reports"])
