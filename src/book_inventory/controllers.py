from book_inventory.models import Book


class BookController:

    def __init__(self, inventory):
        self.inventory = inventory
        self.inventory.load_json_from_storage()

    def create(self) -> None:
        book_data: tuple = self.view.input_book_data()
        book = Book(*book_data)
        self.inventory.books.append(book)

    def search_books_by_isbn(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        self.view.print_books(results)

    def search_books(self) -> None:
        prompt = input("Search:")
        results = Book.search_by_attributes(prompt, self.books, Book.__slots__)
        self.view.print_books(results)

    def index(self) -> list[Book]:
        books_to_print = self.inventory.books
        book_list = []
        for book in books_to_print:
            book_values = []
            for slot in Book.__slots__:
                book_values.append(getattr(book, slot))
            book_list.append(book_values)

        return book_list

    def delete(self, key: str) -> None:
        if not self.model.delete(key):
            raise ValueError("Book not found")
