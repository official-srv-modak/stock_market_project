""" This uses the python libraries to build up the front end of this app

AUTHOR - SOURAV MODAK
DATE - 19 NOV 2020
INDIA

"""
import tkinter as tk
import requests, os
from get_webpages import *

HEIGHT = 500
WIDTH = 600


def clear_entry(event, entry):
    entry.delete(0, "end")

def on_click_get_news_btn(company_name):

    test_url = get_news_url(company_name)
    print("Opening all the news for " + company_name + " on your " + browser + " browser. Each news is in a new tab")
    launch_web_browser(test_url)

def on_click_nifty_btn():
    nifty_companies = get_nifty_companies()
    count = 1
    while count <= len(nifty_companies):
        print("Opening all the news for " + nifty_companies[
            count - 1] + " on your " + browser + " browser. Each news is in a new tab")
        test_url = get_news_url(nifty_companies[count - 1])
        launch_web_browser(test_url)
        while True:
            val = input(
                "Type \"next\" or \"-\" and press enter to go to the next news. REMEBER TO CLOSE THE BROWSER. \"STOP\" and \"?\" to halt\n")
            if val == "next" or val == "-":
                break
            elif val == "stop" or val == "?":
                count = len(nifty_companies) + 1
                break
        count += 1
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

    frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
    frame1.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1, anchor='n')

    button1 = tk.Button(frame1, text="Nifty Companies", font=40, command=lambda: on_click_get_news_btn(entry.get()))
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