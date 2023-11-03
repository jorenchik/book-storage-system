from typing import Dict
from copy import deepcopy

book: Dict = {"ISBN": 12435324242432,
              "title": "Pride and prejudice",
              "author": "John Doe",
              "price": 12.2,
              "quantity_in_stock": 5
              }


def add_book_option():
    pass


def search_book_option():
    pass


def search_book_by_arg_option():
    pass


def list_books_option():
    pass


def delete_book_option():
    pass


if __name__ == "__main__":

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
        print(f"Book #{i}:")
        for key, val in book.items():
            print(key, val, sep=": ")
