from view import print_books, create_book_from_input
from model import Book
from typing import List, Dict
from json import load
from pathlib import Path
import sys


class BookController:

    books: List[Book]

    def __init__(self):
        self.books = self.load_json_from_storage()

    def add_book_option(self):
        book = create_book_from_input()
        self.books.append(book)

    def create_book(self, isbn, title, author, price, quantity_in_stock) -> Book:
        # TODO: validatio
        book = Book(isbn, title, author, price, quantity_in_stock)
        return book

    def search_book_isbn_option(self):
        prompt = input("Search:")
        print(Book.search_by_attributes(prompt, self.books, ["isbn"]))

    def search_book_by_arg_option(self):
        # loop over books and match by
        pass

    def list_books_option(self):
        print_books(self.books)

    def delete_book_option(self):
        # TODO: call search
        # TODO: delete book
        pass

    def exit_option(self):
        # TODO: Save prompt and save call?
        sys.exit(0)

    def load_json_from_storage(self) -> List[Book]:
        book_path = Path('books.json')
        with open(book_path,) as f:
            json_object = load(f)
            book_dicts = json_object['books']
        results = []
        for book_dict in book_dicts:
            book = self.create_book(book_dict["isbn"],
                                    book_dict["title"],
                                    book_dict["author"],
                                    book_dict["price"],
                                    book_dict["quantity_in_stock"])
            results.append(book)

        return results
