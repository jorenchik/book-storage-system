from typing import Dict
from .model import Book
from tabulate import tabulate


class BookViewCLI:

    def input_book_data(self) -> Dict:
        isbn: str = input("Enter the ISBN:")
        title: str = input("Enter the TITLE:")
        author: str = input("Enter the AUTHOR:")
        price: str = input("Enter the PRICE:")
        quantity_in_stock: str = input("Enter the QUANTITY:")
        return isbn, title, author, price, quantity_in_stock

    def print_books(self, books) -> None:
        table = []
        for i, book in enumerate(books):
            tr = []
            for key in Book.__slots__:
                tr.append(getattr(book, key))
            table.append(tr)

        print(
            tabulate(table,
                     headers=Book.__slots__,
                     tablefmt='psql',
                     showindex=False))
