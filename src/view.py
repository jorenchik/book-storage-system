from typing import Dict
from model import Book
from tabulate import tabulate


def create_book_from_input() -> Dict:
    isbn: str = input("Enter the ISBN:")
    title: str = input("Enter the TITLE:")
    author: str = input("Enter the AUTHOR:")
    price: str = input("Enter the PRICE:")
    quantity_in_stock: str = input("Enter the QUANTITY:")
    return {
        "isbn": isbn,
        "title": title,
        "author": author,
        "price": price,
        "quantity_in_stock": quantity_in_stock,
    }


def print_books(books):
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
