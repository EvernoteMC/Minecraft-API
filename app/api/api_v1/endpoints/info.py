from fastapi import APIRouter
from typing import Optional, Union
import minecraft_data

from app import schemas

router = APIRouter()


@router.get("/biome", summary="View info on a biome", response_model=schemas.Biome)
async def biome(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.biomes_name[name_id]
    return mcd.biomes[name_id]

@router.get("/item", summary="View info on an item", response_model=schemas.Item)
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.items_name[name_id]
    return mcd.items[name_id]


@router.get("/block", summary="View info on a block", response_model=schemas.Block)
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.blocks_name[name_id]
    return mcd.blocks[name_id]


@router.get("/effect", summary="View info on an effect", response_model=schemas.Effect)
async def effect(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.effects_name[name_id]
    return mcd.effects[name_id]


@router.get("/entity", summary="View info on a mob", response_model=schemas.Entity)
async def entity(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        return mcd.entities_name[name_id]
    return mcd.entities[name_id]


@router.get(
    "/recipe",
    summary="View info on a loottable",
    response_model=schemas.Recipe
)
def recipes(version: str, id: int, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.recipes[id]

@router.get(
    "/instruments",
    summary="View info on a loottable",
)
def instruments(version: str, id: int, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.instruments[id]

@router.get(
    "/materials",
    summary="View info on a loottable",
)
def materials(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    return mcd.materials[id]

