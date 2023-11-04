from view import create_book_from_input
from model import Book
from typing import List


def add_book_option(books: List[Book]):
    books.append(create_book_from_input())


def search_book_option():
    pass


def search_book_by_arg_option():
    pass


def list_books_option():
    pass


def delete_book_option():
    pass
