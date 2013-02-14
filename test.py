import os, sys
from PIL import Image

im = Image.open("wind010.png")
x = 230
y = 470

pix = im.load()
print pix[x,y]