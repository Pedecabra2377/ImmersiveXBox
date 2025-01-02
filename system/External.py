import os
import os.path
import xbmc
import time

    #This is the drive that the script will check for
PATH = "C:\\XboxDrive.txt"

   #This will put everything in to a loop
while True:
 def printme( str ):
    #This will check the drive and see if the Drive file is available
    #If the file exists it will notify the user saying the drive is mounted
      if os.path.isfile(PATH):
       xbmc.executebuiltin('Notification(External storage,Your external drive is ready to use,00:59,)')
      time.sleep(5)
      return False 
    #If the drive isn't mounted or file isn't available then it will search again
printme();
while False:
  def printme2( str ):
   #This will make sure that the drive is mounted 
    #When unmounted it will then watch to see if it is mounted again
    if not os.path.isfile(PATH):
     time.sleep(5) 
     return True
    #Sleep for a few seconds to lower CPU usage
printme2();