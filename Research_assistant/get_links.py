from googlesearch import search
import requests
from bs4 import BeautifulSoup
from flask import Blueprint, render_template, request, redirect
# query = input('Enter the keywords for the search: ')

get_links_file = Blueprint('get_links_file', __name__, template_folder="templates")

@get_links_file.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == 'GET':
        return render_template("index.html")
    if request.method == 'POST':
        query = request.form['query']
        print(query)
        # Searches google for the key words entered by the user
        # store the links in an array 
        links_arr = []
        for results in search(query):
            # print(results)
            links_arr.append(results)
        # print(len(links))
        
        print('Reached 1')
        # create a class for each link which contains the scraped info etc 
        class Links(object):
            # the link
            # the scraped text
            # number of keyword matches
            def __init__(self, link, scraped_text, num_keywords):
                self.link = link
                self.scraped_text = scraped_text
                self.num_keywords = num_keywords
                
        # need to store the objects in an array so they can be accessed later
        links_obj_arr = []

        # loop throughs the array of links and extracts the relevant information to get the keyword matches
        # scrape the first link and count the number of keyword matches
        print('Reached 2')
        for i in range(len(links_arr)):
            # using the request lib get the html from the links gathered above
            url = links_arr[i]
            r = requests.get(url)
            html_doc = r.text
            # creating the bs4 object
            soup = BeautifulSoup(html_doc, 'html.parser')
            # extracting all the text from the html
            all_text = soup.get_text()
            #print(all_text)

            # count the number of instances of the query found in the document
            num_keywords = 0
            all_text_length = len(all_text)
            query_length = len(query)
            buffer = ""
            for i in range(0, all_text_length - query_length + 1):
                if query[0] in all_text[i]:
                    buffer = all_text[i:i + query_length]
                    #print(buffer)
                    if query in buffer:
                        num_keywords += 1
                        #print(num_keywords)

            links_obj = Links(url, soup, num_keywords)
            links_obj_arr.append(links_obj)
            #print(links_obj.scraped_text)
        print('Reached 3')
        # print(links_obj_arr)
            # to_str_i = str(i)
            # to_str_key = str(num_keywords)
            # print('link: ' + to_str_i + to_str_key)
        
        
        '''
        IF SORTING FROM SCRATCH
        # sort the links by greatest number of keyword matches
        # loop through the array of links objects and sort using just the num_keywords attribute
            #  utilizing merge sort
        # print out the corresponding link
        '''

        # sorting the links object array using the sort method 
        # key(any function) will be a lambda function that simply extract the num_keywords 
        print('Reached 4')
        links_obj_arr.sort(key = lambda x:x.num_keywords, reverse=True)

        # def grab_paragraph():
        #     pass

        # create a class that stores all the relevant information per search
        # this includes: query, links, final result
        # this class must inherit the Links 
        print('Reached 5')
        class Final_Result(Links):
            def __init__(self, query):
                self.query = query
        return links_obj_arr[0].link
                