from fastapi import APIRouter, Depends
from fastapi_keycloak_middleware import CheckPermissions

from app.models import Report

router = APIRouter()


@router.get(
    "/reports",
    response_model=list[Report],
    dependencies=[Depends(CheckPermissions(["prothetic_user"]))],
)
def get_reports() -> list[Report]:
    reports = [Report(message="Отчет 1"), Report(message="Отчет 2")]

    return reports
