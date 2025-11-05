from fastapi import APIRouter
from core.config import settings

from .api_v1 import router as router_api_v1
from .proxy import router as proxy_router


router = APIRouter()

router.include_router(router_api_v1, prefix=settings.api.prefix)
router.include_router(proxy_router)
