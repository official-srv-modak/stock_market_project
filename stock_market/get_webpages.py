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
        best_search_url = url
        break
    return get_table_data(best_search_url)



def main():
    """ The main function """

    """number_of_run = int(input("Enter number of run\n"))
    result = performance_check(number_of_run)"""

    print("WELCOME!!! You can use this program to extract information and news on the stock market and table of companies")


main()