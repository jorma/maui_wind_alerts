import os, sys
from PIL import Image
import pickle

im = Image.open("windarea.png")
x = 0
y = 0

windArea = []


#for y in range(275, 412):
for y in range(304, 305):
	
	for x in range(0, 639):
		pix = im.load()
	
		color = pix[x,y]
	
		if color == (0,0,0):
			coordinate = str(x) + "," + str(y)
			print coordinate
			print "********** black ***********"
			windArea.append(coordinate)
		else:
			print str(x) + "," + str(y)
			print "white"

print windArea

output = open("windArea.txt","w")
pickle.dump(windArea,output)
output.close()
	
