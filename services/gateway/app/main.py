from api import router as api_router
from fastapi import FastAPI

main_app = FastAPI()

main_app.include_router(api_router)
