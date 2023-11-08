from book_inventory.models import Book


class BookController:

    def __init__(self, inventory):
        # Initializes the BookController with a given inventory and loads the
        # inventory data from a JSON file.
        self.inventory = inventory
        self.inventory.load_json_from_storage()

    def create(self, *kwargs):
        if "" in kwargs:
            raise TypeError("Every field should be filled")
        book = Book(*kwargs)
        if not self.inventory.check_unique_isbn(book.isbn):
            raise TypeError("This ISBN already exists")
        self.inventory.books.append(book)

    def search_books_by_isbn(self, prompt):
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            ["isbn"])
        return results

    def search_books(self, prompt, attributes):
        results = Book.search_by_attributes(prompt, self.inventory.books,
                                            attributes)
        return results

    def index(self) -> list[Book]:
        # Returns a list of all books in the inventory, with each book's data
        # represented as a list of values corresponding to the book's attributes.
        books_to_print = self.inventory.books
        book_list = []
        for book in books_to_print:
            book_values = []
            for slot in Book.__slots__:
                book_values.append(getattr(book, slot))
            book_list.append(book_values)

        return book_list

    def delete(self, key: str) -> None:
        # Deletes a book from the inventory based on a given key, typically the ISBN.
        self.inventory.delete(key)
