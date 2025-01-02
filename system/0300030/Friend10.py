#-------------------------------------------------------------------------------
# Name:   	xbox.gamertag.py()
# Purpose:	To get the data from existing xbox live gamertag
# Author:	Dom DXecutioner
# Created:	06.25.2011
# Updated:	09.14.2011
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import urllib, os, re
import xbmc
from BeautifulSoup import *

# general variables
__dataPath__ = os.path.join('special://skin/system/D400040/Friend/' )

__GamerAvatarFolder__ = __dataPath__ + "/avatars/"
__GamerPictureFolder__ = __dataPath__ + "/pictures/"
__GameIconFolder__ = __dataPath__ + "/icons/"

__XbmcFriend10__ = xbmc.getInfoLabel( '$INFO[Skin.string(Friend10)]' )
__XboxGamertag__ = __XbmcFriend10__.replace(" ","%20")

	
def xebi(td):
	log( 'Skin.Setting : ' + td )
	xbmc.executebuiltin( td )

def log(msg):
	xbmc.log( 'XBox.Gamertag: ' + str( msg ), level=xbmc.LOGDEBUG )

def downloadImage(url, destfold, dest=None):
	
	log( 'IMAGE URL: ' + url )
	
	# check if folder exist; otherwise attempt to create it
	if not os.path.exists( destfold ):
		log('FOLDER DOES NOT EXIST: ' + destfold)
		os.makedirs( destfold )
		log('FOLDER CREATED: ' + destfold)
	
	# create full path w/ file name
	filename = destfold + dest
	
	try:
		# check if the file exists; if it does, there's no need to redownload; otherwise download and save
		if not os.path.isfile( filename ):
			urllib.urlretrieve(url, filename)
			log( 'DOWNLOAD COMPLETED: ' + filename )
		else:
			log( 'DOWNLOAD SKIPPED: ' + filename )
			
		return 1
			
	except:
		log( 'DOWNLOAD FAILED: ' + filename )
		return 0

def GetGTNFO():
	gamerCardHTML = ""
	
	# resolved gamercard url
	card_url = "http://live.xbox.com/" + __XboxGamertag__ + ".card"
	log('GAMERCARD URL: ' + card_url)
	
	#  open internet connection, load hmtl to memory and close connection
	wsock = urllib.urlopen( str( card_url ) )
	gamerCardHTML = wsock.read()
	wsock.close()
	log('GAMERCARD HTML: data loaded to memory; will begin querying')

	# process gamer's avatar data
	downloadImage( "http://avatar.xboxlive.com/avatar/" + __XboxGamertag__ + "/avatar-body.png", xbmc.translatePath( __GamerAvatarFolder__ ), __XbmcFriend10__ + '.png' )

	
	# get the info
	soupStrainer  = SoupStrainer( "body" )
	beautifulSoup = BeautifulSoup( gamerCardHTML, soupStrainer )

	# process gamer's profile data
	xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Score,' + beautifulSoup.find( "div", { "id" : "Gamerscore" } ).text + ')')
	#xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Location,' + beautifulSoup.find( "div", { "id" : "Location" } ).text )	
	#xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Motto,' + beautifulSoup.find( "div", { "id" : "Motto" } ).text
	#xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Name,' + beautifulSoup.find( "div", { "id" : "Name" } ).text
	#xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Bio,' + beautifulSoup.find( "div", { "id" : "Bio" } ).text
	xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.Picture,' + __GamerPictureFolder__ + __XbmcFriend10__ + '.png)' )
	downloadImage( beautifulSoup.find( "img", { "id" : "Gamerpic" } )[ "src" ],  xbmc.translatePath( __GamerPictureFolder__ ), __XbmcFriend10__ + '.png' )
	
	# find all list elements of the html, which is where the recently played games data is stored
	list_gamesPlayed = beautifulSoup.findAll ( "li" )
	
	# reset count
	count = 0
	
	# list to shorten code below
	d = [ 'Title', 'LastPlayed', 'EarnedGamescore', 'AvailableGamescore', 'EarnedAchievements', 'AvailableAchievements', 'PercentComplete' ]

	# move thru each game item (div) and get appropriate info
	for game in list_gamesPlayed:
		
		# commense count
		count = count + 1
		
		log ( 'Recently Played Gamed - 0' + str( count ) + ' ========================================')
		print game.text
		# get game's title id to be used as the name of the image after download
		gameTitleID = re.compile('=(.+?)&',re.IGNORECASE).findall( game.a[ "href" ] )
	
		# move thru each data section in the game item [one <a> and the rest <span>]
		for n in range(len( game.findChildren() ) -1 ):
			if n > 0: xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.RecentlyPlayed.' + d[ n - 1 ] + '.' + str( count ) + ',' + game.findChildren( 0 )[ n + 1 ].text + ')' )

		# download game title image
		downloadImage( game.findChildren( 0 )[ 1 ][ "src" ], xbmc.translatePath( __GameIconFolder__ ), gameTitleID[ 0 ] + '.jpg' )
		xebi( 'XBMC.Skin.SetString(XboxLive.Gamer.RecentlyPlayed.Icon.' + str( count ) + ',' + __GameIconFolder__ + gameTitleID[ 0 ] + '.jpg)' )
		
	return

global mode
mode = -1

def main():
	log( '==================================================' )
	# test for internet coXnnection
	#online = onlineChecker()
	# if internet connection is available, let us get the GamerCard info
	#if online == 1:
	nfo = GetGTNFO()
	

if __name__ == '__main__':
	main()