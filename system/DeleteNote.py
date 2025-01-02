

import os

path = xbmc.getInfoLabel( '$INFO[Skin.string(NoteFile)]' )
os.remove(path)
