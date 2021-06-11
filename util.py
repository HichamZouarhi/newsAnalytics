import requests
from xml.etree import ElementTree
from model import News
import browser_cookie3
import constants
import nltk
from string import punctuation
from collections import Counter
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
import spacy
from spacy import displacy
import en_core_web_sm


def get_news_from_item(item, location, persist):
    news = News.News()
    news.hydrate(item, location)
    if persist:
        news.save()

    return news


def get_news_feed_by_location(location, persist=False):
    """
    :param location:
    :param persist: save to db
    :return: list of news
    """
    url = constants.GEO_URL + location
    cookies = browser_cookie3.chrome(domain_name='.google.com')
    response = requests.get(url=url, cookies=cookies)
    root = ElementTree.fromstring(response.content)
    channel = root.find(constants.CHANNEL_TAG)
    news_list = []
    for item in channel.iter(constants.ITEM_TAG):
        news_list.append(get_news_from_item(item, location, persist))

    return news_list


def get_most_used_words_by_location(news_list, limit=10):
    """
    :param limit:
    :param news_list: list of news (objects)
    :return: str most used word, if more than one returns a list
    """
    ps = PorterStemmer()
    stopwords = set(nltk.corpus.stopwords.words('english'))
    key_words = Counter()
    for news in news_list:
        clean_text = BeautifulSoup(news.description, "lxml").text
        key_words.update(ps.stem(w.lower().rstrip(punctuation)) for w in clean_text.split(" ") if w not in stopwords)

    return dict((k, v) for k, v in key_words.most_common(limit))


def get_subjects_from_news_by_geo(news_list, subject=constants.SPACY_GPE, limit=10):
    """
    :param subject:
    :param limit:
    :param news_list:
    :return: most spoken of subject / country based on spacy extraction
    """
    nlp = en_core_web_sm.load()
    subjects = Counter()
    for news in news_list:
        doc = nlp(news.title)
        subjects.update(entity.text.lower() for entity in doc.ents if entity.label_ == subject)

    return dict((k, v) for k, v in subjects.most_common(limit))


def get_sources_by_geo(news_list, limit=10):
    """
    :param news_list:
    :param limit:
    :return: dict of the most speaking sources bout a location
    """
    sources = Counter()
    sources.update(news.source for news in news_list)
    return dict((k, v) for k, v in sources.most_common(limit))
