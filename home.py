from flask import Flask

import util

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

@app.route('/newsbygeo/<string:location>')
def get_news_by_geo(location):
    return util.get_news_feed_by_location(location)
