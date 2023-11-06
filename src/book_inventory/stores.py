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
            if (len(book_data) != len(Book.__slots__)):
                raise TypeError(
                    "Provided list(-/s) element count doesn't match __slots__ element count"
                )
            book = Book(*book_data)
            self.books.append(book)

    def get_file_contents(self, filename: str) -> str:
        book_path = Path(filename)
        with open(book_path) as f:
            file_contents = f.read()
        return file_contents

    def load_json_from_storage(self, filename=JSON_STORAGE_FILENAME) -> None:
        json: str = self.get_file_contents(filename)
        json_object = loads(json)
        books_object = json_object['books']
        self.create_books_from_dict(books_object)
