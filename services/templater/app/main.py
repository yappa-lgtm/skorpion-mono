from api import router as api_router
from core.config import settings
from fastapi import FastAPI

main_app = FastAPI()

main_app.include_router(api_router, prefix=settings.api.prefix)
