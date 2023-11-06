from .view import BookViewCLI
from .model import Book
from .stores import Inventory
import sys


class BookController:

    def __init__(self):
        self.inventory = Inventory()
        self.view = BookViewCLI()
        self.inventory.load_json_from_storage()

    def add_book_option(self) -> None:
        book_data: tuple = self.view.create_book_from_input()
        book = Book(*book_data)
        self.inventory.books.append(book)

    def search_book_isbn_option(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        self.view.print_books(results)

    def search_book_by_arg_option(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.books, Book.__slots__)
        self.view.print_books(results)

    def list_books_option(self, inventory, view) -> None:
        books_to_print = inventory.books
        view.print_books(books_to_print)

    def delete_book_option(self) -> None:
        pass

    def exit_option(self) -> None:
        sys.exit(0)
