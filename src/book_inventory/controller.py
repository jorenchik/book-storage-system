from book_inventory.view import BookViewCLI
from book_inventory.model import Book
from book_inventory.stores import Inventory


class BookController:

    def __init__(self):
        self.inventory = Inventory()
        self.view = BookViewCLI()
        self.inventory.load_json_from_storage()
        self.model = Inventory()

    def create(self) -> None:
        book_data: tuple = self.view.input_book_data()
        book = Book(*book_data)
        self.inventory.books.append(book)

    def search_books_by_isbn(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        self.view.print_books(results)

    def search_books(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.books, Book.__slots__)
        self.view.print_books(results)

    def index(self, inventory, view) -> None:
        books_to_print = inventory.books
        view.print_books(books_to_print)

    def delete(self, key: str) -> None:
        if not self.model.delete(key):
            raise ValueError("Book not found")
