# This Python script 

import os, sys
from PIL import Image
import subprocess

# white is 255, 255, 255
# black is 0, 0, 0

# 0 dark blue is 0, 0, 255
# 0 - 5 blue is 63, 63, 255
# 5 - 10 light blue is 175, 191, 255
# 10 - 15 grey is 223, 215, 255
# 15 - 20 pink is 234, 172, 255
# 20 - 25 purple is 187, 84, 191
# 25 - 30 red is 191, 25, 89


# Uncomment two lines below to get file
#subprocess.call(['./download.sh'])

windArea=[]
for line in open( "windArray_complete.txt", "r" ).readlines():
		line = line.replace('\n', '')
		windArea.append(line)

numOfPts = len(windArea)
#print numOfPts

numOfPts = numOfPts + 0.0
#print windArea

countDarkBlue = 0
countBlue = 0
countLightBlue = 0
countGrey = 0
countPink = 0
countPurple = 0
countRed = 0
countOrange = 0
countBrightOrange = 0
countMauve = 0
countWhite = 0
countBlack = 0

im = Image.open("images/wind014.png")

# Calculated for Lahaina Area

for x in range(0, 6474):
	coordinate = windArea[x]

	coordinatePts = coordinate.split(",")

	x = int(coordinatePts[0])
	y = int(coordinatePts[1])

	pix = im.load()

	color = pix[x,y]

	
	#print "color: " + str(color) + " For coordinate: " + str(x) + "," + str(y)
	
	if color == (0,0,255): #dark blue
		#print "darkblue"
		countDarkBlue += 1
	
	elif color == (63, 63, 255): # blue
		#print "blue"
		countBlue += 1
		
	elif color == (175, 191, 255): # light blue
		#print "light blue"
		countLightBlue += 1

	elif color == (223, 215, 255): # grey
		#print "grey"
		countGrey += 1

	elif color == (234, 172, 255): # pink
		#print "pink"
		countPink += 1

	elif color == (187, 84, 191): # purple
		#print "purple"
		countPurple += 1
		
	elif color == (191, 25, 89): # red
		#print "red"
		countRed += 1
		
	elif color == (255, 25, 25): # orange
		#print "orange"
		countOrange += 1
		
	elif color == (255, 71, 94): # bright orange
		#print "bright orange"
		countBrightOrange += 1

	elif color == (255, 135, 158): # mauve
		#print "mauve"
		countMauve += 1
		
	elif color == (0, 0, 0): # black
		#print "black"
		countBlack += 1
		
	elif color == (255, 255, 255): # white
		#print ""
		countWhite += 1
			
	else:
		#print "not blue"
		#print color
		pass

#print "count is: " + str(count)
print "numOfPts is: " + str(numOfPts)

percentWhite = round((countWhite / numOfPts) * 100)
percentBlack = round((countBlack / numOfPts) * 100)

percentDarkBlue = round((countDarkBlue / numOfPts) * 100)
percentBlue = round((countBlue / numOfPts) * 100)
percentLightBlue = round((countLightBlue / numOfPts) * 100)
percentGrey = round((countGrey / numOfPts) * 100)
percentPink = round((countPink / numOfPts) * 100)
percentPurple = round((countPurple / numOfPts) * 100)
percentRed = round((countRed / numOfPts) * 100)
percentOrange = round((countOrange / numOfPts) * 100)
percentBrightOrange = round((countBrightOrange / numOfPts) * 100)
percentMauve = round((countMauve / numOfPts) * 100)

percentTotal = (percentDarkBlue + percentBlue + percentLightBlue + percentGrey + percentPink + percentPurple + percentRed + percentOrange + percentBrightOrange + percentMauve + percentWhite + percentBlack)

print "Percent Dark Blue: " + str(percentDarkBlue)
print "Percent Blue: " + str(percentBlue)
print "Percent Light Blue: " + str(percentLightBlue)
print "Percent Grey: " + str(percentGrey)
print "Percent Pink: " + str(percentPink)
print "Percent Purple: " + str(percentPurple)
print "Percent Red: " + str(percentRed)
print "Percent Orange: " + str(percentOrange)
print "Percent Bright Orange: " + str(percentBrightOrange)
print "Percent Mauve: " + str(percentMauve)
print "Percent White: " + str(percentWhite)
print "Percent Black: " + str(percentBlack)


print "Total Sum Percentage: " + str(percentTotal)