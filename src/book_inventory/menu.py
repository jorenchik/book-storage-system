from book_inventory.controllers import BookController
from book_inventory import commands
from book_inventory.view import BookViewCLI
from book_inventory.models import Inventory
import sys


class Menu:
    menu_options: dict
    book_controller: BookController

    def __init__(self):
        self.book_controller = BookController()
        self.view = BookViewCLI()
        self.inventory = Inventory()

        self.menu_options = {
            "0": ("Exit", self.exit_option),
            "1":
            commands.CreateBookCommand(
                self.book_controller,
                self.inventory,
            ),
            # "2": {},
            # "3": {},
            "4":
            commands.IndexBooksCommand(
                self.book_controller,
                self.inventory,
                self.view,
            ),
            "5":
            commands.DeleteBookCommand(
                self.book_controller,
                self.inventory,
            ),
            "?": ("Help", self.menu_option),
        }

    def execute_option(self, option):
        if option not in self.menu_options:
            raise (ValueError(f"Option '{option}' does not exist"))
        action = self.menu_options.get(option)
        if isinstance(action, commands.Command):
            action.execute()
        else:
            action[1]()

    def menu_loop(self):
        while True:
            choice = input("> ")
            option = self.menu_options.get(choice)
            if option:
                self.execute_option(choice)

    def exit_option(self):
        sys.exit(0)

    def menu_option(self):
        # TODO: choose show behaviour
        self.print_menu_cli()

    def print_menu_cli(self):
        for entry in self.get_menu_entries():
            print(entry)

    def get_menu_entries(self) -> list[str]:
        entries = []
        for key, option in self.menu_options.items():
            entries.append(self.get_option_entry(key, option))
        return entries

    def get_option_entry(self, key, option):
        if isinstance(option, commands.Command):
            name = option.name
        elif isinstance(option, tuple):
            name = self.get_option_name_from_tuple(option)
        else:
            raise TypeError("Invalid option (not tuple or command)")
        return f"{key}: {name}"

    def get_option_name_from_tuple(self, option: tuple) -> str:
        if len(option) != 2:
            raise ValueError("Invalid tuple option")
        return option[0]


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
#     "6": {
#         "name": "Edit Book",
#     },
#     "?": {
#         "name": "Help",
#         "command": self.print_menu_cli
#     },
# }
