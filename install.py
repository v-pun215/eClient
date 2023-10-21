import os
import time
import platform
import getpass
import time
import wget
import shutil


os.system("title eClient Installer")
print("---eClient Installer---")
print("Getting necessary stuff...")
time.sleep(2)
os_name = platform.platform()
usr_accnt = getpass.getuser()
currn_dir = os.getcwd()
py_ver = platform.python_version()
def end():
    print("Thank you for choosing eClient.")
    print("Setup will now start installing eClient.")
    os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\".format(usr_accnt))
    wget.download("https://libs-pi.vercel.app/eclient.zip", bar=wget.bar_adaptive)
    filename3 = wget.detect_filename("https://libs-pi.vercel.app/eclient.zip")
    os.system('powershell -Command "Expand-Archive -LiteralPath eclient.zip -DestinationPath eClient"')
    os.system("del eclient.zip")
    print("")
    important = input("Do you want to install the SF Pro Display Font automatically? (requires admin rights) (Y/N): ")
    if important.upper() == "Y":
        os.mkdir(r"C:\\Users\\{}\\AppData\\Roaming\\eClient\\root".format(usr_accnt))
        os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\eClient\\root".format(usr_accnt))
        wget.download("https://libs-pi.vercel.app/sf.ttf", bar=wget.bar_adaptive)
        wget.download("https://libs-pi.vercel.app/sfb.ttf", bar=wget.bar_adaptive)
        wget.download("https://libs-pi.vercel.app/FontReg.exe", bar=wget.bar_adaptive)
        wget.download("https://libs-pi.vercel.app/FontReg.md5", bar=wget.bar_adaptive)
        os.system("FontReg.exe /copy")
    else:
        pass
    os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\".format(usr_accnt))
    print("eClient installed.")
    print("Creating shortcut...")
    google = "C:\\Users\\{}\\AppData\\Roaming\\eClient".format(usr_accnt)
    wget.download("https://libs-pi.vercel.app/Shortcut.exe", bar=wget.bar_adaptive)
    shutil.move('Shortcut.exe', 'C:\\Users\\{}\\Desktop'.format(usr_accnt))
    os.chdir("C:\\Users\\{}\\Desktop".format(usr_accnt))
    os.system(f"Shortcut.exe /F:eClient.lnk /A:C /T:{google}\\eclient.pyw /W:{google} /I:{google}\\mc.ico")
    os.system('del Shortcut.exe')
    os.system('cls')
    print("eClient has installed itself onto the machine succesfully.")
    os.system("pause")

'''    elif not dire == "":
        print("Installing eClient to {}...".format(dire))
        os.chdir(dire)
        wget.download("https://libs-pi.vercel.app/eclient.zip", bar=wget.bar_adaptive)
        filename3 = wget.detect_filename("https://libs-pi.vercel.app/eclient.zip")
        os.system('powershell -Command "Expand-Archive -LiteralPath eclient.zip -DestinationPath eClient"')
        os.system("del eclient.zip")
        wget.download("https://libs-pi.vercel.app/command.py", bar=wget.bar_adaptive)
        filename5= wget.detect_filename("https://libs-pi.vercel.app/command.py")
        os.chdir("{}\\eClient\\fonts".format(dire))
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Regular.otf")
        os.system("powershell -executionpolicy bypass -File .\Install-Font.ps1 .\SF Pro Display Bold.otf")
        os.chdir(r"C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\".format(usr_accnt))
        os.system("del command.py")
        os.chdir(dire)
        shutil.move('command.py', 'C:\\Users\\{}\\AppData\\Local\\Programs\\Python\\Python310\\Lib\\site-packages\\minecraft_launcher_lib\\'.format(usr_accnt))
        print("eClient installed.")
        print("Creating shortcut...")
        damn = "C:\\Windows\\System32\\shortcut.exe"
        isExist = os.path.exists(damn)
        wget.download("https://libs-pi.vercel.app/Shortcut.exe", bar=wget.bar_adaptive)
        shutil.move('Shortcut.exe', 'C:\\Users\\{}\\Desktop'.format(usr_accnt))
        google = "{}\\eClient".format(dire)
        os.chdir("C:\\Users\\{}\\Desktop".format(usr_accnt))
        os.system(f"Shortcut.exe /F:eClient.lnk /A:C /T:{google}\\eclient.pyw /W:{google} /I:{google}\\mc.ico")
        os.system("del Shortcut.exe")'''



def java():
    inst = input("Do you have Java 17 installed? (Y/N): ")
    if inst.lower() == "y":
        print("Ok.")
        end()
    else:
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
if py.lower() == "y":
    print("Ok, installing packages.")
    dep()
else:
    print("Installing Python 3.10...")
    wget.download("https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe", bar=wget.bar_adaptive)
    filename = wget.detect_filename("https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe")
    os.system(f"{filename}")
    time.sleep(5)
    os.remove(f"{filename}")
    print("Restarting program....")
    os.system("eClient-v1.7-x64-Installer")
    exit()
    

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
