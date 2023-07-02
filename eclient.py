import json 
from ttkbootstrap import Style
from tkinter.ttk import Progressbar
from tkinter.messagebox import askquestion, showinfo
from tkinter import Label, Canvas, PhotoImage
import tkinter as tk
import sys
import os
import time
from threading import Thread
from tkvideo import tkvideo
import platform
import psutil
import platform
import base64
from ctypes import windll
windll.shcore.SetProcessDpiAwareness(1)

currn_dir = os.getcwd()
mc_dir = r"{}/.minecraft".format(currn_dir)
os_name = platform.platform()

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

if os_name.startswith("Linux"):

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
                "ramlimiterExceptionBypassedSelected": False
                #"executablePath": r"{}/runtime/jre-legacy/linux/jre-legacy/bin/java".format(mc_dir)
            }

elif os_name.startswith("Windows"):
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
                "Fps-Boost" : False,
                "Tor-Enabled" : False,
                "setting-info" : [
                    {
                        "fps_boost_selected" : False,
                        "tor_enabled_selected" : False,
                        "allocated_ram_selected" : None
                    }
                ],
                "allocated_ram" : None,
                "jvm-args": None,
                "executablePath": r"C:\\Program Files\\BellSoft\\LibericaJDK-17\\bin\\java",
                "ramlimiterExceptionBypassed": False,
                "ramlimiterExceptionBypassedSelected": False
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
    s = s.replace('\n','')
    s = s.replace(',}','}')
    s = s.replace(',]',']')
    data = json.loads(s)
    #print(json.dumps(data, indent=4,))

os_name = data["PC-info"][0]["OS"]
username = data["User-info"][0]["username"]
mc_home = data["Minecraft-home"]
fps_boost = data["Fps-Boost"]
tor_enabled = data["Tor-Enabled"]
fps_boost_selected = data["setting-info"][0]["fps_boost_selected"]
tor_enabled_selected = data["setting-info"][0]["tor_enabled_selected"]
ramlimiterExceptionBypassed = data["ramlimiterExceptionBypassed"]
ramlimiterExceptionBypassedSelected = data["ramlimiterExceptionBypassedSelected"]

style = Style()


root = style.master
root.configure(bg = "#3a3a3a")
root.title("eClient Updater")
root.iconbitmap("img/mc.ico")
root.geometry("761x403+140+50")


Tk_Width = 761
Tk_Height = 403

x_Left = int(root.winfo_screenwidth()/2 - Tk_Width/2)
y_Top = int(root.winfo_screenheight()/2 - Tk_Height/2)

root.geometry(f"+{x_Left}+{y_Top}")


root.resizable(False, False)







canvas = Canvas(
    root,
    bg = "#3a3a3a",
    height = 768,
    width = 1024,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = "img/mc1.png")
background = canvas.create_image(
    380.5,201.5,
    image=background_img)





if not os.path.exists(r"{}/settings.json".format(currn_dir)):
    c1 = Label(
            text = "Generating settings.....",
            font = ("SF Pro Display", int(13.0)),
            bg="#3a3a3a",
            fg="cyan1")

else:
    c1 = Label(
            text = "Reading settings.....",
            font = ("SF Pro Display", int(13.0)),
            bg="#3a3a3a",
            fg="cyan1")

c1.place(x=248, y=350)

root.after(10000, lambda: c1.configure(text="Getting everything ready...."))

canvas.create_text(
    400, 200,
    text = "eClient Launcher",
    fill = "white",
    font = ("SF Pro Display", int(26.0), "bold"))




#l1 = Label(root)
#l1.pack()

#v1 = tkvideo(r"{}/intro_gif.mp4".format(currn_dir), l1, loop=1, size=(640,360))


pb1 = Progressbar(root, value=0, style='info.Horizontal.TProgressbar', length=300, mode="indeterminate")
pb1.place(x=250, y=400)        


t1 = Thread(target=lambda: os.system("./main.sh"))
t2 = Thread(target=lambda: os.system("main.bat"))
#t3 = Thread(target=lambda: v1.play())


def checksettings():
    '''A small hack to check settings and start the launcher accordingly.'''
    if tor_enabled and tor_enabled_selected == True:

            #time.sleep(20.0)
            #pb1.stop()
        if os_name.startswith("Linux"):
            res2 = askquestion(title="Grant permission", message="Grant permission to permform administrative task?")
            if res2 == "yes":
                showinfo(title="Ok", message="Please enter your password in the next window to start tor")
                os.system("gksudo service tor start")
            elif res2 == "no":
                showinfo(title="Abort", message="Tor cannot start without administrative privileges.")
                sys.exit(0)
            with open("main.sh", "w") as f:
                f.write("torsocks python3 main.py\n")
                f.close()
                os.system("chmod 700 main.sh")
                root.after(23000, lambda:t1.start())
        elif os_name.startswith("Windows"):
            with open("main.bat", "w") as f:
                f.write("taskkill /f /im python.exe\n")  #frees up cpu and memory
                f.write("yeah.cmd")
                f.close()
                root.after(23000, lambda: t2.start())

    else:
            #time.sleep(20.0)
            #pb1.stop()
        if os_name.startswith("Linux"):
            with open("main.sh", "w") as f:
                f.write("python3 main.py\n")
                f.close()
            os.system("chmod 700 main.sh")
            root.after(23000, lambda: t1.start())
        elif os_name.startswith("Windows"):
            with open("main.bat", "w") as f:
                f.write("taskkill /f /im python.exe\n")  #frees up cpu and memory
                f.write("yeah.cmd")
                f.close()
            root.after(23000, lambda: t2.start())




#root.after(1000, lambda:t3.start())
#root.after(2000, lambda:pb1.start())
window_running = True
pb1.start()
checksettings()
#root.after(20000, lambda: pb1.stop())
root.after(24000, lambda: root.withdraw())
root.after(30000, lambda: root.destroy())



if t1.is_alive() or t2.is_alive():
    pb1.stop()
    
try:
    root.mainloop()
except KeyboardInterrupt:
    print("Program Exited")

