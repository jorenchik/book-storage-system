from __future__ import annotations
from re import match
from pathlib import Path
from json import loads


class Book:
    isbn: str
    title: str
    author: str
    price: float
    quantity_in_stock: int

    LENGTH_ERROR = "{ATTR_NAME} should contain between {MIN_LENGTH}-{MAX_LENGTH} symbols"
    REQUIRED_ERROR = "{ATTR_NAME} is required"
    ATTRIBUTE_LENGTH_ERROR = "Provided list(-/s) element count doesn't match __slots__ element count"

    __slots__ = ["isbn", "title", "author", "price", "quantity_in_stock"]

    def __init__(self, isbn, title, author, price, quantity_in_stock):
        self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    @classmethod
    def search_by_attributes(cls, prompt, books, attribute_list) -> list:
        results = []
        for book in books:
            for attr in attribute_list:
                if str(getattr(book, attr)).__contains__(str(prompt)):
                    results.append(book)
        return results

    @classmethod
    def create_book_from_dict(cls, book_data_dict) -> Book:
        book = Book(*book_data_dict.values())
        return book

    @classmethod
    def create_book_from_list(cls, book_data_list) -> Book:
        if not cls.check_book_creation_data(book_data_list):
            raise TypeError(Book.ATTRIBUTE_LENGTH_ERROR)
        return Book(*book_data_list)

    @classmethod
    def check_book_creation_data(cls, book_data: list[str]) -> bool:
        return len(book_data) == len(Book.__slots__)

    def validate_isbn(self, isbn) -> bool:
        return match(r'^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$', isbn)

    def validate_length(self, attribute_name, min, max) -> bool:
        length = len(getattr(self, attribute_name))
        if not (length >= min and length <= max):
            raise ValueError(
                f"{attribute_name} should contain between 1-50 symbols")


class Inventory:
    JSON_STORAGE_FILENAME = "books.json"
    books: list[Book]

    def __init__(self):
        self.books: list[Book] = []

    # TODO: test
    def get_file_contents(self, filename: str) -> str:
        book_path = Path(filename)
        with open(book_path) as f:
            file_contents = f.read()
        return file_contents

    # TODO: test
    def load_json_from_storage(self, filename=JSON_STORAGE_FILENAME) -> None:
        json: str = self.get_file_contents(filename)
        json_object = loads(json)
        books_object = json_object['books']
        for book_dict in books_object:
            self.books.append(Book.create_book_from_dict(book_dict))

    def delete(self, key: str) -> None:
        book_to_remove = self.find_one_book(key, ["isbn"])
        self.books.remove(book_to_remove)

    def find_one_book(self, key: str, attributes: list[str]) -> Book:
        results = Book.search_by_attributes(key, self.books, attributes)
        count = len(results)
        if count < 1:
            print(count)
            raise ValueError("Book was not found")
        if count > 1:
            raise ValueError(f"More than one book is found: {count}")
        return results[0]

    def check_unique_isbn(self, isbn: str) -> bool:
        if not isinstance(isbn, str):
            raise TypeError("ISBN should be a string")
        return isbn not in [book.isbn for book in self.books]

    def update(self, isbn: str, updated_book: Book) -> None:
        to_update_book = self.find_one_book(isbn, ["isbn"])
        update_index = self.books.index(to_update_book)
        self.books[update_index] = updated_book

    def add_book_to_inventory(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Object added to the inventory should be a Book")
        self.books.append(book)
