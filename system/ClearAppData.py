import os
import xbmc
import shutil


cache  = os.path.join('special://home/userdata/addon_data/') 
path = xbmc.translatePath(cache)


shutil.rmtree(path)






