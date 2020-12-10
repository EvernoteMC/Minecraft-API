from fastapi import APIRouter
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from starlette.responses import StreamingResponse

router = APIRouter()


@router.get("/book", summary="Generate a minecraft book page", status_code=501)
def book():
    pass


@router.get("/death", summary="Generate a minecraft death image", status_code=501)
def death():
    pass


@router.get(
    "/splashscreen", summary="Generate a minecraft splashscreen", status_code=501
)
def splashscreen():
    pass


@router.get("/motd", summary="Generate a message of the day", status_code=501)
def motd():
    pass


@router.get("/sign", summary="Generate an image of a sign")
def sign(line1: str, line2: str, line3: str, line4: str):
    # load the font, image and create a draw area
    W = 242
    font = ImageFont.truetype("assets/Minecraftia-Regular.ttf", 20)
    img = Image.open("assets/sign.png")
    draw = ImageDraw.Draw(img)

    # add all the lines of text
    if line1:
        w, h = draw.textsize(line1, font=font)
        draw.text(((W - w) / 2, 0), line1, font=font)
    if line2:
        w, h = draw.textsize(line2, font=font)
        draw.text(((W - w) / 2, 30), line2, font=font)
    if line3:
        w, h = draw.textsize(line3, font=font)
        draw.text(((W - w) / 2, 60), line3, font=font)
    if line4:
        w, h = draw.textsize(line4, font=font)
        draw.text(((W - w) / 2, 90), line4, font=font)

    # save the image in a buffer so we can send it
    img_io = BytesIO()
    img.save(img_io, "PNG", quality=70)
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")


@router.get("/advancement", summary="Generate an image of an advancement")
def advancement(item: str, title: str, text: str):
    # load font, image and create an area to draw on
    font = ImageFont.truetype("assets/Minecraftia-Regular.ttf", 14)
    img = Image.open("assets/advancement.png").convert("RGBA")
    draw = ImageDraw.Draw(img)

    # Title
    draw.text((60, 11), title, font=font, fill="#defa3c")

    # Message
    draw.text((60, 36), text, font=font, fill=(0, 0, 0, 0))

    # # Item
    item = (
        Image.open(f"items/{item}.png").resize((32, 32), Image.NEAREST).convert("RGBA")
    )

    # make the black around it fully opaque
    pixdata = item.load()
    width, height = item.size
    for y in range(height):
        for x in range(width):
            if pixdata[x, y] == (0, 0, 0, 255):
                pixdata[x, y] = (0, 0, 0, 0)

    # paste item onto image keeping transparency
    img.paste(item, (20, 14), item)

    # save image in buffer so we can send
    img_io = BytesIO()
    img.save(img_io, "PNG", quality=100)
    img_io.seek(0)
    return StreamingResponse(img_io, media_type="image/png")
