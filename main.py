from tkinter import Canvas, PhotoImage, Entry, Tk, StringVar, DoubleVar
from tkinter import Button as Button1
from tkinter import Label as Label1
from tkinter import *
import random, string
import getpass
from tkinter import ttk
from tkinter.font import Font
import tkinter as tk
from tkinter.ttk import Combobox, Progressbar, Frame, Label, Radiobutton, Notebook, Checkbutton, Scale, Button
from tkinter.messagebox import showerror, showinfo, showwarning, askquestion
from tkvideo import tkvideo
import os
import subprocess
import time
import minecraft_launcher_lib
from minecraft_launcher_lib.forge import install_forge_version, run_forge_installer, supports_automatic_install
from minecraft_launcher_lib.fabric import install_fabric, get_all_minecraft_versions, get_stable_minecraft_versions, get_latest_loader_version
import uuid
import platform
from ttkbootstrap import Style
import json
import sys
from threading import Thread
import time
import requests
from speedtracker import SpeedTracker
import wget
from zipfile import ZipFile
from shutil import move
import psutil
from downloadMods import downloadMod
import customtkinter
import webview
import PIL.Image as im
import PIL.ImageTk as imtk
from ctypes import windll, byref, sizeof, c_int
import ctypes
import webbrowser
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWebEngineCore import QWebEngineProfile
from PyQt6.QtCore import QUrl, QLocale
windll.shcore.SetProcessDpiAwareness(1)
myappid = u'vpun215.eclient.idk.1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
#bros cooking
#my gf left this here im not gonna remove it :D
first=False
global usr_accnt
usr_accnt = getpass.getuser()
microaccount = False
with open('msa.txt') as f:
    content = f.read()
    if content == 0:
        microaccount = False
    else:
        microaccount = True

        

cl = "e9ce99a1-de8e-45a3-99e1-b1d3923d2621"
re = "https://eclient-done.vercel.app/"
se = "pLt8Q~usyUN_5OU7twaQzbFd-vM9IdAZ.YsjWaqu"
theman = ""
'''with open('light.txt') as f:
    content = f.read()
    if content == '0':
        theman = "darkly"
    else:
        theman = "flatly"
with open('val.txt') as f:
    content = f.read()
    if content == '':
        content=0
        theman="darkly"
        showerror(title="Error", message="Unknown error has occured.")
    else:
        theman = "flatly"'''


print("")
print('''
           $$$$$$\  $$\ $$\                      $$\     
          $$  __$$\ $$ |\__|                     $$ |    
 $$$$$$\  $$ /  \__|$$ |$$\  $$$$$$\  $$$$$$$\ $$$$$$\   
$$  __$$\ $$ |      $$ |$$ |$$  __$$\ $$  __$$\\_$$  _|  
$$$$$$$$ |$$ |      $$ |$$ |$$$$$$$$ |$$ |  $$ | $$ |    
$$   ____|$$ |  $$\ $$ |$$ |$$   ____|$$ |  $$ | $$ |$$\ 
\$$$$$$$\ \$$$$$$  |$$ |$$ |\$$$$$$$\ $$ |  $$ | \$$$$  |
 \_______| \______/ \__|\__| \_______|\__|  \__|  \____/ 
                                                         
                                                         
                                                         
''')
print("Based on PyCraft.")
print("Copyright © v-pun215.")
print("")
print("Starting eClient....")
#time.sleep(5)
never = "darkly"




style = Style(theme="darkly") #Sets the theme of the comboboxes and progressbar. Cosmo is a light-blue theme
style.configure("TNotebook", tabposition='n')
style.configure("TNotebook.Tab", foreground="#15d38f", background="#4d4d4d", bordercolor="#072A6C", tabposition='n')
#style.theme_create("custom.TNotebook", foreground="#15d38f", background="#23272a", bordercolor="#072A6C")

currn_dir = os.getcwd()
if os.path.exists(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)):
    mc_dir = r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)
else:
    os.mkdir(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt))
    mc_dir = r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)
    
OS = platform.platform()


