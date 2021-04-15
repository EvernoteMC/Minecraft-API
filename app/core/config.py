import logging
import sys

from pydantic import BaseSettings, RedisDsn



class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    version: str = "1.0.0"
    debug: bool = True
    project_name: str = "Minecraft API"
    openapi_url: str = "/api/v1/openapi.json"
    docs_url: str = "/api/v1/docs"
    redoc_url: str = "/api/v1/redocs"
    description: str = "This is the API developed by the [Obsidion-dev](https://github.com/Obsidion-dev) team for use by the minecraft community"
    redis: RedisDsn = "redis://cache/1"

    class Config:
        env_file = ".env"


settings = Settings()
