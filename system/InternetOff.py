import os
import subprocess
startupinfo = subprocess.STARTUPINFO()
startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
subprocess.call('ipconfig /release', startupinfo=startupinfo)