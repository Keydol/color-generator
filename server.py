from flask import Flask
from flask import request
from pydantic import BaseModel, Field
from pydantic.class_validators import root_validator
import settings
import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List

app = Flask(__name__)

class Area(BaseModel):
    square: int
    pixel: int
    color: str

    @root_validator
    def paint_validate(cls, values):
        font = ImageFont.truetype("ARIALUNI.TTF", 13)
        img_path = f"static/map/square_{values['square']}.jpeg"
        img = Image.open(img_path)
        y = ((values["pixel"] -1) // 8) * 64
        x = (((values["pixel"] % 8) or 8) - 1) * 64
        size = 64
        draw = ImageDraw.Draw(img)
        draw.rectangle((x, y, x + size, y + size), fill=values["color"])
        x += 25
        y += 25
        draw.text((x, y), str(values["pixel"]), fill=(18, 57, 51), font=font)
        img.save(img_path)
        return values

@app.route(f"/set_pixel_color_gfdgdfioj34i9483i34", methods=['POST'])
async def generate_pixel_color():
    data = json.loads(request.data)
    area = Area(**data)
    return "200"

app.run()
