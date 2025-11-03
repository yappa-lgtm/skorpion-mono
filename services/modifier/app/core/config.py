from pydantic import BaseModel

from common.config import BaseAppSettings
from common.gunicorn import GunicornRunConfig
from common.logger import BaseLoggingConfig

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

settings = Settings()