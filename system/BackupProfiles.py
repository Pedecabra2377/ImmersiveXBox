import shutil
import xbmc
import os

file1  = os.path.join('special://logpath/userdata/advancedsettings.xml') 
data1 = xbmc.translatePath(file1)
file2  = os.path.join('special://logpath/userdata/favourites.xml') 
data2 = xbmc.translatePath(file2)
file3  = os.path.join('special://logpath/userdata/guisettings.xml') 
data3 = xbmc.translatePath(file3)
file4  = os.path.join('special://logpath/userdata/LCD.xml') 
data4 = xbmc.translatePath(file4)
file5  = os.path.join('special://logpath/userdata/Profiles.xml') 
data5 = xbmc.translatePath(file5)
file6  = os.path.join('special://logpath/userdata/rssfeeds.xml') 
data6 = xbmc.translatePath(file6)
file7  = os.path.join('special://logpath/userdata/sources.xml') 
data7 = xbmc.translatePath(file7)
dest  = xbmc.getInfoLabel( '$INFO[Skin.string(BackupDrive)]' )
if not os.path.exists(dest + 'XboxSystemOS'): os.mkdir(dest + 'XboxSystemOS');
newdest = dest + 'XboxSystemOS' + '/'
if not os.path.exists(newdest + 'BackupData'): os.mkdir(newdest + 'BackupData');
newdest2 = newdest + 'BackupData' + '/'
if os.path.exists(newdest2 + 'ProfileRoot'): shutil.rmtree(newdest2 + 'ProfileRoot');
if not os.path.exists(newdest2 + 'ProfileRoot'): os.mkdir(newdest2 + 'ProfileRoot');
destination = newdest2 + 'ProfileRoot' + '/'
shutil.copy2(data1, destination)
shutil.copy2(data2, destination)
shutil.copy2(data3, destination)
shutil.copy2(data4, destination)
shutil.copy2(data5, destination)
shutil.copy2(data6, destination)
shutil.copy2(data7, destination)