import requests
from xml.etree import ElementTree
from model import News

import constants

def get_news_from_item(item, location):
    news = News()
    news.hydrate(item, location)
    return news


def get_news_feed_by_location(location):
    '''
    :param location:
    :return a list of news ( objects ):
    '''
    url = constants.GEO_URL + location
    response = requests.get(url=url)
    tree = ElementTree.fromstring(response.content)
    items = tree.findall(constants.ITEM_TAG)
    news_list = []
    for item in items:
        news_list.add(get_news_from_item(item, location))

    return news_list
