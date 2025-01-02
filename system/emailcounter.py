import imaplib
import xbmc
username = '$INFO[Skin.String(Email)]'
password = '$INFO[Skin.String(MyPassword)]'
mailbox = 'INBOX'
mailserver = 'imap.gmail.com'
port = '993'
server = imaplib.IMAP4_SSL(mailserver,port)
server.login(username,password)
server.select(mailbox)
data = str(server.status(mailbox, '(MESSAGES UNSEEN)'))
tokens = data.split()
print tokens[5].replace(')\'])','')
xbmc.executebuiltin('XBMC.Skin.SetString(msgcount,' + tokens[5].replace(')\'])','') + ')')
server.close()
server.logout()