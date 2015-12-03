# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 17:30:15 2015

@author: Alan
"""

from PIL import Image
import random

dice_blank = Image.open('dice_blank.png')   #导入空白筛子
spot = Image.open('spot.png')               #导入筛子上的黑点

print(dice_blank.size)
print(spot.size)

print(2828 / 75)