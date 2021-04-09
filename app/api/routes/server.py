from fastapi import APIRouter
from typing import Optional
import aiomcstats
from aiomcstats.models import Status, OfflineStatus, BedrockOffline, BedrockStatus
import io
import base64
from fastapi.encoders import jsonable_encoder
from starlette.responses import StreamingResponse
from fastapi.responses import JSONResponse


router = APIRouter()


@router.get(
    "/java",
    summary="View the status of a java server",
    response_model=Status,
    responses={404: {"model": OfflineStatus}},
)
async def java(server: str, port: Optional[int] = None):
    if port:
        data = await aiomcstats.status(server, port)
    else:
        data = await aiomcstats.status(server)
    if data.online == False:
        return JSONResponse(status_code=404, content=jsonable_encoder(data))
    return data


@router.get("/javaicon", summary="View the icon for a java server")
async def javaicon(server: str, port: Optional[int] = None):
    if port:
        data = await aiomcstats.status(server, port)
    else:
        data = await aiomcstats.status(server)
    encoded = base64.decodebytes(data.icon[22:].encode("utf-8"))
    image_bytesio = io.BytesIO(encoded)
    return StreamingResponse(image_bytesio, media_type="image/png")


@router.get("/motd", summary="View the motd of a server", status_code=501)
async def javamotd(server: str, port: Optional[int] = None):
    pass
    # if port:
    #     data = await status(server, port)
    # else:
    #     data = await status(server)
    # encoded = base64.decodebytes(data.icon[22:].encode("utf-8"))
    # image_bytesio = io.BytesIO(encoded)
    # return StreamingResponse(image_bytesio, media_type="image/png")


@router.get("/bedrock", summary="View the status of a bedrock server",response_model=BedrockStatus,
    responses={404: {"model": BedrockOffline}},)
async def bedrock(server: str, port: Optional[int] = None):
    if port:
        data = await aiomcstats.bedrock(server, port)
    else:
        data = await aiomcstats.bedrock(server)
    if data.online == False:
        return JSONResponse(status_code=404, content=jsonable_encoder(data))
    return data
