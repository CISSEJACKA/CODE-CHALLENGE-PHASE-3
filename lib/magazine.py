class Magazine:
    def __init__(self, name, topic):
        self.name = name
        self.topic = topic
        self._articles = []

    def articles(self):
        return self._articles

    def contributors(self):
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        return [article.title for article in self._articles]

    def contributing_authors(self):
        return list(set(article.author for article in self._articles))

    def __eq__(self, other):
        if isinstance(other, Magazine):
            return self.name == other.name and self.topic == other.topic
        return False

    def __hash__(self):
        return hash((self.name, self.topic))



