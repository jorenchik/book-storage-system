from view import print_books, create_book_from_input
from model import Book
from typing import List
from json import load
from pathlib import Path
import sys


def add_book_option():
    book = create_book_from_input()
    books.append(book)


def validate_book(isbn, title, author, price, quantity_in_stock):
    pass


def create_book(isbn, title, author, price, quantity_in_stock):
    # TODO: Validation logic
    return Book(isbn, title, author, price, quantity_in_stock)


def search_book_option():
    pass


def search_book_by_arg_option():
    pass


def list_books_option():
    print_books(books)


def delete_book_option():
    pass


def menu_option(menu_options):
    # TODO: choose show behaviour
    print_menu_cli(menu_options)


def exit_option():
    # Save?
    sys.exit(0)
    return


def load_json_from_storage() -> List[Book]:
    book_path = Path('books.json')
    with open(book_path,) as f:
        json_object = load(f)
        book_dicts = json_object['books']

    books = []
    for book_dict in book_dicts:
        book = create_book(book_dict["isbn"],
                           book_dict["title"],
                           book_dict["author"],
                           book_dict["price"],
                           book_dict["quantity_in_stock"])
        books.append(book)

    return books


def print_menu_cli(menu_options):
    for i, val in enumerate(menu_options):
        print(i, val, sep=": ")


def main_loop():
    while True:
        print_menu_cli(menu_options)
        option_index = int(input(">"))
        list(menu_options.values())[option_index]()


books = load_json_from_storage()

menu_options = {'Exit': exit_option,
                'Add book': add_book_option,
                'Search a book': search_book_by_arg_option,
                'Search a book (ISBN)': search_book_option,
                'List books': list_books_option,
                'Delete book': delete_book_option}
