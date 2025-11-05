from pathlib import Path
from typing import List

from common.config import BaseAppSettings
from common.gunicorn import GunicornRunConfig
from common.logger import BaseLoggingConfig
from pydantic import BaseModel
import yaml


class Service(BaseModel):
    name: str
    host: str


class ApiV1Prefix(BaseModel):
    prefix: str = "/v1"
    healthcheck: str = "/healthcheck"


class ApiPrefix(BaseModel):
    prefix: str = "/api"
    v1: ApiV1Prefix = ApiV1Prefix()


class Settings(BaseAppSettings):
    run: GunicornRunConfig = GunicornRunConfig()
    api: ApiPrefix = ApiPrefix()
    logging: BaseLoggingConfig = BaseLoggingConfig()
    services: List[Service]


def load_settings() -> Settings:
    routes_path = Path.cwd() / "services.yml"

    with open(routes_path, "r", encoding="utf-8") as f:
        services = yaml.safe_load(f)

    return Settings(**services)


settings = load_settings()
