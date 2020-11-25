from fastapi import FastAPI, Request, Response
from fastapi_caching import CacheManager, RedisBackend
import logging
import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
import uvicorn
from fastapi.responses import JSONResponse
import pydantic

from app.routers import images, info, mojang, render, server
from app.tags import tags_metadata
from app.settings import get_settings

"""
Init stuff.
"""

LOGGER = logging.getLogger("api")

SETTINGS = get_settings()

if SETTINGS.sentry_dsn:  # pragma: no cover
    sentry_sdk.init(dsn=SETTINGS.sentry_dsn)

app = FastAPI(
    title="Obsidion-dev Minecraft API",
    description="A Minecraft API brought to you by the folks at Obsidion-dev",
    version="0.0.1",
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
)

"""
Middleware.
"""

# Sentry Error Tracking
if SETTINGS.sentry_dsn:  # pragma: no cover
    LOGGER.info("Adding Sentry middleware")
    app.add_middleware(SentryAsgiMiddleware)


"""
Routes.
"""

app.include_router(
    images.router,
    prefix="/images",
    tags=["images"],
)
app.include_router(
    info.router,
    prefix="/info",
    tags=["info"],
)
app.include_router(
    mojang.router,
    prefix="/mojang",
    tags=["mojang"],
)
app.include_router(
    render.router,
    prefix="/render",
    tags=["render"],
)
app.include_router(
    server.router,
    prefix="/server",
    tags=["server"],
)

"""
Cache.
"""

# cache_backend = RedisBackend(
#     host=SETTINGS.redis_host,
#     port=SETTINGS.redis_port,
#     prefix="api",
#     app_version="0.0.1",
# )
# cache_manager = CacheManager(cache_backend)

"""
Exception Handler.
"""


@app.exception_handler(pydantic.error_wrappers.ValidationError)
async def handle_validation_error(
    request: Request, exc: pydantic.error_wrappers.ValidationError
):  # pylint: disable=unused-argument
    """
    Handles validation errors.
    """
    return JSONResponse({"message": exc.errors()}, status_code=422)


if __name__ == "__main__":
    uvicorn.run(
        "app.main:APP",
        host="127.0.0.1",
        port=SETTINGS.port,
        log_level="info",
    )
