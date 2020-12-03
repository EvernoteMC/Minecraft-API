from fastapi import APIRouter
from typing import Optional, Union
import minecraft_data

router = APIRouter()


@router.get("/item")
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/block")
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/effect")
async def effect(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.effects_name[name]


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
