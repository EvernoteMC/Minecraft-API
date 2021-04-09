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
    Recipies,
    Materials,
)

router = APIRouter()


@router.get("/item", response_model=Item, summary="View info on an item")
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/block", response_model=Block, summary="View info on a block")
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get("/effect", response_model=Effect, summary="View info on an effect")
async def effect(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.effects_name[name]


@router.get("/mob", response_model=Mob, summary="View info on a mob", status_code=501)
async def mob(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.entities_name[name]


@router.get(
    "/advancement",
    response_model=Achievement,
    summary="View info on an achivement",
)
async def achievement(
    version: str, name_id: Union[str, int], pe: Optional[bool] = False
):
    pass


@router.get(
    "/structure",
    response_model=Structure,
    summary="View info on a structure",
)
async def structure(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    pass


@router.get("/biome", response_model=Biome, summary="View info on a biome")
async def biome(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.biomes_name[name]


@router.get(
    "/command",
    response_model=Commands,
    summary="View info on a command",
)
async def command(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get(
    "/loottable",
    response_model=Loottable,
    summary="View info on a loottable",
)
def loottable(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.find_item_or_block(name_id)


@router.get(
    "/recipies",
    response_model=Recipies,
    summary="View info on a loottable",
)
def recipies(version: str, id: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.recipes[id]


@router.get(
    "/materials",
    response_model=Materials,
    summary="View info on a loottable",
)
def materials(version: str, id: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.materials[id]
