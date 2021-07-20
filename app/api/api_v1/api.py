from app.api.api_v1.endpoints import images
from app.api.api_v1.endpoints import info
from app.api.api_v1.endpoints import mojang
from app.api.api_v1.endpoints import render
from app.api.api_v1.endpoints import server

from fastapi import APIRouter

api_router = APIRouter()
api_router.include_router(images.router, prefix="/images", tags=["images"])
api_router.include_router(info.router, prefix="/info", tags=["info"])
api_router.include_router(mojang.router, prefix="/mojang", tags=["mojang"])
api_router.include_router(render.router, prefix="/render", tags=["render"])
api_router.include_router(server.router, prefix="/server", tags=["server"])
