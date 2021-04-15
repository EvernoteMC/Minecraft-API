from fastapi import APIRouter

router = APIRouter()


# @router.get(
    # "/recipie", summary="Render a png/gif of a minecraft recipe", status_code=501
# )
async def recipie():
    pass


# @router.get("/banner", summary="Render a minecraft banner", status_code=501)
async def banner():
    pass


# @router.get("/item", summary="Render minecraft item", status_code=501)
async def item():
    pass


# @router.get("/block", summary="Render minecraft block", status_code=501)
async def block():
    pass


# @router.get("/mob", summary="Render minecraft mob", status_code=501)
async def mob():
    pass
