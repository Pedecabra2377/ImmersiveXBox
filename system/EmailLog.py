import urllib, os, re
import xbmc
import smtplib

logFolder  = os.path.join('special://logpath') 
path = xbmc.translatePath(logFolder)
f = open(path + '/' + 'xbmc.log')
string = ""
while 1:
    line = f.readline()
    if not line:break
    string += line
f.close()
xbmc.executebuiltin('XBMC.Skin.SetString(LogSubject, Olá, aqui está o meu registro.)')
xbmc.executebuiltin('XBMC.Skin.SetString(LogEmail, playerthreeiii@gmail.com)')



to = xbmc.getInfoLabel( '$INFO[Skin.string(LogEmail)]' )
gmail_user = xbmc.getInfoLabel( '$INFO[Skin.string(MyEmail)]' )
gmail_pwd = xbmc.getInfoLabel( '$INFO[Skin.string(MyPassword)]' )
msg = string
sub = xbmc.getInfoLabel( '$INFO[Skin.string(LogSubject)]' )
server = xbmc.getInfoLabel( '$INFO[Skin.string(EmailServer)]' )
port = xbmc.getInfoLabel( '$INFO[Skin.string(ServerPort)]' )
smtpserver = smtplib.SMTP(server,port)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(gmail_user, gmail_pwd)
header = 'To:' + to + '\n' + 'From: ' + gmail_user + '\n' + 'Subject:' + sub + '\n'
print header
msg = header + '\n' + msg + '\n\n'
smtpserver.sendmail(gmail_user, to, msg)
print 'done!'
smtpserver.close()









