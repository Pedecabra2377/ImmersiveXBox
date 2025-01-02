import socket
from urllib2 import urlopen, URLError, HTTPError

socket.setdefaulttimeout( 23 )  # timeout in seconds

url = 'http://video.xbox.com'
try :
    response = urlopen( url )
except HTTPError, e:
    xbmc.executebuiltin('Skin.SetString(VideoStatus, DOWN:' + str(e.code) +')')
except URLError, e:
    xbmc.executebuiltin('Skin.SetString(VideoStatus, DOWN:' + str(e.reason) +')')
else :
    html = response.read()
    xbmc.executebuiltin('Skin.SetString(VideoStatus, UP)')
    # do something, turn the light on/off or whatever