from typing import Dict
from model import Book
from view import create_book_from_input
from json import load
from pathlib import Path


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


def print_books():
    for i, book in enumerate(books):
        for i, val in book.__dict__().items():
            print(i, val, sep=": ")


if __name__ == "__main__":
    book_path = Path('books.json')
    books = []
    with open(book_path,) as f:
        json_object = load(f)
        book_dicts = json_object['books']

    for book_dict in book_dicts:
        book = Book(book_dict["isbn"],
                    book_dict["title"],
                    book_dict["author"],
                    book_dict["price"],
                    book_dict["quantity_in_stock"])
        books.append(book)

    menu_options = {'Add book': add_book_option,
                    'Search a book': search_book_by_arg_option,
                    'Search a book (ISBN)': search_book_option,
                    'List books': list_books_option,
                    'Delete book': delete_book_option
                    }

    for i, val in enumerate(menu_options):
        print(i, val, sep=": ")

    print_books()
