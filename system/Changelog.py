import urllib, os, re
import xbmc
import smtplib
xbmc.executebuiltin('XBMC.Skin.SetString(TermsXBMC, )')
logFolder  = os.path.join('special://skin/system/Update/') 
path = xbmc.translatePath(logFolder)
f = open(path + '/' + 'Update.txt')
string = ""
while 1:
    line = f.readline()
    if not line:break
    string += line
f.close()

original = string
removed = original.replace(",", "")
xbmc.executebuiltin('XBMC.Skin.SetString(TermsXBMC,' + removed + ')')
xbmc.executebuiltin('xbmc.activatewindow(560)')








