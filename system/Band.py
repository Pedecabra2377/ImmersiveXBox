import os
import xbmc
oPipe = os.popen( "netstat -e" )
sLine = oPipe.read()
xbmc.executebuiltin('Skin.SetString(Bandwidth,' + sLine + ')')