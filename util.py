import requests
from xml.etree import ElementTree
from model import News
import browser_cookie3
import constants
import nltk
from string import punctuation
from collections import Counter


def get_news_from_item(item, location):
    news = News.News()
    news.hydrate(item, location)
    return news


def get_news_feed_by_location(location):
    """
    :param location:
    :return a list of news ( objects ):
    """
    url = constants.GEO_URL + location
    cookies = browser_cookie3.chrome(domain_name='.google.com')
    response = requests.get(url=url, cookies=cookies)
    root = ElementTree.fromstring(response.content)
    channel = root.find(constants.CHANNEL_TAG)
    news_list = []
    for item in channel.iter(constants.ITEM_TAG):
        news_list.append(get_news_from_item(item, location))

    return news_list


def get_most_used_words_by_location(news_list):
    """
    :param news_list: list of news (objects)
    :return: str most used word, if more than one returns a list
    """
    stopwords = set(nltk.corpus.stopwords.words('english'))
    key_words = Counter()
    for news in news_list:
        print(news.description)
        key_words.update(w.lower().rstrip(punctuation) for w in news.description.split(" ") if w not in stopwords)

    return dict((k, v) for k, v in key_words.most_common(10))
