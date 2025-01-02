#-------------------------------------------------------------------------------
# Name:   	xbox.gamertag.py()
# Purpose:	To get the data from existing xbox live gamertag
# Author:	Dom DXecutioner
# Created:	06.25.2011
# Updated:	11.08.2014
#-------------------------------------------------------------------------------
#!/usr/bin/env python

import os, urllib, datetime
import xbmc
from BeautifulSoup import *
from traceback import print_exc

#__XbmcCurrentUser__ = "Major Nelson"
__XbmcCurrentUser__ = xbmc.getInfoLabel( '$INFO[Skin.string(GTAG)]' )
XBLGamertag 		= __XbmcCurrentUser__.replace(" ","%20")

BASE_DIR_CACHE			= xbmc.translatePath("special://profile/script_data/script.xboxlive.gamercard/")
BASE_DIR_CACHE_PICS 	= os.path.join( BASE_DIR_CACHE, "pics" )
BASE_DIR_CACHE_TILES 	= os.path.join( BASE_DIR_CACHE, "tiles" )
BASE_DIR_CACHE_AVATARS 	= os.path.join( BASE_DIR_CACHE, "avatars" )

'''
	XBLGamercard.Gamertag
	XBLGamercard.Picture
	XBLGamercard.Avatar
	
	XBLGamercard.Score
	XBLGamercard.Location
	XBLGamercard.Motto
	XBLGamercard.Bio
	
	XBLGamercard.RecentlyPlayed.Title.#
	XBLGamercard.RecentlyPlayed.Icon.#
	XBLGamercard.RecentlyPlayed.LastPlayed.#
	XBLGamercard.RecentlyPlayed.EarnedGamerscore.#
	XBLGamercard.RecentlyPlayed.AvailableGamerscore.#
	XBLGamercard.RecentlyPlayed.EarnedAchievements.#
	XBLGamercard.RecentlyPlayed.AvailableAchievements.#
	XBLGamercard.RecentlyPlayed.PercentageComplete.#

	XBLGamercard.LastUpdated
'''

def xebi(td):
	log( "ExecuteBuiltin - Skin.Setting : " + td )
	xbmc.executebuiltin( td )

def log(msg):
	#pass
	print "|| script.xboxlive.gamercard-::-%s" % msg
	#xbmc.log( "|| script.xboxlive.gamercard-::-" + str( msg ), level=xbmc.LOGDEBUG )
		
def download(url, destination, name=None):
	_s = "download--> "
	log( _s + "url :" + url )
	log( _s + "dest:" + destination )
	log( _s + "name:" + name )
	
	# check if folder exist; otherwise attempt to create it
	if not os.path.exists( destination ):
		log( _s + "destination does not exists, will attempt to create..." )
		os.makedirs( destination )
		log( _s + "destination created..." )
	# create full path w/ file name
	filename = os.path.join( destination, name )
	
	try:
		# check if the file exists; if it does, there's no need to redownload; otherwise download and save
		if not os.path.isfile( filename ):
			urllib.urlretrieve( url, filename )
			log( _s + "success!" )
		else:
			log( _s + "skipped! filed exists..." )
		return 1
			
	except:
		log( _s + "failed something happened..." )
		return 0

