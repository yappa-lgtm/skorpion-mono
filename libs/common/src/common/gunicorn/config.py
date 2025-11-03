from pydantic import BaseModel


class GunicornRunConfig(BaseModel):
    host: str = "0.0.0.0"
    port: int = 8080
    workers: int = 4
    timeout: int = 3600
