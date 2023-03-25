from bs4 import BeautifulSoup
import urllib.request
import random

webUrl = urllib.request.urlopen("https://wwwnc.cdc.gov/eid/article/29/4/22-1538_article")
soup = BeautifulSoup(webUrl, 'html.parser')

# print(type(webUrl))

def get_links(html) -> list:
    """
    Returns a list of links attached to the <a> tags
    of the given html
    """
    lst = []

    scraper = BeautifulSoup(html, 'html.parser')
    for link in scraper.find_all('a'):
        lst.append(link.get('href'))

    return lst


def filter_key_word(links, filter_words):
    """
    Returns a new list of links from links, composed of strings
    including the given filter words.
    """

    new = []

    for item in links:
        for word in filter_words:
            if word in item and item not in new:
                new.append(item)
    return new


def get_title(html):
    """
    Returns the string title of an article given a link.
    Only works on scientific american journal
    """
    html_cast = urllib.request.urlopen(html)
    scraper = BeautifulSoup(html_cast, 'html.parser')
    title = scraper.find_all('meta')
    new_title = []
    
    for meta in title:
        try:
            if meta['name'] == 'twitter:title':
                new_title.append(meta)
        except:
            continue
            # print("An exception occured my guy")
        

    return new_title
    
    


    # text = scraper.body.get_text()
    # print(text)

    

temp = urllib.request.urlopen('https://www.scientificamerican.com/')
scientific_american_articles = filter_key_word(get_links(temp), ['/article/'])

random_article = scientific_american_articles[random.randint(0, len(scientific_american_articles) - 1)]

new_title = get_title(random_article)
title = str(new_title[0]['content'])
print(title)


