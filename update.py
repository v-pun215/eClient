import os
import time
import platform
import getpass, webbrowser
import time
import wget
import shutil,requests
from pathlib import Path
currn_dir = os.getcwd()
val = False
response = requests.get("https://api.github.com/repos/v-pun215/eClient/releases/latest")
lv = response.json()["name"]
print("Upgrading to eClient {}".format(lv))
os.mkdir("bkp")
#shutil.move('settings.json', 'bkp')
if os.path.exists("\\.minecraft"):
    val = True
    shutil.move('\\.minecraft', 'bkp')
else:
    pass
wget.download("https://libs-pi.vercel.app/eclient.zip", bar=wget.bar_adaptive)
os.remove('yeah.cmd')
os.remove('val.txt')
os.remove('speedtracker.py')
os.remove('requirements.txt')
os.remove('mc.ico')
os.remove('icon.ico')
os.remove('eclient.pyw')
os.remove('main.py')
os.remove('main.bat')
os.remove('password.txt')
os.remove('Install-Font.ps1')
os.remove('light.txt')
os.remove('installer.log')
os.remove('install.py')
os.remove('install.nsi')
os.remove('downloadMods.py')
os.remove('check.py')
os.remove('check.txt')
os.remove('authlib-injector.log')
path = Path("img")
path2 = Path("fonts")
path3 = Path("authlib")
path4 = Path("__pycache__")
path5 = Path("bkp")


shutil.rmtree(path)
shutil.rmtree(path2)
shutil.rmtree(path3)
shutil.rmtree(path4)

print("Extracting eClient...")
filename3 = wget.detect_filename("https://eclient-libs.earthsoft.me/eclient.zip")
os.system('powershell -Command "Expand-Archive -LiteralPath eclient.zip -DestinationPath Update"')
path6 = Path("Update")

source = "{}/Update/".format(currn_dir)
destination = "{}".format(currn_dir)
  
# code to move the files from sub-folder to main folder.
files = os.listdir(source)
for file in files:
    file_name = os.path.join(source, file)
    shutil.move(file_name, destination)
print("Files Moved")

os.system("del eclient.zip")
if val == True:
    shutil.move('bkp\\.minecraft', '\\.minecraft')
print("eClient updated to {}".format(lv))
shutil.rmtree(path5)
shutil.rmtree(path6)
print("Thank you for using eClient.")
