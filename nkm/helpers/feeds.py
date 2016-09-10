import requests
import re
from bs4 import BeautifulSoup


def get_feeds(search_term):
    return google_search_links(search_term)


def google_search_links(search, re_match=None):
    """
    Function to return links from google search
    https://github.com/aviaryan/pythons/blob/master/Others/GoogleSearchLinks.py
    """
    name = search
    name = name.replace(' ', '+')
    url = 'http://www.google.com/search?q=%s&tbm=nws' % name
    url += '&tbs=qdr:d'  # past 24 hrs
    response = requests.get(url)
    html = response.text.encode('utf-8').decode('ascii', 'ignore')
    soup = BeautifulSoup(html, 'lxml')  # phast
    links = []
    for h3 in soup.find_all('h3'):
        link = h3.a['href']
        link = re.sub(r'^.*?=', '', link, count=1)  # prefixed over links \url=q?
        link = re.sub(r'\&sa.*$', '', link, count=1)  # suffixed google things
        link = re.sub(r'\%.*$', '', link)  # NOT SAFE
        if re_match is not None:
            if re.match(re_match, link, flags=re.IGNORECASE) is None:
                continue
        links.append(link)  # link
        # print(h3.get_text()) # text
    return links
