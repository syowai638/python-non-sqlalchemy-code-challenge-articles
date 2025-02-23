from collections import Counter
from collections import OrderedDict

# Defines an Author class to represent an author with a name and a list of articles they've written.
class Author:
    # Initializes an Author instance with a name and an empty list for articles.
    def __init__(self, name):
        # Validates that the name is a non-empty string.
        if not isinstance(name, str) or len(name) <= 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name  # Private attribute to store the author's name.
        self._articles = []  # Private attribute to store a list of articles written by the author.

    # Property decorator to get the author's name.
    @property
    def name(self):
        return self._name

    # Returns the list of articles written by the author.
    def articles(self):
        return self._articles

    # Returns a list of unique magazines where the author has published articles.
    def magazines(self):
        return list(OrderedDict.fromkeys(article.magazine for article in self._articles))

    # Adds an article to the author's list of articles if it doesn't already exist.
    def add_article(self, magazine, title):
        # Validates that the magazine argument is an instance of the Magazine class.
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        # Checks for an existing article with the same title and magazine to prevent duplicates.
        existing_article = next((article for article in self._articles if article.title == title and article.magazine == magazine), None)
        if existing_article is not None:
            return existing_article  # Returns the existing article if found.

        # Creates a new Article instance and adds it to the author's list of articles.
        new_article = Article(self, magazine, title)
        self._articles.append(new_article)
        return new_article  # Returns the newly created article.

    # Returns a list of unique topic areas based on the categories of magazines where the author has published.
    def topic_areas(self):
        return list({magazine.category for magazine in self.magazines()}) if self._articles else None


# Defines a Magazine class to represent a magazine with a name, category, and a list of articles.
class Magazine:
    _instances = {}
    all = []
    
    # Initializes a Magazine instance with a name and a category.
    def __init__(self, name, category):
        # Validates that the name is a string between 2 and 16 characters.
        if not isinstance(name, str) or not (2 <= len(name) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        # Validates that the category is a non-empty string.
        if not isinstance(category, str) or len(category) <= 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name  # Private attribute to store the magazine's name.
        self._category = category  # Private attribute to store the magazine's category.
        self._articles = []  # Private attribute to store a list of articles published in the magazine.
        Magazine.all.append(self)
        Magazine._instances[self] = self._articles

    # Property decorator to get and set the magazine's name with validation.
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not (isinstance(value, str) and 2 <= len(value) <= 16):
            raise ValueError("Name must be a string between 2 and 16 characters")
        self._name = value

    # Property decorator to get and set the magazine's category with validation.
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or value == "":
            raise ValueError("Category must be a non-empty string")
        self._category = value
        
    @classmethod
    def top_publisher(cls):
        if not cls._instances or all(len(articles) == 0 for articles in cls._instances.values()):
            return None  # Return None if there are no magazines with articles

        # Find the magazine with the maximum number of articles
        top_magazine = max(cls._instances, key=lambda m: len(cls._instances[m]), default=None)
        return top_magazine if cls._instances[top_magazine] else None

    # Returns the list of articles published in the magazine.
    def articles(self):
        return self._articles

    # Returns a list of unique authors who have contributed articles to the magazine.
    def contributors(self):
        return list({article.author for article in self._articles})

    # Returns a list of article titles published in the magazine, or None if there are no articles.
    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    # Returns a list of authors who have contributed more than two articles to the magazine, or None if there are none.
    def contributing_authors(self):
        author_counts = Counter(article.author for article in self._articles)
        return [author for author, count in author_counts.items() if count > 2] or None
    
    def add_article(self, article):
        self._articles.append(article)
        Magazine._instances[self] = self._articles  # Update the _instances dictionary

    def remove_article(self, article):
        self._articles.remove(article)
        Magazine._instances[self] = self._articles  # Update the _instances dictionary   
    


# Defines an Article class to represent an article with an author, magazine, and title.
class Article:
    all = []  # Class attribute to keep track of all article instances.

    # Initializes an Article instance with an author, magazine, and title.
    def __init__(self, author, magazine, title):
        # Validates that the author is an instance of the Author class.
        if not isinstance(author, Author):
            raise ValueError("author must be an instance of Author")
        # Validates that the magazine is an instance of the Magazine class.
        if not isinstance(magazine, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        # Validates that the title is a string between 5 and 50 characters.
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters")
        self._author = author  # Private attribute to store the article's author.
        self._magazine = magazine  # Private attribute to store the magazine where the article is published.
        self._title = title  # Private attribute to store the article's title.
        # Adds the article to the author's and magazine's lists of articles.
        self._author._articles.append(self)
        self._magazine._articles.append(self)
        Article.all.append(self)  # Adds the new instance to the class attribute list.

    # Property decorator to get the article's title.
    @property
    def title(self):
        return self._title

    # Property decorator to get and set the article's author with validation.
    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("author must be an instance of Author")
        self._author = value

    # Property decorator to get and set the article's magazine with validation.
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("magazine must be an instance of Magazine")
        self._magazine = value
        