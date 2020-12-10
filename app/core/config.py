import logging
import sys

from databases import DatabaseURL
from loguru import logger
from starlette.config import Config
from starlette.datastructures import Secret

from app.core.logging import InterceptHandler

API_PREFIX = "/api/v1"

JWT_TOKEN_PREFIX = "Token"  # noqa: S105
VERSION = "1.0.0"

config = Config(".env")

DEBUG: bool = config("DEBUG", cast=bool, default=False)

DATABASE_URL: DatabaseURL = config("DB_CONNECTION", cast=DatabaseURL)
MAX_CONNECTIONS_COUNT: int = config("MAX_CONNECTIONS_COUNT", cast=int, default=10)
MIN_CONNECTIONS_COUNT: int = config("MIN_CONNECTIONS_COUNT", cast=int, default=10)

SECRET_KEY: Secret = config("SECRET_KEY", cast=Secret)

PROJECT_NAME: str = config("PROJECT_NAME", default="FastAPI example application")
OPENAPI_URL: str = config("OPENAPI_URL", default="/api/v1/openapi.json")
DOCS_URL: str = config("DOCS_URL", default="/api/v1/docs")
REDOC_URL: str = config("REDOC_URL", default="/api/v1/redoc")

# logging configuration

LOGGING_LEVEL = logging.DEBUG if DEBUG else logging.INFO
LOGGERS = ("uvicorn.asgi", "uvicorn.access")

logging.getLogger().handlers = [InterceptHandler()]
for logger_name in LOGGERS:
    logging_logger = logging.getLogger(logger_name)
    logging_logger.handlers = [InterceptHandler(level=LOGGING_LEVEL)]

logger.configure(handlers=[{"sink": sys.stderr, "level": LOGGING_LEVEL}])
