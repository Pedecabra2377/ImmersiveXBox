import os
import xbmc
__steam__ = xbmc.getInfoLabel( '$INFO[Skin.string(App1location)]' )

os.startfile(__steam__)





