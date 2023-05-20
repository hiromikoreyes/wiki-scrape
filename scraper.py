from bs4 import BeautifulSoup
import json
import urllib.request
import random

name = input("insert search thingy: ")
link = f"https://en.wikipedia.org/wiki/{name}"
webUrl = urllib.request.urlopen(link)
main_html = BeautifulSoup(webUrl, 'html.parser')
print(link)


def get_links(html) -> list:
    """
    Returns a list of links attached to the <a> tags
    of the given html
    """
    lst = []
    for link in html.find_all('a'):
        lst.append(str(link.get('href')))

    return lst


def whitelist_filter(links, filter_key):
    """
    Returns a new list of links from links, composed of strings
    including the given filter_key.
    """

    new = []
    for link in links:
        if link.find(filter_key) == 0 and link not in new:
            new.append(link)
    return new


def blacklist_filter(links, filter_list):
    new = []
    addFlag = True
    for link in links:
        addFlag = True
        for word in filter_list:
            if link.find(word) != -1 and link not in new:
                addFlag = False
        if(addFlag == True): new.append(link)
    return new

# def get_body_content(html):
#     """Only works for wikipedia"""
#     html.p

mess_list = get_links(main_html)
link_list = whitelist_filter(mess_list, '/wiki/')
link_list = blacklist_filter(link_list, ['File:', 'Special:', 'Talk:', 'Category:', 'Help:', '(identifier)', 'Wikipedia:', '(disambiguation)'])

# for x in link_list:
#     print(x)
# print(mess_list)

