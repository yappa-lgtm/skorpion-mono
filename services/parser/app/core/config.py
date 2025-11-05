import os
from common.config import BaseAppSettings
from common.gunicorn import GunicornRunConfig
from common.logger import BaseLoggingConfig
from pydantic import BaseModel


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


print(os.getcwd())

settings = Settings()
