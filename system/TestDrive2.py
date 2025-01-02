import os
import xbmc
import time
import sys
PATH = "/storage/"
while True:
	if not os.path.isfile(PATH + 'Drive.txt') and os.access(PATH + 'Drive.txt', os.R_OK):
  		xbmc.executebuiltin('RunScript(special://skin/system/TestDrive.py)')
  	sys.exit("Error message")
  	time.sleep(5)