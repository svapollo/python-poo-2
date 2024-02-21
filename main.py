from modelos.book import Book
from modelos.library import Library


def main():

    library = Library()
    twilight_book = Book('twilight', 'Stephenie Meyer', 2005)
    library.add_book(twilight_book)
    flowers_algernon_book = Book('flowers for Algernon', 'Daniel Keyes', 1959)
    library.add_book(flowers_algernon_book)
    two_flowers_algernon_book = Book('Two flowers for Algernon', 'Daniel Keyes', 1959)
    library.add_book(two_flowers_algernon_book)
    print(library.check_available_books_year(1959))


if __name__ == '__main__':
    main()
