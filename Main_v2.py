import os, sys
from PIL import Image
import urllib2, urllib

# black is 255, 255, 255
# white is 0, 0, 0

# 0 blue is 0, 0, 255
# 0 - 5 blue is 63, 63, 255
# 5 - 10 light blue is 175, 191, 255
# 10 - 15 grey is 223, 215, 255
# 15 - 20 pink is 234, 172, 255
# 20 - 25 purple is 187, 84, 191
# 25 - 30 red is 191, 25, 89

# Uncomment two lines below to get file
#wgetCommand = "/opt/local/bin/wget -O /Users/jorma/Code/maui_wind_python/images/wind010.png http://weather.mhpcc.edu/wrf/maui2/wind010.png"
#os.system(wgetCommareplace("M", "")

windArea=[]
for line in open( "windArray_complete.txt", "r" ).readlines():
		line = line.replace('\n', '')
		windArea.append( line )

numOfPts = len(windArea)

print numOfPts

numOfPts = numOfPts + 0.0
print windArea

count = 0
im = Image.open("images/wind010.png")

for x in range(0, 434):
	coordinate = windArea[x]

	coordinatePts = coordinate.split(",")

	x = int(coordinatePts[0])
	y = int(coordinatePts[1])

	pix = im.load()

	color = pix[x,y]

	if color == (0,0,255):
		#print "blue"
		count += 1
	
	elif color == (191, 25, 89): # blue
		#print "blue"
		count += 1
		
	elif color == (191, 25, 89): # light blue
		#print "blue"
		count += 1
			
	else:
		#print "not blue"
		print color

print "count is: " + str(count)
print "numOfPts is: " + str(numOfPts)

percentBlue = round((count / numOfPts) * 100)

print "Percent Blue: " + str(percentBlue)