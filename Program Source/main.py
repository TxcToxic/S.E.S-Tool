# Created by -TOXIC-#1835 with <3
# First HWID lock project
# CHANGE WEBSITE CHECKS IF YOU'RE CHANGING ANYTHING!

import os
import tkinter as tk
from tkinter import messagebox as mb
import webbrowser
import requests
import random
import string
import subprocess


devmode = False
tVersion = "1.2.1"


def updateCheck():
    if devmode:
        return True
    cVersion = requests.get("https://gtav-online-community.com/ses/index.json").json()["version"]  # Change this!
    av = requests.get("https://gtav-online-community.com/ses/index.json").json()["available"]  # Change this!
    if av is False:
        return False
    if tVersion == cVersion:
        return True
    else:
        return False


def hwidCheck():
    if devmode:
        return True
    hwidlock = requests.get("https://gtav-online-community.com/ses/index.json").json()["hwidlock"]  # Change this!
    if hwidlock is False:
        return True
    # hwidList = []
    cHwid = str(str(subprocess.check_output('wmic csproduct get uuid')).strip().replace(r"\r", "").split(r"\n")[1].strip())
    hwidPaste = requests.get("https://gtav-online-community.com/ses/hwids").text  # Change this!
    # You can also use Pastebin but RAW!
    if cHwid in hwidPaste:
        return True
    else:
        return False


def rGM():
    def function():
        try:
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\download\*.*')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\*.db')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\cache\lua')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\media\*.*')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\data\*.*')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\demos\*.*')
            os.system(rf'DEL /s /q /f "C:\Program Files (x86)\Steam\steamapps\common\Steamworks Shared\*.*')
            os.system(rf'DEL /s /q /f "C:\Program Files (x86)\Steam\userdata\*.*')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\saves\*.*')
            os.system(rf'DEL /s /q /f "{path.get()}\garrysmod\*.dt')
            return True
        except:
            return False
    if function():
        subprocess.Popen(rf'explorer /path,"{path.get()}\garrysmod"')
        mb.showinfo(title="Success", message="All succeed, the bypass was triggered check if it worked.\n\n"
                                             "Do not forget to change IP & Steam Account.\n\nTool by -TOXIC-#1835")
    else:
        # this case will never come up!
        mb.showerror(title="Error", message="Failed to bypass Garry's Mod, try run this Program as Administrator\n\n"
                                            "Tool by -TOXIC-#1835")
        root.destroy()


def hTD():
    def openPVPN():
        webbrowser.open("https://protonvpn.com/", new=True)

    secRoot = tk.Tk()
    secRoot.title("How to use bypass")
    secRoot.config(bg="#131313")
    secRoot.resizable(height=False, width=False)
    secRoot.geometry("430x200")
    secRoot.iconbitmap("./bin/ses.ico")
    tk.Label(secRoot, text="1) Enter the path else program won't work\n"
                           '2) Click on "-> Bypass GMod <-"\n'
                           '3) Use a VPN (everytime a other server!)\n'
                           '4) Switch steam account\n\n'
                           'As VPN you can use ProtonVPN (if you need free)',
             font=("Consolas", 12), bg="#131313", fg="#003ac2").pack()
    tk.Button(secRoot, text="Open ProtonVPN site\n", font=("Consolas", 12, "underline"), bg="#131313", fg="#003ac2"
              , borderwidth=0, command=openPVPN).pack()
    tk.Label(secRoot, text="Tool by -TOXIC-#1835", font=("Arial Black", 6),
             bg="#131313", fg="#ff0000").pack(side="bottom")


def genPW():
    chars = string.digits + string.ascii_letters + string.punctuation
    num = 5
    num2 = 0
    secRoot = tk.Tk()
    secRoot.title("S.E.S Password Generator")
    secRoot.config(bg="#131313")
    secRoot.resizable(height=False, width=False)
    secRoot.geometry("400x400")
    secRoot.iconbitmap("./bin/ses.ico")
    secRoot.clipboard_clear()
    tk.Label(secRoot, text="S.E.S Tool PwGen", font=("Consolas", 30, "underline", "bold"), bg="#131313", fg="#003ac2").pack()
    tk.Label(secRoot, text="Tool by -TOXIC-#1835", font=("Arial Black", 6), bg="#131313", fg="#ff0000").pack(side="bottom")
    while num > 0:
        pw = "".join(random.choice(chars) for _ in range(32))
        tk.Label(secRoot, text=f"----------------------------------", font=("Consolas", 12),
                 bg="#131313", fg="#003ac2").pack()
        tk.Label(secRoot, text=f"{pw}", font=("Consolas", 12), bg="#131313", fg="#003ac2").pack()
        num2 += 1
        secRoot.clipboard_append(f'PW [{num2}]: {pw}\n')
        num -= 1
    tk.Label(secRoot, text=f"----------------------------------", font=("Consolas", 12),
             bg="#131313", fg="#003ac2").pack()
    tk.Label(secRoot, text=f"All passwords copied to clipboard!", font=("Consolas", 12),
             bg="#131313", fg="#003ac2").pack()


def sGM():
    os.system("start steam://rungameid/4000")


root = tk.Tk()
root.title(f"S.E.S || Version: {tVersion}")
root.config(bg="#131313")
root.resizable(height=False, width=False)
root.geometry("480x260")
root.iconbitmap("./bin/ses.ico")
tk.Label(root, text="S.E.S Tool", font=("Consolas",  30, "underline", "bold"), bg="#131313", fg="#003ac2").pack()
tk.Label(root, text="Tool by -TOXIC-#1835", font=("Arial Black", 6), bg="#131313", fg="#ff0000").pack(side="bottom")
if not updateCheck():
    tk.Label(root, text="OUTDATED OR UNAVAILABLE!", font=("Consolas", 12), bg="#131313", fg="#003ac2").pack()
    webbrowser.open("https://gtav-online-community.com/ses/", new=True)
    mb.showerror(title="Invalid Version", message="The tool is outdated or unavailable download the new version from"
                                                  " the website!")
    root.destroy()
if not hwidCheck():
    tk.Label(root, text="Your HWID is invalid!", font=("Consolas", 12), bg="#131313", fg="#003ac2").pack()
    webbrowser.open("https://discord.gg/6MTF772zpu", new=True)
    mb.showerror(title="Invalid HWID", message="Your HWID was not found in our Database!")
    root.destroy()
if updateCheck() and hwidCheck():
    tk.Label(root, text="The path where's GMod installed", font=("Consolas", 8), bg="#131313", fg="#003ac2").pack()
    tk.Label(root, text=r"e.g. D:\SteamLibrary\steamapps\common\GarrysMod", font=("Consolas", 8), bg="#131313", fg="#003ac2").pack()
    path = tk.Entry(root, font=("Consolas", 8), width=50, bg="#131313", fg="#003ac2", justify="center")
    path.pack()
    tk.Button(root, text="-> Bypass GMod <-", font=("Consolas", 12, "underline"), bg="#131313", fg="#003ac2",
              borderwidth=0, command=rGM).pack()
    tk.Button(root, text="How?", font=("Consolas", 12, "underline"), bg="#131313", fg="#003ac2",
              borderwidth=0, command=hTD).pack()
    tk.Button(root, text="Start Garry's Mod", font=("Consolas", 12, "underline"), bg="#131313", fg="#003ac2",
              borderwidth=0, command=sGM).pack()
    tk.Button(root, text="Generate Password", font=("Consolas", 12, "underline"), bg="#131313", fg="#003ac2",
              borderwidth=0, command=genPW).pack()

root.mainloop()
