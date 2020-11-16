from fastapi import APIRouter

router = APIRouter()


@router.get("/item")
async def item():
    pass


@router.get("/block")
async def block():
    pass


@router.get("/mob")
async def mob():
    pass


@router.get("/achievement")
async def achievement():
    pass


@router.get("/structure")
async def structure():
    pass


@router.get("/biome")
async def biome():
    pass


@router.get("/command")
async def command():
    pass


@router.get("/loottable")
def loottable():
    pass