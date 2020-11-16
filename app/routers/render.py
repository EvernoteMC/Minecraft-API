from fastapi import APIRouter

router = APIRouter()


@router.get("/recipie")
async def recipie():
    pass


@router.get("/banner")
async def banner():
    pass


@router.get("/firework")
async def firework():
    pass