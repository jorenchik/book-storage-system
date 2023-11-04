from typing import Dict
from model import Book


def create_book_from_input() -> Dict:
    isbn: str = input("Enter the ISBN:")
    title: str = input("Enter the TITLE:")
    author: str = input("Enter the AUTHOR:")
    price: float = input("Enter the PRICE:")
    quantity_in_stock: int = input("Enter the QUANTITY:")
    return Book(isbn, title, author, price, quantity_in_stock)


def print_books():
    for i, book in enumerate(books):
        for i, val in book.__dict__().items():
            print(i, val, sep=": ")
