import xbmc
import datetime
dt=datetime.datetime.now()
mon=12-dt.month
day=25-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game0Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=11-dt.month
day=18-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game1Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=11-dt.month
day=14-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game2Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=12-dt.month
day=02-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game3Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=01-dt.month
day=30-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game4Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=02-dt.month
day=10-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game5Countdown,' + str(count) + ')')

dt=datetime.datetime.now()
mon=03-dt.month
day=20-dt.day
count = str(mon) + ' Months ' + str(day) + ' Days '
xbmc.executebuiltin('XBMC.Skin.SetString(Game6Countdown,' + str(count) + ')')