def get_gamercard():
	_s = "get_gamercard--> "
	
	# resolved gamercard url
	url_gamercard = "http://live.xbox.com/" + XBLGamertag + ".card"
	log( _s + "url: " + url_gamercard )
	
	try:
		# open internet connection, load hmtl to memory and close connection
		#request		= urllib2.Request( url_gamercard )
		#request.add_header( "User-agent", "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)" )
		#response	= urllib2.urlopen( request ).read()
		
		request		= urllib.urlopen( url_gamercard )
		response 	= request.read()
		request.close()
		
		gamercard	= BeautifulSoup( response )
		# quick clean up
		response 	= ""
		request		= ""
		# process gamer's profile data
		xebi( "Skin.SetString(XboxLive.Gamer.Score," 		+ gamercard.find("div",{"id" : "Gamerscore"}).text + ")" )
		xebi( "Skin.SetString(XboxLive.Gamer.Location," 	+ gamercard.find("div",{"id" : "Location"}).text + ")" )	
		xebi( "Skin.SetString(XboxLive.Gamer.Motto," 		+ gamercard.find("div",{"id" : "Motto"}).text  + ")" )
		xebi( "Skin.SetString(XboxLive.Gamer.Name," 		+ gamercard.find("div",{"id" : "Name"}).text + ")" )
		xebi( "Skin.SetString(XboxLive.Gamer.Bio," 		+ gamercard.find("div",{"id" : "Bio"}).text + ")" )
		# compose avatar + picture url
		url_avatar	= "http://avatar.xboxlive.com/avatar/" + XBLGamertag + "/avatar-body.png"
		url_picture	= "http://avatar.xboxlive.com/avatar/" + XBLGamertag + "/avatarpic-l.png"
		# download avatar + picture
		download( url_avatar, 	BASE_DIR_CACHE_AVATARS, __XbmcCurrentUser__ + ".png" )
		download( url_picture, 	BASE_DIR_CACHE_PICS, 	__XbmcCurrentUser__ + ".png" )
		# set xbmc strings
		xebi( "Skin.SetString(XboxLive.Gamer.Picture," 	+ os.path.join( BASE_DIR_CACHE_PICS, 	__XbmcCurrentUser__ + ".png)") + ")" )
		xebi( "Skin.SetString(XboxLive.Gamer.Avatar," 	+ os.path.join( BASE_DIR_CACHE_AVATARS, __XbmcCurrentUser__ + ".png)") + ")" )
		# initialize count variable
		count = 0
		# move thru each game item (li) and get appropriate info
		for game in gamercard.findAll( "li" ):
			# begin count
			count += 1
			# get game's title id to be used as the name of the image after download			
			href_titleID 	= game.a[ "href" ]
			posx 			= href_titleID.find( "titleId=" ) + 8
			posl 			= posx + 10
			tile_name 		= href_titleID[ posx:posl ] + ".jpg"
			tile_url 		= game.findChildren(0)[1][ "src" ]
			# download game title image
			download( tile_url, BASE_DIR_CACHE_TILES, tile_name )
			# store game info
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.Title." 					+ str(count) + "," + game.find("span",{"class":"Title"}).text.encode("utf-8") + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.LastPlayed." 				+ str(count) + "," + game.find("span",{"class":"LastPlayed"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.EarnedGamerscore." 		+ str(count) + "," + game.find("span",{"class":"EarnedGamerscore"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.AvailableGamerscore."		+ str(count) + "," + game.find("span",{"class":"AvailableGamerscore"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.EarnedAchievements."		+ str(count) + "," + game.find("span",{"class":"EarnedAchievements"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.AvailableAchievements."	+ str(count) + "," + game.find("span",{"class":"AvailableAchievements"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.PercentageComplete." 		+ str(count) + "," + game.find("span",{"class":"PercentageComplete"}).text + ")" )
			xebi( "Skin.SetString(XboxLive.Gamer.RecentlyPlayed.Icon." 					+ str(count) + "," + os.path.join( BASE_DIR_CACHE_TILES, tile_name ) + ")" )
		# finally, add scrape date [ALT: now.isoformat()] | now.strftime("%Y-%m-%d %H:%M")
		now = datetime.datetime.now()
		xebi( "Skin.SetString(XBLGamercard.LastUpdated,"+ str(now.strftime("%Y-%m-%d %H:%M")) + ")" )
		return True
		
	except:
		print_exc()
		log( _s + "wft!... something went wrong..." )
		return False
		
		
global mode
mode = -1

def main():
	log( "==================================================" )
	if get_gamercard():
		xebi( "XBMC.Notification(XBox Live: Gamertag," + __XbmcCurrentUser__ + " Update Complete!)" )
	else:
		xebi( "XBMC.Notification(XBox Live: Gamertag," + __XbmcCurrentUser__ + " Update Failed!)" )
		
if __name__ == '__main__':
	main()