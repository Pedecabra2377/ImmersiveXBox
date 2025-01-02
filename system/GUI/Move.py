import glob
import shutil
import os
import time
time.sleep(3)
src_dir = "C:/1"
dst_dir = "C:/Assistance/Test1"
for jpgfile in glob.iglob(os.path.join(src_dir, "*.jpg")):
    shutil.copy(jpgfile, dst_dir)