import urllib, os, re
import xbmc
import smtplib

logFolder  = os.path.join('special://logpath') 
path = xbmc.translatePath(logFolder)
f = open(path + '/' + 'xbmc.log')
string = ""
xbmc.executebuiltin('Skin.SetString(LogXBMC, )')
while 1:
    line = f.readline()
    if not line:break
    string += line
f.close()

original = string
removed = original.replace(",", "")
xbmc.executebuiltin('XBMC.Skin.SetString(LogXBMC,' + removed + ')')
xbmc.executebuiltin('ActivateWindow(5523)')







