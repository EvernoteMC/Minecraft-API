import logging
import os
from functools import lru_cache

from pydantic import BaseSettings

__all__ = ("get_settings",)

log = logging.getLogger(__name__)


class _Settings(BaseSettings):
    environment: str = os.getenv("ENVIRONMENT", "dev")
    testing: bool = os.getenv("TESTING", 0)
    redis_host: str = os.getenv("REDIS_HOST", "127.0.0.1")
    redis_port: int = os.getenv("REDIS_PORT", 6379)


@lru_cache()
def get_settings() -> _Settings:
    log.info("Loading config settings from the environment...")
    return _Settings()
