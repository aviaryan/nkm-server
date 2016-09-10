import requests
from readability import Document


def get_page_html(url):
    """
    Gets HTML of a page
    """
    response = requests.get(url, follow_redirects=True)
    return response.text


def extract_article_info(text):
    """
    Gets simplified page from the text
    Uses readability module
    """
    doc = Document(text)
    return {
        'title': doc.title(),
        'content': doc.summary()
    }
