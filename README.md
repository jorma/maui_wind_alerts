maui_wind_python
================

Python script for pulling wind data from Maui @2km website - http://weather.mhpcc.edu/wrf/maui2/wind.html

Script Details:

	- Downloads 10 most recent images from http://weather.mhpcc.edu/wrf/maui2/wind.html
		(7am - 4pm)
		
	- For specified Lahaina area (see misc/wind_area.png) the script checks each pixel to see if it is blue.
	
	- If 5 or more of the 10 images have 50% or more 'blue' (less than 5mph wind), an email alert is sent.


