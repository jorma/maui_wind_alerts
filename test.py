import os, sys
from PIL import Image

im = Image.open("windarea.png")
x = 285
y = 350

pix = im.load()



# go over each pixel 

color = pix[x,y]

if color == (0,0,0):
	print "black"
else:
	print "white"