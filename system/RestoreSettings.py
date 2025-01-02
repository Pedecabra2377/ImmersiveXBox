import glob
import shutil
import os
import xbmc
import time

backupfolder  = os.path.join('special://skin/system/backup/addon_data/') 
src_dir = xbmc.translatePath(backupfolder)

datafolder  = os.path.join('special://home/userdata/addon_data/') 
dst_dir = xbmc.translatePath(datafolder)

shutil.copy(src_dir, dst_dir)

time.sleep(60)

shutil.rmtree(src_dir)