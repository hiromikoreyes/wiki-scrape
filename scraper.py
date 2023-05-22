from bs4 import BeautifulSoup
import json
import urllib.request
import random


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
    return html.find("h1").get_text()   

def get_body_content(html, maxlen):
    """Only works for wikipedia"""
    body = ""
    body_list = []
    tags = html.find_all("p")

    for item in tags:
        body += item.get_text()
        if len(body) >= maxlen: return body[:825]
    return body[:825]


def make_json(filepath, html):
    data = []
    with open(filepath, 'r') as outfile:
        try: data = json.load(outfile)
        except: data = [] 
        data.append({"title": get_title(html), "content": get_body_content(html, 1000).strip()})
    with open(filepath, 'w') as outfile:
        outfile.write(json.dumps(data, indent=4))

def create_request(request):
    """ sends a list of dictionaries of wikipedia titles and bodies, for the first 9 related links
    """
    link = f"https://en.wikipedia.org/wiki/{request}"
    webUrl = urllib.request.urlopen(link)
    main_html = BeautifulSoup(webUrl, 'html.parser')
    link_list = whitelist_filter(get_links(main_html), '/wiki/')
    link_list = blacklist_filter(link_list, ['File:', 'Special:', 'Talk:', 'Category:', 'Help:', '(identifier)', 'Wikipedia:', '(disambiguation)'])

    send_list = []
    while len(send_list) < 6:
        link = f"https://en.wikipedia.org{link_list[random.randint(0, len(link_list) - 1)]}"
        print(link)
        url = urllib.request.urlopen(link)
        html = BeautifulSoup(url, 'html.parser')
        if {"title": get_title(html), "content": get_body_content(html, 875).strip(), "link": link} not in send_list:
            send_list.append({"title": get_title(html), "content": get_body_content(html, 875).strip(), "link": link})
    return send_list


def clean_body(body_string):
    body_string = body_string.strip()
    return body_string