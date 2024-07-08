import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

@pytest.fixture
def setup_author():
    return Author("John Doe")

def test_author_initialization(setup_author):
    assert setup_author.name == "John Doe"

def test_author_articles(setup_author):
    author = setup_author
    article1 = Article(author, Magazine("Tech Magazine", "Technology"), "Python Basics")
    article2 = Article(author, Magazine("Science Journal", "Science"), "Space Exploration")

    assert len(author.articles()) == 2
    assert article1 in author.articles()
    assert article2 in author.articles()

def test_author_magazines(setup_author):
    author = setup_author
    article1 = Article(author, Magazine("Tech Magazine", "Technology"), "Python Basics")
    article2 = Article(author, Magazine("Science Journal", "Science"), "Space Exploration")

    magazines = author.magazines()
    assert len(magazines) == 2
    assert Magazine("Tech Magazine", "Technology") in magazines
    assert Magazine("Science Journal", "Science") in magazines

def test_author_add_article(setup_author):
    author = setup_author
    magazine = Magazine("Tech Magazine", "Technology")
    article = author.add_article(magazine, "Advanced Python")

    assert isinstance(article, Article)
    assert article.author == author
    assert article.magazine == magazine
    assert article.title == "Advanced Python"

def test_author_topic_areas(setup_author):
    author = setup_author
    article1 = Article(author, Magazine("Tech Magazine", "Technology"), "Python Basics")
    article2 = Article(author, Magazine("Science Journal", "Science"), "Space Exploration")

    assert author.topic_areas() == {"Technology", "Science"}

# Additional tests can be added as needed
