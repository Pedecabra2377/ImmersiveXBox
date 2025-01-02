import os
import xbmc
__steam__ = xbmc.getInfoLabel( '$INFO[Skin.string(App2location)]' )

os.startfile(__steam__)





