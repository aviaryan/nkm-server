import requests
import re
from bs4 import BeautifulSoup
from readability import Document


def get_page_html(url):
    """
    Gets HTML of a page
    """
    response = requests.get(url)
    return response.text


def extract_article_info(text):
    """
    Gets simplified page from the text
    Uses readability module
    """
    doc = Document(text)
    # safe fetch title
    title = doc.short_title()
    if not title:
        title = doc.title()
    # content
    content = doc.summary(html_partial=True)
    image = get_page_image(doc.content())
    # return
    return {
        'title': title,
        'content': content,
        'image': image
    }


def get_page_image(page):
    """
    Gets the link to image of the page
    """
    soup = BeautifulSoup(page, 'lxml')
    tags = soup.findAll('img')
    tag = ''
    good_links = []
    for tag in tags:
        if tag.get('src') and tag['src'].startswith('http'):
            good_links.append(tag['src'])
    if len(good_links) > 0:
        return good_links[int(len(good_links) / 2)]
    return None


def get_domain_from_url(url):
    """gets the root domain from url"""
    match = re.findall(r'://.*?(/.*$)', url)
    if len(match) == 0:
        return url
    url = url.replace(match[0], '')
    return url
