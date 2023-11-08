from __future__ import annotations
from re import match, sub
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

    def __tuple__(self):
        values = []
        for attr in Book.__slots__:
            values.append(getattr(self, attr))
        return tuple(values)

    def __init__(self, isbn, title, author, price, quantity_in_stock):
        # Initializes a new Book instance with the provided details, performs
        # validations, and formats the ISBN.
        self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.price = price
        self.quantity_in_stock = quantity_in_stock
        if not self.validate_isbn(self.isbn):
            raise TypeError("Wrong ISBN format")
        self.isbn = sub(r'-', '', self.isbn)
        self.validate_length("title", 0, 100)
        self.validate_length("author", 0, 100)
        try:
            float(self.price)
        except ValueError:
            raise TypeError("price should be a number")
        try:
            float(self.quantity_in_stock)
        except ValueError:
            raise TypeError("quantity in stock should be a number")

    @classmethod
    def search_by_attributes(cls,
                             prompt,
                             books,
                             attribute_list,
                             exact=False) -> list:
        # Searches for books in a given list that match the provided prompt in
        # the specified attributes (case insensitive).
        results = []
        for book in books:
            for attr in attribute_list:
                if exact and str(getattr(book,
                                         attr)).lower() == str(prompt).lower():
                    results.append(book)
                    break
                elif not exact and str(getattr(
                        book, attr)).lower().__contains__(str(prompt).lower()):
                    results.append(book)
                    break
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
            raise TypeError(
                f"{attribute_name} should contain between 1-50 symbols")


class Inventory:
    JSON_STORAGE_FILENAME = "books.json"
    books: list[Book]

    def __init__(self):
        self.books: list[Book] = []

    def get_file_contents(self, filename: str) -> str:
        book_path = Path(filename)
        with open(book_path) as f:
            file_contents = f.read()
        return file_contents

    def load_json_from_storage(self, filename=JSON_STORAGE_FILENAME) -> None:
        # Updates a book in the inventory with a new version based on its ISBN.
        json: str = self.get_file_contents(filename)
        json_object = loads(json)
        books_object = json_object['books']
        isbn_encountered = []
        for book_dict in books_object:
            isbn = book_dict["isbn"]
            if isbn not in isbn_encountered:
                self.books.append(Book.create_book_from_dict(book_dict))
            else:
                print(f"Info: duplicate ISBN:{isbn}, skipping")
            isbn_encountered.append(isbn)

    def delete(self, key: str) -> None:
        # Removes a book from the inventory based on a given key.
        book_to_remove = self.find_one_book(key, ["isbn"], exact=True)
        self.books.remove(book_to_remove)

    def find_one_book(self,
                      key: str,
                      attributes: list[str],
                      exact=False) -> Book:
        results = Book.search_by_attributes(key, self.books, attributes, exact)
        count = len(results)
        if count < 1:
            raise ValueError("Book was not found")
        if count > 1:
            raise ValueError(f"More than one book is found: {count}")
        return results[0]

    def check_unique_isbn(self, isbn: str) -> bool:
        if not isinstance(isbn, str):
            raise TypeError("ISBN should be a string")
        return isbn not in [book.isbn for book in self.books]

    def update(self, isbn: str, updated_book: Book) -> None:
        # Updates a book in the inventory with a new version based on its ISBN.
        to_update_book = self.find_one_book(isbn, ["isbn"])
        update_index = self.books.index(to_update_book)
        self.books[update_index] = updated_book

    def add_book_to_inventory(self, book: Book) -> None:
        if not isinstance(book, Book):
            raise TypeError("Object added to the inventory should be a Book")
        self.books.append(book)
