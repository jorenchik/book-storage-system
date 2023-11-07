from .model import Book
from pathlib import Path
from json import loads


class Inventory:
    books: list[Book]
    JSON_STORAGE_FILENAME = "books.json"

    def __init__(self):
        self.books: list[Book] = []

    def create_books_from_dict(self, book_data_dict) -> None:
        for book_data in book_data_dict:
            book = Book(*book_data.values())
            self.books.append(book)

    def create_books_from_list(self, book_data_list) -> None:
        for book_data in book_data_list:
            if not self.check_book_creation_data(book_data):
                raise TypeError(Book.ATTRIBUTE_LENGTH_ERROR)
            book = Book(*book_data)
            self.books.append(book)

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
        self.create_books_from_dict(books_object)

    def find_one_book(self, key: str, attributes: list[str]) -> Book:
        results = Book.search_by_attributes(key, self.books, attributes)
        count = len(results)
        if count < 1:
            raise ValueError("Book was not found")
        if count > 1:
            raise ValueError(f"More than one book is found: {count}")
        return results[0]

    def delete(self, key: str) -> None:
        book_to_remove = self.find_one_book(key, ["isbn"])
        self.books.remove(book_to_remove)

    def check_unique_isbn(self, isbn: str) -> bool:
        if not isinstance(isbn, str):
            raise TypeError("ISBN should be a string")
        return isbn not in [book.isbn for book in self.books]

    def check_book_creation_data(self, book_data: list[str]) -> bool:
        return len(book_data) == len(Book.__slots__)

    def update(self, isbn: str, updated_book: Book) -> None:
        search_isbn = isbn
        to_update_book = self.find_one_book(search_isbn, ["isbn"])
        self.books.remove(to_update_book)
        self.books.append(updated_book)
