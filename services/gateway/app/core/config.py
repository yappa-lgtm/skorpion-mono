from pathlib import Path
from typing import List, Literal

import yaml
from common.config import BaseAppSettings
from common.gunicorn import GunicornRunConfig
from common.logger import BaseLoggingConfig
from pydantic import BaseModel


class ApiRoutes(BaseModel):
    path: str
    method: Literal["GET", "POST", "PUT", "PATCH", "DELETE"]
    service: str
    url: str
    rate_limit: str


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
    routes: List[ApiRoutes]

    # TODO! CHANGE ON CUSTOM APPLICATION EXCEPTIONS
    @classmethod
    def load_routes_from_yaml(cls, yaml_path: str | Path) -> List[ApiRoutes]:
        path = Path(yaml_path)

        if not path.exists():
            raise FileNotFoundError(f"Routes file not found: {yaml_path}")

        with open(path, "r", encoding="utf-8") as f:
            data = yaml.safe_load(f)

        if not isinstance(data, dict) or "routes" not in data:
            raise ValueError("YAML must contain 'routes' key")

        routes_data = data["routes"]
        if not isinstance(routes_data, list):
            raise ValueError("'routes' must be a list")

        return [ApiRoutes(**route) for route in routes_data]


def load_settings() -> Settings:
    routes = Settings.load_routes_from_yaml(
        Path.cwd() / "services" / "gateway" / "routes.yml"
    )  # TODO! FIX PATH
    return Settings(routes=routes)


settings = load_settings()
