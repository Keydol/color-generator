from flask import Flask
from flask import request
from pydantic import BaseModel, Field
from pydantic.class_validators import root_validator
import settings
import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List


im = Image.open("static/map/map.jpeg")

num = 1
for y in range(0, 2400, 200):
    for x in range(0, 600, 200):
        im_crop = im.crop((x, y, x + 200, y + 200))
        im_crop.save(f'static/map/square_{num}_original.jpeg')
        num += 1
