""" This is used to update the code

AUTHOR - SOURAV MODAK
DATE - 20 NOV 2020
INDIA

"""

import os, subprocess
import tkinter as tk
from tkinter import *

repository_url = "https://github.com/official-srv-modak/StockAll.git"
update_file_path = "update.bat"

def give_pop_up_dialog(message, height, width, button_needed):
    dialog = tk.Tk()
    dialog.title("FYI")

    if height and width:
        canvas1 = tk.Canvas(dialog, height=height, width=width)
        canvas1.pack()
    else:
        canvas1 = tk.Canvas(dialog, height=100, width=300)
        canvas1.pack()

    frame = tk.Frame(dialog, bg='#80c1ff', bd=5)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(frame, text=message, font=40)
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    if button_needed:
        button = tk.Button(frame, text="OK", font=40, command=lambda: close_frame(dialog))
        button.place(relx=0.5, rely=0.8, height=20, width=50, anchor=CENTER)

    dialog.lift()
    dialog.after(10000, lambda:dialog.destroy())
    dialog.mainloop()
    return dialog

def get_local_revision():
    result = subprocess.run("git log -1", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    local_version = str(result.stdout).split("'")[1].split("\\")[0].split("commit")[1].strip()
    print(local_version)
    return local_version

def get_remote_repo_version(repository_url):
    result = subprocess.run("git ls-remote "+repository_url+" HEAD", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    remote_version = str(result.stdout).split("'")[1].split("\\")[0]
    print(remote_version)
    return remote_version

def update_file():
    filehandle = open(update_file_path, 'w')
    StartName = "StockAll.exe"
    filehandle.write("timeout 5\ntaskkill /IM \"StockAll.exe\"\nwmic Path win32_process Where \"CommandLine Like '"+StartName+"'\" Call Terminate\n")
    filehandle.write("git stash\ngit pull\n")
    filehandle.write("timeout 5\nStockAll.exe\nexit\n")
    filehandle.close()
    os.system("start \"\" "+update_file_path)

def check_and_update_package():
    local_version = get_local_revision()
    remote_version = get_remote_repo_version(repository_url)
    if local_version != remote_version:
        give_pop_up_dialog("New update detected, the system will update", 100, 400, True)
        update_file()


def update():

    check_and_update_package()

#update()