import xbmc
xbmc.executebuiltin('Skin.ToggleSetting(Terminal)')
xbmc.executebuiltin('Skin.SetString(Terminal)')
xbmc.executebuiltin('$INFO[Skin.String(Terminal)]')
xbmc.executebuiltin('Skin.SetString(Terminal, )')
xbmc.executebuiltin('Skin.ToggleSetting(Terminal)')



