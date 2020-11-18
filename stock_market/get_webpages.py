""" This is to get the webpages from the internet to scrap up the webpages

AUTHOR - SOURAV MODAK
Date - 15 NOV 2020
INDIA

"""


from googlesearch import search
import time, json
from bs4 import BeautifulSoup
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


def main():
    """ The main function """

    """number_of_run = int(input("Enter number of run\n"))
    result = performance_check(number_of_run)"""

    print("WELCOME!!! You can use this program to extract information and news on the stock market and table of companies")
    print("1. Details on nifty companies")
    print("2. Details on specific compnaies")
    print("3. Exit")
    val = input()
    if val ==  "1":
        table = get_companies_table("nifty companies")
        tuple_cnt = 0
        for tuple in table[0]:
            if re.search("name", tuple) or re.search("NAME", tuple) or re.search("Name", tuple):
                break
            tuple_cnt += 1
        list_of_companies = list()
        for row in table[1:]:
            list_of_companies.append(row[tuple_cnt])
        print(list_of_companies)



main()