from fastapi import APIRouter

from app.api.routes import images, info, mojang, render, server

router = APIRouter()
router.include_router(images.router, tags=["images"], prefix="/images")
router.include_router(info.router, tags=["info"], prefix="/info")
router.include_router(mojang.router, tags=["mojang"], prefix="/mojang")
router.include_router(render.router, tags=["render"], prefix="/render")
router.include_router(server.router, tags=["server"], prefix="/server")
