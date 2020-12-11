from fastapi import APIRouter
from typing import Optional


router = APIRouter()


@router.get("/java/", summary="View the status of a java server", status_code=501)
async def java(server: str, port: Optional[int] = None):
    pass


@router.get("/javaicon/", summary="View the icon for a java server", status_code=501)
async def javaicon(server: str, port: Optional[int] = None):
    pass


@router.get("/bedrock/", summary="View the status of a bedrock server", status_code=501)
async def bedrock(server: str, port: Optional[int] = None):
    pass
