from view import *
from model import Book
from typing import List


def add_book_option(books: List[Book]):
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
    print_books()


def delete_book_option():
    pass
