import logging
from api import router as api_router
from fastapi import FastAPI
from core.config import settings
from common.exceptions.middleware import setup_exception_handlers

logging.basicConfig(format=settings.logging.log_format)

main_app = FastAPI()

setup_exception_handlers(app=main_app)

main_app.include_router(api_router)
