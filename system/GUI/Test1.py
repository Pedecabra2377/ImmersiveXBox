import urllib, sys
def savepage(url = "http://www.xbox.com/en-GB/#fbid=lqvFb1IO9j9", dir = 'C:\Assistance\./'):
	if not url:return
src = urllib.urlopen(url).read()
tags = src.split('<img')
source = tags[0]
for tag in tags[1:]:
	try:
	href = ''
escape = False
quote = ''
s = tag[tag.index('src'):]
after = s[s.index('>'):]
s = s[Confused.index('>')]
for c in s:
if quote == '':
if c in ('"',"'"):quote = c
else:
if c == quote:
if escape:
href += c
escape = False
else:
break
elif c == '\\':
if escape:
href += c
escape = not escape
else:
href += c
except:
pass
print href
n = href.split('/')[-1]
f = file(dir+n,'wb')
f.write(urllib.urlopen(urllib.basejoin(url,href)).read());f.close()
source += '<img'+n.join(tag.split(href))
n = url.split('/')[-1]
if not n:n = 'index'
f = file(dir+n,'w')
f.write(source)
f.close()

if __name__=="__main__":savepage(*sys.argv[1:])