from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from common.exceptions.api import APIException
import logging

logger = logging.getLogger(__name__)


def setup_exception_handlers(app: FastAPI):
    @app.exception_handler(APIException)
    async def api_exception_handler(request: Request, exc: APIException):
        logger.error(f"APIException: {exc.message}")
        return JSONResponse(
            status_code=exc.status_code,
            content=exc.to_dict(),
        )

    @app.exception_handler(Exception)
    async def unhandled_exception_handler(request: Request, exc: Exception):
        logger.exception("Unhandled exception", exc_info=exc)
        error = APIException()
        return JSONResponse(
            status_code=error.status_code,
            content=error.to_dict(),
        )
