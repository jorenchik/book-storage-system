# TODO: add command name for menu (in their classes)


class Command:
    controller_method_name: str
    name: str

    def execute(self):
        pass


class IndexBooksCommand(Command):
    controller_method_name: str = "index"
    name = "List"

    def __init__(self, book_controller, inventory, view):
        self.book_controller = book_controller
        self.inventory = inventory
        self.inventory.load_json_from_storage()
        self.books = self.inventory.books
        self.view = view

    def execute(self):
        getattr(self.book_controller,
                self.controller_method_name)(self.inventory, self.view)


class CreateBookCommand(Command):
    controller_method_name: str = "create_book"
    name = "Create"

    def __init__(self, book_controller, inventory):
        self.book_controller = book_controller
        self.inventory = inventory
        self.inventory.load_json_from_storage()

    def execute(self):
        getattr(self.book_controller, self.controller_method_name)()


class DeleteBookCommand(Command):
    controller_method_name: str = "delete_option"
    name = "Delete"

    def __init__(self, controller, inventory):
        self.controller = controller
        self.inventory = inventory

    def execute(self):
        getattr(self.controller, self.controller_method_name)()
