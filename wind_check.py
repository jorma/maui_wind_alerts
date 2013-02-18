# This Python script was created by Jorma to send me an email alert if it looks like tomorrow is going to be a calm day around Lahaina. See the ReadMe for more info

import os, sys
from PIL import Image
import subprocess
import smtplib
import email.utils
from email.mime.text import MIMEText

totalBlue = 0

def main():
	# Uncomment line below to download image files
	subprocess.call(['./download.sh'])
	
	images = ["images/wind011.png","images/wind012.png","images/wind013.png","images/wind014.png","images/wind015.png","images/wind016.png","images/wind017.png","images/wind018.png","images/wind019.png","images/wind020.png"]
	
		
	for x in range(0, 10):
		im = Image.open(images[x])
		windCheck(im)
	
	print "Total Blue: " + str(totalBlue)
	
	
	if totalBlue >= 5:
		SendEmail("Jorma","aloha@jorma.com","Looks like it is going to be a calm day in Lahaina!")
	else:
		pass
		
	
def windCheck(imageName):
	numOfPts = 6474.0 # this number is from the number of coordinate points in the windArea list
	countBlue = 0
	global totalBlue
	windArea=[]
	
	for line in open( "windArray_complete.txt", "r" ).readlines():
			line = line.replace('\n', '')
			windArea.append(line)
	
	for x in range(0, 6474):
		
		coordinate = windArea[x]
		coordinatePts = coordinate.split(",")

		x = int(coordinatePts[0])
		y = int(coordinatePts[1])

		pix = imageName.load()

		color = pix[x,y]
		
	
		if color == (0,0,255): #dark blue
			countBlue += 1
	
		elif color == (63, 63, 255): # blue
			countBlue += 1
			
		else:
			pass

	percentBlue = round((countBlue / numOfPts) * 100)

	print "Percent Blue: " + str(percentBlue)
	
	if (percentBlue >= 50):
		totalBlue += 1
	else:
		pass

	
def SendEmail(name,emailAddr,emailBody):
	print "********Send Email*********"
	msg = MIMEText('Aloha -\n\n ' + emailBody) 
	msg['To'] = email.utils.formataddr((name, emailAddr))
	msg['From'] = email.utils.formataddr(('Jorma', 'jorma@minustide.net'))
	msg['Subject'] = 'Email Alert: Calm day in Lahaina'

	conn = smtplib.SMTP('mail.minustide.net')
	conn.login('jorma@minustide.net', 'xxxxxxxx')
	conn.sendmail(msg['From'], msg['To'], msg.as_string())
	conn.quit()

if __name__ == '__main__':
	main()