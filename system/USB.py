import xbmc
import time
import sys
while 1 == 1:
  try:
    with open('C:\XboxDrive.txt') as file:
        xbmc.executebuiltin('Notification(External Storage,Your removable device is ready,5000,)')
  	time.sleep(2)
	sys.exit("Error message")
  except IOError as e:
    time.sleep(3)
try:
    with open('F:\XboxDrive.txt') as file:
        xbmc.executebuiltin('Notification(External Storage,Your removable device is ready,5000,)')
	time.sleep(2)
	sys.exit("Error message")
except IOError as e:
    xbmc.executebuiltin('Dialog.Close(1)')
time.sleep(3)
sys.exit("Error message")
try:
    with open('A:\XboxDrive.txt') as file:
        xbmc.executebuiltin('Notification(External Storage,Your removable device is ready,5000,)')
	time.sleep(2)
	sys.exit("Error message")
except IOError as e:
    xbmc.executebuiltin('Dialog.Close(1)')
time.sleep(3)
sys.exit("Error message")