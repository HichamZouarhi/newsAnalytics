from flask import Flask
import util
import json


app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/newsbygeo/<string:location>')
def get_news_by_geo(location):
    news_list = util.get_news_feed_by_location(location)
    return json.dumps([ob.__dict__ for ob in news_list])


@app.route('/keywordsbygeo/<string:location>')
def get_key_words_by_geo(location):
    news_list = util.get_news_feed_by_location(location)
    key_words = util.get_most_used_words_by_location(news_list)
    print(key_words)
    return json.dumps(key_words)

