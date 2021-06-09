from flask import Flask
import util
import json
from model.News import db


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/database.db"
db.init_app(app)


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/newsbygeo/<string:location>')
def get_news_by_geo(location):
    news_list = util.get_news_feed_by_location(location, persist=False)
    return json.dumps([obj.to_dict() for obj in news_list])


@app.route('/keywordsbygeo/<string:location>/<int:limit>')
def get_key_words_by_geo(location, limit):
    news_list = util.get_news_feed_by_location(location)
    key_words = util.get_most_used_words_by_location(news_list, limit)
    return json.dumps(key_words)

