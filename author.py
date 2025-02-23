def __init__(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string.")
        self._articles = []

    @property
    def name(self):
        return self._name  # Name is immutable

    def articles(self):
        return self._articles

    def magazines(self):
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        if isinstance(magazine, Magazine) and isinstance(title, str) and 5 <= len(title) <= 50:
            article = Article(self, magazine, title)
            self._articles.append(article)
            magazine._articles.append(article)
            return article
        else:
            raise ValueError("Invalid magazine instance or title length.")

    def topic_areas(self):
        topics = list(set(mag.category for mag in self.magazines()))
        return topics if topics else None  # Return None if no articles