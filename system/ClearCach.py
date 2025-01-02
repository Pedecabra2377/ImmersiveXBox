import os
import xbmc
import shutil


cache  = os.path.join('special://home/userdata/addon_data/script.extendedinfo/') 
path = xbmc.translatePath(cache)


shutil.rmtree(path)
xbmc.executebuiltin('Notification(     ,Done,00:59,)')





