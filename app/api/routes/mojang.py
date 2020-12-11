from fastapi import APIRouter
import aiohttp

from app.models.mojang import MojangStatus


router = APIRouter()

mojang_sites = (
    "https://www.minecraft.net",
    "https://account.mojang.com",
    "https://authserver.mojang.com",
    "https://api.mojang.com",
    "https://textures.minecraft.net",
)


@router.get(
    "/check/", response_model=MojangStatus, summary="View the status of mojang services"
)
async def check():
    status = {}
    for site in mojang_sites:
        async with aiohttp.ClientSession() as session:
            async with session.get(site) as response:
                status[site] = "green" if response.status == 200 else "red"
    return status
