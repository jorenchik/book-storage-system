from book_inventory.controller import BookController
from book_inventory.commands import IndexBooksCommand, CreateBookCommand, DeleteBookCommand
from book_inventory.view import BookViewCLI


class Menu:
    menu_options: dict
    book_controller: BookController

    def __init__(self):
        self.menu_options = {
            "0": {},
            "1": CreateBookCommand(),
            "2": {},
            "3": {},
            "4": IndexBooksCommand(),
            "5": DeleteBookCommand(),
            "?": {},
        }

    def execute_option(self, option):
        if option in self.menu_options:
            self.menu_options.get(option).execute()
        else:
            raise (ValueError(f"Option '{option}' does not exist"))

    def menu_loop(self):
        while True:
            choice = input("> ")
            option = self.menu_options.get(choice)
            if option:
                self.execute_option(choice)

    def menu_option(self):
        # TODO: choose show behaviour
        self.print_menu_cli(self.menu_options)

    def print_menu_cli(self):
        for key, val in self.menu_options.items():
            print(key, val["name"], sep=": ")


# TODO: make commands for each option
# self.menu_options = {
#     "0": {
#         "name": "Exit",
#         "command": self.book_controller.exit
#     },
#     "1": {
#         "name": "Add book",
#         "command": self.book_controller.create_book
#     },
#     "2": {
#         "name": "Search a book",
#         "command": self.book_controller.search_book_by_all_slots
#     },
#     "3": {
#         "name": "Search a book (ISBN)",
#         "command": self.book_controller.search_book_by_isbn
#     },
#     "4": {
#         "name": "List books",
#         "command": self.book_controller.index,
#         "args":
#         [self.book_controller.inventory, self.book_controller.view]
#     },
#     "5": {
#         "name": "Delete book",
#         "command": self.book_controller.delete_book_by_isbn
#     },
#     "?": {
#         "name": "Help",
#         "command": self.print_menu_cli
#     },
# }
