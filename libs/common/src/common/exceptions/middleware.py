import logging
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from starlette.exceptions import HTTPException as StarletteHTTPException
from common.exceptions.api import (
    APIException,
    RouteNotFoundException,
    ValidationModelException,
)

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(APIException)
    async def api_exception_handler(request: Request, exc: APIException):
        logger.error(f"APIException: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.to_dict(),
        )

    @app.exception_handler(StarletteHTTPException)
    async def http_exception_handler(request: Request, exc: StarletteHTTPException):
        logger.error(exc)
        if exc.status_code == status.HTTP_404_NOT_FOUND:
            route_exc = RouteNotFoundException(request.url.path)
            return JSONResponse(
                status_code=route_exc.status_code,
                content=route_exc.to_dict(),
            )

        error = APIException(
            status_code=exc.status_code,
            message=str(exc.detail),
            code="http_error",
        )
        return JSONResponse(
            status_code=error.status_code,
            content=error.to_dict(),
        )

    @app.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        logger.error(exc)
        error = ValidationModelException(
            details=exc.errors(),
        )
        return JSONResponse(
            status_code=error.status_code,
            content=error.to_dict(),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception", exc_info=exc)
        error = APIException()
        return JSONResponse(
            status_code=error.status_code,
            content=error.to_dict(),
        )
