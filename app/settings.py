"""Settings."""

import logging
from functools import lru_cache

from pydantic import BaseSettings

__all__ = ("get_settings",)

log = logging.getLogger("app.config")


class _Settings(BaseSettings):
    environment: str = "dev"
    testing: bool = 0
    redis_host: str = "127.0.0.1"
    redis_port: int = 6379
    sentry_dsn: str = None


@lru_cache()
def get_settings(**kwargs) -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return _Settings(**kwargs)
