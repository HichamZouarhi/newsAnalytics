from flask import Flask

import constants
import util
import json
from model.News import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/database.db"
db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/newsbygeo/<string:location>/<string:history>')
def get_news_by_geo(location, history=False):
    news_list = []
    if history:
        news_list = util.get_news_from_db_by_location(location)
    else:
        news_list = util.get_news_feed_by_location(location, persist=False)
    return json.dumps([obj.to_dict() for obj in news_list])


@app.route('/keywordsbygeo/<string:location>/<int:limit>')
def get_key_words_by_geo(location, limit):
    news_list = util.get_news_feed_by_location(location)
    key_words = util.get_most_used_words_by_location(news_list, limit)
    return json.dumps(key_words)


@app.route('/countriesbygeo/<string:location>/<int:limit>')
def get_countries_by_geo(location, limit):
    news_list = util.get_news_feed_by_location(location, persist=False)
    countries = util.get_subjects_from_news_by_geo(news_list, constants.SPACY_GPE, limit)
    return json.dumps(countries)


@app.route('/sourcesbygeo/<string:location>/<int:limit>')
def get_sources_by_geo(location, limit):
    news_list = util.get_news_feed_by_location(location, persist=False)
    sources = util.get_sources_by_geo(news_list, limit)
    return json.dumps(sources)
