from fastapi import APIRouter


from .healthcheck import router as healthcheck_router
from core.config import settings

router = APIRouter(prefix=settings.api.v1.prefix)

router.include_router(healthcheck_router, prefix=settings.api.v1.healthcheck)