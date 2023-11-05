from typing import Dict
from controller import BookController


class Menu:
    menu_options: Dict
    book_controller: BookController

    def __init__(self):
        self.book_controller = BookController()
        self.menu_options = {
            "Exit": self.book_controller.exit_option,
            "Add book": self.book_controller.add_book_option,
            "Search a book": self.book_controller.search_book_by_arg_option,
            "Search a book (ISBN)":
            self.book_controller.search_book_isbn_option,
            "List books": self.book_controller.list_books_option,
            "Delete book": self.book_controller.delete_book_option,
        }

    def menu_loop(self):
        while True:
            self.print_menu_cli(self.menu_options)
            option_index = int(input(">"))
            list(self.menu_options.values())[option_index]()

    def menu_option(self, menu_options):
        # TODO: choose show behaviour
        self.print_menu_cli(self.menu_options)

    def print_menu_cli(self, menu_options):
        for i, val in enumerate(menu_options):
            print(i, val, sep=": ")
