""" This uses the python libraries to build up the front end of this app

AUTHOR - SOURAV MODAK
DATE - 19 NOV 2020
INDIA

"""
import tkinter as tk
from tkinter import *
import webbrowser
from unittest.mock import call

from googlesearch import search
from tkinter.ttk import *
from get_webpages import *
from threading import Thread
import os
from pyLoadingScreen import LoadingScreen

HEIGHT = 500
WIDTH = 600


def clear_entry(event, entry):
    if entry.get() == "Company name":
        entry.delete(0, "end")

def on_click_get_news_btn(company_name):
    if company_name and company_name != "Company name":
        test_url = get_news_url(company_name)
        print(
            "Opening all the news for " + company_name + " on your " + browser + " browser. Each news is in a new tab")
        launch_web_browser(test_url)
        give_pop_up_dialog("All pages loaded", 0, 0, True)
    else:
        give_pop_up_dialog("Enter a valid company name", 0, 0, True)

def fill_nifty_text(text):
    text.delete(1.0, "end")
    nifty_companies = get_nifty_companies()
    count = 1
    for companies in nifty_companies:
        text.insert(INSERT, str(count) + ". " + companies + "\n")
        count += 1

def close_frame(root):
    root.destroy()

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

def on_click_refresh_button(text):
    fill_nifty_text(text)
    give_pop_up_dialog("The list has been refreshed", 0, 0, True)

def on_click_nifty_btn():

    page1 = tk.Tk()
    page1.title("Nifty Companies")

    canvas1 = tk.Canvas(page1, height=HEIGHT, width=WIDTH)
    canvas1.pack()

    background_label1 = tk.Label(page1, bg='#80c1ff')
    background_label1.place(relwidth=1, relheight=1)

    frame = tk.Frame(page1, bg='#80c1ff', bd=5)
    frame.place(relx=0, rely=0, relwidth=0.75, relheight=1)

    text = tk.Text(frame, font=40)
    text.place(relwidth=0.7, relheight=1)

    button = tk.Button(frame, text="Refresh", font=40, command=lambda: on_click_refresh_button(text))
    button.place(relx=0.7, relheight=0.1, relwidth=0.3)

    fill_nifty_text(text)

    page1.mainloop()
    return

def progressbar(frame):
    progress = Progressbar(frame, orient=HORIZONTAL, length=100, mode='indeterminate')
    progress.place(relx=0.5, rely=0.5, relwidth=0.5, anchor="n")
    progress.pack(pady=20)
    frame.update_idletasks()
    time.sleep(1)

def download(query):
    try:
        wbbrowser = webbrowser.get("windows-default")
    except:
        wbbrowser = webbrowser.get("macosx")
    output = search("download "+query, lang='en', num=10, stop=10, pause=2)
    output = list(output)
    wbbrowser.open_new_tab(output[0])
    quit()

def loading_screen():
    frame = give_pop_up_dialog("Loading... Please wait...", 100, 200, False)

def gui():

    x=0
    #x = os.system("git")
    import subprocess
    try:
        result = subprocess.run("git", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except FileNotFoundError as e:
        print("git not installed in the system")
        give_pop_up_dialog("Git not found in system. It is needed to maintain this software.\nWe would like to redirect to the download page.\nJust click next... next...next", 150, 500, True)
        t1 = Thread(target=loading_screen).start()
        t2 = Thread(target=download, args=(r"""git for windows""",)).start()
        quit()

    x = os.system(r"""start "" "C:\Program Files\Mozilla Firefox\firefox.exe" """)
    os.system("taskkill /IM firefox.exe /F")
    print(x)
    if x != 0:
        print("Mozilla firefox not found in System")
        give_pop_up_dialog("Mozilla firefox not found in System. Redirecting to the download page", 150, 500, True)
        t3 = Thread(target=loading_screen).start()
        t4 = Thread(target=download, args=(r"""mozilla firefox""",)).start()
        quit()

    root = tk.Tk()
    root.title("StockALL")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    def callback(event=None):
        x = entry.get()
        on_click_get_news_btn(x)

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    entry = tk.Entry(frame, font=40)
    frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')
    frame.bind("<Return>", callback)

    entry.place(relwidth=0.65, relheight=1)
    entry.insert(0, 'Company name')
    entry.bind("<Button-1>", lambda event: clear_entry(event, entry))
    entry.bind("<Return>", callback)

    button = tk.Button(frame, text="Get news", font=40, command=lambda: on_click_get_news_btn(entry.get(), root))
    button.place(relx=0.7, relheight=1, relwidth=0.3)


    frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
    frame1.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1, anchor='n')

    button1 = tk.Button(frame1, text="Nifty Companies", font=40, command=lambda: on_click_nifty_btn())
    button1.place(relheight=1, relwidth=1)

    root.mainloop()

def main():

    if len(sys.argv) > 1:
        choice = sys.argv[1]
        if choice == "1":
            console()
        else:
            gui()
    else:
        gui()

main()