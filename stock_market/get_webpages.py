""" This is to get the webpages from the internet to scrap up the webpages

AUTHOR - SOURAV MODAK
Date - 15 NOV 2020
INDIA

"""


from googlesearch import search
import webbrowser, selenium
import sys
import time, json
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import urllib.request
from pprint import pprint
from html_table_parser import HTMLTableParser
import pandas as pd
import os
import re

"""from nltk.corpus import wordnet as wn
nouns = {x.name().split('.', 1)[0] for x in wn.all_synsets('n')}"""
try:
    # For Python 3.0 and later
    from urllib.request import urlopen
except ImportError:
    # Fall back to Python 2's urllib2
    from urllib2 import urlopen


def get_table_data(URL):
    """ This is to get the tabular data from the websites"""

    def url_get_contents(url):
        print("Requesting information to... "+url)
        req = urllib.request.Request(url=url)
        f = urllib.request.urlopen(req)
        return f.read()

    xhtml = url_get_contents(URL).decode('utf-8')
    print("Success!!! Parsing")
    p = HTMLTableParser()
    p.feed(xhtml)
    return (p.tables[1])
    """print("\n\nPANDAS DATAFRAME\n")
    print(pd.DataFrame(p.tables[1]))"""

def get_companies_table(query):
    """ This will just use google search and get the tabular from first and only first search result. The problem here
    is if the query is not proper enough for the google servers to generate the tabular search result, you are doomed"""

    output = search(query, lang='en', num=10, stop=10, pause=2)
    for url in output:
        try:
            table = get_table_data(url) #filter on the table variable
            return table
        except:
            print("Sorry no table in the url... Trying another")
            continue

def filter_table(table):
    """ This is to add filter to the table s that we dont pick up useless tables
    It returns True or False depending upon if the table is accepted. Sometimes it can return the table
    instead of a True which can work as fine for an if statement like :- if filter table :"""


    for row in table:
        for tuple in row[0:1]:
            if tuple in nouns:
                table = table[0:]

    return False

def get_news_url(company_name):
    """ This will return the news of all the companies that is entered as the argument"""

    #company_name = list_of_companies[0]
    query = "news of "+company_name
    output = search(query, lang='en', num=10, stop=10, pause=2)
    out = list()
    output_list = list()

    for url in output:
        output_list.append(url)
    return output_list

def get_nifty_companies():
    """ Return the list of all the nifty companies"""

    table = get_companies_table("nifty companies")
    tuple_cnt = 0
    for tuple in table[0]:
        if re.search("name", tuple) or re.search("NAME", tuple) or re.search("Name", tuple):
            break
        tuple_cnt += 1
    list_of_companies = list()
    for row in table[1:]:
        list_of_companies.append(row[tuple_cnt])
    #print(list_of_companies)
    return list_of_companies


def launch_web_browser(sites):
    print('Opening Sites')

    browser = "firefox"

    wbbrowser = webbrowser.get(browser)
    count = 0
    try:
        for url in sites:
            if count == 0:
                wbbrowser.open_new(url.strip())
                #time.sleep(1)
            else:
                wbbrowser.open_new_tab(url.strip())
                time.sleep(1)
            count += 1
    except Exception as e:
        print(e)

def main():
    """ The main function """

    print("WELCOME!!! You can use this program to extract information and news on the stock market and table of companies")
    while True:
        print("1. Details on nifty companies")
        print("2. Details on specific compnaies")
        print("3. Exit")
        val = input()
        if val == "1":
            nifty_companies = get_nifty_companies()
            count = 1
            while count <= len(nifty_companies):
                print("Opening all the news for " + nifty_companies[
                    count - 1] + " on your default browser. Each news is in a new tab")
                test_url = get_news_url(nifty_companies[count - 1])
                launch_web_browser(test_url)
                while True:
                    val = input(
                        "Type \"next\" or \"-\" and press enter to go to the next news. REMEBER TO CLOSE THE BROWSER\n")
                    if val == "next" or val == "-":
                        break
                    elif val == "stop" or val == "?":
                        count = len(nifty_companies) + 1
                        break
                count += 1
        elif val == "2":
            company_name = input("Enter the company name : \n")
            test_url = get_news_url(nifty_companies[count - 1])
            launch_web_browser(test_url)

        elif val == "3":
            print("Bye bye!")
            quit()

main()