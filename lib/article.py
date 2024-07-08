class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        self.author._articles.append(self)
        self.magazine._articles.append(self)


