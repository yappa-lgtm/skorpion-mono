from pydantic_settings import BaseSettings, SettingsConfigDict
from typing import Literal

class BaseAppSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=(".env.template", ".env"),
        case_sensitive=False,
        env_nested_delimiter="__",
        env_prefix="APP_CONFIG__",
    )
    env: Literal["dev", "prod"] = "dev" 
