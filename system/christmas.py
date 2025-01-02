from time import sleep
import xbmc
while True:
    import datetime
    dt=datetime.datetime.now()
    mon=12-dt.month
    day=25-dt.day
    hr=23-dt.hour
    mn=60-dt.minute
    sec=60-dt.second
    count = str(mon) + ' Months ' + str(day) + ' Days ' + str(hr) + ' Hours ' + str(mn) + ' Minutes ' + str(sec) + ' Seconds '
    xbmc.executebuiltin('XBMC.Skin.SetString(NotepadText,' + str(count) + ')')
    sleep(1)