import glob
import shutil
import os
import xbmc

backupfolder = os.path.join('special://skin/system/backup/addon_data') 
src_dir = xbmc.translatePath(backupfolder)

datafolder = os.path.join('special://home/userdata/addon_data') 
dst_dir = xbmc.translatePath(datafolder)

shutil.copy(dst_dir, src_dir)

