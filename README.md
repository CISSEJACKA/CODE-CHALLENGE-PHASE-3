# CODE-CHALLENGE-PHASE-3

#About
The project allows you to create instances of Authors, Magazines, and Articles, and establish relationships between them. 

#usage
Example usage
from lib.author import Author
from lib.magazine import Magazine
from lib.article import Article

 Create instances
author1 = Author("John Doe")
magazine1 = Magazine("Tech Review", "Technology")
article1 = Article(author1, magazine1, "Artificial Intelligence in 2025")

Use class methods and instance methods to explore relationships
print(author1.articles())  # List of articles written by author1
print(magazine1.articles())  # List of articles published in magazine1
print(magazine1.contributors())  # List of authors who contributed to magazine1

#Testing
pytest

#License
This project is licensed under the MIT License 

