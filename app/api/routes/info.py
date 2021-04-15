from fastapi import APIRouter
from typing import Optional, Union
import minecraft_data

from app.models.info import (
    Biome,
    Item,
    Block,
    Effect,
    Entity,
    Recipe,
)

router = APIRouter()


@router.get("/biome", summary="View info on a biome")
async def biome(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.biomes_name[name]

@router.get("/item", summary="View info on an item")
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.items_name[name_id]
    return mcd.items[name_id]


@router.get("/block", summary="View info on a block")
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.blocks_name[name_id]
    return mcd.blocks[name_id]


@router.get("/effect", summary="View info on an effect")
async def effect(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.effects_name[name]


@router.get("/entity", summary="View info on a mob")
async def entity(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)

    return mcd.entities_name[name]


@router.get(
    "/recipe",
    summary="View info on a loottable",
)
def recipes(version: str, id: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.recipes[id]

