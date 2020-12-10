from fastapi import APIRouter

router = APIRouter()


@router.get(
    "/recipie", summary="Render a png/gif of a minecraft recipe", status_code=501
)
async def recipie():
    pass


@router.get("/banner", summary="Render a minecraft banner", status_code=501)
async def banner():
    pass


@router.get("/image", summary="Convert an image to a minecraft one", status_code=501)
async def image():
    pass
