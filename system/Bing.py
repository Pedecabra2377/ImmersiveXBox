#!/usr/bin/python
import urllib2
from urllib import urlopen
from datetime import date
import re
import sys

def download(url, filename):
    try:
        with urlopen(url) as instream, open(filename, 'wb') as outfile:
            outfile.write(instream.read())
    except Exception as e:
        print(f"Erro ao baixar: {e}")

if __name__ == "__main__":
    dest = 'cache/Bing_img.jpg'

    doc = urllib2.urlopen('http://www.bing.com')
    content = doc.read()

    result = re.search(r"g_img={url:'([^']*)", content)
    if result:
        url_img = 'http://www.bing.com' + result.group(1).replace('\\', '')
        download(url_img, dest)
    else:
        print("Não encontrou a URL da imagem")