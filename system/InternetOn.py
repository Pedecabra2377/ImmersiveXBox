import os
import subprocess
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.call('ipconfig /renew', startupinfo=startupinfo)