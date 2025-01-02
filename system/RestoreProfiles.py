import shutil
import xbmc
import os

dest2  = xbmc.getInfoLabel( '$INFO[Skin.string(RestoreDrive)]' )
root  = os.path.join('special://logpath/userdata/') 
destination = xbmc.translatePath(root)
file1  = dest2 + 'advancedsettings.xml'
file2  = dest2 + 'favourites.xml' 
file3  = dest2 + 'guisettings.xml'
file4  = dest2 + 'LCD.xml'
file5  = dest2 + 'Profiles.xml'
file6  = dest2 + 'rssfeeds.xml'
file7  = dest2 + 'sources.xml'
if os.path.exists(destination + 'advancedsettings.xml'): os.remove(destination + 'advancedsettings.xml');
if os.path.exists(destination + 'favourites.xml'): os.remove(destination + 'favourites.xml');
if os.path.exists(destination + 'guisettings.xml'): os.remove(destination + 'guisettings.xml');
if os.path.exists(destination + 'LCD.xml'): os.remove(destination + 'LCD.xml');
if os.path.exists(destination + 'profiles.xml'): os.remove(destination + 'profiles.xml');
if os.path.exists(destination + 'rssfeeds.xml'): os.remove(destination + 'rssfeeds.xml');
if os.path.exists(destination + 'sources.xml'): os.remove(destination + 'sources.xml');
shutil.copy2(file1, destination)
shutil.copy2(file2, destination)
shutil.copy2(file3, destination)
shutil.copy2(file4, destination)
shutil.copy2(file5, destination)
shutil.copy2(file6, destination)
shutil.copy2(file7, destination)