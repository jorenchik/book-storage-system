from book_inventory.view import BookViewCLI
from book_inventory.model import Book
from book_inventory.stores import Inventory
import sys


class BookController:

    def __init__(self):
        self.inventory = Inventory()
        self.view = BookViewCLI()
        self.inventory.load_json_from_storage()

    def create_book(self) -> None:
        book_data: tuple = self.view.create_book_from_input()
        book = Book(*book_data)
        self.inventory.books.append(book)

    def search_book_by_isbn(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        self.view.print_books(results)

    def search_book_by_all_slots(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.books, Book.__slots__)
        self.view.print_books(results)

    def index(self, inventory, view) -> None:
        books_to_print = inventory.books
        view.print_books(books_to_print)

    def delete_book_by_isbn(self) -> None:
        pass

    def exit(self) -> None:
        sys.exit(0)
