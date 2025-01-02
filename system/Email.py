import smtplib
 
to = xbmc.getInfoLabel( '$INFO[Skin.string(EmailTo)]' )
gmail_user = xbmc.getInfoLabel( '$INFO[Skin.string(MyEmail)]' )
gmail_pwd = xbmc.getInfoLabel( '$INFO[Skin.string(MyPassword)]' )
msg = xbmc.getInfoLabel( '$INFO[Skin.string(MyMessage)]' )
sub = xbmc.getInfoLabel( '$INFO[Skin.string(MySubject)]' )
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



