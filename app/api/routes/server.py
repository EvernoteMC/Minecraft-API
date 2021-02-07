from fastapi import APIRouter
from typing import Optional
from aiomcstats import status
from aiomcstats.models.status import Status, OfflineStatus
import io
import base64
from starlette.responses import StreamingResponse


router = APIRouter()


@router.get(
    "/java",
    summary="View the status of a java server",
    response_model=Status,
    responses={404: {"model": OfflineStatus}},
)
async def java(server: str, port: Optional[int] = None):
    if port:
        data = await status(server, port)
    else:
        data = await status(server)
    return data


@router.get("/javaicon", summary="View the icon for a java server")
async def javaicon(server: str, port: Optional[int] = None):
    if port:
        data = await status(server, port)
    else:
        data = await status(server)
    encoded = base64.decodebytes(data.icon[22:].encode("utf-8"))
    image_bytesio = io.BytesIO(encoded)
    return StreamingResponse(image_bytesio, media_type="image/png")


@router.get("/motd", summary="View the motd of a server")
async def javaicon(server: str, port: Optional[int] = None):
    if port:
        data = await status(server, port)
    else:
        data = await status(server)
    # encoded = base64.decodebytes(data.icon[22:].encode("utf-8"))
    # image_bytesio = io.BytesIO(encoded)
    # return StreamingResponse(image_bytesio, media_type="image/png")


@router.get("/bedrock", summary="View the status of a bedrock server", status_code=501)
async def bedrock(server: str, port: Optional[int] = None):
    pass
