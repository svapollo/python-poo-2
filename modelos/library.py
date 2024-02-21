class Library:
    def __init__(self):
        self.books = []
        self._available = True

    def __repr__(self):
        return f"Library with {len(self.books)} books"

    def add_book(self, book):
        self.books.append(book)

    def lend_book(self):
        if self.is_available():
            self._available = False
            print('You borrowed this book')
        else:
            print('This book is not available, sorry')

    def is_available(self):
        print(f"Book available: {self._available}")
        return self._available

    def check_available_books_year(self, year_publication):
        matching_books = [book for book in self.books if book.year_publication == year_publication]
        return matching_books
