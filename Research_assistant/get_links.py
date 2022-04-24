from googlesearch import search
import requests
from bs4 import BeautifulSoup

query = input('Enter the keywords for the search: ')

# Searches google for the key words entered by the user
# store the links in an array 
links_arr = []
for results in search(query):
    # print(results)
    links_arr.append(results)
# print(len(links))

# create a class for each link which contains the scraped info etc 
class Links(object):
    # the link
    # the scraped text
    # number keywords
    def __init__(self, link, scraped_text, num_keywords):
        self.link = link
        self.scraped_text = scraped_text
        self.num_keywords = num_keywords
        
# need to store the objects in an array so they can be accessed later
links_obj_arr = []
# make another array that contains the keyword matches
# scrape the first link and count the number of keyword matches
for i in range(len(links_arr)):
    # using the request lib get the html from the links gathered above
    url = links_arr[i]
    r = requests.get(url)
    html_doc = r.text
    # creating the bs4 object
    soup = BeautifulSoup(html_doc, 'html.parser')
    # extracting all the text from the html
    all_text = soup.get_text()
    # count the number of instances of the query found in the document
    num_keywords = 0
    for i in all_text:
        if query in all_text:
            num_keywords += 1
    links_obj = Links(url, soup, num_keywords)
    links_obj_arr.append(links_obj)
print(links_obj_arr)
    # to_str_i = str(i)
    # to_str_key = str(num_keywords)
    # print('link: ' + to_str_i + to_str_key)

# create a class that stores all the relevant information per search
# this includes: query, links, final result
# another class per link which stores the scraped info, num of keyword matches etc