class Book:
    isbn: str
    title: str
    author: str
    price: float
    quantity_in_stock: int

    LENGTH_ERROR = "{ATTR_NAME} should contain between {MIN_LENGTH}-{MAX_LENGTH} symbols"
    REQUIRED_ERROR = "{ATTR_NAME} is required"

    __slots__ = ["isbn", "title", "author", "price", "quantity_in_stock"]

    def validate_isbn(self) -> bool:
        return match(r'^(?=(?:\D*\d){10}(?:(?:\D*\d){3})?$)[\d-]+$', book.isbn)

    def validate_length(self, attribute_name, min, max) -> bool:
        length = len(getattr(self, attribute_name))
        if not (length >= min and length <= max):
            raise ValueError(
                f"{attribute_name} should contain between 1-50 symbols")

    def __init__(self, isbn, title, author, price, quantity_in_stock):
        self.isbn = str(isbn)
        self.title = title
        self.author = author
        self.price = price
        self.quantity_in_stock = quantity_in_stock
