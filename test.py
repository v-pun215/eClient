import os, getpass, wget, shutil
from elevate import elevate
usr_accnt = getpass.getuser()
elevate()
print("Creating shortcut...")
#wget.download("https://eclient-libs.earthsoft.me/shortcut.exe", bar=wget.bar_adaptive)
#shutil.move('shortcut.exe', 'C:\\Windows\\System32'.format(usr_accnt))
google = "C:\\Users\\{}\\AppData\\Roaming\\eClient".format(usr_accnt)
os.chdir(r"C:\\Users\\{}\\Desktop\\ ".format(usr_accnt))
os.system(f"shortcut.exe /F:eClient.lnk /A:C /T:{google}\\eclient.pyw /W:{google} /I:{google}\\mc.ico")