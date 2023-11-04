class Book:
    isbn: str
    title: str
    author: str
    price: float
    quantity_in_stock: int

    LENGTH_ERROR = "{ATTR_NAME} should contain between {MIN_LENGTH}-{MAX_LENGTH} symbols"
    REQUIRED_ERROR = "{ATTR_NAME} is required"

    __slots__ = ["isbn", "title", "author", "price", "quantity_in_stock"]


    def __init__(self, isbn, title, author, price, quantity_in_stock):
        self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.price = price
        self.quantity_in_stock = quantity_in_stock
