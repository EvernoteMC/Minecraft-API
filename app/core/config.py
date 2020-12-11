import logging
import sys

from loguru import logger
from pydantic import BaseSettings

from app.core.logging import InterceptHandler


class Settings(BaseSettings):
    api_prefix: str = "/api/v1"
    version: str = "1.0.0"
    debug: bool = True
    project_name: str = "Minecraft API"
    openapi_url: str = "/api/v1/openapi.json"
    docs_url: str = "/api/v1/docs"
    redoc_url: str = "/api/v1/redocs"
    description: str = "This is the API developed by the [Obsidion-dev](https://github.com/Obsidion-dev) team for use by the minecraft community"

    class Config:
        env_file = ".env"


settings = Settings()

# logging configuration

LOGGING_LEVEL = logging.DEBUG if settings.debug else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
