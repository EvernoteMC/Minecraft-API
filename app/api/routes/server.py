from fastapi import APIRouter
from typing import Optional, Union
from pydantic import BaseModel


router = APIRouter()


@router.get("/java/")
async def java(server: str, port: Optional[int] = None):
    pass


@router.get("/javaicon/")
async def javaicon(server: str, port: Optional[int] = None):
    pass


@router.get("/bedrock/")
async def bedrock(server: str, port: Optional[int] = None):
    pass
