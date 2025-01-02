import os
import xbmc
__steam__ = xbmc.getInfoLabel( '$INFO[Skin.string(SteamLocation)]' )

os.startfile(__steam__)





