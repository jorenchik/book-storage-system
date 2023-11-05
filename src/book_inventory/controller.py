from view import print_books, create_book_from_input
from .model import Book
from stores import Inventory
import sys


class BookController:

    def __init__(self):
        self.inventory = Inventory()
        self.inventory.load_json_from_storage()

    def add_book_option(self) -> None:
        book_data: tuple = create_book_from_input()
        book = Book(*book_data)
        self.inventory.books.append(book)

    def search_book_isbn_option(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        print_books(results)

    def search_book_by_arg_option(self) -> None:
        pass

    def list_books_option(self) -> None:
        print_books(self.inventory.books)

    def delete_book_option(self) -> None:
        pass

    def exit_option(self) -> None:
        sys.exit(0)
