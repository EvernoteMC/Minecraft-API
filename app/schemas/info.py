from typing import List, Optional, Union, Dict, Any
from enum import Enum


from pydantic import BaseModel, Extra, Field, conint, constr, confloat


###########
## Biome ##
###########
class Biome(BaseModel):
    id: conint(ge=0) = Field(..., description="The unique identifier for a biome")
    name: str = Field(..., description="The name of a biome")
    category: str = Field(..., description="The category of a biome")
    temperature: confloat(ge=-1.0, le=2.0) = Field(
        ..., description="An indicator for the temperature in a biome"
    )
    precipitation: str = Field(
        ..., description="The type of precipitation: none, rain or snow"
    )
    depth: float = Field(..., description="The depth of a biome")
    dimension: str = Field(
        ..., description="The dimension of a biome: overworld, nether or end"
    )
    displayName: constr(regex=r"\S+") = Field(
        ..., description="The display name of a biome"
    )
    color: conint(ge=0) = Field(..., description="The color in a biome")
    rainfall: confloat(ge=0.0, le=1.0) = Field(
        ..., description="How much rain there is in a biome"
    )


##########
## Item ##
##########
class ItemVariation(BaseModel):
    metadata: conint(ge=0)
    displayName: str


class Item(BaseModel):
    class Config:
        extra = Extra.allow

    id: conint(ge=0) = Field(..., description="The unique identifier for an item")
    displayName: str = Field(..., description="The display name of an item")
    stackSize: conint(ge=0) = Field(..., description="Stack size for an item")
    enchantCategories: Optional[List[str]] = Field(
        None, description="describes categories of enchants this item can use"
    )
    fixedWith: Optional[List[str]] = Field(
        None, description="describes what items this item can be fixed with in an anvil"
    )
    maxDurability: Optional[conint(ge=0)] = Field(
        None,
        description="the amount of durability an item has before being damaged/used",
    )
    name: constr(regex=r"\S+") = Field(..., description="The name of an item")
    variations: Optional[List[ItemVariation]] = None
    durability: Optional[Optional[conint(ge=0)]] = Field(
        None, description="The durability of an item"
    )


###########
## Block ##
###########
class BoundingBox(Enum):
    block = "block"
    empty = "empty"


class BlockVariation(BaseModel):
    metadata: conint(ge=0)
    displayName: str
    description: Optional[str] = None


class BlockType(Enum):
    enum = "enum"
    bool = "bool"
    int = "int"


class State(BaseModel):
    name: str = Field(..., description="The name of the property")
    type: BlockType = Field(..., description="The type of the property")
    values: Optional[List] = Field(
        None, description="The possible values of the property"
    )
    num_values: confloat(ge=1.0) = Field(
        ..., description="The number of possible values"
    )


class DropItem(BaseModel):
    id: conint(ge=0)
    metadata: conint(ge=0)


class Drop(BaseModel):
    minCount: Optional[confloat(ge=0.0)] = Field(
        None, description="minimum number or chance, default : 1"
    )
    maxCount: Optional[confloat(ge=0.0)] = Field(
        None, description="maximum number or chance, default : minCount"
    )
    drop: Union[int, DropItem]


class Block(BaseModel):
    id: conint(ge=0) = Field(..., description="The unique identifier for a block")
    displayName: str = Field(..., description="The display name of a block")
    name: constr(regex=r"\S+") = Field(..., description="The name of a block")
    hardness: Optional[confloat(ge=0.0)] = Field(
        None, description="Hardness of a block"
    )
    stackSize: conint(ge=0) = Field(..., description="Stack size for a block")
    diggable: bool = Field(..., description="true if a block is diggable")
    boundingBox: BoundingBox = Field(..., description="BoundingBox of a block")
    material: Optional[str] = Field(None, description="Material of a block")
    harvestTools: Optional[Dict[str, Any]] = Field(
        None,
        description="Using one of these tools is required to harvest a block, without that you get a 3.33x time penalty.",
    )
    variations: Optional[List[BlockVariation]] = None
    states: Optional[List[State]] = None
    drops: List[Union[int, Drop]]
    transparent: bool = Field(..., description="true if a block is transparent")
    emitLight: conint(ge=0, le=15) = Field(
        ..., description="Light emitted by that block"
    )
    filterLight: conint(ge=0, le=15) = Field(
        ..., description="Light filtered by that block"
    )
    minStateId: Optional[conint(ge=0)] = Field(None, description="Minimum state id")
    maxStateId: Optional[conint(ge=0)] = Field(None, description="Maximum state id")
    defaultState: Optional[conint(ge=0)] = Field(None, description="Default state id")
    resistance: Optional[Optional[confloat(ge=-1.0)]] = Field(
        None, description="Blast resistance"
    )


############
## Effect ##
############
class EffectType(Enum):
    good = "good"
    bad = "bad"


class Effect(BaseModel):
    id: conint(ge=0) = Field(..., description="The unique identifier for an effect")
    displayName: str = Field(..., description="The display name of an effect")
    name: constr(regex=r"\S+") = Field(..., description="The name of an effect")
    type: EffectType = Field(
        ..., description="Whether an effect is positive or negative"
    )


############
## Entity ##
############
class Entity(BaseModel):
    id: conint(ge=0) = Field(..., description="The unique identifier for an entity")
    internalId: Optional[conint(ge=0)] = Field(
        None,
        description="The internal id of an entity : used in eggs metadata for example",
    )
    displayName: str = Field(..., description="The display name of an entity")
    name: constr(regex=r"\S+") = Field(..., description="The name of an entity")
    type: str = Field(..., description="The type of an entity")
    width: Optional[float] = Field(..., description="The width of the entity")
    height: Optional[float] = Field(..., description="The height of the entity")
    category: Optional[str] = Field(
        None, description="The category of an entity : a semantic category"
    )


############
## Recipe ##
############
class Id(BaseModel):
    __root__: Optional[int] = Field(..., description="A single numerical ID or null.")


class Metadata(BaseModel):
    __root__: int


class Count(BaseModel):
    __root__: int


class IdMetadataArray(BaseModel):
    __root__: List[Union[Id, Metadata]] = Field(
        ...,
        description="A list of id and metadata. This is preferred if there are many items at once, e.g. in a shape.",
        title="[id,metadata]",
    )


class IdMetadataCountObject(BaseModel):
    id: Id
    metadata: Optional[Metadata] = None
    count: Optional[Count] = None


class RecipeItem(BaseModel):
    __root__: Union[Id, IdMetadataArray, IdMetadataCountObject] = Field(
        ..., description="An item can be represented different ways."
    )


class ShapeRow(BaseModel):
    __root__: List[RecipeItem] = Field(..., max_items=3, min_items=1)


class Shape(BaseModel):
    __root__: List[ShapeRow] = Field(
        ...,
        description="A shape is a list of rows, which are lists of items. There must be at least one row with at least one item in it. All rows must have the same length. Empty rows at the beginning or end of a shape may be omitted. Empty colums at the end may also be omitted. When an item can be crafted in a 2x2 grid, the shape may not be larger than 2x2.",
        max_items=3,
        min_items=1,
    )


class Ingredients(BaseModel):
    __root__: List[RecipeItem] = Field(..., min_items=1)


class ShapedRecipe(BaseModel):
    result: RecipeItem
    inShape: Shape
    outShape: Optional[Shape] = None


class ShapelessRecipe(BaseModel):
    result: RecipeItem
    ingredients: Ingredients


class Recipe(BaseModel):
    __root__: Union[ShapedRecipe, ShapelessRecipe]
