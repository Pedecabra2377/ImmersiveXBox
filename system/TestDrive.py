import os
import xbmc
import time
import sys
PATH = "/storage/"
while True:
  if os.path.isfile(PATH + 'Drive.txt') and os.access(PATH + 'Drive.txt', os.R_OK):
  	xbmc.executebuiltin('Notification(Armazenamento,Seu armazenamento está pronto para uso,00:59,)')
  xbmc.executebuiltin('RunScript(special://skin/system/TestDrive2.py)')
  sys.exit("Error message")