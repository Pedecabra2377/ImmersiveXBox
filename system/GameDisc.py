import os
import xbmc
__Disc__ = xbmc.getInfoLabel( '$INFO[Skin.string(GameDiscLocation)]' )

os.startfile(__Disc__)





