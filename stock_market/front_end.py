""" This uses the python libraries to build up the front end of this app

AUTHOR - SOURAV MODAK
DATE - 19 NOV 2020
INDIA

"""
import tkinter as tk
from tkinter import *
from tkinter.ttk import *
import os
from get_webpages import *

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
        give_pop_up_dialog("All pages loaded")
    else:
        give_pop_up_dialog("Enter a valid company name")

def fill_nifty_text(text):
    text.delete(1.0, "end")
    nifty_companies = get_nifty_companies()
    count = 1
    for companies in nifty_companies:
        text.insert(INSERT, str(count) + ". " + companies + "\n")
        count += 1

def close_frame(root):
    root.destroy()

def give_pop_up_dialog(message):
    dialog = tk.Tk()
    dialog.title("FYI")

    canvas1 = tk.Canvas(dialog, height=100, width=300)
    canvas1.pack()

    frame = tk.Frame(dialog, bg='#80c1ff', bd=5)
    frame.place(relx=0, rely=0, relwidth=1, relheight=1)

    label = tk.Label(frame, text=message, font=40)
    label.place(relx=0.5, rely=0.5, anchor=CENTER)

    button = tk.Button(frame, text="OK", font=40, command=lambda: close_frame(dialog))
    button.place(relx=0.5, rely=0.8, height=20, width=50, anchor=CENTER)

    dialog.lift()
    dialog.mainloop()

def on_click_refresh_button(text):
    fill_nifty_text(text)
    give_pop_up_dialog("The list has been refreshed")

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

def gui():
    root = tk.Tk()
    root.title("StockALL")

    canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
    canvas.pack()

    background_image = tk.PhotoImage(file='background.png')
    background_label = tk.Label(root, image=background_image)
    background_label.place(relwidth=1, relheight=1)

    frame = tk.Frame(root, bg='#80c1ff', bd=5)
    frame.place(relx=0.5, rely=0.3, relwidth=0.75, relheight=0.1, anchor='n')

    entry = tk.Entry(frame, font=40)
    entry.place(relwidth=0.65, relheight=1)
    entry.insert(0, 'Company name')
    entry.bind("<Button-1>", lambda event: clear_entry(event, entry))

    button = tk.Button(frame, text="Get news", font=40, command=lambda: on_click_get_news_btn(entry.get()))
    button.place(relx=0.7, relheight=1, relwidth=0.3)

    progress = Progressbar(root, orient=HORIZONTAL, length=100, mode='indeterminate')
    progress.place(relx=0.5, relheight=0.1, relwidth=0.3)

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