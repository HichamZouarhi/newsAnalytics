from flask_sqlalchemy import SQLAlchemy
import constants

db = SQLAlchemy()


class News(db.Model):
    __tablename__ = 'news'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=False, nullable=False)
    location = db.Column(db.String, unique=False, nullable=False)
    link = db.Column(db.String, unique=False, nullable=False)
    publication_date = db.Column(db.String, unique=False, nullable=False)
    source = db.Column(db.String, unique=False, nullable=False)
    description = db.Column(db.String, unique=False, nullable=False)

    def hydrate(self, item, location):
        self.title = item.find(constants.TITLE_TAG).text
        self.location = location
        self.link = item.find(constants.LINK_TAG).text
        self.publication_date = item.find(constants.PUBLICATION_DATE_TAG).text
        self.source = item.find(constants.SOURCE_TAG).text
        self.description = item.find(constants.DESCRIPTION_TAG).text

    def dump(self):
        print("item ---")
        print("title : " + self.title)
        print("location : " + self.location)
        print("link : " + self.link)
        print("publication date : " + self.publication_date)
        print("source : " + self.source)
        print("description : " + self.description)

    def save(self):
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        news_dict = {"id": self.id,
                     "title": self.title,
                     "location": self.location,
                     "link": self.link,
                     "pubDate": self.publication_date,
                     "source": self.source,
                     "description": self.description}
        return news_dict
