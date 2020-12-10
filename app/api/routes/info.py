from fastapi import APIRouter
from typing import Optional, Union
import minecraft_data

from app.models.info import (
    Biome,
    Item,
    Block,
    Effect,
    Mob,
    Structure,
    Commands,
    Loottable,
    Achievement,
)

router = APIRouter()


@router.get("/item", response_model=Item)
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/block", response_model=Block)
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/effect", response_model=Effect)
async def effect(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.effects_name[name]


@router.get("/mob", response_model=Mob)
async def mob():
    pass


@router.get("/achievement", response_model=Achievement)
async def achievement():
    pass


@router.get("/structure", response_model=Structure)
async def structure():
    pass


@router.get("/biome", response_model=Biome)
async def biome(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.biomes_name[name]


@router.get("/command", response_model=Commands)
async def command():
    pass


@router.get("/loottable", response_model=Loottable)
def loottable():
    pass
