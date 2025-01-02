import urllib, os, re
import xbmc
import smtplib

path = "C:\Shell\CURVER.XWM"
f = open(path)
string = ""
while 1:
    line = f.readline()
    if not line:break
    string += line
f.close()

original = string
CURVER = original.replace(",", "")
xbmc.executebuiltin('XBMC.Skin.SetString(SysVer,' + CURVER + ')')








