from fastapi import FastAPI
from fastapi_caching import CacheManager, RedisBackend, ResponseCache, hashers

from app.routers import images, info, mojang, render, server
from app.tags import tags_metadata
from app.settings import get_settings

settings = get_settings()

app = FastAPI(
    title="Obsidion-dev Minecraft API",
    description="A Minecraft API brought to you by the folks at Obsidion-dev",
    version="0.0.1",
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    redoc_url=None,
)


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

cache_backend = RedisBackend(
    host=settings.redis_host,
    port=settings.redis_port,
    prefix="api",
    app_version="0.0.1",
)
cache_manager = CacheManager(cache_backend)