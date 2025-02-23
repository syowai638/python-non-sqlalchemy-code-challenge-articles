#!/usr/bin/env python3
import ipdb

from article import Article
from author import Author
from magazine import Magazine

if __name__ == '__main__':
    print("HELLO! :) Let's debug! 🚀")

    # Create instances to test
    author_1 = Author("Carry Bradshaw")
    magazine_1 = Magazine("Vogue", "Fashion")
    magazine_2 = Magazine("AD", "Architecture")

    article_1 = Article(author_1, magazine_1, "How to wear a tutu with style")
    article_2 = Article(author_1, magazine_1, "Dating life in NYC")
    article_3 = Article(author_1, magazine_2, "2023 Eccentric Design Trends")

    print("Articles by Carry Bradshaw:", author_1.articles())
    print("Magazines contributed to by Carry Bradshaw:", author_1.magazines())
    print("Topics Carry Bradshaw writes about:", author_1.topic_areas())

    print("Articles in Vogue:", magazine_1.article_titles())
    print("Contributors in Vogue:", magazine_1.contributors())

    # Start debugging
    ipdb.set_trace()
