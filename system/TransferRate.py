import socket
import time
from urllib2 import urlopen, URLError, HTTPError
from datetime import datetime

startTime = datetime.now()

socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://live.xbox.com'
try :
    response = urlopen( url )
except HTTPError, e:
    Timing = (datetime.now()-startTime)
    xbmc.executebuiltin('Skin.SetString(Transfer,' + Timing + ')')
except URLError, e:
    Timing = (datetime.now()-startTime)
    xbmc.executebuiltin('Skin.SetString(Transfer,' + Timing + ')')
else :
    html = response.read()
    Timing = (datetime.now()-startTime)
    xbmc.executebuiltin('Skin.SetString(Transfer,' + str(Timing) + ')')
    # do something, turn the light on/off or whatever