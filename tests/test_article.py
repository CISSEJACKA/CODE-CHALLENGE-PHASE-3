import pytest
from lib.author import Author
from lib.article import Article
from lib.magazine import Magazine

@pytest.fixture
def setup_article():
    author = Author("John Doe")
    magazine = Magazine("Tech Magazine", "Technology")
    return Article(author, magazine, "Python Basics")

def test_article_initialization(setup_article):
    article = setup_article
    assert article.author.name == "John Doe"
    assert article.magazine.name == "Tech Magazine"
    assert article.title == "Python Basics"

def test_article_author(setup_article):
    article = setup_article
    new_author = Author("Jane Smith")
    article.author = new_author
    assert article.author == new_author

def test_article_magazine(setup_article):
    article = setup_article
    new_magazine = Magazine("Science Journal", "Science")
    article.magazine = new_magazine
    assert article.magazine == new_magazine

# Additional tests can be added as needed

