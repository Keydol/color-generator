from flask import Flask
from flask import request
from pydantic import BaseModel, Field
from pydantic.class_validators import root_validator
import settings
import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List

app = Flask(__name__)

class SquareInfo(BaseModel):
    rgb_color: list = Field(exclusiveMaximum=3)
    owner_name: str

    @root_validator
    def strip_name(cls, values):
        if len(values["owner_name"]) > 10:
            values["owner_name"] = values["owner_name"][:9] + "..."
        return values


class PaintMap:
    @staticmethod
    def get_coords(square_name: str, size: int):
        square_coords = {
            "subsquare_1": (0, 0),
            "subsquare_2": (0, size),
            "subsquare_3": (size, 0),
            "subsquare_4": (size, size)
        }
        return square_coords[square_name]


    @staticmethod
    def paint(subsquares: SquareInfo, img_name: str):
        square = Image.open(f"static/map/{img_name}_original.jpeg")
        square = square.convert("RGBA")
        size = int(square.size[0] / 2)
        font = ImageFont.truetype("ARIALUNI.TTF", 15)
        x = 5
        y = size - 20

        for subsquare_name, subsquare_info in subsquares.items():
            color = subsquare_info.rgb_color
            name = subsquare_info.owner_name

            mask = Image.new('RGBA', (size, size), (color[0], color[1], color[2], 100))
            draw_text = ImageDraw.Draw(mask)
            w, h = font.getsize(name)
            draw_text.rectangle((x, y, x + w, y + h), fill=(0, 0, 0, 150))
            draw_text.text((x, y), name, fill='#ffffff', font=font)

            coords = PaintMap.get_coords(subsquare_name, size)
            square.paste(mask, coords, mask)
        
        square = square.convert('RGB')
        square.save(f"static/map/{img_name}.jpeg")

class MainTerritory(BaseModel):
    map: Dict[str, Dict[str, SquareInfo]]
    # |1 2|
    # |3 4|

    @root_validator
    def paint_validate(cls, values):
        for img_name, square in values["map"].items():
            if square:
                PaintMap.paint(square, img_name)
        return values

@app.route(f"/generate_map_color_{settings.TOKEN}", methods=['POST'])
async def generate_map_color():
    data = json.loads(request.data)
    territories = MainTerritory(**data)
    return "200"

app.run()
