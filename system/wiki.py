import xbmc
import urllib
import urllib2
from BeautifulSoup import BeautifulSoup

article= "Albert Einstein"
article = urllib.quote(article)

opener = urllib2.build_opener()
opener.addheaders = [('User-agent', 'Mozilla/5.0')] #wikipedia needs this

resource = opener.open("http://en.wikipedia.org/wiki/" + article)
data = resource.read()
resource.close()
soup = BeautifulSoup(data)
string = soup.find('div',id="bodyContent").p
xbmc.executebuiltin('XBMC.Skin.SetString(NotepadText,' + str(string) + ')')
