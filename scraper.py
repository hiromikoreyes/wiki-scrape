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

def get_title(html):
    return html.find(class_="mw-page-title-main").get_text()   

def get_body_content(html, maxlen):
    """Only works for wikipedia"""
    body = ""
    body_list = []
    tags = html.find_all("p")

    for item in tags:
        body += item.get_text()
        if len(body) >= maxlen: return body
    return body

def make_json(html):
    data = {"title": get_title(html), "content": get_body_content(html, 1000).strip()}
    json_object = json.dumps(data, indent=4)
    with open("sample.json", 'w') as outfile:
        outfile.write(json_object)

def update_json(filepath, html):
    data = []
    with open(filepath, 'r') as outfile:
        try: data = json.load(outfile)
        except: data = [] 
        data.append({"title": get_title(html), "content": get_body_content(html, 1000).strip()})
    with open(filepath, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))


mess_list = get_links(main_html)
link_list = whitelist_filter(mess_list, '/wiki/')
link_list = blacklist_filter(link_list, ['File:', 'Special:', 'Talk:', 'Category:', 'Help:', '(identifier)', 'Wikipedia:', '(disambiguation)'])
# make_json(main_html)
update_json("sample.json", main_html)

# f = open('sample.json',)
# data = json.load(f)

# print(data)

# for x in link_list:
#     print(x)
# print(mess_list)

