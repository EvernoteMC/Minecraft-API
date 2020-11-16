from fastapi import FastAPI

from .routers import images, info, mojang, render, server
from .tags import tags_metadata

app = FastAPI(
    title="Obsidion-dev Minecraft API",
    description="A Minecraft API brought to you by the folks at Obsidion-dev",
    version="0.0.1",
    openapi_tags=tags_metadata,
    openapi_url="/api/v1/openapi.json",
    redoc_url=None,
)


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
