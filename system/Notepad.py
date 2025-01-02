
path = xbmc.getInfoLabel( '$INFO[Skin.string(NotesName)]' )
f = open("special://userdata/" + path + ".txt", "a");
print f

value = xbmc.getInfoLabel( '$INFO[Skin.string(NotepadText)]' )
myString = str(value)

f.write(myString)

f.close()