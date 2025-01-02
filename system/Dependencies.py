import os
import xbmc
import zipfile

__addondir__ = xbmc.getInfoLabel( '$INFO[Skin.string(addondir)]' )


fh = open('Dependencies.zip', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outpath = "__addondir__"
    z.extract(name, outpath)
fh.close()


