class Book:

    def __init__(self, title, author, year_publication):
        self.title = title
        self.author = author
        self.year_publication = year_publication

    def __str__(self):
        return f"Title: {self.title}| Author: {self.author}| \
Year of Publication: {self.year_publication}"

    def __repr__(self):
        return self.__str__()

