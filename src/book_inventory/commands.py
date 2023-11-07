from book_inventory.controller import BookController
from book_inventory.stores import Inventory
from book_inventory.view import BookViewCLI


class IndexBooksCommand:
    controller_method_name: str = "index"

    def __init__(self,
                 book_controller=BookController(),
                 inventory=Inventory(),
                 view=BookViewCLI()):
        self.book_controller = book_controller
        self.inventory = inventory
        self.inventory.load_json_from_storage()
        self.books = self.inventory.books
        self.view = view

    def execute(self):
        getattr(self.book_controller, self.controller_method_name)(self.books,
                                                                   self.view)
