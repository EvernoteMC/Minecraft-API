from fastapi import APIRouter, Body, Depends, HTTPException
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
        if name_id not in mcd.biomes_name:
            raise HTTPException(
                status_code=404, detail="The biome could not be found.",
            )
        return mcd.biomes_name[name_id]
    if name_id not in mcd.biomes:
        raise HTTPException(
            status_code=404, detail="The biome could not be found.",
        )
    return mcd.biomes[name_id]


@router.get("/item", summary="View info on an item", response_model=schemas.Item)
async def item(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        if name_id not in mcd.items_name:
            raise HTTPException(
                status_code=404, detail="The item could not be found.",
            )
        return mcd.items_name[name_id]
    if name_id not in mcd.items:
        raise HTTPException(
            status_code=404, detail="The item could not be found.",
        )
    return mcd.items[name_id]


@router.get("/block", summary="View info on a block", response_model=schemas.Block)
async def block(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        if name_id not in mcd.blocks_name:
            raise HTTPException(
                status_code=404, detail="The block could not be found.",
            )
        return mcd.blocks_name[name_id]
    if name_id not in mcd.blocks:
        raise HTTPException(
            status_code=404, detail="The block could not be found.",
        )
    return mcd.blocks[name_id]


@router.get("/effect", summary="View info on an effect", response_model=schemas.Effect)
async def effect(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        if name_id not in mcd.effects_name:
            raise HTTPException(
                status_code=404, detail="The effect could not be found.",
            )
        return mcd.effects_name[name_id]
    if name_id not in mcd.effects:
        raise HTTPException(
            status_code=404, detail="The effect could not be found.",
        )
    return mcd.effects[name_id]


@router.get("/entity", summary="View info on a mob", response_model=schemas.Entity)
async def entity(version: str, name_id: Union[str, int], pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if type(name_id) == str:
        if name_id not in mcd.entities_name:
            raise HTTPException(
                status_code=404, detail="The entity could not be found.",
            )
        return mcd.entities_name[name_id]
    if name_id not in mcd.entities:
        raise HTTPException(
            status_code=404, detail="The entity could not be found.",
        )
    return mcd.entities[name_id]


@router.get(
    "/recipe", summary="View info on a loottable", response_model=schemas.Recipe
)
def recipes(version: str, id: int, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if id not in mcd.recipes:
        raise HTTPException(
            status_code=404, detail="The recipe could not be found.",
        )
    return mcd.recipes[id]


@router.get(
    "/instruments", summary="View info on a loottable",
)
def instruments(version: str, id: int, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if id not in mcd.instruments:
        raise HTTPException(
            status_code=404, detail="The instrument could not be found.",
        )
    return mcd.instruments[id]


@router.get(
    "/materials", summary="View info on a loottable",
)
def materials(version: str, name: str, pe: Optional[bool] = False):
    if pe:
        mcd = minecraft_data(version, "pe")
    else:
        mcd = minecraft_data(version)
    if id not in mcd.materials:
        raise HTTPException(
            status_code=404, detail="The material could not be found.",
        )
    return mcd.materials[id]
