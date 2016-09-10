import requests
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
    # return
    return {
        'title': title,
        'content': doc.summary(html_partial=True)
    }
