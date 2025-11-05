import logging


from fastapi import APIRouter, Request
from fastapi.responses import JSONResponse
import httpx
from core.config import settings
from core.exceptions import ServiceNotFoundException, ServiceUnavailableException

logger = logging.getLogger(__name__)

router = APIRouter()


async def forward_request(
    service_name: str, service_url: str, method: str, path: str, body=None, headers=None
):
    try:
        async with httpx.AsyncClient(follow_redirects=True, timeout=5) as client:
            url = f"{service_url}{path}"
            response = await client.request(method, url, json=body, headers=headers)
            return response
    except (httpx.ConnectError, httpx.ConnectTimeout, httpx.ReadTimeout):
        raise ServiceUnavailableException(service_name=service_name)


@router.api_route(
    "/{service}/{path:path}", methods=["GET", "POST", "PUT", "DELETE", "PATCH"]
)
async def gateway(service: str, path: str, request: Request):
    service_obj = next((s for s in settings.services if s.name == service), None)

    if not service_obj:
        raise ServiceNotFoundException(service_name=service)

    body = await request.json() if request.method in ["POST", "PUT", "PATCH"] else None
    headers = dict(request.headers)

    service_url = service_obj.host

    response = await forward_request(
        service, service_url, request.method, f"/{path}", body, headers
    )

    return JSONResponse(status_code=response.status_code, content=response.json())
