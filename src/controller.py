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

    def add_book_option(self) -> None:
        book_values: dict = create_book_from_input()
        book = Book(
            book_values.get("isbn"),
            book_values.get("title"),
            book_values.get("author"),
            book_values.get("price"),
            book_values.get("quantity_in_stock"),
        )
        self.books.append(book)

    def search_book_isbn_option(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.books, ["isbn"])
        print_books(results)

    def search_book_by_arg_option(self) -> None:
        pass

    def list_books_option(self) -> None:
        print_books(self.books)

    def delete_book_option(self) -> None:
        pass

    def exit_option(self) -> None:
        sys.exit(0)

    def load_json_from_storage(self) -> List[Book]:
        book_path = Path('books.json')
        with open(book_path, ) as f:
            json_object = load(f)
            book_dicts = json_object['books']
        results = []

        for book_dict in book_dicts:
            book = Book(book_dict["isbn"], book_dict["title"],
                        book_dict["author"], book_dict["price"],
                        book_dict["quantity_in_stock"])
            results.append(book)
        return results
