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


def get_localised_news_webpages(location_city, language):
    """This is the method which will give the localised webpages from the search based on the location of the user"""

    start_time = time.time()
    query = location_city + " news"
    output_list = list()
    output = search(query, lang=language, tld="co.in", num=10, stop=10, pause=2)
    for url in output:
        if not url.endswith("/"):
            output_list.append(url)
    print("SEARCH TIME : --- %s seconds ---" % (time.time() - start_time))
    return output_list

def get_webpage_data_list(url_list):
    """This is to return the webpages in the json format"""

    output_list = list()
    start_time = time.time()
    for url in url_list:
        try:
            response = urlopen(url)
            data = response.read()
        except Exception as e:
            print("Exception")
        #data = BeautifulSoup(data, 'html.parser')
        output_list.append(data)
    time_taken = (time.time() - start_time)
    print("WEBPAGE EXTRACTION : --- %s seconds ---" % time_taken)
    return output_list

def performance_check(number_of_run):
    """ Just to check the performance and get the avg time of execution"""

    start_time_total = time.time()
    time_list = list()
    count = 1
    sum = 0
    while count <= number_of_run:
        start_time = time.time()
        get_webpage_data_list(get_localised_news_webpages("visakhapatnam", "en"))
        print("Done")
        time_taken = (time.time() - start_time)
        time_list.append(time_taken)
        sum += time_taken
        avg = sum / count
        count += 1

    output_list = list()
    output_list.append(time_list)
    output_list.append(avg)

    print("TOTAL TIME for " + str(count - 1)+" RUNS : --- %s seconds ---" % (time.time() - start_time_total))
    return output_list

def get_companies_table(query):
    """ This will just use google search and get the tabular from first and only first search result. The problem here
    is if the query is not proper enough for the google servers to generate the tabular search result, you are doomed"""

    output = search(query, lang='en', num=10, stop=10, pause=2)
    for url in output:
        best_search_url = url
        break
    get_table_data(best_search_url)

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
    pprint(p.tables[1])
    """print("\n\nPANDAS DATAFRAME\n")
    print(pd.DataFrame(p.tables[1]))"""


"""number_of_run = int(input("Enter number of run\n"))
result = performance_check(number_of_run)"""

print(get_companies_table("nifty companies"))