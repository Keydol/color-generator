from flask import Flask
from flask import request
from pydantic import BaseModel
from pydantic.class_validators import root_validator
import settings
import json
from PIL import Image

app = Flask(__name__)

class SquareTerritory(BaseModel):
    square_1: list = None            # | 1 2 |
    square_2: list = None            # | 3 4 |
    square_3: list = None
    square_4: list = None


class PaintMap:
    @staticmethod
    def paint(colors: SquareTerritory, img_name: str):
        square = Image.open(f"static/map/{img_name}_original.jpeg")
        square = square.convert("RGBA")

        c1 = colors.square_1
        color_square_1 = Image.new('RGBA', (100, 100), (c1[0], c1[1], c1[2], c1[3]))

        c2 = colors.square_2
        color_square_2 = Image.new('RGBA', (100, 100), (c2[0], c2[1], c2[2], c1[3]))

        c3 = colors.square_3
        color_square_3 = Image.new('RGBA', (100, 100), (c3[0], c3[1], c3[2], c3[3]))

        c4 = colors.square_4
        color_square_4 = Image.new('RGBA', (100, 100), (c4[0], c4[1], c4[2], c4[3]))

        square.paste(color_square_1, (0, 0), color_square_1) # up left
        square.paste(color_square_2, (0, 100), color_square_2) # down left
        square.paste(color_square_3, (100, 0), color_square_3) # up right
        square.paste(color_square_4, (100, 100), color_square_4) # down right
        square.save(f"static/map/{img_name}.jpeg")


class MainTerritory(BaseModel):
    square_1: SquareTerritory = None            # | 1  2  3  4  |
    square_2: SquareTerritory = None            # | 5  6  7  8  |
    square_3: SquareTerritory = None            # | 9  10 11 12 |
    square_4: SquareTerritory = None            # | 13 14 15 16 |
    square_5: SquareTerritory = None            # | 17 18 19 20 |
    square_6: SquareTerritory = None            # | 21 22 23 24 |
    square_7: SquareTerritory = None            # | 25 26 27 28 |
    square_8: SquareTerritory = None            # | 29 30 31 32 |
    square_9: SquareTerritory = None            # | 33 34 35 36 |
    square_10: SquareTerritory = None           # | 37 38 39 40 |
    square_11: SquareTerritory = None           # | 41 42 43 44 |
    square_12: SquareTerritory = None           # | 45 46 47 48 |
    square_13: SquareTerritory = None
    square_14: SquareTerritory = None
    square_15: SquareTerritory = None
    square_16: SquareTerritory = None
    square_17: SquareTerritory = None
    square_18: SquareTerritory = None
    square_19: SquareTerritory = None
    square_20: SquareTerritory = None
    square_21: SquareTerritory = None
    square_22: SquareTerritory = None
    square_23: SquareTerritory = None
    square_24: SquareTerritory = None
    square_25: SquareTerritory = None
    square_26: SquareTerritory = None
    square_27: SquareTerritory = None
    square_28: SquareTerritory = None
    square_29: SquareTerritory = None
    square_30: SquareTerritory = None
    square_31: SquareTerritory = None
    square_32: SquareTerritory = None
    square_33: SquareTerritory = None
    square_34: SquareTerritory = None
    square_35: SquareTerritory = None
    square_36: SquareTerritory = None
    square_37: SquareTerritory = None
    square_38: SquareTerritory = None
    square_39: SquareTerritory = None
    square_40: SquareTerritory = None
    square_41: SquareTerritory = None
    square_42: SquareTerritory = None
    square_43: SquareTerritory = None
    square_44: SquareTerritory = None
    square_45: SquareTerritory = None
    square_46: SquareTerritory = None
    square_47: SquareTerritory = None
    square_48: SquareTerritory = None

    @root_validator()
    def paint_validate(cls, values):
        for img_name, colors in values.items():
            if colors:
                PaintMap.paint(colors, img_name)
        return values

@app.route(f"/generate_map_color_{settings.TOKEN}", methods=['POST'])
async def generate_map_color():
    data = json.loads(request.data)
    territories = MainTerritory(**data)
    return "200"


# @app.route("/", methods=['GET'])
# async def get_main():
#     return '<img src="static/map/square_1.jpeg">'


app.run()
