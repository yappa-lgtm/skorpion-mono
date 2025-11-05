from common.exceptions.middleware import setup_exception_handlers
from api import router as api_router
from core.config import settings
from fastapi import FastAPI

main_app = FastAPI()

setup_exception_handlers(app=main_app)

main_app.include_router(api_router, prefix=settings.api.prefix)
