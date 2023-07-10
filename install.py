import os
import time
import platform
import getpass
import time
import wget
import shutil
from elevate import elevate
elevate()


print("-eClient Setup-")
print("Getting necessary stuff...")
time.sleep(2)
os_name = platform.platform()
usr_accnt = getpass.getuser()
currn_dir = os.getcwd()
py_ver = platform.python_version()
def end():
    print("Thank you for choosing eClient.")
    print("Setup will now start installing eClient.")
    dire = input("Where do you want to install eClient? (Default: C:\\Users\\{}\\AppData\\Roaming\\eClient): ".format(usr_accnt))
    if dire == "":
        print("Installing eClient to default directory...")
        os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\".format(usr_accnt))
        wget.download("https://eclient-libs.earthsoft.me/eclient.zip", bar=wget.bar_adaptive)
        filename3 = wget.detect_filename("https://eclient-libs.earthsoft.me/eclient.zip")
        os.system('powershell -Command "Expand-Archive -LiteralPath eclient.zip -DestinationPath eClient"')
        os.system("del eclient.zip")
        wget.download("https://eclient-libs.earthsoft.me/Install-Font.ps1", bar=wget.bar_adaptive)
        wget.download("https://eclient-libs.earthsoft.me/command.py", bar=wget.bar_adaptive)
        filename5= wget.detect_filename("https://eclient-libs.earthsoft.me/command.py")
        filename4 = wget.detect_filename("https://eclient-libs.earthsoft.me/Install-Font.ps1")
        os.system('move "Install-Font.ps1" "eClient/fonts"')
        os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\eClient\fonts".format(usr_accnt))
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Regular.otf")
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Bold.otf")
        os.chdir(r"C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\".format(usr_accnt))
        os.system("del command.py")
        os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\".format(usr_accnt))
        shutil.move('command.py', 'C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\'.format(usr_accnt))
        print("eClient installed.")
        print("Creating shortcut...")
        wget.download("https://eclient-libs.earthsoft.me/shortcut.exe", bar=wget.bar_adaptive)
        shutil.move('shortcut.exe', 'C:\\Windows\\System32'.format(usr_accnt))
        google = "C:\\Users\\{}\\AppData\\Roaming\\eClient".format(usr_accnt)
        os.chdir(r"C:\\Users\\{}\\Desktop\\ ".format(usr_accnt))
        os.system(f"shortcut.exe /F:eClient.lnk /A:C /T:{google}\\eclient.pyw /W:{google} /I:{google}\\mc.ico")
    elif not dire == "":
        print("Installing eClient to {}...".format(dire))
        os.chdir(dire)
        wget.download("https://eclient-libs.earthsoft.me/eclient.zip", bar=wget.bar_adaptive)
        filename3 = wget.detect_filename("https://eclient-libs.earthsoft.me/eclient.zip")
        os.system('powershell -Command "Expand-Archive -LiteralPath eclient.zip -DestinationPath eClient"')
        os.system("del eclient.zip")
        wget.download("https://eclient-libs.earthsoft.me/Install-Font.ps1", bar=wget.bar_adaptive)
        wget.download("https://eclient-libs.earthsoft.me/command.py", bar=wget.bar_adaptive)
        filename5= wget.detect_filename("https://eclient-libs.earthsoft.me/command.py")
        filename4 = wget.detect_filename("https://eclient-libs.earthsoft.me/Install-Font.ps1")
        shutil.move('Install-Font.ps1', 'eClient/fonts')
        os.chdir("{}\\eClient\\fonts".format(dire))
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Regular.otf")
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Bold.otf")
        os.chdir(r"C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\".format(usr_accnt))
        os.system("del command.py")
        os.chdir(dire)
        shutil.move('command.py', 'C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\'.format(usr_accnt))
        print("eClient installed.")
        print("Creating shortcut...")
        wget.download("https://eclient-libs.earthsoft.me/shortcut.exe", bar=wget.bar_adaptive)
        shutil.move('shortcut.exe', 'C:\\Windows\\System32'.format(usr_accnt))
        google2 = "{}\\eClient".format(dire)
        os.chdir(r"C:\\Users\\{}\\Desktop\\ ".format(usr_accnt))
        os.system(f"shortcut.exe /F:eClient.lnk /A:C /T:{google2}\\eclient.pyw /W:{google2} /I:{google2}\\mc.ico")
        print("Shortcut created.")
        os.system("pause")


def java():
    inst = input("Do you have Java 17 installed? (Y/N): ")
    if inst == "Y" or "y":
        print("Ok.")
        end()
    elif inst == "N" or "n":
        os.system("cls")
        print("Installing Java 17.....")
        wget.download("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi", bar=wget.bar_adaptive)
        filename2 = wget.detect_filename("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi")
        os.system(f"msiexec /i {filename2}")
        time.sleep(5)
        os.remove(f"{filename2}")
        end()
def dep():
    os.system("cls")
    wget.download("https://libs-pi.vercel.app/requirements.txt", bar=wget.bar_adaptive)
    os.system("pip install -r requirements.txt")
    os.system("cls")
    java()

py = input("Do you have Python 3.10 installed? (Y/N): ")
if py == "Y" or "y":
    print("Ok, installing packages.")
    dep()
elif py == "N" or "n":
    print("Installing Python 3.10...")
    wget.download("https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe", bar=wget.bar_adaptive)
    filename = wget.detect_filename("https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exei")
    os.system(f"msiexec /i {filename}")
    time.sleep(5)
    os.remove(f"{filename}")
    dep()
    

'''if os_name.startswith("Linux"):
    os.system("clear")
    os.system("python3 -m pip install -r requirements.txt")
    os.system("sudo apt-get install gksudo fonts-symbola autoconf automake libtool gcc tor gtk2-engines-murrine python3 -y")
    os.system("git clone https://git.torproject.org/torsocks.git") # Fix for torsocks syscall issue 217
    os.chdir("torsocks")
    os.system("./autogen.sh")
    os.system("./configure")
    os.system("make")
    os.system("sudo make install")
    os.system("clear")
    os.system("sudo rm -r torsocks")
    os.system("cd -")
    os.system("clear")
    import wget
    print("Installing Java 17.......")
    #wget.download("https://download.java.net/java/GA/jdk13.0.2/d4173c853231432d94f001e99d882ca7/8/GPL/openjdk-13.0.2_linux-x64_bin.tar.gz", bar=wget.bar_adaptive)
    os.system("sudo apt install openjdk-17-jdk -y")
    print("All requirements installed. Run eclient.py now to run the launcher.")
elif os_name.startswith("Windows"):
    os.system("cls")
    os.system("pip install -r requirements.txt")
    os.system("cls")
    os.chdir(r"C:\\Users\\{}\\Downloads\\ ".format(usr_accnt))
    

    os.system("cls")
    print("Installing Java 17.....")
    wget.download("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi", bar=wget.bar_adaptive)
    filename = wget.detect_filename("https://download.bell-sw.com/java/17.0.3+7/bellsoft-jdk17.0.3+7-windows-amd64.msi")
    os.system(f"msiexec /i {filename}")
    time.sleep(5)
    os.remove(f"{filename}")
    print("All requirements installed. Run eclient.py now to run the launcher.")
'''
