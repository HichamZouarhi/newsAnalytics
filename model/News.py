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
        self.title = item.get(constants.TITLE_TAG)
        self.location = location
        self.link = item.get(constants.LINK_TAG)
        self.publication_date = item.get(constants.PUBLICATION_DATE_TAG)
        self.source = item.get(constants.SOURCE_TAG)
        self.description = item.get(constants.DESCRIPTION_TAG)