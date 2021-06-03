import requests
from xml.etree import ElementTree
from model import News
import browser_cookie3
import json
import constants


def get_news_from_item(item, location):
    news = News.News()
    news.hydrate(item, location)
    return news


def get_news_feed_by_location(location):
    '''
    :param location:
    :return a list of news ( objects ):
    '''
    url = constants.GEO_URL + location
    cookies = browser_cookie3.chrome(domain_name='.google.com')
    response = requests.get(url=url, cookies=cookies)
    root = ElementTree.fromstring(response.content)
    channel = root.find(constants.CHANNEL_TAG)
    # items = channel.findall(constants.ITEM_TAG)
    news_list = []
    for item in channel.iter(constants.ITEM_TAG):
        news_list.append(get_news_from_item(item, location))

    return json.dumps([ob.__dict__ for ob in news_list])
