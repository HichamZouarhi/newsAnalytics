import constants


class News:
    def __init__(self):
        self.title = None
        self.location = None
        self.link = None
        self.publication_date = None
        self.source = None
        self.description = None

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
