from typing import Dict
from copy import deepcopy

book: Dict = {"title": "Pride and prejudice",
              "author": "John Doe",
              "ISBN": 12435324242432,
              "price": 12.2,
              "quantity_in_stock": 5
              }

if __name__ == "__main__":
    books = [book, deepcopy(book)]

    for i, book in enumerate(books):
        print(f"Book #{i}:")
        for key, val in book.items():
            print(key, val, sep=": ")
