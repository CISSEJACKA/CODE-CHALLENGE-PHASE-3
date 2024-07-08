from lib.article import Article

class Author:
    def __init__(self, name):
        self.name = name
        self._articles = []

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    def topic_areas(self):
        return set(article.magazine.topic for article in self._articles)

    def __eq__(self, other):
        if isinstance(other, Author):
            return self.name == other.name
        return False

    def __hash__(self):
        return hash(self.name)





