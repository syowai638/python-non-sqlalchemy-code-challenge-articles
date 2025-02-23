all = []  # Keep track of all articles

    def __init__(self, author, magazine, title):
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author.")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine.")
        if not isinstance(title, str) or not (5 <= len(title) <= 50):
            raise ValueError("Title must be a string between 5 and 50 characters.")

        self.author = author
        self.magazine = magazine
        self._title = title  # Immutable title

        Article.all.append(self)  # Track all instances

    @property
    def title(self):
        return self._title  # Enforce immutability