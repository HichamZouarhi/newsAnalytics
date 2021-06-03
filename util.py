import requests
from xml.etree import ElementTree
from model import News
import browser_cookie3
import json

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
    # print("getting browser cookies")
    cookies = browser_cookie3.chrome(domain_name='.google.com')
    # print("sending GET request")
    response = requests.get(url=url, cookies=cookies)
    tree = ElementTree.fromstring(response.content)
    items = tree.findall(constants.ITEM_TAG)
    news_list = []
    for item in items:
        print(item)
        news_list.add(get_news_from_item(item, location))

    return json.dumps(news_list)
