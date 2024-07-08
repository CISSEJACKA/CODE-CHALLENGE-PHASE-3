import pytest
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

@pytest.fixture
def setup_magazine():
    return Magazine("Tech Magazine", "Technology")

def test_magazine_initialization(setup_magazine):
    magazine = setup_magazine
    assert magazine.name == "Tech Magazine"
    assert magazine.topic == "Technology"

def test_magazine_articles(setup_magazine):
    magazine = setup_magazine
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    article1 = Article(author1, magazine, "Python Basics")
    article2 = Article(author2, magazine, "Advanced Python")

    assert len(magazine.articles()) == 2

def test_magazine_contributors(setup_magazine):
    magazine = setup_magazine
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    article1 = Article(author1, magazine, "Python Basics")
    article2 = Article(author2, magazine, "Advanced Python")

    contributors = magazine.contributors()
    assert author1 in contributors
    assert author2 in contributors

def test_magazine_article_titles(setup_magazine):
    magazine = setup_magazine
    article1 = Article(Author("John Doe"), magazine, "Python Basics")
    article2 = Article(Author("Jane Smith"), magazine, "Advanced Python")

    titles = magazine.article_titles()
    assert "Python Basics" in titles
    assert "Advanced Python" in titles

def test_magazine_contributing_authors(setup_magazine):
    magazine = setup_magazine
    author1 = Author("John Doe")
    author2 = Author("Jane Smith")
    article1 = Article(author1, magazine, "Python Basics")
    article2 = Article(author2, magazine, "Advanced Python")

    assert set(magazine.contributing_authors()) == {author1, author2}



