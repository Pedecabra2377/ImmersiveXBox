import xbmcgui
window = xbmcgui.Window(xbmcgui.getCurrentWindowId())
window.setProperty('Browser.URL', 'https://www.bing.com')
window.doModal()