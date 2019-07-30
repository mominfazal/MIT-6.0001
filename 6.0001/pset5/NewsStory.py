class NewsStory():
    def __init__(self, guid, title, description, link, pubdate):
        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate

    def get_guid(self):
        """ get guid """
        return self.guid

    def get_title(self):
        """ get title """
        return self.title

    def get_description(self):
        """ get description """
        return self.description

    def get_link(self):
        """ get link """
        return self.link

    def get_pubdate(self):
        """ get pubdate """
        return self.pubdate
