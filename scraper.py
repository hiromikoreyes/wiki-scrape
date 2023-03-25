from bs4 import BeautifulSoup
import urllib.request

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


def get_content(html):
    """
    Returns the string content of an article given a link.
    Only works on scientific american journal
    """
    scraper = BeautifulSoup(html)
    


    
    





temp = urllib.request.urlopen('https://www.scientificamerican.com/')
lst = get_links(temp)
new = filter_key_word(lst, ['/article/'])

for item in new:
    print(item)

# print(soup.get_text())
# f = open("sample.txt", "w")
# content = soup.body.get_text()



# print(content)
# f.write(content)
# f.close()




