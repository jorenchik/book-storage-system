from typing import Dict
from copy import deepcopy
from model import Book
from view import create_book_from_input


book: Dict = {"ISBN": 12435324242432,
              "title": "Pride and prejudice",
              "author": "John Doe",
              "price": 12.2,
              "quantity_in_stock": 5
              }


def add_book_option():
    books.append(create_book_from_input())


def search_book_option():
    pass


def search_book_by_arg_option():
    pass


def list_books_option():
    pass


def delete_book_option():
    pass


if __name__ == "__main__":
    book = Book(12435324242432, "Pride and prejudice", "John Doe", 12.2, 5)
    books = [book]

    menu_options = {'Add book': add_book_option,
                    'Search a book': search_book_by_arg_option,
                    'Search a book (ISBN)': search_book_option,
                    'List books': list_books_option,
                    'Delete book': delete_book_option
                    }

    for i, val in enumerate(menu_options):
        print(i, val, sep=": ")

for i, book in enumerate(books):
    for i, val in book.__dict__().items():
        print(i, val, sep=": ")