def get_size(bytes, suffix="B"):
    #Found this on some website, i don't remember now. Used to get the total ram in GB.
    """
    Scale bytes to its proper format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor


svmem = psutil.virtual_memory()


#Generates the settings.json file which is afterwards read by the settings window. Very important for the program to run
if OS.startswith("Linux"):

    settings = {
                "accessToken": None,
                "clientToken": None,
                "User-info" : [
                    {
                        "username": None,
                        "AUTH_TYPE": None,
                        "UUID": None,
                        "Password": None
                    }
                ],
                "PC-info" : [
                    {
                        "OS": platform.platform(),
                        "Total-Ram": f"{get_size(svmem.total)}",
                    }
                ],
                "Minecraft-home" : mc_dir,
                "selected-version": None,
                "Fps-Boost" : False,
                "Tor-Enabled" : False,
                "setting-info" : [
                    {
                        "fps_boost_selected" : False,
                        "tor_enabled_selected" : False,
                        "allocated_ram_selected" : None,
                    }
                ],
                "allocated_ram" : None,
                "jvm-args": None,
                "executablePath": "java",
                "ramlimiterExceptionBypassed": False,
                "ramlimiterExceptionBypassedSelected": False,
                "verbose": True
                #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir)
            }

elif OS.startswith("Windows"):
    settings = {
                "accessToken": None,
                "clientToken": None,
                "User-info" : [
                    {
                        "username": None,
                        "AUTH_TYPE": None,
                        "UUID": None
                    }
                ],
                "PC-info" : [
                    {
                        "OS": platform.platform(),
                        "Total-Ram": f"{get_size(svmem.total)}",
                    }
                ],
                "Minecraft-home" : mc_dir,
                "selected-version": None,
                "Tor-Enabled" : False,
                "setting-info" : [
                    {
                        "tor_enabled_selected" : False,
                        "allocated_ram_selected" : None
                    }
                ],
                "allocated_ram" : None,
                "jvm-args": None,
                "executablePath": r"C:\\Program Files\\BellSoft\\LibericaJDK-8\\bin\\java.exe",
                "ramlimiterExceptionBypassed": False,
                "ramlimiterExceptionBypassedSelected": False,
                "verbose": True
                #"executablePath": r"{}/runtime/jre-legacy/windows/jre-legacy/bin/java".format(mc_dir)
            }


if not os.path.exists(r"{}/settings.json".format(currn_dir)):
    with open("settings.json", "w") as js_set:
        json.dump(settings, js_set, indent=4)
        js_set.close()
else:
    pass



with open("settings.json", "r") as js_read:
    s = js_read.read()
    s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
    s = s.replace('\n','')  #Found this on stackoverflow.
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s)
    #print(json.dumps(data, indent=4,))

os_name = data["PC-info"][0]["OS"]
mc_home = data["Minecraft-home"]
username = data["User-info"][0]["username"]
uid = data["User-info"][0]["UUID"]
accessToken = data["accessToken"]
mc_dir = data["Minecraft-home"]
auth_type = data["User-info"][0]["AUTH_TYPE"]
jvm_args = data["jvm-args"]
selected_ver = data["selected-version"]
tor_enabled = data["Tor-Enabled"]
tor_enabled_selected = data["setting-info"][0]["tor_enabled_selected"]
allocated_ram = data["allocated_ram"]
allocated_ram_selected = data["setting-info"][0]["allocated_ram_selected"]
ramlimiterExceptionBypassed = data["ramlimiterExceptionBypassed"]
ramlimiterExceptionBypassedSelected = data["ramlimiterExceptionBypassedSelected"]
verbose = data["verbose"]


def reload_data():

    '''Reloads the json data.'''

    global mc_home
    global username
    global uid
    global os_name
    global mc_dir
    global selected_ver
    global ramlimiterExceptionBypassed
    global verbose
    global ramlimiterExceptionBypassedSelected
    global auth_type
    global jvm_args
    global allocated_ram
    global allocated_ram_selected
    global accessToken


    with open("settings.json", "r") as js_read:
        s = js_read.read()
        s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
        s = s.replace('\n','')  #Found this on stackoverflow.
        s = s.replace(',}','}')
        s = s.replace(',]',']')
        data = json.loads(s)
        #print(json.dumps(data, indent=4,))

    os_name = data["PC-info"][0]["OS"]
    mc_home = data["Minecraft-home"]
    username = data["User-info"][0]["username"]
    uid = data["User-info"][0]["UUID"]
    accessToken = data["accessToken"]
    mc_dir = data["Minecraft-home"]
    auth_type = data["User-info"][0]["AUTH_TYPE"]
    jvm_args = data["jvm-args"]
    selected_ver = data["selected-version"]
    tor_enabled = data["Tor-Enabled"]
    tor_enabled_selected = data["setting-info"][0]["tor_enabled_selected"]
    allocated_ram = data["allocated_ram"]
    allocated_ram_selected = data["setting-info"][0]["allocated_ram_selected"]
    ramlimiterExceptionBypassed = data["ramlimiterExceptionBypassed"]
    ramlimiterExceptionBypassedSelected = data["ramlimiterExceptionBypassedSelected"]
    verbose = data["verbose"]





#print("Your OS is {}. Nice one!".format(OS))




if os.path.exists(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)):
    print("Existing minecraft installation, checking for versions...")

else:
     os.mkdir(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt))
     os.chdir(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt))
     os.mkdir("versions")

connected = True

def check_internet(url='https://www.google.com', timeout=5):
    global connected
    #Checks internet connection at startup
    try:
        r2 = requests.head(url, timeout=timeout)
        print("Connected to the Internet!")
        return True
    except requests.ConnectionError:
        connected = False
        print("No internet connection available.")
        eClient()
    except requests.exceptions.Timeout:
        connected = False
        print("Connection Timed Out.")
        eClient()




class eClient():
    global currn_dir
    global connected
    global fps_boost_selected
    global fps_boost
    global tor_enabled_selected
    global tor_enabled
    global allocated_ram
    global allocated_ram_selected
    global mc_home
    global username
    global uid
    global os_name
    global mc_dir
    global selected_ver
    global ramlimiterExceptionBypassed
    global ramlimiterExceptionBypassedSelected
    global auth_type
    global jvm_args

    '''print("")
    print('------EXTREMELY IMPORTANT------')
    print("")
    print("After the Installation of any MC Version is complete, press stop download. ")
    print("I am still trying to fix this problem.")
    print("")
    print("-------------------------------")
    print("")'''
    def docs(self):
        webbrowser.open('https://github.com/v-pun215/eClient/wiki')
    '''def open_popup():
        top= Toplevel(self)
        top.geometry("800x550")
        top.title("Welcome to eClient!")
        Label(top, text= "Welcome to eClient!", font=("SF Pro Display", 25,'bold')).place(x=25,y=20)
        Label(top, text= "If you have any issues, fell free to report them at eClient's ", font=("SF Pro Display", 11)).place(x=10,y=90)
        Label(top, text= "GitHub.", font=("SF Pro Display", 11)).place(x=10,y=110)
        Label(top, text= "Enter Minecraft Directory:", font=("SF Pro Display", 20, 'bold')).place(x=10,y=110)
        self.hulk = Entry(
            top,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", 20),
            highlightthickness = 0)

        self.hulk.insert(0, f"{mc_home}")

        self.googoo = root.hulk.get()

        self.hulk.place(
            x = 10.0, y = 147.0,
            width = 547.0,
            height = 62)

        self.saveboi = Button(
            top,
            text="Save",
            command = root.save,
            bootstyle="success-outline")

        self.saveboi.place(
            x = 790, y = 147,
            width = 119,
            height = 60)'''



    global data

    def __init__(self):
        '''try:
            self.r2 = requests.head("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            connected = False
            print("No internet connection available.")'''



        self.custom_font = Font(family="SF Pro Display", size=26)
        self.custom_font1 = Font(family="SF Pro Display", size=14)
        self.custom_font2 = Font(family="SF Pro Display", size=26)
        self.custom_font3 = Font(family="SF Pro Display", size=16)
        self.custom_font4 = Font(family="SF Pro Display", size=12)
        



        self.os_name = data["PC-info"][0]["OS"]
        '''self.username = data["User-info"][0]["username"]
        self.uid = data["User-info"][0]["UUID"]
        self.mc_dir = data["Minecraft-home"]'''

        self.window = style.master

        self.Tk_Width = 1270
        self.Tk_Height = 736

        self.window.geometry("1024x600+110+60")
        self.window.title("eClient Launcher")
        self.window.configure(bg="#23272a")
        



        if os_name.startswith("Windows"):
            self.window.iconbitmap(r"{}/mc.ico".format(currn_dir))

        self.x_Left = int(self.window.winfo_screenwidth()/2 - self.Tk_Width/2)
        self.y_Top = int(self.window.winfo_screenheight()/2 - self.Tk_Height/2)

        self.window.geometry(f"+{self.x_Left}+{self.y_Top}")
        if os.path.isfile("refresh_token.json"):
            with open("refresh_token.json", "r", encoding="utf-8") as f:
                refresh_token = json.load(f)
                # Do the login with refresh token
                try:
                    account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(cl, se, re, refresh_token)
                    global msaoptions
                    msaoptions = {
                        "username": account_informaton["name"],
                        "uuid": account_informaton["id"],
                        "token": account_informaton["access_token"]
                    }
                # Show the window if the refresh token is invalid
                except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                    pass
        


        self.canvas4 = Canvas(
            self.window,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas4.place(x = 0, y = 0)

        self.nb = Notebook(self.window)
        self.nb.pack(expand=True, fill="both")


        self.frame1 = Frame(self.nb)
        self.frame1.pack(fill='both', expand=True)

        self.p1 = Frame(self.nb)

        self.canvas2 = Canvas(
            self.p1,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas2.place(x = 0, y = 0)

        self.background_img2 = PhotoImage(file = r"img/mc2.png")
        self.background2 = self.canvas2.create_image(
            505,280,
            image=self.background_img2)

        self.b9 = Button(
            self.p1,
            text="Download",
            #height=2,
            #width=10,
            #background="green",
            #foreground="white",
            command = self.handle_download,
            bootstyle="success-outline"
            )

        self.b9.place(
            x = 1, y = 515,
            width = 249,
            height = 48)

        self.b10 = Button(
            self.p1,
            text="Select version",
            #height=2,
            #width=20,
            command=self.save_version,
            #background="green",
            #foreground="white",
            #relief="flat",
            #font=self.custom_font3,
            bootstyle="info-outline"
            )
        self.b10.place(
            x=880, y=515,
            width = 139,
            height = 48
        )


        



        if connected == False:
            self.b9["state"] = "disabled"

            self.offline_versions = []

            self.versions_folder = r"{}/versions".format(mc_dir)

            self.options_dl = ("Vanilla", "Forge", "Fabric")

            self.sub_folders = [self.name for self.name in os.listdir(self.versions_folder) if os.path.isdir(os.path.join(self.versions_folder, self.name))]
            # prints list of minecraft versions
            for self.f in self.sub_folders:
                self.offline_versions.append(self.f)

            self.canvas2.create_text(
                400, 50.0,
                text = "Available Offline",
                fill = "white",
                font = ("SF Pro Display", int(16.0), 'bold'))

            try:
                self.offversionsList = Combobox(self.p1, width=15)
                self.offversionsList.place(x=320, y=100)
                self.offversionsList["values"] = self.offline_versions
                self.offversionsList["state"] = "readonly"
                self.offversionsList.current(0)
            except:
                showerror(message="There are no downloaded versions. If you have downloaded versions, please restart the launcher.")


        else:
            self.canvas2.create_text(
                100, 50.0,
                text = "Run Options",
                fill = "white",
                font = ("SF Pro Display", int(16.0), "bold"))

            self.vanilla_version_list = minecraft_launcher_lib.utils.get_available_versions(mc_dir)

            self.forge_version_list = minecraft_launcher_lib.forge.list_forge_versions()

            self.fabric_version_list = get_stable_minecraft_versions()


            self.forge_versions = []

            self.versions = []

            self.fabric_versions = []

            self.fpsversions = []

            self.fpsversions.append("1.8.9")

            for i in self.vanilla_version_list:
                self.versions.append((i["type"], i["id"]))

            for j in self.forge_version_list:
                self.forge_versions.append(j)

            for k in self.fabric_version_list:
                self.fabric_versions.append(k)

            self.fversionsList = Combobox(self.p1, width=15)
            self.fversionsList.place(x=610, y=100)
            self.fversionsList["values"] = self.forge_versions
            self.fversionsList["state"] = "readonly"
            self.fversionsList.current(0)

            self.fversionsList.bind('<<ComboboxSelected>>')

            self.versionsList = Combobox(self.p1, width=15)
            self.versionsList.place(x=320, y=100)
            self.versionsList["values"] = self.versions
            self.versionsList["state"] = "readonly"
            self.versionsList.current(0)

            self.versionsList.bind('<<ComboboxSelected>>')

            self.options_dl = ("Vanilla", "Forge", "Fabric")


            self.frversionsList = Combobox(self.p1, width=15)
            self.frversionsList.place(x=10, y=280)
            self.frversionsList["values"] = self.fabric_versions
            self.frversionsList["state"] = "readonly"
            self.frversionsList.current(0)

            self.frversionsList.bind('<<ComboboxSelected>>')

            


            self.canvas2.create_text(
                680, 50.0,
                text = "Forge",
                fill = "white",
                font = ("SF Pro Display", int(16.0), "bold"))

            self.canvas2.create_text(
                400, 50.0,
                text = "Vanilla",
                fill = "white",
                font = ("SF Pro Display", int(16.0), "bold"))

            self.canvas2.create_text(
                80, 250,
                text = "Fabric",
                fill = "white",
                font = ("SF Pro Display", int(16.0), "bold"))

            

            self.selected_download = tk.StringVar()
            self.download_options = Combobox(self.p1, textvariable=self.selected_download, width=15)
            self.download_options["values"] = self.options_dl
            self.download_options["state"] = "readonly"
            self.download_options.place(x=10, y=100)
            self.download_options.current(0)

            self.download_options.bind('<<ComboboxSelected>>')

            self.p1.pack(fill='both', expand=True)




        self.canvas = Canvas(
            self.frame1,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas.place(x = 0, y = 0)
        
        def resize_image(e, updated_background_image):
            resized_background_image = updated_background_image.resize((e.width, e.height), im.ANTIALIAS)
            return resized_background_image
        self.background_img = PhotoImage(file = f"img/mc2.png")
        self.background = self.canvas.create_image(
            505,280,
            image=self.background_img)

        self.canvas.create_text(
            500,160,
            text = "eClient Launcher",
            fill = "white",
            font = ("SF Pro Display", int(36.0), "bold")
        )
        self.b13 = Button(
            self.frame1,
            text="Install New Mods",
            command=self.launch_modinstaller,
            bootstyle="primary")
        def mc_news():
            import threading
            webview.create_window('Minecraft Changelog', 'https://changelog-eclient.earthsoft.me/')
            webview.start()
            server1.join()
            server2.join()
        def lunar():
            subprocess.call([r'll.cmd'])
            #self.img3 = PhotoImage(file = f"img/img4.png")
        self.rickroll = Button(
            self.frame1,
            #image = self.img3,
            text = f'Minecraft Changelog',
            #background="green",
            #foreground="white",
            #height=20,
            #width=20,
            command=mc_news,
            bootstyle="info-outline")
        '''self.rick = Button(
            self.frame1,
            #image = self.img3,
            text = f'Lunar Client (Cracked)',
            #background="green",
            #foreground="white",
            #height=20,
            #width=20,
            command=lunar,
            bootstyle="info-outline")'''
        
        
        if auth_type == "Offline Login":
            self.b3 = Button(
                self.frame1,
                #image = self.img3,
                text = f'{selected_ver}\n' + 'Ready to Play',
                #background="green",
                #foreground="white",
                #height=20,
                #width=20,
                command=self.handle_run,
                bootstyle="info-outline")
        elif auth_type == "Mojang Login":
            self.b3 = Button(
                self.frame1,
                #image = self.img3,
                text = f'{selected_ver}\n' + 'Ready to Play',
                #background="green",
                #foreground="white",
                #height=20,
                #width=20,
                command=self.password_window,
                bootstyle="info-outline")
        elif auth_type == "ElyBy Login":
            self.b3 = Button(
                self.frame1,
                #image = self.img3,
                text = f'{selected_ver}\n' + 'Ready to Play',
                #background="green",
                #foreground="white",
                #height=20,
                #width=20,
                command=self.password_window,
                bootstyle="info-outline")
        elif auth_type == "Microsoft Account":
            self.b3 = Button(
                self.frame1,
                #image = self.img3,
                text = f'{selected_ver}\n' + 'Ready to Play',
                #background="green",
                #foreground="white",
                #height=20,
                #width=20,
                command=self.handle_run,
                bootstyle="info-outline")
        else:
            def importantboi():
                showerror(message="Please login to your account first. Learn more: https://github.com/v-pun215/eClient/wiki")
            self.b3 = Button(
                self.frame1,
                #image = self.img3,
                text = "Login in with accnt",
                #background="green",
                #foreground="white",
                #height=20,
                #width=20,
                command=importantboi,
                bootstyle="info-outline")
        if connected == True:

            self.b3.place(
                x = 820, y = 503,
                width = 200,
                height = 60)
            self.rickroll.place(
                x = 1, y = 503,
                width = 200,
                height = 60)
            '''self.rick.place(
                x = 380, y = 480,
                width = 249,
                height = 60)'''


        elif connected == False:
            self.b3.place(
                x = 820, y = 503,
                width = 200,
                height = 60)
            self.rickroll.place(
                x = 1, y = 503,
                width = 200,
                height = 60)
            '''self.rick.place(
                x = 380, y = 480,
                width = 249,
                height = 60)'''







            '''self.img5 = PhotoImage(file = f"img/img6.png")
            self.b5 = Button(
                self.frame1,
                image = self.img5,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            self.b5.place(
                x = 1200, y = 0,
                width = 70,
                height = 50)

            self.img6 = PhotoImage(file = f"img/img7.png")
            self.b6 = Button(
                self.frame1,
                image = self.img6,
                borderwidth = 0,
                highlightthickness = 0,
                relief = "flat")

            self.b6.place(
                x = 1112, y = 0,
                width = 70,
                height = 52)'''



        '''self.img10 = PhotoImage(file = f"img/user.png")
        self.b10 = Button1(
            self.frame1,
            image = self.img10,
            borderwidth = 0,
            highlightthickness = 0,
            command=self.profile_window,
            relief = "flat")

        self.b10.place(
            x = 930, y = 0,
            width = 89,
            height = 87)'''

        self.l3 = Label(self.frame1)
        self.l3.place(x=1, y=1)

        self.l4 = Label(self.frame1)
        self.l4.place(x=1, y=35)


        if connected == True:

            self.l3.config(text=data["User-info"][0]["username"], font=self.custom_font3, foreground="white", background="#384766")

            self.custom_font1 = Font(family="SF Pro Display", size=14)

            self.acc_method = data["User-info"][0]["AUTH_TYPE"]

            if self.acc_method == "Mojang Login":
                self.l4.config(text="Mojang Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "ElyBy Login":
                self.l4.config(text="ElyBy Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "Offline Login":
                self.l4.config(text="Offline Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "Microsoft Account":
                self.l4.config(text="Microsoft Account", font=self.custom_font1, foreground="white", background="#384766")
            '''elif microaccount == True:
                self.acc
                self.l4.config(text="Microsoft Account", font=self.custom_font1, foreground="white", background="#384766")'''

        elif connected == False:

            with open("settings.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            self.l3.config(text=data["User-info"][0]["username"], font=self.custom_font3, foreground="white", background="#689BCA")

            self.custom_font1 = Font(family="SF Pro Display", size=14)

            self.l4.config(text="User is offline", font=self.custom_font1, foreground="white", background="#689BCA")


        '''self.canvas.create_text(
            55, 550,
            text = "v1.0",
            fill = "white",
            font = ("SF Pro Display", int(16.0)))'''

        if not connected:
            showerror(title="No internet access.",
                     message="You are offline!\n You won't have access to the following features: \n Skins System \n Downloads \n Ely.by accounts \n The game can crash")


        
        if os.path.exists(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)):
            self.mc_dir = r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)
        else:
            os.mkdir(r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt))
            self.mc_dir = r"C:\\Users\\{}\\AppData\\Roaming\\.minecraft".format(usr_accnt)
        


        #global variables
        self.cb1 = ""
        self.verb1= BooleanVar()

        self.cb2 = ""
        self.s1 = ""

        self.current_value = DoubleVar()


        #Small hack for remembering settings in the gui


        if tor_enabled_selected == True:
            self.cb2 = StringVar(value="selected")
        else:
            cb2 = StringVar(value="deselected")




        self.window_s = Frame(self.nb)
        self.window_10 = Frame(self.nb)

        self.svmem = psutil.virtual_memory()



        

        self.canvas5 = Canvas(
            self.window_s,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas5.place(x = 3, y = 0)

        self.value_label = Label(
        self.canvas5,
        text=self.get_current_value(),
        foreground="#15d38f",
        style = "info.TLabel",
        background='#23272a'
        )

        self.value_label.place(x=270, y=530)


        self.background_img3 = PhotoImage(file = f"img/mc2.png")
        self.background3 = self.canvas5.create_image(
                500.0, 280.0,
                image=self.background_img3)

        self.canvas5.create_text(
            500, 45.5,
            text = "Settings",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))


        self.current_value_label = Label(
            self.canvas5,
            text='Ram Assigned:',
            style = "info.TLabel",
            background='#23272a',
            foreground="#15d38f"
        )

        self.current_value_label.place(x=200, y=500)





        self.canvas5.create_text(
            260, 105,
            text = "Minecraft Directory(requires relaunch)",
            fill = "white",
            font = ("SF Pro Display", int(17.0), "bold"))

        self.canvas5.create_text(
            245.5, 378.0,
            text = "Memory Allocation(requires relaunch)",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))

        self.canvas5.create_text(
            520, 310,
            text = "Minecraft Settings",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))

        self.str_ram = data["PC-info"][0]["Total-Ram"].strip("    GB")
        self.ram = float(self.str_ram)
        self.med_ram = (self.ram*1000)/2

        self.slider = Scale(
            self.window_s,
            from_=128,
            to=self.ram*1000,
            command=self.slider_changed,
            style="info.Horizontal.TScale",
            variable=self.current_value,
            length = "1000"
        )

        self.slider.place(x=5, y=430)


        #Very important system check.

        self.first_time_run = True

        if allocated_ram and allocated_ram_selected == None:
            #slider.set(allocated_ram_selected)
            self.first_time_run = True
            print(self.first_time_run)
        elif allocated_ram and allocated_ram_selected != None:
            self.slider.set(allocated_ram)
            self.current_value_label.config(text=f"Ram Assigned: {allocated_ram}", font=self.custom_font4)
            self.first_time_run = False
            print(self.first_time_run)




        self.l7 = Label(
            self.window_s,
            text=f"Total : {self.ram*1000} MB",
            style = "info.TLabel",
            background='black',
            foreground="#15d38f",
            font=self.custom_font4
        )

        self.l7.place(x=460, y=500)


            #self.entry0_img = PhotoImage(file = f"img/img_textBox3.png")
            #self.entry0_bg = self.canvas5.create_image(
            #    333.5, 297.0,
            #    image = self.entry0_img)

        self.entry0 = Entry(
            self.window_s,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", 20),
            highlightthickness = 0)

        self.entry0.insert(0, f"{mc_home}")

        self.curn_path = self.entry0.get()

        self.entry0.place(
            x = 10.0, y = 147.0,
            width = 547.0,
            height = 62)

        self.b7 = Button(
            self.canvas5,
            text="Save",
            command = self.save,
            bootstyle="success-outline")

        self.b7.place(
            x = 790, y = 147,
            width = 119,
            height = 60)

        self.b15 = Button(
            self.canvas5,
            text="Save",
            command = self.save_ram,
            bootstyle="danger-outline")

        self.b15.place(
            x = 790, y = 520,
            width = 120,
            height = 40)


        self.flt_s1 = ""
        self.s1 = ""
        self.flt_s2 = ""
        self.s2 = ""

        self.window_t = Frame(self.nb)
        self.window_11 = Frame(self.nb)

        self.canvas6 = Canvas(
            self.window_t,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas6.place(x = 3, y = 0)
        self.canvas10 = Canvas(
            self.window_10,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas10.place(x = 3, y = 0)

        self.canvas11 = Canvas(
            self.window_11,
            bg = "#23272a",
            height = 720,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas11.place(x = 3, y = 0)


        self.background_img4 = PhotoImage(file = f"img/mc2.png")
        self.background4 = self.canvas6.create_image(
                500.0, 280.0,
                image=self.background_img4)
        
        self.background10 = self.canvas10.create_image(
                500.0, 280.0,
                image=self.background_img4)

        self.canvas10.create_text(
            510.0, 55.0,
            text = "Microsoft Login",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas10.create_text(
            510.0, 255.0,
            text = "Other Accounts",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas10.create_text(
            250.0, 330.0,
            text = "Type",
            fill = "white",
            font = ("SF Pro Display", int(18.0), "bold"))
        self.canvas10.create_text(
            750.0, 330.0,
            text = "Username",
            fill = "white",
            font = ("SF Pro Display", int(18.0), "bold"))
        self.options = ("Mojang Login", "Offline Login", "ElyBy Login",)

        if connected == True:

            self.options = ("Mojang Login", "Offline Login", "ElyBy Login",)

            self.selected_option = tk.StringVar()
            self.acc_options = Combobox(self.canvas10, textvariable=self.selected_option)
            self.acc_options["values"] = self.options
            self.acc_options["state"] = "readonly"
            self.acc_options.place(x=150, y=380)


            self.acc_options.bind('<<ComboboxSelected>>')
        elif connected == False:

            self.options = ("Offline Login")

            self.selected_option = tk.StringVar()
            self.acc_options = Combobox(self.canvas10, textvariable=self.selected_option)
            self.acc_options["values"] = self.options
            self.acc_options["state"] = "readonly"
            self.acc_options.place(x=1500, y=380)


            self.acc_options.bind('<<ComboboxSelected>>')
        self.entry0 = Entry(
            self.canvas10,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", 16),
            highlightthickness = 0)

        self.entry0.insert(0, f"{username}")

        self.entry0.place(
            x = 630, y = 380,
            width = 250,
            height = 33)
        self.b11 = Button(self.canvas10, text="Save", command=self.save_acc, bootstyle="success-outline")
        self.b11.place(x=470, y=510)
        
        
        
        self.microsoftbutton = Button(
            self.canvas10,
            text="Login",
            command=self.microsoft_login,
            bootstyle="primary")
        self.microsoftbutton.place(
            x = 440, y = 100,
            width = 120,
            height = 40)

        self.background11 = self.canvas11.create_image(
                500.0, 280.0,
                image=self.background_img4)
        self.canvas11.create_text(
            510.0, 55.0,
            text = "Help",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas11.create_text(
            500.0, 100.0,
            text = "The documentation is available as this project's GitHub page.",
            fill = "white",
            font = ("SF Pro Display", int(12.0)))
        self.canvas11.create_text(
            510.0, 250.0,
            text = "Credits",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas11.create_text(
            508.0, 290.0,
            text = "shasankp000 for PyCraft",
            fill = "white",
            font = ("SF Pro Display", int(12.0)))
        self.canvas11.create_text(
            508.0, 320.0,
            text = "v-pun215 for eClient",
            fill = "white",
            font = ("SF Pro Display", int(12.0)))
        self.canvas11.create_text(
            510.0, 380.0,
            text = "About",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas11.create_text(
            508.0, 420.0,
            text = "Version 1.8",
            fill = "white",
            font = ("SF Pro Display", int(12.0)))
        self.canvas11.create_text(
            508.0, 450.0,
            text = "© v-pun215 2023. No rights reserved.",
            fill = "white",
            font = ("SF Pro Display", int(12.0)))
        

        self.github = Button(
            self.canvas11,
            text="Documentation",
            command=self.docs,
            bootstyle="primary")

        
        self.b13.place(
            x = 420, y = 420,
            width = 180,
            height = 40)
        self.github.place(
            x = 420, y = 120,
            width = 180,
            height = 40)

        

        self.canvas6.create_text(
            250.0, 55.0,
            text = "Bypass RAM Limiter",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))


        self.canvas6.create_text(
            220.0, 115.0,
            text = "JVM Arguments",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))
        self.canvas6.create_text(
            220.0, 285.0,
            text = "Verbose Mode",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))


        self.entry2 = Entry(
            self.window_t,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", 20),
            highlightthickness = 0)
        if verbose == True:
            self.verb1 = BooleanVar(value=True)
        else:
            self.verb1 = BooleanVar(value=False)
        
        self.verb = Checkbutton(self.window_t, bootstyle="success-round-toggle", onvalue=True, offvalue=False, command=self.verbcheck, variable=self.verb1)
        self.verb.place(x=600, y=280.0)
        
        '''self.canvas6.create_text(
            220.0, 300.0,
            text = "Dark Mode",
            fill = "white",
            font = ("SF Pro Display", int(20.0), "bold"))'''


        self.login_method = auth_type
        

        if self.login_method == "Mojang Login":
            self.j1 = jvm_args
            self.entry2.insert(0, f"{self.j1}")

        elif self.login_method == "ElyBy Login":
            self.j2 = jvm_args
            self.entry2.insert(0, f"{self.j2}")

        elif self.login_method == "Offline Login":
            self.j1 = jvm_args
            self.entry2.insert(0, f"{self.j1}")

        elif self.login_method == "Microsoft Account":
            self.j1 = jvm_args
            self.entry2.insert(0, f"{self.j1}")


        self.entry2.place(
            x = 120.0, y = 167.0,
            width = 547.0,
            height = 62)

        

        if ramlimiterExceptionBypassedSelected== True:
            self.cb1 = StringVar(value="selected")
        else:
            self.cb1 = StringVar(value="deselected")


        self.sn1 = Checkbutton(self.window_t, bootstyle="success-round-toggle", onvalue="selected", offvalue="deselected", command=self.check2, variable=self.cb1)
        self.sn1.place(x=600, y=55.0)
        with open('val.txt') as dam:
            content = dam.read()
        #global val
        #val = content
        #nah = IntVar(value=val)
        #self.dm = Checkbutton(self.window_t, bootstyle="success-round-toggle", command=self.toggle_dm, variable=nah)
        #global isit
        #isit = nah.get()
        #self.dm.place(x=600, y=290.0)

        self.nb.add(self.frame1, text="Home")
        self.nb.add(self.p1, text="Installations")
        self.nb.add(self.window_s, text="Settings")
        self.nb.add(self.window_t, text="Additional Settings")
        self.nb.add(self.window_10, text="Accounts")
        self.nb.add(self.window_11, text="Help")


        


        self.window.resizable(False, False)
        self.window.mainloop()
        '''with open('ninst.txt') as f:
            content = f.read()
            if content == '0':
                first= True
                open_popup()
                f = open("ninst.txt", "w")
                f.write("1")
                f.close()
            else:
                pass'''
    def restart(self):
        os.system("taskkill /f /im python.exe")
        os.system("python main.py")
        
    '''def toggle_dm(self):
        global dark
        global style
        if self.dm.get() == "selected":
            dark = False
            print("selected")
        elif self.dm.get() == "deselected":
            dark = True
            print("deselected")
        if dark == True:
            never = "darkly"
            style = Style(theme=never)
            print("darkly")
        elif dark == False:
            never = "flatly"
            style = Style(theme=never)
            print("flatly")
        if isit == 0:
            print("selected")
            f = open("light.txt", "w")
            f.write("1")
            f3 = open("val.txt", "w")
            f3.write("1")
            print("Relaunching...")
            f.close()
            self.restart()
        if isit == 1:
            print("deselected")
            f = open("light.txt", "w")
            f.write("0")
            print("Relaunching...")
            f2 = open("val.txt", "w")
            f2.write("0")
            f.close()
            self.restart()'''

    


    def generate_cracked_uid(self):

        if data["User-info"][0]["UUID"] == None:

            self.uid = uuid.uuid4().hex

            with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()

        elif data["User-info"][0]["UUID"] != None:

            self.uid = data["User-info"][0]["UUID"]

    '''def splash_screen(self):
        #Splash Screen for the launcher
        self.splash_s = style.master
        self.splash_s.title("eClient Loader")
        self.splash_s.geometry("761x403+140+50")

        self.Tk_Width = 761
        self.Tk_Height = 403

        self.x_Left = int(self.splash_s.winfo_screenwidth()/2 - self.Tk_Width/2)
        self.y_Top = int(self.splash_s.winfo_screenheight()/2 - self.Tk_Height/2)

        self.splash_s.geometry(f"+{self.x_Left}+{self.y_Top}")


        self.splash_s.resizable(False, False)


        self.canvas6 = Canvas(
            self.splash_s,
            bg = "#3a3a3a",
            height = 768,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas6.place(x = 0, y = 0)

        self.background_img6 = PhotoImage(file = "img/mc1.png")
        self.background6 = self.canvas6.create_image(
            380.5,201.5,
            image=self.background_img6)


        if not os.path.exists(r"{}/settings.json".format(currn_dir)):
            sefl.c1 = Label1(
                    self.splash_s,
                    text = "Generating settings.....",
                    font = ("SF Pro Display", int(16.0)),
                    bg="#3a3a3a",
                    fg="cyan1")

        else:
            self.c1 = Label1(
                    self.splash_s,
                    text = "Reading settings.....",
                    font = ("SF Pro Display", int(16.0)),
                    bg="#3a3a3a",
                    fg="cyan1")

        self.c1.place(x=248, y=350)

        self.splash_s.after(10000, lambda: self.c1.configure(text="Getting everything ready...."))

        self.canva6.create_text(
            400, 200,
            text = "eClient Launcher 1.04",
            fill = "cyan1",
            font = ("Galiver Sans", int(26.0)))


        self.pb3 = Progressbar(self.splash_s, value=0, style='info.Horizontal.TProgressbar', length=300, mode="indeterminate")
        self.pb3.place(x=250, y=400)


        window_running = True
        self.pb3.start()
        self.splash_s.after(20000, lambda: self.pb3.stop())
        self.splash_s.after(24000, lambda: self.splash_s.withdraw())
        self.splahs_s.after(30000, lambda: self.splash_s.destroy())

        self.splash_s.mainloop()'''



    def printProgressBar(self, iteration, total, prefix='', suffix='', decimals=1, length=100, fill='█', printEnd="\r"):
        """
        Call in a loop to create terminal progress bar
        @params:
            iteration   - Required  : current iteration (Int)
            total       - Required  : total iterations (Int)
            prefix      - Optional  : prefix string (Str)
            suffix      - Optional  : suffix string (Str)
            decimals    - Optional  : positive number of decimals in percent complete (Int)
            length      - Optional  : character length of bar (Int)
            fill        - Optional  : bar fill character (Str)
            printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
        """
        self.percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
        self.filledLength = int(length * iteration // total)
        self.bar = fill * self.filledLength + '-' * (length - self.filledLength)
        print('\r%s |%s| %s%% %s' % (prefix, self.bar, self.percent, suffix), end=printEnd)
        # Print New Line on Complete
        if iteration == total:
            print()








    '''def check2(self):
        global fps_boost
        global fps_boost_selected
        if cb1.get() == "selected":
            fps_boost = True
            fps_boost_selected = True

        elif cb1.get() == "deselected":
            fps_boost = False
            fps_boost_selected = False


        data["Fps-Boost"] = fps_boost
        data["setting-info"][0]["fps_boost_selected"] = fps_boost_selected


        with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()'''

    def verbcheck(self):
            global verbose
            if self.verb1.get() == True:
                verbose = True

            elif self.verb1.get() == False:
                verbose = False

            data["verbose"] = verbose

            with open("settings.json", "w") as js_set:
                json.dump(data, js_set, indent=4)
                js_set.close()
    def check2(self):
        global ramlimiterExceptionBypassed
        global ramlimiterExceptionBypassedSelected
        if self.cb1.get() == "selected":
            ramlimiterExceptionBypassed = True
            ramlimiterExceptionBypassedSelected = True

        elif self.cb1.get() == "deselected":
            ramlimiterExceptionBypassed = False
            ramlimiterExceptionBypassedSelected = False
    



        data["ramlimiterExceptionBypassed"] = ramlimiterExceptionBypassed
        data["ramlimiterExceptionBypassedSelected"] = ramlimiterExceptionBypassedSelected


        with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()




    def check3(self):
        global tor_enabled
        global tor_enabled_selected
        if self.cb2.get() == "selected":
            tor_enabled = True
            tor_enabled_selected = True

        elif self.cb2.get() == "deselected":
            tor_enabled = False
            tor_enabled_selected = False

        data["Tor-Enabled"] = tor_enabled
        data["setting-info"][0]["tor_enabled_selected"] = tor_enabled_selected

        with open("settings.json", "w") as js_set:
                json.dump(data, js_set, indent=4)
                js_set.close()


    def save(self):
        '''Saves the minecraft home dir path, which is entered.'''
        global mc_home
        mc_home = self.entry0.get()
        data["Minecraft-home"] = mc_home

        with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()




    def get_current_value(self):
        return '{: .2f} MB'.format(self.current_value.get())

    def slider_changed(self, event):

        try:
            self.value_label.configure(text=self.get_current_value())
            self.s1 = self.get_current_value()
            self.flt_s1 = float(self.s1.rstrip(" MB"))
            #print(s1)
            data["setting-info"][0]["allocated_ram_selected"] = self.flt_s1
        except NameError:
            pass

        with open("settings.json", "w") as js_set:
                json.dump(data, js_set, indent=4)
                js_set.close()

    def get_size(self, bytes, suffix="B"):
        """
        Scale bytes to its proper format
        e.g:
            1253656 => '1.20MB'
            1253656678 => '1.17GB'
        """
        self.factor = 1024
        for self.unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < self.factor:
                return f"{bytes:.2f}{self.unit}{suffix}"
            bytes /= self.factor





    def save_ram(self):
        self.s2 = self.get_current_value()
        self.flt_s2 = float(self.s2.rstrip(" MB"))
        data["allocated_ram"] = self.flt_s2
        data["setting-info"][0]["allocated_ram_selected"] = self.flt_s2
        print("Selected: ", self.flt_s2)

        with open("settings.json", "w") as js_set:
                json.dump(data, js_set, indent=4)
                js_set.close()

        #print(s1)

        if self.flt_s2>(self.med_ram):
            if ramlimiterExceptionBypassed == True:
                self.slider.set(self.flt_s2)
                self.current_value_label.config(text=f"Ram Assigned: {self.flt_s2} MB", font=self.custom_font4)
                showinfo(title="Done", message=f"Allocated {self.flt_s2} MB of ram")


                data["allocated_ram"] = self.flt_s2
                data["setting-info"][0]["allocated_ram_selected"] = self.flt_s2
                print("Selected: ", self.flt_s2)
                print("Changed to: ", self.flt_s2)

                with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()

            else:

                self.slider.set(self.med_ram)
                self.current_value_label.config(text=f"Ram Assigned: {self.med_ram} MB", font=self.custom_font4)
                data["allocated_ram"] = self.med_ram
                data["setting-info"][0]["allocated_ram_selected"] = self.flt_s2
                print("Changed to: ", self.med_ram)

                with open("settings.json", "w") as js_set:
                        json.dump(data, js_set, indent=4)
                        js_set.close()

                showerror(title="Error!", message="Cannot assign more than 50 percent of host OS's ram. This is intended for low end pc(s) to run smoothly.")

        elif self.flt_s2<(self.med_ram):
            self.slider.set(self.flt_s2)
            self.current_value_label.config(text=f"Ram Assigned: {self.flt_s2} MB", font=self.custom_font4)

            data["allocated_ram"] = self.flt_s2
            data["setting-info"][0]["allocated_ram_selected"] = self.flt_s2
            print("Changed to: ", self.flt_s2)

            with open("settings.json", "w") as js_set:
                    json.dump(data, js_set, indent=4)
                    js_set.close()

            showinfo(title="Done", message=f"Allocated {self.flt_s2} MB of ram")

    
    '''def dc_invite(self):
        webbrowser.open("https://discord.gg/SsnX8DtPcD")

    def git_invite(self):
        webbrowser.open("https://github.com/shasankp000")

    def mc_news(self):
        webview.create_window('Minecraft Caves and Cliffs update 1.17.1', 'https://www.minecraft.net/en-us/article/caves---cliffs--part-i-out-today-java')
        webview.start()

    def changelog(self):
        webview.create_window('eClient 1.04 Changelog', "https://github.com/shasankp000/eClient/blob/main/changelog.md")
        webview.start()

    def skinview(self):
        webbrowser.open("https://ely.by/skins")'''

    def maximum(self, max_value, value):
        self.max_value[0] = value

    def run_mc(self):
        '''Runs minecraft with the specifed version'''

        with open("settings.json", "r") as js_read:
            s = js_read.read()
            s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
            s = s.replace('\n','')  #Found this on stackoverflow.
            s = s.replace(',}','}')
            s = s.replace(',]',']')
            data = json.loads(s)


        self.login_method = data["User-info"][0]["AUTH_TYPE"]
        self.detected_ver = ""  # yet another small hack
        self.runtime_ver = data["selected-version"]

        with open("settings.json", "r") as js_read1:
            self.s1 = js_read1.read()
            self.s1 = self.s1.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
            self.s1 = self.s1.replace('\n','')  #Found this on stackoverflow.
            self.s1 = self.s1.replace(',}','}')
            self.s1 = self.s1.replace(',]',']')
            self.data1 = json.loads(self.s1)
            #print(json.dumps(data, indent=4,))

        self.mc_dir = data["Minecraft-home"]

        self.allocated_ram = self.data1["allocated_ram"]
        self.allocated_ram_selected = self.data1["setting-info"][0]["allocated_ram_selected"]

        self.modified_ram = self.allocated_ram//1
        self.ram_mb = int(self.modified_ram)

        self.ram_gb = self.allocated_ram//1000
        self.int_ram_gb = int(self.ram_gb)

        print(self.allocated_ram)
        self.cpu_count = os.cpu_count()

        
        if self.os_name.startswith("Linux"):
            self.j1 = [f"-Xmx{int(self.ram_mb)}M", "-Xms128M"]
        elif self.os_name.startswith("Windows"):
            self.j1 = [f"-Xmx{int(self.ram_mb)}M", "-Xms128M"]


        data["jvm-args"] = self.j1

        with open("settings.json", "w") as js_set:
            json.dump(data, js_set, indent=4)
            js_set.close()
        if connected == True:
            if self.runtime_ver.startswith("Vanilla"): #Checking for selected version before running minecraft.
                if self.login_method == "Microsoft Account":
                    try:
                        if data["selected-version"].startswith("Vanilla: snapshot"):
                            print(data["selected-version"])
                            mcdonalds = data["selected-version"]
                            self.mc_ver = mcdonalds.partition(' ')[2]
                            print(self.mc_ver)
                        else:
                            self.mc_ver = data["selected-version"].strip("Vanilla: ")
                        self.detected_ver = ""  # yet another small hack
                        if connected == True:
                            if self.mc_ver.startswith("release"):
                                self.detected_ver = self.mc_ver.strip("release ")
                            elif self.mc_ver.startswith("snapshot "):
                                print(self.mc_ver)
                                self.detected_ver = self.mc_ver.partition(' ')[2]
                                print(self.detected_ver)
                        elif connected == False:
                            self.detected_ver = self.mc_ver

                        with open("refresh_token.json", "r", encoding="utf-8") as f:
                            refresh_token = json.load(f)
                            # Do the login with refresh token
                            try:
                                se = "pLt8Q~usyUN_5OU7twaQzbFd-vM9IdAZ.YsjWaqu"
                                re = "https://eclient-done.vercel.app/"
                                cl = "e9ce99a1-de8e-45a3-99e1-b1d3923d2621"
                                account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(cl, se, re, refresh_token)
                                msaoptions = {
                                    "username": account_informaton["name"],
                                    "uuid": account_informaton["id"],
                                    "token": account_informaton["access_token"]
                                }
                                
                                
                            # Show the window if the refresh token is invalid
                            except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                                pass
                        self.window.withdraw()
                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, msaoptions)

                        print(self.detected_ver)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)

                elif self.login_method == "Mojang Login":
                    try:
                        self.usr = data["User-info"][0]["username"]
                        self.pwd = self.pwd1

                        if data["selected-version"].startswith("Vanilla: snapshot"):
                            print(data["selected-version"])
                            mcdonalds = data["selected-version"]
                            self.mc_ver = mcdonalds.partition(' ')[2]
                            print(self.mc_ver)
                        else:
                            self.mc_ver = data["selected-version"].strip("Vanilla: ")
                        self.detected_ver = ""

                        # This is done to get only the version number, cutting out the rest of the string including whitespace
                        if connected == True:
                            if self.mc_ver.startswith("release"):
                                self.detected_ver = self.mc_ver.strip("release ")
                            elif self.mc_ver.startswith("snapshot "):
                                print(self.mc_ver)
                                self.detected_ver = self.mc_ver.partition(' ')[2]
                                print(self.detected_ver)
                        elif connected == False:
                            self.detected_ver = self.mc_ver

                        print(self.detected_ver)


                        self.login_data = minecraft_launcher_lib.account.login_user(self.usr, self.pwd)

                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.options["uuid"]

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()


                        self.window.withdraw()
                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)

                elif self.login_method == "Offline Login":

                    self.generate_cracked_uid()
                    def get_random_string(length):
                        # choose from all lowercase letter
                        letters = string.ascii_lowercase
                        result_str = ''.join(random.choice(letters) for i in range(length))
                        print("Random password generated:", result_str)

                    try:
                        self.usr = data["User-info"][0]["username"]
                        self.pwd = get_random_string(10)
                        if data["selected-version"].startswith("Vanilla: snapshot"):
                            print(data["selected-version"])
                            mcdonalds = data["selected-version"]
                            self.mc_ver = mcdonalds.partition(' ')[2]
                            print(self.mc_ver)
                        else:
                            self.mc_ver = data["selected-version"].strip("Vanilla: ")

                        if connected == True:
                            if self.mc_ver.startswith("release"):
                                self.detected_ver = self.mc_ver.strip("release ")
                            elif self.mc_ver.startswith("snapshot "):
                                print(self.mc_ver)
                                self.detected_ver = self.mc_ver.partition(' ')[2]
                                print(self.detected_ver)
                        elif connected == False:
                            self.detected_ver = self.mc_ver


                        print(self.detected_ver)

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid

                        self.window.withdraw()
                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)

                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)

                elif self.login_method == "ElyBy Login":
                    self.ely_authenticate()

                    if data["selected-version"].startswith("Vanilla: snapshot"):
                            print(data["selected-version"])
                            mcdonalds = data["selected-version"]
                            self.mc_ver = mcdonalds.partition(' ')[2]
                            print(self.mc_ver)
                    else:
                        self.mc_ver = data["selected-version"].strip("Vanilla: ")

                    if self.mc_ver.startswith("release"):
                        self.detected_ver = self.mc_ver.strip("release ")
                    elif self.mc_ver.startswith("snapshot "):
                        print(self.mc_ver)
                        self.detected_ver = self.mc_ver.partition(' ')[2]
                        print(self.detected_ver)


                    try:
                        self.j2 = [r"-javaagent:{}/authlib/".format(currn_dir) + "" + f"authlib-injector-1.2.3.jar=ely.by", f"-Xmx{int(self.ram_mb)}M", "-Xms128M"]


                        data["User-info"][0]["username"] = self.usr
                        data["jvm-args"] = self.j2

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        self.accessToken = data["accessToken"]

                        self.options = {
                        "username": self.usr,
                        "uuid": self.uid,
                        "token": self.accessToken,
                        "jvmArguments" : self.j2,
                        "executablePath": "java" #self.data1["executablePath"]
                        #"executablePath" : executablePath
                        }

                        data["executablePath"] = self.options["executablePath"]
                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid
                        data["jvm-args"] = self.j2

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                        print(e)

            elif self.runtime_ver.startswith("Forge"):
                if self.login_method == "Microsoft Account":
                    try:
                        self.mc_ver = data["selected-version"].strip("Forge: ")
                        if connected == True:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]
                        elif connected == False:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]

                        with open("refresh_token.json", "r", encoding="utf-8") as f:
                            refresh_token = json.load(f)
                            # Do the login with refresh token
                            try:
                                se = "pLt8Q~usyUN_5OU7twaQzbFd-vM9IdAZ.YsjWaqu"
                                re = "https://eclient-done.vercel.app/"
                                cl = "e9ce99a1-de8e-45a3-99e1-b1d3923d2621"
                                account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(cl, se, re, refresh_token)
                                msaoptions = {
                                    "username": account_informaton["name"],
                                    "uuid": account_informaton["id"],
                                    "token": account_informaton["access_token"]
                                }
                                
                                
                            # Show the window if the refresh token is invalid
                            except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                                pass
                        self.window.withdraw()
                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver1, self.mc_dir, msaoptions)

                        print(self.detected_ver)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                if self.login_method == "Mojang Login":
                    try:
                        self.usr = data["User-info"][0]["username"]
                        self.pwd = self.pwd1
                        self.mc_ver = data["selected-version"].strip("Forge: ")

                        # This is done to get only the version number, cutting out the rest of the string including whitespace

                        # Not required while running forge
                        if connected == True:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]
                        elif connected == False:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]



                        self.login_data = minecraft_launcher_lib.account.login_user(self.usr, self.pwd)


                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.options["uuid"]

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()



                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver1, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)

                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                        print(e)

                elif self.login_method == "Offline Login":

                    self.generate_cracked_uid()


                    self.usr = data["User-info"][0]["username"]
                    self.pwd = self.pwd1
                    self.mc_ver = data["selected-version"].strip("Forge: ")

                    try:
                        if connected == True:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]
                        elif connected == False:
                            self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]





                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver1, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                        print(e)

                elif self.login_method == "ElyBy Login":
                    self.ely_authenticate()

                    self.mc_ver = data["selected-version"].strip("Forge: ")

                    self.detected_ver1 = self.mc_ver[:7]+"forge-"+self.mc_ver[7:]

                    self.v1 = self.detected_ver1.rstrip(self.detected_ver1[7:])


                    try:

                        self.j2 = [r"-javaagent:{}/authlib/".format(currn_dir) + "" + f"authlib-injector-1.2.3.jar=ely.by", f"-Xmx{int(self.ram_mb)}M", "-Xms128M"]


                        data["User-info"][0]["username"] = self.usr
                        data["jvm-args"] = self.j2

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        self.accessToken = data["accessToken"]
                        self.options = {
                        "username": self.usr,
                        "uuid": self.uid,
                        "token": self.accessToken,
                        "jvmArguments" : self.j2,
                        "executablePath": self.data1["executablePath"]
                        #"executablePath" : executablePath
                        }

                        data["executablePath"] = self.options["executablePath"]
                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid
                        data["jvm-args"] = self.j2

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()


                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver1, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                        print(e)

            elif self.runtime_ver.startswith("Fabric"):
                self.lv = get_latest_loader_version()
                if self.login_method == "Microsoft Account":
                    try:
                        self.mc_ver = data["selected-version"].strip("Fabric: ")
                        if connected == True:
                            self.v1 = self.mc_ver[:6]

                            # This is done to get only the version number, cutting out the rest of the string including whitespace

                            # Not required while running forge
                            self.detected_ver2 = f"fabric-loader-{self.lv}-{self.v1}"
                        elif connected == False:
                            self.detected_ver2 = self.mc_ver

                        with open("refresh_token.json", "r", encoding="utf-8") as f:
                            refresh_token = json.load(f)
                            # Do the login with refresh token
                            try:
                                se = "pLt8Q~usyUN_5OU7twaQzbFd-vM9IdAZ.YsjWaqu"
                                re = "https://eclient-done.vercel.app/"
                                cl = "e9ce99a1-de8e-45a3-99e1-b1d3923d2621"
                                account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(cl, se, re, refresh_token)
                                msaoptions = {
                                    "username": account_informaton["name"],
                                    "uuid": account_informaton["id"],
                                    "token": account_informaton["access_token"]
                                }
                                
                                
                            # Show the window if the refresh token is invalid
                            except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                                pass
                        self.window.withdraw()
                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver2, self.mc_dir, msaoptions)

                        print(self.detected_ver)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=e)
                if self.login_method == "Mojang Login":
                    try:
                        self.usr = data["User-info"][0]["username"]
                        self.pwd = self.pwd1
                        self.mc_ver = data["selected-version"].strip("Fabric: ")


                        if connected == True:
                            self.v1 = self.mc_ver[:6]

                            # This is done to get only the version number, cutting out the rest of the string including whitespace

                            # Not required while running forge
                            self.detected_ver2 = f"fabric-loader-{self.lv}-{self.v1}"
                        elif connected == False:
                            self.detected_ver2 = self.mc_ver



                        self.login_data = minecraft_launcher_lib.account.login_user(self.usr, self.pwd)


                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.login_data["selectedProfile"]["name"],
                            "uuid": self.login_data["selectedProfile"]["id"],
                            "token": self.login_data["accessToken"],
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.options["uuid"]

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()



                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver2, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)

                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=f"{e}. Try re-downloading this fabric version, seems like a new loader version has been released.")
                        print(e)

                elif self.login_method == "Offline Login":

                    self.generate_cracked_uid()

                    self.usr = data["User-info"][0]["username"]
                    self.pwd = self.pwd1
                    self.mc_ver = data["selected-version"].strip("Fabric: ")



                    try:
                        if connected == True:
                            self.v1 = self.mc_ver[:6]

                            # This is done to get only the version number, cutting out the rest of the string including whitespace

                            # Not required while running forge
                            self.detected_ver2 = f"fabric-loader-{self.lv}-{self.v1}"
                        elif connected == False:
                            self.detected_ver2 = self.mc_ver




                        if os_name.startswith("Linux"):

                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": "java"
                            #"executablePath" : executablePath
                            }

                        else:
                            self.options = {
                            "username": self.usr,
                            "uuid": self.uid,
                            "token": "",
                            "jvmArguments": self.j1,
                            "executablePath": self.data1["executablePath"] #The path to the java executable
                            #"executablePath" : executablePath
                            }

                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid



                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()

                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver2, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=f"{e}. Try re-downloading this fabric version, seems like a new loader version has been released.")
                        print(e)

                elif self.login_method == "ElyBy Login":
                    self.ely_authenticate()

                    self.mc_ver = data["selected-version"].strip("Fabric: ")

                    self.v1 = self.mc_ver[:6]

                    self.detected_ver2 = f"fabric-loader-{self.lv}-{self.mc_ver}"




                    try:

                        self.j2 = [r"-javaagent:{}/authlib/".format(currn_dir) + "" + f"authlib-injector-1.2.3.jar=ely.by", f"-Xmx{int(self.ram_mb)}M", "-Xms128M"]


                        data["User-info"][0]["username"] = self.usr
                        data["jvm-args"] = self.j2

                        with open("settings.json", "r") as js_read:
                            s = js_read.read()
                            s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
                            s = s.replace('\n','')  #Found this on stackoverflow.
                            s = s.replace(',}','}')
                            s = s.replace(',]',']')
                            data = json.loads(s)


                        self.accessToken = data["accessToken"]
                        self.uid = data["User-info"][0]["UUID"]


                        self.options = {
                        "username": self.usr,
                        "uuid": self.uid,
                        "token": self.accessToken,
                        "jvmArguments" : self.j2,
                        "executablePath": self.data1["executablePath"]
                        #"executablePath" : executablePath
                        }

                        data["executablePath"] = self.options["executablePath"]
                        data["jvm-args"] = self.j2
                        data["User-info"][0]["username"] = self.usr
                        data["User-info"][0]["UUID"] = self.uid

                        with open("settings.json", "w") as js_set:
                            json.dump(data, js_set, indent=4)
                            js_set.close()


                        self.window.withdraw()

                        self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver2, self.mc_dir, self.options)
                        print(f"Launching minecraft version {self.mc_ver}")
                        subprocess.call(self.minecraft_command)
                    except minecraft_launcher_lib.exceptions.VersionNotFound as e:
                        showerror(title="Error!", message=f"{e}. Try re-downloading this fabric version, seems like a new loader version has been released.")
                        print(e)

        elif connected == False:

            self.usr = data["User-info"][0]["username"]
            self.uid = uid

            self.detected_ver2 = self.offversionsList.get()

            if os_name.startswith("Linux"):

                self.options = {
                "username": self.usr,
                "uuid": self.uid,
                #"token": self.accessToken
                "jvmArguments": self.j1,
                "executablePath": "java"
                #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir) #The path to the java executable
                #"executablePath" : executablePath
                }

            else:
                self.options = {
                "username": self.usr,
                "uuid": self.uid,
                #"token": self.accessToken,
                "jvmArguments": self.j1,
                "executablePath": self.data1["executablePath"] #The path to the java executable
                #"executablePath" : executablePath
                }

            data["User-info"][0]["username"] = self.usr
            data["User-info"][0]["UUID"] = self.options["uuid"]
            data["selected-version"] = self.detected_ver2

            with open("settings.json", "w") as js_set:
                json.dump(data, js_set, indent=4)
                js_set.close()



            self.window.withdraw()

            self.minecraft_command = minecraft_launcher_lib.command.get_minecraft_command(self.detected_ver2, self.mc_dir, self.options)
            print(f"Launching minecraft version {self.detected_ver2}")
            subprocess.call(self.minecraft_command)


    def ely_authenticate(self):
        '''Connects to ely.by for user authorization'''

        self.usr = data["User-info"][0]["username"]
        self.pwd = self.pwd1
        acpass = file1 = open("password.txt","r+")
        self.client_token = str(uuid.uuid4())

        self.acc_data ={
            "username": self.usr,
            "password": self.pwd,
            "clientToken" : self.client_token,
            "requestUser" : True
        }


        self.r = requests.get(f"https://authserver.ely.by/api/users/profiles/minecraft/{self.usr}")
        if self.r.status_code == 200:
            print("[OK] [200]", "User found, getting details........")
            self.r1 = requests.post(f"https://authserver.ely.by/auth/authenticate", data=self.acc_data)
            if self.r1.status_code == 200:
                self.accessToken = self.r1.json()["accessToken"]
                self.uid = self.r1.json()["user"]["id"]

                data["User-info"][0]["UUID"] = self.uid
                data["clientToken"] = self.client_token
                data["accessToken"] = self.accessToken

                with open("settings.json", "w") as f:
                    json.dump(data, f, indent=4 )
                    f.close()

                '''with open("user_details.json", "r") as js_read:
                    s = js_read.read()
                    s = s.replace('\t','')  #Trailing commas in dict cause file read problems, these lines will fix it.
                    s = s.replace('\n','')
                    s = s.replace(',}','}')
                    s = s.replace(',]',']')
                    data1 = json.loads(s)
                    print(json.dumps(data1, indent=4))'''

            elif self.r1.status_code == 404:
                showerror(title="Error", message=f"Data entered is either incomplete or account is secured with Oauth2. Error code: {self.r1.status_code}")
                print("Data entered is either incomplete or account is secured with Oauth2")
        elif self.r.status_code == 404:
            print("[ERROR] 404", "User does not exist.")
            showerror(title="User not found", message=f"The specified user does not exist. Error code: {self.r.status_code}")



    def download(self):
        '''Downloads minecraft with the specified version'''
        self.dl_opt = self.download_options.get()
        self.selected_ver = ""
        self.l5 = ""
        self.detected_ver1 = ""  # yet another small hack

        self.max_value = [0]

        self.callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: self.printProgressBar(value, self.max_value[0]),
            "setMax": lambda value: self.maximum(self.max_value, value)
        }

        if self.dl_opt == "Vanilla":
            self.selected_ver = self.versionsList.get()

            if self.selected_ver.startswith("release"):
                    self.detected_ver1 = self.selected_ver.strip("release ")
            elif self.selected_ver.startswith("snapshot"):
                    split_string = self.selected_ver.split(' ')
                    new_string_list = split_string[1:]
                    new_string = ' '.join(new_string_list)
                    self.detected_ver1 = new_string
                    print(self.detected_ver1)

            #showinfo(title="Installation started...", message=f"Installing minecraft version {self.selected_ver}")
            print(f"Installing {self.detected_ver1}")
            minecraft_launcher_lib.install.install_minecraft_version(self.detected_ver1,self.mc_dir, callback=self.callback)
            

            data["selected-version"] = "Vanilla:" + " " + f"{self.selected_ver}"
            with open("settings.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            self.selected_version = data["selected-version"]

            #self.l5.config(text=self.selected_version, font=self.custom_font, fg="#15d38f", bg="#23272a")

        elif self.dl_opt == "Forge":
            self.selected_ver = self.fversionsList.get()

            if supports_automatic_install(self.selected_ver):
                showinfo(title="Installation started..", message=f"Installing forge version {self.selected_ver}")
                install_forge_version(self.selected_ver, self.mc_dir, callback=self.callback)

                data["selected-version"] = "Forge:" + " " + f"{self.selected_ver}"
                with open("settings.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()

                self.selected_version = data["selected-version"]

                self.l5.config(text=self.selected_version, font=self.custom_font, fg="#15d38f", bg="#23272a")
            else:
                showinfo(title="Installation started..", message=f"Installing forge version {self.selected_ver}")
                run_forge_installer(self.selected_ver)

                data["selected-version"] = "Forge:" + " " + f"{self.selected_ver}"
                with open("settings.json", "w") as f:
                    json.dump(data, f, indent=4)
                    f.close()

                self.selected_version = data["selected-version"]

                self.l5.config(text=self.selected_version, font=self.custom_font, fg="#15d38f", bg="#23272a")

        elif self.dl_opt == "Fabric":
            self.selected_ver = self.frversionsList.get()

            showinfo(title="Installation started..", message=f"Installing fabric version {self.selected_ver}")
            install_fabric(self.selected_ver, self.mc_dir, callback=self.callback)

            data["selected-version"] = "Fabric:" + " " + f"{self.selected_ver}"
            with open("settings.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            self.selected_version = data["selected-version"]

            self.l5.config(text=self.selected_version, font=self.custom_font, fg="#15d38f", bg="#23272a")


        elif self.dl_opt == "Ares Client":
            self.selected_ver = self.fpsversionsList.get()

            try:
                showinfo(title="Installation started", message="Installing Ares Client....")
                print("Downloading Ares Client, stable version.")
                print("Download might be a bit slow, as it is from a mediafire link.")
                os.chdir(self.mc_dir)
                wget.download("https://download2390.mediafire.com/gdkggxf25fkg/92l0eryou1seqi6/AresNovemberUpdate.zip", bar=wget.bar_adaptive)
                print("Installing Ares Client.......")
                self.filename = wget.detect_filename("download2390.mediafire.com/gdkggxf25fkg/92l0eryou1seqi6/AresNovemberUpdate.zip")
                with ZipFile(self.filename, "r") as self.f1:
                    self.f1.extractall()
                move(r"{}/Ares".format(self.mc_dir), r"{}/versions".format(self.mc_dir))
                print("Done")
                os.remove(self.filename)

            except:
                showerror(title="Error", message="Errors encountered while downloading....")


    def save_version(self):
        if connected == True:
            self.dl_opt = self.download_options.get()

        if connected == True:
            if self.dl_opt == "Vanilla":
                if connected == True:
                    self.selected_ver = self.versionsList.get()
                    data["selected-version"] = "Vanilla:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    #self.l5.config(text=self.selected_version, font=self.custom_font, fg="#15d38f", bg="#23272a")
                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')
                elif connected == False:
                    self.selected_ver = self.offversionsList.get()
                    data["selected-version"] = "Vanilla:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')

            elif self.dl_opt == "Forge":
                if connected == True:
                    self.selected_ver = self.fversionsList.get()
                    data["selected-version"] = "Forge:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')
                elif connected == False:
                    self.selected_ver = self.offversionsList.get()
                    data["selected-version"] = "Forge" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')

            elif self.dl_opt == "Fabric":
                if connected == True:
                    self.selected_ver = self.frversionsList.get()
                    data["selected-version"] = "Fabric:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')
                elif connected == False:
                    self.selected_ver = self.offversionsList.get()
                    data["selected-version"] = "Fabric:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')

            elif self.dl_opt == "Ares Client":
                if connected == True:
                    self.selected_ver = self.fpsversionsList.get()
                    data["selected-version"] = "Ares:" + " " + f"{self.selected_ver}"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')
                elif connected == False:
                    self.selected_ver == self.offversionsList.get()
                    data["selected-version"] = "Ares:" + " " + "1.8.9"
                    with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()

                    self.selected_version = data["selected-version"]

                    self.b3.config(text = f'{self.selected_version}\n' + 'Ready to Play')


        elif connected == False:
            self.selected_version = self.offversionsList.get()

            data["selected_version"] = self.selected_version

            with open("settings.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            self.b3.config(text = f"{self.selected_version}\n" + "Ready to Play")


    def save_acc(self):
        self.u1 = self.entry0.get()
        showinfo(title="Account saved", message="Please restart eClient to see changes.")

        if connected == True:

            self.acc_method = self.acc_options.get()



            if data["User-info"][0]["username"] != None:
                #self.l3.config(text=self.u1, font=self.custom_font3, foreground="#15d38f", background="#23272a")

                data["User-info"][0]["username"] = self.u1
                data["User-info"][0]["AUTH_TYPE"] = self.acc_method

                if self.acc_method == "Mojang Login":
                    self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                    self.l4.config(text="mojang account", font=self.custom_font1, foreground="white", background="#384766")
                elif self.acc_method == "ElyBy Login":
                    self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                    self.l4.config(text="ely.by account", font=self.custom_font1, foreground="white", background="#384766")
                elif self.acc_method == "Offline Login":
                    self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                    self.l4.config(text="no account", font=self.custom_font1, foreground="white", background="#384766")
                elif self.acc_method == "Microsoft Account":
                    with open('name.json') as f:
                        data1 = json.load(f)
                    data["User-info"][0]["username"] = data1
                    data["User-info"][0]["AUTH_TYPE"] = self.acc_method
                    self.l3.config(text=data1, font=self.custom_font3, foreground="white", background="#384766")
                    self.l4.config(text="Microsoft Account", font=self.custom_font1, foreground="white", background="#384766")

                with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()


            else:
                self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")

                if self.acc_method == "Microsoft Login":
                    with open('name.json') as f:
                        data1 = json.load(f)
                    data["User-info"][0]["username"] = data1
                else:
                    data["User-info"][0]["username"] = self.u1
                data["User-info"][0]["AUTH_TYPE"] = self.acc_method

                with open("settings.json", "w") as f:
                        json.dump(data, f, indent=4)
                        f.close()
   


            if self.acc_method == "Mojang Login":
                self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                self.l3.config(text=data["User-info"][0]["username"], font=self.custom_font3, foreground="white", background="#384766")
                self.l4.config(text="Mojang Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "ElyBy Login":
                self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                self.l3.config(text=data["User-info"][0]["username"], font=self.custom_font3, foreground="white", background="#384766")
                self.l4.config(text="ElyBy Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "Offline Login":
                self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
                self.l3.config(text=data["User-info"][0]["username"], font=self.custom_font3, foreground="white", background="#384766")
                self.l4.config(text="Offline Account", font=self.custom_font1, foreground="white", background="#384766")
            elif self.acc_method == "Microsoft Account":
                with open('name.json') as f:
                    data1 = json.load(f)
                data["User-info"][0]["username"] = data1
                self.l3.config(text=data1, font=self.custom_font3, foreground="white", background="#384766")
                self.l4.config(text="Microsoft Account", font=self.custom_font1, foreground="white", background="#384766")
                

        else:
            data["User-info"][0]["AUTH_TYPE"] = "Offline Login"

            with open("settings.json", "w") as f:
                json.dump(data, f, indent=4)
                f.close()

            if data["User-info"][0]["username"] == None:
                self.l3.config(text=self.u1, font=self.custom_font3, foreground="white", background="#384766")
            else:
                self.l3.config(text=data["User-info"][0]["username"], foreground="white", background="#384766")


            self.l4.config(text="User is offline", font=self.custom_font1, foreground="white", background="#384766")

    def profile_window(self):

        self.p2 = tk.Toplevel()
        self.p2.title("Account Window")
        self.p2.geometry("800x450")

        self.p2.configure(bg = "#23272a")
        self.p2.resizable(False,False)
        self.canvas3 = Canvas(
            self.p2,
            bg = "#23272a",
            height = 600,
            width = 800,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas3.place(x = 0, y = 0)


        self.background_img1 = PhotoImage(file = f"img/bg2.png")
        self.background1 = self.canvas3.create_image(
            400, 225,
            image=self.background_img1)


        self.canvas3.create_text(
            80, 380,
            text = "Accounts",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))

        if connected == True:

            self.options = ("Mojang Login", "Offline Login", "ElyBy Login",)

            self.selected_option = tk.StringVar()
            self.acc_options = Combobox(self.p2, textvariable=self.selected_option)
            self.acc_options["values"] = self.options
            self.acc_options["state"] = "readonly"
            self.acc_options.place(x=10, y=410)


            self.acc_options.bind('<<ComboboxSelected>>')
            self.canvas3.create_text(
                150,50,
                text = "Microsoft Login (beta)",
                fill="white",
                font=("SF Pro Display", int(17.0), "bold"))
            self.msa = Button(self.canvas3, text="Open Login Window", command=self.microsoft_login, bootstyle="success-outline")
            self.msa.place(x=40, y=80)

        elif connected == False:

            self.options = ("Offline Login")

            self.selected_option = tk.StringVar()
            self.acc_options = Combobox(self.p2, textvariable=self.selected_option)
            self.acc_options["values"] = self.options
            self.acc_options["state"] = "readonly"
            self.acc_options.place(x=10, y=410)


            self.acc_options.bind('<<ComboboxSelected>>')





        '''self.entry0_img = PhotoImage(file = f"img/img_textBox0.png")
        self.entry0_bg = self.canvas3.create_image(
            400, 442,
            image = self.entry0_img)'''

        self.entry0 = Entry(
            self.p2,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", 16),
            highlightthickness = 0)

        self.entry0.insert(0, f"{username}")

        self.entry0.place(
            x = 260, y = 410,
            width = 250,
            height = 33)
        
        self.canvas3.create_text(
            360, 380.0,
            text = "Username",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))

        self.b11 = Button(self.p2, text="Save", command=self.save_acc, bootstyle="success-outline")
        self.b11.place(x=540, y=410)

    def microsoft_login(self):
        #os.system("python msa.py")
        subprocess.call('python msa.py', shell=True)
        print("Microsoft Account added. Please relaunch eClient.")
        data["User-info"][0]["AUTH_TYPE"] = "Microsoft Account"
        with open("name.json") as f:
            data1 = json.load(f)
        data["User-info"][0]["username"] = data1
        self.l3.config(text=data1, font=self.custom_font3, foreground="white", background="#384766")
        self.l4.config(text="Microsoft Account", font=self.custom_font1, foreground="white", background="#384766")
        with open("uuid.json") as f:
            data2 = json.load(f)
        data["User-info"][0]["UUID"] = data2
        with open("settings.json", "w") as msa_set:
            json.dump(data, msa_set, indent=4)
            msa_set.close()
        with open("refresh_token.json", "r", encoding="utf-8") as f:
                refresh_token = json.load(f)
                # Do the login with refresh token
                try:
                    account_informaton = minecraft_launcher_lib.microsoft_account.complete_refresh(cl, se, re, refresh_token)
                    global msaoptions
                    msaoptions = {
                        "username": account_informaton["name"],
                        "uuid": account_informaton["id"],
                        "token": account_informaton["access_token"]
                    }
                # Show the window if the refresh token is invalid
                except minecraft_launcher_lib.exceptions.InvalidRefreshToken:
                    pass
        showinfo(title="Microsoft Account", message="Microsoft Account added. Please relaunch eClient.")
        
        
        
        
        

    def confirm(self):
        self.pwd1 = self.entry1.get()
        self.p3.destroy()
        self.handle_run()
        print(self.pwd1)

    


    def password_window(self):
        if self.acc_method == "Microsoft Account":
            self.handle_run()
        else:
            self.p3 = tk.Toplevel()
            self.p3.title("Enter Password")
            self.p3.geometry("630x200")

            self.p3.configure(bg="white")
            self.p3.resizable(False,False)
            self.canvas4 = Canvas(
                self.p3,
                height = 200,
                width = 800,
                bd = 0,
                highlightthickness = 0,
                relief = "ridge")
            self.canvas4.place(x = 0, y = 0)

            '''self.entry1_img = PhotoImage(file = f"img/img_textBox1.png")
            self.entry1_bg = self.canvas4.create_image(
                230, 92,
                image = self.entry1_img)'''

            self.entry1 = Entry(
                self.canvas4,
                bd = 0,
                bg = "#c4c4c4",
                show = ".",
                font = ("SF Pro Display", 16),
                highlightthickness = 0)


            self.canvas4.create_text(
                80, 80,
                text = "Password: ",
                fill = "white",
                font = ("SF Pro Display", int(16.0), "bold"))

            self.entry1.place(
                x = 155, y = 60 ,
                width = 300,
                height = 36)


            self.l6 = tk.Label(self.canvas4, text="Please enter your password to play. It won't be saved.", font=Font(family="SF Pro Display", size=16), foreground="#15d38f", background="#23272a")
            self.l6.place(x=10, y=135)

            self.b12 = Button(self.canvas4, text="Confirm", command=self.confirm, bootstyle="warning-outline")
            self.b12.place(x=520,y=62)





    def start_download(self):
        '''Initiates a second window consisting of the download progressbar, while hiding the previous one.'''

        def close():
            '''restores the minimized original window and cancels the download.
            res = askquestion(title='Abort?', message="Really cancel the download?")
            if res == "yes":
                try:
                    if self.dl_thread.is_alive():
                        self.window.deiconify()
                        self.pw.destroy()
                        raise KeyboardInterrupt
                        self.dl_thread.join()
                        self.t2.join()
                        print("Done. Closed.")


                except tk.TclError:
                    print("Download window closed.")
            elif res == "no":
                pass'''
            pass


        self.window.withdraw()
        self.pw = tk.Toplevel()
        def disable_event():
            pass
        self.pw.protocol("WM_DELETE_WINDOW", disable_event)
        self.pw.geometry("375x150")
        self.pw.title("Downloading...")
        if os_name.startswith("Windows"):
            self.pw.iconbitmap("icon.ico")
        self.pw.configure(bg = "#ffffff")
        self.pw.resizable(False,False)
        self.canvas1 = Canvas(
            self.pw,
            bg = "#3a3a3a",
            height = 768,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas1.place(x = 0, y = 0)
        t2nine1 = self.selected_ver.capitalize()
        textynine = f"Downloading {t2nine1}"
        
        self.canvas1.create_text(
                200, 80,
                text = textynine,
                fill = "white",
                font = ("SF Pro Display", int(13.0),))
        try:
            self.pw.wm_protocol("WM_DELETE_WINDOW", lambda:close())
        except tk.TclError():
            print("Download window closed.")

        self.max_value = [0]

        self.callback = {
            "setStatus": lambda text: print(text),
            "setProgress": lambda value: self.printProgressBar(value, self.max_value[0]),
            "setMax": lambda value: self.maximum(self.max_value, value)
        }

        self.output = self.callback["setStatus"]

        print(type(self.output))
        

        self.pb = Progressbar(self.pw, bootstyle="success", orient='horizontal', length=280, mode="indeterminate")
        self.pb.place(x=50, y=140)


    def stop_download(self):
        '''restores the minimized original window and cancels the download.'''
        self.window.deiconify()
        self.pw.destroy()
        print("Download terminated")
        #raise KeyboardInterrupt

    def handle_progress(self):
        '''handles the progress bar increment'''
        self.pb.start()

    def handle_download(self):
        '''Starts the download thread'''
        self.start_download()

        
        try:
            self.t2 = Thread(target=self.handle_progress)
            self.t2.start()

            self.dl_thread = Thread(target=self.download) # Download thread
            self.dl_thread.start()

            self.monitor(self.dl_thread)
        except KeyboardInterrupt:
            self.dl_thread.join(timeout=4.0)
            self.t2.join(timeout=6.0)


        print("Download Started.")

       


    def monitor(self, dl_thread):
        '''Monitors the download thread, and updates the progressbar'''
        if self.dl_thread.is_alive():
            self.window.after(100, lambda: self.monitor(self.dl_thread))
        else:
            print("Install finished")
            self.stop_download()


    def handle_run(self):
        '''Creates the thread on which minecraft is running'''
        self.t4 = Thread(target=self.run_mc)
        self.t4.start()

        self.monitor_mc(self.t4)

    def monitor_mc(self, t4):
        '''Monitors the thread on which minecraft is running'''
        if self.t4.is_alive():
            self.window.after(100, lambda: self.monitor_mc(self.t4))
        else:
            t4.join(timeout=3.0)
            self.window.deiconify()
    
    def launch_modinstaller(self):
        #Launches the modinstaller window.

        #self.window.withdraw()
        self.mod_win = tk.Toplevel()
        self.mod_win.geometry("740x270")
        self.mod_win.title("Mod Installer")
        if os_name.startswith("Windows"):
            self.mod_win.iconbitmap("mc.ico")
        self.mod_win.configure(bg = "#ffffff")
        self.mod_win.resizable(False,False)
        self.canvas7 = Canvas(
            self.mod_win,
            bg = "#3a3a3a",
            height = 768,
            width = 1024,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge")
        self.canvas7.place(x = 0, y = 0)

        self.canvas7.create_text(
            80.0, 55.0,
            text = "Mod Name:",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))

        self.entry3 = Entry(
            self.mod_win,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", int(16.0), "bold"),
            highlightthickness = 0)

        self.entry3.place(
            x = 155.0, y = 40,
            width = 500,
            height = 30)

        self.canvas7.create_text(
            165.0, 95.0,
            text = "Mod Loader(fabric/forge):",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))


        self.entry4 = Entry(
            self.mod_win,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", int(16.0), "bold"),
            highlightthickness = 0)

        self.entry4.place(
            x = 330.0, y = 80,
            width = 380,
            height = 30)

        self.canvas7.create_text(
            100.0, 135.0,
            text = "Game Version:",
            fill = "white",
            font = ("SF Pro Display", int(16.0), "bold"))

        self.entry5 = Entry(
            self.mod_win,
            bd = 0,
            bg = "#c4c4c4",
            font = ("SF Pro Display", int(16.0), "bold"),
            highlightthickness = 0)

        self.entry5.place(
            x = 195.0, y = 120,
            width = 480,
            height = 30)


        self.b16 = Button(
            self.mod_win,
            text="Download",
            command=self.download_mod,
            bootstyle="info-outline")


        self.b16.place(
            x = 75, y = 190,
            width = 180,
            height = 40)
        
        self.modfol = Button(
            self.mod_win,
            text="Open Mods Folder",
            command=self.modfolder,
            bootstyle="info-outline")
        self.modfol.place(
            x = 275, y =190,
            width=180,
            height=40)
        self.modsboi = Button(
            self.mod_win,
            text="See Mods Installed",
            command=self.modsins,
            bootstyle="info-outline")
        self.modsboi.place(
            x = 475, y =190,
            width=180,
            height=40)
        
        
        
    def modsins(self):
        os.system("python mc.py")
    def modfolder(self):
        moduser = getpass.getuser()
        path = f"C:/Users/{moduser}/AppData/Roaming/.minecraft/mods/"
        path = os.path.realpath(path)
        os.startfile(path)

    def download_mod(self):
        '''Downloads the mod from Modrinth'''
        self.modname = self.entry3.get()
        self.modloader = self.entry4.get()
        self.gamever = self.entry5.get()
        


        downloadMod(self.modname,self.modloader,self.gamever, mc_dir)


if __name__ == "__main__":
    try:
        check_internet("https://www.google.com")

        eClient()

    except KeyboardInterrupt:
        print("Program Exited")
