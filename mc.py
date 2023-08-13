import tkinter as tk
from tkinter.font import Font
import os
from ctypes import windll, byref, sizeof, c_int
import ctypes, getpass
windll.shcore.SetProcessDpiAwareness(1)
myappid = u'vpun215.eclient.idk.1.0' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
# WINDOW CREATION
win = tk.Tk()
win.title("Mods")
win.iconbitmap("mod.ico")
username = getpass.getuser()
modsfolder = f"C://users//{username}//AppData//Roaming//.minecraft//mods"
geo = win.geometry
geo("300x500+400+400")
win['bg'] = '#222222'
# get the list of files
flist = os.listdir(modsfolder)
custom_font1 = Font(family="SF Pro Display", size=12)
lbox = tk.Listbox(win,borderwidth=0, highlightthickness=0, height=30)
lbox.configure(background="#222222", foreground="white", font=custom_font1)
lbox.pack()

# THE ITEMS INSERTED WITH A LOOP
for item in flist:
    lbox.insert(tk.END, item)

win.mainloop()
