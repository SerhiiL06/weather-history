from fastapi import Request, status
from fastapi.responses import JSONResponse

from src.infrastructure.models.base import Base


class ThirdApiUnavailable(Exception):

    def __init__(self, service_name: str) -> None:
        self.api = service_name


def unavailable(request: Request, exc: ThirdApiUnavailable):
    error_text = {"location": exc.api}
    resp = JSONResponse(
        content={"code": "503", "msg": error_text},
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
    )
    return resp
