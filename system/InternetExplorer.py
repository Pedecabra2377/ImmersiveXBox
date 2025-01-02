import os
import xbmc
__steam__ = xbmc.getInfoLabel( '$INFO[Skin.string(IELocation)]' )

os.startfile(__steam__)





