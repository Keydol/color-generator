from flask import Flask
from flask import request
from pydantic import BaseModel, Field
from pydantic.class_validators import root_validator
import settings
import json
from PIL import Image, ImageDraw, ImageFont
from typing import Dict, List


im = Image.open("static/map/map.jpeg")


# img_1 = (0, 0, 200, 200)
# img_2 = (200, 0, 400, 200)
# img_3 = (400, 0, 600, 200)
# img_4 = (600, 0, 800, 200)

# im1_crop = im.crop((0, 0, 200, 200))
# im2_crop = im.crop((200, 0, 400, 200))
# im3_crop = im.crop((400, 0, 600, 200))
# im4_crop = im.crop((600, 0, 800, 200))

# im5_crop = im.crop((0, 200, 200, 400))
# im6_crop = im.crop((200, 200, 400, 400))
# im7_crop = im.crop((400, 200, 600, 400))
# im8_crop = im.crop((600, 200, 800, 400))

num = 1
for i in range(0, 2400, 200):
    im1_crop = im.crop((0, i, 200, i+200))
    im2_crop = im.crop((200, i, 400, i+200))
    im3_crop = im.crop((400, i, 600, i+200))
    im4_crop = im.crop((600, i, 800, i+200))
    breakpoint()
    im1_crop.save(f'static/map/square_{num}_original.jpeg', quality=95)
    num += 1
    im2_crop.save(f'static/map/square_{num}_original.jpeg')
    num += 1
    im3_crop.save(f'static/map/square_{num}_original.jpeg')
    num += 1
    im4_crop.save(f'static/map/square_{num}_original.jpeg')
    num += 1