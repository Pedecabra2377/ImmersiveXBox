# imageDownloader.py
# Finds and downloads all images from any given URL.
# FB - 201009083
import urllib2
from os.path import basename
from urlparse import urlsplit
from BeautifulSoup import BeautifulSoup # for HTML parsing

url = " https://www.youtube.com/user/IGNentertainment/videos "  
urlContent = urllib2.urlopen(url).read()
soup = BeautifulSoup(''.join(urlContent))
imgTags = soup.findAll('img') # find all image tags

# download all images
for imgTag in imgTags:
    imgUrl = imgTag['src']
    try:
 
        imgData = urllib2.urlopen(imgUrl).read()
        fileName = basename(urlsplit(imgUrl)[2])
        output = open('C:\Assistance\Art\game1.jpg','wb')
        output.write(imgData)
        output.close()
    except:
        pass