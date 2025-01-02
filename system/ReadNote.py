import urllib, os, re
import xbmc
import smtplib

path = xbmc.getInfoLabel( '$INFO[Skin.string(NoteFile)]' )
f = open(path)
string = ""
while 1:
    line = f.readline()
    if not line:break
    string += line
f.close()

original = string
removed = original.replace(",", "")
xbmc.executebuiltin('XBMC.Skin.SetString(NotepadText,' + removed + ')')








