from typing import Optional

from pydantic import BaseModel, Field


class Biome(BaseModel):
    """The color in a biome"""

    color: Optional[int]
    """The display name of a biome"""
    display_name: Optional[str]
    """The unique identifier for a biome"""
    id: int
    """The name of a biome"""
    name: str
    """How much rain there is in a biome"""
    rainfall: float
    """An indicator for the temperature in a biome"""
    temperature: float


class Item(BaseModel):
    pass


class Block(BaseModel):
    pass


class Effect(BaseModel):
    pass


class Mob(BaseModel):
    pass


class Structure(BaseModel):
    pass


class Commands(BaseModel):
    pass


class Loottable(BaseModel):
    pass


class Achievement(BaseModel):
    pass


class Materials(BaseModel):
    pass


class Recipies(BaseModel):
    pass
