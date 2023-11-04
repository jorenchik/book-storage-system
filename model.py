class Book:
    isbn: str
    title: str
    author: str
    price: float
    quantity_in_stock: int

    def __init__(self, isbn, title, author, price, quantity_in_stock):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __dict__(self):
        return {"ISBN": self.isbn,
                "title": self.title,
                "author": self.author,
                "price": self.price,
                "quantity_in_stock": self.quantity_in_stock, }
