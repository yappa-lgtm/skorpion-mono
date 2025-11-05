from api import router as api_router
from fastapi import FastAPI
from common.exceptions.middleware import setup_exception_handlers

main_app = FastAPI()

setup_exception_handlers(app=main_app)

main_app.include_router(api_router)
