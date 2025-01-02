import os
import xbmc
__chrome__ = xbmc.getInfoLabel( '$INFO[Skin.string(chrome)]' )


import subprocess
subprocess.call([__chrome__, '--kiosk', 'https://www.bing.com/search?q='])



